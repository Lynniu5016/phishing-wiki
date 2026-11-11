# 釣魚郵件怎麼辨識？— LLM Wiki

以「先討論、後生成」方式建立的 LLM Wiki，並以此為唯一知識來源產生教學 HTML 簡報。

- 目標觀眾：大學生／上班族（會用 email，不懂技術）
- 內容深度：實用為主，搭配基礎技術（SPF／DKIM／DMARC、郵件標頭）
- 使用的 LLM：Claude（負責搜尋來源、ingest、撰寫 Wiki 與簡報；每一步的檢查結果記錄在 `wiki/log.md`）

| 目錄 | 內容 |
|---|---|
| `AGENTS.md` | Wiki 規則（給 LLM 讀的 schema） |
| `raw/` | 原始資料清單與存檔 |
| `wiki/` | LLM 維護的 Wiki 頁面（index、log、sources、concepts） |
| `slides/` | 教學 HTML 簡報與大綱（GitHub Pages） |
| `index.html` | GitHub Pages 首頁，自動導向簡報 |
| `docs/workflow.md` | loop／graph 設計、執行紀錄、反思 |
| `docs/submission.md` | 繳交內容整理 |
| `tools/` | lint.py、check_outline.py、check_slides.py |

簡報：https://lynniu5016.github.io/phishing-wiki/slides/
