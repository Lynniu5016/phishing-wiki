# S05 Fortinet〈Massive Winos 4.0 Campaigns Target Taiwan〉

- 來源：Fortinet FortiGuard Labs，Cara Lin，2026-02-20，https://www.fortinet.com/blog/threat-research/massive-winos-40-campaigns-target-taiwan
- 類型：業界研究（一手技術分析）
- 可信度備註：一手來源；內容偏技術，Wiki 只取一般人看得懂的部分
- 原始資料：`raw/S05-fortinet-winos-taiwan-2026.md`

## 重點摘要
- 2026 年初，有駭客鎖定台灣發動多起釣魚行動，誘餌模仿稅務稽查通知、報稅軟體和電子發票 [S05]。
- 其中一種是附上 RAR 壓縮檔，裡面放一份正常的誘餌文件和一個惡意捷徑檔 [S05]。
- 攻擊者用 taxfnat[.]tw 這種看起來像官方的網域來假冒財政部 [S05]。
- 有封電子發票郵件「顯示」的連結是財政部電子發票網址，實際卻連到另一個陌生網域 [S05]。
- 惡意程式會關掉電腦上的防毒軟體，例如 Microsoft Defender，以便長期遠端控制 [S05]。
- 攻擊者會輪替使用不同網域，Fortinet 認為光靠封鎖固定網域不夠 [S05]。
- Fortinet 建議：來自非信任來源的文件或連結都要極度小心 [S05]。

## 對應概念頁
- [[case-taiwan-tax-phishing]]：完整案例
- [[malicious-links-attachments]]：顯示連結與實際連結不同、壓縮檔裡的捷徑檔
- [[sender-spoofing]]：仿冒官方網域
- [[red-flags]]：連結文字不可信
