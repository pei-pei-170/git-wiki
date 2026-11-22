# 操作紀錄

本檔案只能往後新增，不可刪改舊紀錄。每筆紀錄的格式與操作類型見 CLAUDE.md 第 7 節。

## 2026-11-22 17:03｜setup｜建立專案結構
- 做了什麼：依第 2 節建立 raw/、wiki/sources/、wiki/concepts/、slides/、tools/ 資料夾，wiki/index.md、wiki/overview.md、wiki/log.md 的空白版本，以及 tools/check.py（當時 setup 類型尚未存在，本筆於 17:42 補記）
- 討論結果：以 hw10/ 作為 git-wiki/ 根目錄；README.md、根目錄 index.html、slides/ 內的檔案暫不建立
- 檢查結果：check.py 通過；另用兩組測試資料驗證，故意寫錯的一組抓到 44 個錯誤、5 個警告，全部正確的一組 0 個錯誤、0 個警告
- 待找資料：無

## 2026-11-22 17:42｜setup｜規則調整與 git init
- 做了什麼：CLAUDE.md 新增 setup 操作類型（第 7 節）、stored: full 須以 curl 下載並用程式轉檔的規則與一篇多網址的 url 寫法（第 3 節）、ingest 最後依第 11 節 commit（第 5 節）、check.py 的兩項新檢查（第 9 節）；check.py 新增 setup 類型與「已 commit 的 raw 檔案被修改、刪除、改名」檢查；新增 tools/html2md.py 與 .gitattributes（統一 LF 換行，避免 raw 在 Windows 上被轉成 CRLF）；執行 git init（分支 main）
- 討論結果：使用者決定新增 setup 類型、curl 規則、git init 與 raw 修改檢查，檢查通過後 commit
- 檢查結果：check.py 通過（以這次 commit 的內容檢查）；raw 修改檢查另用暫存 repository 測試「未 commit 的修改」「已 commit 的修改」「刪除」三種情況，皆回報錯誤
- 待找資料：無

## 2026-11-22 17:46｜ingest｜S01
- 做了什麼：用 curl 下載 Pro Git 1.1 About Version Control 與 1.3 What is Git?，以 tools/html2md.py 轉成 raw/S01-progit-version-control-and-what-is-git.md（1.1 有 806 字、1.3 有 1373 字，轉換前 HTML 正文與轉換後 markdown 字數一致）；新增 sources/S01-progit-version-control-and-what-is-git.md、concepts/version-control.md、concepts/git.md、concepts/three-states.md；更新 index.md、overview.md（含「簡報範圍決定」）
- 討論結果：三個概念頁照規劃建立，three-states.md 寫得最完整；三種版本控制類型在概念頁保留，簡報只用一句話對比集中式與分散式，本地版本控制不放；「複製資料夾加上日期」的痛點當簡報開場；SHA-1、index、RCS 不放進簡報；commit.md 等 S02 再建立；原文的 check out 是一般動詞，記在 three-states.md 的「新手常見誤解」
- 檢查結果：轉檔程式第一次執行時，因終端機 cp950 編碼無法輸出 U+2009 字元而中斷（markdown 檔已完整寫出），修正輸出編碼後重跑，結果與第一次相同。check.py 第一次執行通過但有 9 個警告，全是 ### 小標題被誤判為「未標註來源的段落」，屬於 check.py 的錯誤；修正 check.py（小標題視為段落分隔）後重跑，0 個錯誤、0 個警告
- 待找資料：(1) 修改、暫存、commit 與 push 到 GitHub 的實際指令（S01 沒有任何指令範例）；(2) 現行 Git 使用的雜湊演算法是否仍只有 SHA-1（S01 為 2014 年的描述）；(3) git checkout 與 git switch 的說明，用來在簡報中區分一般動詞 check out 與指令
