---
name: progress-note
description: Draft TSGH-aligned English inpatient Progress Notes from clinician-supplied facts. Use for daily notes, problem-list updates, SOAP/DAP/PAP documentation, interval assessment, or problem-oriented plans.
---

# Progress Note

Create a concise English Progress Note for clinician review. Use POMR and per-problem SOAP when no local format is supplied. When the requester provides a predecessor note, senior's note, institutional example, or explicitly requests a global SOAP format, preserve that established documentation structure while applying the source and safety rules below.

## Safety and source rules

- Use only records the requester is authorized to handle and only supplied information.
- Preserve exact dates, times, values, medication names, doses, routes, frequencies, and problem numbers. Keep every supplied unit directly beside its measured value; never drop, convert, or guess a unit.
- Omit missing content from the note rather than writing `Not provided`, `None provided`, `Plan not provided`, or a bracketed placeholder. Put clinically relevant gaps and possible further-evaluation prompts only in a clearly separated `Physician considerations — outside the medical record` section after the note.
- Do not invent or infer symptoms, examinations, diagnoses, trends, treatment responses, plans, or a normal finding.
- Do not independently recommend tests, medications, procedures, dose changes, disposition, or follow-up.
- Distinguish patient-reported information, objective data, and clinician assessment. Flag conflicts rather than silently reconciling them.
- Keep data local and treat the result as requiring clinician review and sign-off.

## Output modes

- Default to **Copy mode**: output the completed Progress Note first. Append an outside-record physician-considerations section only when a clinically relevant gap, conflict, or ambiguous unit needs attention.
- Use **Review mode** only when requested: output the note, followed by the same clearly separated outside-record section for essential omissions, material conflicts, ambiguous dates/units/attribution, inconsistent problem numbering, and statements requiring verification.

## Reference-format handling

When a prior note is supplied as a formatting reference:

1. Treat its layout, labels, abbreviation density, ordering, and problem-grouping conventions as the format source. Do not treat embedded clinical facts as current facts unless the requester also supplies or identifies them as part of the same patient's usable record.
2. Identify whether the reference uses global SOAP, per-problem SOAP, DAP, PAP, or another structure. Follow that structure instead of forcing the default POMR layout.
3. Match useful local conventions such as compact dated event lists, system tags, arrows for documented changes, diagnosis headings with indented course details, and concise action lists.
4. Preserve a reference tag such as `[N]`, `[S]`, `[V]`, `[I]`, or `[P]` only when its meaning is demonstrated by the reference. Do not guess the meaning of an ambiguous tag; use an explicit heading instead.
5. Use the reference as a structural model, not as permission to reproduce its classification errors, unsupported interpretations, misspellings, or data from another encounter.
6. When later nursing data are added, update the current observations in `O:` and place only explicit new orders or authorized actions in `P:`. Do not revise `A:` solely because a nursing observation was added unless the requester or supplied clinician documentation provides the corresponding assessment.

## TSGH RCC/ICU global SOAP variant

Use this compact variant when the requester asks to follow an RCC/ICU predecessor note or supplies a similar senior-authored example:

```text
S:
[Patient-reported information or why it cannot be obtained]
[Concise attributed interval history and relevant documented negatives]

O:
[Vital sign]
[N] [Nutrition, when established by the reference]
[S] [Sensorium/neurological status, when established by the reference]
[V] [Ventilator and respiratory status]
[I] [Infection, antimicrobial course, and microbiology]
[Renal/HD]
[Physical examination]
[Lines/Skin]
[Imaging]
[Laboratory]

A:
*. [Major diagnosis or established problem]:
- [Dated complication, procedure, response, or current status]

P:
*. [Documented current action]
[Dated medication or support change]
[Explicit laboratory or imaging follow-up schedule]
```

Keep the note global: use one `S/O/A/P` sequence, organize `O:` by systems, and organize `A:` and `P:` by major diagnoses or active management domains. Preserve the predecessor's established problem order and grouping when supplied. Put only the most decision-relevant current results and trends in the main note; retain exact dates for older events that materially explain today's assessment or plan.

In this variant:

- A noncommunicative patient's `S:` should state that subjective information could not be obtained. A short interval history may follow when its source or attribution is clear.
- `O:` may be dense, but do not duplicate the same GCS, ventilator setting, culture, image, or laboratory value under multiple headings.
- `A:` should distinguish an active condition from a historical or resolved complication when the supplied clinician documentation does so.
- `P:` should remain concise and action-oriented. Preserve exact medication changes, support settings, treatment dates, and monitoring schedules; do not add a rationale or endpoint that was not supplied.

