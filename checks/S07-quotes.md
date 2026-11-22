# S07 逐句核對

- 對象：S07（GitHub Docs〈Adding locally hosted code to GitHub〉）ingest 時新增或修改的事實陳述
- 不列入核對：標註「（Sxx 討論）」的專案決定、overview.md「簡報範圍決定」中的取捨，以及摘要頁資訊區塊中的年份與時效風險說明（關於資料本身的後設資訊）
- 核對日期：2026-11-22
- 驗證方式：`python tools/verify_quotes.py checks/S07-quotes.md`
- 備註：S07 原文是 markdown，夾有 HTML，原句照原文保留 HTML 標籤以便逐字比對

## 1｜sources/S07 重點 1
- 句子：存在自己電腦上的程式碼，不論是否已用 Git 追蹤，都可以用 GitHub CLI 或 Git 指令匯入 GitHub，也可以改用 GitHub Desktop。
- 來源：S07
- 原句：
  - If your code is stored locally on your computer and is tracked by Git or not tracked by any version control system (VCS), you can import the code to GitHub using GitHub CLI or Git commands.
  - Alternatively, you can use GitHub CLI or GitHub Desktop.

## 2｜sources/S07 重點 2
- 句子：絕對不要把密碼、API key 之類的敏感資訊 git add、commit 或 push 到遠端 repository。
- 來源：S07
- 原句：
  - Never `git add`, `commit`, or `push` sensitive information, for example passwords or API keys, to a remote repository.

## 3｜sources/S07 重點 3
- 句子：程式碼還沒被任何版本控制系統追蹤時，先開啟終端機（Windows 是 Git Bash），進入專案根目錄，初始化 Git repository。
- 來源：S07
- 原句：
  - If your locally-hosted code isn't tracked by any VCS, the first step is to initialize a Git repository.
  - Open <span class="platform-mac">Terminal</span><span class="platform-linux">Terminal</span><span class="platform-windows">Git Bash</span>.
  - Navigate to the root directory of your project.

## 4｜sources/S07 重點 3
- 句子：Git 2.28.0 以上可以用 git init -b main 設定預設分支名稱。
- 來源：S07
- 原句：
  - If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using `-b`.
  - git init -b main

## 5｜sources/S07 重點 3
- 句子：接著用 git add . 暫存檔案，再用 git commit -m "First commit" commit。
- 來源：S07
- 原句：
  - Add the files in your new local repository. This stages them for the first commit.
  - $ git add .
  - $ git commit -m "First commit"

## 6｜sources/S07 重點 4
- 句子：用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。
- 來源：S07
- 原句：
  - Before you can add your local repository to GitHub using Git, you must authenticate to GitHub on the command line.

## 7｜sources/S07 重點 5
- 句子：在 GitHub 建立新的 repository 時，為了避免錯誤，不要用 README、license 或 gitignore 檔案初始化它，這些檔案可以等專案 push 到 GitHub 之後再加。
- 來源：S07
- 原句：
  - To avoid errors, do not initialize the new repository with README, license, or gitignore files. You can add these files after your project has been pushed to GitHub.

## 8｜sources/S07 重點 6
- 句子：用 git remote add origin REMOTE-URL 新增遠端，用 git remote -v 確認，再用 git push origin main 把本地 repository 的變更推送到 GitHub。
- 來源：S07
- 原句：
  - git remote add origin REMOTE-URL
  - To verify that you set the remote URL correctly, run the following command.
  - git remote -v
  - To push the changes in your local repository to GitHub, run the following command.
  - git push origin main

## 9｜sources/S07 衝突 1
- 句子：S07 在初始化步驟寫「By default, the initial branch is called main」，S03 說用 git init 建立新 repository 時，Git 預設會建立 master。
- 來源：S07、S03
- 原句：
  - Initialize the local directory as a Git repository. By default, the initial branch is called `main`.
  - By default Git will create a branch called *master* when you create a new repository with `git init`.

## 10｜sources/S07 衝突 2
- 句子：macOS 段落寫 git push -u origin main，Windows 與 Linux 段落寫 git push origin main。
- 來源：S07
- 原句：
  - <div class="ghd-tool mac">
  - git push -u origin main
  - <div class="ghd-tool windows">
  - <div class="ghd-tool linux">
  - git push origin main

