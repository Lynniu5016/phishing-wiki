# 簡報大綱：釣魚郵件怎麼辨識？（v2）

- 受眾：大學生／上班族（會用 email，不懂技術）
- 規則：每個事實句標「← 概念頁 [S0X]」或「← 概念頁 [定義]」；`[教學]` 只能是問句、指示或結構性文字；`[示意]` 是重繪的示意畫面，內容必須來自標註的頁面
- 教學結構：引起動機 → 學習目標 → 概念 → 辨識技巧 → 實作 → 行動 → 測驗 → 總結
- 每張投影片底部顯示「出處」，連到 GitHub 上對應的 Wiki 頁面

---

## 1. 封面：這封信，你會點嗎？
- 示意畫面：一封電子發票通知，顯示的連結是財政部電子發票網址 [示意] ← case-taiwan-tax-phishing [S05]
- 提問：這封信哪裡有問題？上完這份簡報再回來看 [教學]

## 2. 學完你會知道
- 目標 1：說出什麼是釣魚郵件 [教學]
- 目標 2：用三個地方檢查一封信：語氣、寄件者、連結附件 [教學]
- 目標 3：在 Gmail 查看一封信有沒有通過驗證 [教學]
- 目標 4：知道收到可疑信時該怎麼做 [教學]

## 3. 為什麼要學這個？
- 2026 年第二季全球記錄到 1,069,681 起釣魚攻擊，比上一季增加 10.1%（APWG）← phishing-trends [S02]
- 釣魚是 16% 資料外洩事件的入侵途徑（Verizon DBIR 2026）← phishing-trends [S06]
- Q1→Q2 簡訊釣魚 +40%、電話釣魚 +20%（APWG）← phishing-trends [S02]

## 4. 什麼是釣魚？
- 犯罪者假裝成你信任的人或機構，引誘你點連結、開附件或交出個資 ← what-is-phishing [S01]
- 管道不只 email，還有簡訊、社群私訊、電話 ← what-is-phishing [S01]
- 兩種手段：社交工程（讓你以為對方可信）＋技術手法（植入惡意程式偷帳密）← what-is-phishing [S02]
- 公司常見變形：商業電子郵件詐騙（BEC），冒充同事或廠商騙匯款 ← what-is-phishing [S02]

## 5. 真實故事：Omar 被釣了
- 收到假網購通知：付款失敗，要立刻登入確認 ← what-is-phishing [S01]
- 趕時間點了連結，在假網站登入，密碼和信用卡被盜 ← what-is-phishing [S01]
- 他漏看的兩個徵兆：要求「立刻」處理、寄件地址不是賣家正式網域 ← red-flags [S01]
- 提問：如果是你，會在哪一步停下來？[教學]

## 6. 就發生在台灣：假冒稅務單位
- 2026 年初，駭客假冒稅務稽查、報稅軟體、電子發票通知寄出釣魚信 ← case-taiwan-tax-phishing [S05]
- 附件是壓縮檔，裡面放正常的誘餌文件和惡意捷徑檔 ← case-taiwan-tax-phishing [S05]
- 用 taxfnat[.]tw 這種像官方的網域；信中顯示財政部網址，實際卻連到陌生網域 ← case-taiwan-tax-phishing [S05]
- 中招後惡意程式會關掉防毒軟體，讓駭客遠端控制電腦 ← case-taiwan-tax-phishing [S05]

## 7. 檢查點一：語氣與要求
- 急迫或情緒化：「不立刻處理就會有嚴重後果」← red-flags [S01]
- 索取帳密、信用卡等個人或財務資料 ← red-flags [S01]
- 兩段式釣魚：第一封是正常的商業詢問，你回信後下一封才附釣魚連結 ← red-flags [S02]
- AI 寫的釣魚信可能完全沒有錯字，不能再靠錯字判斷 ← red-flags [S01]

## 8. 檢查點二：寄件者
- 相似網域：只差幾個字母，例如 amazan.com ← sender-spoofing [S01]
- 詐騙者會在「寄件者顯示名稱」上動手腳，躲過郵件過濾 ← sender-spoofing [S02]
  - 顯示名稱和實際寄件 email 地址是兩個不同欄位 ← sender-spoofing [定義]
