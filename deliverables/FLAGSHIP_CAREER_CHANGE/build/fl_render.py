# -*- coding: utf-8 -*-
"""Render the flagship visual assets with the house renderer."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "V4-V11_SYNC/build")
import rdeck
from rdeck import render_html, shoot
from PIL import Image
import svg23
import fl_frames as F

VIS = os.path.join(OUT, "04_VISUAL_ASSETS")
SVG_FAMILIES = ("FLAG_01_THE_MOVE", "FLAG_02D_WHERE_ADVICE_STOPS",
                "FLAG_05C_HIGHER_TITLE", "FLAG_06C_ALL_GAPS",
                "FLAG_07D_COMPLETE", "FLAG_08_EXPERIENCED_AND_NEW")


def contact_sheet(paths, path, cols=5, w=300):
    h_ = int(w * 1080 / 1920.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 12,
                           rows * h_ + (rows + 1) * 12), (236, 232, 224))
    for i, p in enumerate(paths):
        sh.paste(Image.open(p).convert("RGB").resize((w, h_), Image.LANCZOS),
                 (12 + (i % cols) * (w + 12), 12 + (i // cols) * (h_ + 12)))
    sh.save(path)
    return path


def main():
    os.makedirs(VIS, exist_ok=True)
    cards, names = [], []
    for fam, name, draw, note in F.states():
        c = rdeck.Card(len(cards) + 1, name + ".png")
        draw(c)
        cards.append(c)
        names.append(name + ".png")
    html = render_html(cards, os.path.join(VIS, "_f.html"), "FLAGSHIP")
    made = shoot(html, VIS, names)
    os.remove(html)
    idx = {nm[:-4]: c for nm, c in zip(names, cards)}
    svgs = []
    for key in SVG_FAMILIES:
        p = os.path.join(VIS, key + ".svg")
        svg23.write(idx[key], p)
        svgs.append(p)
    pngs = [os.path.join(VIS, n) for n in names]
    sheet = contact_sheet(pngs, os.path.join(VIS, "Phone_Size_Contact_Sheet.png"))
    return pngs, svgs, sheet, cards


if __name__ == "__main__":
    p, s, sheet, cards = main()
    print("%d png, %d svg" % (len(p), len(s)))
    from PIL import Image as I
    bad = [x for x in p if I.open(x).size != (1920, 1080)]
    print("wrong size:", bad)
    print(sheet, I.open(sheet).size)