## 11｜sources/S07 衝突 3
- 句子：git add . 範例的註解寫「To unstage a file, use 'git reset HEAD YOUR-FILE'」，S05 說從 Git 2.23.0 起，很多復原操作改用 git restore。
- 來源：S07、S05
- 原句：
  - To unstage a file, use 'git reset HEAD YOUR-FILE'.
  - From Git version 2.23.0 onwards, Git will use `git restore` instead of `git reset` for many undo operations.

## 12｜push-to-github 定義
- 句子：存在自己電腦上的程式碼，不論是否已用 Git 追蹤，都可以用 Git 指令匯入 GitHub。
- 來源：S07
- 原句：
  - If your code is stored locally on your computer and is tracked by Git or not tracked by any version control system (VCS), you can import the code to GitHub using GitHub CLI or Git commands.

## 13｜push-to-github 白話
- 句子：把程式碼匯入 GitHub，可以讓你和別人更容易一起進行專案、管理程式碼。
- 來源：S07
- 原句：
  - Importing your source code to GitHub makes it easier for you and others to work together on projects and manage code.

## 14｜push-to-github 白話
- 句子：除了直接輸入 Git 指令，也可以改用 GitHub CLI 或 GitHub Desktop。
- 來源：S07
- 原句：
  - You can do this by typing Git commands directly. Alternatively, you can use GitHub CLI or GitHub Desktop.

## 15｜push-to-github 開始之前
- 句子：絕對不要把密碼、API key 之類的敏感資訊 git add、commit 或 push 到遠端 repository。
- 來源：S07
- 原句：
  - Never `git add`, `commit`, or `push` sensitive information, for example passwords or API keys, to a remote repository.

## 16｜push-to-github 步驟一
- 句子：如果本地的程式碼還沒被任何版本控制系統追蹤，第一步是初始化 Git repository。如果專案已經用 Git 追蹤，可以跳到步驟二。
- 來源：S07
- 原句：
  - If your locally-hosted code isn't tracked by any VCS, the first step is to initialize a Git repository. If your project is already tracked by Git, skip to

## 17｜push-to-github 步驟一 1
- 句子：開啟終端機，Windows 使用 Git Bash。
- 來源：S07
- 原句：
  - Open <span class="platform-mac">Terminal</span><span class="platform-linux">Terminal</span><span class="platform-windows">Git Bash</span>.

## 18｜push-to-github 步驟一 2
- 句子：進入專案的根目錄。
- 來源：S07
- 原句：
  - Navigate to the root directory of your project.

## 19｜push-to-github 步驟一 3
- 句子：把本地資料夾初始化為 Git repository。
- 來源：S07
- 原句：
  - Initialize the local directory as a Git repository.

## 20｜push-to-github 步驟一 4
- 句子：加入新 repository 中的檔案，這會把它們暫存起來，準備第一次 commit。
- 來源：S07
- 原句：
  - Add the files in your new local repository. This stages them for the first commit.

## 21｜push-to-github 步驟一 5
- 句子：commit 已經暫存的檔案。
- 來源：S07
- 原句：
  - Commit the files that you've staged in your local repository.

## 22｜push-to-github 步驟二
- 句子：用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。
- 來源：S07
- 原句：
  - Before you can add your local repository to GitHub using Git, you must authenticate to GitHub on the command line.

## 23｜push-to-github 步驟二 1
- 句子：在 GitHub 建立新的 repository。為了避免錯誤，不要用 README、license 或 gitignore 檔案初始化新的 repository，這些檔案可以等專案 push 到 GitHub 之後再加。
- 來源：S07
- 原句：
  - Create a new repository on GitHub. To avoid errors, do not initialize the new repository with README, license, or gitignore files. You can add these files after your project has been pushed to GitHub.

## 24｜push-to-github 步驟二 2
- 句子：在 repository 的 Quick Setup 頁面上方，點複製圖示，複製遠端 repository 的網址。
- 來源：S07
- 原句：
  - At the top of your repository on GitHub's Quick Setup page, click
  - to copy the remote repository URL.

## 25｜push-to-github 步驟三 1
- 句子：在終端機中，把目前的工作目錄切換到本地專案。
- 來源：S07
- 原句：
  - Change the current working directory to your local project.

## 26｜push-to-github 步驟三 2
- 句子：新增遠端 repository 的網址，你的本地 repository 會被推送到這裡。把 REMOTE-URL 換成 GitHub 上 repository 的完整網址。
- 來源：S07
- 原句：
  - To add the URL for the remote repository where your local repository will be pushed, run the following command. Replace `REMOTE-URL` with the repository's full URL on GitHub.

