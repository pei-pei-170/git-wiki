# .gitignore（忽略檔案）

> `.gitignore` 是一個列出檔名規則的檔案，讓 Git 不要自動加入符合規則的檔案，也不要把它們顯示為未追蹤。[S02]

## 白話解釋

專案中常有一些檔案，你不希望 Git 自動加入，甚至不希望它們出現在未追蹤清單裡。這些通常是自動產生的檔案，例如記錄檔，或建置系統產生的檔案。[S02] 在開始工作之前，就幫新的 repository 設定好 `.gitignore`，通常是個好主意，這樣可以避免不小心 commit 真的不想放進 Git repository 的檔案。[S02]

GitHub 維護了一份相當完整的 `.gitignore` 範例清單，涵蓋數十種專案與程式語言，可以當作起點：<https://github.com/github/gitignore>。[S02]

### 規則

- 空行，或以 `#` 開頭的行，會被忽略。[S02]
- 可以使用標準的 glob 規則（shell 使用的簡化版正規表示式），而且會套用到整個工作目錄的所有子資料夾。[S02]
- 規則以斜線（`/`）開頭，可以避免套用到子資料夾。[S02]
- 規則以斜線（`/`）結尾，代表指定的是資料夾。[S02]
- 規則以驚嘆號（`!`）開頭，代表排除這條規則（也就是不要忽略）。[S02]

glob 規則中，`*` 代表零個或多個字元，`[abc]` 代表括號中的任一字元，`?` 代表單一字元，`[0-9]` 代表範圍內的任一字元，`**` 可以比對多層資料夾，例如 `a/**/z` 可以比對 `a/z`、`a/b/z`、`a/b/c/z`。[S02]

### 子資料夾中的 .gitignore

簡單的情況下，repository 根目錄只有一個 `.gitignore`，套用到整個 repository，但子資料夾中也可以有自己的 `.gitignore`，它的規則只套用到該資料夾底下的檔案。[S02]

## 指令範例

忽略以 `.o` 或 `.a` 結尾的檔案（編譯程式碼產生的目的檔與封存檔），以及以 `~` 結尾的檔案（許多文字編輯器用來標記暫存檔）：[S02]

```console
$ cat .gitignore
*.[oa]
*~
```

更多規則的範例：[S02]

```
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```

## 新手常見誤解

- **以為 `.gitignore` 的規則只作用在根目錄**：標準的 glob 規則會套用到整個工作目錄的所有子資料夾。只想作用在目前資料夾時，規則要以 `/` 開頭，例如 `/TODO` 只忽略目前資料夾的 TODO，不忽略 `subdir/TODO`。[S02]
- **不小心暫存了不該追蹤的檔案，以為只能把檔案刪掉**：忘了寫進 `.gitignore` 而不小心暫存的檔案，例如大型記錄檔，可以用 `git rm --cached <檔案>`，讓檔案留在硬碟上，但不再被 Git 追蹤。[S02]

## 時效註記

無

## 相關頁面

- [git add（加入暫存區）](git-add.md)：被忽略的檔案不會被自動加入
- [git status（查看檔案狀態）](git-status.md)：被忽略的檔案不會出現在未追蹤清單

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
