# S06 逐句核對

- 對象：S06（Pro Git 2.5 Working with Remotes）ingest 時新增或修改的事實陳述
- 不列入核對：標註「（Sxx 討論）」的專案決定（例如 default-branch.md 的改編範圍擴大），以及 overview.md「簡報範圍決定」中的取捨
- 核對日期：2026-11-22
- 驗證方式：`python tools/verify_quotes.py checks/S06-quotes.md`

## 1｜sources/S06 重點 1
- 句子：遠端 repository 是放在網際網路或某個網路上的專案版本，可以有好幾個，每個通常是唯讀或可讀可寫。
- 來源：S06
- 原句：
  - Remote repositories are versions of your project that are hosted on the Internet or network somewhere.
  - You can have several of them, each of which generally is either read-only or read/write for you.

## 2｜sources/S06 重點 1
- 句子：和別人協作，就是管理這些遠端 repository，並在需要分享工作時對它們 push 和 pull 資料。
- 來源：S06
- 原句：
  - Collaborating with others involves managing these remote repositories and pushing and pulling data to and from them when you need to share work.

## 3｜sources/S06 重點 2
- 句子：git remote 列出已設定的遠端簡稱，加上 -v 會顯示網址。
- 來源：S06
- 原句：
  - To see which remote servers you have configured, you can run the `git remote` command.
  - It lists the shortnames of each remote handle you’ve specified.
  - You can also specify `-v`, which shows you the URLs that Git has stored for the shortname

## 4｜sources/S06 重點 2
- 句子：clone 下來的 repository 至少會有 origin，這是 Git 替 clone 來源伺服器取的預設名稱。
- 來源：S06
- 原句：
  - If you’ve cloned your repository, you should at least see `origin` — that is the default name Git gives to the server you cloned from:

## 5｜sources/S06 重點 3
- 句子：git remote add <shortname> <url> 可以明確新增一個遠端，之後就能用簡稱代替完整網址。
- 來源：S06
- 原句：
  - Here’s how to add a new remote explicitly.
  - To add a new remote Git repository as a shortname you can reference easily, run `git remote add <shortname> <url>`:
  - Now you can use the string `pb` on the command line instead of the whole URL.

## 6｜sources/S06 重點 4
- 句子：git fetch 只把資料下載到本地，不會自動合併。
- 來源：S06
- 原句：
  - It’s important to note that the `git fetch` command only downloads the data to your local repository — it doesn’t automatically merge it with any of your work

## 7｜sources/S06 重點 4
- 句子：git pull 會自動 fetch，再合併到目前的分支。
- 來源：S06
- 原句：
  - you can use the `git pull` command to automatically fetch and then merge that remote branch into your current branch.

## 8｜sources/S06 重點 5
- 句子：git push <remote> <branch> 把 commit 推送到遠端，例如 git push origin master。
- 來源：S06
- 原句：
  - The command for this is simple: `git push <remote> <branch>`.
  - then you can run this to push any commits you’ve done back up to the server:
  - $ git push origin master

## 9｜sources/S06 重點 5
- 句子：只有在你對伺服器有寫入權限，而且這段時間沒有別人先 push 時，這個指令才會成功。
- 來源：S06
- 原句：
  - This command works only if you cloned from a server to which you have write access and if nobody has pushed in the meantime.

## 10｜sources/S06 重點 6
- 句子：git remote show 查看遠端的詳細資訊，git remote rename、git remote remove 用來改名與移除遠端。
- 來源：S06
- 原句：
  - If you want to see more information about a particular remote, you can use the `git remote show <remote>` command.
  - You can run `git remote rename` to change a remote’s shortname.
  - you can either use `git remote remove` or `git remote rm`:

## 11｜sources/S06 時效風險
- 句子：範例使用 master 與多種傳輸協定，並提到 Git 2.27 起的 pull 警告。
- 來源：S06
- 原句：
  - $ git push origin master
  - Notice that these remotes use a variety of protocols
  - From Git version 2.27 onward, `git pull` will give a warning if the `pull.rebase` variable is not set.

