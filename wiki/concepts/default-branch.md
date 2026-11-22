# 預設分支名稱（master 與 main）

> 用 `git init` 建立新 repository 時，Git 預設會建立名為 master 的分支，從 Git 2.28 起，可以設定成其他名稱，例如 main。[S03]

## 白話解釋

**Git 本身**：用 `git init` 建立新 repository 時，Git 預設會建立名為 master 的分支。[S03] 從 Git 2.28 起，可以用 `init.defaultBranch` 設定新 repository 的初始分支名稱。[S03] 《Pro Git》因為 Git 本身仍以 master 為預設，所以全書的範例都使用 master。[S02]

**GitHub 等平台**：GitHub 在 2020 年中把預設分支名稱從 master 改成 main，其他 Git 平台也跟進，所以有些新建立的 repository，預設分支名稱是 main 而不是 master。[S02] 預設分支名稱也可以修改，所以你也可能看到其他名稱。[S02]

### 本專案簡報的改編決定

這是 S03 ingest 討論時，使用者確認的簡報處理方式，簡報中的範例輸出依此頁改編。（S03 討論）

- **決定**：簡報先教 `git config --global init.defaultBranch main`，之後的範例輸出，一律把分支名稱寫成 main，並在範例下方註明「輸出改編自 S02，分支名稱依 S03 的設定改為 main」。（S03 討論）範例指令也比照辦理，例如 `git push origin master` 改成 `git push origin main`。（S06 討論）
- **依據一（S03）**：從 Git 2.28 起，可以用 `init.defaultBranch` 把新 repository 的初始分支名稱設成 main。[S03]
- **依據二（S02）**：GitHub 在 2020 年中把預設分支名稱改成 main，其他 Git 平台也跟進。[S02, 2020]
- **佐證（S06）**：`git clone` 會讓本地的 master 分支，追蹤 clone 來源伺服器上的遠端 master 分支，原文特別寫了「或不論預設分支叫什麼名字」。[S06]
- **待補依據（S07）**：S07 的文件本身就使用 `git push origin main`，ingest S07 後補上，作為這個指令的直接依據。（S06 討論）
- **為什麼改**：S02 的範例輸出都是 master [S02]。如果照抄，學生在 GitHub 上看到的 main，會和範例中的 master 不一致，新手可能被兩種名稱弄混。設定 `init.defaultBranch main` 之後，學生自己建立的 repository 也會是 main，與 GitHub 新 repository 的預設一致。[S02] [S03]
- **改編範圍**：只把範例指令與輸出中的分支名稱 master 改成 main，其他內容照原文。輸出的例子有 `On branch master` 改成 `On branch main`、`'origin/master'` 改成 `'origin/main'`、`[master 463dc4f]` 改成 `[main 463dc4f]`。（S03 討論）指令的例子有 `git push origin master` 改成 `git push origin main`，範圍原本只有範例輸出，S06 討論時擴大到範例指令。（S06 討論）
- **前提**：`init.defaultBranch` 要 Git 2.28 以上的版本才能使用。[S03]
- **例外**：說明「Git 本身預設是 master」的投影片，要加上 `data-legacy` 屬性。（S03 討論）
- **時效的寫法**：「Git 本身預設是 master」沒有更新的資料可以確認，也不另外找來源。簡報如果要提到這一點，要寫成「依 Pro Git 線上版，2026-11-22 擷取」。（lint 討論）

## 指令範例

把新 repository 的預設分支名稱設成 main：[S03]

```console
$ git config --global init.defaultBranch main
```

## 新手常見誤解

- **以為 Git 本身的預設就是 main**：用 `git init` 建立新 repository 時，Git 預設仍會建立 master。main 是 GitHub 等平台新 repository 的預設，或是你自己用 `init.defaultBranch` 設定的結果。[S02] [S03]
- **以為 `init.defaultBranch` 會把已經存在的分支改名**：它設定的是用 `git init` 建立新 repository 時的初始分支名稱。[S03]

## 時效註記

> ⚠️ 過時：《Pro Git》範例輸出中的分支名稱是 `master` [S02, 2014]。
> 現行做法：GitHub 在 2020 年中把預設分支名稱從 `master` 改成 `main`，其他 Git 平台也跟進，但 Git 本身仍以 `master` 為預設，而且預設分支名稱可以修改 [S02, 2020]。從 Git 2.28 起，可以用 `init.defaultBranch` 設定新 repository 的初始分支名稱 [S03]。

- 「Git 本身預設是 master」這個說法有時效性，目前沒有更新的資料可以確認。本專案不另外找來源，簡報的寫法見上方「時效的寫法」。[S02] [S03]
- 其他頁面範例輸出中的 master，都用一行連結指到這裡，這組過時／現行做法只寫在本頁。（lint 討論）

## 相關頁面

- [git config（Git 設定）](git-config.md)：`init.defaultBranch` 也是一項 Git 設定
- [git status（查看檔案狀態）](git-status.md)：輸出的第一行會顯示目前所在的分支
- [Commit（提交）](commit.md)：commit 的輸出會顯示 commit 到哪個分支
- [git push（推送到遠端）](git-push.md)：push 指令中要寫出分支名稱

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
- [S06｜Pro Git 2.5 Git Basics - Working with Remotes](../sources/S06-progit-working-with-remotes.md)
