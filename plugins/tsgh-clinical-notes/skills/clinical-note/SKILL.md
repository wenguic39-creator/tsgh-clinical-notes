---
name: clinical-note
description: Route clinician-supplied inpatient data into a TSGH-aligned English Admission Note or Acceptance Summary, problem-oriented Progress Note, Weekly Summary, Discharge Summary, or Operation Note. Use when raw clinical records need to become one of these copy-ready note types.
---

# Clinical Note

Provide one entry point for the installed inpatient documentation skills. Accept messy pasted source material, identify the requested note type and format, and return a copy-ready English draft by default.

## Source and safety rules

- Use only records the requester is authorized to handle and only the minimum necessary identifiers.
- Do not invent, infer, normalize, or silently reconcile symptoms, findings, diagnoses, trends, treatment responses, medications, doses, tests, procedures, or plans.
- Preserve clinically important dates, times, values, units, medication details, uncertainty, attribution, and conflicts.
- Distinguish patient-reported information, observed facts, test results, and clinician-authored assessment or plans.
- Treat every result as a draft requiring physician review and sign-off, without adding that warning to Copy mode output.
- Keep source data local. Do not use web search, plugins, connectors, or remote services while processing a clinical note.

## Input handling

Accept unstructured mixtures of admission records, progress and nursing notes, laboratory data, imaging, medication records, procedures, consultations, weekly summaries, and clinician-authored plans. Sort events by date and time only when unambiguous. Remove exact duplicates while retaining meaningful changes.

The requester may use:

```text
Use $clinical-note.
Note type: admission | acceptance | progress | weekly | discharge | operation
Mode: copy | review

[paste source data]
```

Both fields are optional when they can be inferred safely. Default to Copy mode.

## Route the note

Honor an explicit note type. Otherwise route as follows:

- **Admission or acceptance**: full admission note, initial history and physical, acceptance summary, admission summary, or a new hospitalization narrative. Read and follow `../admission-summary/SKILL.md` completely. Preserve the requester's distinction between a full Admission Note and a three-section Acceptance/Admission Summary.
- **Progress**: progress note, daily note, today's note, SOAP, DAP, PAP, problem list update, or one-day inpatient review. Read and follow `../progress-note/SKILL.md` completely.
- **Weekly**: weekly summary, week summary, seven-day course, or synthesis of several dated daily notes. Read and follow `../weekly-summary/SKILL.md` completely.
- **Discharge**: discharge summary, discharge course, discharge diagnoses and instructions, or final hospitalization summary. Read and follow `../discharge-summary/SKILL.md` completely.
- **Operation**: operation note, operative note, surgical record, procedure dictation, or post-procedure operative documentation. Read and follow `../operation-note/SKILL.md` completely.

If the note type remains genuinely ambiguous after examining the wording, record type, and date range, ask one short clarification question. Do not generate multiple note types unless requested.

## TSGH-aligned documentation principles

Apply the local guide's four quality criteria throughout: completeness, clarity, accuracy, and timeliness. Keep each note internally consistent and suitable for problem-oriented follow-up.

- For a full admission note, retain the supplied information needed to establish the initial database, provisional problems, and initial plans. The institutional target is completion within 24 hours of admission; do not claim compliance when timestamps are absent.
- For progress documentation, preserve stable problem numbers and use assessment for the clinician's current interpretation, not as a duplicate diagnosis label.
- For discharge documentation, reconcile admission and final diagnoses only from explicit clinician documentation and make the hospital course chronological.
- For operation documentation, capture the indication, findings, critical steps, specimens or implants, blood loss, complications, closure, and postoperative condition when supplied.

## Output modes

### Copy mode - default

Return only the final note in the routed skill's required format. Do not include a preface, warning, citation, source summary, explanation, or closing remark. Retain only headings required by that format.

### Review mode

Return the completed note first. Then add:

`Review flags`

List only:

- essential missing fields that prevent an accurate statement or complete required section;
- material conflicts between supplied records;
- ambiguous dates, times, units, medication details, attribution, problem numbering, or procedure details;
- output statements that require physician verification;
- a possible institutional timing issue only when supplied timestamps demonstrate it.

Do not propose new diagnoses, tests, treatments, or procedures in Review flags.

## Routing quality check

Before responding, confirm internally that:

1. the correct note type, subtype, and mode were selected;
2. all clinical content is traceable to the supplied records;
3. no information from another patient, task, or unrelated case was used;
4. dates, units, uncertainty, problem numbering, and medication or procedure details remain faithful to the source;
5. the output follows the routed skill's required structure;
6. Copy mode contains nothing except the copy-ready note.
