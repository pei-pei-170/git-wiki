# S09 逐句核對

- 對象：S09（GitHub Changelog〈Git password authentication is shutting down〉）ingest 時新增或修改的事實陳述
- 不列入核對：標註「（Sxx 討論）」的專案決定、overview.md「簡報範圍決定」中的取捨，以及摘要頁資訊區塊中的授權與年份（關於資料本身的後設資訊）
- 核對日期：2026-11-22
- 驗證方式：`python tools/verify_quotes.py checks/S09-quotes.md`
- 備註：S09 依第 3 節只保存摘錄，原句對應 raw 中保存的兩個引用片段

## 1｜sources/S09 重點 1
- 句子：從 2021 年 8 月 13 日太平洋標準時間 09:00 起，在 GitHub.com 驗證 Git 操作時，不再接受帳號密碼。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 2｜sources/S09 重點 2
- 句子：所有需要驗證的 Git 操作，都必須改用以 token 為基礎的驗證方式。
- 來源：S09
- 原句：
  - token-based authentication
  - will be required for all authenticated Git operations

## 3｜sources/S09 重點 3
- 句子：以 token 為基礎的驗證方式，原文舉的例子有 personal access token、OAuth、SSH key，以及 GitHub App installation token。
- 來源：S09
- 原句：
  - token-based authentication (for example, personal access, OAuth, SSH Key, or GitHub App installation token)

## 4｜sources/S09 時效風險
- 句子：說明的是 2021 年 8 月 13 日起生效的變更。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST

## 5｜sources/S09 衝突 1
- 句子：S08 說 PAT 可以代替密碼，S09 說 GitHub 已不接受帳號密碼，兩者一致。
- 來源：S08、S09
- 原句：
  - You can use a personal access token in place of a password
  - we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 6｜sources/S09 衝突 2
- 句子：S09 把 SSH key 也列為以 token 為基礎的驗證方式之一。
- 來源：S09
- 原句：
  - token-based authentication (for example, personal access, OAuth, SSH Key, or GitHub App installation token)

## 7｜personal-access-token 為什麼不能用密碼
- 句子：從 2021 年 8 月 13 日起，在 GitHub.com 驗證 Git 操作時，GitHub 不再接受帳號密碼，所有需要驗證的 Git 操作，都必須使用以 token 為基礎的驗證方式。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com
  - token-based authentication
  - will be required for all authenticated Git operations

## 8｜personal-access-token 為什麼不能用密碼
- 句子：這些方式除了 personal access token，還有 OAuth、SSH key 與 GitHub App installation token。
- 來源：S09
- 原句：
  - (for example, personal access, OAuth, SSH Key, or GitHub App installation token)

## 9｜personal-access-token 誤解（新增）
- 句子：從 2021 年 8 月 13 日起，在 GitHub.com 驗證 Git 操作時不再接受帳號密碼。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 10｜personal-access-token 過時
- 句子：在 GitHub.com 驗證 Git 操作時使用帳號密碼。
- 來源：S09
- 原句：
  - we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 11｜personal-access-token 現行做法
- 句子：從 2021 年 8 月 13 日起，GitHub 不再接受帳號密碼，需要驗證的 Git 操作都必須使用以 token 為基礎的驗證方式，例如 personal access token。透過 HTTPS 時，在密碼提示輸入 personal access token。
- 來源：S09、S08
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords
  - token-based authentication (for example, personal access
  - will be required for all authenticated Git operations
  - When prompted for your password, enter your personal access token instead of a password.

## 12｜git-push 時效註記（新增）
- 句子：GitHub 從 2021 年 8 月 13 日起不再接受用帳號密碼驗證 Git 操作。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 13｜push-to-github 時效註記（新增）
- 句子：GitHub 從 2021 年 8 月 13 日起不再接受用帳號密碼驗證 Git 操作。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 14｜overview 第 14 項（新增）
- 句子：GitHub 從 2021 年 8 月 13 日起，不再接受用帳號密碼驗證 Git 操作。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com

## 15｜index S09 說明
- 句子：2021 年 8 月 13 日起不再接受用帳號密碼驗證 Git 操作。
- 來源：S09
- 原句：
  - starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com
