# S01｜Pro Git 1.1 About Version Control；1.3 What is Git?

- 來源：[1.1 Getting Started - About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)、[1.3 Getting Started - What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)（《Pro Git》第 2 版，Scott Chacon、Ben Straub 著，CC BY-NC-SA 3.0）
- 年份：2014（第 2 版印刷版年份；線上版持續修訂，本次取得日期為 2026-11-22）
- 時效風險：中

## 重點

1. 版本控制是記錄一個或一組檔案隨時間變化的系統，之後可以叫回特定版本；不只程式碼，幾乎任何類型的檔案都適用。[S01]
2. 版本控制系統分為本地、集中式、分散式三類：集中式有伺服器單點故障的風險，分散式的每一份 clone 都是完整備份。[S01]
3. Git 把資料視為一連串的快照，而不是每個檔案的差異清單；沒有變更的檔案只存連結。[S01]
4. Git 幾乎所有操作都在本地進行，因此速度快，離線也能 commit。[S01]
5. Git 用 SHA-1 雜湊值檢查資料完整性，而且操作幾乎只會新增資料，commit 之後就很難遺失。[S01]
6. 檔案有已修改、已暫存、已提交三種狀態，對應工作目錄、暫存區、Git 目錄三個區域，基本流程是「修改 → 暫存 → commit」。[S01]

## 影響的 wiki 頁面

- 新增 [版本控制（Version Control）](../concepts/version-control.md)
- 新增 [Git](../concepts/git.md)
- 新增 [三種狀態與三個區域](../concepts/three-states.md)

## 與其他資料的衝突或過時之處

- 目前沒有其他資料可以比對。
- 線上版會持續修訂，內容不一定等於 2014 年的印刷版；之後若有其他年份的資料，需要比對用語與說法。
- 原文多處的 check out 是一般動詞「取出」，不是 Git 指令，說明見 [三種狀態與三個區域](../concepts/three-states.md) 的「新手常見誤解」。
