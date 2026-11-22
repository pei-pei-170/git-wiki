# git diff（查看變更內容）

> `git diff` 會顯示確切新增與刪除了哪些行，比只列出檔名的 `git status` 更詳細。[S02]

## 白話解釋

`git diff` 最常用來回答兩個問題：哪些地方改了但還沒暫存？哪些已經暫存、準備要 commit？[S02]

- 不加任何參數的 `git diff`，比較的是工作目錄與暫存區，顯示你改了但還沒暫存的變更。[S02]
- `git diff --staged`，比較的是暫存區與上一次 commit，顯示已暫存、會進入下一次 commit 的變更；`--staged` 與 `--cached` 是同義詞。[S02]

要特別注意：單獨執行 `git diff`，不會顯示上次 commit 以來的所有變更，只會顯示還沒暫存的變更；如果所有變更都已經暫存，`git diff` 就不會有任何輸出。[S02]

如果比較喜歡用圖形化或外部的比較程式，可以改用 `git difftool`；執行 `git difftool --tool-help` 可以看到系統上有哪些可用的工具。[S02]

## 指令範例

查看改了但還沒暫存的變更：[S02]

```console
$ git diff
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
index 8ebb991..643e24f 100644
--- a/CONTRIBUTING.md
+++ b/CONTRIBUTING.md
@@ -65,7 +65,8 @@ branch directly, things can get messy.
 Please include a nice description of your changes when you submit your PR;
 if we have to read the whole diff to figure out why you're contributing
 in the first place, you're less likely to get feedback and have your change
-merged in.
+merged in. Also, split your changes into comprehensive chunks if your patch is
+longer than a dozen lines.

 If you are starting to work on a particular area, feel free to submit a PR
 that highlights your work in progress (and note in the PR title that it's
```

查看已暫存、會進入下一次 commit 的變更：[S02]

```console
$ git diff --staged
diff --git a/README b/README
new file mode 100644
index 0000000..03902a1
--- /dev/null
+++ b/README
@@ -0,0 +1 @@
+My Project
```

## 新手常見誤解

- **以為 `git diff` 沒有輸出，就代表沒有任何變更**：`git diff` 只顯示還沒暫存的變更；如果變更都已經暫存，它就沒有輸出，這時要用 `git diff --staged` 查看。[S02]

## 時效註記

無

## 相關頁面

- [git status（查看檔案狀態）](git-status.md)：只列出檔名，想看細節時改用 `git diff`
- [三種狀態與三個區域](three-states.md)：`git diff` 比較的就是工作目錄、暫存區與上一次 commit

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
