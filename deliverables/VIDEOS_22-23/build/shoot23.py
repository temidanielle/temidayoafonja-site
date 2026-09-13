# -*- coding: utf-8 -*-
"""Render every card to PNG, and build contact sheets for visual inspection."""
import os, sys, math
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rdeck import render_html, shoot
from PIL import Image
import masters23 as M
import geocheck23 as G

HERE = os.path.dirname(os.path.abspath(__file__))


def png(n, outdir):
    cards, names = G.cards_for(n)
    html = render_html(cards, os.path.join(outdir, "_v%d.html" % n), "V%d" % n)
    return shoot(html, outdir, names), names


def sheet(paths, path, cols=4, w=460):
    h = int(w * 1080 / 1920.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 12,
                           rows * h + (rows + 1) * 12), (236, 232, 224))
    for i, p in enumerate(paths):
        im = Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS)
        sh.paste(im, (12 + (i % cols) * (w + 12), 12 + (i // cols) * (h + 12)))
    sh.save(path)
    return path


def phone(paths, path, cols=6, w=190):
    """What the card looks like at phone scale. Legibility is judged here."""
    return sheet(paths, path, cols, w)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/v2223_png"
    for n in M.VIDEOS:
        d = os.path.join(out, "V%d" % n)
        os.makedirs(d, exist_ok=True)
        made, names = png(n, d)
        print("V%d  %d png" % (n, len(made)))
        print(" ", sheet(made, os.path.join(out, "V%d_sheet.png" % n)))
        print(" ", phone(made, os.path.join(out, "V%d_phone.png" % n)))
