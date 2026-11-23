# Git 與 GitHub 入門：LLM Wiki 與教學簡報

這個專案依照 Karpathy 的 LLM Wiki 模式，先把 Git 與 GitHub 的原始資料整理成互相連結的 wiki，再以這份 wiki 作為**唯一的知識來源**，製作一份教學型 HTML 簡報。

- **觀眾**：沒用過 Git 的大學生、研究生
- **教學目標**：看完能說明「為什麼需要版本控制」，並能完成 commit、push 到 GitHub 的基本流程
- **整理與製作**：由 Claude Code 依 [CLAUDE.md](CLAUDE.md) 的規則進行，每一步都在 [wiki/log.md](wiki/log.md) 留下紀錄

## 怎麼看

| 內容 | 位置 |
|---|---|
| 首頁 | [index.html](index.html)：連到簡報與 wiki |
| 簡報（17 張） | [slides/index.html](slides/index.html)：鍵盤左右鍵或畫面按鈕換頁，手機也能看 |
| 簡報大綱 | [slides/outline.md](slides/outline.md)：每張的教學目標、要點與依據 |
| wiki 目錄 | [wiki/index.md](wiki/index.md) |
| 新手學習路線 | [wiki/overview.md](wiki/overview.md)：也記錄了簡報範圍的所有決定 |

在本機看簡報，可以在專案資料夾執行下列指令，再用瀏覽器開啟 http://127.0.0.1:8765/ ：

```
python -m http.server 8765 --bind 127.0.0.1 --directory slides
```

## 專案結構

```
├── CLAUDE.md          專案規則（給 Claude Code 看）
├── README.md          本文件
├── WORKFLOW.md        流程設計與實際執行的回顧
├── index.html         首頁
├── raw/               原始資料（寫入後不可修改）
├── wiki/
│   ├── index.md       所有 wiki 頁面的目錄
│   ├── overview.md    新手學習路線與簡報範圍決定
│   ├── log.md         操作紀錄（只能往後新增）
│   ├── sources/       每篇原始資料一頁摘要
│   └── concepts/      每個概念一頁
├── checks/            逐句核對的對照表（wiki 的每句話對應到原文的哪一句）
├── slides/
│   ├── outline.md     簡報大綱
│   └── index.html     教學簡報
└── tools/             檢查與轉檔工具
```

## 資料來源

| 編號 | 標題 | 出處 | 授權 | 保存方式 |
|---|---|---|---|---|
| S01 | Pro Git 1.1 About Version Control、1.3 What is Git? | git-scm.com | CC BY-NC-SA 3.0 | 全文 |
| S02 | Pro Git 2.2 Recording Changes to the Repository | git-scm.com | CC BY-NC-SA 3.0 | 全文 |
| S03 | Pro Git 1.6 First-Time Git Setup | git-scm.com | CC BY-NC-SA 3.0 | 全文 |
| S04 | Pro Git 2.1 Getting a Git Repository | git-scm.com | CC BY-NC-SA 3.0 | 全文 |
| S05 | Pro Git 2.4 Undoing Things | git-scm.com | CC BY-NC-SA 3.0 | 全文 |
| S06 | Pro Git 2.5 Working with Remotes | git-scm.com | CC BY-NC-SA 3.0 | 全文 |
| S07 | Adding locally hosted code to GitHub | GitHub Docs | CC BY 4.0 | 全文 |
| S08 | Managing your personal access tokens | GitHub Docs | CC BY 4.0 | 全文 |
| S09 | Git password authentication is shutting down | GitHub Blog（GitHub Changelog） | 未標示 | 摘錄 |

《Pro Git》第 2 版由 Scott Chacon、Ben Straub 撰寫，Apress 出版，取自 git-scm.com。授權允許轉載的資料以 curl 下載後用程式轉成 markdown，保存全文。授權未標示的 S09 只保存連結、兩個引用片段與自己的摘要。原始資料的版權屬於原作者，依各自的授權保存，每個 raw 檔開頭的資訊區塊都記有網址、授權與取得日期。

## 工作流程

1. **Ingest**：一次加入一篇資料。先存進 `raw/`，在對話中討論重點與要新增的頁面，經使用者確認後才寫入 wiki。
2. **逐句核對**：寫入後把每一句事實陳述對照原文的英文原句，寫成 `checks/Sxx-quotes.md`，用程式確認原句確實存在，找不到原句的句子要刪除或改寫。
3. **Lint**：定期檢查孤立頁面、斷掉的連結、互相矛盾的說法、沒有標註來源的句子，以及過時資訊的標註。
4. **大綱與簡報**：只讀 wiki 規劃大綱，經使用者確認後產生簡報，再逐張檢查內容是否都能在 wiki 找到。

詳細規則見 [CLAUDE.md](CLAUDE.md)，每一次操作、檢查失敗與重新生成都記在 [wiki/log.md](wiki/log.md)。

依 log.md 與 checks/ 整理的流程圖（最初設計與實際使用的流程）、各節點的錯誤統計、流程修改紀錄與逐句核對的數字，見 [WORKFLOW.md](WORKFLOW.md)。

## 工具

只使用 Python 標準函式庫（Windows 用 `python`，macOS / Linux 用 `python3`）。

| 指令 | 用途 |
|---|---|
| `python tools/check.py` | 檢查所有能自動判斷的規則：raw 的資訊區塊與是否被修改、wiki 格式、來源標註、連結、log 格式、分號、簡報的 data-sources 與過時用語 |
| `python tools/verify_quotes.py` | 驗證 `checks/` 對照表中的英文原句都逐字存在於 raw |
| `python tools/build_slides.py` | 由大綱與程式中的投影片內容產生 `slides/index.html` |
| `python tools/html2md.py` | 把 curl 下載的 Pro Git 網頁轉成 markdown |
| `python tools/md2raw.py` | 原文本身是 markdown 時，加上資訊區塊存成 raw |
