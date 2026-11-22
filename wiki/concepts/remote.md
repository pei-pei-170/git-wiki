# Remote（遠端 repository）

> 遠端 repository 是放在網際網路或某個網路上的專案版本。[S06]

## 白話解釋

要在任何 Git 專案中協作，你需要知道如何管理遠端 repository。[S06] 你可以有好幾個遠端 repository，每一個對你來說通常是唯讀，或是可讀可寫。[S06] 和別人協作，就是管理這些遠端 repository，並在需要分享工作時，對它們推送（push）和拉取（pull）資料。[S06]

「遠端」不一定代表 repository 在網路上的別台電腦，只代表它在「別的地方」，它甚至可以和你在同一台電腦上。[S06]

### origin

clone 下來的 repository，至少會有一個名為 origin 的遠端，這是 Git 替你 clone 的來源伺服器取的預設名稱。[S06] `git clone` 會自動幫你加上 origin 這個遠端，想明確新增遠端時，可以用 `git remote add`。[S06]

### 查看遠端

`git remote` 會列出每個遠端的簡稱。[S06] 加上 `-v`，會顯示 Git 為這個簡稱儲存的網址，分別用在讀取（fetch）與寫入（push）。[S06]

### 新增遠端

執行 `git remote add <shortname> <url>`，可以新增一個遠端，並取一個方便引用的簡稱。[S06] 之後在指令中，就可以用這個簡稱代替完整的網址。[S06]

推上 GitHub 時，GitHub Docs 的做法是用 `git remote add origin REMOTE-URL` 新增遠端，把 `REMOTE-URL` 換成 GitHub 上 repository 的完整網址，再用 `git remote -v` 確認遠端網址設定正確，完整流程見 [把本地 repository 推上 GitHub](push-to-github.md)。[S07]

## 指令範例

clone 一個 repository 後，查看它的遠端：[S06]

```console
$ git clone https://github.com/schacon/ticgit
Cloning into 'ticgit'...
remote: Reusing existing pack: 1857, done.
remote: Total 1857 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (1857/1857), 374.35 KiB | 268.00 KiB/s, done.
Resolving deltas: 100% (772/772), done.
Checking connectivity... done.
$ cd ticgit
$ git remote
origin
```

顯示遠端的網址：[S06]

```console
$ git remote -v
origin	https://github.com/schacon/ticgit (fetch)
origin	https://github.com/schacon/ticgit (push)
```

新增一個名為 `pb` 的遠端：[S06]

```console
$ git remote
origin
$ git remote add pb https://github.com/paulboone/ticgit
$ git remote -v
origin	https://github.com/schacon/ticgit (fetch)
origin	https://github.com/schacon/ticgit (push)
pb	https://github.com/paulboone/ticgit (fetch)
pb	https://github.com/paulboone/ticgit (push)
```

## 新手常見誤解

- **以為「遠端」一定在別台電腦上**：遠端 repository 也可以和你在同一台電腦上，「遠端」只代表它在別的地方。[S06]
- **以為每次都要輸入完整的網址**：用 `git remote add` 新增遠端之後，就可以在指令中用簡稱代替完整的網址。[S06]

## 時效註記

- 原文範例中的遠端使用了多種傳輸協定，例如 `https://`、`git://` 與 `git@github.com:`。本專案沒有較新的資料確認這些協定的現況，簡報也不放傳輸協定。[S06]

## 相關頁面

- [git push（推送到遠端）](git-push.md)：把 commit 推送到遠端
- [git clone（複製 repository）](git-clone.md)：clone 會自動加上 origin
- [Repository（儲存庫）](repository.md)：遠端 repository 也是一個 repository
- [版本控制（Version Control）](version-control.md)：分散式版本控制可以同時搭配多個遠端
- [把本地 repository 推上 GitHub](push-to-github.md)：用 `git remote add origin` 連到 GitHub

## 來源

- [S06｜Pro Git 2.5 Git Basics - Working with Remotes](../sources/S06-progit-working-with-remotes.md)
- [S07｜Adding locally hosted code to GitHub](../sources/S07-github-adding-locally-hosted-code.md)
