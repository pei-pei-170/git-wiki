# S08 逐句核對

- 對象：S08（GitHub Docs〈Managing your personal access tokens〉）ingest 時新增或修改的事實陳述
- 不列入核對：標註「（Sxx 討論）」的專案決定、overview.md「簡報範圍決定」中的取捨，以及摘要頁資訊區塊中的年份說明（關於資料本身的後設資訊）
- 核對日期：2026-11-22
- 驗證方式：`python tools/verify_quotes.py checks/S08-quotes.md`
- 備註：S08 原文是 markdown，原句照原文保留 markdown 與 HTML 標記以便逐字比對

## 1｜sources/S08 重點 1
- 句子：在命令列或透過 API 向 GitHub 驗證身分時，可以用 personal access token 代替密碼。要像對待密碼一樣對待 token。
- 來源：S08
- 原句：
  - You can use a personal access token in place of a password when authenticating to GitHub in the command line or with the API.
  - Treat your access tokens like passwords.

## 2｜sources/S08 重點 2
- 句子：GitHub 目前支援 fine-grained personal access token 與 personal access token (classic) 兩種，並建議盡可能使用 fine-grained。classic 比較不安全，可以存取你能存取的所有 repository。
- 來源：S08
- 原句：
  - GitHub currently supports two types of personal access tokens: fine-grained personal access tokens and personal access tokens (classic).
  - GitHub recommends that you use fine-grained personal access tokens instead of personal access tokens (classic) whenever possible.
  - Personal access tokens (classic) are less secure.
  - Your personal access token (classic) can access every repository that you can access.

## 3｜sources/S08 重點 3
- 句子：建立 PAT 之前，先考慮有沒有更安全的驗證方式，例如在命令列改用 GitHub CLI 或 Git Credential Manager。GitHub 會自動移除一年沒用的 token，也強烈建議替 token 設定有效期限。
- 來源：S08
- 原句：
  - Before creating a new personal access token, consider if there is a more secure method of authentication available to you:
  - To access GitHub from the command line, you can use [GitHub CLI](/en/github-cli/github-cli/about-github-cli) or [Git Credential Manager]
  - As a security precaution, GitHub automatically removes personal access tokens that haven't been used in a year. To provide additional security, we highly recommend adding an expiration to your personal access tokens.

## 4｜sources/S08 重點 4
- 句子：建立 fine-grained token 時，要設定名稱、有效期限、資源擁有者、repository 存取範圍與權限。存取範圍與權限都應該選擇符合需要的最小範圍。
- 來源：S08
- 原句：
  - Under **Token name**, enter a name for the token.
  - Under **Expiration**, select an expiration for the token.
  - Under **Resource owner**, select a resource owner.
  - Under **Repository access**, select which repositories you want the token to access.
  - Under **Permissions**, select which permissions to grant the token.
  - You should choose the minimal repository access that meets your needs.
  - You should choose the minimal permissions necessary for your needs.

## 5｜sources/S08 重點 5
- 句子：透過 HTTPS 進行 Git 操作時，出現密碼提示就輸入 PAT。使用者名稱仍然要輸入，但驗證身分靠的是 token。PAT 只能用在 HTTPS 的 Git 操作。
- 來源：S08
- 原句：
  - Once you have a personal access token, you can enter it instead of your password when performing Git operations over HTTPS.
  - Although you are required to enter your username along with your personal access token, the username is not used to authenticate you. Instead, the personal access token is used to authenticate you.
  - Personal access tokens can only be used for HTTPS Git operations.

## 6｜sources/S08 重點 6
- 句子：可以用 Git 用戶端快取 PAT，不必每次手動輸入。不再需要的 token 應該刪除。
- 來源：S08
- 原句：
  - Instead of manually entering your personal access token for every HTTPS Git operation, you can cache your personal access token with a Git client.
  - You should delete a personal access token if it is no longer needed.

## 7｜sources/S08 時效風險
- 句子：原文也說 fine-grained token 的功能缺口會隨時間補上。
- 來源：S08
- 原句：
  - All of these gaps will be solved over time, as GitHub continues to invest in more secure access patterns.

## 8｜sources/S08 衝突 1
- 句子：S07 說用 Git 把本地 repository 加到 GitHub 之前，必須先在命令列完成身分驗證，S08 補上做法：透過 HTTPS 進行 Git 操作時，在密碼提示輸入 PAT。
- 來源：S07、S08
- 原句：
  - Before you can add your local repository to GitHub using Git, you must authenticate to GitHub on the command line.
  - When prompted for your password, enter your personal access token instead of a password.

