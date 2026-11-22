# git push（推送到遠端）

> `git push <remote> <branch>` 會把你做過的 commit 推送到遠端伺服器，讓專案可以分享給別人。[S06]

## 白話解釋

commit 只會記錄在你本地的副本裡，等有網路連線時再上傳。[S01] 當專案到了你想分享的階段，就要把它推送到上游（upstream）。[S06] 指令很簡單：`git push <remote> <branch>`。[S06] 例如要把 master 分支推送到 origin 伺服器，而 clone 通常會自動幫你設定好這兩個名稱。[S06]

### push 成功的條件

只有在兩個條件都成立時，`git push` 才會成功：[S06]

1. 你 clone 的伺服器，你有寫入權限。[S06]
2. 這段時間沒有別人先 push。[S06]

如果你和別人同時 clone，他們先 push，你再 push，你的 push 就會被拒絕。[S06] 這時必須先取得他們的工作，整合進你的工作，才能再 push。[S06]

### push 之後

只能 amend 還在本地、還沒 push 到任何地方的 commit。已經 push 過的 commit 再 amend 並強制推送，會造成協作者的問題，見 [Commit（提交）](commit.md)。[S05]

## 指令範例

把本地的 master 分支推送到 origin：[S06]

```console
$ git push origin master
```

## 新手常見誤解

- **以為 commit 之後就自動上傳到遠端**：commit 只記錄在本地的副本，要 push 才會推送到遠端。[S01] [S06]
- **以為 push 一定會成功**：沒有寫入權限，或別人先 push 了，你的 push 就會被拒絕。[S06]
- **以為已經 push 的 commit 還可以隨意 amend**：已經 push 過的 commit 再 amend 並強制推送，會造成協作者的問題。[S05]

## 時效註記

- 範例指令中的分支名稱是 `master`，過時說法、現行做法與簡報的處理方式，見 [預設分支名稱（master 與 main）](default-branch.md)。[S06]

## 相關頁面

- [Remote（遠端 repository）](remote.md)：push 的對象
- [Commit（提交）](commit.md)：push 推送的是 commit
- [git clone（複製 repository）](git-clone.md)：clone 會自動設定 origin
- [預設分支名稱（master 與 main）](default-branch.md)：push 指令中的分支名稱

## 來源

- [S01｜Pro Git 1.1 About Version Control、1.3 What is Git?](../sources/S01-progit-version-control-and-what-is-git.md)
- [S05｜Pro Git 2.4 Git Basics - Undoing Things](../sources/S05-progit-undoing-things.md)
- [S06｜Pro Git 2.5 Git Basics - Working with Remotes](../sources/S06-progit-working-with-remotes.md)