## 27｜push-to-github 步驟三 3
- 句子：確認遠端網址設定正確。
- 來源：S07
- 原句：
  - To verify that you set the remote URL correctly, run the following command.

## 28｜push-to-github 步驟三 4
- 句子：把本地 repository 的變更推送到 GitHub。如果你的預設分支不叫 main，就把 main 換成你的預設分支名稱。
- 來源：S07
- 原句：
  - To push the changes in your local repository to GitHub, run the following command.
  - If your default branch is not named "main," replace "main" with the name of your default branch.

## 29｜push-to-github 指令範例
- 句子：以下指令依序取自 S07 各步驟，REMOTE-URL 要換成 GitHub 上 repository 的完整網址。
- 來源：S07
- 原句：
  - git init -b main
  - $ git add .
  - $ git commit -m "First commit"
  - git remote add origin REMOTE-URL
  - git remote -v
  - git push origin main
  - Replace `REMOTE-URL` with the repository's full URL on GitHub.

## 30｜push-to-github 指令範例
- 句子：git init -b main 要 Git 2.28.0 以上才能使用。
- 來源：S07
- 原句：
  - If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using `-b`.

## 31｜push-to-github 誤解 1
- 句子：為了避免錯誤，不要用 README、license 或 gitignore 檔案初始化新的 repository，可以等 push 之後再加。
- 來源：S07
- 原句：
  - To avoid errors, do not initialize the new repository with README, license, or gitignore files.
  - You can add these files after your project has been pushed to GitHub.

## 32｜push-to-github 誤解 2
- 句子：用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。
- 來源：S07
- 原句：
  - you must authenticate to GitHub on the command line.

## 33｜push-to-github 誤解 3
- 句子：絕對不要把密碼、API key 之類的敏感資訊 add、commit 或 push 到遠端 repository。
- 來源：S07
- 原句：
  - sensitive information, for example passwords or API keys, to a remote repository.

## 34｜push-to-github 時效註記 1
- 句子：S07 的 macOS 段落寫 git push -u origin main，Windows 與 Linux 段落寫 git push origin main。
- 來源：S07
- 原句：
  - git push -u origin main
  - git push origin main

## 35｜push-to-github 時效註記 2
- 句子：S07 在 git add . 範例的註解中，取消暫存的寫法是 git reset HEAD YOUR-FILE。
- 來源：S07
- 原句：
  - To unstage a file, use 'git reset HEAD YOUR-FILE'.

## 36｜default-branch GitHub Docs
- 句子：S07 在初始化步驟寫「By default, the initial branch is called main」，並說明 Git 2.28.0 以上可以用 git init -b main 設定預設分支名稱，Git 2.27.1 以下可以用 git symbolic-ref 設定。
- 來源：S07
- 原句：
  - By default, the initial branch is called `main`.
  - If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using `-b`.
  - If you’re using Git 2.27.1 or an earlier version, you can set the name of the default branch using `git symbolic-ref`.

## 37｜default-branch 不一致 S03
- 句子：S03 說，用 git init 建立新 repository 時，Git 預設會建立名為 master 的分支。
- 來源：S03
- 原句：
  - By default Git will create a branch called *master* when you create a new repository with `git init`.

## 38｜default-branch 不一致 S07
- 句子：S07 說，初始分支預設叫 main，這句話之後緊接著說明用 git init -b main 設定預設分支名稱。
- 來源：S07
- 原句：
  - By default, the initial branch is called `main`.
  - If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using `-b`.

## 39｜default-branch 直接依據
- 句子：GitHub Docs 推送到 GitHub 的步驟，本身就使用 git push origin main，並說明如果預設分支不叫 main，就換成你的預設分支名稱。
- 來源：S07
- 原句：
  - git push origin main
  - If your default branch is not named "main," replace "main" with the name of your default branch.

## 40｜git-init GitHub Docs 做法
- 句子：開啟終端機（Windows 使用 Git Bash），進入專案的根目錄，把本地資料夾初始化為 Git repository。
- 來源：S07
- 原句：
  - <span class="platform-windows">Git Bash</span>
  - Navigate to the root directory of your project.
  - Initialize the local directory as a Git repository.

## 41｜git-init GitHub Docs 做法
- 句子：Git 2.28.0 以上可以用 git init -b main 設定預設分支名稱，Git 2.27.1 以下可以用 git init && git symbolic-ref HEAD refs/heads/main。
- 來源：S07
- 原句：
  - If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using `-b`.
  - git init -b main
  - If you’re using Git 2.27.1 or an earlier version
  - git init && git symbolic-ref HEAD refs/heads/main