## 9｜sources/S08 衝突 2
- 句子：S08 說 PAT 可以代替密碼。
- 來源：S08
- 原句：
  - You can use a personal access token in place of a password

## 10｜personal-access-token 定義
- 句子：Personal access token 是在命令列或透過 API 向 GitHub 驗證身分時，可以用來代替密碼的 token。
- 來源：S08
- 原句：
  - You can use a personal access token in place of a password when authenticating to GitHub in the command line or with the API.

## 11｜personal-access-token 白話
- 句子：要像對待密碼一樣對待 token。PAT 和密碼一樣，有相同的安全風險。
- 來源：S08
- 原句：
  - Treat your access tokens like passwords.
  - Personal access tokens are like passwords, and they share the same inherent security risks.

## 12｜personal-access-token 白話
- 句子：PAT 是用來代表你自己存取 GitHub 資源的。
- 來源：S08
- 原句：
  - Personal access tokens are intended to access GitHub resources on behalf of yourself.

## 13｜personal-access-token 白話
- 句子：token 能存取的資源與能做的動作，和 token 的擁有者相同，還會再受到 token 被授予的範圍或權限限制，token 不能給使用者額外的存取能力。
- 來源：S08
- 原句：
  - A token has the same capabilities to access resources and perform actions on those resources that the owner of the token has, and is further limited by any scopes or permissions granted to the token. A token cannot grant additional access capabilities to a user.

## 14｜personal-access-token 兩種 PAT（fine-grained）
- 句子：GitHub 建議盡可能使用這一種。每個 token 只能存取單一使用者或組織擁有的資源，還可以再限定只能存取特定的 repository，並授予特定的細緻權限。
- 來源：S08
- 原句：
  - GitHub recommends that you use fine-grained personal access tokens instead of personal access tokens (classic) whenever possible.
  - Each token is limited to access resources owned by a single user or organization.
  - Each token can be further limited to only access specific repositories for that user or organization.
  - Each token is granted specific, fine-grained permissions

## 15｜personal-access-token 兩種 PAT（classic）
- 句子：比較不安全，可以存取你在組織中能存取的所有 repository，以及個人帳號中所有的個人 repository。但目前有些功能只有 classic 能用。
- 來源：S08
- 原句：
  - Personal access tokens (classic) are less secure. However, some features currently will only work with personal access tokens (classic):
  - it will grant access to all repositories within the organizations that you have access to, as well as all personal repositories in your personal account.

## 16｜personal-access-token 兩種 PAT
- 句子：fine-grained token 雖然比較安全、容易控制，但不能完成 classic token 能做的每一件事。
- 來源：S08
- 原句：
  - Fine-grained personal access tokens, while more secure and controllable, cannot accomplish every task that a personal access token (classic) can.

## 17｜personal-access-token 安全建議 1
- 句子：建立新的 PAT 之前，先考慮有沒有更安全的驗證方式。例如要從命令列存取 GitHub，可以改用 GitHub CLI 或 Git Credential Manager，不必建立 PAT。
- 來源：S08
- 原句：
  - Before creating a new personal access token, consider if there is a more secure method of authentication available to you:
  - To access GitHub from the command line, you can use [GitHub CLI](/en/github-cli/github-cli/about-github-cli) or [Git Credential Manager]
  - instead of creating a personal access token.

## 18｜personal-access-token 安全建議 2
- 句子：GitHub 會自動移除一年沒用過的 token。為了更安全，原文強烈建議替 token 設定有效期限。
- 來源：S08
- 原句：
  - As a security precaution, GitHub automatically removes personal access tokens that haven't been used in a year. To provide additional security, we highly recommend adding an expiration to your personal access tokens.

## 19｜personal-access-token 安全建議 3
- 句子：repository 的存取範圍與權限，都應該選擇符合需要的最小範圍。
- 來源：S08
- 原句：
  - You should choose the minimal repository access that meets your needs.
  - You should choose the minimal permissions necessary for your needs.

## 20｜personal-access-token 安全建議 4
- 句子：不再需要的 token 應該刪除。
- 來源：S08
- 原句：
  - You should delete a personal access token if it is no longer needed.

## 21｜personal-access-token 步驟 1
- 句子：如果 email 還沒驗證，先驗證 email。
- 來源：S08
- 原句：
  - [Verify your email address](/en/account-and-profile/how-tos/email-preferences/verifying-your-email-address), if it hasn't been verified yet.

## 22｜personal-access-token 步驟 2
- 句子：在 GitHub 任一頁面的右上角點大頭貼，再點 Settings。
- 來源：S08
- 原句：
  - In the upper-right corner of any page on GitHub, click your profile picture, then click
  - Settings**.

