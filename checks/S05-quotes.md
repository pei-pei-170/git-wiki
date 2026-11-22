# S05 逐句核對

- 對象：S05（Pro Git 2.4 Undoing Things）ingest 時新增或修改的事實陳述，另順帶核對上一輪 S03 摘要頁的 2 句
- 核對日期：2026-11-22
- 結果：核對 54 句（本輪 52 句，上一輪 S03 的 2 句），找不到原句而刪改 4 句。改寫後的 2 句另列一筆，並通過驗證
- 驗證方式：`python tools/verify_quotes.py checks/S05-quotes.md`

## 1｜sources/S05 重點1
- 句子：復原要小心，有些復原操作本身無法再復原，這是 Git 中少數做錯就可能失去部分工作成果的地方。
- 來源：S05
- 原句：
  - Be careful, because you can’t always undo some of these undos.
  - This is one of the few areas in Git where you may lose some work if you do it wrong.

## 2｜sources/S05 重點2
- 句子：git commit --amend 可以重做上一個 commit，例如補上忘了暫存的檔案或修改 commit 訊息。
- 來源：S05
- 原句：
  - One of the common undos takes place when you commit too early and possibly forget to add some files, or you mess up your commit message.
  - If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the `--amend` option:

## 3｜sources/S05 重點2
- 句子：它會用新的 commit 完全取代舊的，所以只能用在還沒 push 的 commit。
- 來源：S05
- 處理：改寫，原文沒有寫「所以」的因果關係，改寫成兩個獨立的句子，改寫後見下一筆
- 原句：（找不到）

## 4｜sources/S05 重點2（改寫後）
- 句子：它會用新的 commit 完全取代舊的。只能用在還沒 push 的 commit。
- 來源：S05
- 原句：
  - *replacing* it entirely with a new, improved commit
  - Only amend commits that are still local and have not been pushed somewhere.

## 5｜sources/S05 重點3
- 句子：舊做法是用 git reset HEAD <file> 取消暫存，用 git checkout -- <file> 放棄修改，後者是危險的指令。
- 來源：S05
- 原句：
  - it says use `git reset HEAD <file>
  - (use "git checkout -- <file>..." to discard changes in working directory)
  - It’s important to understand that `git checkout -- <file>` is a dangerous command.

## 6｜sources/S05 重點4
- 句子：Git 2.23.0 新增了 git restore，基本上是 git reset 的替代方案。
- 來源：S05
- 原句：
  - Git version 2.23.0 introduced a new command: `git restore`.
  - It’s basically an alternative to `git reset` which we just covered.

## 7｜sources/S05 重點4
- 句子：取消暫存用 git restore --staged <file>，放棄修改用 git restore <file>，後者一樣是危險的指令。
- 來源：S05
- 原句：
  - it says use `git restore --staged <file>
  - (use "git restore <file>..." to discard changes in working directory)
  - It’s important to understand that `git restore <file>` is a dangerous command.

## 8｜sources/S05 重點5
- 句子：git status 的輸出會提示如何復原暫存區與工作目錄的變更。
- 來源：S05
- 原句：
  - The nice part is that the command you use to determine the state of those two areas also reminds you how to undo changes to them.

## 9｜sources/S05 重點6
- 句子：commit 過的東西幾乎都能救回來，包括被 --amend 覆蓋的 commit。
- 來源：S05
- 原句：
  - Remember, anything that is *committed* in Git can almost always be recovered.
  - commits that were overwritten with an `--amend` commit can be recovered

## 10｜sources/S05 重點6
- 句子：從來沒有 commit 過的東西一旦遺失，很可能再也找不回來。
- 來源：S05
- 原句：
  - However, anything you lose that was never committed is likely never to be seen again.

## 11｜sources/S05 年份
- 句子：線上版已修訂，包含 Git 2.23.0 新增的 git restore。
- 來源：S05
- 處理：刪除，原文沒有說 Git 2.23.0 晚於印刷版，「線上版已修訂」是推論
- 原句：（找不到）

## 12｜sources/S05 時效風險
- 句子：同一頁並列 Git 2.23.0 前後兩種復原指令。
- 來源：S05
- 原句：
  - Let’s retrace our steps, and undo things with `git restore` instead of `git reset`.

