---
name: weekly-summary
description: Draft a concise TSGH-aligned single-paragraph English inpatient Weekly Summary from clinician-supplied dated records. Use to synthesize a defined inpatient period or prepare a reliable building block for a long, complex discharge course.
---

# Weekly Summary

Create one comprehensive but concise English paragraph summarizing the inpatient course during the requested period. For a long or complex stay, write it so verified weekly summaries can later be combined chronologically into the discharge course without changing facts.

## Source and safety rules

- Use only supplied records the requester is authorized to handle.
- Do not invent or infer diagnoses, causal relationships, treatment responses, complications, or future plans.
- Do not independently recommend tests, medications, procedures, dose changes, disposition, or follow-up.
- Preserve important dates, values, medication and procedure details, problem numbering when relevant, uncertainty, and conflicts. Keep every supplied unit directly beside its measured value; never drop, convert, or guess a unit.
- Distinguish an intervention from its indication and a temporal sequence from a proven causal relationship.
- Keep data local and treat the result as requiring physician review and sign-off.

## Output modes

- Default to **Copy mode**: output the single-paragraph Weekly Summary first. Append `---` and `Physician considerations — outside the medical record` only when a clinically relevant gap, conflict, or ambiguous unit needs attention.
- Use **Review mode** only when requested: output the paragraph, followed by the same outside-record section for essential omissions, material conflicts, ambiguous dates/units/attribution, and statements requiring verification.

## Workflow

1. Identify the covered start and end dates, admission reason, relevant baseline condition, and established problem numbers when supplied.
2. Combine progress and nursing notes, laboratory data, imaging, procedures, consultations, treatment records, and documented education or disposition planning.
3. Select events that explain a meaningful clinical issue, management decision, operation or procedure, response, complication, consultation, or unresolved problem.
4. Arrange events chronologically and keep the documented chain clear: finding -> clinician assessment -> intervention -> documented response -> current status or next step.
5. Compress repetitive daily observations into trends only when at least two dated observations support them. Do not claim improvement, deterioration, stability, or tolerance without explicit support.
6. Retain specialty-specific events, operations, major diagnostic turning points, device changes, complications, and key pathology or imaging results needed for a future discharge course.
7. Produce exactly one paragraph in Copy mode.

## Paragraph structure

Use this order when the corresponding facts are available:

1. Start with `After admission, ...` or, for a later week, `During this week, ...` and identify the major active problem or initial evaluation.
2. Present key findings that affected assessment or management.
3. State documented medications, procedures, operations, consultations, monitoring, nutrition, or rehabilitation and their supplied purposes.
4. Describe documented responses, complications, and follow-up findings.
5. End with the current condition and clinician-supplied direction for the next period.

Do not force every element into the paragraph. Omit unsupported details rather than adding standard care.

## Style

- Use precise, chronological professional medical English.
- Prefer simple past tense for completed events and present tense for the current condition. Use future wording only for supplied plans.
- Use transitions such as `Subsequently`, `Given these findings`, `After the procedure`, and `During follow-up` only when they do not imply an unsupported causal relationship.
- Avoid raw-data dumping, repetitive daily lists, generic filler, and canned monitoring sentences.
- Do not silently change a medication, diagnosis, procedure name, problem number, or timeline to improve prose.

## Missing or conflicting information

- Omit a missing detail when the paragraph remains accurate.
- If the covered period or another essential fact is missing, omit it from the paragraph and identify it outside the medical record. A neutral prompt may ask the physician to confirm the missing fact or consider whether focused examination, laboratory testing, imaging, monitoring, or consultation is clinically indicated; never present it as an actual plan.
- State a clinically important unresolved conflict briefly; do not choose one value or interpretation.

## Final check

Confirm internally that every finding, diagnosis, intervention, response, complication, and future action is traceable to the supplied information; chronology is accurate; supported trends have multiple time points; and the final answer is exactly one paragraph in Copy mode.


## Maintenance

When asked to modify this skill, resolve the tsgh-clinical-notes plugin's marketplace source and edit that authoring copy. Installed cache copies and archived standalone skills are not maintenance sources. Follow the plugin-root AGENTS.md when present.
