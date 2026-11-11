# S04 原始資料筆記：Google〈Trace an email with its full header〉

- 來源：Google Gmail 說明中心
- URL：https://support.google.com/mail/answer/29436?hl=en
- 擷取日期：2026-11-11
- 著作權：© Google。本檔只記錄操作步驟要點，原文請見連結。

## 擷取筆記
- 目的：查看收到郵件的完整標頭，可以知道信是從哪裡來的。
- Gmail（瀏覽器）：開啟郵件 → 點「回覆」旁的「更多」→「顯示原始郵件」（Show original）→ 新視窗顯示完整標頭 → 可按「複製到剪貼簿」。
- 分析標頭：把複製的標頭貼到 Google Admin Toolbox Messageheader（https://toolbox.googleapps.com/apps/messageheader/），按「Analyze the header above」。
- 檢查信件是否延遲：在「顯示原始郵件」視窗看「Created at」旁的時間。
- 其他郵件程式：Outlook（檔案 → 內容，看「網際網路標頭」）、Apple Mail（檢視 → 郵件 → 所有標頭）、Yahoo（更多 → 檢視原始郵件）等。
- **本頁沒有說明標頭中的驗證結果（SPF／DKIM／DMARC）要怎麼看。**