## POMR problem-list rules

1. Preserve an established problem number for the entire hospitalization. Never renumber problems merely because priority changes or a problem resolves.
2. When no prior numbering is supplied, assign numbers once in clinician-supplied priority order or, when that order is absent, by documented severity and urgency. Do not claim this matches the official chart until verified.
3. A problem may be a documented diagnosis, symptom, abnormal examination or laboratory finding, physiologic issue, psychological issue, behavioral issue, social/demographic issue, or risk factor.
4. Do not put `possible`, `probable`, `suspected`, or `rule out` in the problem label when a more concrete documented symptom or finding can represent the unresolved problem. Preserve the clinician's differential and uncertainty in `A:` instead.
5. Group closely related findings only when the source treats them as one clinical problem. Keep distinct problems separate when doing so affects assessment or management.
6. Mark a problem `active`, `inactive`, or `resolved` only when the source does so. Do not delete resolved problems from an established list.
7. Daily notes need not repeat unchanged details for every problem. Address newly identified, active, or meaningfully changed problems and retain enough context to understand the change.

## SOAP definitions

- `S:` patient-reported complaint, symptoms, relevant history, function, intake/output, tolerance, or concerns. Include negatives only when documented.
- `O:` vital signs, examination, laboratory, microbiology/pathology, imaging, procedures, and other observed data. Describe a trend only when at least two time points support it.
- `A:` the clinician's analysis of the problem's present status, response, cause, differential, or unresolved issue. Assessment is not merely a repeated diagnosis. Preserve terms such as `possible`, `cannot rule out`, `improving`, `worsening`, `unchanged`, and `resolved` only when documented.
- `P:` clinician-authorized next actions. Organize documented actions as diagnostic, therapeutic, educational/informed, consultation, follow-up, monitoring, or disposition plans when useful.

If the source provides no subjective information for a problem, do not transform silence into `no complaint` and do not insert missing-data filler. Omit the empty SOAP field when the established format permits; otherwise retain the label with no fabricated content and flag an essential gap outside the medical record. Apply the same principle to `O:`, `A:`, and `P:`. A possible further examination, laboratory test, imaging study, monitoring step, or consultation may appear only as a neutral physician consideration outside the note, never as an ordered plan unless documented.

## Workflow

1. Identify note date/time, hospital day, author role, and supplied medical-condition descriptor.
2. Reconstruct or preserve the problem list and its numbering.
3. Select problems requiring documentation today based on supplied new or changed information.
4. Separate S, O, A, and P under each problem. Do not place a clinician interpretation under Objective or raw data alone under Assessment.
5. Remove repetition while retaining evidence needed for today's assessment and plan.

## Default output

Use this format unless the requester specifies another:

### Date / Hospital Day

Write `Date: YYYY/MM/DD` and `Hospital day: [number]` only when supplied. Include the note time or author role only when provided and requested.

### Medical Condition

Use a supplied descriptor such as `good`, `fair`, `serious`, or `critical`, and a supplied trajectory such as `improving`, `worsening`, or `unchanged`. Omit this heading if neither is documented.

### Problem List

List established problems with stable numbers and documented status when supplied:

`#1. [Problem] - [active/inactive/resolved]`

Do not invent the status or alter the original numbering.

### Problem-oriented Progress

For each addressed problem, use:

`#1. [Problem]`

`S: [supplied subjective information]`

`O: [supplied objective information]`

`A: [supplied clinician assessment/current status]`

`P: [supplied plan]`

When the requester explicitly asks for DAP or PAP, preserve the same problem numbering and map content without mixing assessment with raw data or adding plans.

## Style

- Use concise professional medical English and readable phrases.
- Avoid copying a fixed normal template or duplicating the same result under multiple problems unless it independently affects each assessment.
- Keep the reasoning chain visible: new evidence -> current assessment -> documented action.
- Do not add citations, explanations, or a second interpretation outside the note.

## Final check

Confirm internally that problem numbers remain stable; every S/O/A/P statement is in the correct category and traceable to the supplied record; the assessment adds the documented interpretation rather than repeating the diagnosis; and no action, trend, normal finding, or problem status was invented.
