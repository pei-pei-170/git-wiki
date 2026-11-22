# S02｜Pro Git 2.2 Git Basics - Recording Changes to the Repository

- 來源：[2.2 Git Basics - Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)（《Pro Git》第 2 版，Scott Chacon、Ben Straub 著，CC BY-NC-SA 3.0）
- 年份：2014（第 2 版印刷版年份，線上版已修訂，包含 2020 年中之後才寫的 Note，本次取得日期為 2026-11-22）
- 時效風險：高（範例輸出使用 master 分支，且新舊兩種提示混用）

## 重點

1. 工作目錄中的檔案分為已追蹤與未追蹤，已追蹤的檔案可能是未修改、已修改或已暫存，並在「編輯 → 暫存 → commit」之間循環。[S02]
2. `git status` 是查看檔案處於哪種狀態的主要工具，`git status -s` 會用兩欄的精簡格式顯示。[S02]
3. `git add` 是多用途指令，可以開始追蹤新檔案或暫存修改。暫存的是執行 `git add` 當下的版本，之後再修改就要再 add 一次。[S02]
4. `git commit` 只記錄暫存區中的快照。用 `-m` 可以直接寫 commit 訊息，`-a` 會自動暫存所有已追蹤的檔案，但有時會包進不想要的變更。[S02]
5. `.gitignore` 列出要忽略的檔名規則，通常用於自動產生的檔案，例如記錄檔或建置系統產生的檔案，建議開始專案前就設定好。[S02]
6. `git diff` 顯示還沒暫存的變更，`git diff --staged` 顯示已暫存的變更。另外還介紹了刪除檔案的 `git rm` 與改名的 `git mv`（見下方補充）。[S02]

## 影響的 wiki 頁面

- 新增 [Commit（提交）](../concepts/commit.md)
- 新增 [git add（加入暫存區）](../concepts/git-add.md)
- 新增 [git status（查看檔案狀態）](../concepts/git-status.md)
- 新增 [.gitignore（忽略檔案）](../concepts/gitignore.md)
- 新增 [git diff（查看變更內容）](../concepts/git-diff.md)
- 更新 [三種狀態與三個區域](../concepts/three-states.md)：加入已追蹤與未追蹤、檔案狀態的循環，並補上指令範例

## 與其他資料的衝突或過時之處

- **預設分支名稱**：原文範例輸出中的分支名稱都是 `master` [S02, 2014]。原文的 Note 則說 GitHub 在 2020 年中把預設分支名稱改成 `main`，其他 Git 平台也跟進，但 Git 本身仍以 `master` 為預設 [S02, 2020]。標註方式見 [預設分支名稱（master 與 main）](../concepts/default-branch.md) 的「時效註記」。
- **新舊提示混用**：只有一個範例輸出的取消暫存提示是 `git restore --staged <file>`，其他範例都是 `git reset HEAD <file>`，放棄修改的提示則是 `git checkout -- <file>`。S02 沒有說明哪一種是現行寫法。[S02]
- **用語**：S01 用 working tree，S02 混用 working directory 與 working tree，wiki 一律寫「工作目錄」。[S01] [S02]

## 補充：git rm 與 git mv（不建概念頁、不放進簡報）

- 要從 Git 移除檔案，必須把它從已追蹤的檔案中移除（更精確地說，是從暫存區移除），然後 commit，`git rm` 會做這件事，同時也把檔案從工作目錄刪除。[S02]
- 如果只是直接刪掉工作目錄中的檔案，它會出現在 `git status` 輸出的「Changes not staged for commit」區，接著執行 `git rm`，才會暫存這個刪除動作，下次 commit 後檔案就不再被追蹤。[S02]
- 檔案修改過或已經加入暫存區時，必須加上 `-f` 強制移除。這是安全機制，避免誤刪還沒記錄在快照中、無法從 Git 救回的資料。[S02]
- `git rm --cached <檔案>` 會讓檔案留在硬碟上，但不再被 Git 追蹤，適合忘了寫進 `.gitignore` 而不小心暫存的檔案，例如大型記錄檔。[S02]
- `git rm` 可以接檔案、資料夾或萬用字元，例如 `git rm log/\*.log`。`*` 前面的反斜線是必要的，因為 Git 除了 shell 之外，也會自己展開檔名。[S02]
- 和許多其他版本控制系統不同，Git 不會明確追蹤檔案搬移，改名時不會存任何中繼資料，而是事後推斷出這是改名。[S02]
- `git mv file_from file_to` 等於依序執行 `mv`、`git rm`、`git add` 三個指令，只是比較方便。用任何工具改名都可以，只要在 commit 前處理好 add 與 rm。[S02]