## 13｜sources/S05 衝突1
- 句子：S02 範例輸出中的 git reset HEAD、git checkout -- 提示，與 S05 前半段的輸出相同。
- 來源：S02、S05
- 原句：
  - (use "git reset HEAD <file>..." to unstage)
  - (use "git checkout -- <file>..." to discard changes in working directory)

## 14｜sources/S05 衝突1
- 句子：S05 說從 Git 2.23.0 起，很多復原操作改用 git restore。
- 來源：S05
- 原句：
  - From Git version 2.23.0 onwards, Git will use `git restore` instead of `git reset` for many undo operations.

## 15｜sources/S05 衝突3
- 句子：S05 的範例輸出中分支名稱是 master。
- 來源：S05
- 原句：
  - On branch master

## 16｜git-restore 定義
- 句子：git restore 是 Git 2.23.0 新增的指令，基本上是 git reset 的替代方案。
- 來源：S05
- 原句：
  - Git version 2.23.0 introduced a new command: `git restore`.
  - It’s basically an alternative to `git reset` which we just covered.

## 17｜git-restore 定義
- 句子：從 Git 2.23.0 起，很多復原操作 Git 都改用 git restore。
- 來源：S05
- 原句：
  - From Git version 2.23.0 onwards, Git will use `git restore` instead of `git reset` for many undo operations.

## 18｜git-restore 白話
- 句子：復原要小心，因為有些復原操作本身不一定能再復原。
- 來源：S05
- 原句：
  - Be careful, because you can’t always undo some of these undos.

## 19｜git-restore 白話
- 句子：這是 Git 中少數做錯就可能失去部分工作成果的地方。
- 來源：S05
- 原句：
  - This is one of the few areas in Git where you may lose some work if you do it wrong.

## 20｜git-restore 白話
- 句子：用來判斷暫存區與工作目錄狀態的 git status，也會提示你怎麼復原這兩個區域的變更。
- 來源：S05
- 原句：
  - The nice part is that the command you use to determine the state of those two areas also reminds you how to undo changes to them.

## 21｜git-restore 取消暫存
- 句子：例如你改了兩個檔案，想分成兩次 commit，卻不小心輸入 git add *，把兩個檔案都暫存了。
- 來源：S05
- 原句：
  - For example, let’s say you’ve changed two files and want to commit them as two separate changes, but you accidentally type `git add *` and stage them both.

