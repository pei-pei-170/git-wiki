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

## 2026-11-22 19:17｜ingest｜S04
- 做了什麼：用 curl 下載 Pro Git 2.1 Getting a Git Repository，以 tools/html2md.py 轉成 raw/S04-progit-getting-a-git-repository.md（HTML 正文與 markdown 皆為 759 字，html2md.py 不需修改）。新增 sources/S04-progit-getting-a-git-repository.md、concepts/repository.md、git-init.md、git-clone.md。更新 three-states.md（Git 目錄就是 .git 子資料夾、S04 的 check out 一般動詞例子）、version-control.md（S04 對完整副本的佐證）、commit.md（第一次 commit 的連結）、git-status.md（連到 git clone）、index.md、overview.md（學習路線、S04 的簡報取捨、push 路線的待決事項）。另外新增分號寫作規則：CLAUDE.md 第 1 節與第 9 節、check.py 新增全形分號檢查（wiki 頁面、slides/outline.md、簡報內文、log.md 中 2026-11-22 19:13 之後的紀錄，程式碼除外）
- 討論結果：repository 另外建一頁 repository.md，git-init.md 連過去。簡報的 commit 訊息一律用雙引號，理由是與 S02 的範例一致。push 到 GitHub 的路線記成待決事項，等 S06 後再決定。使用者新增寫作規則：wiki、簡報、log.md 的中文不使用全形分號，改用句號分成兩句或用逗號連接，raw、程式碼區塊與指令不適用
- 檢查結果：寫入 S04 頁面後 check.py 通過。分號規則與 log.md「不可刪改舊紀錄」衝突，因此 log.md 的舊紀錄維持原樣，check.py 只檢查 2026-11-22 19:13 之後的紀錄。現有 wiki 頁面共 108 個分號（15 個舊頁面 107 個，加上新寫的 repository.md 連結文字 1 個），逐行決定改成句號、逗號或頓號後以程式替換，替換前核對每一行的數量，程式碼與行內程式碼不動。S01 的頁面標題原本用分號分隔兩節，改成頓號，所有連到 S01 的連結文字一併更新。逐行檢查時另外修正兩處：S02 摘要頁的連結仍指向 git-status.md 的時效註記（該區塊已在上一筆 fix 移到 default-branch.md），改連 default-branch.md。version-control.md 的相關頁面把 Git 寫成「最常見的」分散式版本控制系統，raw 沒有依據，改成「一種」。另用暫存資料測試分號檢查，正文、大綱、新紀錄、投影片內文都會報錯，行內程式碼、程式碼區塊、投影片的 pre 與舊紀錄不會。最後 check.py 通過，0 個錯誤、0 個警告
- 待找資料：無

## 2026-11-22 19:22｜setup｜ingest 流程加入逐句核對
- 做了什麼：CLAUDE.md 第 5 節在「寫入 wiki」之後新增第 4 步「逐句核對」，原本的第 4～6 步改為第 5～7 步。寫入 wiki 後，把這次新增或修改的每一句事實陳述對照 raw 列出對應的英文原句，找不到原句的句子要刪除或改寫，並在回報中列出被刪改的句子，核對幾句、刪改幾句記進該筆 log 的「檢查結果」
- 討論結果：使用者要求把檢查往前移到寫入當下。原因是寫入時加入了原文沒有的說法，而且兩次都是事後才發現。第 1 次是 S01 摘要頁的「線上版會持續修訂」，在 S01–S03 的 lint 發現。第 2 次是 version-control.md 相關頁面中「最常見的」分散式版本控制系統，在 S04 修改分號時逐行檢查發現
- 檢查結果：check.py 通過，0 個錯誤、0 個警告
- 待找資料：無