## 12｜sources/S06 衝突 1
- 句子：S06 補充了 S04 沒有提到的部分：clone 會自動加上名為 origin 的遠端。
- 來源：S06
- 原句：
  - We’ve mentioned and given some demonstrations of how the `git clone` command implicitly adds the `origin` remote for you.

## 13｜sources/S06 衝突 2
- 句子：S06 說可以有好幾個遠端 repository，與 S01「這類系統大多也能同時搭配多個遠端儲存庫」的說法一致。
- 來源：S06、S01
- 原句：
  - You can have several of them
  - many of these systems deal pretty well with having several remote repositories they can work with

## 14｜sources/S06 衝突 3
- 句子：範例指令與輸出中的分支名稱是 master。
- 來源：S06
- 原句：
  - $ git push origin master
  - HEAD branch: master

## 15｜sources/S06 衝突 4
- 句子：範例中的遠端使用了多種傳輸協定，例如 https://、git:// 與 git@github.com:。
- 來源：S06
- 原句：
  - Notice that these remotes use a variety of protocols
  - origin	https://github.com/schacon/ticgit (fetch)
  - koke      git://github.com/koke/grit.git (fetch)
  - origin    git@github.com:mojombo/grit.git (fetch)

## 16｜sources/S06 補充 fetch
- 句子：git fetch <remote> 會連到遠端專案，下載所有你還沒有的資料。之後你會有那個遠端所有分支的參照，可以隨時合併或查看。
- 來源：S06
- 原句：
  - The command goes out to that remote project and pulls down all the data from that remote project that you don’t have yet.
  - After you do this, you should have references to all the branches from that remote, which you can merge in or inspect at any time.

## 17｜sources/S06 補充 fetch
- 句子：clone 時，Git 會自動把來源 repository 加成名為 origin 的遠端，所以 git fetch origin 會取得自從 clone（或上次 fetch）之後，別人推送到那台伺服器的新工作。
- 來源：S06
- 原句：
  - If you clone a repository, the command automatically adds that remote repository under the name “origin”.
  - So, `git fetch origin` fetches any new work that has been pushed to that server since you cloned (or last fetched from) it.

## 18｜sources/S06 補充 fetch
- 句子：git fetch 只把資料下載到本地 repository，不會自動和你的工作合併，也不會改動你正在做的東西，準備好時要自己手動合併。
- 來源：S06
- 原句：
  - only downloads the data to your local repository — it doesn’t automatically merge it with any of your work or modify what you’re currently working on.
  - You have to merge it manually into your work when you’re ready.

## 19｜sources/S06 補充 pull
- 句子：如果目前的分支設定為追蹤某個遠端分支，可以用 git pull 自動 fetch，再把那個遠端分支合併到目前的分支。
- 來源：S06
- 原句：
  - If your current branch is set up to track a remote branch
  - you can use the `git pull` command to automatically fetch and then merge that remote branch into your current branch.

## 20｜sources/S06 補充 pull
- 句子：預設上，git clone 會自動讓本地的 master 分支，追蹤 clone 來源伺服器上的遠端 master 分支（或不論預設分支叫什麼名字）。
- 來源：S06
- 原句：
  - by default, the `git clone` command automatically sets up your local `master` branch to track the remote `master` branch (or whatever the default branch is called) on the server you cloned from.

## 21｜sources/S06 補充 pull.rebase
- 句子：從 Git 2.27 起，如果沒有設定 pull.rebase，git pull 會發出警告，直到你設定為止。
- 來源：S06
- 原句：
  - From Git version 2.27 onward, `git pull` will give a warning if the `pull.rebase` variable is not set.
  - Git will keep warning you until you set the variable.

