# CLAUDE.md：Git 與 GitHub 入門 LLM Wiki

這份文件是給 Claude Code 看的專案規則。每次開始工作前請先完整讀完，並遵守第 9 節的檢查流程。

## 1. 專案目的

1. 依照 Karpathy 的 LLM Wiki 模式，建立一份「Git 與 GitHub 入門」的知識庫：原始資料放在 `raw/`，由 Claude 整理成互相連結的 wiki 頁面。
2. 再以這份 wiki 為**唯一知識來源**，製作一份教學型 HTML 簡報。

簡報的觀眾是**沒用過 Git 的大學生、研究生**。看完後要能說明「為什麼需要版本控制」，並能完成 commit、push 到 GitHub 的基本流程。

所有中文一律使用台灣繁體中文與台灣用語（例如「程式」不是「程序」、「資料」不是「數據」、「預設」不是「默認」）。

## 2. 檔案結構

```
git-wiki/
├── CLAUDE.md              ← 本文件
├── README.md              ← 給人看的專案介紹
├── index.html             ← 網站首頁：連到簡報與 GitHub 上的 wiki
├── raw/                   ← 原始資料（寫入後不可修改）
│   └── S01-<slug>.md
├── wiki/
│   ├── index.md           ← 所有 wiki 頁面的目錄
│   ├── overview.md        ← 主題總覽：新手學 Git 的完整路線
│   ├── log.md             ← 操作紀錄（只能往後新增）
│   ├── sources/           ← 每篇原始資料一頁摘要，檔名與 raw 相同
│   └── concepts/          ← 每個概念一頁，檔名為小寫英文 slug
├── slides/
│   ├── outline.md         ← 簡報大綱
│   └── index.html         ← 教學 HTML 簡報
└── tools/
    ├── check.py           ← 規則檢查程式
    └── html2md.py         ← 把下載的 HTML 轉成 markdown（目前支援 git-scm.com 的 Pro Git 頁面）
```

## 3. 原始資料 `raw/`

- 檔名：`S<兩位數編號>-<小寫英文 slug>.md`，例如 `S01-progit-about-version-control.md`。編號依加入順序，不可重複使用。
- 每個檔案開頭必須有以下資訊區塊：

```
---
id: S01
title: 原文標題
url: https://...
publisher: 出版者或網站
published: 出版或最後更新年份（不知道就寫 unknown）
license: 授權
stored: full 或 excerpt
retrieved: YYYY-MM-DD
---
```

- **授權規則**：
  - 授權允許轉載時（《Pro Git》為 CC BY-NC-SA 3.0、GitHub Docs 為 CC BY 4.0），`stored: full`，保存原文全文。
  - 其他資料（例如 GitHub Blog），`stored: excerpt`，只保存連結、少量引用句與自己的重點摘要，不可貼上全文。
- **全文的取得方式**（`stored: full`）：
  - 必須用 `curl` 下載原始網頁，再用程式轉成 markdown 存檔（Pro Git 頁面使用 `tools/html2md.py`，其他網站需先擴充程式）。不可以用摘要或改寫的內容。
  - 存檔後要回報字數（轉換前 HTML 正文與轉換後 markdown 的字數），並列出原文第一段和最後一段讓我核對。
- 一篇資料包含多個網頁時，`url` 欄位列出所有網址，以空格分隔。
- **寫入後不可修改**：raw 是證據，wiki 寫錯時去改 wiki，不改 raw。已經 commit 過的 raw 檔案被修改、刪除或改名時，`check.py` 會回報錯誤。

## 4. Wiki 頁面格式

### 4-1. 資料摘要頁 `wiki/sources/Sxx-<slug>.md`

```
# S01｜原文標題

- 來源：連結
- 年份：2014
- 時效風險：高 / 中 / 低（越舊、越常改版的工具，風險越高）

## 重點
（3～6 點，每點都要能在 raw 原文中找到）

## 影響的 wiki 頁面
（這次新增或更新了哪些概念頁）

## 與其他資料的衝突或過時之處
（沒有就寫「無」）
```

