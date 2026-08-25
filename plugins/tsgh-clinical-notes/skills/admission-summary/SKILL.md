---
name: admission-summary
description: Draft TSGH-aligned English Acceptance/Admission Summaries or full Admission Notes from clinician-supplied admission facts. Use for a new hospitalization, initial history and physical, or the Brief History, Impression, and Plans acceptance format.
---

# Admission Summary and Admission Note

Create either a three-section Acceptance/Admission Summary or a full Admission Note. Treat the result as a clinician-review draft, not a signed record.

## Input gate

- Use only records the requester is authorized to handle and the minimum necessary identifiers.
- Work solely from supplied facts. Do not infer, normalize, add, or silently reconcile findings, diagnoses, time points, medication doses, tests, or management plans.
- Preserve exact dates, times, values, units, medication details, source attribution, and uncertainty.
- If facts conflict or are missing, retain the uncertainty, write `Not provided`, or leave a requested blank; do not resolve it.
- Do not make new diagnostic or treatment recommendations. Organize only clinician-documented impressions and plans.
- Keep data local and treat every result as requiring clinician review and sign-off.

## Choose the format

- Use **Acceptance Summary** for `acceptance summary`, `admission summary`, or a request for `Brief History / Impression / Plans`.
- Use **Full Admission Note** for `admission note`, `initial H&P`, `initial history and physical`, or a request for the complete admission database.
- If the wording is only `admission` and the intended format cannot be inferred from the supplied fields, ask one short clarification question.

The TSGH writing priorities are completeness, clarity, accuracy, and timeliness. The institutional target is completion of the full admission note within 24 hours of admission. Do not claim the timing requirement was met unless timestamps establish it; in Review mode, flag a demonstrated delay.

## Output modes

- Default to **Copy mode**: output only the completed note. Do not add a draft warning, preface, explanation, citation, or review commentary.
- Use **Review mode** only when requested: output the completed note, followed by `Review flags` listing essential omissions, material conflicts, ambiguous attribution or timing, and statements requiring clinician verification.

## Common drafting rules

1. Build a chronological account from the chief complaint through admission.
2. Keep the chief complaint concise and include the duration. Prefer the patient's supplied wording; do not substitute a diagnosis for a symptom-based complaint unless the source explicitly documents a referral reason as the complaint.
3. In the present illness, describe baseline health, onset, chronology, symptom characteristics, relevant evaluation or treatment, and the reason for hospital care. Use OPQRST/LQQOPERA elements only when supplied. Include only past, social, or exposure history relevant to the current illness; place pertinent concurrent disease near the end.
4. Record positive and negative findings only when explicitly documented. Never generate a normal review of systems or examination from silence.
5. Preserve test dates, values, units, and comparison context. Do not convert units or mix reference conventions without instruction.
6. Keep provisional diagnoses and differentials explicitly provisional. Include supporting rationale only when supplied by the clinician or directly documented as such.
7. For medications, preserve the documented generic or brand name, dose, route, frequency, duration, and hold criteria. Prefer a generic name only when it is supplied or the requester authorizes conversion.

## Acceptance Summary

Use exactly these headings in Copy mode.

### Brief History

Write one coherent chronological paragraph. Start:

`This is a [age]-year-old [gender] with a past history of [relevant PMHx].`

If age is unavailable, use `This is a [ ]-year-old ...` for manual completion. Describe onset, progression, interim management or absence of it, and the trigger for emergency evaluation. Integrate only pertinent supplied positive and negative findings, examination, laboratory data, and imaging. Include the admission date as `YYYY/MM/DD` only when unambiguous. End:

`Under the impression of [stated diagnosis], [he/she/the patient] was admitted to our ward on [YYYY/MM/DD] for [stated admission reason].`

Use a gendered pronoun only when supplied; otherwise use `the patient`.

### Impression

List only documented primary and secondary diagnoses or impressions, one per line. Preserve clinician-supplied problem order and uncertainty. When supported, use:

`*. [Diagnosis or problem] (supporting data: [specific documented finding])`

`*. [Diagnosis or problem], with documented differential considerations of [supplied differential]`

Do not create a differential, etiology, or supporting rationale. If the diagnosis remains uncertain, a symptom, abnormal finding, or functional problem may be used only when it is already documented as the problem.

### Plans

Use these subsections and number each independently. Include only supplied actions; do not pad lists.

#### Diagnostic plans

List ordered or explicitly planned tests, imaging, consultations, and monitoring evaluations.

#### Treatment plans

List documented medications, procedures, therapies, and monitoring parameters.

#### Educational and informed plans

List documented condition explanations, safety measures, shared decisions, consent discussions, or patient/family education. Include standard institutional wording only when the requester confirms it is an authorized plan.

For a plan category with no supplied action, write `1. No plan provided in the source material.`

## Full Admission Note

Use the headings below in this order. Write `Not provided` under a required section that has no source data; do not fabricate normal or negative findings.

### General Data

Include only supplied identifiers and demographics relevant to care: age/date of birth, gender, occupation, marital status, residence region, referral source, information source and reliability, and admission date/time.

### Chief Complaint

State the principal symptom or problem and duration in one concise line.

### Present Illness

Write a chronological narrative following the common drafting rules.

### Past Medical and Surgical History

Include documented diagnoses, onset or duration, treatment and control status, prior hospitalizations, operations, trauma, and relevant institutions or dates.

### Personal and Exposure History

Include supplied tobacco, alcohol, betel nut, occupation, travel, occupation exposure, contact, clustering, vaccination, sexual, developmental, obstetric, or other relevant history. Do not assume that a missing exposure is negative.

### Allergy History

Record the allergen and documented reaction. Write `Not provided` rather than `NKDA` unless no known allergy is explicitly documented.

### Family History

Include relevant familial disease and pedigree information when supplied.

### Psycho-socio-economic Assessment

Include supplied education or health literacy, family function and support, main caregiver, financial or resource concerns, safety, and the patient's or family's understanding and concerns. For children or patients needing a guardian, retain the supplied principal caregiver and psychosocial concerns.

### Review of Systems

Organize documented positives and negatives by system. Do not create a blanket negative review.

### Physical Examination

Record supplied vital signs, height/weight when relevant, mental status, and system findings. The examination should address the complaint and review-of-systems findings while retaining any other documented abnormalities.

### Laboratory and Radiological Results

List admission-relevant results with dates, values, units, and explicit comparison context when supplied.

### Provisional Diagnoses / Impression

List clinician-documented problems in priority order. Preserve uncertainty and include supplied supporting reasoning or differential considerations without adding new ones.

### Initial Plans

Organize the supplied plan into `Diagnostic`, `Therapeutic`, and `Educational and informed` subsections. Add `Consultation` or `Follow-up` only when documented.

## Final check

Confirm internally that every diagnosis, supporting fact, and plan is traceable to the source; required full-note domains are not silently omitted; the chief complaint includes a duration when supplied; and no normal finding, allergy status, recommendation, dose, or timing claim was invented.
