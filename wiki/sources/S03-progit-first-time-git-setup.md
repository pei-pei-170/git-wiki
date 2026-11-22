# S03｜Pro Git 1.6 Getting Started - First-Time Git Setup

- 來源：[1.6 Getting Started - First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)（《Pro Git》第 2 版，Scott Chacon、Ben Straub 著，CC BY-NC-SA 3.0）
- 年份：2014（第 2 版印刷版年份；線上版已修訂，包含 Git 2.28 之後才有的預設分支設定；本次取得日期為 2026-11-22）
- 時效風險：中（設定指令本身穩定，但部分路徑與編輯器的說明有時效性）

## 重點

1. `git config` 用來讀取與設定 Git 的設定變數，設定存在三個層級：`--system`（整台電腦）、`--global`（你個人的所有 repository）、`--local`（單一 repository，預設值），後面的層級會覆蓋前面的。[S03]
2. 安裝 Git 後的第一件事是設定 `user.name` 與 `user.email`；每個 commit 都會使用這些資訊，而且會永久寫進之後建立的 commit。[S03]
3. `core.editor` 可以設定 Git 需要你輸入訊息時使用的編輯器，沒設定就用系統預設的編輯器；沒設定好時，Git 開啟編輯器可能會陷入非常混亂的狀態。[S03]
4. 用 `git init` 建立新 repository 時，Git 預設會建立名為 master 的分支；從 Git 2.28 起，可以用 `init.defaultBranch` 設定成其他名稱，例如 main。[S03]
5. `git config --list` 列出所有設定，`git config <key>` 查看單一設定；同一個設定出現多次時，Git 以最後讀到的值為準。[S03]

## 影響的 wiki 頁面

- 新增 [git config（Git 設定）](../concepts/git-config.md)
- 新增 [預設分支名稱（master 與 main）](../concepts/default-branch.md)：整合 S02 與 S03 的說法，並記錄簡報範例輸出的改編決定
- 更新 [Commit（提交）](../concepts/commit.md)：commit 會記錄 user.name 與 user.email；編輯器的預設行為與 Warning
- 更新 [git status（查看檔案狀態）](../concepts/git-status.md)、[git add（加入暫存區）](../concepts/git-add.md)、[三種狀態與三個區域](../concepts/three-states.md)：時效註記改連到預設分支名稱頁

## 與其他資料的衝突或過時之處

- 與 S02 沒有衝突，而是互相補充：S02 的 Note 說 Git 本身仍以 master 為預設 [S02, 2020]，S03 進一步說明 `git init` 預設建立 master、Git 2.28 起可以修改 [S03]。
- 線上版加入 Git 2.28 的內容，但文中沒有寫年份，所以 S03 的引用不標年份；過時與現行的年份沿用 S02 的標註（S03 討論的決定）。
- 有時效性、但不放進簡報的內容：Windows XP 的設定檔路徑，以及「撰寫當時 Notepad++ 的 64 位元版不支援所有外掛」。[S03]
