# 簡報大綱：Git 與 GitHub 入門

**觀眾**：沒用過 Git 的大學生、研究生。

**教學目標**：看完能說明「為什麼需要版本控制」，並能完成 commit、push 到 GitHub 的基本流程。

**結構**：引起動機（第 1 張）→ 觀念（第 2～5 張）→ 實際操作（第 6～13 張）→ 常見錯誤（第 14～15 張）→ 總結（第 16 張）→ 小測驗（第 17 張），共 17 張。

**規劃依據**：只依 `wiki/` 的內容規劃，主要遵守 `wiki/overview.md` 的「簡報範圍決定」。

**共同規則**：

- 範例指令與輸出中的分支名稱一律用 main，範例下方註明「改編自 Pro Git，分支名稱依 S03 的設定改為 main」，依據 `concepts/default-branch.md`。
- commit 訊息一律用雙引號，push 一律用 `git push origin main`，不加 `-u`。
- 不使用「check out」這個字，避免新手和指令混淆。
- 「術語」欄列出該張第一次出現、需要先解釋的詞，解釋的內容都要能在依據的 wiki 頁面找到。wiki 沒有定義的術語（終端機、Git Bash、HTTPS、分支），只說明在哪裡使用，不下定義。
- 標註「教學例子」的內容是為了說明而舉的情境，不包含 wiki 沒有的事實（CLAUDE.md 第 6-2 節）。
- 投影片只能載入 Google Fonts，所以不使用 Pro Git 網站上的圖片，狀態循環等圖改用 HTML 與 CSS 畫。

**wiki 缺少的資料與處理方式**（大綱討論）：

- 術語定義：終端機、Git Bash、HTTPS、分支，wiki 都沒有定義，簡報只說明在哪裡使用，不下定義。
- 前提條件：安裝 Git、註冊 GitHub 帳號，wiki 沒有資料，列為第 4 張的「課前準備」，假設學生已經完成。
- 投影片底部要連到「GitHub 上對應的 wiki 頁面」：本專案的 repository 是 https://github.com/pei-pei-170/git-wiki ，wiki 頁面的連結格式為 `https://github.com/pei-pei-170/git-wiki/blob/main/wiki/<data-sources 中的路徑>`。

## 第 1 張｜你是不是也這樣管理檔案？
- 教學目標：意識到「複製資料夾再加上日期」管理版本的問題，引起學習動機
- 要點：
  - 情境（教學例子）：報告_v1、報告_v2_最終版、報告_v2_最終版_真的最終版
  - 很多人把檔案複製到另一個資料夾（聰明一點的會加上時間戳記）來管理版本，這種做法很簡單，但非常容易出錯：忘了自己在哪個資料夾、寫到錯的檔案、覆蓋掉不想覆蓋的檔案
  - 拋出問題：有沒有辦法隨時回到任何一個版本，又不會弄亂？
- 術語：無
- 依據：concepts/version-control.md、sources/S01-progit-version-control-and-what-is-git.md

## 第 2 張｜什麼是版本控制
- 教學目標：看完能說明版本控制是什麼，以及為什麼需要它
- 要點：
  - 定義：記錄一個或一組檔案隨時間的變化，之後可以叫回特定版本的系統
  - 不只程式碼，幾乎任何類型的檔案都能做版本控制
  - 好處：把檔案或整個專案回復到先前的狀態、比較變化、查出是誰改了什麼、弄壞或遺失時可以救回
  - 一句話對比：集中式的伺服器壞了大家都不能工作（單點故障），分散式的每一份 clone 都是完整備份
- 術語：版本控制系統（VCS）、clone（從別處複製一份完整的 repository，第 6 張再詳細說明）
- 依據：concepts/version-control.md、sources/S01-progit-version-control-and-what-is-git.md

## 第 3 張｜Git 是什麼
- 教學目標：看完能說出 Git 的三個特色
- 要點：
  - Git 是一種分散式版本控制系統
  - 存的是「快照」：每次 commit，Git 會把所有檔案當下的樣子拍成一張照片，沒有變更的檔案只存連結
  - 大部分操作都在本地進行，沒有網路也能 commit，有網路時再上傳
  - commit 之後的快照很難遺失
- 術語：commit（把專案目前的狀態存成一個快照）、快照
- 依據：concepts/git.md、sources/S01-progit-version-control-and-what-is-git.md

