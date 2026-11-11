# Wiki 操作紀錄

## 2026-11-11｜討論｜確定主題、受眾與範圍
- 動作：與 LLM 討論（先討論、後生成）
- 決定：
  - 主題：釣魚郵件怎麼辨識？
  - 受眾：大學生／上班族（會用 email，不懂技術）
  - 深度：實用為主＋基礎技術（SPF／DKIM／DMARC、看標頭）
  - 來源偏好：官方＋業界報告
  - 平台：GitHub repo（Markdown），簡報以 GitHub Pages 發布
- 異動頁面：無（尚未生成）

## 2026-11-11｜來源選擇｜初選 6 篇
- 動作：LLM 搜尋並提出 6 篇候選來源，各自對應簡報區塊
- 初選：CISA、APWG Q2 2026、Google sender guidelines、Google 標頭說明、iThome 報導（TWCERT／假冒查稅）、Verizon DBIR（二手摘要）

## 2026-11-11｜來源檢查｜替換 2 篇非一手來源
- 動作：使用者要求重新檢查來源品質
- 檢查標準：是否為一手來源、是否符合「官方＋業界」偏好、是否夠新
- 發現問題：
  - 第 5 篇為新聞媒體轉述，非一手 → 改為 Fortinet FortiGuard Labs 原始研究（2026-02，台灣稅務／電子發票主題釣魚）
  - 第 6 篇原本引用二手摘要 → 改為 Verizon DBIR 官方頁面
  - TWCERT 官網未找到對應的單篇一手公告，暫不採用
- 異動頁面：`raw/sources.md`
- 心得：來源品質問題在 ingest 前就攔下，成本最低

## 2026-11-11｜建立｜repo 骨架
- 動作：建立 `AGENTS.md`（Wiki 規則）、`raw/sources.md`、`wiki/index.md`、`wiki/log.md`、`docs/workflow.md`
- 待辦：依序 ingest S01–S06

## 2026-11-11｜Ingest｜S01 CISA〈Recognize and Report Phishing〉
- 動作：擷取 CISA 原文存入 raw/（美國聯邦政府著作，公有領域）→ 建立來源摘要頁 → 建立 5 個概念頁 → 更新 index
- 異動頁面：
  - 新增 `raw/S01-cisa-recognize-report-phishing.md`
  - 新增 `wiki/sources/S01-cisa-recognize-report.md`
  - 新增 `wiki/concepts/` what-is-phishing、red-flags、sender-spoofing、malicious-links-attachments、what-to-do
  - 更新 `wiki/index.md`、`raw/sources.md`
- 新增工具：`tools/lint.py`，把 AGENTS.md 可自動化的規則寫成程式（未標來源、來源編號不存在、連結目標不存在、未列入 index、孤兒頁）

## 2026-11-11｜Lint｜S01 後第 1 次（自動檢查通過，人工檢查未通過）
- `tools/lint.py`：0 個問題
- 人工逐句對照 raw/ 原文，發現 2 處**標錯來源**：
  - red-flags：「短網址＝把長網址縮成一小段……」標成 `[S01]`，但 CISA 原文沒有這個定義，是 LLM 自己補的
  - sender-spoofing：「相似網域＝只差幾個字母的假網址」同樣標成 `[S01]`，原文只有 amazan.com 例子，沒有這個術語
- 根本原因：AGENTS.md 規則 2「只能用來源內容」和規則 4「術語要有白話定義」衝突，來源沒給定義時 LLM 就自己寫，並順手標上來源
- 自動 lint 的盲點：只能檢查「有沒有標來源」，無法檢查「標的來源有沒有真的這樣說」
- 修正：
  - **修改 AGENTS.md 規則 4**：新增 `[定義]` 標記，只限一句話的術語解釋，不得用於例子、數字或主張
  - **修改 tools/lint.py**：把所有 `[定義]` 列出，強制人工確認
  - 兩處定義改標 `[定義]`，與來源事實拆成不同行

## 2026-11-11｜Lint｜S01 後第 2 次（通過）
- `tools/lint.py`：0 個問題；`[定義]` 2 處，人工確認皆為術語解釋 ✅
- 人工對照：其餘句子皆可在 raw/S01 找到依據 ✅
- 觀察：LLM 最容易在「術語定義」和「舉例」時加入來源沒有的內容，之後 ingest 這兩類句子要優先人工對照