## 22｜sources/S06 補充 pull.rebase
- 句子：想要 Git 的預設行為（能 fast-forward 就 fast-forward，否則建立合併 commit），執行 git config --global pull.rebase "false"。想在 pull 時 rebase，執行 git config --global pull.rebase "true"。
- 來源：S06
- 原句：
  - If you want the default behavior of Git (fast-forward if possible, else create a merge commit):
  - `git config --global pull.rebase "false"`
  - If you want to rebase when pulling:
  - `git config --global pull.rebase "true"`

## 23｜sources/S06 補充 remote show
- 句子：git remote show <remote> 會列出遠端 repository 的網址與追蹤分支的資訊，也會列出它下載過的所有遠端參照。
- 來源：S06
- 原句：
  - It lists the URL for the remote repository as well as the tracking branch information.
  - It also lists all the remote references it has pulled down.

## 24｜sources/S06 補充 rename
- 句子：git remote rename 可以改遠端的簡稱，這也會改掉所有遠端追蹤分支的名稱，例如原本的 pb/master 會變成 paul/master。
- 來源：S06
- 原句：
  - You can run `git remote rename` to change a remote’s shortname.
  - It’s worth mentioning that this changes all your remote-tracking branch names, too.
  - What used to be referenced at `pb/master` is now at `paul/master`.

## 25｜sources/S06 補充 remove
- 句子：git remote remove 或 git remote rm 可以移除遠端，例如搬了伺服器、不再使用某個鏡像，或某位貢獻者不再貢獻時。
- 來源：S06
- 原句：
  - If you want to remove a remote for some reason — you’ve moved the server or are no longer using a particular mirror, or perhaps a contributor isn’t contributing anymore — you can either use `git remote remove` or `git remote rm`:

## 26｜sources/S06 補充 remove
- 句子：移除後，與那個遠端相關的所有遠端追蹤分支與設定也都會被刪除。
- 來源：S06
- 原句：
  - Once you delete the reference to a remote this way, all remote-tracking branches and configuration settings associated with that remote are also deleted.

## 27｜remote 定義
- 句子：遠端 repository 是放在網際網路或某個網路上的專案版本。
- 來源：S06
- 原句：
  - Remote repositories are versions of your project that are hosted on the Internet or network somewhere.

## 28｜remote 白話
- 句子：要在任何 Git 專案中協作，你需要知道如何管理遠端 repository。
- 來源：S06
- 原句：
  - To be able to collaborate on any Git project, you need to know how to manage your remote repositories.

## 29｜remote 白話
- 句子：你可以有好幾個遠端 repository，每一個對你來說通常是唯讀，或是可讀可寫。
- 來源：S06
- 原句：
  - You can have several of them, each of which generally is either read-only or read/write for you.

## 30｜remote 白話
- 句子：和別人協作，就是管理這些遠端 repository，並在需要分享工作時，對它們推送（push）和拉取（pull）資料。
- 來源：S06
- 原句：
  - Collaborating with others involves managing these remote repositories and pushing and pulling data to and from them when you need to share work.

## 31｜remote 白話
- 句子：「遠端」不一定代表 repository 在網路上的別台電腦，只代表它在「別的地方」，它甚至可以和你在同一台電腦上。
- 來源：S06
- 原句：
  - It is entirely possible that you can be working with a “remote” repository that is, in fact, on the same host you are.
  - The word “remote” does not necessarily imply that the repository is somewhere else on the network or Internet, only that it is elsewhere.

## 32｜remote origin
- 句子：clone 下來的 repository，至少會有一個名為 origin 的遠端，這是 Git 替你 clone 的來源伺服器取的預設名稱。
- 來源：S06
- 原句：
  - If you’ve cloned your repository, you should at least see `origin` — that is the default name Git gives to the server you cloned from:

## 33｜remote origin
- 句子：git clone 會自動幫你加上 origin 這個遠端，想明確新增遠端時，可以用 git remote add。
- 來源：S06
- 原句：
  - how the `git clone` command implicitly adds the `origin` remote for you.
  - Here’s how to add a new remote explicitly.

