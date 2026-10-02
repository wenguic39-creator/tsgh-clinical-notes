# TSGH Clinical Notes maintenance

This plugin is the single authoring source for clinical-note, admission-summary,
progress-note, weekly-summary, discharge-summary, and operation-note.
For this personal installation, the marketplace source is
`C:\Users\USER\plugins\tsgh-clinical-notes`.

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
- Follow plugin-creator's local update flow: validate the personal marketplace name,
  update the manifest with its cachebuster helper, reinstall
  `tsgh-clinical-notes@personal`, and verify installed files match this source.
  Preserve the marketplace entry and unrelated configuration.
- New tasks are the pickup boundary after reinstall. Existing tasks may retain
  earlier skill context; do not claim they have refreshed automatically.
- Local maintenance does not authorize pushing to GitHub, publishing a plugin,
  or sending clinical data to external services.

See MAINTENANCE.md for the source decision and archive location.
