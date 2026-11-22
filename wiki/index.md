# Wiki 目錄

本 wiki 整理「Git 與 GitHub 入門」的知識，所有內容都來自 `raw/` 中的原始資料。每新增一頁都要在這裡登記。

## 總覽

- [新手學 Git 的完整路線](overview.md)：用新手的學習順序把各個概念串起來，是規劃簡報大綱的起點。
- [操作紀錄](log.md)：每次 ingest、lint、製作簡報的紀錄，只能往後新增。

## 資料摘要

- [S01｜Pro Git 1.1 About Version Control、1.3 What is Git?](sources/S01-progit-version-control-and-what-is-git.md)：版本控制是什麼、三種版本控制系統，以及 Git 的特色與三種狀態。
- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](sources/S02-progit-recording-changes.md)：用 `git status`、`git add`、`git commit` 記錄變更，以及 `.gitignore`、`git diff`、`git rm`、`git mv`。
- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](sources/S03-progit-first-time-git-setup.md)：第一次使用 Git 前的設定：身分、編輯器、預設分支名稱與檢查設定。
- [S04｜Pro Git 2.1 Git Basics - Getting a Git Repository](sources/S04-progit-getting-a-git-repository.md)：取得 repository 的兩種方式：`git init` 與 `git clone`。
- [S05｜Pro Git 2.4 Git Basics - Undoing Things](sources/S05-progit-undoing-things.md)：復原操作：`git commit --amend`，以及 Git 2.23.0 前後兩種取消暫存與放棄修改的寫法。
- [S06｜Pro Git 2.5 Git Basics - Working with Remotes](sources/S06-progit-working-with-remotes.md)：遠端 repository：`git remote`、`git push`，以及 fetch、pull 與遠端的管理。
- [S07｜Adding locally hosted code to GitHub](sources/S07-github-adding-locally-hosted-code.md)：GitHub Docs：在 GitHub 建立 repository，把本地的程式碼推上去。
- [S08｜Managing your personal access tokens](sources/S08-github-personal-access-tokens.md)：GitHub Docs：建立與使用 personal access token，在命令列代替密碼驗證身分。
- [S09｜Git password authentication is shutting down](sources/S09-github-changelog-password-auth-shutdown.md)：GitHub Changelog（摘錄）：2021 年 8 月 13 日起不再接受用帳號密碼驗證 Git 操作。

## 概念

- [版本控制（Version Control）](concepts/version-control.md)：記錄檔案變化、可以叫回特定版本的系統，以及本地、集中式、分散式三種類型。
- [Git](concepts/git.md)：用快照記錄資料的分散式版本控制系統，大部分操作在本地，commit 後很難遺失。
- [git config（Git 設定）](concepts/git-config.md)：設定的三個層級，以及第一次 commit 前要設定的名稱與 email。
- [預設分支名稱（master 與 main）](concepts/default-branch.md)：Git 預設 master、GitHub 預設 main，以及簡報範例改編為 main 的決定。
- [Repository（儲存庫）](concepts/repository.md)：Git 用來記錄專案的地方，也就是專案資料夾中的 `.git` 子資料夾。
- [git init（建立 repository）](concepts/git-init.md)：把既有的資料夾變成 repository，再 add、commit 完成第一次 commit。
- [git clone（複製 repository）](concepts/git-clone.md)：複製一個現有的 repository，包含完整的歷史。
- [三種狀態與三個區域](concepts/three-states.md)：已修改、已暫存、已提交，對應工作目錄、暫存區、Git 目錄，以及已追蹤與未追蹤，是學 commit 的核心。
- [git status（查看檔案狀態）](concepts/git-status.md)：查看哪些檔案未追蹤、已修改或已暫存。
- [git add（加入暫存區）](concepts/git-add.md)：開始追蹤新檔案、暫存修改。暫存的是 add 當下的版本。
- [Commit（提交）](concepts/commit.md)：把暫存區的快照記錄進歷史，用 `-m` 直接寫訊息，用 `--amend` 修正還沒 push 的上一個 commit。
- [git restore（復原檔案）](concepts/git-restore.md)：取消暫存與放棄修改，Git 2.23.0 起取代舊的 `git reset HEAD`、`git checkout --`。
- [Remote（遠端 repository）](concepts/remote.md)：放在網際網路或某個網路上的專案版本，clone 時預設名稱為 origin。
- [git push（推送到遠端）](concepts/git-push.md)：把 commit 推送到遠端，需要寫入權限，而且沒有別人先 push。
- [把本地 repository 推上 GitHub](concepts/push-to-github.md)：從 `git init` 到 `git push origin main` 的完整流程。
- [Personal access token（個人存取權杖）](concepts/personal-access-token.md)：在命令列透過 HTTPS 驗證身分時，用來代替密碼的 token。
- [.gitignore（忽略檔案）](concepts/gitignore.md)：列出不想被 Git 追蹤的檔名規則。
- [git diff（查看變更內容）](concepts/git-diff.md)：查看確切改了哪幾行，分成未暫存與已暫存。