## 2026-11-11｜決策｜raw/ 的著作權處理
- 問題：S02–S06 都是有著作權的資料，repo 是公開的，不能整篇複製原文
- 決定：公有領域資料（S01）存正文；其他來源只存「事實與數字筆記＋頁碼＋原文連結」
- 異動頁面：`AGENTS.md` 目錄結構說明

## 2026-11-11｜Ingest｜S02 APWG 2026 Q2
- 異動頁面：新增 `wiki/sources/S02-apwg-q2-2026.md`、`wiki/concepts/phishing-trends.md`；更新 what-is-phishing、red-flags、sender-spoofing
- 擷取時發現：報告內文與圖表有 2 處數字不一致（禮物卡 54%／55%、社群詐騙 22.7%／22.8%）→ 依規則 6 兩者並列

## 2026-11-11｜Lint｜S02 後（自動通過，人工 3 處修正）
- `tools/lint.py`：0 個問題，`[定義]` 3 處
- 人工對照發現：
  1. red-flags：「所以第一封信沒有連結不代表安全」標 `[S02]`，但 APWG 沒這樣寫，是 LLM 從「兩段式釣魚」**自行推論** → 刪除
  2. sender-spoofing：顯示名稱的 `[定義]` 寫了「寄件者可以自己隨便填」，這是**主張不是定義**，違反 `[定義]` 用途限制 → 改成純定義
  3. phishing-trends：「實際數量可能比回報的多」比原文說得更強（原文只說「可能影響回報數量」）→ 改回原文強度
- 修正後重跑：通過

## 2026-11-11｜Ingest｜S03 Google 寄件者規範
- 異動頁面：新增 `wiki/sources/S03-google-sender-guidelines.md`、`wiki/concepts/email-authentication.md`；更新 sender-spoofing、red-flags

## 2026-11-11｜Lint｜S03 後第 1 次（未通過）
- `tools/lint.py`：2 個問題——email-authentication 連到尚未建立的 `[[reading-email-headers]]`
- 人工對照另發現 1 處：「收件者不用設定，但可以查看結果」標 `[S03]`，但 S03 是寫給寄件者的文件，沒有提到收件者 → 刪除，改由後續來源支持
- **修改 tools/lint.py**：連到 index 中「⬜ 規劃中」的頁面改為警告（頁面建立後自動消失），連到完全不存在的頁面仍是錯誤
- 原因：ingest 是一篇一篇做的，頁面之間互相引用時一定會先連到還沒建的頁面，原本的規則會讓每篇都卡住

## 2026-11-11｜Lint｜S03 後第 2 次（通過，1 個警告）

## 2026-11-11｜Ingest｜S04 Google 查看完整標頭
- 異動頁面：新增 `wiki/sources/S04-google-trace-header.md`
- **發現缺口**：S04 只教怎麼打開標頭，沒說明驗證結果要怎麼看，但簡報規劃需要「看驗證結果」這一段
- 處理：**回到「選來源」步驟**，從 S04 頁面的相關文章找到 Google〈Check if your Gmail message is authenticated〉，新增為 S07
- 異動頁面：`raw/sources.md` 新增 S07

## 2026-11-11｜Ingest｜S07 Google 檢查郵件是否通過驗證（補充來源）
- 異動頁面：新增 `wiki/sources/S07-google-check-authenticated.md`、`wiki/concepts/reading-email-headers.md`；更新 email-authentication、red-flags
- reading-email-headers 建立後，S03 留下的警告自動消失

## 2026-11-11｜Lint｜S04＋S07 後（自動通過，人工 2 處修正）
- `tools/lint.py`：0 個問題，`[定義]` 5 處
- 人工對照發現：
  1. **脫離原文脈絡**：S07 說「垃圾郵件發送者也能通過驗證」，原文出現在寫給寄件者、談「送達率」的段落；LLM 把它改寫成「通過驗證不等於安全」，變成原文沒有的結論 → 改成如實陳述，並註明原文脈絡（email-authentication、reading-email-headers、S07 摘要頁共 3 處）
  2. 郵件標頭的 `[定義]` 多了「平常收件匣不會顯示」這個主張 → 刪除
- 修正後重跑：通過

## 2026-11-11｜Ingest｜S05 Fortinet 台灣稅務主題釣魚（2026-02）
- 擷取過程：文章網址一開始無法直接抓取，經由 Fortinet 另一篇相關文章的連結取得原文
- 異動頁面：新增 `wiki/sources/S05-fortinet-winos-taiwan-2026.md`、`wiki/concepts/case-taiwan-tax-phishing.md`；更新 malicious-links-attachments、sender-spoofing、red-flags
- 惡意網域一律保留原文的 `[.]` 去活化寫法

