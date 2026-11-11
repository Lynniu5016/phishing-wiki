#!/usr/bin/env python3
"""HTML 簡報檢查：每張投影片 data-src 標的 Wiki 頁面存在，且該頁真的引用了該來源。"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
h = (ROOT / "slides/index.html").read_text(encoding="utf-8")
bad = []
srcs = re.findall(r'data-src="([^"]*)"', h)
for i, src in enumerate(srcs, 1):
    for r in filter(None, src.split(",")):
        page, s = r.split(":")
        p = ROOT / "wiki/concepts" / f"{page}.md"
        if not p.exists() or f"[{s}]" not in p.read_text(encoding="utf-8"):
            bad.append(f"第 {i} 張：{r}")
print(f"投影片 {len(srcs)} 張，出處標記 {sum(len([x for x in s.split(',') if x]) for s in srcs)} 個")
if bad: print("問題：", *bad, sep="\n - "); sys.exit(1)
print("出處對照通過 ✅")
