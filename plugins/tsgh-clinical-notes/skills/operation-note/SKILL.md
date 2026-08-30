---
name: operation-note
description: Draft a TSGH-aligned English Operation Note from clinician-supplied operative facts. Use for surgical or procedural documentation covering indication, findings, critical steps, specimens or implants, blood loss, complications, closure, and postoperative condition.
---

# Operation Note

Create a complete, concise English Operation Note that reflects what actually occurred. Treat it as a clinician-review draft, not a signed operative record.

## Input gate and safety

- Use only supplied records the requester is authorized to handle and only the minimum necessary identifiers.
- Do not invent or infer a time-out, consent, diagnosis, finding, maneuver, anatomy, device, specimen, blood loss, complication, count, closure method, postoperative order, or patient condition.
- Preserve exact laterality, anatomy, dates/times, procedure and device names, dimensions, quantities, medication details, estimated blood loss, urine output, and uncertainty. Keep every supplied unit directly beside its measured value; never drop, convert, or guess a unit.
- Never write `Not provided`, `None provided`, or a missing-data placeholder inside the operative record. Keep missing critical elements and possible verification or further-evaluation prompts in a clearly separated `Physician considerations — outside the medical record` section after the note.
- Distinguish preoperative diagnosis, postoperative diagnosis, indication, findings, and procedure. Do not make them interchangeable.
- Do not independently recommend operative technique, antibiotics, thromboprophylaxis, drains, monitoring, or postoperative care.
- Keep data local and treat the result as requiring surgeon review and sign-off.

## Output modes

- Default to **Copy mode**: output the completed Operation Note first. Append an outside-record physician-considerations section only when a missing critical element, conflict, or ambiguous unit needs attention.
- Use **Review mode** only when requested: output the note, followed by the same outside-record section for missing critical elements, laterality or count conflicts, ambiguous timing/anatomy/device details, unexplained diagnosis changes, and statements requiring verification.

## Drafting workflow

1. Identify patient and record identifiers, operation date/time, urgency, operators, anesthesia, preoperative diagnosis, postoperative diagnosis, and exact procedure title when supplied.
2. Establish the indication and brief relevant history without copying the full admission history.
3. Reconstruct the sequence from time-out, positioning, preparation, incision/approach, exposure, key maneuvers, findings, specimens or implants, hemostasis, irrigation, closure, dressing, debriefing, and transport only to the extent documented.
4. Retain critical anatomy encountered, pathology and anatomic variants, structures protected, technique and material used, prostheses or implants, and unexpected complications.
5. State where specimens were sent and how they were labeled only when supplied. If the same procedure was performed on the contralateral side or repeated, abbreviate by reference only when the source confirms it was carried out identically.
6. Record postoperative condition and destination separately from postoperative instructions.

## Required output

Use the headings below in this order. Leave a missing required item blank and identify it only outside the medical record; never convert silence into `none`, `normal`, or `without complication`. A possible examination, test, monitoring step, or consultation may appear only as a neutral physician consideration, never as an operative or postoperative order unless supplied.

### Date and Time

### Elective / Emergency Status

### Preoperative Diagnosis

### Postoperative Diagnosis

Preserve the documented difference from the preoperative diagnosis. Do not copy it automatically.

### Procedure Performed

Use the exact procedure name, laterality, site, and major approach.

### Surgeon and Assistants

### Anesthesia

Include type and named anesthesia personnel when supplied.

### Indication

Give a concise supplied reason for the operation and relevant history.

### Positioning, Preparation, and Time-out

Record only documented positioning, preparation/draping, prophylaxis, inserted tubes or lines, and safety check.

### Incision and Approach

Include location, length, approach, and local anesthetic when supplied.

### Operative Findings

Describe key pathology, anatomy, variants, and unexpected findings.

### Procedure Details

Describe the operation step by step from exposure through completion. Include critical steps, adjacent critical structures, dissection or mobilization, techniques and equipment, tissue excised, reconstruction, hemostasis, irrigation, and any unexpected event when supplied.

### Specimens

Record tissue or fluid, labeling, and destination. Use `No specimen submitted` only when explicitly documented.

### Implants / Prostheses

Include type, manufacturer, model, size, serial or lot information, and location when supplied. Use `None` only when explicitly documented.

### Estimated Blood Loss and Urine Output

Preserve documented amounts and units. Do not estimate a missing value.

### Drains, Tubes, and Packing

Include type, size, number, and location when supplied.

### Complications

Describe documented complications and management. Use `None` or `No immediate complication` only when explicitly documented.

### Closure and Dressing

State structures or layers closed in order, closure material and technique, final wound management, and dressing when supplied.

### Counts / Debriefing

Record count and debriefing status only when explicitly documented.

### Postoperative Condition and Disposition

State documented condition, ventilation or device status when relevant, and transport destination such as PACU, ICU, or ward.

### Postoperative Instructions

List only surgeon-documented care instructions, monitoring, antibiotics, thromboprophylaxis, activity, diet, drains, imaging, or laboratory follow-up.

### Signature

Retain supplied author/operator identity. Otherwise leave `[surgeon signature]` for manual completion.

## Style and completeness

- Use past tense for performed steps and exact surgical terminology.
- Be concise without omitting critical steps, complications, implants, specimens, or closure details.
- Do not use a copied template statement unless the record confirms it for this operation.
- If operative images are supplied and their inclusion is requested, preserve their documented site, orientation, and annotation; do not infer anatomy from an unverified image alone.

## Final check

Confirm internally that laterality and procedure names are consistent; preoperative and postoperative diagnoses are independently sourced; critical steps, specimens, implants, blood loss, complications, closure, and destination are not assumed; and every operative statement is traceable to the supplied record.
