---
name: progress-note
description: Draft TSGH-aligned English inpatient Progress Notes from clinician-supplied facts. Use for daily notes, problem-list updates, SOAP/DAP/PAP documentation, interval assessment, or problem-oriented plans.
---

# Progress Note

Create a concise English Progress Note for clinician review. By default, produce one conventional daily SOAP entry with global `S/O/A/P` sections and no POMR problem numbers or problem-oriented subdivision. Use POMR only when the requester explicitly asks for `POMR`, a `problem-oriented` note, a numbered problem list, or explicitly asks to follow a supplied POMR format. Do not infer a POMR request merely because the source contains multiple diagnoses or problems. Use per-problem SOAP only when the requester explicitly asks for it. When the requester provides a predecessor note, senior's note, or institutional example, preserve its useful local conventions while applying the current request and the source and safety rules below.

## Safety and source rules

- Use only records the requester is authorized to handle and only supplied information.
- Preserve exact dates, times, values, medication names, doses, routes, and frequencies. When POMR is explicitly requested, also preserve established problem numbers. Keep every supplied unit directly beside its measured value; never drop, convert, or guess a unit.
- Omit missing content from the note rather than writing `Not provided`, `None provided`, `Plan not provided`, or a bracketed placeholder. Put clinically relevant gaps and possible further-evaluation prompts only in a clearly separated `Physician considerations — outside the medical record` section after the note.
- Do not invent or infer symptoms, examinations, diagnoses, trends, treatment responses, plans, or a normal finding.
- Do not independently recommend tests, medications, procedures, dose changes, disposition, or follow-up.
- Distinguish patient-reported information, objective data, and clinician assessment. Flag conflicts rather than silently reconciling them.
- State clinical content directly in the copy-ready note. Never use record-source scaffolding such as `Per nursing documentation`, `According to the nursing note`, `Per chart review`, `The chart showed`, `The record noted`, or similar wording. Use concise person-level attribution such as `The patient reported` or `The family stated` only when clinically relevant.
- Format every generated list item, including outside-record physician considerations, with the literal prefix `*.`. Do not use `-`, `+`, numbered Markdown lists, or Unicode bullets.
- Process supplied records only within the current authorized ChatGPT or Codex session. Do not send clinical source data to web search, connectors, external plugins, MCP servers, or other services. Loading this plugin's bundled skills and references is allowed.
- ChatGPT on the web may process records in the cloud; do not claim on-device-only processing. Use only data permitted by the requester's institutional policy for the selected host.
- Treat the result as requiring clinician review and sign-off.

## Output modes

- Default to **Copy mode**: output the completed Progress Note first. Append an outside-record physician-considerations section only when a clinically relevant gap, conflict, or ambiguous unit needs attention.
- Use **Review mode** only when requested: output the note, followed by the same clearly separated outside-record section for essential omissions, material conflicts, ambiguous dates/units/attribution, inconsistent problem numbering, and statements requiring verification.

## Reference-format handling

When a prior note is supplied as a formatting reference:

1. Treat its layout, labels, abbreviation density, ordering, and problem-grouping conventions as the format source. Do not treat embedded clinical facts as current facts unless the requester also supplies or identifies them as part of the same patient's usable record.
2. Identify whether the reference uses conventional global SOAP, POMR, per-problem SOAP, DAP, PAP, or another structure. Follow its useful conventions, but activate POMR only when the requester explicitly asks for POMR or explicitly asks to follow that reference's POMR structure. In all cases, normalize generated list markers to `*.` unless the requester explicitly requests another marker.
3. Match useful local conventions such as compact dated event lists, system tags, arrows for documented changes, diagnosis headings with indented course details, and concise action lists.
4. Preserve a reference tag such as `[N]`, `[S]`, `[V]`, `[I]`, or `[P]` only when its meaning is demonstrated by the reference. Do not guess the meaning of an ambiguous tag; use an explicit heading instead.
5. Use the reference as a structural model, not as permission to reproduce its classification errors, unsupported interpretations, misspellings, or data from another encounter.
6. When later nursing data are added, update the current observations in `O:` and place only explicit new orders or authorized actions in `P:`. Do not revise `A:` solely because a nursing observation was added unless the requester or supplied clinician documentation provides the corresponding assessment.

## Explicit single-entry EMR POMR mode

Use this hybrid format only when the requester explicitly asks for POMR or a problem-oriented note and one daily SOAP entry is linked to one EMR problem:

1. Link the entry to the problem selected by the requester. If no selection is supplied, use the established primary active problem only when it is unambiguous from the clinician-supplied problem order and today's management. Otherwise, keep the note accurate and place a concise problem-selection question outside the medical record.
2. Keep one global `S:` section for today's patient- or family-reported interval information and one global `O:` section for current observations, examination, results, procedures, and treatments. Do not repeat the same data under multiple problems.
3. Use `A:` as today's problem-oriented assessment list. Preserve stable problem numbers from admission or prior notes, and include active, new, or meaningfully changed problems relevant today.
4. Use `P:` with the same problem numbers. Each plan must map to the problem it addresses. A plan spanning several problems may carry multiple supported numbers. Do not create a plan merely to fill a missing number.
5. The EMR-selected problem is the anchor for the single entry, not a reason to hide other active problems. Place the selected primary problem first in `A:` and `P:` while preserving its established number.
6. If the user asks for one SOAP only, do not generate multiple standalone SOAP entries.

