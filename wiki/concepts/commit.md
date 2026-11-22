# Commit（提交）

> Commit 是把你在暫存區準備好的快照記錄進專案歷史。每次 commit，都是記錄一份之後可以回復或拿來比較的專案快照。[S02]

## 白話解釋

暫存區設定成你想要的樣子之後，就可以 commit。[S02] 還沒暫存的變更，也就是建立或修改後還沒執行 `git add` 的檔案，不會進入這次 commit，而是以已修改的狀態留在磁碟上。[S02] 這些沒暫存的變更，之後可以再 commit 一次加進歷史。[S02]

每次 commit 時，Git 基本上會把所有檔案當下的樣子拍成一張快照並儲存起來。[S01] commit 之後的快照就很難遺失。[S01]

每個 commit 都會使用你設定的 `user.name` 與 `user.email`，而且會永久寫進 commit 裡，所以第一次 commit 之前，要先用 `git config` 設定好。[S03]

### 寫 commit 訊息

最簡單的 commit 方式是輸入 `git commit`，這會開啟你選擇的編輯器，通常是 vim 或 emacs，也可以用 `git config --global core.editor` 設定成其他編輯器。[S02] 編輯器中預設的 commit 訊息，包含被註解掉的最新 `git status` 輸出，以及最上方的一行空白。你可以刪掉這些註解、輸入自己的訊息，離開編輯器後，Git 就會用這個訊息建立 commit（註解會被去掉）。[S02]

如果沒有設定編輯器，Git 會使用系統預設的編輯器。沒有設定好編輯器時，Git 開啟它可能會讓你陷入非常混亂的狀態。[S03]

另一種方式是在 `-m` 後面直接寫 commit 訊息，這樣就不會開啟編輯器。[S02]

### 跳過暫存區

暫存區很適合精確地安排每次 commit 的內容，但有時比你的工作流程需要的更複雜。[S02] 在 `git commit` 加上 `-a`，Git 會在 commit 前自動暫存所有「已經追蹤」的檔案，讓你跳過 `git add`。[S02]

### 修正上一個 commit（`--amend`）

常見的復原情況之一，是太早 commit，可能忘了加某些檔案，或把 commit 訊息寫錯。[S05] 想重做這個 commit，就先補上忘記的修改並暫存，再用 `--amend` 重新 commit。[S05] 這個指令會用暫存區的內容來 commit。如果上次 commit 之後沒有任何變更，快照會完全一樣，改變的只有 commit 訊息。[S05] 它會開啟同一個 commit 訊息編輯器，裡面已經有上一個 commit 的訊息。[S05]

最後只會有一個 commit，第二次 commit 會取代第一次的結果。[S05] 要特別了解，amend 不是修正上一個 commit，而是用一個新的 commit 把它完全取代，就像上一個 commit 從來沒發生過，也不會出現在 repository 的歷史中。[S05] 它的好處是可以小幅改進最後一個 commit，不必在歷史中留下「Oops, forgot to add a file」這類的 commit 訊息。[S05]

**只能 amend 還在本地、還沒 push 到任何地方的 commit。** 已經 push 過的 commit 再 amend 並強制推送，會造成協作者的問題。[S05] push 的說明見 [git push（推送到遠端）](git-push.md)。[S06]

## 指令範例

開啟編輯器寫 commit 訊息：[S02]

```console
$ git commit
```

在新建立的 repository 中做第一次 commit，流程是先 `git add` 再 `git commit`，見 [git init（建立 repository）](git-init.md)。[S04]

在 `-m` 後面直接寫 commit 訊息：[S02]

```console
$ git commit -m "Story 182: fix benchmarks for speed"
[master 463dc4f] Story 182: fix benchmarks for speed
 2 files changed, 2 insertions(+)
 create mode 100644 README
```

輸出中可以看到：commit 到哪個分支（`master`）、這個 commit 的 SHA-1 檢查碼（`463dc4f`）、改了幾個檔案，以及新增與刪除幾行的統計。[S02]

用 `-a` 跳過暫存區，自動暫存已追蹤的檔案再 commit：[S02]

```console
$ git commit -a -m 'Add new benchmarks'
[master 83e38c7] Add new benchmarks
 1 file changed, 5 insertions(+), 0 deletions(-)
```

commit 之後才發現忘了暫存某個檔案，補上後用 `--amend` 重新 commit：[S05]

```console
$ git commit -m 'Initial commit'
$ git add forgotten_file
$ git commit --amend
```

## 新手常見誤解

- **以為 commit 會包含所有改過的檔案**：commit 只記錄暫存區的快照，改過但沒有執行 `git add` 的檔案，不會進入這次 commit。[S02]
- **以為 `git add` 之後再改檔案，commit 會包含最新的版本**：commit 進去的是最後一次執行 `git add` 時的版本，之後的修改要再 add 一次。[S02]
- **用 `git commit -a` 省事，卻包進不想要的變更**：`-a` 會把所有已追蹤且有變更的檔案都暫存起來，很方便，但有時會把不想要的變更也包進 commit。[S02] 而且 `-a` 只會自動暫存「已經追蹤」的檔案。[S02]
- **以為 `--amend` 只是修改上一個 commit**：它是用新的 commit 把上一個 commit 完全取代，舊的 commit 不會出現在 repository 的歷史中。[S05]
- **以為已經 push 的 commit 也可以隨意 amend**：只能 amend 還沒 push 的 commit，已經 push 過再 amend 並強制推送，會造成協作者的問題。[S05]

## 時效註記

- 範例輸出中的分支名稱是 `master`，過時說法、現行做法與簡報的處理方式，見 [預設分支名稱（master 與 main）](default-branch.md)。[S02] [S03]

## 相關頁面

- [三種狀態與三個區域](three-states.md)：commit 就是把已暫存的內容變成已提交
- [git config（Git 設定）](git-config.md)：第一次 commit 前要設定名稱與 email
- [預設分支名稱（master 與 main）](default-branch.md)：commit 輸出中的分支名稱
- [git add（加入暫存區）](git-add.md)：commit 之前要先把變更加入暫存區
- [git restore（復原檔案）](git-restore.md)：復原還沒 commit 的變更
- [git status（查看檔案狀態）](git-status.md)：commit 前確認哪些變更已經暫存
- [Git](git.md)：commit 記錄的是快照，以及 SHA-1 檢查碼
- [git push（推送到遠端）](git-push.md)：commit 之後，用 push 分享到遠端

## 來源

- [S01｜Pro Git 1.1 About Version Control、1.3 What is Git?](../sources/S01-progit-version-control-and-what-is-git.md)
- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
- [S04｜Pro Git 2.1 Git Basics - Getting a Git Repository](../sources/S04-progit-getting-a-git-repository.md)
- [S05｜Pro Git 2.4 Git Basics - Undoing Things](../sources/S05-progit-undoing-things.md)
- [S06｜Pro Git 2.5 Git Basics - Working with Remotes](../sources/S06-progit-working-with-remotes.md)
