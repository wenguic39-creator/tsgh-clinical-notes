---
name: admission-summary
description: Draft TSGH-aligned English Acceptance/Admission Summaries or full Admission Notes from clinician-supplied admission facts. Use for a new hospitalization, initial history and physical, or the Brief History, Impression, and Plans acceptance format.
---

# Admission Summary and Admission Note

Create either a three-section Acceptance/Admission Summary or a full Admission Note. Treat the result as a clinician-review draft, not a signed record.

## Input gate

- Use only records the requester is authorized to handle and the minimum necessary identifiers.
- Work solely from supplied facts. Do not infer, normalize, add, or silently reconcile findings, diagnoses, time points, medication doses, tests, or management plans.
- Preserve exact dates, times, test values, units, medication details, source attribution, and uncertainty.
- Never write `Not provided`, `None provided`, an invented normal/negative statement, or a filler plan inside the medical record when source data are absent. Do not use bracketed placeholders for missing patient facts.
- Keep missing clinically relevant information and possible follow-up evaluation outside the medical record, as described under **Outside-record physician considerations**.
- Do not turn an outside-record consideration into an order or documented plan. Organize only clinician-documented impressions and plans inside the note.
- Keep data local and treat every result as requiring clinician review and sign-off.

## Choose the format

- Use **Acceptance Summary** for `acceptance summary`, `admission summary`, or a request for `Brief History / Impression / Plans`.
- Use **Full Admission Note** for `admission note`, `initial H&P`, `initial history and physical`, or a request for the complete admission database.
- If the wording is only `admission` and the intended format cannot be inferred from the supplied fields, ask one short clarification question.

The TSGH writing priorities are completeness, clarity, accuracy, and timeliness. The institutional target is completion of the full admission note within 24 hours of admission. Do not claim the timing requirement was met unless timestamps establish it; flag a demonstrated delay outside the medical record.

## Output modes

- Default to **Copy mode**: output the copy-ready note first. If a clinically relevant source item is missing, conflicting, ambiguous, or requires consideration of further evaluation, append the outside-record section after the note. Do not add any other preface, warning, citation, or commentary.
- Use **Review mode** only when requested: use the same note-first structure and a more complete outside-record section for essential omissions, material conflicts, ambiguous attribution or timing, and statements requiring clinician verification.
- If no outside-record consideration is needed, return only the note.

## Common drafting rules

1. Build a chronological account from the chief complaint through admission.
2. Keep the chief complaint concise and include the duration when supplied. Prefer the patient's supplied wording; do not substitute a diagnosis for a symptom-based complaint unless the source explicitly documents a referral reason as the complaint.
3. In the present illness, describe supplied baseline health, onset, chronology, symptom characteristics, evaluation or treatment, pathology, imaging, tentative diagnosis, and reason for admission. Use OPQRST/LQQOPERA elements only when supplied.
4. Record positive and negative findings only when explicitly documented. Never copy the template's sample normal review of systems, examination, exposure history, family history, psychosocial statements, or allergy status unless supported by this patient's source.
5. Preserve every supplied unit directly beside its test value, including `%`, temperature units, pressure units, rates, concentrations, and dimensions. Do not convert, standardize, or drop a supplied unit. If a measurement is supplied without a unit, do not guess one; omit the unverified measurement when safe and flag it outside the medical record for unit verification. Established dimensionless scores and ratios may remain as documented.
6. Keep provisional diagnoses and differentials explicitly provisional. Include supporting rationale only when supplied by the clinician or directly documented as such.
7. For medications, preserve the documented generic or brand name, dose, route, frequency, duration, and hold criteria. Prefer a generic name only when it is supplied or the requester authorizes conversion.
8. Use the provided admission template as the field-order and wording-style reference, not as patient data. Template alternatives and stock sentences are choices, not defaults.
9. Establish the admission problem list as the longitudinal POMR index. Preserve prior problem numbers when supplied. When no numbering exists, assign `#1.`, `#2.`, and subsequent numbers once in clinician-supplied priority order; do not claim that newly assigned numbers are already the official chart numbering.
10. Keep the primary admitting problem as `#1.` when the supplied clinician order supports it. Retain secondary acute problems, relevant chronic conditions, functional or psychosocial problems, and risk factors only when documented and clinically relevant to the hospitalization.
11. Link each diagnostic, therapeutic, and educational plan to its problem number when the relationship is explicitly supplied or unambiguous from the clinician-authored context. Do not invent a linkage. Leave an unclear plan unnumbered and flag the missing relationship outside the medical record when clinically important.
12. Format every generated list item, including outside-record physician considerations, with the literal prefix `*.`. Do not use `-`, `+`, numbered Markdown lists, or Unicode bullets. When listing a numbered problem, write `*. #1. [Problem]`.
13. State clinical facts directly in the medical record. Never use record-source scaffolding such as `Per nursing documentation`, `According to the nursing note`, `Per chart review`, `The chart showed`, `The record noted`, or similar wording. Person-level attribution such as `The patient reported` or `The family stated` remains appropriate when clinically relevant.

