#!/usr/bin/env python3
"""Regenerate the master manuscript from the shipping handbook PDF so the words
always match the product. Usage: python3 gen_manuscript.py <handbook.pdf> <out.md> <buildtime>"""
import sys, re, fitz

PDF, OUT, BT = sys.argv[1], sys.argv[2], sys.argv[3]
d = fitz.open(PDF)

def clean(t):
    lines = [ln.rstrip() for ln in t.splitlines()]
    out = []
    for ln in lines:
        # drop the running footer line (title / url / page number)
        if re.match(r"^Keep the Proof\s*$", ln): continue
        if ln.strip() == "temidayoafonja.com": continue
        if re.match(r"^\d+$", ln.strip()): continue
        out.append(ln)
    # collapse blank runs
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip()
    return txt

parts = []
parts.append("# KEEP THE PROOF - Master Manuscript\n")
parts.append("**How to Track Your Work Accomplishments Before You Need a Resume**  ")
parts.append("**A 60-Minute Career Evidence System**\n")
parts.append(f"Version 1.0.1 - Revised {BT} CT (America/Chicago)  ")
parts.append("Author: Temidayo Afonja, Founder and Principal, The Density Group  ")
parts.append("Primary URL: temidayoafonja.com\n")
parts.append("This manuscript is the full reading copy of the shipping handbook, extracted from the "
             "final PDF so the words match the product exactly. A section-to-page map follows at the end.\n")
parts.append("---\n")

page_map = []
for i in range(d.page_count):
    n = i + 1
    txt = clean(d[i].get_text())
    if n == 1:
        parts.append(f"## [Page {n}] - Cover\n")
        page_map.append((n, "COVER", "Keep the Proof"))
        continue
    parts.append(f"## [Page {n}]\n")
    parts.append(txt + "\n")
    # map: first line = eyebrow/kicker, second meaningful = title
    ls = [l for l in txt.splitlines() if l.strip()]
    ey = ls[0].strip() if ls else ""
    title = ls[1].strip() if len(ls) > 1 else ""
    page_map.append((n, ey.upper()[:40], title[:52]))

parts.append("---\n")
parts.append("## Section-to-page map\n")
parts.append("| Page | Section | Title / first line |")
parts.append("| --- | --- | --- |")
for n, sec, title in page_map:
    parts.append(f"| {n} | {sec} | {title} |")

open(OUT, "w").write("\n".join(parts) + "\n")
print("wrote", OUT, "-", d.page_count, "pages")
