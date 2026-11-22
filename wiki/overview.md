# 總覽：新手學 Git 的完整路線

> 本頁用新手的學習順序，把 `concepts/` 中的概念頁串成一條路線，是規劃簡報大綱的起點。

## 學習路線

1. [版本控制（Version Control）](concepts/version-control.md)：先理解為什麼需要版本控制。很多人用「把檔案複製到加上日期的資料夾」來管理版本，但這很容易出錯。版本控制可以回到先前的版本、比較變化、查出是誰改的、救回遺失的檔案。[S01] 接著認識集中式與分散式的差別：集中式的伺服器是單點故障，分散式的每一份 clone 都是完整備份。[S01]
2. [Git](concepts/git.md)：Git 是分散式版本控制系統，用快照記錄專案。大部分操作都在本地，離線也能 commit。commit 之後的資料很難遺失。[S01]
3. [git config（Git 設定）](concepts/git-config.md)：開始使用前先設定名稱與 email，因為每個 commit 都會永久記錄它們。用 `git config --list` 確認設定。[S03]
4. [預設分支名稱（master 與 main）](concepts/default-branch.md)：用 `init.defaultBranch` 把預設分支設成 main，與 GitHub 新 repository 的預設一致。[S02] [S03]
5. [Repository（儲存庫）](concepts/repository.md)：Git 用來記錄專案的地方，就是專案資料夾裡的 `.git` 子資料夾。取得 repository 有兩種方式。[S01] [S04]
   - [git init（建立 repository）](concepts/git-init.md)：把既有的資料夾變成 repository。執行後還沒有任何檔案被追蹤，要 add 再 commit。[S04]
   - [git clone（複製 repository）](concepts/git-clone.md)：複製一個現有的 repository，包含完整的歷史。[S04]
6. [三種狀態與三個區域](concepts/three-states.md)：檔案先分成已追蹤與未追蹤，已追蹤的檔案會在已修改、已暫存、已提交之間循環，對應工作目錄、暫存區、Git 目錄。[S01] [S02] 這是之後學 commit 指令的核心。
7. [git status（查看檔案狀態）](concepts/git-status.md)：隨時用它確認每個檔案處於哪種狀態。[S02]
8. [git add（加入暫存區）](concepts/git-add.md)：開始追蹤新檔案、暫存修改。暫存的是 add 當下的版本，之後再改就要再 add。[S02]
9. [Commit（提交）](concepts/commit.md)：把暫存區的快照記錄進歷史，用 `-m` 直接寫 commit 訊息。[S02] 忘了加檔案或訊息寫錯時，可以用 `--amend` 重做還沒 push 的上一個 commit。[S05]
10. [git restore（復原檔案）](concepts/git-restore.md)：不小心暫存時用 `git restore --staged` 取消暫存，`git restore <file>` 會丟掉修改，是危險的指令。commit 過的幾乎都救得回來，沒 commit 過的可能永遠消失。[S05]
11. [.gitignore（忽略檔案）](concepts/gitignore.md)：開始專案前就設定好，避免不小心 commit 自動產生的檔案。[S02]
12. [git diff（查看變更內容）](concepts/git-diff.md)：想知道確切改了哪幾行時使用（只留在 wiki，不放進簡報）。[S02]

## 簡報範圍決定

以下是 ingest 討論時與使用者確認的簡報取捨，規劃大綱時要遵守：

