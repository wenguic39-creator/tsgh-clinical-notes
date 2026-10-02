---
name: clinical-note
description: Route clinician-supplied inpatient data into a TSGH-aligned English clinical note or a Chinese B/P/Sc/Sp/E/P/D holistic-care assessment. Use for Admission, Acceptance, Progress, Weekly, Discharge, or Operation Notes, and for 全人照護評估 or whole-person care forms.
---

# Clinical Note

Provide one entry point for the installed inpatient documentation skills and the Chinese holistic-care assessment form. Accept messy pasted source material, identify the requested output type and format, and return a copy-ready draft by default.

## Source and safety rules

- Use only records the requester is authorized to handle and only the minimum necessary identifiers.
- Do not invent, infer, normalize, or silently reconcile symptoms, findings, diagnoses, trends, treatment responses, medications, doses, tests, procedures, or plans.
- Preserve clinically important dates, times, values, medication details, uncertainty, attribution, and conflicts. Keep every supplied unit directly beside its measured value; never drop, convert, or guess a unit.
- Never place `Not provided`, `None provided`, `Plan not provided`, bracketed missing-data placeholders, or equivalent filler inside a medical record. Omit the missing content or leave a required local-form field blank, and place any clinically relevant gap in the outside-record physician section.
- Distinguish patient-reported information, observed facts, test results, and clinician-authored assessment or plans.
- Treat every result as a draft requiring physician review and sign-off, without adding that warning to Copy mode output.
- Keep source data local. Do not use web search, plugins, connectors, or remote services while processing a clinical note.

## Input handling

Accept unstructured mixtures of admission records, progress and nursing notes, laboratory data, imaging, medication records, procedures, consultations, weekly summaries, and clinician-authored plans. Sort events by date and time only when unambiguous. Remove exact duplicates while retaining meaningful changes.

The requester may use:

```text
Use $clinical-note.
Note type: admission | acceptance | progress | weekly | discharge | operation | holistic-care
Mode: copy | review

[paste source data]
```

Both fields are optional when they can be inferred safely. Default to Copy mode.

## Route the note

Honor an explicit note type. Otherwise route as follows:

- **Admission or acceptance**: full admission note, initial history and physical, acceptance summary, admission summary, or a new hospitalization narrative. Read and follow `../admission-summary/SKILL.md` completely. Preserve the requester's distinction between a full Admission Note and a three-section Acceptance/Admission Summary.
- **Progress**: progress note, daily note, today's note, SOAP, DAP, PAP, problem list update, or one-day inpatient review. Read and follow `../progress-note/SKILL.md` completely. Treat `SOAP` alone as conventional non-POMR SOAP; activate POMR only when the requester explicitly asks for POMR, a problem-oriented note, numbered problems, or explicitly requests a supplied POMR format.
- **Weekly**: weekly summary, week summary, seven-day course, or synthesis of several dated daily notes. Read and follow `../weekly-summary/SKILL.md` completely.
- **Discharge**: discharge summary, discharge course, discharge diagnoses and instructions, or final hospitalization summary. Read and follow `../discharge-summary/SKILL.md` completely.
- **Operation**: operation note, operative note, surgical record, procedure dictation, or post-procedure operative documentation. Read and follow `../operation-note/SKILL.md` completely.
- **Holistic care**: 全人照護評估, whole-person care assessment, holistic-care form, or a request using the B/P/Sc/Sp/E/P/D framework. Read [references/holistic-care-assessment.md](references/holistic-care-assessment.md) completely and follow its required Chinese structure. This is an educational or care-planning assessment, not one of the six English clinical-note types.

If the note type remains genuinely ambiguous after examining the wording, record type, and date range, ask one short clarification question. Do not generate multiple note types unless requested.

## TSGH-aligned documentation principles

Apply the local guide's four quality criteria throughout: completeness, clarity, accuracy, and timeliness. Keep each note internally consistent and suitable for longitudinal follow-up.