## 22｜git-restore 取消暫存
- 句子：這時 git status 會在「Changes to be committed」下方提示，用 git restore --staged <file> 取消暫存。
- 來源：S05
- 原句：
  - Right below the “Changes to be committed” text, it says use `git restore --staged <file>

## 23｜git-restore 取消暫存
- 句子：執行後，這個檔案仍然是已修改，但回到了未暫存的狀態。
- 來源：S05
- 原句：
  - The `CONTRIBUTING.md` file is modified but once again unstaged.

## 24｜git-restore 放棄修改
- 句子：想把它恢復成上次 commit 時（或剛 clone 時）的樣子，git status 也會在「Changes not staged for commit」區提示，用 git restore <file> 放棄修改。
- 來源：S05
- 原句：
  - revert it back to what it looked like when you last committed (or initially cloned, or however you got it into your working directory)?
  - Luckily, `git status` tells you how to do that, too.
  - (use "git restore <file>..." to discard changes in working directory)

## 25｜git-restore 危險
- 句子：git restore <file> 是危險的指令。你對那個檔案做的所有本地修改都會消失，Git 會直接用最後一次暫存或 commit 的版本取代它。
- 來源：S05
- 原句：
  - It’s important to understand that `git restore <file>` is a dangerous command.
  - Any local changes you made to that file are gone — Git just replaced that file with the last staged or committed version.

## 26｜git-restore 危險
- 句子：除非你非常確定不要那些還沒儲存的本地修改，否則絕對不要使用這個指令。
- 來源：S05
- 原句：
  - Don’t ever use this command unless you absolutely know that you don’t want those unsaved local changes.

## 27｜git-restore 救回
- 句子：commit 過的東西幾乎都能救回來，連被 --amend 覆蓋的 commit 也可以。
- 來源：S05
- 原句：
  - Remember, anything that is *committed* in Git can almost always be recovered.
  - commits that were overwritten with an `--amend` commit can be recovered

## 28｜git-restore 救回
- 句子：從來沒有 commit 過的東西一旦遺失，很可能就再也找不回來了。
- 來源：S05
- 原句：
  - However, anything you lose that was never committed is likely never to be seen again.

## 29｜git-restore 誤解1
- 句子：git restore --staged <file> 只是把檔案移出暫存區，檔案仍然是已修改的狀態。
- 來源：S05
- 原句：
  - The `CONTRIBUTING.md` file is modified but once again unstaged.

## 30｜git-restore 誤解2
- 句子：不加 --staged 時，對那個檔案的所有本地修改都會消失。
- 來源：S05
- 原句：
  - Any local changes you made to that file are gone — Git just replaced that file with the last staged or committed version.

## 31｜git-restore 誤解3
- 句子：commit 過的東西幾乎都能救回，但從來沒有 commit 過的東西一旦遺失，很可能再也找不回來。
- 來源：S05
- 原句：
  - can almost always be recovered.
  - is likely never to be seen again.

## 32｜git-restore 過時
- 句子：取消暫存用 git reset HEAD <file>，放棄修改用 git checkout -- <file>。
- 來源：S05
- 原句：
  - $ git reset HEAD CONTRIBUTING.md
  - $ git checkout -- CONTRIBUTING.md

## 33｜git-restore 現行
- 句子：取消暫存用 git restore --staged <file>，放棄修改用 git restore <file>。
- 來源：S05
- 原句：
  - $ git restore --staged CONTRIBUTING.md
  - $ git restore CONTRIBUTING.md

## 34｜git-restore 時效
- 句子：git reset HEAD <file> 不會動到工作目錄的檔案，所以相對安全，但 git reset 加上 --hard 時是危險的指令。
- 來源：S05
- 原句：
  - It’s true that `git reset` can be a dangerous command, especially if you provide the `--hard` flag.
  - However, in the scenario described above, the file in your working directory is not touched, so it’s relatively safe.

## 35｜commit amend
- 句子：常見的復原情況之一，是太早 commit，可能忘了加某些檔案，或把 commit 訊息寫錯。
- 來源：S05
- 原句：
  - One of the common undos takes place when you commit too early and possibly forget to add some files, or you mess up your commit message.

## 36｜commit amend
- 句子：想重做這個 commit，就先補上忘記的修改並暫存，再用 --amend 重新 commit。
- 來源：S05
- 原句：
  - If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the `--amend` option:

## 37｜commit amend
- 句子：這個指令會用暫存區的內容來 commit。
- 來源：S05
- 原句：
  - This command takes your staging area and uses it for the commit.

## 38｜commit amend
- 句子：如果上次 commit 之後沒有任何變更，快照會完全一樣，改變的只有 commit 訊息。
- 來源：S05
- 原句：
  - then your snapshot will look exactly the same, and all you’ll change is your commit message.

## 39｜commit amend
- 句子：它會開啟同一個 commit 訊息編輯器，裡面已經有上一個 commit 的訊息。
- 來源：S05
- 原句：
  - The same commit-message editor fires up, but it already contains the message of your previous commit.

## 40｜commit amend
- 句子：最後只會有一個 commit，第二次 commit 會取代第一次的結果。
- 來源：S05
- 原句：
  - You end up with a single commit — the second commit replaces the results of the first.

## 41｜commit amend
- 句子：amend 不是修正上一個 commit，而是用一個新的 commit 把它完全取代，就像上一個 commit 從來沒發生過，也不會出現在 repository 的歷史中。
- 來源：S05
- 原句：
  - you’re not so much fixing it as *replacing* it entirely with a new, improved commit
  - Effectively, it’s as if the previous commit never happened, and it won’t show up in your repository history.

## 42｜commit amend
- 句子：好處是可以小幅改進最後一個 commit，不必在歷史中留下「Oops, forgot to add a file」這類的 commit 訊息。
- 來源：S05
- 原句：
  - The obvious value to amending commits is to make minor improvements to your last commit, without cluttering your repository history with commit messages of the form, “Oops, forgot to add a file”

## 43｜commit amend
- 句子：只能 amend 還在本地、還沒 push 到任何地方的 commit。已經 push 過的 commit 再 amend 並強制推送，會造成協作者的問題。
- 來源：S05
- 原句：
  - Only amend commits that are still local and have not been pushed somewhere.
  - Amending previously pushed commits and force pushing the branch will cause problems for your collaborators.

## 44｜commit 範例說明
- 句子：commit 之後才發現忘了暫存某個檔案，補上後用 --amend 重新 commit。
- 來源：S05
- 原句：
  - As an example, if you commit and then realize you forgot to stage the changes in a file you wanted to add to this commit, you can do something like this:

## 45｜commit 誤解
- 句子：它是用新的 commit 把上一個 commit 完全取代，舊的 commit 不會出現在 repository 的歷史中。
- 來源：S05
- 原句：
  - *replacing* it entirely
  - it won’t show up in your repository history.

## 46｜commit 誤解
- 句子：只能 amend 還沒 push 的 commit，已經 push 過再 amend 並強制推送，會造成協作者的問題。
- 來源：S05
- 原句：
  - Only amend commits that are still local and have not been pushed somewhere.
  - will cause problems for your collaborators.

## 47｜git-status 範例說明
- 句子：從 Git 2.23.0 起，輸出中的復原提示改用 git restore，例如不小心用 git add * 暫存了兩個檔案時。
- 來源：S05
- 原句：
  - From Git version 2.23.0 onwards, Git will use `git restore` instead of `git reset` for many undo operations.
  - (use "git restore --staged <file>..." to unstage)

## 48｜git-status 時效
- 句子：S02 範例輸出中，取消暫存的提示大多是 git reset HEAD <file>，放棄修改的提示是 git checkout -- <file>。
- 來源：S02
- 原句：
  - (use "git reset HEAD <file>..." to unstage)
  - (use "git checkout -- <file>..." to discard changes in working directory)

## 49｜git-add 時效
- 句子：範例輸出中，取消暫存的提示有 git restore --staged <file> 與 git reset HEAD <file> 兩種。
- 來源：S02
- 原句：
  - (use "git restore --staged <file>..." to unstage)
  - (use "git reset HEAD <file>..." to unstage)

## 50｜git.md 誤解
- 句子：commit 過的東西幾乎都能救回來，連被 --amend 覆蓋的 commit 也可以，但從來沒有 commit 過的東西一旦遺失，很可能再也找不回來。
- 來源：S05
- 原句：
  - can almost always be recovered.
  - commits that were overwritten with an `--amend` commit can be recovered
  - is likely never to be seen again.

## 51｜overview 第 9 項
- 句子：忘了加檔案或訊息寫錯時，可以用 --amend 重做還沒 push 的上一個 commit。
- 來源：S05
- 原句：
  - possibly forget to add some files, or you mess up your commit message.
  - Only amend commits that are still local and have not been pushed somewhere.

## 52｜overview 第 10 項
- 句子：不小心暫存時用 git restore --staged 取消暫存，git restore <file> 會丟掉修改，是危險的指令。
- 來源：S05
- 原句：
  - it says use `git restore --staged <file>
  - `git restore <file>` is a dangerous command.

## 53｜overview 第 10 項
- 句子：commit 過的幾乎都救得回來，沒 commit 過的可能永遠消失。
- 來源：S05
- 原句：
  - can almost always be recovered.
  - is likely never to be seen again.

## 54｜sources/S03 年份（上一輪）
- 句子：線上版已修訂，包含 Git 2.28 之後才有的預設分支設定。
- 來源：S03
- 處理：刪除，原文沒有說 Git 2.28 晚於印刷版，「線上版已修訂」是推論（上一輪寫入，核對時順帶發現）
- 原句：（找不到）

## 55｜sources/S03 衝突2（上一輪）
- 句子：線上版加入 Git 2.28 的內容，但文中沒有寫年份。
- 來源：S03
- 處理：改寫，「加入」暗示是後來才加的，改寫後見下一筆（上一輪寫入，核對時順帶發現）
- 原句：（找不到）

## 56｜sources/S03 衝突2（改寫後）
- 句子：原文提到 Git 2.28，但沒有寫年份。
- 來源：S03
- 原句：
  - From Git version 2.28 onwards, you can set a different name for the initial branch.