## 第 4 張｜開始之前：設定身分與預設分支
- 教學目標：能完成第一次使用 Git 前的設定
- 要點：
  - 課前準備：已安裝 Git、已註冊 GitHub 帳號
  - 在哪裡輸入指令：開啟終端機，Windows 請開啟 Git Bash 輸入指令（只說明在哪裡使用，不下定義）
  - `git config --global user.name "你的名字"` 與 `git config --global user.email 你的email`：每個 commit 都會永久記錄這兩項，所以第一次 commit 前就要設定好，加上 `--global` 只要設定一次
  - `git config --global init.defaultBranch main`：讓之後建立的 repository 預設分支叫 main，與 GitHub 新 repository 的預設一致（GitHub 自 2020 年中起，新 repository 的預設分支名稱是 main）
  - 設定預設分支需要 Git 2.28 以上 [S03]
  - 分支的說法：「main 是這個專案預設的分支名稱，本簡報不教分支，只要記得名稱要和 GitHub 一致即可」
  - 用 `git config --list` 或 `git config user.name` 確認設定
  - 不提「Git 本身預設是 master」，所以這張不需要 `data-legacy`
- 術語：終端機、Git Bash、分支（三者都只說明在哪裡使用，不下定義）
- 依據：concepts/git-config.md、concepts/default-branch.md、concepts/push-to-github.md、sources/S02-progit-recording-changes.md、sources/S03-progit-first-time-git-setup.md、sources/S07-github-adding-locally-hosted-code.md

## 第 5 張｜三個區域與三種狀態
- 教學目標：看完能說明檔案在 Git 中的三種狀態，以及它們對應的三個區域
- 要點：
  - 三個區域：工作目錄（你修改檔案的地方）、暫存區（記錄下一次 commit 要包含哪些內容）、Git 目錄（Git 存放專案資料的地方）
  - 三種狀態：已修改（改了還沒 commit）、已暫存（標記要放進下一次 commit）、已提交（已經安全存進本地資料庫）
  - 已追蹤與未追蹤：新檔案一開始是未追蹤的，Git 不會自動把它放進 commit
  - 循環圖：編輯 → 暫存 → commit，然後不斷重複
- 術語：工作目錄、暫存區（staging area）、Git 目錄、已追蹤、未追蹤
- 依據：concepts/three-states.md、sources/S01-progit-version-control-and-what-is-git.md、sources/S02-progit-recording-changes.md

## 第 6 張｜建立 repository：git init
- 教學目標：能在自己的專案資料夾建立 Git repository
- 要點：
  - repository：Git 用來記錄專案的地方，也就是專案資料夾裡的 `.git` 子資料夾
  - 取得 repository 有兩種方式：`git init` 把既有的資料夾變成 repository，`git clone <url>` 複製一個現有的 repository（會下載完整的歷史）。本課使用 `git init`
  - 先用 `cd` 進入專案資料夾，再執行 `git init`
  - 執行後只建立了 `.git`，這時還沒有任何檔案被追蹤，要 add 再 commit
- 術語：repository（儲存庫）、`.git` 資料夾
- 依據：concepts/repository.md、concepts/git-init.md、concepts/git-clone.md、sources/S04-progit-getting-a-git-repository.md

## 第 7 張｜查看狀態：git status
- 教學目標：能看懂 `git status` 的輸出，判斷每個檔案處於哪種狀態
- 要點：
  - `git status` 是判斷哪些檔案處於哪種狀態的主要工具，任何時候不確定就先執行它
  - 輸出的四種區塊：Untracked files（未追蹤）、Changes to be committed（已暫存，會進入下一次 commit）、Changes not staged for commit（已修改但還沒暫存）、nothing to commit, working tree clean（沒有任何變更）
  - 範例輸出採用 Git 2.23.0 起的新版輸出（提示是 `git restore`），分支名稱改成 main
  - `git status` 只列出檔名，不顯示改了哪幾行
- 術語：無（狀態名稱已在第 5 張說明）
- 依據：concepts/git-status.md、concepts/default-branch.md、sources/S02-progit-recording-changes.md、sources/S05-progit-undoing-things.md

## 第 8 張｜加入暫存區：git add
- 教學目標：能用 `git add` 追蹤新檔案、暫存修改過的檔案
- 要點：
  - `git add <檔案>`：開始追蹤新檔案，或暫存修改過的檔案
  - `git add .`：GitHub Docs 用這個指令加入新 repository 中的檔案並暫存，準備第一次 commit
  - 把 `git add` 想成「把這份內容加進下一次 commit」，不是「把檔案加進專案」
  - 暫存的是執行 `git add` 那一刻的內容，之後再改就要再 add 一次
