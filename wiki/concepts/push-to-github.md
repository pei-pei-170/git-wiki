# 把本地 repository 推上 GitHub

> 存在自己電腦上的程式碼，不論是否已用 Git 追蹤，都可以用 Git 指令匯入 GitHub。[S07]

## 白話解釋

把程式碼匯入 GitHub，可以讓你和別人更容易一起進行專案、管理程式碼。[S07] 除了直接輸入 Git 指令，也可以改用 GitHub CLI 或 GitHub Desktop。[S07]

**開始之前：** 絕對不要把密碼、API key 之類的敏感資訊 `git add`、`commit` 或 `push` 到遠端 repository。[S07]

### 步驟一：在本地建立 repository 並 commit

如果本地的程式碼還沒被任何版本控制系統追蹤，第一步是初始化 Git repository。如果專案已經用 Git 追蹤，可以跳到步驟二。[S07]

1. 開啟終端機，Windows 使用 Git Bash。[S07]
2. 進入專案的根目錄。[S07]
3. 把本地資料夾初始化為 Git repository，做法見 [git init（建立 repository）](git-init.md)。[S07]
4. 加入新 repository 中的檔案，這會把它們暫存起來，準備第一次 commit。[S07]
5. commit 已經暫存的檔案。[S07]

### 步驟二：在 GitHub 建立新的 repository

用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。[S07]

1. 在 GitHub 建立新的 repository。為了避免錯誤，不要用 README、license 或 gitignore 檔案初始化新的 repository，這些檔案可以等專案 push 到 GitHub 之後再加。[S07]
2. 在 repository 的 Quick Setup 頁面上方，點複製圖示，複製遠端 repository 的網址。[S07]

### 步驟三：連到遠端並 push

1. 在終端機中，把目前的工作目錄切換到本地專案。[S07]
2. 新增遠端 repository 的網址，你的本地 repository 會被推送到這裡。把 `REMOTE-URL` 換成 GitHub 上 repository 的完整網址。[S07]
3. 確認遠端網址設定正確。[S07]
4. 把本地 repository 的變更推送到 GitHub。如果你的預設分支不叫 main，就把 main 換成你的預設分支名稱。[S07]

## 指令範例

以下指令依序取自 S07 各步驟，`REMOTE-URL` 要換成 GitHub 上 repository 的完整網址：[S07]

```shell
git init -b main
git add .
git commit -m "First commit"
git remote add origin REMOTE-URL
git remote -v
git push origin main
```

`git init -b main` 要 Git 2.28.0 以上才能使用。[S07] 簡報設定預設分支名稱的方法是 `git config --global init.defaultBranch main`，`git init -b main` 只留在 wiki，見 [預設分支名稱（master 與 main）](default-branch.md)。（S07 討論）

## 新手常見誤解

- **以為在 GitHub 建立 repository 時，先勾選 README 比較好**：為了避免錯誤，不要用 README、license 或 gitignore 檔案初始化新的 repository，可以等 push 之後再加。[S07]
- **以為用 Git 指令推送到 GitHub 不需要驗證身分**：用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。[S07]
- **以為密碼或 API key 跟著專案 commit 也沒關係**：絕對不要把密碼、API key 之類的敏感資訊 add、commit 或 push 到遠端 repository。[S07]

## 時效註記

- S07 的 macOS 段落寫 `git push -u origin main`，Windows 與 Linux 段落寫 `git push origin main`。[S07] 簡報用不加 `-u` 的寫法。（S07 討論）
- S07 在 `git add .` 範例的註解中，取消暫存的寫法是 `git reset HEAD YOUR-FILE`，現行寫法見 [git restore（復原檔案）](git-restore.md)。[S05] [S07]

## 相關頁面

- [git init（建立 repository）](git-init.md)：步驟一的初始化
- [git add（加入暫存區）](git-add.md)：步驟一的暫存
- [Commit（提交）](commit.md)：步驟一的 commit
- [Remote（遠端 repository）](remote.md)：步驟三新增的 origin
- [git push（推送到遠端）](git-push.md)：步驟三的 push
- [預設分支名稱（master 與 main）](default-branch.md)：push 指令中的分支名稱

## 來源

- [S05｜Pro Git 2.4 Git Basics - Undoing Things](../sources/S05-progit-undoing-things.md)
- [S07｜Adding locally hosted code to GitHub](../sources/S07-github-adding-locally-hosted-code.md)
