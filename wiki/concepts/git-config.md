# git config（Git 設定）

> `git config` 是 Git 內建的工具，用來讀取與設定「控制 Git 外觀與運作各方面」的設定變數。[S03]

## 白話解釋

裝好 Git 之後，要先做幾件事來自訂 Git 的環境；這些事在每台電腦上通常只要做一次，升級 Git 後設定也會保留，之後也可以隨時重新執行指令來修改。[S03]

### 設定存在三個地方

| 層級 | 設定檔位置 | 選項 | 影響範圍 |
|---|---|---|---|
| 系統 | `[path]/etc/gitconfig` | `--system` | 這台電腦的每個使用者與他們所有的 repository；修改需要管理員權限。[S03] |
| 個人 | `~/.gitconfig` 或 `~/.config/git/config` | `--global` | 你這個使用者在這台電腦上所有的 repository。[S03] |
| 單一 repository | 該 repository 的 `.git/config` | `--local`（預設） | 只有這個 repository；必須在 repository 裡執行。[S03] |

每個層級都會覆蓋前一個層級的值，所以 `.git/config` 中的值，優先於 `[path]/etc/gitconfig` 中的值。[S03] 在 Windows 上，Git 會在 `$HOME` 資料夾（大多數人是 `C:\Users\$USER`）尋找 `.gitconfig`。[S03]

### 身分：名稱與 email

安裝 Git 後的第一件事，是設定你的使用者名稱與 email；這很重要，因為每個 Git commit 都會使用這些資訊，而且它們會永久寫進你之後建立的 commit 裡。[S03] 加上 `--global` 只需要設定一次，之後 Git 在這台電腦上都會使用這些資訊；如果某個專案想用不同的名稱或 email，就在該專案中執行同樣的指令，但不加 `--global`。[S03] 許多圖形介面工具在第一次執行時，也會協助你完成這個設定。[S03]

### 編輯器

Git 需要你輸入訊息時，會開啟預設的文字編輯器；如果沒有設定，Git 會使用系統預設的編輯器。[S03] 可以用 `core.editor` 改成其他編輯器；在 Windows 上，必須寫出編輯器執行檔的完整路徑。[S03] 原文提醒：如果沒有這樣設定好編輯器，Git 嘗試開啟它時，你可能會陷入非常混亂的狀態，例如在 Windows 上，Git 的操作在編輯途中提早中止。[S03]

### 預設分支名稱

用 `git init` 建立新 repository 時，Git 預設會建立名為 master 的分支；從 Git 2.28 起，可以用 `init.defaultBranch` 設定成其他名稱。[S03] 詳見 [預設分支名稱（master 與 main）](default-branch.md)。[S03]

### 檢查設定

`git config --list` 會列出 Git 目前找得到的所有設定。[S03] 你可能會看到同一個設定出現不只一次，因為 Git 從不同的檔案讀到了同一個設定；這時 Git 會使用每個設定最後讀到的值。[S03] 想查看某個設定的值，可以輸入 `git config <key>`；想知道某個值來自哪個設定檔，可以加上 `--show-origin`。[S03]

## 指令範例

設定名稱與 email（只需要做一次）：[S03]

```console
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

把預設分支名稱設成 main（Git 2.28 起）：[S03]

```console
$ git config --global init.defaultBranch main
```

列出所有設定：[S03]

```console
$ git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
...
```

查看單一設定：[S03]

```console
$ git config user.name
John Doe
```

把編輯器設成 Emacs：[S03]

```console
$ git config --global core.editor emacs
```

## 新手常見誤解

- **以為名稱和 email 之後再設定也沒關係**：每個 commit 都會使用這些資訊，而且會永久寫進之後建立的 commit，所以要在第一次 commit 前設定好。[S03]
- **以為每個 repository 都要重新設定一次**：加上 `--global` 只要設定一次，Git 在這台電腦上都會使用這些資訊。[S03]
- **看到 `git config --list` 中同一個設定出現兩次，以為設定壞了**：這是因為 Git 從不同的設定檔讀到同一個設定，會以最後讀到的值為準。[S03]

## 時效註記

- `init.defaultBranch` 要 Git 2.28 以上的版本才能使用。[S03]
- 原文中 Windows XP 的設定檔路徑，以及「撰寫當時 Notepad++ 的 64 位元版不支援所有外掛」的說法，都有時效性。[S03]

## 相關頁面

- [Commit（提交）](commit.md)：commit 會記錄這裡設定的名稱與 email
- [預設分支名稱（master 與 main）](default-branch.md)：`init.defaultBranch` 的詳細說明與簡報的處理方式

## 來源

- [S03｜Pro Git 1.6 Getting Started - First-Time Git Setup](../sources/S03-progit-first-time-git-setup.md)