### 4-2. 概念頁 `wiki/concepts/<slug>.md`

```
# Commit（提交）

> 一句話定義。[S02]

## 白話解釋
## 指令範例
## 新手常見誤解
## 時效註記
## 相關頁面
## 來源
```

- **每一段事實陳述的句尾都要標註來源**，例如 `[S02]`。標註的來源必須存在於 `raw/`。
- **不可加入 raw 中沒有的知識**。覺得重要但找不到來源的內容，寫進 `log.md` 的「待找資料」，不要寫進 wiki。
- **專案的教學決定**（例如簡報要怎麼改編範例）不是知識，句尾標註「（Sxx 討論）」，代表依據是 `log.md` 中該次 ingest 的討論結果；決定中引用的事實仍要標註 `[Sxx]`。
- 「相關頁面」用相對連結互相連結，例如 `[Branch（分支）](branch.md)`。
- 「時效註記」沒有就寫「無」。

### 4-3. 過時資訊的處理

不同年份的資料說法不一致時，**兩種說法都保留並標註年份**，不可默默覆蓋：

```
> ⚠️ 過時：《Pro Git》使用 `git checkout` 切換分支 [S03, 2014]。
> 現行做法：Git 2.23 起新增 `git switch` 專門用來切換分支 [S06, 2019]。
```

年份標註原文陳述該說法的年份。線上版的內容可能在出版後修訂（例如《Pro Git》線上版加入了 2020 年的說明），這時可以標註文中寫明的年份，但不可早於 raw 的 `published`。

簡報一律教現行做法，必要時再補充舊寫法。

### 4-4. `wiki/index.md` 與 `wiki/overview.md`

- `index.md` 依「資料摘要」「概念」分類，列出每一頁的連結與一句話說明。每次新增頁面都要更新。
- `overview.md` 用新手學習順序把概念串起來，是規劃簡報大綱的起點。

## 5. Ingest：加入一篇資料（先討論、後生成）

每次只加入一篇資料，步驟如下：

1. 讀取資料，依第 3 節存到 `raw/`（`stored: full` 要用 curl 下載、程式轉檔，並回報字數與首尾段）。
2. **在對話中提出討論，然後停下來等我回覆**，內容包含：
   - 這篇資料的 3～6 個重點
   - 預計新增或更新哪些概念頁
   - 與既有 wiki 有沒有衝突或過時的地方
   - 哪些內容適合新手、哪些太進階不放進簡報
3. 我確認或調整後，才寫入 wiki：摘要頁、概念頁、更新 `index.md` 與 `overview.md`。
4. 執行 `python tools/check.py`，有錯誤就修正。
5. 在 `log.md` 寫一筆紀錄（格式見第 7 節）。
6. 依第 11 節格式 commit。

**未經我確認就寫入 wiki，視為違反規則。**

## 6. 製作簡報

### 6-1. 規劃大綱 `slides/outline.md`

1. 只讀 `wiki/` 的內容規劃，**不可讀 `raw/` 或上網查資料**。wiki 不夠就停下來告訴我缺什麼。
2. 教學結構：引起動機的問題 → 觀念 → 實際操作 → 常見錯誤 → 總結 → 小測驗，共 12～18 張。
3. 每張投影片在大綱中列出：

```
## 第 3 張｜什麼是 Commit
- 教學目標：看完能說明 commit 是什麼
- 要點：……
- 依據：concepts/commit.md、sources/S02-....md
```

4. **大綱完成後停下來等我確認**，才開始做 HTML。

### 6-2. 產生 HTML `slides/index.html`

- 單一 HTML 檔，不使用任何框架或 CDN 套件，只允許 Google Fonts。
- 每張投影片是一個 `<section class="slide" data-sources="concepts/commit.md sources/S02-....md">`，`data-sources` 必須與大綱的「依據」相同。
- 每張投影片底部用小字顯示資料來源，並連到 GitHub 上對應的 wiki 頁面，讓讀者可以追溯。
- 支援鍵盤左右鍵與畫面按鈕換頁、顯示頁碼，手機也能瀏覽。
- 新手看不懂的術語，第一次出現時要先解釋。

