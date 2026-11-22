# git clone（複製 repository）

> `git clone <url>` 會取得一個現有 Git repository 的完整副本，專案歷史中每個檔案的每個版本，預設都會被下載。[S04]

## 白話解釋

想取得一個現有 Git repository 的副本時，例如一個你想參與貢獻的專案，要用的指令是 `git clone`。[S04] 這個指令叫 clone 而不是 checkout，是很重要的差別。Git 取得的不只是一份工作副本，而是伺服器上幾乎所有資料的完整副本。[S04] 事實上，如果伺服器的硬碟損毀，通常可以用任何一個用戶端的 clone，把伺服器恢復到被 clone 時的狀態。[S04]

執行 `git clone <url>` 時，Git 會做這幾件事：[S04]

1. 建立一個與專案同名的資料夾。[S04]
2. 在裡面初始化 `.git` 子資料夾。[S04]
3. 下載這個 repository 的所有資料。[S04]
4. 取出最新版本的工作副本。[S04]

進入這個新資料夾，就會看到專案的檔案，可以開始修改或使用。[S04] clone 下來的檔案全部都是已追蹤且未修改的狀態，因為 Git 才剛把它們取出來，你還沒編輯任何東西。[S02]

clone 時，Git 會自動把來源 repository 加成名為 origin 的遠端，見 [Remote（遠端 repository）](remote.md)。[S06] 預設上，`git clone` 也會自動讓本地的 master 分支，追蹤 clone 來源伺服器上的遠端 master 分支（或不論預設分支叫什麼名字）。[S06]

如果想用不同的資料夾名稱，可以在網址後面再加上資料夾名稱。[S04]

Git 有好幾種傳輸協定可以用。上面的例子用的是 `https://`，你也可能看到 `git://`，或是使用 SSH 傳輸協定的 `user@server:path/to/repo.git`。[S04]

## 指令範例

clone libgit2 這個專案，會建立名為 `libgit2` 的資料夾：[S04]

```console
$ git clone https://github.com/libgit2/libgit2
```

clone 到名為 `mylibgit` 的資料夾：[S04]

```console
$ git clone https://github.com/libgit2/libgit2 mylibgit
```

## 新手常見誤解

- **以為 clone 只會下載最新版的檔案**：clone 預設會下載專案歷史中每個檔案的每個版本，不只是一份工作副本。[S04]
- **以為 clone 之後，要先 `git add` 才能開始追蹤**：clone 下來的檔案已經全部是已追蹤的狀態。[S02]

## 時效註記

- 原文列出的傳輸協定（`https://`、`git://`、SSH）可能有時效性，本專案沒有較新的資料確認，也不放進簡報。[S04]

## 相關頁面

- [Repository（儲存庫）](repository.md)：clone 複製的就是整個 repository
- [git init（建立 repository）](git-init.md)：取得 repository 的另一種方式
- [版本控制（Version Control）](version-control.md)：分散式版本控制中，每份 clone 都是完整備份
- [git status（查看檔案狀態）](git-status.md)：剛 clone 完執行 `git status` 的樣子
- [Remote（遠端 repository）](remote.md)：clone 會自動加上名為 origin 的遠端

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S04｜Pro Git 2.1 Git Basics - Getting a Git Repository](../sources/S04-progit-getting-a-git-repository.md)
- [S06｜Pro Git 2.5 Git Basics - Working with Remotes](../sources/S06-progit-working-with-remotes.md)
