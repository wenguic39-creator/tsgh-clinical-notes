# TSGH Clinical Notes for ChatGPT and Codex

TSGH-aligned clinical-documentation workflows packaged as an instruction-only Agent Plugins 1.0 plugin for ChatGPT Chat/Work on the web and desktop, and Codex. It includes six skills: a clinical-note router, Admission, Progress, Weekly, Discharge, and Operation Notes. The router also provides the Chinese B/P/Sc/Sp/E/P/D holistic-care assessment.

![TSGH Clinical Notes cover](plugins/tsgh-clinical-notes/assets/logo.png)

## ChatGPT on the web

For your own account, use Plugin Creator to save or update the plugin from the packaged ZIP. Open its returned plugin link, install it, start a new Work chat, and select `@TSGH Clinical Notes`.

For a ChatGPT workspace, an admin can import this GitHub marketplace from **Admin > Plugins > Add > Import marketplace**:

- Source: `https://github.com/wenguic39-creator/tsgh-clinical-notes`
- Path: leave empty (the marketplace is at the repository root)
- Branch: `main`, or the specific branch you want to test

Members install the imported plugin from their workspace's Plugins directory, then invoke it in a new chat with an `@` mention. Creation/import availability depends on workspace permissions. A local Codex marketplace installation and a ChatGPT account installation are separate; cloning this repository alone does not install it on the web.

This skills-only package needs no MCP server, hosting, API key, or desktop hooks. Public universal-directory publication is a separate review process; this repository is not itself a public directory listing.

## Codex installation

Clone or download this repository, then run:

```powershell
codex plugin marketplace add "<full path to this repository>"
codex plugin add tsgh-clinical-notes@tsgh-team
```

Open a new Codex task after installation.

## Build an installable ZIP

From this repository, with Python 3.10 or later:

```powershell
python scripts/package_plugin.py
```

This validates the portable and compatibility manifests, all six skills, assets, and relative references, then writes `dist/tsgh-clinical-notes-0.1.2.zip`. It includes the hidden `.codex-plugin/plugin.json`. Use `--check` to validate without exporting. The script checks package structure and content; host installation and drafting still need a separate smoke test.

GitHub Actions also builds the ZIP on pull requests, pushes to `main`, and manual runs. Download the `tsgh-clinical-notes-plugin` artifact and unpack the Actions artifact once to get the plugin ZIP inside. GitHub's **Download ZIP** is a repository snapshot, not this single-plugin upload package.

## Package layout

```text
.agents/plugins/marketplace.json       # Existing tsgh-team marketplace
plugins/tsgh-clinical-notes/
  plugin.json                         # Portable manifest; canonical metadata
  .codex-plugin/plugin.json           # Synchronized compatibility manifest
  skills/                             # Six skills plus bundled references
  assets/                             # Existing logos
scripts/package_plugin.py             # Validation and export
```

## Official documentation

- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [ChatGPT plugin installation](https://learn.chatgpt.com/docs/plugins)
- [GitHub workspace import and sync](https://learn.chatgpt.com/docs/enterprise/plugin-management)

## Clinical safety

- Use only authorized, minimum-necessary, and appropriately de-identified clinical information.
- Do not place patient names, national identifiers, medical-record numbers, or other identifying information in public tasks.
- Every generated note is a draft and requires review by a qualified clinician before entry into the medical record.
- Web Work can process supplied records in the cloud. Use only information your institutional policy permits for the selected host. The plugin does not send records to an additional clinical service, web search, or connector; it cannot make the host's processing on-device-only.
- The cover includes Tri-Service General Hospital identity elements. Confirm institutional brand authorization before redistribution or reuse outside the intended setting.

完整中文說明請見 [安裝說明.md](安裝說明.md)。