## 2026-11-22 19:31｜ingest｜S05
- 做了什麼：用 curl 下載 Pro Git 2.4 Undoing Things，以 tools/html2md.py 轉成 raw/S05-progit-undoing-things.md（HTML 正文與 markdown 皆為 1463 字）。html2md.py 改為把 h4 標題轉成 ####（原本會轉成與 h3 同級的 ###），以 S02 回歸測試輸出與 raw 完全相同。新增 sources/S05-progit-undoing-things.md、concepts/git-restore.md（過時／現行做法區塊只寫在這頁）。更新 commit.md（新增 --amend 段落）、git-status.md（新增 Git 2.23.0 起的輸出範例，時效註記改連到 git-restore.md）、git-add.md（時效註記改連到 git-restore.md）、git.md（commit 過的幾乎都能救回）、index.md、overview.md（學習路線、S05 的簡報取捨）。CLAUDE.md 第 4-3 節與 check.py 允許用版本號代替年份。CLAUDE.md 第 9 節與 check.py 的過時用語清單新增 git reset HEAD，git checkout 的建議文字改成用 git restore（依 S05）
- 討論結果：頁面規劃照建議，--amend 放在 commit.md。原文只寫版本時，用版本號代替年份，寫成 [S05, Git 2.23.0]。git reset HEAD 加進過時用語清單，git checkout 規則的建議文字改成用 git restore（S03 記錄的「建議文字失去來源」已處理）。簡報中 git status 的範例改用 S05 新版段落的輸出，分支名稱依 default-branch.md 改成 main
- 檢查結果：依第 5 節第 4 步逐句核對，本輪新增或修改的事實陳述 52 句，另順帶核對上一輪 S03 摘要頁的 2 句，共 54 句。每句對照 raw 列出英文原句，並以程式確認原句逐字存在於標註的 raw 檔。找不到原句、刪改 4 句：(1) S05 摘要頁重點 2「它會用新的 commit 完全取代舊的，所以只能用在還沒 push 的 commit」，原文沒有寫「所以」的因果關係，改寫成兩個獨立的句子。(2) S05 摘要頁年份「線上版已修訂，包含 Git 2.23.0 新增的 git restore」，原文沒有說 Git 2.23.0 晚於印刷版，刪除。(3) S03 摘要頁年份「線上版已修訂，包含 Git 2.28 之後才有的預設分支設定」，同樣是推論，刪除。(4) S03 摘要頁「線上版加入 Git 2.28 的內容」，「加入」暗示是後來才加的，改寫成「原文提到 Git 2.28，但沒有寫年份」。S02 摘要頁的「線上版已修訂，包含 2020 年中之後才寫的 Note」有原文的 mid-2020 可以推得，保留。check.py 通過，0 個錯誤、0 個警告
- 待找資料：無（S02 待找資料第 1 項「取消暫存與放棄修改的現行寫法」已由 S05 解決，S03 待找資料第 3 項「git checkout 規則建議文字的新來源」也已由 S05 解決）

## 2026-11-22 19:47｜setup｜逐句核對工具與資料清單調整
- 做了什麼：新增 tools/verify_quotes.py，驗證 checks/Sxx-quotes.md 中的每一句英文原句都逐字存在於標註的 raw，找不到原句卻沒寫處理方式時也會報錯。把 S05 的對照表從暫存資料夾移進專案，轉成 checks/S05-quotes.md（56 筆，即核對的 54 句加上改寫後的 2 句），以 verify_quotes.py 驗證通過。另用暫存資料測試，改錯的原句與缺少處理方式都會報錯。CLAUDE.md 第 2 節結構圖新增 checks/ 與 tools/verify_quotes.py，第 5 節第 4 步改為產生 checks/Sxx-quotes.md 並用這支程式驗證。overview.md 的待 ingest 清單依新規劃更新
- 討論結果：使用者要求對照表放在 checks/，不放在 wiki/ 裡，核對程式整理成可重複使用的工具，之後每次 ingest 都產生 checks/Sxx-quotes.md 並驗證。資料清單調整：S06 照原本的 Pro Git 2.5 Working with Remotes。S07 改成 GitHub Docs〈Adding locally hosted code to GitHub〉，原因是目前沒有資料說明如何在 GitHub 建立 repository 並推上去。personal access token 改成 S08。GitHub email 隱私是否補一篇，改為 S08 之後再決定。--amend 和編輯器的矛盾等規劃大綱時再決定
- 檢查結果：verify_quotes.py 驗證 checks/S05-quotes.md 通過。check.py 通過，0 個錯誤、0 個警告
- 待找資料：無

