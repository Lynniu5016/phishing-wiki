#!/usr/bin/env python3
"""大綱檢查：每個事實句的 Wiki 頁面存在，且該頁面真的引用了標註的來源。"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
outline = (ROOT / "slides/outline.md").read_text(encoding="utf-8").splitlines()
REF = re.compile(r"← ([a-z0-9-]+) \[(S\d{2}|定義)\]")
problems, facts, teach = [], 0, 0
weak = []
def grams(x):
    x = re.sub(r"←.*", "", x)
    x = re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]", "", x)
    return {x[i:i+2] for i in range(len(x)-1)}
start = outline.index("---") + 1 if "---" in outline else 0
for n, line in enumerate(outline, 1):
    s = line.strip()
    if n <= start or not s.startswith("- "): continue
    if "[教學]" in s:
        teach += 1
        if REF.search(s): problems.append(f"{n}: [教學] 句不應帶事實出處")
        continue
    if "← raw/sources.md" in s: continue
    m = REF.search(s)
    if not m:
        problems.append(f"{n}: 沒有標 Wiki 出處：{s[:40]}"); continue
    facts += 1
    page, src = m.groups()
    p = ROOT / "wiki/concepts" / f"{page}.md"
    if not p.exists():
        problems.append(f"{n}: 頁面不存在 {page}")
    elif f"[{src}]" not in p.read_text(encoding="utf-8"):
        problems.append(f"{n}: {page} 頁面裡沒有引用 [{src}]")
    else:
        g = grams(s)
        best = max((len(g & grams(l)) / max(len(g),1) for l in p.read_text(encoding="utf-8").splitlines() if f"[{src}]" in l), default=0)
        if best < 0.3:
            weak.append(f"{n}: 與 {page} 中標 [{src}] 的句子相似度低（{best:.0%}），請人工確認：{s[:30]}")
print(f"事實句 {facts}、教學句 {teach}")
if weak:
    print(f"相似度警告 {len(weak)} 個："); [print(" ?", w) for w in weak]
if problems:
    print(f"發現 {len(problems)} 個問題："); [print(" -", x) for x in problems]; sys.exit(1)
print("大綱可追溯性檢查通過 ✅")
