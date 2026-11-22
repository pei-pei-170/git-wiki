# Repository（儲存庫）

> Repository 是 Git 用來記錄專案的地方，存放在專案資料夾中的 `.git` 子資料夾裡，包含專案的中繼資料與物件資料庫。[S01] [S04]

## 白話解釋

在專案資料夾執行 `git init`，會建立一個名為 `.git` 的子資料夾，裡面是 repository 需要的所有檔案，也就是一個 Git repository 的骨架。[S04] 這個資料夾就是 Git 目錄，Git 在這裡存放專案的中繼資料（metadata，描述資料的資料）與物件資料庫。[S01] 它是 Git 最重要的部分，從另一台電腦 clone repository 時，複製的就是它。[S01]

取得 Git repository 通常有兩種方式。[S04]

1. 把一個還沒納入版本控制的本地資料夾，變成 Git repository，做法見 [git init（建立 repository）](git-init.md)。[S04]
2. 從別處 clone 一個現有的 Git repository，做法見 [git clone（複製 repository）](git-clone.md)。[S04]

兩種方式最後都會在你的電腦上得到一個 Git repository，可以開始工作。[S04]

在分散式版本控制系統中，用戶端會完整複製整個 repository，包含完整的歷史。[S01] 所以 repository 不只存在伺服器上，你電腦上的那一份也是完整的。[S01] [S04]

## 指令範例

把目前的資料夾變成 Git repository：[S04]

```console
$ git init
```

從別處 clone 一個現有的 repository：[S04]

```console
$ git clone https://github.com/libgit2/libgit2
```

## 新手常見誤解

- **以為 repository 只存在 GitHub 等伺服器上**：用 `git clone` 時，Git 會取得伺服器上幾乎所有資料的完整副本，專案歷史中每個檔案的每個版本都會被下載到你的電腦。[S04]
- **以為執行 `git init` 後，資料夾裡的檔案就開始被追蹤**：`git init` 只建立 `.git` 子資料夾，這時專案中還沒有任何檔案被追蹤。[S04]

## 時效註記

無

## 相關頁面

- [git init（建立 repository）](git-init.md)：在既有資料夾建立 repository
- [git clone（複製 repository）](git-clone.md)：複製一個現有的 repository
- [三種狀態與三個區域](three-states.md)：Git 目錄就是 repository 的所在
- [版本控制（Version Control）](version-control.md)：分散式版本控制中，每份 clone 都是完整備份

## 來源

- [S01｜Pro Git 1.1 About Version Control、1.3 What is Git?](../sources/S01-progit-version-control-and-what-is-git.md)
- [S04｜Pro Git 2.1 Git Basics - Getting a Git Repository](../sources/S04-progit-getting-a-git-repository.md)