### 6-3. 逐張檢查與重新生成

每完成一張投影片就檢查：內容是否都能在 `data-sources` 的 wiki 頁找到、術語是否已定義、有沒有使用過時寫法。不通過就重新生成**那一張**，最多重試 2 次，仍不通過就停下來回報我。每次重新生成都要記錄在 `log.md`。

## 7. 操作紀錄 `wiki/log.md`

每次操作在檔案最後新增一筆，不可刪改舊紀錄：

```
## 2026-11-22 16:10｜ingest｜S01
- 做了什麼：新增 sources/S01-...、concepts/version-control.md
- 討論結果：使用者要求「集中式版本控制」不放進簡報
- 檢查結果：check.py 通過 / 發現 2 個錯誤（列出）並已修正
- 待找資料：（沒有就寫「無」）
```

操作類型：`setup`（建立或調整專案結構、規則、工具）、`ingest`、`lint`、`outline`、`slide`、`regenerate`、`fix`。**檢查失敗和重新生成也要照實記錄**，這是之後反思流程設計的依據。

## 8. Lint：健康檢查

每 ingest 2～3 篇，或我說「lint」時執行，檢查：

- 有沒有孤立頁面（沒有任何頁面連到它）、斷掉的連結
- 不同頁面之間有沒有互相矛盾的說法
- 有沒有句子沒標來源，或標註的來源不存在
- 過時資訊有沒有照第 4-3 節標註

結果寫進 `log.md`，能修正的直接修正，需要判斷的列出來問我。

## 9. 檢查程式

```bash
python tools/check.py
```

（這個專案在 Windows 上開發，macOS / Linux 請改用 `python3`。）

`tools/check.py` 需檢查以下能自動判斷的規則，有錯誤時以結束代碼 1 結束：

- `raw/` 每個檔案的資訊區塊欄位齊全，`stored` 與 `license` 符合第 3 節規則
- `raw/` 中已經 commit 過的檔案，在工作目錄或之後的 commit 中被修改、刪除或改名（需要 git）
- `log.md` 每筆紀錄的標題格式、操作類型與欄位符合第 7 節
- `wiki/sources/` 與 `raw/` 一一對應
- 概念頁具備第 4-2 節的所有段落，且至少標註一個來源
- 所有 `[Sxx]` 標註都對應到存在的 raw 檔案
- wiki 內部連結沒有斷掉、沒有孤立頁面、每一頁都列在 `index.md`
- 簡報：每張 `section.slide` 都有 `data-sources`，且指向存在的 wiki 頁面；投影片張數與 `outline.md` 一致
- **過時用語**：簡報中出現下列用語時發出錯誤，除非該投影片有 `data-legacy` 屬性（代表是刻意說明舊寫法，或說明 Git 本身的預設值）：
  - `git checkout`（切換分支請用 `git switch`）
  - `master`：本簡報教學生用 `init.defaultBranch` 把預設分支設成 `main`，與 GitHub 新 repository 的預設一致 [S02, S03]，範例輸出依 `wiki/concepts/default-branch.md` 改編為 `main`。說明「Git 本身預設是 `master`」的投影片要加上 `data-legacy`。
  - 用帳號密碼推送到 GitHub（需改用 personal access token 或 SSH）

  發現新的過時用語時，要加進這份清單與 `check.py`。

程式無法判斷的部分（內容是否正確、新手是否看得懂），由 Claude 自行檢查並在回報中說明。

## 10. 禁止事項

- 不可修改 `raw/` 中已存在的檔案。
- 不可加入沒有來源的知識，也不可讓簡報內容超出 wiki。
- 未經確認不可跳過第 5、6 節中「停下來等我確認」的步驟。
- 不可刪改 `log.md` 的舊紀錄。

## 11. Commit 訊息格式

```
<類型>: <說明>
```

類型為 `ingest`、`wiki`、`slides`、`tools`、`docs`。例如：`ingest: S03 Pro Git 分支簡介`。