- For a full admission note, retain the supplied information needed to establish the initial database, provisional problems, and initial plans. The institutional target is completion within 24 hours of admission; do not claim compliance when timestamps are absent.
- For progress documentation, use assessment for the clinician's current interpretation, not as a duplicate diagnosis label. Preserve and display stable problem numbers only when POMR is explicitly requested.
- For discharge documentation, reconcile admission and final diagnoses only from explicit clinician documentation and make the hospital course chronological.
- For operation documentation, capture the indication, findings, critical steps, specimens or implants, blood loss, complications, closure, and postoperative condition when supplied.
- In Admission Notes, Acceptance Summaries, and Progress Notes, format every generated list item with the literal prefix `*.`. Do not use `-`, `+`, numbered Markdown lists, or Unicode bullets for list items. Problem identifiers such as `#1.` remain stable identifiers and follow `*.` when the item is listed.
- In the copy-ready medical record, state clinical content directly. Never introduce facts with record-source scaffolding such as `Per nursing documentation`, `According to the nursing note`, `Per chart review`, `The chart showed`, `The record noted`, or similar wording. When clinically important, retain person-level attribution such as `The patient reported` or `The family stated`; place unresolved source conflicts outside the medical record.
- For a holistic-care assessment, use Chinese, preserve the exact B/P/Sc/Sp/E/P/D section order, use plain headings without Markdown bold markers, and begin every list item with `*.`. Because the form requires every domain, explicitly identify an unsupported psychosocial, spiritual, economic, preference, or disposition field as not documented and state what should be clarified; never invent the missing fact.

## Output modes

### Copy mode - default

Return the copy-ready output first in the routed skill's required format. When clinically relevant information is missing, conflicting, or ambiguous, append the boundary `---` and the heading `Physician considerations — outside the medical record`, followed by concise physician-facing prompts. Keep these prompts out of a clinical note and do not represent a possible test, examination, or consultation as an actual order or plan. For Admission Notes, Acceptance Summaries, and Progress Notes, each consideration also starts with `*.`. For holistic-care assessments, handle required-domain gaps inside the form as directed by its reference rather than appending duplicate considerations. If no such consideration is needed, return only the requested output. Do not include any other preface, warning, citation, source summary, explanation, or closing remark.

### Review mode

Return the completed note first. Then add the same outside-record section with a more complete set of flags. Do not use `Review flags` inside the medical record.

List only:

- essential missing fields that prevent an accurate statement or complete required section, with a neutral prompt to confirm the information or consider whether focused examination, laboratory testing, imaging, monitoring, or consultation is clinically indicated;
- material conflicts between supplied records;
- ambiguous dates, times, units, medication details, attribution, problem numbering, or procedure details;
- output statements that require physician verification;
- a possible institutional timing issue only when supplied timestamps demonstrate it.

Do not present a new diagnosis, test, treatment, or procedure as decided or ordered. Possible further evaluation may appear only as a question or consideration for the physician and only when relevant to an actual gap in the supplied case.

## Routing quality check

Before responding, confirm internally that:

1. the correct note type, subtype, and mode were selected;
2. all clinical content is traceable to the supplied records;
3. no information from another patient, task, or unrelated case was used;
4. dates, uncertainty, problem numbering, and medication or procedure details remain faithful to the source, and every included measured value retains its supplied unit;
5. the output follows the routed skill's required structure;
6. no missing-data filler appears inside the note, and any physician consideration is clearly separated outside the medical record;
7. admission and progress list items use `*.` consistently, and the copy-ready note contains no record-source scaffolding such as `Per nursing documentation`.
8. a holistic-care assessment uses the complete Chinese B/P/Sc/Sp/E/P/D structure, plain headings, `*.` list items, and transparent gap statements instead of invented psychosocial facts.
9. an ordinary SOAP request remains non-POMR, while any POMR structure or problem numbering is supported by an explicit request.


## Maintenance

When asked to modify this skill, resolve the tsgh-clinical-notes plugin's marketplace source and edit that authoring copy. Installed cache copies and archived standalone skills are not maintenance sources. Follow the plugin-root AGENTS.md when present.
