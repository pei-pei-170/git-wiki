# git init（建立 repository）

> `git init` 會把目前這個還沒納入版本控制的資料夾，變成一個 Git [repository](repository.md)。[S04]

## 白話解釋

如果你有一個還沒納入版本控制的專案資料夾，想開始用 Git 管理，要先進入這個專案資料夾，再執行 `git init`。[S04] 它會建立一個名為 `.git` 的子資料夾，裡面是 repository 需要的所有檔案。[S04] 什麼是 repository，見 [Repository（儲存庫）](repository.md)。[S04]

**這時專案中還沒有任何檔案被追蹤。** [S04] 如果資料夾裡已經有檔案，想開始管理它們，應該先追蹤這些檔案，再做第一次 commit。[S04] 做法是用幾個 `git add` 指定要追蹤的檔案，再執行 `git commit`。[S04] 完成後，你就有一個包含已追蹤檔案與第一次 commit 的 Git repository。[S04]

用 `git init` 建立新 repository 時，Git 預設會建立名為 master 的分支，從 Git 2.28 起可以改成其他名稱，見 [預設分支名稱（master 與 main）](default-branch.md)。[S03] S07 對預設分支的說法與 S03 不一致，兩種說法都記在該頁的「兩份資料的說法不一致」。[S03] [S07]

GitHub Docs 的做法是：開啟終端機（Windows 使用 Git Bash），進入專案的根目錄，把本地資料夾初始化為 Git repository。[S07] Git 2.28.0 以上可以用 `git init -b main` 設定預設分支名稱，Git 2.27.1 以下可以用 `git init && git symbolic-ref HEAD refs/heads/main`。[S07] 接著用 `git add .` 加入新 repository 中的檔案並暫存，再用 `git commit` 完成第一次 commit。[S07] 簡報設定預設分支名稱的方法是 `git config --global init.defaultBranch main`，`git init -b main` 只留在 wiki。（S07 討論）

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

GitHub Docs 的寫法，初始化時一併指定預設分支名稱（Git 2.28.0 以上）：[S07]

```shell
git init -b main
```

加入新 repository 中的檔案並暫存，再 commit：[S07]

```shell
$ git add .
$ git commit -m "First commit"
```

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
- [把本地 repository 推上 GitHub](push-to-github.md)：`git init` 之後推上 GitHub 的完整流程

## 來源

- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
- [S04｜Pro Git 2.1 Git Basics - Getting a Git Repository](../sources/S04-progit-getting-a-git-repository.md)
- [S07｜Adding locally hosted code to GitHub](../sources/S07-github-adding-locally-hosted-code.md)
