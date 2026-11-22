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

## 2026-11-22 18:03｜ingest｜S02
- 做了什麼：用 curl 下載 Pro Git 2.2 Recording Changes to the Repository，以 tools/html2md.py 轉成 raw/S02-progit-recording-changes.md（HTML 正文與 markdown 皆為 4102 字）；html2md.py 新增提示框（Note、Tip）轉成引用區塊、保留程式碼區塊的語言標記，並修正字數計算；check.py 的年份檢查改為只在「年份早於 published」時警告，CLAUDE.md 第 4-3 節補上對應規則；新增 sources/S02-progit-recording-changes.md（含 git rm、git mv 補充）、concepts/commit.md、git-add.md、git-status.md、gitignore.md、git-diff.md；更新 concepts/three-states.md（已追蹤與未追蹤、狀態循環、指令範例）、index.md、overview.md
- 討論結果：頁面規劃照建議；git-diff.md 留在 wiki、不放進簡報；git commit -a 放常見錯誤；簡報強調用 -m 避免卡在編輯器；年份標註採做法 A（標文中寫明的年份，例如 [S02, 2020]）；master 先照原文保留並依第 4-3 節標註，簡報怎麼處理等 ingest S03 後再決定（已記在 overview.md「簡報範圍決定」的待決事項）；git rm、git mv 只寫在摘要頁、不建概念頁。**資料規劃調整**：教學目標是 commit 與 push，不需要分支，剩下的資料依序為 S03 Pro Git 1.6 First-Time Git Setup、S04 2.1 Getting a Git Repository、S05 2.4 Undoing Things、S06 2.5 Working with Remotes、S07 GitHub Docs personal access tokens（用網址加 .md 下載原文）；原本規劃的分支章節、GitHub Hello World、Git 2.23 部落格文章不做。**規則待修正**：S02 的 Note 指出 Git 本身仍以 master 為預設，只有 GitHub 等平台的新 repository 預設為 main，所以 CLAUDE.md 第 9 節「master 作為預設分支名稱就是過時」的規則寫得太簡化，等 S03 之後連同 check.py 一起修正
- 檢查結果：html2md.py 第一次轉換時，markdown 比 HTML 正文少 9 個字；逐字比對後確認是 git diff 輸出範例中有一行 markdown 連結語法，字數計算誤把它當成連結而扣掉網址，內容沒有遺漏；修正字數計算後兩者皆為 4102 字，轉出內容與修正前相同；以修改後的 html2md.py 重新轉換 S01，輸出與 raw 完全相同。比對字數時 import html2md.py 產生的 tools/__pycache__/ 已刪除。check.py 第一次執行即通過，0 個錯誤、0 個警告；另以暫存資料測試年份早於 published 時仍會警告
- 待找資料：(1) 取消暫存與放棄修改的現行寫法（S02 範例輸出混用 git restore --staged、git reset HEAD、git checkout --，待 S05 確認）；(2) 修改預設分支名稱的方法，以及 Git 本身的預設分支名稱是否仍為 master（待 S03 確認）；(3) S01 待找資料第 3 項的 git switch 不再尋找（不教分支），改由 S05 確認取消暫存、放棄修改的寫法

## 2026-11-22 18:40｜ingest｜S03
- 做了什麼：用 curl 下載 Pro Git 1.6 First-Time Git Setup，以 tools/html2md.py 轉成 raw/S03-progit-first-time-git-setup.md（HTML 正文與 markdown 皆為 1033 字，html2md.py 不需修改）；新增 sources/S03-progit-first-time-git-setup.md、concepts/git-config.md、concepts/default-branch.md（含簡報範例改編為 main 的依據、原因與範圍）；更新 concepts/commit.md（commit 會記錄 user.name 與 user.email、編輯器的預設行為與 Warning、時效註記）、git-status.md、git-add.md、three-states.md（時效註記改連到 default-branch.md）、index.md、overview.md（學習路線加入設定步驟、待決事項改為已決定、S03 的簡報取捨）。修正 CLAUDE.md 第 9 節的 master 規則與 check.py 的提示訊息；CLAUDE.md 第 4-2 節新增「（Sxx 討論）」標註專案教學決定的規則，check.py 不再對有此標註的段落發出「未標註來源」警告
- 討論結果：頁面規劃照建議；年份標註的過時與現行兩行沿用 [S02, 2014]、[S02, 2020]，S03 只標 [S03]；簡報範例輸出改成 main 並註明改編自 S02、依 S03 設定，改編決定先寫進 default-branch.md、簡報再引用該頁，說明「Git 本身預設是 master」的投影片加 data-legacy；第 9 節的 master 規則照建議修正（S02 記錄的「規則寫得太簡化」已處理）；git checkout 規則原本的建議「切換分支請用 git switch」，因為不 ingest Git 2.23 部落格文章（S02 討論的資料規劃調整）而失去來源，建議文字等 S05 之後再改；寫入 wiki、修正規則、commit 之後接著做 lint
- 檢查結果：check.py 第一次執行有 3 個錯誤、4 個警告：3 個錯誤是 index.md 尚未登記新頁面（當時還沒更新 index.md），4 個警告是 default-branch.md 中的專案決定段落沒有 [Sxx] 標註；決定段落加上「（S03 討論）」並修改 check.py、更新 index.md 後重跑，0 個錯誤、0 個警告
- 待找資料：(1) GitHub 的 email 隱私設定（commit 會永久記錄 email，push 到 GitHub 後別人看得到），S07 之後視時間決定要不要補一篇；(2) 「Git 本身預設是 master」是否仍成立（S02、S03 都沒有寫年份更新的確認）；(3) git checkout 規則建議文字的新來源，待 S05

