# git add（加入暫存區）

> `git add` 是一個多用途指令，用來開始追蹤新檔案、暫存修改過的檔案，也能做其他事，例如把有合併衝突的檔案標記為已解決。[S02]

## 白話解釋

與其把 `git add` 想成「把這個檔案加進專案」，不如想成「把這份內容精確地加進下一次 commit」。[S02]

**開始追蹤新檔案**：新增的檔案一開始是未追蹤的，除非你明確要求，否則 Git 不會把未追蹤的檔案放進 commit 快照，這是為了避免你不小心把產生出來的二進位檔，或其他不想要的檔案也包進去。[S02] 執行 `git add <檔案>` 之後，檔案就變成已追蹤並且已暫存，會出現在 `git status` 輸出的「Changes to be committed」區。[S02]

**暫存修改過的檔案**：已追蹤的檔案被修改後，會出現在「Changes not staged for commit」區，代表它在工作目錄中被修改了，但還沒暫存，執行 `git add` 才會把它暫存起來。[S02]

**暫存的是當下的版本**：Git 暫存的，是你執行 `git add` 那一刻的檔案內容。[S02] 如果 add 之後又修改檔案，同一個檔案會同時出現在已暫存與未暫存兩區。這時 commit，進去的是上次 add 時的版本，而不是工作目錄中目前的版本，所以要再執行一次 `git add`，才能暫存最新的版本。[S02]

`git add` 可以接檔案或資料夾的路徑，如果是資料夾，會把資料夾中的所有檔案都加進來。[S02]

## 指令範例

開始追蹤新檔案 `README`，它會變成已暫存：[S02]

```console
$ git add README
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)

    new file:   README
```

暫存修改過的檔案 `CONTRIBUTING.md`：[S02]

```console
$ git add CONTRIBUTING.md
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   README
    modified:   CONTRIBUTING.md
```

add 之後又修改了 `CONTRIBUTING.md`，它會同時出現在已暫存與未暫存兩區，要再 add 一次：[S02]

```console
$ vim CONTRIBUTING.md
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   README
    modified:   CONTRIBUTING.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md
```

## 新手常見誤解

- **以為 `git add` 是「把檔案加進專案」，做一次就好**：`git add` 是把「這份內容」加進下一次 commit，檔案每次修改後，都要再 add 才會暫存最新的版本。[S02]
- **以為 add 之後的修改也會自動進入 commit**：commit 進去的是最後一次 add 時的版本。[S02]
- **以為 Git 會自動記錄新增的檔案**：新檔案在明確執行 `git add` 之前都是未追蹤的，不會進入 commit。[S02]

## 時效註記

- 範例輸出中的分支名稱是 `master`，過時說法、現行做法與簡報的處理方式，見 [預設分支名稱（master 與 main）](default-branch.md)。[S02] [S03]
- 範例輸出中，取消暫存的提示有 `git restore --staged <file>` 與 `git reset HEAD <file>` 兩種，過時說法與現行做法見 [git restore（復原檔案）](git-restore.md)。[S02] [S05]

## 相關頁面

- [三種狀態與三個區域](three-states.md)：`git add` 讓檔案從已修改變成已暫存
- [git status（查看檔案狀態）](git-status.md)：add 前後用它確認檔案狀態
- [Commit（提交）](commit.md)：add 之後的下一步
- [.gitignore（忽略檔案）](gitignore.md)：不想被 add 的檔案寫在這裡
- [git restore（復原檔案）](git-restore.md)：不小心 add 了，用 `git restore --staged` 取消暫存

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S05｜Pro Git 2.4 Git Basics - Undoing Things](../sources/S05-progit-undoing-things.md)
