# 三種狀態與三個區域

> Git 中的檔案有三種主要狀態：已修改（modified）、已暫存（staged）、已提交（committed），並對應 Git 專案的三個區域：工作目錄、暫存區、Git 目錄。[S01]

## 白話解釋

《Pro Git》特別提醒：如果希望之後學 Git 順利，這是最需要記住的重點。[S01]

### 三種狀態

| 狀態 | 意思 |
|---|---|
| 已修改（modified） | 檔案已經改過，但還沒 commit 進資料庫。[S01] |
| 已暫存（staged） | 把某個已修改檔案的目前版本做了標記，要放進下一次 commit 的快照。[S01] |
| 已提交（committed） | 資料已經安全地存進本地資料庫。[S01] |

### 三個區域

- **工作目錄（working tree）**：專案某一個版本被取出來的樣子；這些檔案從 Git 目錄的壓縮資料庫中取出，放到磁碟上，讓你使用或修改。[S01]
- **暫存區（staging area）**：一個檔案，通常放在 Git 目錄裡，記錄下一次 commit 要包含哪些內容。[S01] 它在 Git 中的技術名稱是「index」，但稱為「staging area」也一樣通用。[S01]
- **Git 目錄（Git directory）**：Git 存放專案中繼資料（metadata，描述資料的資料）與物件資料庫的地方。[S01] 這是 Git 最重要的部分，從另一台電腦 clone（複製）儲存庫時，複製的就是它。[S01]

### 基本工作流程

1. 在工作目錄中修改檔案。[S01]
2. 選擇性地只把想放進下一次 commit 的變更加入暫存區；只有這些變更會被加入暫存區。[S01]
3. 執行 commit：Git 把暫存區中的檔案依當下的樣子做成快照，永久存進 Git 目錄。[S01]

### 怎麼判斷檔案現在是哪種狀態

- 檔案的某個版本已經在 Git 目錄中 → 已提交。[S01]
- 檔案修改過，而且已經加入暫存區 → 已暫存。[S01]
- 檔案取出之後有更動，但還沒加入暫存區 → 已修改。[S01]

《Pro Git》之後的〈Git Basics〉一章，會說明如何善用這些狀態，或完全跳過暫存這一步。[S01]

### 已追蹤與未追蹤

工作目錄中的每個檔案，先分成兩種：已追蹤（tracked）與未追蹤（untracked）。[S02] 已追蹤的檔案，是上一個快照中有的檔案，加上新暫存的檔案；它們可能是未修改、已修改或已暫存，簡單說就是 Git 知道的檔案。[S02] 其他的都是未追蹤的檔案：工作目錄中不在上一個快照、也不在暫存區的檔案。[S02]

剛 clone 一個 repository 時，所有檔案都是已追蹤且未修改，因為 Git 才剛把它們取出來，你還沒編輯任何東西。[S02] 編輯檔案後，Git 會把它們視為已修改；接著你選擇性地暫存這些已修改的檔案，再把暫存的變更全部 commit，然後不斷重複這個循環。[S02]

![The lifecycle of the status of your files](https://git-scm.com/book/en/v2/images/lifecycle.png)
*圖：檔案狀態的循環（出自《Pro Git》2.2 節）* [S02]

## 指令範例

每個步驟對應的指令如下，詳細說明見各指令的頁面：[S02]

- 查看檔案目前的狀態：`git status`。[S02]
- 暫存（未追蹤或已修改 → 已暫存）：`git add <檔案>`。[S02]
- 提交（已暫存 → 已提交）：`git commit -m "commit 訊息"`。[S02]

```console
$ git add README
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)

    new file:   README
```

## 新手常見誤解

- **把原文的 check out 當成 `git checkout` 指令**：S01 中的 check out 是一般動詞「取出」，指把檔案從 Git 目錄的壓縮資料庫取出、放到磁碟上成為工作目錄。[S01] 原文說「工作目錄是專案某一個版本的 checkout」、「檔案在 checked out 之後有更動」，以及集中式系統的用戶端從中央伺服器「check out」檔案，都是這個意思；這兩節沒有介紹任何指令。[S01]
- **以為改過的檔案都會自動進入下一次 commit**：commit 只會把暫存區中的內容做成快照；暫存是「選擇性」的，你可以只挑想要的變更放進暫存區。[S01] 還沒執行 `git add` 的變更，會以已修改的狀態留在磁碟上。[S02]
- **以為「已暫存」就代表已經存好了**：已暫存只是標記要放進下一次 commit；要等 commit 之後，資料才算安全地存進本地資料庫。[S01]
- **以為暫存區是一個資料夾**：暫存區其實是一個檔案，通常放在 Git 目錄裡。[S01]

## 時效註記

- 指令範例的輸出中，分支名稱是 `master`，過時說法與現行做法見 [git status（查看檔案狀態）](git-status.md) 的「時效註記」。[S02]

## 相關頁面

- [Git](git.md)：commit 時 Git 會把暫存區的內容做成快照，commit 後就很難遺失
- [版本控制（Version Control）](version-control.md)：為什麼需要記錄檔案的各個版本
- [git status（查看檔案狀態）](git-status.md)：查看檔案目前處於哪種狀態
- [git add（加入暫存區）](git-add.md)：已修改 → 已暫存
- [Commit（提交）](commit.md)：已暫存 → 已提交

## 來源

- [S01｜Pro Git 1.1 About Version Control；1.3 What is Git?](../sources/S01-progit-version-control-and-what-is-git.md)
- [S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository](../sources/S02-progit-recording-changes.md)