## 2026-11-22 18:42｜lint｜S01–S03
- 做了什麼：依第 8 節檢查 S01～S03 的 16 個 wiki 頁面。check.py 自動檢查（孤立頁面、斷掉的連結、來源標註、index 登記、raw 未被修改）全部通過；另以人工檢查用語、頁面之間的矛盾、事實陳述是否有 raw 依據，以及過時資訊的標註。修正 3 處：(1) S01 摘要頁原本寫「線上版會持續修訂」，S01 原文沒有這個說法，屬於寫入時的推論，改為引用 S02、S03 線上版含 2014 年之後內容的證據 [S02, 2020] [S03]；(2) commit.md、git-status.md、default-branch.md 三處「過時／現行做法」區塊的用字統一；(3) 補上 3 組只有單向的相關頁面連結（git.md → commit.md、three-states.md → git-diff.md、git-status.md → gitignore.md）
- 討論結果：無（lint 結果中需要判斷的項目已列出，等使用者回覆）：(1) 「過時／現行做法」區塊在 commit.md、git-status.md、default-branch.md 重複出現三次，之後修改容易漏改，是否只保留在 default-branch.md、其他兩頁改成連結；(2) CLAUDE.md 第 4-3 節的範例引用 [S03, 2014]（git checkout）與 [S06, 2019]（git switch），但實際的 S03 是 1.6 First-Time Git Setup，S06 規劃為 2.5 Working with Remotes，而且不教分支，範例容易誤導，是否改寫
- 檢查結果：用語掃描未發現非台灣用語，「工作目錄」譯名一致；頁面之間沒有互相矛盾的說法；抽查 16 個事實陳述，都能在標註的 raw 中找到對應原文；master 已依第 4-3 節標註；SHA-1、RCS 等有時效性的說法已寫在時效註記；S02 範例輸出中的 git reset HEAD、git checkout -- 因為還沒有現行做法的來源，未使用第 4-3 節格式，已註明待 S05 確認。修正後 check.py 通過，0 個錯誤、0 個警告
- 待找資料：彙整目前仍待處理的項目：(1) push 到 GitHub 的指令（S01 待找資料第 1 項，status、add、commit 已由 S02 補上），待 S06；(2) 現行 Git 的雜湊演算法是否仍只有 SHA-1（S01），目前沒有規劃來源；(3) 取消暫存與放棄修改的現行寫法（S02），待 S05；(4) 「Git 本身預設是 master」是否仍成立（S02、S03），目前沒有規劃來源；(5) git checkout 規則建議文字的新來源（S03），待 S05；(6) GitHub 的 email 隱私設定（S03），S07 之後視時間決定

## 2026-11-22 18:46｜fix｜lint 後續修正
- 做了什麼：「過時／現行做法」區塊只保留在 concepts/default-branch.md，commit.md 與 git-status.md 改成一行連結；CLAUDE.md 第 4-3 節的範例改用本專案實際的 master 與 main 例子，並補充「同一組過時／現行做法只寫在一個概念頁」；default-branch.md 與 overview.md 記錄「Git 本身預設是 master」在簡報中的寫法；CLAUDE.md 第 4-2 節與 check.py 的決定標註擴充為「（Sxx 討論）」或「（lint 討論）」
- 討論結果：使用者同意 lint 提出的兩項修改；「（S03 討論）」標註規則保留；兩項沒有規劃來源的待找資料（SHA-1 的現況、Git 本身預設是否仍為 master）不另外找來源，簡報如果要提到 Git 預設是 master，寫成「依 Pro Git 線上版，2026-11-22 擷取」
- 檢查結果：check.py 通過，0 個錯誤、0 個警告
- 待找資料：無（lint 彙整的第 2、4 項依使用者決定不再尋找）
