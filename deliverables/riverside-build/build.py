# -*- coding: utf-8 -*-
"""Build the Riverside edit asset set for one video.

    python3 build.py 2

Writes, under deliverables/video-N-slides/riverside/:
    Video_N_Riverside_Edit_Deck.pptx
    Video_N_Riverside_PNG/          1920 x 1080 PNGs, semantic filenames
    Video_N_Riverside_PNG.zip
    Riverside_Edit_Map.txt
    Riverside_Slide_Audit.txt

The existing presentation and reveal decks are never opened for writing.
"""
import os, sys, shutil, zipfile, hashlib, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import qa
from cards import SETS, TITLES, build_cards
from audits import AUDIT, ORIGINALS, BRAND_NOTE
from rdeck import render_html, render_pptx, shoot
from PIL import Image

REPO = "/home/user/temidayoafonja-site"
DELIV = os.path.join(REPO, "deliverables")
WRAP = 78


def wrap(text, indent=""):
    out = []
    for para in text.split("\n"):
        if not para.strip():
            out.append("")
            continue
        out.extend(textwrap.wrap(para, WRAP - len(indent),
                                 initial_indent=indent, subsequent_indent=indent))
    return "\n".join(out)


def edit_map(n):
    specs = SETS[n]
    L = []
    L.append("=" * WRAP)
    L.append("RIVERSIDE EDIT MAP")
    L.append("Video %d  ยท  %s" % (n, TITLES[n]))
    L.append("=" * WRAP)
    L.append("")
    L.append(wrap(
        "%d visual assets for a talking-head edit. Temidayo is on camera for the "
        "long stretches between them. Each one is a full-frame 1920 x 1080 PNG, "
        "uploaded to Riverside individually, with its own prompt below."
        % len(specs)))
    L.append("")
    for i, s in enumerate(specs, start=1):
        L.append("-" * WRAP)
        L.append("SLIDE %d OF %d" % (i, len(specs)))
        L.append("")
        L.append("  FILE")
        L.append("    " + s["file"])
        L.append("")
        L.append("  SCRIPT MATCH")
        L.append(wrap(s["script"], "    "))
        L.append("")
        L.append("  PURPOSE")
        L.append(wrap(s["purpose"], "    "))
        L.append("")
        L.append("  DISPLAY")
        L.append("    " + s["display"])
        L.append("")
        L.append("  SUGGESTED SCREEN TIME")
        L.append("    " + s["seconds"])
        L.append("")
        L.append("  RIVERSIDE AI PROMPT  (copy and paste with this image)")
        L.append(wrap('"' + s["prompt"] + '"', "    "))
        L.append("")
    L.append("=" * WRAP)
    L.append("END OF MAP")
    L.append("=" * WRAP)
    return "\n".join(L).replace("ยท", "-")


def slide_audit(n):
    a = AUDIT[n]
    main, reveal = ORIGINALS[n]
    new = len(SETS[n])
    L = []
    L.append("=" * WRAP)
    L.append("RIVERSIDE SLIDE AUDIT")
    L.append("Video %d  -  %s" % (n, TITLES[n]))
    L.append("=" * WRAP)
    L.append("")
    L.append("COUNTS")
    L.append("  Original presentation deck        %2d slides" % main)
    L.append("  Original reveal build deck        %2d slides" % reveal)
    L.append("  Riverside edit asset set          %2d slides" % new)
    L.append("  Reduction against the reveal deck %2d fewer" % (reveal - new))
    L.append("")
    L.append(wrap("Both original decks are untouched. This set is additive and "
                  "lives in its own folder."))
    L.append("")
    L.append("-" * WRAP)
    L.append("KEPT AND MERGED")
    L.append("-" * WRAP)
    for src, verdict, dest, why in a["keep"]:
        L.append("")
        L.append("  %s  [%s]" % (src, verdict))
        L.append("    to: %s" % dest)
        L.append(wrap(why, "    "))
    L.append("")
    L.append("-" * WRAP)
    L.append("REMOVED")
    L.append("-" * WRAP)
    for src, verdict, why in a["removed"]:
        L.append("")
        L.append("  %s  [%s]" % (src, verdict))
        L.append(wrap(why, "    "))
    if a["added"]:
        L.append("")
        L.append("-" * WRAP)
        L.append("ADDED")
        L.append("-" * WRAP)
        for dest, why in a["added"]:
            L.append("")
            L.append("  %s" % dest)
            L.append(wrap(why, "    "))
    L.append("")
    L.append("-" * WRAP)
    L.append("SCRIPT AND SLIDE CONFLICTS THAT NEED YOUR DECISION")
    L.append("-" * WRAP)
    if not a["conflicts"]:
        L.append("")
        L.append("  None found.")
    for where, what, done in a["conflicts"]:
        L.append("")
        L.append("  %s" % where)
        L.append("")
        L.append(wrap("THE CONFLICT: " + what, "    "))
        L.append("")
        L.append(wrap("WHAT I DID: " + done, "    "))
    L.append("")
    L.append("-" * WRAP)
    L.append(wrap(BRAND_NOTE.strip()))
    L.append("")
    L.append("=" * WRAP)
    L.append("END OF AUDIT")
    L.append("=" * WRAP)
    return "\n".join(L)


def build(n):
    out = os.path.join(DELIV, "video-%d-slides" % n, "riverside")
    png_dir = os.path.join(out, "Video_%d_Riverside_PNG" % n)
    shutil.rmtree(png_dir, ignore_errors=True)
    os.makedirs(png_dir, exist_ok=True)

    cards = build_cards(n)
    names = [c.filename for c in cards]
    html = render_html(cards, os.path.join(out, "_deck.html"),
                       "Video %d Riverside" % n)

    problems = qa.check(qa.measure(os.path.abspath(html)), names)
    if problems:
        for p in problems:
            print("  GEOMETRY:", p)
        raise SystemExit("geometry QA failed for video %d" % n)

    shoot(os.path.abspath(html), png_dir, names)
    os.remove(html)

    pptx = os.path.join(out, "Video_%d_Riverside_Edit_Deck.pptx" % n)
    render_pptx(cards, pptx)

    open(os.path.join(out, "Riverside_Edit_Map.txt"), "w").write(edit_map(n))
    open(os.path.join(out, "Riverside_Slide_Audit.txt"), "w").write(slide_audit(n))

    zpath = os.path.join(out, "Video_%d_Riverside_PNG.zip" % n)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in names:
            zi = zipfile.ZipInfo("Video_%d_Riverside_PNG/" % n + f,
                                 date_time=(2026, 9, 4, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, open(os.path.join(png_dir, f), "rb").read())

    return out, png_dir, pptx, zpath, names


if __name__ == "__main__":
    build(int(sys.argv[1]))