- 術語：暫存（stage）
- 依據：concepts/git-add.md、sources/S02-progit-recording-changes.md、sources/S07-github-adding-locally-hosted-code.md

## 第 9 張｜提交：git commit -m
- 教學目標：能用 `git commit -m` 完成一次 commit，並看懂輸出
- 要點：
  - `git commit -m "First commit"`：在 `-m` 後面直接寫 commit 訊息
  - 不加 `-m` 時會開啟系統預設的編輯器，所以本課一律用 `-m`
  - commit 只記錄暫存區的快照，改過但沒有 add 的檔案不會進入這次 commit
  - commit 輸出：commit 到哪個分支（main）、這個 commit 的檢查碼、改了幾個檔案（範例輸出的分支名稱改成 main）
- 術語：commit 訊息
- 依據：concepts/commit.md、concepts/default-branch.md、sources/S02-progit-recording-changes.md、sources/S03-progit-first-time-git-setup.md、sources/S07-github-adding-locally-hosted-code.md

## 第 10 張｜.gitignore：不想被追蹤的檔案
- 教學目標：能說明 `.gitignore` 的用途，並寫出簡單的規則
- 要點：
  - `.gitignore` 列出檔名規則，讓 Git 不要自動加入符合規則的檔案，也不把它們列為未追蹤
  - 通常用於自動產生的檔案，例如記錄檔、建置系統產生的檔案
  - 開始專案前就設定好，避免不小心 commit 不想放進 repository 的檔案
  - 簡單範例：`*.[oa]`（忽略 .o 與 .a 檔）、`build/`（忽略 build 資料夾）
  - GitHub 提供各種專案與程式語言的 `.gitignore` 範本清單
- 術語：無
- 依據：concepts/gitignore.md、sources/S02-progit-recording-changes.md

## 第 11 張｜遠端 repository 與 origin
- 教學目標：能說明遠端 repository 是什麼，以及 origin 這個名稱的意思
- 要點：
  - 遠端 repository：放在網際網路或某個網路上的專案版本，例如 GitHub 上的那一份
  - commit 只記錄在本地，要 push 才會推送到遠端，分享給別人
  - origin：clone 時 Git 預設替來源取的遠端名稱。自己新增遠端時用 `git remote add origin <url>`，GitHub Docs 也用 origin 這個名稱
  - 用 `git remote -v` 確認遠端的網址
- 術語：遠端（remote）、origin、push
- 依據：concepts/remote.md、concepts/git-push.md、sources/S01-progit-version-control-and-what-is-git.md、sources/S06-progit-working-with-remotes.md、sources/S07-github-adding-locally-hosted-code.md

## 第 12 張｜身分驗證：personal access token
- 教學目標：能在 GitHub 建立 personal access token，並說明為什麼需要它
- 要點：
  - GitHub 從 2021 年 8 月 13 日起，不再接受用帳號密碼驗證 Git 操作，要改用以 token 為基礎的驗證方式
  - personal access token（PAT）可以代替密碼，要像對待密碼一樣保管
  - 建立 fine-grained token：Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token
  - 填名稱、設定有效期限，repository 只選需要的，權限只給最小的（push 需要把 Contents 設成 write）
  - PAT 只能用在 HTTPS 的 Git 操作，遠端網址是 SSH 時要改成 HTTPS
  - 這張同時出現「密碼」與「token」，依 check.py 的規則不會被當成過時用語
- 術語：personal access token（PAT）、HTTPS（只說明在哪裡使用，不下定義）
- 依據：concepts/personal-access-token.md、sources/S08-github-personal-access-tokens.md、sources/S09-github-changelog-password-auth-shutdown.md

## 第 13 張｜實際操作：把專案推上 GitHub
- 教學目標：能依步驟把本地專案推上 GitHub
- 要點：
  - 本地：`git init` → `git add .` → `git commit -m "First commit"`
  - GitHub：建立新的 repository，不要用 README、license 或 gitignore 初始化，再從 Quick Setup 頁面複製網址
  - 連到遠端：`git remote add origin <網址>` → `git remote -v` 確認
  - 推上去：`git push origin main`，出現 Username 輸入使用者名稱，出現 Password 貼上 personal access token
  - 這張是第 4～12 張的總整理，用一張流程圖串起來