## 2026-11-22 20:03｜ingest｜S06
- 做了什麼：用 curl 下載 Pro Git 2.5 Working with Remotes，以 tools/html2md.py 轉成 raw/S06-progit-working-with-remotes.md（HTML 正文與 markdown 皆為 1729 字，html2md.py 不需修改）。新增 sources/S06-progit-working-with-remotes.md（含 fetch、pull 與 git remote show、rename、remove 的補充）、concepts/remote.md、concepts/git-push.md。更新 git-clone.md（clone 會自動加上 origin 並設定追蹤）、commit.md（amend 連到 git push）、default-branch.md（改編範圍擴大成範例指令與輸出、S06 的佐證、S07 的待補依據）、index.md、overview.md（學習路線、S06 的簡報取捨、push 路線延到 S07 後決定）。產生 checks/S06-quotes.md
- 討論結果：fetch 和 pull 只寫在摘要頁，不建概念頁，比照 git rm、git mv。default-branch.md 的改編範圍擴大成「範例指令與輸出」，S07 的文件本身用 git push origin main，ingest S07 後補上作為直接依據。push 被拒絕時，簡報只用一句話說明需要先取得別人的更新，不教合併。push 路線延到 S07 之後決定
- 檢查結果：依第 5 節第 4 步逐句核對 60 句，以 tools/verify_quotes.py 驗證 checks/S06-quotes.md，60 句都找到原句，刪改 0 句。另外，ingest 討論時曾說「S06 說 clone 會自動加上 origin，和 S04 一致」，但 S04 沒有提到 origin，寫入摘要頁時已改寫成「S06 補充了 S04 沒有提到的部分」，沒有寫進 wiki。check.py 通過，0 個錯誤、0 個警告
- 待找資料：push 到 GitHub 時的身分驗證（S06 沒有說明），待 S08

## 2026-11-22 20:11｜ingest｜S07
- 做了什麼：用 curl 下載 GitHub Docs〈Adding locally hosted code to GitHub〉的 .md 原文，新增 tools/md2raw.py，只加上資訊區塊與網址註解，內容不做任何刪改，存成 raw/S07-github-adding-locally-hosted-code.md（原文與存檔正文皆為 2084 字，內容完全相同，字數含 svg 圖示中的座標數字）。CLAUDE.md 第 2 節加入 md2raw.py，第 3 節加入 markdown 原文的存檔規則。新增 sources/S07-github-adding-locally-hosted-code.md、concepts/push-to-github.md。更新 default-branch.md（S07 作為 git push origin main 的直接依據、與 S03 說法不一致、簡報的設定方法）、git-init.md、remote.md、git-push.md、git-restore.md、git-add.md、commit.md、index.md、overview.md（push 路線改為已決定、S07 的簡報取捨）。產生 checks/S07-quotes.md
- 討論結果：新增 push-to-github.md 作為完整流程。S07 與 S03 對預設分支的說法都保留並註明不一致。簡報教 git config --global init.defaultBranch main，git init -b main 只留在 wiki。簡報用 git push origin main，不加 -u，wiki 記錄 macOS 段落的寫法不同。push 到 GitHub 採用路線 A，overview.md 的待決事項標成已決定。同意新增 tools/md2raw.py 並更新 CLAUDE.md
- 檢查結果：依第 5 節第 4 步逐句核對 54 句，以 tools/verify_quotes.py 驗證 checks/S07-quotes.md，54 句都找到原句，刪改 0 句。另外，寫完摘要頁後發現資訊區塊的時效風險說明「GitHub 的介面與建議做法可能改版」是推測，在建立對照表之前已改寫成「網頁沒有標示年份，無法判斷內容寫於何時」，這句屬於後設資訊，不列入對照表。check.py 通過，0 個錯誤、0 個警告
- 待找資料：push 到 GitHub 前的身分驗證方式（S07 只說必須先驗證），待 S08