## 23｜personal-access-token 步驟 3
- 句子：在左側欄點 Developer settings。
- 來源：S08
- 原句：
  - In the left sidebar, click
  - Developer settings**.

## 24｜personal-access-token 步驟 4
- 句子：在左側欄的 Personal access tokens 底下，點 Fine-grained tokens。
- 來源：S08
- 原句：
  - In the left sidebar, under
  - Personal access tokens**, click **Fine-grained tokens**.

## 25｜personal-access-token 步驟 5
- 句子：點 Generate new token。
- 來源：S08
- 原句：
  - Click **Generate new token**.

## 26｜personal-access-token 步驟 6
- 句子：在 Token name 輸入 token 的名稱。
- 來源：S08
- 原句：
  - Under **Token name**, enter a name for the token.

## 27｜personal-access-token 步驟 7
- 句子：在 Expiration 選擇 token 的有效期限。
- 來源：S08
- 原句：
  - Under **Expiration**, select an expiration for the token.

## 28｜personal-access-token 步驟 8
- 句子：在 Resource owner 選擇資源擁有者，token 只能存取這個擁有者的資源。
- 來源：S08
- 原句：
  - Under **Resource owner**, select a resource owner. The token will only be able to access resources owned by the selected resource owner.

## 29｜personal-access-token 步驟 9
- 句子：在 Repository access 選擇要讓 token 存取哪些 repository，應選擇符合需要的最小範圍。token 一定包含 GitHub 上所有公開 repository 的唯讀權限。
- 來源：S08
- 原句：
  - Under **Repository access**, select which repositories you want the token to access. You should choose the minimal repository access that meets your needs. Tokens always include read-only access to all public repositories on GitHub.

## 30｜personal-access-token 步驟 10
- 句子：在 Permissions 選擇要授予 token 的權限，應選擇符合需要的最小權限。
- 來源：S08
- 原句：
  - Under **Permissions**, select which permissions to grant the token.
  - You should choose the minimal permissions necessary for your needs.

## 31｜personal-access-token 步驟 11
- 句子：點 Generate token。
- 來源：S08
- 原句：
  - Click **Generate token**.

## 32｜personal-access-token 範例網址
- 句子：原文列出的常用範例網址中，「Push access to repositories」的設定是 contents=write，也就是把 Contents 權限設成 write。
- 來源：S08
- 原句：
  - Below are some example URLs that generate the tokens we see most often:
  - [Push access to repositories](https://github.com/settings/personal-access-tokens/new?name=Repo-writing+token
  - Just+contents:write\&contents=write)

## 33｜personal-access-token 命令列使用
- 句子：有了 PAT 之後，透過 HTTPS 進行 Git 操作時，就可以輸入它來代替密碼。
- 來源：S08
- 原句：
  - Once you have a personal access token, you can enter it instead of your password when performing Git operations over HTTPS.

## 34｜personal-access-token 命令列使用
- 句子：例如在命令列 clone 時，會提示你輸入使用者名稱和密碼，在密碼提示時，輸入 PAT 而不是密碼。
- 來源：S08
- 原句：
  - For example, to clone a repository on the command line you would enter the following `git clone` command. You would then be prompted to enter your username and password. When prompted for your password, enter your personal access token instead of a password.

## 35｜personal-access-token 命令列使用
- 句子：使用者名稱仍然要輸入，但驗證身分靠的是 PAT，不輸入使用者名稱會收到憑證無效的錯誤訊息。
- 來源：S08
- 原句：
  - Although you are required to enter your username along with your personal access token, the username is not used to authenticate you. Instead, the personal access token is used to authenticate you.
  - If you do not enter a username, you will receive an error message that your credentials are invalid.

## 36｜personal-access-token 命令列使用
- 句子：PAT 只能用在 HTTPS 的 Git 操作。如果 repository 使用 SSH 的遠端網址，需要把遠端從 SSH 改成 HTTPS。
- 來源：S08
- 原句：
  - Personal access tokens can only be used for HTTPS Git operations. If your repository uses an SSH remote URL, you will need to [switch the remote from SSH to HTTPS]

## 37｜personal-access-token 命令列使用
- 句子：如果沒有出現使用者名稱和密碼的提示，你的憑證可能已經快取在電腦上。
- 來源：S08
- 原句：
  - If you are not prompted for your username and password, your credentials may be cached on your computer.

