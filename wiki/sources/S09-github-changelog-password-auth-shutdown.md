# S09｜Git password authentication is shutting down

- 來源：[Git password authentication is shutting down](https://github.blog/changelog/2021-08-12-git-password-authentication-is-shutting-down/)（GitHub Changelog，授權未標示，依第 3 節只保存摘錄）
- 年份：2021
- 時效風險：低（說明的是 2021 年 8 月 13 日起生效的變更）

## 重點

1. 從 2021 年 8 月 13 日太平洋標準時間 09:00 起，在 GitHub.com 驗證 Git 操作時，不再接受帳號密碼。[S09]
2. 所有需要驗證的 Git 操作，都必須改用以 token 為基礎的驗證方式。[S09]
3. 以 token 為基礎的驗證方式，原文舉的例子有 personal access token、OAuth、SSH key，以及 GitHub App installation token。[S09]

## 影響的 wiki 頁面

- 更新 [Personal access token（個人存取權杖）](../concepts/personal-access-token.md)：新增為什麼不能用密碼，以及第 4-3 節的過時／現行做法區塊
- 更新 [git push（推送到遠端）](../concepts/git-push.md)、[把本地 repository 推上 GitHub](../concepts/push-to-github.md)：時效註記連到 PAT 頁

## 與其他資料的衝突或過時之處

- 與既有 wiki 沒有矛盾。S08 說 PAT 可以代替密碼 [S08]，S09 說 GitHub 已不接受帳號密碼 [S09, 2021]，兩者一致。
- S09 把 SSH key 也列為以 token 為基礎的驗證方式之一 [S09]。本專案不教 SSH，過時用語規則也只寫 personal access token。（S09 討論）
