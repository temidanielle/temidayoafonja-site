# -*- coding: utf-8 -*-
"""Render every state for V1, V2 and V3 to PNG, plus SVG for the key frames."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "V4-V11_SYNC/build")
sys.path.append(DELIV + "FLAGSHIP_CAREER_CHANGE/build")
import rdeck
from rdeck import render_html, shoot
from PIL import Image
import svg23
import st_frames as F

# Editable vector source is written for the frames an editor is most likely to
# re-time or re-colour: every memory card, every CTA, every Watch Next, and the
# frame that is each video's visual payoff.
SVG_KEYS = {
 1: ("V1_01_THE_MOVE", "V1_03_MATCHING_WORDS", "V1_07D_COMPLETE",
     "V1_08_EXPERIENCED_AND_NEW", "V1_09A_MEMORY_LINE", "V1_10_CTA",
     "V1_11_WATCH_NEXT"),
 2: ("V2_01_VALUE_VS_LEGIBLE", "V2_02_THE_SENTENCE", "V2_04_UNDERNEATH",
     "V2_07D_ALL", "V2_10A_MEMORY_LINE", "V2_11_CTA", "V2_12_WATCH_NEXT"),
 3: ("V3_03A_THE_RULE", "V3_05D_ALL", "V3_07_THE_WORK", "V3_10_BEFORE_YOU_RESIGN",
     "V3_11A_MEMORY_LINE", "V3_12_CTA", "V3_13_WATCH_NEXT"),
}

def vis_dir(n):
    return os.path.join(OUT, "V%d" % n, "04_VISUAL_ASSETS")

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

def build(n):
    vis = vis_dir(n)
    os.makedirs(vis, exist_ok=True)
    cards, names = [], []
    for fam, name, draw, note in F.states(n):
        c = rdeck.Card(len(cards) + 1, name + ".png")
        draw(c)
        cards.append(c)
        names.append(name + ".png")
    html = render_html(cards, os.path.join(vis, "_f.html"), "V%d" % n)
    shoot(html, vis, names)
    os.remove(html)
    idx = {nm[:-4]: c for nm, c in zip(names, cards)}
    svgs = []
    for key in SVG_KEYS[n]:
        p = os.path.join(vis, key + ".svg")
        svg23.write(idx[key], p)
        svgs.append(p)
    pngs = [os.path.join(vis, x) for x in names]
    sheet = contact_sheet(pngs, os.path.join(vis, "Phone_Size_Contact_Sheet.png"))
    return pngs, svgs, sheet, cards

if __name__ == "__main__":
    for n in (1, 2, 3):
        p, s, sheet, cards = build(n)
        bad = [os.path.basename(x) for x in p
               if Image.open(x).size != (1920, 1080)]
        print("V%d  %d png  %d svg  contact sheet %s  wrong size: %s"
              % (n, len(p), len(s), Image.open(sheet).size, bad or "none"))
