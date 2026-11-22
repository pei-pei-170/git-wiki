# S07｜Adding locally hosted code to GitHub

- 來源：[Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)（GitHub Docs，CC BY 4.0）
- 年份：unknown（本次取得日期為 2026-11-22）
- 時效風險：中（網頁沒有標示年份，無法判斷內容寫於何時）

## 重點

1. 存在自己電腦上的程式碼，不論是否已用 Git 追蹤，都可以用 GitHub CLI 或 Git 指令匯入 GitHub，也可以改用 GitHub Desktop。[S07]
2. 絕對不要把密碼、API key 之類的敏感資訊 `git add`、`commit` 或 `push` 到遠端 repository。[S07]
3. 程式碼還沒被任何版本控制系統追蹤時，先開啟終端機（Windows 是 Git Bash），進入專案根目錄，初始化 Git repository。Git 2.28.0 以上可以用 `git init -b main` 設定預設分支名稱。接著用 `git add .` 暫存檔案，再用 `git commit -m "First commit"` commit。[S07]
4. 用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。[S07]
5. 在 GitHub 建立新的 repository 時，為了避免錯誤，不要用 README、license 或 gitignore 檔案初始化它，這些檔案可以等專案 push 到 GitHub 之後再加。[S07]
6. 用 `git remote add origin REMOTE-URL` 新增遠端，用 `git remote -v` 確認，再用 `git push origin main` 把本地 repository 的變更推送到 GitHub。[S07]

## 影響的 wiki 頁面

- 新增 [把本地 repository 推上 GitHub](../concepts/push-to-github.md)
- 更新 [預設分支名稱（master 與 main）](../concepts/default-branch.md)：S07 作為 `git push origin main` 的直接依據，並記錄與 S03 說法不一致之處
- 更新 [git init（建立 repository）](../concepts/git-init.md)：`git init -b main`、Windows 使用 Git Bash、`git add .`
- 更新 [Remote（遠端 repository）](../concepts/remote.md)、[git push（推送到遠端）](../concepts/git-push.md)、[git add（加入暫存區）](../concepts/git-add.md)、[git restore（復原檔案）](../concepts/git-restore.md)、[Commit（提交）](../concepts/commit.md)

## 與其他資料的衝突或過時之處

- **預設分支的說法與 S03 不一致**：S07 在初始化步驟寫「By default, the initial branch is called `main`」[S07]，S03 說用 `git init` 建立新 repository 時，Git 預設會建立 master [S03]。兩種說法都保留，見 [預設分支名稱（master 與 main）](../concepts/default-branch.md)。（S07 討論）
- **S07 內部不一致**：macOS 段落寫 `git push -u origin main`，Windows 與 Linux 段落寫 `git push origin main`。[S07] 簡報用不加 `-u` 的寫法。（S07 討論）
- **舊寫法**：`git add .` 範例的註解寫「To unstage a file, use 'git reset HEAD YOUR-FILE'」[S07]，S05 說從 Git 2.23.0 起，很多復原操作改用 `git restore` [S05]。見 [git restore（復原檔案）](../concepts/git-restore.md)。
