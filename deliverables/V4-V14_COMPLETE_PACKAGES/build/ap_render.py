# -*- coding: utf-8 -*-
"""Render V12, V13 and V14 cards from their approved card specification.

These three have no rendered artwork anywhere in the workspace. Their card
copy is fully specified and locked in the production modules: an id, a
headline, the copy lines and an on-card label. Rendering that specification is
production execution, not creative redesign, and no line of card copy is
changed here.

They are Watch-Me-Read videos, so the artifact is the structure. Every card is
a plain reading surface on the house palette: a headline, the copy lines, and
the label where one exists. Nothing is turned into a framework diagram.

The asset specification records these as NEW RENDERS FROM AN APPROVED
SPECIFICATION, which is a different provenance from the V4 to V11 assets that
are reused byte for byte.
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
for p in ("riverside-build", "VIDEOS_22-23/build", "V4-V11_SYNC/build"):
    sys.path.append(DELIV + p)
import rdeck
from rdeck import render_html, shoot
from PIL import Image
import svg23
from lay23 import lines as lay_lines, statement, watch_next, stamp, badge, _ground
from layouts import S, TH, BAND_TOP, BAND_BOT, compose
from rdeck import MARGIN, CW, block, rect, GOLD, DISPLAY, BODY
import ap_src as A

OUT = os.path.join(os.path.dirname(HERE), "_rendered")

def _split(line):
    """Card copy uses four spaces to separate a label from its value."""
    if "    " in line:
        a, b = line.split("    ", 1)
        return a.strip(), b.strip()
    return None, line.strip()

def draw(card, headline, copy, label):
    def _d(c):
        dark = True
        back, ink, dim = _ground(c, dark, headline)
        rows = []
        for ln in copy:
            lab, val = _split(ln)
            if lab:
                rows.append((lab, val))
            else:
                rows.append((None, val))
        if all(r[0] is None for r in rows):
            lay_lines(c, headline, None, [("", r[1]) for r in rows],
                      foot=label, dark=dark, size=44)
        else:
            lay_lines(c, headline, None,
                      [(r[0] or "", r[1]) for r in rows],
                      foot=label, dark=dark, size=40)
    return _d

def cards(n):
    out = []
    for cid, headline, copy, label in A._mod(n).FULLSCREEN[n]:
        if cid.endswith("WATCH_NEXT"):
            out.append((cid, (lambda t: (lambda c: watch_next(c, t)))(copy[0])))
        else:
            out.append((cid, draw(cid, headline, copy, label)))
    return out

def build(n):
    vis = os.path.join(OUT, "V%02d" % n)
    os.makedirs(vis, exist_ok=True)
    cs, names = [], []
    for cid, fn in cards(n):
        c = rdeck.Card(len(cs) + 1, cid + ".png")
        fn(c)
        cs.append(c)
        names.append(cid + ".png")
    html = render_html(cs, os.path.join(vis, "_f.html"), "V%d" % n)
    shoot(html, vis, names)
    os.remove(html)
    idx = {nm[:-4]: c for nm, c in zip(names, cs)}
    svgs = []
    for cid in list(idx)[:1] + [x for x in idx if x.endswith("WATCH_NEXT")]:
        p = os.path.join(vis, cid + ".svg")
        svg23.write(idx[cid], p)
        svgs.append(p)
    pngs = [os.path.join(vis, x) for x in names]
    sheet = os.path.join(vis, "Phone_Size_Contact_Sheet.png")
    contact(pngs, sheet)
    return pngs, svgs, sheet, cs

def contact(paths, path, cols=5, w=300):
    h_ = int(w * 1080 / 1920.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 12,
                           rows * h_ + (rows + 1) * 12), (236, 232, 224))
    for i, p in enumerate(paths):
        sh.paste(Image.open(p).convert("RGB").resize((w, h_), Image.LANCZOS),
                 (12 + (i % cols) * (w + 12), 12 + (i // cols) * (h_ + 12)))
    sh.save(path)
    return path

def copy_unchanged(n):
    """Every rendered card must carry its specified copy, unchanged."""
    bad = []
    for cid, headline, copy, label in A._mod(n).FULLSCREEN[n]:
        c = rdeck.Card(1, cid + ".png")
        dict(cards(n))[cid](c)
        got = []
        for el in c.els:
            if el.get("t") != "text":
                continue
            for pa in el.get("paras", []):
                if pa.get("text"):
                    got.append(pa["text"])
        blob = " ".join(got).lower()
        for ln in copy:
            lab, val = _split(ln)
            if val.lower() not in blob:
                bad.append("V%d %s missing copy: %s" % (n, cid, val[:40]))
            if lab and lab.lower() not in blob:
                bad.append("V%d %s missing label: %s" % (n, cid, lab[:30]))
        if label and label.lower() not in blob:
            bad.append("V%d %s missing on-card label: %s" % (n, cid, label[:40]))
    return bad

if __name__ == "__main__":
    for n in (12, 13, 14):
        pngs, svgs, sheet, cs = build(n)
        bad = [os.path.basename(x) for x in pngs
               if Image.open(x).size != (1920, 1080)]
        cu = copy_unchanged(n)
        print("V%d  %d png  %d svg  wrong size: %s  copy unchanged: %s"
              % (n, len(pngs), len(svgs), bad or "none",
                 "yes" if not cu else cu[:2]))
