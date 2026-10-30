# TSGH Clinical Notes maintenance

This plugin is the single authoring source for clinical-note, admission-summary,
progress-note, weekly-summary, discharge-summary, and operation-note.
For this repository, the authoring source is `plugins/tsgh-clinical-notes`.
The root `plugin.json` is canonical; keep the compatibility manifest at
`.codex-plugin/plugin.json` synchronized. Preserve the six independent skills.

- Make requested changes in this source tree. Do not edit installed files under
  `.codex/plugins/cache`, restore archived standalone skills as active copies, or
  create parallel copies under `.codex/skills` or `.agents/skills`.
- Read the affected SKILL.md and preserve existing user-approved clinical behavior
  unless the current request changes it. A source-maintenance change alone must not
  change note structure, clinical content rules, or output modes.
- Keep the six note types as separate skills in this one plugin. Do not merge their
  note formats merely to consolidate maintenance.
- Before an update, save a dated backup outside skill-discovery directories.
  Validate changed skills with the installed skill-creator validator and validate
  the plugin with the installed plugin-creator validator. Test relevant behavior
  when clinical drafting instructions change, using synthetic/de-identified data.
- For repository changes, validate and export with `scripts/package_plugin.py`
  from the repository root. Use the installed skill validator for changed skills;
  use a plugin-creator validator if available, otherwise document the structural
  check and verify the package with the target host.
- For a local installation, resolve its actual marketplace source and use the
  supported local update/reinstall flow. Preserve its marketplace name and
  unrelated configuration; do not assume another user's Windows path.
- For an editable private account plugin, inspect its current release and use a
  guarded account update. For GitHub-managed workspace plugins, update the owning
  repository and sync through workspace administration. Keep ownership and sharing.
- New tasks are the pickup boundary after reinstall. Existing tasks may retain
  earlier skill context; do not claim they have refreshed automatically.
- Local maintenance does not authorize pushing to GitHub, publishing a plugin,
  or sending clinical data to external services.
- An explicit request to change the GitHub plugin authorizes repository edits and
  a reviewable pull request. Public directory submission and changes to sharing
  need their own authorization. Cloud drafting must use only records permitted
  for the selected host; never describe web Work as on-device-only processing.

See MAINTENANCE.md for the source decision and archive location.
