# Commit（提交）

> Commit 是把你在暫存區準備好的快照記錄進專案歷史；每次 commit，都是記錄一份之後可以回復或拿來比較的專案快照。[S02]

## 白話解釋

暫存區設定成你想要的樣子之後，就可以 commit。[S02] 還沒暫存的變更，也就是建立或修改後還沒執行 `git add` 的檔案，不會進入這次 commit，而是以已修改的狀態留在磁碟上。[S02] 這些沒暫存的變更，之後可以再 commit 一次加進歷史。[S02]

每次 commit 時，Git 基本上會把所有檔案當下的樣子拍成一張快照並儲存起來。[S01] commit 之後的快照就很難遺失。[S01]

每個 commit 都會使用你設定的 `user.name` 與 `user.email`，而且會永久寫進 commit 裡，所以第一次 commit 之前，要先用 `git config` 設定好。[S03]

### 寫 commit 訊息

最簡單的 commit 方式是輸入 `git commit`，這會開啟你選擇的編輯器，通常是 vim 或 emacs，也可以用 `git config --global core.editor` 設定成其他編輯器。[S02] 編輯器中預設的 commit 訊息，包含被註解掉的最新 `git status` 輸出，以及最上方的一行空白；你可以刪掉這些註解、輸入自己的訊息，離開編輯器後，Git 就會用這個訊息建立 commit（註解會被去掉）。[S02]

如果沒有設定編輯器，Git 會使用系統預設的編輯器；沒有設定好編輯器時，Git 開啟它可能會讓你陷入非常混亂的狀態。[S03]

另一種方式是在 `-m` 後面直接寫 commit 訊息，這樣就不會開啟編輯器。[S02]

### 跳過暫存區

暫存區很適合精確地安排每次 commit 的內容，但有時比你的工作流程需要的更複雜。[S02] 在 `git commit` 加上 `-a`，Git 會在 commit 前自動暫存所有「已經追蹤」的檔案，讓你跳過 `git add`。[S02]

## 指令範例

開啟編輯器寫 commit 訊息：[S02]

```console
$ git commit
```

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

## 新手常見誤解

- **以為 commit 會包含所有改過的檔案**：commit 只記錄暫存區的快照；改過但沒有執行 `git add` 的檔案，不會進入這次 commit。[S02]
- **以為 `git add` 之後再改檔案，commit 會包含最新的版本**：commit 進去的是最後一次執行 `git add` 時的版本；之後的修改要再 add 一次。[S02]
- **用 `git commit -a` 省事，卻包進不想要的變更**：`-a` 會把所有已追蹤且有變更的檔案都暫存起來，很方便，但有時會把不想要的變更也包進 commit。[S02] 而且 `-a` 只會自動暫存「已經追蹤」的檔案。[S02]

## 時效註記

> ⚠️ 過時：原文範例輸出中的分支名稱是 `master` [S02, 2014]。
> 現行做法：GitHub 在 2020 年中把預設分支名稱從 `master` 改成 `main`，其他 Git 平台也跟進；但 Git 本身仍以 `master` 為預設，而且預設分支名稱可以修改 [S02, 2020]。從 Git 2.28 起，可以用 `init.defaultBranch` 設定新 repository 的初始分支名稱 [S03]。

- 簡報如何處理範例輸出中的 master，見 [預設分支名稱（master 與 main）](default-branch.md)。[S02] [S03]

## 相關頁面

- [三種狀態與三個區域](three-states.md)：commit 就是把已暫存的內容變成已提交
- [git config（Git 設定）](git-config.md)：第一次 commit 前要設定名稱與 email
- [預設分支名稱（master 與 main）](default-branch.md)：commit 輸出中的分支名稱
- [git add（加入暫存區）](git-add.md)：commit 之前要先把變更加入暫存區
- [git status（查看檔案狀態）](git-status.md)：commit 前確認哪些變更已經暫存
- [Git](git.md)：commit 記錄的是快照，以及 SHA-1 檢查碼

## 來源

- [S01｜Pro Git 1.1 About Version Control；1.3 What is Git?](../sources/S01-progit-version-control-and-what-is-git.md)
- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