## Acceptance Summary

Use exactly these headings in the medical-record portion.

### Brief History

Write one coherent chronological paragraph. When age, gender, and relevant history are supplied, prefer:

`This is a [age]-year-old [gender] with a past history of [relevant PMHx].`

When a demographic element or past history is missing, rewrite the opening naturally with only supplied facts; do not insert a placeholder. Describe onset, progression, interim management or absence of it, and the trigger for evaluation. Integrate only pertinent supplied positive and negative findings, examination, laboratory data, pathology, and imaging. End with the documented impression, admission date, and admission purpose only to the extent supplied; omit unavailable clauses rather than inserting blanks.

### Impression

List only documented primary and secondary diagnoses or impressions, one per line. Preserve clinician-supplied problem order and uncertainty. When supported, use:

`*. #1. [Diagnosis or problem] (supporting data: [specific documented finding])`

`*. #2. [Diagnosis or problem], with documented differential considerations of [supplied differential]`

Do not create a differential, etiology, or supporting rationale. If the diagnosis remains uncertain, a symptom, abnormal finding, or functional problem may be used only when already documented as the problem.

### Plans

Include only supplied actions; do not pad lists. Use only the applicable subsections below and omit a subsection with no documented action. Flag the absent clinically important plan category outside the medical record when physician attention is warranted.

#### Diagnostic plans

List ordered or explicitly planned tests, imaging, consultations, and monitoring evaluations. Prefix an item with the corresponding problem number when the relationship is supported, for example `*. #1. Follow the ordered sputum culture.`

#### Therapeutic plans

List documented medications, procedures, therapies, and monitoring parameters. Prefix an item with the corresponding problem number when the relationship is supported.

#### Educational plans

List documented condition explanations, safety measures, shared decisions, consent discussions, or patient/family education. Prefix an item with the corresponding problem number when the relationship is supported. Include template wording only when the requester confirms it was actually discussed or planned for this patient.

## Full Admission Note

Follow the supplied TSGH admission template's order. Keep the standard headings below, but do not place filler text under a heading with no source data. Omit empty optional subheadings; when a required heading must remain for the local form, leave its content blank and identify the gap only outside the medical record.

### Chief complaint

State the principal symptom or problem and duration in one concise line.

### Present illness

Write a chronological narrative following the common drafting rules. Incorporate supplied biopsy/pathology findings, CT/MR or other imaging, tentative diagnosis, impression, and reason for admission in sequence. Do not copy unused template sentence stems.

### *. Past history

Include supplied systemic diseases, onset or duration, treatment and control status, prior hospitalizations, operations, trauma, and relevant institutions or dates. Use explicit denials only when documented.

### *. Personal history

