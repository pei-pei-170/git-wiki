# S06｜Pro Git 2.5 Git Basics - Working with Remotes

- 來源：[2.5 Git Basics - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)（《Pro Git》第 2 版，Scott Chacon、Ben Straub 著，CC BY-NC-SA 3.0）
- 年份：2014（第 2 版印刷版年份，本次取得日期為 2026-11-22）
- 時效風險：中（指令本身穩定，但範例使用 master 與多種傳輸協定，並提到 Git 2.27 起的 pull 警告）

## 重點

1. 遠端 repository 是放在網際網路或某個網路上的專案版本，可以有好幾個，每個通常是唯讀或可讀可寫。和別人協作，就是管理這些遠端 repository，並在需要分享工作時對它們 push 和 pull 資料。[S06]
2. `git remote` 列出已設定的遠端簡稱，加上 `-v` 會顯示網址。clone 下來的 repository 至少會有 `origin`，這是 Git 替 clone 來源伺服器取的預設名稱。[S06]
3. `git remote add <shortname> <url>` 可以明確新增一個遠端，之後就能用簡稱代替完整網址。[S06]
4. `git fetch` 只把資料下載到本地，不會自動合併。`git pull` 會自動 fetch，再合併到目前的分支（見下方補充）。[S06]
5. `git push <remote> <branch>` 把 commit 推送到遠端，例如 `git push origin master`。只有在你對伺服器有寫入權限，而且這段時間沒有別人先 push 時，這個指令才會成功。[S06]
6. `git remote show` 查看遠端的詳細資訊，`git remote rename`、`git remote remove` 用來改名與移除遠端（見下方補充）。[S06]

## 影響的 wiki 頁面

- 新增 [Remote（遠端 repository）](../concepts/remote.md)
- 新增 [git push（推送到遠端）](../concepts/git-push.md)
- 更新 [git clone（複製 repository）](../concepts/git-clone.md)：clone 會自動加上 origin，並設定本地分支追蹤遠端分支
- 更新 [Commit（提交）](../concepts/commit.md)：「只能 amend 還沒 push 的 commit」連到 git push
- 更新 [預設分支名稱（master 與 main）](../concepts/default-branch.md)：改編範圍擴大成範例指令與輸出，並補上 S06 的佐證

## 與其他資料的衝突或過時之處

- 與既有 wiki 沒有矛盾。S06 補充了 S04 沒有提到的部分：clone 會自動加上名為 origin 的遠端。[S06]
- S06 說可以有好幾個遠端 repository [S06]，與 S01「這類系統大多也能同時搭配多個遠端儲存庫」的說法一致 [S01]。
- 範例指令與輸出中的分支名稱是 master，處理方式見 [預設分支名稱（master 與 main）](../concepts/default-branch.md)。[S06]
- 範例中的遠端使用了多種傳輸協定，例如 `https://`、`git://` 與 `git@github.com:`，簡報不放傳輸協定。[S06]

## 補充：fetch 與 pull（不建概念頁、不放進簡報）

- `git fetch <remote>` 會連到遠端專案，下載所有你還沒有的資料。之後你會有那個遠端所有分支的參照，可以隨時合併或查看。[S06]
- clone 時，Git 會自動把來源 repository 加成名為 origin 的遠端，所以 `git fetch origin` 會取得自從 clone（或上次 fetch）之後，別人推送到那台伺服器的新工作。[S06]
- `git fetch` 只把資料下載到本地 repository，不會自動和你的工作合併，也不會改動你正在做的東西，準備好時要自己手動合併。[S06]
- 如果目前的分支設定為追蹤某個遠端分支，可以用 `git pull` 自動 fetch，再把那個遠端分支合併到目前的分支。[S06] 預設上，`git clone` 會自動讓本地的 master 分支，追蹤 clone 來源伺服器上的遠端 master 分支（或不論預設分支叫什麼名字）。[S06]
- 從 Git 2.27 起，如果沒有設定 `pull.rebase`，`git pull` 會發出警告，直到你設定為止。想要 Git 的預設行為（能 fast-forward 就 fast-forward，否則建立合併 commit），執行 `git config --global pull.rebase "false"`。想在 pull 時 rebase，執行 `git config --global pull.rebase "true"`。[S06]

## 補充：git remote show、rename、remove（不建概念頁、不放進簡報）

- `git remote show <remote>` 會列出遠端 repository 的網址與追蹤分支的資訊，也會列出它下載過的所有遠端參照。[S06]
- `git remote rename` 可以改遠端的簡稱，這也會改掉所有遠端追蹤分支的名稱，例如原本的 `pb/master` 會變成 `paul/master`。[S06]
- `git remote remove` 或 `git remote rm` 可以移除遠端，例如搬了伺服器、不再使用某個鏡像，或某位貢獻者不再貢獻時。移除後，與那個遠端相關的所有遠端追蹤分支與設定也都會被刪除。[S06]
