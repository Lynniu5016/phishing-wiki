# S07 Google〈Check if your Gmail message is authenticated〉

- 來源：Google Gmail 說明中心，https://support.google.com/mail/answer/180707?hl=en
- 類型：官方文件（給收件者）
- 可信度備註：一手來源；擷取於 2026-11-11；因 S04 有缺口而補入
- 原始資料：`raw/S07-google-check-authenticated.md`

## 重點摘要
- 寄件者名稱旁出現問號，代表這封信沒有通過驗證，Gmail 不確定它是否真的來自顯示的寄件者 [S07]。
- 看到問號時，回信或下載附件都要小心 [S07]。
- 未通過驗證不一定是垃圾郵件，例如郵寄清單這類大量寄送的正當郵件有時會驗證失敗 [S07]。
- 在 Gmail App 的「安全性詳細資料」看到「寄件者」（Mailed by）和「簽署者」（Signed by）都有網域，就代表已驗證 [S07]。
- SPF 指定哪些主機可以用某個網域寄信；DKIM 讓寄件者對郵件做電子簽章，收件者可以驗證 [S07]。
- Google 在寫給寄件者的段落提到，垃圾郵件發送者同樣能讓郵件通過驗證 [S07]。

## 對應概念頁
- [[reading-email-headers]]：怎麼看驗證結果
- [[email-authentication]]：SPF、DKIM 的補充說明、驗證的限制
- [[red-flags]]：寄件者旁的問號