## 34｜remote 查看遠端
- 句子：git remote 會列出每個遠端的簡稱。
- 來源：S06
- 原句：
  - It lists the shortnames of each remote handle you’ve specified.

## 35｜remote 查看遠端
- 句子：加上 -v，會顯示 Git 為這個簡稱儲存的網址，分別用在讀取（fetch）與寫入（push）。
- 來源：S06
- 原句：
  - which shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote:
  - origin	https://github.com/schacon/ticgit (fetch)
  - origin	https://github.com/schacon/ticgit (push)

## 36｜remote 新增遠端
- 句子：執行 git remote add <shortname> <url>，可以新增一個遠端，並取一個方便引用的簡稱。之後在指令中，就可以用這個簡稱代替完整的網址。
- 來源：S06
- 原句：
  - To add a new remote Git repository as a shortname you can reference easily, run `git remote add <shortname> <url>`:
  - Now you can use the string `pb` on the command line instead of the whole URL.

## 37｜remote 誤解 1
- 句子：遠端 repository 也可以和你在同一台電腦上，「遠端」只代表它在別的地方。
- 來源：S06
- 原句：
  - on the same host you are.
  - only that it is elsewhere.

## 38｜remote 誤解 2
- 句子：用 git remote add 新增遠端之後，就可以在指令中用簡稱代替完整的網址。
- 來源：S06
- 原句：
  - Now you can use the string `pb` on the command line instead of the whole URL.

## 39｜remote 時效註記
- 句子：原文範例中的遠端使用了多種傳輸協定，例如 https://、git:// 與 git@github.com:。
- 來源：S06
- 原句：
  - Notice that these remotes use a variety of protocols
  - koke      git://github.com/koke/grit.git (fetch)
  - origin    git@github.com:mojombo/grit.git (fetch)

## 40｜git-push 定義
- 句子：git push <remote> <branch> 會把你做過的 commit 推送到遠端伺服器，讓專案可以分享給別人。
- 來源：S06
- 原句：
  - The command for this is simple: `git push <remote> <branch>`.
  - then you can run this to push any commits you’ve done back up to the server:
  - When you have your project at a point that you want to share, you have to push it upstream.

## 41｜git-push 白話
- 句子：commit 只會記錄在你本地的副本裡，等有網路連線時再上傳。
- 來源：S01
- 原句：
  - you can commit happily (to your *local* copy, remember?) until you get to a network connection to upload.

## 42｜git-push 白話
- 句子：當專案到了你想分享的階段，就要把它推送到上游（upstream）。指令很簡單：git push <remote> <branch>。
- 來源：S06
- 原句：
  - When you have your project at a point that you want to share, you have to push it upstream.
  - The command for this is simple: `git push <remote> <branch>`.

## 43｜git-push 白話
- 句子：例如要把 master 分支推送到 origin 伺服器，而 clone 通常會自動幫你設定好這兩個名稱。
- 來源：S06
- 原句：
  - If you want to push your `master` branch to your `origin` server (again, cloning generally sets up both of those names for you automatically)

## 44｜git-push 成功的條件
- 句子：只有在兩個條件都成立時，git push 才會成功：你 clone 的伺服器你有寫入權限，而且這段時間沒有別人先 push。
- 來源：S06
- 原句：
  - This command works only if you cloned from a server to which you have write access and if nobody has pushed in the meantime.

## 45｜git-push 成功的條件
- 句子：如果你和別人同時 clone，他們先 push，你再 push，你的 push 就會被拒絕。
- 來源：S06
- 原句：
  - If you and someone else clone at the same time and they push upstream and then you push upstream, your push will rightly be rejected.

## 46｜git-push 成功的條件
- 句子：這時必須先取得他們的工作，整合進你的工作，才能再 push。
- 來源：S06
- 原句：
  - You’ll have to fetch their work first and incorporate it into yours before you’ll be allowed to push.