Use this copy-ready structure:

```text
S:
*. [Supplied interval history]

O:
*. [Supplied objective finding]

A:
*. #1. [Problem]: [supplied current interpretation and decision-relevant evidence]
*. #2. [Problem]: [supplied current interpretation and decision-relevant evidence]

P:
*. #1. [Documented action]
*. #2. [Documented action]
```

## TSGH RCC/ICU global SOAP variant

Use this compact variant when the requester asks to follow an RCC/ICU predecessor note or supplies a similar senior-authored example:

```text
S:
*. [Patient-reported information or why it cannot be obtained]
*. [Concise interval history and relevant documented negatives]

O:
*. [Vital sign]
*. [N] [Nutrition, when established by the reference]
*. [S] [Sensorium/neurological status, when established by the reference]
*. [V] [Ventilator and respiratory status]
*. [I] [Infection, antimicrobial course, and microbiology]
*. [Renal/HD]
*. [Physical examination]
*. [Lines/Skin]
*. [Imaging]
*. [Laboratory]

A:
*. [Supplied current interpretation, dated complication, procedure, response, or status]

P:
*. [Documented current action, dated medication or support change, or explicit follow-up schedule]
```

Keep the note global: use one `S/O/A/P` sequence and organize `O:` by systems. In ordinary SOAP mode, keep `A:` and `P:` concise and unnumbered; do not turn diagnoses into a POMR problem list. If POMR is explicitly requested, organize `A:` and `P:` by established problem numbers and preserve the predecessor's problem order and grouping. Put only the most decision-relevant current results and trends in the main note; retain exact dates for older events that materially explain today's assessment or plan.

In this variant:

- A noncommunicative patient's `S:` should state that subjective information could not be obtained. A short interval history may follow when its source or attribution is clear.
- `O:` may be dense, but do not duplicate the same GCS, ventilator setting, culture, image, or laboratory value under multiple headings.
- `A:` should distinguish an active condition from a historical or resolved complication when the supplied clinician documentation does so.
- `P:` should remain concise and action-oriented. Preserve exact medication changes, support settings, treatment dates, and monitoring schedules; do not add a rationale or endpoint that was not supplied.

## POMR problem-list rules

Apply these rules only after an explicit POMR request. They do not apply to an ordinary SOAP request.

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
2. Determine whether POMR was explicitly requested. A request for `SOAP` alone means conventional, non-POMR SOAP.
3. For conventional SOAP, select the supplied information needed for today's global `S/O/A/P` without creating problem numbers or a problem list. For explicit POMR, reconstruct or preserve the problem list and select active or changed problems for today's note.
4. Build one global `S/O/A/P` by default. Use problem-oriented `A/P` or separate S/O/A/P blocks under each problem only when explicitly requested. Do not place a clinician interpretation under Objective or raw data alone under Assessment.
5. Remove repetition while retaining evidence needed for today's assessment and plan.

## Default output

Use this format unless the requester specifies another:

### Date / Hospital Day

Write `Date: YYYY/MM/DD` and `Hospital day: [number]` only when supplied. Include the note time or author role only when provided and requested.

### Medical Condition

Use a supplied descriptor such as `good`, `fair`, `serious`, or `critical`, and a supplied trajectory such as `improving`, `worsening`, or `unchanged`. Omit this heading if neither is documented.

### SOAP

Use one conventional global `S/O/A/P` without POMR numbering:

`S:`

`*. [supplied subjective information]`

`O:`

`*. [supplied objective information]`

`A:`

`*. [supplied clinician assessment/current status]`

`P:`

`*. [documented plan]`

Do not make the `A:` list function as a numbered problem list in ordinary SOAP mode. If POMR is explicitly requested, use the explicit POMR structure above, preserve established problem numbers and documented status, and omit unchanged inactive or resolved problems unless they remain relevant to today's care. When the requester explicitly asks for DAP or PAP, map the supplied content without adding POMR numbering unless POMR was also explicitly requested.

## Style

- Use concise professional medical English and readable phrases.
- Avoid copying a fixed normal template or duplicating the same result under multiple problems unless it independently affects each assessment.
- Keep the reasoning chain visible: new evidence -> current assessment -> documented action.
- Use `*.` for every generated list item. Keep each problem's assessment or plan compact enough to remain on one list item when readable.
- Write direct clinical statements and remove record-source scaffolding. Do not write `Per nursing documentation`, `According to the nursing note`, `Per chart review`, `The chart showed`, `The record noted`, or close variants.
- Do not add citations, explanations, or a second interpretation outside the note.

## Final check

Confirm internally that one SOAP entry was produced when requested; an ordinary SOAP request uses conventional global, unnumbered `S/O/A/P`; POMR appears only after an explicit POMR or problem-oriented request; when POMR is used, problem numbers remain stable and match between `A:` and `P:`; every generated list item begins with `*.`; no record-source scaffolding appears in the copy-ready note; every S/O/A/P statement is in the correct category and traceable to the supplied record; the assessment adds the documented interpretation rather than repeating the diagnosis; and no action, trend, normal finding, or problem status was invented.


## Maintenance

When asked to modify this skill, resolve the tsgh-clinical-notes plugin's marketplace source and edit that authoring copy. Installed cache copies and archived standalone skills are not maintenance sources. Follow the plugin-root AGENTS.md when present.