Include supplied tobacco exposure with amount and duration, alcohol, betel nut, marital status, occupation, travel, occupational exposure, contact, clustering, vaccination, sexual, developmental, obstetric, or other relevant history. Preserve quantified exposure units such as packs/day and years when supplied. Do not assume a missing exposure is negative.

### *. Allergy history

Record the allergen and documented reaction. Use `No known allergy` or an equivalent only when explicitly documented. Otherwise leave the heading blank and flag allergy verification outside the medical record.

### *. Family history

Include relevant familial disease and pedigree information when supplied. Do not insert a stock statement that family history is unremarkable.

### *. Psycho-socio-economic assessment

Include only supplied biological/functional status, emotional state, family support, social activity, spiritual needs, education or health literacy, main caregiver, financial or resource concerns, safety, and the patient's or family's understanding and concerns.

### Review of Systems

Separate documented positive and negative findings. Do not copy the template's blanket negative symptom list or generate a negative review from silence.

### Vital signs

Record only supplied vital signs, preserving each value with its unit.

### Physical examination

Record supplied height/weight with units, consciousness, general appearance, and system findings. Include only findings actually documented for this patient; do not use either sample normal examination block as a default.

### General laboratory data

List admission-relevant results with dates, exact values, and the original units. Keep value-unit pairs intact. Include reference ranges and comparison context only when supplied.

### Chest X-ray and other imaging

Record the supplied date and report wording for chest radiography and other relevant imaging. Omit modality subheadings with no result.

### Impression

List clinician-documented problems in priority order as the initial POMR problem list. Use stable identifiers in the form `*. #1. [Problem]`. Preserve uncertainty and supplied supporting reasoning or differential considerations without adding new ones.

### Diagnostic plans

List only ordered or explicitly planned tests, imaging, consultations, cultures, or monitoring. Link each item to the corresponding problem number when supported. Do not copy the template's routine panels or consultations unless documented for this patient.

### Therapeutic plans

List only documented medications, procedures, therapies, supportive care, monitoring parameters, or consultations. Link each item to the corresponding problem number when supported. Do not copy conditional or generic template treatments as actual plans.

### Educational plans

List only education, consent, prognosis, shared decisions, safety measures, or family discussions explicitly documented for this patient. Link each item to the corresponding problem number when supported.

## Outside-record physician considerations

When any clinically relevant field is absent, a value lacks its unit, records conflict, or the supplied data leave an important admission question unresolved, append this exact boundary after the note:

`---`

`Physician considerations — outside the medical record`

Use concise bullets that identify the gap and a neutral action for physician consideration, for example:

- `*. Allergy status is absent; consider confirming allergens and reactions before sign-off.`
- `*. The unit for [test] [value] is absent; verify the original unit before entering this result in the medical record.`
- `*. No admission imaging result was supplied; consider whether additional imaging is clinically indicated based on the presentation.`
- `*. No documented diagnostic plan addresses [supplied unresolved problem]; consider whether further examination, laboratory testing, imaging, monitoring, or consultation is indicated.`

Do not state that an examination or test was ordered, completed, normal, required, or recommended unless the source says so. Tailor considerations to the actual case and omit generic suggestions that are not clinically relevant. This section is never part of the copy-ready medical record.

## Final check

Confirm internally that every diagnosis, supporting fact, and plan is traceable to the source; the initial problem list uses stable numbers; supported plans map to those numbers; every generated list item begins with `*.`; no record-source scaffolding such as `Per nursing documentation` appears in the copy-ready note; no missing-data phrase or placeholder appears inside the note; every included measured value retains its supplied unit; no template example was treated as patient data; and all missing-data or further-evaluation prompts are confined to the outside-record section.


## Maintenance

When asked to modify this skill, resolve the tsgh-clinical-notes plugin's marketplace source and edit that authoring copy. Installed cache copies and archived standalone skills are not maintenance sources. Follow the plugin-root AGENTS.md when present.
