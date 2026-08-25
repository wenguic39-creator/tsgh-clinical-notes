# TSGH Clinical Notes for Codex

TSGH-aligned English inpatient clinical-documentation workflows packaged as a Codex plugin. It includes Admission, Progress, Weekly, Discharge, and Operation Note skills.

![TSGH Clinical Notes cover](plugins/tsgh-clinical-notes/assets/logo.png)

## Install

Clone or download this repository, then run:

```powershell
codex plugin marketplace add "<full path to this repository>"
codex plugin add tsgh-clinical-notes@tsgh-team
```

Open a new Codex task after installation.

## Clinical safety

- Use only authorized, minimum-necessary, and appropriately de-identified clinical information.
- Do not place patient names, national identifiers, medical-record numbers, or other identifying information in public tasks.
- Every generated note is a draft and requires review by a qualified clinician before entry into the medical record.
- The cover includes Tri-Service General Hospital identity elements. Confirm institutional brand authorization before redistribution or reuse outside the intended setting.

完整中文說明請見 [安裝說明.md](安裝說明.md)。
