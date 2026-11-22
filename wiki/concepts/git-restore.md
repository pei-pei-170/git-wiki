# git restore（復原檔案）

> `git restore` 是 Git 2.23.0 新增的指令，基本上是 `git reset` 的替代方案。從 Git 2.23.0 起，很多復原操作 Git 都改用 `git restore`。[S05]

## 白話解釋

復原要小心，因為有些復原操作本身不一定能再復原。這是 Git 中少數做錯就可能失去部分工作成果的地方。[S05]

好消息是，用來判斷暫存區與工作目錄狀態的 `git status`，也會提示你怎麼復原這兩個區域的變更。[S05]

### 取消暫存（`--staged`）

例如你改了兩個檔案，想分成兩次 commit，卻不小心輸入 `git add *`，把兩個檔案都暫存了。[S05] 這時 `git status` 會在「Changes to be committed」下方提示，用 `git restore --staged <file>` 取消暫存。[S05] 執行後，這個檔案仍然是已修改，但回到了未暫存的狀態。[S05]

### 放棄修改

如果你不想保留對某個檔案的修改，想把它恢復成上次 commit 時（或剛 clone 時）的樣子，`git status` 也會在「Changes not staged for commit」區提示，用 `git restore <file>` 放棄修改。[S05]

**`git restore <file>` 是危險的指令。** 你對那個檔案做的所有本地修改都會消失，Git 會直接用最後一次暫存或 commit 的版本取代它。[S05] 除非你非常確定不要那些還沒儲存的本地修改，否則絕對不要使用這個指令。[S05]

### commit 過的幾乎都救得回來

在 Git 中，commit 過的東西幾乎都能救回來，連被 `--amend` 覆蓋的 commit 也可以。[S05] 但從來沒有 commit 過的東西一旦遺失，很可能就再也找不回來了。[S05]

## 指令範例

不小心用 `git add *` 暫存了兩個檔案：[S05]

```console
$ git add *
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   CONTRIBUTING.md
	renamed:    README.md -> README
```

取消暫存 `CONTRIBUTING.md`，它會回到「Changes not staged for commit」區：[S05]

```console
$ git restore --staged CONTRIBUTING.md
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    README.md -> README

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CONTRIBUTING.md
```

放棄對 `CONTRIBUTING.md` 的修改（危險，修改會消失）：[S05]

```console
$ git restore CONTRIBUTING.md
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    README.md -> README
```

## 新手常見誤解

- **以為取消暫存會把修改丟掉**：`git restore --staged <file>` 只是把檔案移出暫存區，檔案仍然是已修改的狀態。[S05]
- **以為 `git restore <file>` 和取消暫存一樣安全**：不加 `--staged` 時，對那個檔案的所有本地修改都會消失。[S05]
- **以為沒 commit 的修改弄丟了也找得回來**：commit 過的東西幾乎都能救回，但從來沒有 commit 過的東西一旦遺失，很可能再也找不回來。[S05]

## 時效註記

> ⚠️ 過時：取消暫存用 `git reset HEAD <file>`，放棄修改用 `git checkout -- <file>` [S05, 2014]。
> 現行做法：Git 2.23.0 新增了 `git restore`，從這個版本起，很多復原操作 Git 都改用 `git restore`，取消暫存用 `git restore --staged <file>`，放棄修改用 `git restore <file>` [S05, Git 2.23.0]。

- 舊做法中，`git reset HEAD <file>` 不會動到工作目錄的檔案，所以相對安全，但 `git reset` 加上 `--hard` 時是危險的指令。`git checkout -- <file>` 和 `git restore <file>` 一樣是危險的指令。[S05]
- S02 範例輸出中的 `git reset HEAD`、`git checkout --` 提示，與 S05 前半段（舊做法）的輸出相同。[S02] [S05]
- 範例輸出中的分支名稱是 `master`，過時說法、現行做法與簡報的處理方式，見 [預設分支名稱（master 與 main）](default-branch.md)。[S02] [S03]

## 相關頁面

- [git status（查看檔案狀態）](git-status.md)：輸出會提示如何復原
- [git add（加入暫存區）](git-add.md)：取消暫存就是復原 `git add`
- [Commit（提交）](commit.md)：用 `--amend` 修正上一個 commit
- [三種狀態與三個區域](three-states.md)：復原的是暫存區與工作目錄
- [預設分支名稱（master 與 main）](default-branch.md)：範例輸出中的分支名稱

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
- [S05｜Pro Git 2.4 Git Basics - Undoing Things](../sources/S05-progit-undoing-things.md)
