# -*- coding: utf-8 -*-
"""Render every frame to PNG and build a phone-size contact sheet per video.

Mobile legibility is a hard requirement and is checked by looking at the
frames at phone width, not by trusting font-size metadata.
"""
import os, sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rdeck import shoot, render_pptx
import geocheck, masters1421 as M
from PIL import Image

PHONE_W = 393          # a common phone logical width
COLS = 2


def contact_sheet(pngs, out_path, cols=COLS, phone_w=PHONE_W, pad=18):
    """Each frame scaled to the width it occupies on a phone, tiled."""
    tiles = []
    for p in pngs:
        im = Image.open(p).convert("RGB")
        h = int(round(im.height * phone_w / im.width))
        tiles.append(im.resize((phone_w, h), Image.LANCZOS))
    rows = (len(tiles) + cols - 1) // cols
    tw, th = phone_w, tiles[0].height
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * pad,
                              rows * th + (rows + 1) * pad), (24, 26, 30))
    for i, t in enumerate(tiles):
        x = pad + (i % cols) * (tw + pad)
        y = pad + (i // cols) * (th + pad)
        sheet.paste(t, (x, y))
    sheet.save(out_path)
    return out_path


def build(n, vis_dir, work):
    probs, html, cards, names = geocheck.check(n, work)
    if probs:
        raise SystemExit("V%d geometry problems remain: %s" % (n, probs))
    png_dir = os.path.join(vis_dir, "Support_Reference_PNG")
    shoot(os.path.abspath(html), png_dir, names)
    render_pptx(cards, os.path.join(vis_dir,
                                    "V%d_Reference_Deck.pptx" % n))
    sheet = contact_sheet([os.path.join(png_dir, x) for x in names],
                          os.path.join(vis_dir,
                                       "V%d_Phone_Size_Contact_Sheet.png" % n))
    return png_dir, sheet, names


if __name__ == "__main__":
    out = sys.argv[1]
    for n in M.VIDEOS:
        d = os.path.join(out, "V%d" % n)
        os.makedirs(d, exist_ok=True)
        png_dir, sheet, names = build(n, d, "/tmp/v1421_geo")
        print("V%-3d %d PNGs, deck, contact sheet" % (n, len(names)))