## 38｜personal-access-token 命令列使用
- 句子：也可以用 Git 用戶端快取 PAT，不必每次手動輸入，Git 會把憑證暫時存在記憶體中，直到超過有效時間為止。
- 來源：S08
- 原句：
  - Instead of manually entering your personal access token for every HTTPS Git operation, you can cache your personal access token with a Git client. Git will temporarily store your credentials in memory until an expiry interval has passed.

## 39｜personal-access-token 指令範例
- 句子：在命令列 clone 時，在 Password 提示輸入 PAT。
- 來源：S08
- 原句：
  - When prompted for your password, enter your personal access token instead of a password.
  - $ git clone https://github.com/USERNAME/REPO.git
  - Password: YOUR-PERSONAL-ACCESS-TOKEN

## 40｜personal-access-token 誤解 1
- 句子：在密碼提示時，輸入 PAT 而不是密碼。
- 來源：S08
- 原句：
  - When prompted for your password, enter your personal access token instead of a password.

## 41｜personal-access-token 誤解 2
- 句子：使用者名稱仍然要輸入，不輸入會收到憑證無效的錯誤訊息。
- 來源：S08
- 原句：
  - you are required to enter your username along with your personal access token
  - If you do not enter a username, you will receive an error message that your credentials are invalid.

## 42｜personal-access-token 誤解 3
- 句子：PAT 和密碼一樣，有相同的安全風險，要像對待密碼一樣對待它。
- 來源：S08
- 原句：
  - Personal access tokens are like passwords, and they share the same inherent security risks.
  - Treat your access tokens like passwords.

## 43｜personal-access-token 誤解 4
- 句子：repository 的存取範圍與權限，都應該選擇符合需要的最小範圍。
- 來源：S08
- 原句：
  - You should choose the minimal repository access that meets your needs.
  - You should choose the minimal permissions necessary for your needs.

## 44｜personal-access-token 時效註記
- 句子：fine-grained token 目前不支援 classic token 的所有功能，原文說 GitHub 正在補上這些缺口，會隨時間解決。
- 來源：S08
- 原句：
  - Fine-grained personal access tokens do not support every feature of personal access tokens (classic). These feature gaps are not permanent - GitHub is working to close them.
  - All of these gaps will be solved over time

## 45｜git-push 推送到 GitHub（更新）
- 句子：透過 HTTPS 進行 Git 操作時，出現密碼提示就輸入 personal access token 代替密碼。
- 來源：S08
- 原句：
  - you can enter it instead of your password when performing Git operations over HTTPS.
  - When prompted for your password, enter your personal access token instead of a password.

## 46｜git-push 誤解（更新）
- 句子：透過 HTTPS 時，在密碼提示輸入 personal access token。
- 來源：S08
- 原句：
  - When prompted for your password, enter your personal access token instead of a password.

## 47｜push-to-github 步驟二（更新）
- 句子：透過 HTTPS 進行 Git 操作時，出現密碼提示就輸入 personal access token 代替密碼。
- 來源：S08
- 原句：
  - you can enter it instead of your password when performing Git operations over HTTPS.
  - When prompted for your password, enter your personal access token instead of a password.

## 48｜push-to-github 誤解（更新）
- 句子：透過 HTTPS 時，在密碼提示輸入 personal access token。
- 來源：S08
- 原句：
  - When prompted for your password, enter your personal access token instead of a password.

## 49｜remote 推上 GitHub（更新）
- 句子：PAT 只能用在 HTTPS 的 Git 操作，如果遠端網址是 SSH，需要把遠端從 SSH 改成 HTTPS。
- 來源：S08
- 原句：
  - Personal access tokens can only be used for HTTPS Git operations. If your repository uses an SSH remote URL, you will need to [switch the remote from SSH to HTTPS]

## 50｜overview 第 14 項
- 句子：在 GitHub 建立 fine-grained token，只給最小的權限並設定有效期限。push 時出現密碼提示就輸入 token，token 要像密碼一樣保管。
- 來源：S08
- 原句：
  - GitHub recommends that you use fine-grained personal access tokens
  - You should choose the minimal permissions necessary for your needs.
  - we highly recommend adding an expiration to your personal access tokens.
  - When prompted for your password, enter your personal access token instead of a password.
  - Treat your access tokens like passwords.

## 51｜index S08 說明
- 句子：建立與使用 personal access token，在命令列代替密碼驗證身分。
- 來源：S08
- 原句：
  - You can use a personal access token in place of a password when authenticating to GitHub in the command line or with the API.

## 52｜index personal-access-token 說明
- 句子：在命令列透過 HTTPS 驗證身分時，用來代替密碼的 token。
- 來源：S08
- 原句：
  - you can enter it instead of your password when performing Git operations over HTTPS.
