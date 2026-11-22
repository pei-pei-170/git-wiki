# S08｜Managing your personal access tokens

- 來源：[Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)（GitHub Docs，CC BY 4.0）
- 年份：unknown（本次取得日期為 2026-11-22）
- 時效風險：中（網頁沒有標示年份，原文也說 fine-grained token 的功能缺口會隨時間補上）

## 重點

1. 在命令列或透過 API 向 GitHub 驗證身分時，可以用 personal access token 代替密碼。要像對待密碼一樣對待 token。[S08]
2. GitHub 目前支援 fine-grained personal access token 與 personal access token (classic) 兩種，並建議盡可能使用 fine-grained。classic 比較不安全，可以存取你能存取的所有 repository。[S08]
3. 建立 PAT 之前，先考慮有沒有更安全的驗證方式，例如在命令列改用 GitHub CLI 或 Git Credential Manager。GitHub 會自動移除一年沒用的 token，也強烈建議替 token 設定有效期限。[S08]
4. 建立 fine-grained token 時，要設定名稱、有效期限、資源擁有者、repository 存取範圍與權限。存取範圍與權限都應該選擇符合需要的最小範圍。[S08]
5. 透過 HTTPS 進行 Git 操作時，出現密碼提示就輸入 PAT。使用者名稱仍然要輸入，但驗證身分靠的是 token。PAT 只能用在 HTTPS 的 Git 操作。[S08]
6. 可以用 Git 用戶端快取 PAT，不必每次手動輸入。不再需要的 token 應該刪除。[S08]

## 影響的 wiki 頁面

- 新增 [Personal access token（個人存取權杖）](../concepts/personal-access-token.md)
- 更新 [git push（推送到遠端）](../concepts/git-push.md)、[把本地 repository 推上 GitHub](../concepts/push-to-github.md)：push 前的身分驗證接上 PAT
- 更新 [Remote（遠端 repository）](../concepts/remote.md)：PAT 只能用在 HTTPS 的遠端網址

## 與其他資料的衝突或過時之處

- 與既有 wiki 沒有矛盾。S07 說用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成身分驗證 [S07]，S08 補上做法：透過 HTTPS 進行 Git 操作時，在密碼提示輸入 PAT [S08]。
- S08 說 PAT 可以代替密碼 [S08]。「GitHub 已不接受密碼」的說法另以 S09 作為來源。（S08 討論）
