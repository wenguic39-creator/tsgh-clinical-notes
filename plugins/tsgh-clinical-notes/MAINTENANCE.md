# 病歷 skills 維護來源

## 2026-10-03：GitHub 與 ChatGPT 套件

本 repository 的維護來源是 `plugins/tsgh-clinical-notes`；根目錄 `plugin.json`
使用 Agent Plugins 1.0，`.codex-plugin/plugin.json` 保留 Codex 相容格式。
兩者版本與展示設定必須一致。

0.1.2 以既有私人帳號 0.1.1 的通用 manifest 為基礎；檢查時帳號版與
GitHub 版的全部 skills 和參考檔文字一致。保留六個 skills、病歷格式與
臨床事實規則，只將執行環境說明改為適用於獲准的 ChatGPT／Codex session。
網頁版可在雲端執行，不承諾資料只在本機處理；不追加搜尋或外部服務。

從 repository 根目錄執行 `python scripts/package_plugin.py` 驗證並產生
`dist/tsgh-clinical-notes-0.1.2.zip`，包含隱藏的相容 manifest 與既有資產。
GitHub marketplace 保持 `tsgh-team` 名稱。個人帳號更新與 GitHub 工作區
同步是不同的發佈路徑；GitHub push 本身不會更新手動上傳的私人外掛。
完整安裝與驗證說明見 repository 根目錄 `安裝說明.md`。

## 2026-09-06：本機来源整理歷史

統一日期：2026-09-06。

唯一維護來源：`C:\Users\USER\plugins\tsgh-clinical-notes`。
日常使用入口：已安裝的 `tsgh-clinical-notes@personal` plugin。

涵蓋 clinical-note、admission-summary、progress-note、weekly-summary、
discharge-summary、operation-note 六個 skills。

選用此來源的依據：整理前 plugin 原始碼與已安裝版本的全部 15 個檔案
完全一致，且保留後續加入的病歷格式、原始單位、缺失資料與病歷外
醫師提醒規則。六份 standalone skills 與 plugin 有文字差異，因此封存
standalone 版本；本次不重新合併或改寫臨床輸出規則。

舊版與更新前 plugin 備份存放於：
`C:\Users\USER\Documents\Codex\Skill Archives\tsgh-clinical-notes\2026-09-06-source-unification`。
其中 `standalone` 為原六份獨立 skills，`plugin-before` 為更新前原始碼。
這些是歷史備份，不是日常維護入口。

未來更新只修改唯一維護來源；驗證後刷新版本並重新安裝 plugin。
`.codex/plugins/cache` 是安裝產物，不直接編輯；也不再另建六份
standalone skills。具體維護規則見同目錄 AGENTS.md。

回復時先保存目前版本，再由維護者比較備份並選擇一個正式來源；若需要
完整撤回本次整理，可將 standalone 子目錄中的六份 skill 移回原本
`.codex/skills`，並由 plugin-before 還原原始碼後依正式流程重新安裝。
完整撤回會恢復整理前的重複入口，不能視為正常更新方式。

本次只做本機來源整理，未發布或推送任何遠端版本。
