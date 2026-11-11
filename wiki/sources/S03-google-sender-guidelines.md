# S03 Google〈Email sender guidelines〉

- 來源：Google Gmail 說明中心，https://support.google.com/mail/answer/81126?hl=en
- 類型：官方文件（寫給寄件者的規範）
- 可信度備註：一手來源；未標示更新日，擷取於 2026-11-11；內容是 Gmail 的規定，不一定適用其他郵件服務
- 原始資料：`raw/S03-google-sender-guidelines.md`（著作權資料，只存筆記）

## 重點摘要
- 2024 年 2 月起，寄信到個人 Gmail 的所有寄件者都必須設定 SPF 或 DKIM [S03]。
- 每天寄超過 5,000 封的大量寄件者，必須同時設定 SPF、DKIM 和 DMARC [S03]。
- SPF 用來阻止別人冒用你的網域寄出未授權郵件 [S03]。
- DKIM 讓收件端確認「這封信真的是網域擁有者寄的」[S03]。
- DMARC 告訴收件端：沒通過 SPF 或 DKIM 的郵件要怎麼處理 [S03]。
- 要通過 DMARC，驗證用的網域必須和 From: 欄位顯示的網域一致 [S03]。
- 經過驗證的郵件有助保護收件者不受偽冒與釣魚郵件影響 [S03]。
- Google 要求正當寄件者的顯示名稱只能用來表明身分，不能放「URGENT REQUEST」這類主旨內容，也不能用 emoji 假裝已驗證 [S03]。
- 未經允許冒用其他網域或寄件者稱為偽冒（spoofing）[S03]。

## 對應概念頁
- [[email-authentication]]：SPF、DKIM、DMARC
- [[sender-spoofing]]：偽冒的定義、顯示名稱規範
- [[red-flags]]：正當寄件者不會做的事