## 2026-11-22 20:19｜ingest｜S08
- 做了什麼：用 curl 下載 GitHub Docs〈Managing your personal access tokens〉的 .md 原文，以 tools/md2raw.py 存成 raw/S08-github-personal-access-tokens.md（原文與存檔正文皆為 6459 字，內容完全相同，字數含 svg 圖示中的座標數字）。新增 sources/S08-github-personal-access-tokens.md、concepts/personal-access-token.md。更新 git-push.md、push-to-github.md（身分驗證接上 PAT）、remote.md（PAT 只能用在 HTTPS）、index.md、overview.md（學習路線、S08 的簡報取捨、待 ingest 清單）。修改 CLAUDE.md 第 9 節與 check.py 的「用帳號密碼推送」規則。產生 checks/S08-quotes.md
- 討論結果：頁面規劃照建議。「用帳號密碼推送」規則的建議文字改成「命令列透過 HTTPS 驗證時，輸入 personal access token 代替密碼 [S08]」，拿掉 SSH。另外補一篇 S09（GitHub Changelog〈Git password authentication is shutting down〉，stored 用 excerpt），作為「GitHub 已不接受密碼」的來源。password 規則改成同一張投影片出現 token 時不報錯。GitHub email 隱私不補資料，在待找資料標記為「已知但本專案不涵蓋」。lint 等 S09 寫入後再做，範圍是 S04 到 S09
- 檢查結果：依第 5 節第 4 步逐句核對 52 句，以 tools/verify_quotes.py 驗證 checks/S08-quotes.md，52 句都找到原句，刪改 0 句。**規則本身含有沒來源的知識**：CLAUDE.md 第 9 節「用帳號密碼推送到 GitHub 是過時用語（需改用 personal access token 或 SSH）」這條規則，是在建立專案時就寫好的，它的依據（GitHub 已不接受密碼、可以改用 SSH）從來沒有 ingest 進 wiki。S08 只說 PAT 可以代替密碼，沒有說密碼已不能用，也沒有說明 SSH，等於規則本身含有沒來源的知識。這次拿掉「或 SSH」，「GitHub 已不接受密碼」改由 S09 補上來源。**password 規則的誤判**：原本的規則只要投影片文字出現 password 或「GitHub 密碼」等字樣就報錯，但 S08 的現行做法就是在「Password:」提示輸入 token，範例輸出本身就有 Password 這個字，照這個做法寫的投影片會被誤判成過時用語。誤判的原因是規則只比對字面，沒有區分「用密碼推送」和「在密碼提示輸入 token」。修改後，同一張投影片也出現 token 時不報錯，並用暫存資料測試：只寫「GitHub 密碼」的投影片會報錯，寫「Password: 提示時貼上 personal access token」的投影片不會。check.py 通過，0 個錯誤、0 個警告
- 待找資料：(1) 「GitHub 已不接受密碼」的來源，待 S09。(2) GitHub 的 email 隱私設定：已知但本專案不涵蓋

