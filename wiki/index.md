# Wiki 目錄

本 wiki 整理「Git 與 GitHub 入門」的知識，所有內容都來自 `raw/` 中的原始資料。每新增一頁都要在這裡登記。

## 總覽

- [新手學 Git 的完整路線](overview.md)：用新手的學習順序把各個概念串起來，是規劃簡報大綱的起點。
- [操作紀錄](log.md)：每次 ingest、lint、製作簡報的紀錄，只能往後新增。

## 資料摘要

- [S01｜Pro Git 1.1 About Version Control；1.3 What is Git?](sources/S01-progit-version-control-and-what-is-git.md)：版本控制是什麼、三種版本控制系統，以及 Git 的特色與三種狀態。
- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](sources/S02-progit-recording-changes.md)：用 `git status`、`git add`、`git commit` 記錄變更，以及 `.gitignore`、`git diff`、`git rm`、`git mv`。

## 概念

- [版本控制（Version Control）](concepts/version-control.md)：記錄檔案變化、可以叫回特定版本的系統，以及本地、集中式、分散式三種類型。
- [Git](concepts/git.md)：用快照記錄資料的分散式版本控制系統，大部分操作在本地，commit 後很難遺失。
- [三種狀態與三個區域](concepts/three-states.md)：已修改、已暫存、已提交，對應工作目錄、暫存區、Git 目錄，以及已追蹤與未追蹤；是學 commit 的核心。
- [git status（查看檔案狀態）](concepts/git-status.md)：查看哪些檔案未追蹤、已修改或已暫存。
- [git add（加入暫存區）](concepts/git-add.md)：開始追蹤新檔案、暫存修改；暫存的是 add 當下的版本。
- [Commit（提交）](concepts/commit.md)：把暫存區的快照記錄進歷史，用 `-m` 直接寫訊息。
- [.gitignore（忽略檔案）](concepts/gitignore.md)：列出不想被 Git 追蹤的檔名規則。
- [git diff（查看變更內容）](concepts/git-diff.md)：查看確切改了哪幾行，分成未暫存與已暫存。
