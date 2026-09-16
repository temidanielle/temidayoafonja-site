# -*- coding: utf-8 -*-
"""Render one batch's visual assets into the synchronized packages."""
import os, sys, json, math
BATCH = sys.argv[1]
DEST = sys.argv[2]
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.insert(0, DELIV + "V4-V11_SYNC/build")
if BATCH == "sprint":
    sys.path.insert(0, DELIV + "SPRINT_V4-V9/build")
    import frames as F
    import lay23 as L
    NUMS = (4, 5, 6, 7, 8, 9)
else:
    sys.path.insert(0, DELIV + "V10-V11/build")
    import frames1011 as F
    import lay1011 as L
    NUMS = (10, 11)
import rdeck
from rdeck import render_html, shoot
from PIL import Image
import svg23
import overrides

changed = overrides.apply({n: F.SETS[n] for n in NUMS}, L)


def contact_sheet(paths, path, cols=6, w=190):
    h_ = int(w * 1080 / 1920.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 10,
                           rows * h_ + (rows + 1) * 10), (236, 232, 224))
    for i, p in enumerate(paths):
        sh.paste(Image.open(p).convert("RGB").resize((w, h_), Image.LANCZOS),
                 (10 + (i % cols) * (w + 10), 10 + (i // cols) * (h_ + 10)))
    sh.save(path)
    return path


out = {}
for n in NUMS:
    vis = os.path.join(DEST % n, "04_VISUAL_ASSETS")
    os.makedirs(vis, exist_ok=True)
    cards, names = [], []
    for f, st in F.states(n):
        c = rdeck.Card(len(cards) + 1, st["name"] + ".png")
        st["draw"](c)
        cards.append(c)
        names.append(st["name"] + ".png")
    html = render_html(cards, os.path.join(vis, "_v.html"), "V%d" % n)
    made = shoot(html, vis, names)
    os.remove(html)
    idx = {nm[:-4]: c for nm, c in zip(names, cards)}
    svgs = []
    for f in F.SETS[n]:
        if f.get("svg"):
            st = f["states"][0]
            svgs.append(svg23.write(
                idx[st["name"]], os.path.join(vis, st["name"] + ".svg"),
                "V%d  %s" % (n, st["name"])))
    sheet = contact_sheet(made, os.path.join(
        vis, "Phone_Size_Contact_Sheet.png"))
    sizes = {os.path.basename(p): Image.open(p).size for p in made}
    out[n] = dict(png=[os.path.basename(p) for p in made],
                  svg=[os.path.basename(p) for p in svgs],
                  sheet=os.path.basename(sheet),
                  families=len(F.SETS[n]), states=len(F.states(n)),
                  all_1080=all(v == (1920, 1080) for v in sizes.values()))
print(json.dumps(dict(videos=out, changed=changed)))
