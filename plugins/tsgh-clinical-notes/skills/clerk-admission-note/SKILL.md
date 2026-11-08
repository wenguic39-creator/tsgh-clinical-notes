---
name: clerk-admission-note
description: Draft a TSGH-aligned Clerk admission note with the same content and order as a full Admission Note and main headings in literal square brackets. Use for Clerk admission note, clerk admission, or clerk-admission-note requests.
---

# Clerk admission note

Process supplied records only within the current authorized ChatGPT or Codex session. Do not send clinical source data to external services. A medication reference lookup may include only non-patient product-identification details as specified by the shared medication rule. Web sessions may process data in the cloud; do not claim on-device-only processing.

Read and follow [Admission Summary and Admission Note](../admission-summary/SKILL.md) completely. Select its Full Admission Note content and its Clerk admission note heading rule. Also read and apply [Medication names](../../references/medication-names.md).

Produce the same clinical content, field order, supplied-fact safeguards, Copy/Review modes, `*.` body list markers, and explicit-only POMR behavior as a full Admission Note. Render every main medical-record section heading as a plain literal `[Heading]` line, for example `[Chief complaint]`, `[Present illness]`, `[Past history]`, and `[Impression]`. Remove Markdown markers and a heading-level `*.` only from those main headings. Leave subheadings, body content, and the outside-record physician-considerations heading under the parent skill's rules.

Do not turn this into an Acceptance Summary, add clinical facts, bracket prose or missing-data placeholders, or change the headings of an ordinary Admission Note that was not requested as Clerk. An explicit request for this skill is a Clerk request even if the accompanying text merely says admission note.
