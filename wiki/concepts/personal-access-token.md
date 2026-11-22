# Personal access token（個人存取權杖）

> Personal access token（簡稱 PAT）是在命令列或透過 API 向 GitHub 驗證身分時，可以用來代替密碼的 token。[S08]

## 白話解釋

**要像對待密碼一樣對待 token。** PAT 和密碼一樣，有相同的安全風險。[S08]

PAT 是用來代表你自己存取 GitHub 資源的。[S08] token 能存取的資源與能做的動作，和 token 的擁有者相同，還會再受到 token 被授予的範圍或權限限制，token 不能給使用者額外的存取能力。[S08]

### 兩種 PAT

| 類型 | 說明 |
|---|---|
| fine-grained personal access token | GitHub 建議盡可能使用這一種。每個 token 只能存取單一使用者或組織擁有的資源，還可以再限定只能存取特定的 repository，並授予特定的細緻權限。[S08] |
| personal access token (classic) | 比較不安全，可以存取你在組織中能存取的所有 repository，以及個人帳號中所有的個人 repository。但目前有些功能只有 classic 能用。[S08] |

fine-grained token 雖然比較安全、容易控制，但不能完成 classic token 能做的每一件事。[S08]

### 安全建議

- 建立新的 PAT 之前，先考慮有沒有更安全的驗證方式。例如要從命令列存取 GitHub，可以改用 GitHub CLI 或 Git Credential Manager，不必建立 PAT。[S08]
- GitHub 會自動移除一年沒用過的 token。為了更安全，原文強烈建議替 token 設定有效期限。[S08]
- repository 的存取範圍與權限，都應該選擇符合需要的最小範圍。[S08]
- 不再需要的 token 應該刪除。[S08]

### 建立 fine-grained token 的步驟

1. 如果 email 還沒驗證，先驗證 email。[S08]
2. 在 GitHub 任一頁面的右上角點大頭貼，再點 Settings。[S08]
3. 在左側欄點 Developer settings。[S08]
4. 在左側欄的 Personal access tokens 底下，點 Fine-grained tokens。[S08]
5. 點 Generate new token。[S08]
6. 在 Token name 輸入 token 的名稱。[S08]
7. 在 Expiration 選擇 token 的有效期限。[S08]
8. 在 Resource owner 選擇資源擁有者，token 只能存取這個擁有者的資源。[S08]
9. 在 Repository access 選擇要讓 token 存取哪些 repository，應選擇符合需要的最小範圍。token 一定包含 GitHub 上所有公開 repository 的唯讀權限。[S08]
10. 在 Permissions 選擇要授予 token 的權限，應選擇符合需要的最小權限。[S08]
11. 點 Generate token。[S08]

原文列出的常用範例網址中，「Push access to repositories」的設定是 `contents=write`，也就是把 Contents 權限設成 write。[S08]

### 在命令列使用

有了 PAT 之後，透過 HTTPS 進行 Git 操作時，就可以輸入它來代替密碼。[S08] 例如在命令列 clone 時，會提示你輸入使用者名稱和密碼，在密碼提示時，輸入 PAT 而不是密碼。[S08] 使用者名稱仍然要輸入，但驗證身分靠的是 PAT，不輸入使用者名稱會收到憑證無效的錯誤訊息。[S08]

PAT 只能用在 HTTPS 的 Git 操作。如果 repository 使用 SSH 的遠端網址，需要把遠端從 SSH 改成 HTTPS。[S08]

如果沒有出現使用者名稱和密碼的提示，你的憑證可能已經快取在電腦上。[S08] 也可以用 Git 用戶端快取 PAT，不必每次手動輸入，Git 會把憑證暫時存在記憶體中，直到超過有效時間為止。[S08]

## 指令範例

在命令列 clone 時，在 `Password` 提示輸入 PAT：[S08]

```shell
$ git clone https://github.com/USERNAME/REPO.git
Username: YOUR-USERNAME
Password: YOUR-PERSONAL-ACCESS-TOKEN
```

## 新手常見誤解

- **以為 `Password` 提示要輸入 GitHub 的密碼**：在密碼提示時，輸入 PAT 而不是密碼。[S08]
- **以為有了 token 就不用輸入使用者名稱**：使用者名稱仍然要輸入，不輸入會收到憑證無效的錯誤訊息。[S08]
- **以為 token 外流沒關係**：PAT 和密碼一樣，有相同的安全風險，要像對待密碼一樣對待它。[S08]
- **以為權限給越多越方便**：repository 的存取範圍與權限，都應該選擇符合需要的最小範圍。[S08]

## 時效註記

- fine-grained token 目前不支援 classic token 的所有功能，原文說 GitHub 正在補上這些缺口，會隨時間解決。[S08]

## 相關頁面

- [git push（推送到遠端）](git-push.md)：push 到 GitHub 時，用 PAT 驗證身分
- [把本地 repository 推上 GitHub](push-to-github.md)：完整流程中的身分驗證
- [Remote（遠端 repository）](remote.md)：PAT 只能用在 HTTPS 的遠端網址

## 來源

- [S08｜Managing your personal access tokens](../sources/S08-github-personal-access-tokens.md)
