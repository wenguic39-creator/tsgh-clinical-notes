#!/usr/bin/env python3
"""Validate and export the skills-only plugin; uses Python 3.10+ standard library."""

import argparse
import json
from pathlib import Path
import re
import zipfile


REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins" / "tsgh-clinical-notes"
SKILLS = {
    "clinical-note", "admission-summary", "progress-note", "weekly-summary",
    "discharge-summary", "operation-note",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root=PLUGIN):
    root = root.resolve()
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    legacy = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    require(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "Use Agent Plugins 1.0 schema")
    require(manifest.get("name") == root.name == "tsgh-clinical-notes", "Plugin identity must match its directory")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")), "Use a numeric release version")
    require(not {"skills", "mcpServers", "apps", "interface"} & manifest.keys(), "Portable components must use fixed paths or OpenAI extensions")
    for key in ("name", "version", "description", "author"):
        require(manifest.get(key) == legacy.get(key), f"Compatibility manifest differs: {key}")
    interface = manifest["extensions"]["com.openai"]["interface"]
    require(interface == legacy.get("interface"), "OpenAI presentation metadata must match")
    require(0 < len(interface["shortDescription"]) <= 30, "Subtitle must contain 1-30 characters")
    prompts = interface["defaultPrompt"]
    require(isinstance(prompts, str) or (isinstance(prompts, list) and 1 <= len(prompts) <= 3 and all(isinstance(p, str) and p for p in prompts)), "Use one prompt or up to three prompts")
    require(legacy.get("skills") in ("./skills", "./skills/"), "Compatibility manifest must discover all skills")
    require({p.name for p in (root / "skills").iterdir() if p.is_dir()} == SKILLS, "Expected all six skills")
    # This export is deliberately skills-only, so it can run without a desktop server.
    for config in (manifest["extensions"]["com.openai"], legacy):
        require(not any(config.get(k) for k in ("apps", "mcpServers", "hooks")), "Do not add service or hook dependencies to this skills-only package")
    require(not any((root / p).exists() for p in ("mcp.json", ".mcp.json", ".app.json", "hooks")), "Unexpected service or hook dependency")
    for key in ("logo", "composerIcon"):
        relative = interface[key]
        asset = (root / relative).resolve()
        require(relative.startswith("./assets/") and asset.is_relative_to(root), "Assets must stay inside the plugin")
        require(asset.is_file() and 0 < asset.stat().st_size <= 5 * 1024 * 1024, f"Missing or oversized asset: {relative}")
    for skill in sorted(SKILLS):
        source = root / "skills" / skill / "SKILL.md"
        content = source.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        require(front is not None, f"Invalid skill frontmatter: {skill}")
        require(f"name: {skill}" in front.group(1).splitlines(), f"Skill name differs: {skill}")
        require(re.search(r"^description: \S", front.group(1), re.M), f"Missing skill description: {skill}")
        require("current authorized ChatGPT or Codex session" in content, f"Missing host-aware data rule: {skill}")
        # Check relative Markdown references and quoted sibling skill routes.
        links = re.findall(r"\]\(([^)]+)\)", content)
        links += re.findall(r"`(\.\./[^`]+/SKILL\.md)`", content)
        for link in links:
            if "://" in link or link.startswith("#"):
                continue
            target = (source.parent / link.split("#", 1)[0]).resolve()
            require(target.is_relative_to(root) and target.is_file(), f"Broken or escaping reference: {skill}: {link}")
    files = sorted(p for p in root.rglob("*") if p.is_file())
    require(not any(p.is_symlink() for p in root.rglob("*")), "Symlinks cannot be packaged")
    require(not any(p.name.startswith(".env") or p.name in {".git", "node_modules", "__pycache__"} for p in root.rglob("*")), "Unexpected development files")
    return manifest, files


def package(output_dir):
    manifest, files = validate()
    output_dir = output_dir.resolve()
    require(not output_dir.is_relative_to(PLUGIN), "Write the archive outside the plugin directory")
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{manifest['name']}-{manifest['version']}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for source in files:
            entry = zipfile.ZipInfo(source.relative_to(PLUGIN.parent).as_posix(), (2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, source.read_bytes())
    # Verify every archived byte, including hidden compatibility files.
    with zipfile.ZipFile(archive) as bundle:
        require(bundle.testzip() is None and len(bundle.namelist()) == len(files), "Archive integrity check failed")
        for source in files:
            require(bundle.read(source.relative_to(PLUGIN.parent).as_posix()) == source.read_bytes(), "Archive content differs")
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without creating a ZIP")
    parser.add_argument("--output-dir", type=Path, default=REPO / "dist")
    args = parser.parse_args()
    try:
        if args.check:
            manifest, files = validate()
            print(f"Validated {manifest['name']} {manifest['version']}: {len(SKILLS)} skills, {len(files)} files")
        else:
            print(package(args.output_dir))
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, f"Packaging failed: {error}\n")


if __name__ == "__main__":
    main()
