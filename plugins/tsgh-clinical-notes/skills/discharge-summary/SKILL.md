---
name: discharge-summary
description: Draft a TSGH-aligned English Discharge Summary from clinician-supplied hospitalization records. Use for final diagnoses, hospital course and treatment, complications, condition on discharge, and documented discharge instructions.
---

# Discharge Summary

Create an accurate, chronological English Discharge Summary that communicates the completed hospitalization and documented transition plan. Treat it as a clinician-review draft, not a signed record.

## Source and safety rules

- Use only supplied records the requester is authorized to handle and only the minimum necessary identifiers.
- Do not invent or infer final diagnoses, causal relationships, treatment effects, complications, resolved status, medication reconciliation, follow-up, or discharge readiness.
- Preserve exact dates, values, units, medication details, procedure names, pathology or imaging wording, uncertainty, and conflicts.
- Distinguish admission diagnoses from final discharge diagnoses. Use only clinician-documented final diagnoses in the discharge list.
- Do not independently recommend medication changes, follow-up, tests, diet, activity, wound care, or warning signs.
- Keep data local and treat the result as requiring physician review and sign-off.

## Output modes

- Default to **Copy mode**: output only the completed Discharge Summary with the required headings and no warning, preface, citation, explanation, or commentary.
- Use **Review mode** only when requested: output the summary, followed by `Review flags` for essential omissions, material conflicts, unreconciled diagnoses or medications, ambiguous dates/units/attribution, and statements requiring verification.

## Workflow

1. Establish admission and discharge dates, admission reason, initial diagnoses, final diagnoses, procedures, and discharge destination when supplied.
2. Reconcile the timeline from admission records, problem-oriented progress notes, weekly summaries, operation notes, consultations, investigations, and treatment records without changing facts.
3. For a short stay, write the course directly and concisely. For a long or complex stay, combine verified weekly summaries chronologically, then integrate major operations, specialty care, complications, and final status.
4. Include evidence supporting a final diagnosis only when documented or directly linked by the responsible clinician. Do not promote a provisional differential into a final diagnosis.
5. Preserve the documented indication, major findings, and outcome of procedures or operations without reproducing the entire operation note.
6. Reconcile discharge medications and instructions only from the final clinician-authored discharge plan.

## Required output

Use the headings below in this order. Write `Not provided` when a required field lacks source data; do not fabricate a normal or negative statement.

### Admission Date

Use `YYYY/MM/DD` only when unambiguous.

### Discharge Date

Use `YYYY/MM/DD` only when unambiguous.

### Admission Diagnoses

List clinician-documented diagnoses or problems present at admission. Preserve provisional wording.

### Discharge Diagnoses

List clinician-documented final diagnoses in supplied priority order. Do not copy unresolved rule-out diagnoses as final.

### Chief Complaint

State the supplied principal symptom or reason for admission and duration.

### Present Illness

Summarize the pre-admission course concisely without duplicating the hospital course.

### Past History

Include only history relevant to the admission or discharge plan.

### Allergy History

Record the allergen and reaction. Use `No known drug allergies` only when explicitly documented.

### Physical Examination on Admission

Summarize documented admission findings relevant to the hospitalization.

### Laboratory, Imaging, and Diagnostic Results

Include decisive or management-changing results with dates, units, and final report status when supplied. Separate pathology or special examinations when the source or requester requires distinct fields.

### Hospital Course and Treatment

Write a concise chronological narrative. Include major diagnostic turning points, treatments, operations or procedures, consultations, clinically important responses, complications, and unresolved issues. Use documented temporal or causal links only.

### Complications

List documented inpatient complications and their status. Write `None documented` only when the source explicitly states there were no complications; otherwise write `Not provided`.

### Condition on Discharge

State only the documented condition, functional status, key devices or wounds, oxygen or nutrition needs, and disposition.

### Discharge Medications

Preserve the final documented name, dose, route, frequency, duration, indication, and hold criteria when supplied. Do not infer that an inpatient medication continues after discharge.

### Discharge Instructions

List only documented follow-up appointments or tests, diet, activity, wound/device care, rehabilitation, education, return precautions, and pending-result responsibilities. Preserve who should follow a pending result when supplied.

## Style

- Use concise professional medical English and chronological organization.
- Avoid copying every daily value, repeating the same event in multiple sections, or pasting weekly summaries without integration.
- Use operation and specialty terminology exactly as documented; avoid colloquial substitutions.
- Keep the final diagnoses, course, condition, medications, and instructions mutually consistent. Surface conflicts in Review mode rather than silently fixing them.

## Final check

Confirm internally that admission and discharge diagnoses are distinguished; the course explains major management and outcomes without unsupported causality; complications and discharge condition are not assumed; final medications and instructions come from the discharge plan; and every statement is traceable to the supplied record.
