# git status（查看檔案狀態）

> `git status` 是用來判斷哪些檔案處於哪種狀態的主要工具。[S02]

## 白話解釋

`git status` 的輸出會把檔案分成幾區：[S02]

| 輸出中的區塊 | 意思 |
|---|---|
| `Untracked files` | 未追蹤的檔案：Git 發現上一個快照（commit）中沒有、也還沒暫存的檔案。[S02] |
| `Changes to be committed` | 已暫存的變更，會進入下一次 commit。[S02] |
| `Changes not staged for commit` | 已追蹤的檔案在工作目錄中被修改了，但還沒暫存。[S02] |
| `nothing to commit, working tree clean` | 工作目錄是乾淨的：已追蹤的檔案都沒有修改，也沒有未追蹤的檔案。[S02] |

輸出也會告訴你目前在哪個分支，以及這個分支和伺服器上的同一個分支有沒有分歧。[S02]

`git status` 只會列出檔名，如果想知道確切改了哪幾行，要用 `git diff`。[S02]

### 精簡格式

`git status` 的輸出很完整，但也相當冗長，執行 `git status -s` 或 `git status --short`，會得到精簡許多的輸出。[S02] 輸出有兩欄：左欄是暫存區的狀態，右欄是工作目錄的狀態。`??` 代表未追蹤的新檔案，`A` 代表新加入暫存區的檔案，`M` 代表修改過的檔案。[S02]

## 指令範例

剛用 [git clone](git-clone.md) 複製完 repository 時執行：[S02]

```console
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

新增一個 `README` 檔案後執行，`README` 會出現在「Untracked files」區：[S02]

```console
$ echo 'My Project' > README
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    README

nothing added to commit but untracked files present (use "git add" to track)
```

精簡格式：[S02]

```console
$ git status -s
 M README
MM Rakefile
A  lib/git.rb
M  lib/simplegit.rb
?? LICENSE.txt
```

上例中，`README` 在工作目錄中修改了但還沒暫存，`lib/simplegit.rb` 修改了而且已暫存，`Rakefile` 則是修改、暫存之後又再修改，所以同時有已暫存與未暫存的變更。[S02]

## 新手常見誤解

- **以為 `git status` 會顯示改了什麼內容**：它只列出檔名，要看確切新增、刪除了哪幾行，要用 `git diff`。[S02]
- **以為新增的檔案 Git 會自動記錄**：新檔案會列在「Untracked files」區，在執行 `git add` 之前都不會進入 commit。[S02]
- **看到同一個檔案同時出現在已暫存與未暫存兩區，以為出錯了**：這代表檔案在 `git add` 之後又被修改。暫存區保存的是 add 當下的版本。[S02]

## 時效註記

- 範例輸出中的分支名稱是 `master`，過時說法、現行做法與簡報的處理方式，見 [預設分支名稱（master 與 main）](default-branch.md)。[S02] [S03]

- 範例輸出中，取消暫存的提示有兩種寫法：一個範例是 `git restore --staged <file>`，其他範例是 `git reset HEAD <file>`。放棄修改的提示則是 `git checkout -- <file>`。S02 沒有說明哪一種是現行寫法，待 S05 確認。[S02]

## 相關頁面

- [三種狀態與三個區域](three-states.md)：`git status` 顯示的就是檔案目前的狀態
- [git add（加入暫存區）](git-add.md)：把未追蹤或已修改的檔案加入暫存區
- [git diff（查看變更內容）](git-diff.md)：想看確切改了哪幾行時使用
- [Commit（提交）](commit.md)：「Changes to be committed」區的內容會進入下一次 commit
- [預設分支名稱（master 與 main）](default-branch.md)：輸出第一行顯示的分支名稱
- [.gitignore（忽略檔案）](gitignore.md)：被忽略的檔案不會出現在未追蹤清單

## 來源

- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