## 42｜git-init GitHub Docs 做法
- 句子：接著用 git add . 加入新 repository 中的檔案並暫存，再用 git commit 完成第一次 commit。
- 來源：S07
- 原句：
  - Add the files in your new local repository. This stages them for the first commit.
  - $ git add .
  - Commit the files that you've staged in your local repository.

## 43｜git-init 指令範例
- 句子：GitHub Docs 的寫法，初始化時一併指定預設分支名稱（Git 2.28.0 以上），再加入檔案並暫存、commit。
- 來源：S07
- 原句：
  - git init -b main
  - $ git add .
  - $ git commit -m "First commit"

## 44｜remote 推上 GitHub
- 句子：用 git remote add origin REMOTE-URL 新增遠端，把 REMOTE-URL 換成 GitHub 上 repository 的完整網址，再用 git remote -v 確認遠端網址設定正確。
- 來源：S07
- 原句：
  - git remote add origin REMOTE-URL
  - Replace `REMOTE-URL` with the repository's full URL on GitHub.
  - To verify that you set the remote URL correctly, run the following command.
  - git remote -v

## 45｜git-push 推送到 GitHub
- 句子：用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。
- 來源：S07
- 原句：
  - Before you can add your local repository to GitHub using Git, you must authenticate to GitHub on the command line.

## 46｜git-push 推送到 GitHub
- 句子：GitHub Docs 用 git push origin main 把本地 repository 的變更推送到 GitHub，如果你的預設分支不叫 main，就換成你的預設分支名稱。
- 來源：S07
- 原句：
  - To push the changes in your local repository to GitHub, run the following command.
  - git push origin main
  - If your default branch is not named "main," replace "main" with the name of your default branch.

## 47｜git-push 誤解（新增）
- 句子：用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成 GitHub 的身分驗證。
- 來源：S07
- 原句：
  - you must authenticate to GitHub on the command line.

## 48｜git-push 時效註記（新增）
- 句子：S07 的 macOS 段落寫 git push -u origin main，Windows 與 Linux 段落寫 git push origin main。
- 來源：S07
- 原句：
  - git push -u origin main
  - git push origin main

## 49｜git-restore 時效註記（新增）
- 句子：S07 在 git add . 範例的註解中寫「To unstage a file, use 'git reset HEAD YOUR-FILE'」，也是舊做法的寫法。
- 來源：S07、S05
- 原句：
  - To unstage a file, use 'git reset HEAD YOUR-FILE'.
  - $ git reset HEAD CONTRIBUTING.md

## 50｜git-add 指令範例（新增）
- 句子：GitHub Docs 在新 repository 中加入檔案並暫存，準備第一次 commit 的寫法是 git add .。
- 來源：S07
- 原句：
  - Add the files in your new local repository. This stages them for the first commit.
  - $ git add .

## 51｜commit 誤解（新增）
- 句子：絕對不要把密碼、API key 之類的敏感資訊 add、commit 或 push 到遠端 repository。
- 來源：S07
- 原句：
  - Never `git add`, `commit`, or `push` sensitive information, for example passwords or API keys, to a remote repository.

## 52｜overview 第 13 項
- 句子：在本地 init、add、commit，在 GitHub 建立 repository，再用 git remote add origin 與 git push origin main 推上去。用 Git 推送到 GitHub 之前，必須先完成身分驗證。
- 來源：S07
- 原句：
  - Initialize the local directory as a Git repository.
  - $ git add .
  - $ git commit -m "First commit"
  - Create a new repository on GitHub.
  - git remote add origin REMOTE-URL
  - git push origin main
  - you must authenticate to GitHub on the command line.

## 53｜index S07 說明
- 句子：在 GitHub 建立 repository，把本地的程式碼推上去。
- 來源：S07
- 原句：
  - Create a new repository on GitHub.
  - To push the changes in your local repository to GitHub, run the following command.

## 54｜index push-to-github 說明
- 句子：從 git init 到 git push origin main 的完整流程。
- 來源：S07
- 原句：
  - git init -b main
  - git push origin main

## 55｜push-to-github 步驟三 1（lint 時改寫）
- 句子：在終端機中，切換到本地專案的資料夾。
- 來源：S07
- 原句：
  - Change the current working directory to your local project.

（第 55 筆是 S04～S09 lint 時改寫第 25 筆的句子，原因是原本的「目前的工作目錄」與 Git 的工作目錄（working tree）撞名。第 25 筆依「對照表只能往後新增」的規則保留原狀。）