## 2026-11-11｜Lint｜S05 後（自動通過，人工 2 處修正）
- `tools/lint.py`：0 個問題，`[定義]` 6 處
- 人工對照發現 2 處 LLM **加油添醋**：「降低戒心」（原文沒有）、「在背景下載」（原文沒有「背景」）→ 刪除
- 修正後重跑：通過

## 2026-11-11｜Ingest｜S06 Verizon DBIR 2026
- 來源調整：官方頁面只有摘要數字，「釣魚占 16%」這個數字原本只在二手報導看到 → 改抓官方**執行摘要 PDF**，確認 16% 出自一手來源
- 異動頁面：新增 `wiki/sources/S06-verizon-dbir-2026.md`；更新 phishing-trends（新增「來源之間的差異」段）、what-is-phishing
- 擷取時發現 2 處官方文件自相矛盾 → 依規則 6 並列：
  - 資料期間：執行摘要寫 2024-10～2025-11，官網寫 2024-11-01～2025-10-31
  - 社交工程占比：內文 16%，圖表 17%
- **刻意不採用**：區域資料（APAC 與台灣較相關），但 PDF 轉文字後兩個區塊的數字無法確定對應哪一區，寧可不用

## 2026-11-11｜Lint｜S06 後（通過）
- `tools/lint.py`：0 個問題，`[定義]` 6 處，人工確認皆為術語解釋
- 人工對照：無新增問題

## 2026-11-11｜整合｜跨來源更新 what-to-do
- 把 S05（稅務類誘餌建議）、S07（問號警示處理）補進 what-to-do
- 總 lint：概念頁 9、來源 7，全部通過；規劃中頁面全部建立完成

## 階段小結：ingest 階段的錯誤統計
| 錯誤類型 | 次數 | 自動 lint 抓得到？ |
|---|---|---|
| 來源沒說、LLM 自己補的定義或推論 | 4（S01×2、S02、S03） | ✗ |
| `[定義]` 裡夾帶主張 | 2（S02、S04） | ✗ |
| 說得比原文強、脫離原文脈絡 | 2（S02、S07） | ✗ |
| 加油添醋的形容 | 2（S05） | ✗ |
| 連到尚未建立的頁面 | 1（S03） | ✓ |
| 來源缺口（需要回頭補來源） | 1（S04→S07） | ✗ |
- 觀察：10 個內容錯誤全部發生在「把來源改寫成 Wiki 句子」這一步，而且自動 lint 一個都抓不到，全靠人工逐句對照原文

## 2026-11-11｜Query｜產生簡報大綱 `slides/outline.md`
- 動作：依受眾與 Wiki 內容排出 16 張投影片，每個事實句標註來自哪個概念頁與來源
- 新增工具：`tools/check_outline.py`，檢查每個事實句的概念頁存在、且該頁真的引用了標註的來源
- **檢查往前移**：在生成 HTML 之前就檢查大綱可追溯性，而不是等 HTML 做完才檢查

## 2026-11-11｜大綱檢查｜第 1 次（自動通過，人工 5 處問題）
- `check_outline.py`：事實句 49、教學句 7，全部通過
- 人工對照發現 5 處問題：
  1. 投影片 7：「顯示名稱和寄件地址是不同欄位」其實是 `[定義]`，卻標成 `[S02]`；腳本只檢查「整頁有沒有 [S02]」，所以沒抓到
  2. 投影片 10：「收件者只需要看結果」標成 `[教學]`——這正是 S03 lint 時從 Wiki 刪掉的無來源主張，**換個標籤又溜進大綱**
  3. 投影片 12：「驗證結果要搭配徵兆一起看」標成 `[教學]`——也是 S07 lint 時刪掉的推論，同樣用 `[教學]` 溜回來
  4. 投影片 13：「打電話查證」比 Wiki 說得多（Wiki 是「從官網找聯絡方式」）
  5. 投影片 15 Q4：「取消訂閱」標到 what-to-do，但那一頁沒有這句，應該是 malicious-links-attachments
- 發現的漏洞：
  - 腳本只做「頁面層級」檢查，無法確認句子內容真的在那一頁
  - `[教學]` 標籤成了新的漏洞：LLM 會把無來源的結論包裝成「教學用語」

