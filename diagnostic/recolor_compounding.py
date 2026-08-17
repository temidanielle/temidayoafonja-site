#!/usr/bin/env python3
"""Recolor the Compounding state from orange/rust to the blue family, matching
the Field Kit. Page 2 only, colour-only, via targeted content-stream operator
replacement (no covering rectangles, no text reflow):

  - Matrix Compounding quadrant fill : rust  -> light blue #C7D9E8
  - Matrix Compounding quadrant frame : rust  -> navy   #0F2347 (matches others)
  - Matrix "Compounding" label        : white -> navy   #0F2347 (legible on blue)
  - Legend "Compounding." key text     : rust  -> mid-blue #2C5282
  - Legend Compounding left bar        : rust  -> mid-blue #2C5282

Every other rust element (brand mark, statement numbers, the other three states'
keys/bars, gold accents) and all text, fields, and positions are untouched.

Usage: python3 recolor_compounding.py in.pdf out.pdf
"""
import sys, re, fitz

MID   = ".172549 .321569 .509804"   # #2C5282
LIGHT = ".780392 .85098 .909804"    # #C7D9E8
NAVY  = ".058824 .137255 .278431"   # #0F2347
RUST  = r"\.756863 \.266667 \.054902 rg"

def recolor(src, out):
    d = fitz.open(src)
    pg = d[1]                                   # page 2 (Scoring and Placement)
    pg.clean_contents()
    cxref = int(d.xref_get_key(pg.xref, "Contents")[1].split()[0])
    cs = d.xref_stream(cxref).decode("latin-1")

    def sub(pat, repl, label):
        nonlocal cs
        cs, n = re.subn(pat, repl, cs, count=1)
        assert n == 1, f"{label}: expected 1 replacement, got {n}"

    sub(RUST + r"(\s+402 795\.2)", MID + r" rg\1", "legend bar")
    sub(RUST + r"(\s+BT/\w+ 11\.46582 Tf 1 0 0 -1 414 807)", MID + r" rg\1", "legend key")
    sub(RUST + r"(\s+594\.6667 613\.6667 117\.33331 66\.66669 re W n)", LIGHT + r" rg\1", "quadrant fill")
    sub(RUST + r"(\s+596 615 114)", NAVY + r" rg\1", "quadrant frame")
    sub(r"1 1 1 rg( BT/FGLLIQ 16 Tf 1 0 0 -1 607\.78109 652\.0962)", NAVY + r" rg\1", "matrix label")

    d.update_stream(cxref, cs.encode("latin-1"))
    d.save(out, deflate=True, garbage=0)
    print("wrote", out)

if __name__ == "__main__":
    recolor(sys.argv[1], sys.argv[2])