- 術語：無（都已在前面說明）
- 依據：concepts/push-to-github.md、concepts/git-push.md、concepts/personal-access-token.md、sources/S07-github-adding-locally-hosted-code.md、sources/S08-github-personal-access-tokens.md

## 第 14 張｜常見錯誤（一）：add 與 commit
- 教學目標：能避免 add 與 commit 的常見錯誤，並在不小心 add 時取消暫存
- 要點：
  - add 之後又修改了檔案：同一個檔案會同時出現在已暫存與未暫存兩區，commit 進去的是上次 add 的版本，要再 add 一次
  - `git commit -a` 很方便，但可能把不想要的變更也包進 commit
  - 不小心 add 了不想 commit 的檔案：用 `git restore --staged <file>` 取消暫存，檔案的修改還在
  - 警告：`git restore <file>`（不加 `--staged`）會丟掉這個檔案的所有修改，除非非常確定，否則不要使用
- 術語：取消暫存
- 依據：concepts/git-add.md、concepts/commit.md、concepts/git-restore.md、sources/S02-progit-recording-changes.md、sources/S05-progit-undoing-things.md

## 第 15 張｜常見錯誤（二）：push 到 GitHub
- 教學目標：能判斷 push 失敗的常見原因
- 要點：
  - 輸入 GitHub 密碼結果失敗：從 2021 年 8 月起不接受密碼，在 Password 提示貼上 personal access token
  - push 被拒絕：沒有寫入權限，或別人先 push 了，需要先取得別人的更新才能再 push（本課不教合併）
  - 在 GitHub 建立 repository 時勾選了 README：為了避免錯誤，要推上本地專案時不要勾選，可以 push 之後再加
  - 不要把密碼、API key 之類的敏感資訊 add、commit 或 push 到遠端
  - 分支名稱不是 main：例如沒有做第 4 張的設定，Git 預設會用 master（依 Pro Git 線上版，2026-11-22 擷取），push 指令要把 main 換成自己的分支名稱 [S03] [S07]
  - 這張提到 Git 本身的預設分支名稱，要加上 `data-legacy`
- 術語：API key（wiki 只說它和密碼一樣屬於敏感資訊，沒有進一步的定義）
- 依據：concepts/git-push.md、concepts/personal-access-token.md、concepts/push-to-github.md、concepts/default-branch.md、sources/S03-progit-first-time-git-setup.md、sources/S06-progit-working-with-remotes.md、sources/S07-github-adding-locally-hosted-code.md、sources/S08-github-personal-access-tokens.md、sources/S09-github-changelog-password-auth-shutdown.md

## 第 16 張｜總結
- 教學目標：能用一句話說出版本控制的價值，並記得完整流程
- 要點：
  - 流程回顧：設定 → `git init` → `git add` → `git commit -m` → `git remote add origin` → `git push origin main`
  - commit 過的東西幾乎都能救回來，從來沒有 commit 過的東西一旦遺失，很可能就找不回來了，所以要常 commit
  - commit 只在本地，push 之後才會出現在 GitHub
- 術語：無
- 依據：concepts/git-restore.md、concepts/push-to-github.md、concepts/git-push.md、sources/S01-progit-version-control-and-what-is-git.md、sources/S05-progit-undoing-things.md、sources/S07-github-adding-locally-hosted-code.md

## 第 17 張｜小測驗
- 教學目標：確認學生能回答本課的關鍵問題
- 要點：五題，每題都附答案，答案預設隱藏，點一下才顯示
  - 第一次 commit 之前，一定要用 `git config` 設定哪兩項？（答：user.name 與 user.email）
  - `git add` 之後又修改了檔案，直接 commit，進去的是哪個版本？（答：上次 add 時的版本）
  - 不小心 add 了不想 commit 的檔案，用哪個指令取消暫存？（答：`git restore --staged <file>`）
  - push 到 GitHub 出現 Password 提示時，要輸入什麼？（答：personal access token）
  - 在 GitHub 建立要推上本地專案的 repository 時，要不要勾選 README？（答：不要）
- 術語：無
- 依據：concepts/git-config.md、concepts/git-add.md、concepts/git-restore.md、concepts/personal-access-token.md、concepts/push-to-github.md、sources/S02-progit-recording-changes.md、sources/S03-progit-first-time-git-setup.md、sources/S05-progit-undoing-things.md、sources/S07-github-adding-locally-hosted-code.md、sources/S08-github-personal-access-tokens.md