- Google 規定正當寄件者的顯示名稱不能放「URGENT REQUEST」這類主旨內容 ← sender-spoofing [S03]
- 不是真的回覆，主旨卻加 Re: 或 Fwd: —— Google 規定正當寄件者不能這樣做 ← red-flags [S03]

## 9. 檢查點三：連結與附件
- 顯示的連結文字不一定是真正目的地（台灣電子發票案例）← malicious-links-attachments [S05]
- 來源不明的短網址是常見徵兆 ← red-flags [S01]
- 附件可能是壓縮檔，裡面藏惡意捷徑檔 ← malicious-links-attachments [S05]
- 懷疑是釣魚時，連「取消訂閱」連結都不要點 ← malicious-links-attachments [S01]

## 10. 技術一點：郵件驗證 SPF、DKIM、DMARC
- SPF：網域公告「誰可以用我的網域寄信」← email-authentication [S03]
- DKIM：讓收件端確認「這封信真的是網域擁有者寄的」← email-authentication [S03]
- DMARC：告訴收件端，沒通過 SPF 或 DKIM 的信要怎麼處理 ← email-authentication [S03]
- 這些由寄件端在自己網域的網域服務商完成 ← email-authentication [S03]
- 2024 年起寄信到 Gmail 必須設定 SPF 或 DKIM；大量寄件者三者都要設 ← email-authentication [S03]

## 11. 實作：自己檢查一封信
- 最簡單：看寄件者旁有沒有問號 ← reading-email-headers [S07]
- Gmail App：查看詳細資料 → 查看安全性詳細資料，看「寄件者」和「簽署者」有沒有網域 ← reading-email-headers [S07]
- Gmail 網頁版：更多 →「顯示原始郵件」看完整標頭 ← reading-email-headers [S04]
- 進階：把標頭貼到 Google Admin Toolbox Messageheader 自動分析 ← reading-email-headers [S04]
- 未通過驗證不一定是詐騙，郵寄清單有時也會驗證失敗 ← reading-email-headers [S07]
- Google 提到垃圾郵件發送者也能讓信通過驗證 ← reading-email-headers [S07]
- 提問：看到「已驗證」就能完全放心嗎？想想前面看過的檢查點 [教學]

## 12. 收到可疑信怎麼辦？
- 辨識：對照三個檢查點 ← what-to-do [S01]
- 抗拒並回報：不點連結附件，用「回報垃圾郵件」功能 ← what-to-do [S01]
- 刪除：不回信、不點任何連結 ← what-to-do [S01]
- 覺得可能是真的？不要用信裡的連結和電話，自己搜尋官網、從官網找聯絡方式 ← what-to-do [S01]
- 事前防護：強密碼＋密碼管理器、開啟多因素驗證（MFA）、不拖延軟體更新 ← what-to-do [S01]

## 13. 小測驗（互動，點擊看答案）
- 題目只能考 Wiki 裡有的內容，每題答案標註出處 [教學]
- Q1 錯字很少的信就比較安全？→ 錯，AI 寫的信可能沒有錯字 ← red-flags [S01]
- Q2 信中顯示財政部網址就可以點？→ 錯，顯示的連結可能和實際不同 ← malicious-links-attachments [S05]
- Q3 寄件者旁出現問號代表什麼？→ 未通過驗證 ← reading-email-headers [S07]
- Q4 懷疑是釣魚，可以點「取消訂閱」嗎？→ 不行，任何連結都不要點 ← malicious-links-attachments [S01]
- 回到封面那封信：請指出它的問題 [教學]

## 14. 帶走這張檢查清單
- 停：語氣是不是在催你、要你的資料？[教學]
- 看：寄件者網域對不對？連結指向哪裡？附件是什麼？[教學]
- 查：Gmail 有沒有出現問號？[教學]
- 報：回報並刪除；要查證就自己找官網 [教學]

## 15. 參考來源與製作方式
- 列出 S01–S07 來源與連結 ← raw/sources.md
- 本簡報內容全部來自 LLM Wiki，連結到 GitHub repo 與 docs/workflow.md [教學]
