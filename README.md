# TSGH Clinical Notes for ChatGPT and Codex

TSGH 格式的住院病歷草稿外掛，版本 **0.1.2**。包含六個 skills：clinical-note（格式分流）、Admission、Progress、Weekly、Discharge、Operation；也支援中文 B/P/Sc/Sp/E/P/D 全人照護評估。

**分享給同事：**先看 [中文安裝說明](安裝說明.md)，或到 [Releases 下載完整外掛 ZIP](https://github.com/wenguic39-creator/tsgh-clinical-notes/releases/latest)。GitHub 的 **Code > Download ZIP** 是整份原始碼，不能直接當作單一外掛上傳。

![TSGH Clinical Notes cover](plugins/tsgh-clinical-notes/assets/logo.png)

## Choose an installation route

| Environment | Installation route | Requirements |
| --- | --- | --- |
| ChatGPT personal account | Download the release ZIP and ask Plugin Creator to save it as your own private plugin | Plugin creation must be available to the account |
| ChatGPT managed workspace | An administrator imports this repository as a marketplace, or uploads the release ZIP | Workspace upload/import and installation permissions |
| Codex | Register the repository marketplace, then install `tsgh-clinical-notes@tsgh-team` | A client that supports plugin marketplaces |

This is an instruction-only package: no MCP server, API key, desktop process, or separately hosted service is required. Web use does not require the author's computer to be online. Availability in ChatGPT web, desktop, and mobile depends on the account, workspace, and product surface; each surface has not been independently tested. A GitHub link alone does not install the plugin or grant access to the author's private copy. This repository is not an OpenAI public-directory listing.

### Personal ChatGPT account

Download `tsgh-clinical-notes-0.1.2.zip` from Releases. In an account with Plugin Creator available, attach the ZIP and ask:

> Save this tsgh-clinical-notes package as my private plugin. Preserve all six skills, references, and assets. If an editable copy already exists, verify its identity and update it without changing its sharing.

Open the returned plugin link and install if prompted. Start a new supported chat, select `@TSGH Clinical Notes`, and supply the note type and permitted source facts. If creation is unavailable, check the account's permissions; cloning the repository will not enable it.

### Managed ChatGPT workspace

An administrator opens **Admin Console > Plugins > Add > Import marketplace**:

- Source: `https://github.com/wenguic39-creator/tsgh-clinical-notes`
- Path: empty; the repository contains `.agents/plugins/marketplace.json`
- Branch: `main` for updates, or `v0.1.2` to pin the release

Review import results and workspace installation settings. Members then install the plugin from the workspace directory. GitHub-managed copies can receive updates through marketplace sync; manually uploaded personal copies need a separate update.

### Codex

Clone or download the **whole repository**, then register its marketplace:

```powershell
codex plugin marketplace add "<full path to this repository>"
codex plugin add tsgh-clinical-notes@tsgh-team
```

Start a new task after installation. These are Codex CLI commands, not commands to paste into an ordinary ChatGPT conversation. If the installed client has different commands, consult `codex plugin --help`.

## Try it

Select the installed plugin and ask for a `SOAP progress note`, an `Admission Note`, or a `全人照護評估`, followed by authorized source facts. Ordinary SOAP stays non-POMR; numbered problems require an explicit request. Review every draft before use.

## Build and release

Python 3.10+; no third-party packages are needed:

```powershell
python scripts/package_plugin.py --check
python scripts/package_plugin.py
```

The deterministic build validates manifests, six skills, assets, and relative references. It exports `dist/tsgh-clinical-notes-0.1.2.zip` and `dist/SHA256SUMS`, including hidden compatibility files. It does not prove successful installation or clinical drafting in every host.

GitHub Actions validates pull requests and builds artifacts. After a merge to `main`, it publishes a missing version as a GitHub Release with the ZIP, checksum, and matching notes from `releases/v<version>.md`. Existing releases are left intact. For future releases, synchronize both manifests, add release notes, and review the changes before merging.

## Data handling

Use only authorized, minimum-necessary clinical data. Do not put patient records or identifiers in public issues, pull requests, or repository files. Web processing may occur in the cloud; follow institutional policy for the selected host. All output requires clinician review. The existing artwork contains Tri-Service General Hospital identity elements; verify authorization before reusing those elements.

## Official references

- [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256)
- [GitHub marketplace import and sync](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github)
- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