## 2026-11-11｜修改檢查流程｜大綱檢查加強
- **修改 tools/check_outline.py**：加上句子相似度比對，跟概念頁中同來源句子的字詞重疊太低就發出警告
  - 試跑結果：4 個警告中 2 個是真問題（第 4、5 項）、2 個是誤報（摘要式改寫）；第 1–3 項仍抓不到
- **修改 AGENTS.md**：新增「簡報大綱」規則，`[教學]` 只能是問句、指示或結構性文字，不得包含事實主張
- 修正：5 處全部修改（第 3 項改成提問句「看到已驗證就能完全放心嗎？」）

## 2026-11-11｜大綱檢查｜第 2 次（通過）
- `check_outline.py`：事實句 51、教學句 6；相似度警告 2 個，人工確認皆為誤報（摘要式改寫，內容正確）
- 待使用者確認大綱後產生 HTML

## 2026-11-11｜大綱優化｜對照作業要求修改為 v2（v1 備份未保留於 repo，差異如下）
- 對照評分標準 9–10 分的要求逐項檢查：
  - 「Wiki 與簡報有明確對應」→ v1 的對應只寫在 outline.md，觀眾看不到 → **v2 每張投影片底部顯示「出處」，直接連到 GitHub 上的 Wiki 頁面**
  - 「清楚的教學結構」→ v1 缺少學習目標，結尾和開頭沒有呼應 → **v2 新增「學完你會知道」，測驗最後一題回到封面那封信**
  - 對初學者的負擔 → v1 有 16 張且徵兆分散在 4 張 → **v2 整併為 15 張**：兩段式釣魚併入檢查點一、Re:/Fwd: 併入檢查點二、驗證結果解讀併入實作、事前防護併入「怎麼辦」；三個檢查點對應目標 2
  - 新增 `[示意]` 標記：重繪的示意郵件畫面，內容必須來自標註的 Wiki 頁面，並在畫面上註明是示意
  - 新增「參考來源與製作方式」頁，連到 Wiki 與 workflow.md
- `check_outline.py` 修正：原本從第 6 行開始檢查，會誤判 v2 的說明區 → 改為從 `---` 之後開始
- 檢查結果：事實句 48、教學句 14，通過；相似度警告 2 個，與 v1 相同，人工確認為誤報

## 2026-11-11｜生成｜HTML 簡報 `slides/index.html`
- 依 outline v2 生成 15 張投影片：鍵盤左右鍵、按鈕、手機左右滑動切換；網址 `#s1`～`#s15` 可直接連到某一張；測驗可點擊看答案；支援深色模式
- 新增工具：`tools/check_slides.py`，檢查每張投影片的出處標記都對得上 Wiki

## 2026-11-11｜HTML 檢查｜第 1 次
- `check_slides.py`：出處對照通過
- 人工比對 HTML 與大綱：**發現 1 處 LLM 在生成時自己加字**——BEC 的說明寫成「冒充同事、**主管**或廠商」，大綱和 Wiki 都只有「同事（員工）或廠商」→ 刪除「主管」
- 瀏覽器檢查（Playwright，桌機 1280×760、手機 390×780）：JavaScript 錯誤 0、沒有水平捲動；封面標題在桌機斷行不自然（「辨／識？」）→ 標題加上 `text-wrap: balance`
- 說明：檢查環境沒有網路，截圖使用系統備用字型；GitHub Pages 上會載入 Noto Sans TC／Noto Serif TC

## 2026-11-11｜HTML 檢查｜第 2 次（通過）
- `check_slides.py` 通過；人工比對無其他落差；版面修正後重新截圖確認
- **修改 workflow**：流程圖新增「HTML 出處對照」節點，以及 ingest 發現缺口時回到「選來源」的虛線

## 2026-11-11｜文件｜完成 docs/workflow.md 與 docs/submission.md
- workflow.md：補上流程說明表、會重複執行的步驟、檢查點、設計理由、執行紀錄摘要與錯誤統計；反思段落列出證據，結論由使用者撰寫
- submission.md：依繳交格式整理 6 項內容（學號、系級待填）

## 2026-11-11｜發布｜GitHub Pages 設定
- 問題：使用者回報 GitHub Pages 無法正常顯示簡報
- 處理：新增根目錄 `index.html`（自動導向 `slides/`）與 `.nojekyll`（讓 GitHub Pages 直接提供靜態檔案，不經 Jekyll 處理）
- 發布設定：Settings → Pages → Deploy from a branch → `main`／`/(root)`

## 2026-11-11｜文件｜反思定稿
- 使用者完成反思文字，更新至 `docs/workflow.md` 與 `docs/submission.md` 第 6 項
