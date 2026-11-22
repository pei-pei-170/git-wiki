# S04｜Pro Git 2.1 Git Basics - Getting a Git Repository

- 來源：[2.1 Git Basics - Getting a Git Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)（《Pro Git》第 2 版，Scott Chacon、Ben Straub 著，CC BY-NC-SA 3.0）
- 年份：2014（第 2 版印刷版年份，本次取得日期為 2026-11-22）
- 時效風險：低（`git init`、`git clone` 的用法穩定，只有傳輸協定的說明可能有時效性）

## 重點

1. 取得 Git repository 通常有兩種方式：把還沒納入版本控制的本地資料夾變成 Git repository，或是從別處 clone 一個現有的 repository。兩種方式最後都會在你的電腦上得到一個可以開始工作的 repository。[S04]
2. 在專案資料夾執行 `git init`，會建立一個名為 `.git` 的子資料夾，裡面是 repository 需要的所有檔案。這時專案中還沒有任何檔案被追蹤。[S04]
3. 要開始管理既有的檔案，先用 `git add` 指定要追蹤的檔案，再用 `git commit` 完成第一次 commit。[S04]
4. `git clone <url>` 會取得伺服器上幾乎所有資料的完整副本，專案歷史中每個檔案的每個版本預設都會被下載，所以這個指令叫 clone 而不是 checkout。[S04]
5. `git clone` 會建立一個資料夾、在裡面初始化 `.git`、下載所有資料，並取出最新版本的工作副本。也可以另外指定資料夾名稱。[S04]

## 影響的 wiki 頁面

- 新增 [Repository（儲存庫）](../concepts/repository.md)
- 新增 [git init（建立 repository）](../concepts/git-init.md)
- 新增 [git clone（複製 repository）](../concepts/git-clone.md)
- 更新 [三種狀態與三個區域](../concepts/three-states.md)：Git 目錄就是 `git init` 建立的 `.git` 子資料夾，並補上 check out 是一般動詞的例子
- 更新 [版本控制（Version Control）](../concepts/version-control.md)：每份 clone 都是完整備份
- 更新 [Commit（提交）](../concepts/commit.md)：第一次 commit 的例子
- 更新 [git status（查看檔案狀態）](../concepts/git-status.md)：「剛 clone 完」的例子連到 git clone

## 與其他資料的衝突或過時之處

- 與既有 wiki 沒有衝突。S04 說每份 clone 幾乎都能用來復原伺服器 [S04]，與 S01「每一份 clone 都是完整備份」的說法一致 [S01]。
- 原文說 clone 會 checks out 一份工作副本，這裡的 check out 又是一般動詞「取出」，不是指令。[S04]
- 第一次 commit 的例子用單引號 `'Initial project version'` [S04]，S02 的例子用雙引號 [S02]。簡報一律用雙引號，理由是與 S02 的範例一致。（S04 討論）