- 開場：用「把檔案複製到加上日期的資料夾」的痛點引起動機（S01 討論）。
- 版本控制的類型：只用一句話對比集中式與分散式，本地版本控制不放（S01 討論）。
- 不放進簡報：SHA-1 雜湊、暫存區的技術名稱 index、RCS（S01 討論）。
- 原文的 check out 是一般動詞「取出」，簡報中要避免讓新手和指令混淆（S01 討論）。
- commit 一律教 `git commit -m`，強調用 `-m` 可以避免卡在編輯器（S02 討論）。
- `git commit -a` 放在「常見錯誤」：它可能把不想要的變更也包進 commit（S02 討論）。
- `git diff` 留在 wiki，不放進簡報（S02 討論）。
- 不放進簡報：`git status -s` 精簡格式、`.gitignore` 萬用字元細節與子資料夾規則、`git diff --staged`、`--cached` 與 `difftool`、編輯器設定與 `commit -v`、`git rm`、`git mv`（S02 討論）。
- ~~**待決事項**：範例輸出中的分支名稱 `master` 在簡報中怎麼處理，等 ingest S03 之後再決定（S02 討論）。~~ 已於 S03 決定，見下一點。
- 範例輸出中的分支名稱改成 `main`，並註明「輸出改編自 S02，分支名稱依 S03 的設定改為 main」。改編的依據、原因與範圍寫在 [預設分支名稱（master 與 main）](concepts/default-branch.md)，簡報引用該頁。說明「Git 本身預設是 master」的投影片加上 `data-legacy`（S03 討論）。
- 簡報如果要提到「Git 本身預設是 master」，寫成「依 Pro Git 線上版，2026-11-22 擷取」。這個說法與 SHA-1 的現況都不另外找來源（lint 討論）。
- 放進簡報的設定有三項：第一次使用前設定 `user.name` 與 `user.email`，並強調 commit 會永久記錄這兩項。用 `git config --global init.defaultBranch main` 設定預設分支名稱。用 `git config --list` 或 `git config user.name` 確認設定（S03 討論）。
- 編輯器只用一句話帶過：沒設定時會開啟系統預設的編輯器，所以簡報一律用 `-m`（S03 討論）。
- 不放進簡報：設定的三個層級細節（含 `--system` 與各系統的設定檔路徑）、`core.editor` 的設定（含 Notepad++ 路徑寫法）、`--show-origin`、重複的設定值。「在特定專案使用不同 email」頂多一句話帶過（S03 討論）。
- 放進簡報：取得 repository 的兩種方式、`git init` 會建立 `.git` 但還沒追蹤任何檔案、「init → add → commit」的第一次 commit 流程（適合當實際操作的主軸）、`git clone <url>` 會下載完整的歷史（S04 討論）。
- 不放進簡報：各系統的 `cd` 路徑寫法（頂多一行帶過）、`.git` 的內部結構、伺服器端的 hooks、與 Subversion 的 checkout 比較、指定 clone 的資料夾名稱、`git://` 與 SSH 等傳輸協定（S04 討論）。
- 簡報的 commit 訊息一律用雙引號，理由是與 S02 的範例一致（S04 討論）。
- **待決事項**：push 到 GitHub 要教哪一條路線，一是先在本地 `git init`，之後再連到 GitHub 並 push，二是先在 GitHub 建立 repository，再 clone 下來。等 ingest S06（2.5 Working with Remotes）之後再決定（S04 討論）。
- 放進簡報：`git restore --staged <file>` 放在「常見錯誤」（不小心 add 了不想 commit 的檔案）。`git restore <file>` 要搭配強烈的危險警告。「commit 過的幾乎都能救回，沒 commit 的可能永遠消失」放在總結，鼓勵學生常 commit。`git commit --amend` 用在忘了加檔案或訊息打錯，並提醒只能用在還沒 push 的 commit（S05 討論）。
- 不放進簡報：`git reset` 的運作細節與 `--hard`、stash 與分支、資料救援、rebase 的風險。舊寫法 `git reset HEAD`、`git checkout --` 只留在 [git restore（復原檔案）](concepts/git-restore.md) 的過時／現行做法區塊（S05 討論）。
- 簡報中 `git status` 的範例，改用 S05 新版段落（Git 2.23.0 起）的輸出，提示是 `git restore`，分支名稱依 [預設分支名稱（master 與 main）](concepts/default-branch.md) 改成 main（S05 討論）。

## 尚未涵蓋的主題

教學目標是 commit 與 push，不教分支。依序待 ingest 的資料如下，找不到來源的主題記在 [操作紀錄](log.md) 各筆的「待找資料」：

- S06：Pro Git 2.5 Working with Remotes（push 到遠端）
- S07：GitHub Docs personal access tokens（推送到 GitHub 時的身分驗證）
- 視時間決定：GitHub 的 email 隱私設定（commit 會永久記錄 email，push 到 GitHub 後別人看得到），S07 之後再決定要不要補一篇
