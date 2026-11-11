# S05 原始資料筆記：Fortinet FortiGuard Labs〈Massive Winos 4.0 Campaigns Target Taiwan〉

- 來源：Fortinet FortiGuard Labs，作者 Cara Lin，發布日期 2026-02-20
- URL：https://www.fortinet.com/blog/threat-research/massive-winos-40-campaigns-target-taiwan
- 擷取日期：2026-11-11
- 著作權：© Fortinet。本檔只記錄事實要點，原文請見連結。惡意網址一律依原文以 [.] 去活化。

## 擷取筆記
- FortiGuard Labs 觀察到多起鎖定台灣的釣魚行動，主題刻意利用在地業務流程，散布惡意程式 Winos 4.0（ValleyRat），手法是夾帶惡意附件或內嵌連結。
- 誘餌模仿官方通知：稅務稽查通知、報稅軟體安裝檔、雲端電子發票下載。
- 攻擊者輪替使用多個網域和雲端服務，Fortinet 認為只靠封鎖固定網域不足以作為主要防禦。
- 行動 1（稅務主題）：RAR 壓縮檔「taxIs_RX3001.rar」，內含一份無害的誘餌文件和一個惡意捷徑檔（LNK）；執行後會下載下一階段惡意程式。
- 行動 2（稅務／電子發票主題）：假冒財政部文件；使用 taxfnat[.]tw 偽裝成台灣官方網域，實際把受害者導向中國的雲端空間下載「E-Invoice.rar」。
- 另一種變體：電子發票郵件中「顯示」的連結是 www.einvoice.nat.gov[.]tw，但實際連到 njhwuyklw[.]com。
- 另有一起行動使用名為「綜合所得稅電子結算申報繳稅.exe」的合法檔案做 DLL 側載。
- 最終惡意程式會關閉大量資安產品的程序（包含 Microsoft Defender、趨勢科技等），以便長期遠端控制電腦。
- 結論：此攻擊者擅長設計在地化的釣魚誘餌，常註冊看起來和該國相關的網域，提高稅務與公文誘餌的可信度；來自非信任來源的文件或連結都要極度小心。