## 47｜git-push push 之後
- 句子：只能 amend 還在本地、還沒 push 到任何地方的 commit。已經 push 過的 commit 再 amend 並強制推送，會造成協作者的問題。
- 來源：S05
- 原句：
  - Only amend commits that are still local and have not been pushed somewhere.
  - Amending previously pushed commits and force pushing the branch will cause problems for your collaborators.

## 48｜git-push 誤解 1
- 句子：commit 只記錄在本地的副本，要 push 才會推送到遠端。
- 來源：S01、S06
- 原句：
  - to your *local* copy, remember?
  - you have to push it upstream.

## 49｜git-push 誤解 2
- 句子：沒有寫入權限，或別人先 push 了，你的 push 就會被拒絕。
- 來源：S06
- 原句：
  - This command works only if you cloned from a server to which you have write access and if nobody has pushed in the meantime.
  - your push will rightly be rejected.

## 50｜git-push 誤解 3
- 句子：已經 push 過的 commit 再 amend 並強制推送，會造成協作者的問題。
- 來源：S05
- 原句：
  - Amending previously pushed commits and force pushing the branch will cause problems for your collaborators.

## 51｜git-push 時效註記
- 句子：範例指令中的分支名稱是 master。
- 來源：S06
- 原句：
  - $ git push origin master

## 52｜git-clone 白話（更新）
- 句子：clone 時，Git 會自動把來源 repository 加成名為 origin 的遠端。
- 來源：S06
- 原句：
  - If you clone a repository, the command automatically adds that remote repository under the name “origin”.

## 53｜git-clone 白話（更新）
- 句子：預設上，git clone 也會自動讓本地的 master 分支，追蹤 clone 來源伺服器上的遠端 master 分支（或不論預設分支叫什麼名字）。
- 來源：S06
- 原句：
  - by default, the `git clone` command automatically sets up your local `master` branch to track the remote `master` branch (or whatever the default branch is called) on the server you cloned from.

## 54｜commit（更新）
- 句子：push 的說明見 git push（推送到遠端）。
- 來源：S06
- 原句：
  - The command for this is simple: `git push <remote> <branch>`.

## 55｜default-branch 佐證（S06）
- 句子：git clone 會讓本地的 master 分支，追蹤 clone 來源伺服器上的遠端 master 分支，原文特別寫了「或不論預設分支叫什麼名字」。
- 來源：S06
- 原句：
  - automatically sets up your local `master` branch to track the remote `master` branch (or whatever the default branch is called)

## 56｜overview 第 11 項
- 句子：放在網際網路或某個網路上的專案版本，clone 下來的 repository 會有名為 origin 的遠端，也可以用 git remote add 新增。
- 來源：S06
- 原句：
  - hosted on the Internet or network somewhere.
  - you should at least see `origin`
  - run `git remote add <shortname> <url>`:

## 57｜overview 第 12 項
- 句子：commit 只記錄在本地，要用 git push <remote> <branch> 推送到遠端。沒有寫入權限，或別人先 push 了，push 就會被拒絕。
- 來源：S01、S06
- 原句：
  - to your *local* copy, remember?
  - The command for this is simple: `git push <remote> <branch>`.
  - to which you have write access and if nobody has pushed in the meantime.
  - your push will rightly be rejected.

## 58｜index S06 說明
- 句子：遠端 repository：git remote、git push，以及 fetch、pull 與遠端的管理。
- 來源：S06
- 原句：
  - you can run the `git remote` command.
  - `git push <remote> <branch>`
  - $ git fetch <remote>
  - you can use the `git pull` command

## 59｜index remote 說明
- 句子：放在網際網路或某個網路上的專案版本，clone 時預設名稱為 origin。
- 來源：S06
- 原句：
  - hosted on the Internet or network somewhere.
  - that is the default name Git gives to the server you cloned from:

## 60｜index git-push 說明
- 句子：把 commit 推送到遠端，需要寫入權限，而且沒有別人先 push。
- 來源：S06
- 原句：
  - push any commits you’ve done back up to the server:
  - to which you have write access and if nobody has pushed in the meantime.
