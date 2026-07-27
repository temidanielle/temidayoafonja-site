#!/usr/bin/env python3
"""
FONT BUILD  (provenance / run-once; requires network)
=====================================================

Downloads the two brand faces from Google Fonts, subsets them to the character
set the brand uses, normalises the family names, and writes the woff2 files that
`generate.py` reads and embeds.

    Cormorant Garamond, weight 500  ->  fonts/CormorantGaramond-Medium.subset.woff2
    Montserrat,         weight 600  ->  fonts/Montserrat-SemiBold.subset.woff2

The subset woff2 files are committed to the repo, so `generate.py` never needs a
network connection. Re-run this only to refresh or re-subset the fonts.

    python3 build_fonts.py
"""

import os
import urllib.request

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")

# Latin subset (unicode-range U+0000-00FF) of each static instance, taken from
# the Google Fonts CSS2 API. Pinned so the build is reproducible.
SOURCES = [
    dict(
        family="Cormorant Garamond",
        out="CormorantGaramond-Medium.subset.woff2",
        url=("https://fonts.gstatic.com/s/cormorantgaramond/v21/"
             "co3umX5slCNuHLi8bLeY9MK7whWMhyjypVO7abI26QOD_s06KnTOig.woff2"),
    ),
    dict(
        family="Montserrat",
        out="Montserrat-SemiBold.subset.woff2",
        url=("https://fonts.gstatic.com/s/montserrat/v31/"
             "JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCu173w5aXo.woff2"),
    ),
]

# Current strings plus headroom for future editions (headlines change).
CHARS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         "abcdefghijklmnopqrstuvwxyz"
         "0123456789"
         " .,:;'\"’‘“”!?&()/-–—")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")


def build(src):
    raw = os.path.join(FONTS, "_src_" + src["out"])
    req = urllib.request.Request(src["url"], headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(raw, "wb") as fh:
        fh.write(data)

    opts = Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]     # keep kerning / ligatures for shaping
    opts.name_IDs = ["*"]
    opts.recalc_bounds = True
    ss = Subsetter(options=opts)

    font = TTFont(raw)
    ss.populate(text=CHARS)
    ss.subset(font)

    # Normalise the (odd Google static-instance) names so @font-face resolves.
    fam = src["family"]
    name = font["name"]
    for nid, val in [(1, fam), (2, "Regular"), (4, fam),
                     (6, fam.replace(" ", "")), (16, fam), (17, "Regular")]:
        name.setName(val, nid, 3, 1, 0x409)

    out = os.path.join(FONTS, src["out"])
    font.save(out)
    os.remove(raw)
    weight = font["OS/2"].usWeightClass
    print(f"  wrote fonts/{src['out']}  family='{fam}'  weight={weight}  "
          f"glyphs={len(font.getGlyphOrder())}")


def main():
    os.makedirs(FONTS, exist_ok=True)
    print("Building subset fonts from Google Fonts...")
    for src in SOURCES:
        build(src)
    print("Done.")


if __name__ == "__main__":
    main()
