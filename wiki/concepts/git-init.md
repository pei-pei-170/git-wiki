# git init（建立 repository）

> `git init` 會把目前這個還沒納入版本控制的資料夾，變成一個 Git [repository](repository.md)。[S04]

## 白話解釋

如果你有一個還沒納入版本控制的專案資料夾，想開始用 Git 管理，要先進入這個專案資料夾，再執行 `git init`。[S04] 它會建立一個名為 `.git` 的子資料夾，裡面是 repository 需要的所有檔案。[S04] 什麼是 repository，見 [Repository（儲存庫）](repository.md)。[S04]

**這時專案中還沒有任何檔案被追蹤。** [S04] 如果資料夾裡已經有檔案，想開始管理它們，應該先追蹤這些檔案，再做第一次 commit。[S04] 做法是用幾個 `git add` 指定要追蹤的檔案，再執行 `git commit`。[S04] 完成後，你就有一個包含已追蹤檔案與第一次 commit 的 Git repository。[S04]

用 `git init` 建立新 repository 時，Git 預設會建立名為 master 的分支，從 Git 2.28 起可以改成其他名稱，見 [預設分支名稱（master 與 main）](default-branch.md)。[S03]

## 指令範例

先進入專案資料夾，不同系統的路徑寫法略有不同：[S04]

```console
$ cd /home/user/my_project
```

```console
$ cd /Users/user/my_project
```

```console
$ cd C:/Users/user/my_project
```

上面三行依序是 Linux、macOS、Windows 的例子。[S04]

建立 repository：[S04]

```console
$ git init
```

追蹤既有的檔案，並做第一次 commit：[S04]

```console
$ git add *.c
$ git add LICENSE
$ git commit -m 'Initial project version'
```

原文這裡的 commit 訊息用單引號，簡報一律改用雙引號，理由是與 S02 的範例一致。（S04 討論）

## 新手常見誤解

- **以為執行 `git init` 後，檔案就會自動被追蹤**：`git init` 只建立 `.git` 子資料夾，要用 `git add` 追蹤檔案、再 `git commit`，才算完成第一次 commit。[S04]
- **以為要在任何地方執行 `git init` 都可以**：要先用 `cd` 進入想管理的專案資料夾，再執行 `git init`。[S04]

## 時效註記

無

## 相關頁面

- [Repository（儲存庫）](repository.md)：`git init` 建立的就是 repository
- [git clone（複製 repository）](git-clone.md)：取得 repository 的另一種方式
- [git add（加入暫存區）](git-add.md)：`git init` 之後追蹤檔案的下一步
- [Commit（提交）](commit.md)：完成第一次 commit
- [預設分支名稱（master 與 main）](default-branch.md)：`git init` 建立的初始分支名稱

## 來源

- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
- [S04｜Pro Git 2.1 Git Basics - Getting a Git Repository](../sources/S04-progit-getting-a-git-repository.md)
