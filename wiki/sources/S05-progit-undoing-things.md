# S05｜Pro Git 2.4 Git Basics - Undoing Things

- 來源：[2.4 Git Basics - Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things)（《Pro Git》第 2 版，Scott Chacon、Ben Straub 著，CC BY-NC-SA 3.0）
- 年份：2014（第 2 版印刷版年份，本次取得日期為 2026-11-22）
- 時效風險：高（同一頁並列 Git 2.23.0 前後兩種復原指令）

## 重點

1. 復原要小心，有些復原操作本身無法再復原，這是 Git 中少數做錯就可能失去部分工作成果的地方。[S05]
2. `git commit --amend` 可以重做上一個 commit，例如補上忘了暫存的檔案或修改 commit 訊息。它會用新的 commit 完全取代舊的。只能用在還沒 push 的 commit。[S05]
3. 舊做法是用 `git reset HEAD <file>` 取消暫存，用 `git checkout -- <file>` 放棄修改，後者是危險的指令。[S05]
4. Git 2.23.0 新增了 `git restore`，基本上是 `git reset` 的替代方案。取消暫存用 `git restore --staged <file>`，放棄修改用 `git restore <file>`，後者一樣是危險的指令。[S05]
5. `git status` 的輸出會提示如何復原暫存區與工作目錄的變更。[S05]
6. commit 過的東西幾乎都能救回來，包括被 `--amend` 覆蓋的 commit。從來沒有 commit 過的東西一旦遺失，很可能再也找不回來。[S05]

## 影響的 wiki 頁面

- 新增 [git restore（復原檔案）](../concepts/git-restore.md)：取消暫存與放棄修改，以及新舊兩種寫法的過時／現行做法區塊
- 更新 [Commit（提交）](../concepts/commit.md)：新增 `--amend` 段落
- 更新 [git status（查看檔案狀態）](../concepts/git-status.md)：新增 Git 2.23.0 起的輸出範例，時效註記改連到 git restore
- 更新 [git add（加入暫存區）](../concepts/git-add.md)：時效註記改連到 git restore
- 更新 [Git](../concepts/git.md)：commit 過的東西幾乎都能救回

## 與其他資料的衝突或過時之處

- S02 範例輸出中的 `git reset HEAD <file>`、`git checkout -- <file>` 提示，與 S05 前半段的輸出相同 [S02] [S05]。S05 說從 Git 2.23.0 起，很多復原操作改用 `git restore` [S05, Git 2.23.0]。過時說法與現行做法見 [git restore（復原檔案）](../concepts/git-restore.md) 的「時效註記」。
- 原文只寫版本、沒寫年份，所以現行做法標註版本號 `[S05, Git 2.23.0]`。（S05 討論）
- S05 的範例輸出中分支名稱是 master，處理方式見 [預設分支名稱（master 與 main）](../concepts/default-branch.md)。[S05]
