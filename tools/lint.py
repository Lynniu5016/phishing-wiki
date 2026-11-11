#!/usr/bin/env python3
"""Wiki lint：依 AGENTS.md 第 5 節自動檢查。用法：python3 tools/lint.py"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CONCEPTS = WIKI / "concepts"
SOURCES = WIKI / "sources"
SKIP_SECTIONS = {"來源", "相關概念", "對應概念頁"}
CITE = re.compile(r"\[S\d{2}\]")
DEF = re.compile(r"\[定義\]")
defs = []
LINK = re.compile(r"\[\[([a-z0-9-]+)\]\]")

problems = []
concept_names = {p.stem for p in CONCEPTS.glob("*.md")}
source_ids = {p.stem[:3] for p in SOURCES.glob("S*.md")}
index_text = (WIKI / "index.md").read_text(encoding="utf-8")
linked = set()
planned = set(re.findall(r"⬜ `([a-z0-9-]+)`", index_text))
warnings = []

def check_page(path, require_cite):
    section = ""
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if s.startswith("#"):
            section = s.lstrip("#").strip(); continue
        if s.startswith("- 來源：") or s.startswith("- 類型：") or s.startswith("- 可信度") or s.startswith("- 原始資料："):
            continue
        for m in LINK.findall(s):
            linked.add(m)
            if m not in concept_names and m in planned:
                warnings.append(f"{path.relative_to(ROOT)}:{n} 連到規劃中、尚未建立的頁面 [[{m}]]")
            elif m not in concept_names:
                problems.append(f"{path.relative_to(ROOT)}:{n} 連結到不存在的頁面 [[{m}]]")
        for c in CITE.findall(s):
            if c[1:4] not in source_ids:
                problems.append(f"{path.relative_to(ROOT)}:{n} 引用不存在的來源 {c}")
        if require_cite and s and section not in SKIP_SECTIONS and not s.startswith(">"):
            if DEF.search(s):
                defs.append(f"{path.relative_to(ROOT)}:{n} {s[:50]}")
            elif not CITE.search(s):
                problems.append(f"{path.relative_to(ROOT)}:{n} 未標來源：{s[:40]}")

for p in sorted(CONCEPTS.glob("*.md")):
    check_page(p, True)
    if p.stem not in index_text:
        problems.append(f"{p.relative_to(ROOT)} 未列在 index.md")
for p in sorted(SOURCES.glob("S*.md")):
    check_page(p, True)
    if p.stem not in index_text:
        problems.append(f"{p.relative_to(ROOT)} 未列在 index.md")
for name in concept_names - linked:
    problems.append(f"wiki/concepts/{name}.md 是孤兒頁（沒有其他頁面連到）")

print(f"檢查頁面：概念 {len(concept_names)}、來源 {len(source_ids)}")
if defs:
    print(f"[定義] 共 {len(defs)} 處，請人工確認只用於術語解釋：")
    for d in defs: print(" ?", d)
if warnings:
    print(f"警告 {len(warnings)} 個（規劃中頁面，建立後自動消失）：")
    for w in warnings: print(" !", w)
if problems:
    print(f"發現 {len(problems)} 個問題：")
    for x in problems: print(" -", x)
    sys.exit(1)
print("全部通過 ✅")