## 2026-11-22 21:02｜ingest｜S09
- 做了什麼：用 curl 下載 GitHub Changelog〈Git password authentication is shutting down〉並完整讀過（下載的檔案只放在暫存資料夾）。依第 3 節存成 excerpt：raw/S09-github-changelog-password-auth-shutdown.md 只保存連結、發布日期、2 個引用片段與 3 點自己的摘要，正文 988 字元。新增 sources/S09-github-changelog-password-auth-shutdown.md。更新 personal-access-token.md（新增「為什麼不能用密碼」與第 4-3 節的過時／現行做法區塊，提到 SSH key 也是其中一種方式）、git-push.md、push-to-github.md（時效註記連到 PAT 頁）、index.md、overview.md。CLAUDE.md 第 9 節與 check.py 的「用帳號密碼推送」規則，改為標註 [S09, 2021]。產生 checks/S09-quotes.md
- 討論結果：原文正文只有兩句重點，整句引用等於貼上幾乎全文，所以 excerpt 只引用兩個關鍵片段，使用者同意。頁面規劃照建議，不新增概念頁。過時用語規則不恢復「或 SSH」，只在 PAT 頁提一句 SSH key 也是其中一種方式。raw 的 license 欄位原本寫「未標示（GitHub Blog，非 CC 授權）」，使用者指出網頁上只是沒有標示授權，不能確定是哪一種，改成「未標示」（raw 當時還沒 commit，修改不違反規則）
- 檢查結果：依第 5 節第 4 步逐句核對 15 句，以 tools/verify_quotes.py 驗證 checks/S09-quotes.md，15 句都找到原句，刪改 0 句。check.py 通過，0 個錯誤、0 個警告
- 待找資料：無（「GitHub 已不接受密碼」的來源已由 S09 補上）

## 2026-11-22 21:03｜lint｜S04–S09
- 做了什麼：依第 8 節檢查 S04～S09 相關的 wiki 頁面（全 wiki 共 30 頁）。自動檢查：check.py（孤立頁面、斷掉的連結、來源標註、index 登記、分號、raw 未被修改）通過，tools/verify_quotes.py 驗證 checks/ 中 S05～S09 的 5 份對照表全部通過（共 237 筆）。另以程式掃描摘要頁與 overview.md 中沒有 [Sxx] 也沒有「（Sxx 討論）」的句子，以及提到 master、git reset HEAD、git checkout --、密碼的概念頁是否連到集中說明的頁面。S04 是在逐句核對流程建立前寫入的，沒有對照表，抽查 15 句 S04 時期的事實陳述，都在 raw 中找到原句。人工檢查頁面之間的矛盾、用語與過時標註。修正 5 處：(1) git-clone.md 提到 master 但沒有連到 default-branch.md，補上連結。(2) git-init.md 直接寫 S03 的「git init 預設建立 master」，沒有提醒與 S07 說法不一致，補上指向 default-branch.md 的說明。(3) push-to-github.md 把 S07 的 current working directory 譯成「目前的工作目錄」，與本 wiki 中 Git 的工作目錄（working tree）撞名，改成「切換到本地專案的資料夾」並加註，checks/S07-quotes.md 第 25 筆的句子一併更新後重新驗證通過。(4) overview.md 的簡報取捨仍寫「如果採用先 git init 的路線」，改成路線 A 已於 S07 決定。(5) overview.md 漏記「--amend 會開啟編輯器，與一律用 -m 的決定矛盾，等規劃大綱時再決定」這個待決事項（原本只記在 log.md），因為規劃大綱時只能讀 wiki，補進「簡報範圍決定」
- 討論結果：無（lint 結果中需要判斷的項目已列出，等使用者回覆）
- 檢查結果：掃描到的其他結果經確認不需修改：overview.md「簡報範圍決定」的引言不是事實陳述。commit.md 的「密碼」出自「不要 commit 密碼或 API key」，講的是敏感資訊，不是用密碼驗證，屬於誤判。三組過時／現行做法區塊各只寫在一頁（default-branch.md、git-restore.md、personal-access-token.md），其他頁面都用連結指過去。頁面之間沒有其他互相矛盾的說法。修正後 check.py 通過，0 個錯誤、0 個警告，verify_quotes.py 通過
- 待找資料：彙整目前狀態：(1) push 到 GitHub 的指令，已由 S02、S06、S07 補上。(2) SHA-1 的現況，依 lint 討論不另外找來源。(3) git checkout 與 git switch，已由 S05 處理，不教分支。(4) Git 本身的預設分支是否仍為 master，依 lint 討論不另外找來源。(5) GitHub 的 email 隱私設定，已知但本專案不涵蓋。(6) 「GitHub 已不接受密碼」的來源，已由 S09 補上。目前沒有待找的資料
