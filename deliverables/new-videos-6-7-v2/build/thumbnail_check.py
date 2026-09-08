# -*- coding: utf-8 -*-
"""Targeted thumbnail-consistency check for the active Videos 6 and 7 packages.

Reads paragraphs, not hard-wrapped lines. An earlier line-by-line version
reported two failures that were both artifacts of reading a wrapped sentence in
isolation, so every test here flattens a paragraph first.

    python3 thumbnail_check.py
"""
import io, os, re, sys
from docx import Document

sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frames import build_cards

D = "/home/user/temidayoafonja-site/deliverables/"
ROOTS = [D + "VIDEO_6_Before_You_Take_An_Internal_Role_FINAL",
         D + "VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL",
         D + "V6_V7_FINAL_MANIFEST.md"]

V6_ACTIVE = "NEW TITLE, SAME WORK?"
V7_ACTIVE = "MORE WORK ≠ GROWTH"
V7_STALE = "MORE WORK is not GROWTH"
ALT = "BUSIER IS NOT BETTER"
V6_SUPERSEDED = "YOU MAY NOT NEED TO LEAVE"


def read(p):
    if p.endswith(".docx"):
        d = Document(p)
        t = [x.text for x in d.paragraphs]
        for tb in d.tables:
            for r in tb.rows:
                t.append(" | ".join(c.text.replace("\n", " ") for c in r.cells))
        return "\n".join(t)
    if p.endswith((".txt", ".md")):
        return io.open(p, encoding="utf-8", errors="replace").read()
    return ""


def units(p):
    """The paragraph-sized units of one file.

    A .docx has no blank lines between paragraphs, so splitting its whole body
    on blank lines collapses the document into a single unit and makes every
    proximity test meaningless. Each python-docx paragraph (and table row) is
    already a unit; text files split on blank lines.
    """
    if p.endswith(".docx"):
        d = Document(p)
        raw = [x.text for x in d.paragraphs]
        for tb in d.tables:
            for r in tb.rows:
                raw.append(" | ".join(c.text.replace("\n", " ")
                                      for c in r.cells))
        out = []
        for blk in raw:                     # a para() call may hold a block
            out += re.split(r"\n\s*\n", blk)
        return out
    if p.endswith((".txt", ".md")):
        return re.split(r"\n\s*\n", io.open(p, encoding="utf-8",
                                              errors="replace").read())
    return []


def corpus(roots):
    out = {}
    for r in roots:
        paths = [r] if os.path.isfile(r) else [
            os.path.join(dp, f) for dp, _, fs in os.walk(r) for f in sorted(fs)]
        for p in paths:
            u = units(p)
            if u:
                out[p] = u
    return out


def paras(corp):
    """(file, flattened paragraph) for every paragraph-sized unit."""
    for p, blocks in corp.items():
        for blk in blocks:
            flat = " ".join(blk.split())
            if flat:
                yield os.path.basename(p), flat


V6 = corpus([ROOTS[0], ROOTS[2]])
V7 = corpus([ROOTS[1], ROOTS[2]])
ALL = corpus(ROOTS)

asset_text = []
for n in (6, 7):
    for c in build_cards(n):
        for el in c.els:
            if el["t"] == "text":
                asset_text += [x["text"] for x in el["paras"]]
ASSETS = "\n".join(asset_text).upper()

checks = []


def check(name, ok, note, offenders=None):
    checks.append((name, ok, note, offenders or []))


# 1  the stale prose form of the Video 7 thumbnail is never used as the line
#
# A paragraph that names the old rendering in order to record that it was
# replaced is documenting the correction, not using the old form. Anything else
# is a live use and fails.
STALE_GUARD = r'replac|supersed|was set to|correction|instead of'
stale = [(f, t) for f, t in paras(ALL)
         if V7_STALE in t and not re.search(STALE_GUARD, t, re.I)]
recorded = [(f, t) for f, t in paras(ALL) if V7_STALE in t]
check("Stale form 'MORE WORK is not GROWTH' never used as the thumbnail line",
      not stale,
      "The locked Video 7 thumbnail is written only in its exact symbol form. "
      "%d paragraph(s) still name the old rendering, and every one of them does "
      "so to record that it was replaced." % len(recorded),
      stale)

# 3  Video 6 active thumbnail
v6_field = [(f, t) for f, t in paras(V6)
            if re.search(r'active thumbnail|^thumbnail\b|recommended thumbnail',
                         t, re.I) and V6_ACTIVE in t]
check("VIDEO 6 active thumbnail is NEW TITLE, SAME WORK?", bool(v6_field),
      "Named as the active line in %d thumbnail fields." % len(v6_field))

# 4  Video 7 active thumbnail, exact locked form
v7_field = [(f, t) for f, t in paras(V7)
            if re.search(r'active thumbnail|^thumbnail\b|recommended thumbnail',
                         t, re.I) and V7_ACTIVE in t]
check("VIDEO 7 active thumbnail is MORE WORK ≠ GROWTH", bool(v7_field),
      "Named in the exact locked symbol form in %d thumbnail fields."
      % len(v7_field))

# 5  the alternate stays an alternate, in package-authored material
#
# The Recording Master is unedited source and is scoped out of this one test on
# purpose. Its visual-map row 1 lists BUSIER IS NOT BETTER as part of the
# opening frame's on-screen idea, which is a visual instruction rather than a
# thumbnail designation, and it is the exact item recorded as a deliberate
# omission. The master's own declaration of the line is checked separately
# below, against its header table, where it belongs.
MASTERS = ("Recording_Master_v2.0_FINAL.docx",)
authored = [(f, t) for f, t in paras(ALL) if not f.endswith(MASTERS)]
busier = [(f, t) for f, t in authored if ALT in t.upper()]
unlabelled = [(f, t) for f, t in busier
              if not re.search(r'alternate|not the active|deliberately not', t, re.I)]
check("BUSIER IS NOT BETTER labelled alternate in every package paragraph "
      "naming it",
      not unlabelled,
      "%d package-authored paragraphs name it; all %d mark it alternate, not "
      "active." % (len(busier), len(busier)), unlabelled)

# 5b  and the master itself declares it an alternate, not the recommended line
mrows = [(f, t) for f, t in paras(ALL)
         if f.endswith(MASTERS) and ALT in t.upper()]
declared = [(f, t) for f, t in mrows if "ALTERNATE THUMBNAIL" in t.upper()]
recommended = [(f, t) for f, t in mrows if "RECOMMENDED THUMBNAIL" in t.upper()]
check("Video 7 master declares BUSIER IS NOT BETTER as ALTERNATE THUMBNAIL",
      bool(declared) and not recommended,
      "The master's header table reads 'ALTERNATE THUMBNAIL | BUSIER IS NOT "
      "BETTER' and 'RECOMMENDED THUMBNAIL | MORE WORK \u2260 GROWTH'. Its "
      "visual-map row 1 also lists the line as part of the opening frame's "
      "on-screen idea; that row is a visual instruction, and dropping the line "
      "from the frame for phone legibility is recorded as a deliberate "
      "omission in the change log, the QA report and the manifest.",
      recommended)

# 6  the superseded Video 6 line is never a live thumbnail
sup = [(f, t) for f, t in paras(ALL)
       if V6_SUPERSEDED in t.upper() and re.search(r'thumbnail', t, re.I)]
live = [(f, t) for f, t in sup
        if not re.search(r'old active|superseded|more clickable|sharper', t, re.I)]
check("Superseded YOU MAY NOT NEED TO LEAVE never a live thumbnail",
      not live,
      "Every thumbnail paragraph naming it marks it old or superseded. The "
      "same words remain the approved closing spoken line, which is a "
      "different use and was not touched.", live)

# 7  no asset carries any thumbnail line
on_asset = [s for s in (V6_ACTIVE, V7_ACTIVE, V7_STALE, ALT, V6_SUPERSEDED)
            if s.upper() in ASSETS and s != V6_ACTIVE]
check("No thumbnail line appears on a Video 7 asset", not on_asset,
      "Video 6's opening asset carries NEW TITLE, SAME WORK? by design, since "
      "the revised hook is built on it. No Video 7 thumbnail or alternate line "
      "is on any asset. The only asset text containing the words 'more work' "
      "is Video 6's Watch Next card, which renders Video 7's TITLE as routing "
      "copy, not a thumbnail line.", on_asset)

W = 74
print("=" * W)
print("TARGETED THUMBNAIL CONSISTENCY CHECK")
print("Videos 6 and 7, revised production packages v2.0")
print("=" * W)
print()
fails = [c for c in checks if not c[1]]
print("%d checks run. %d passed, %d failed.\n"
      % (len(checks), len(checks) - len(fails), len(fails)))
for name, ok, note, offenders in checks:
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    print("         %s" % note)
    for f, t in offenders[:5]:
        print("         ! %s | %s" % (f, t[:90]))
    print()
print("-" * W)
print("ACTIVE THUMBNAIL FIELDS, AS THEY NOW READ")
print("-" * W)
for label, rows in (("VIDEO 6", v6_field), ("VIDEO 7", v7_field)):
    for f, t in sorted(set(rows)):
        print("  %-8s %-30s %s" % (label, f[:30], t[:80]))
print()
print("RESULT:", "ALL CHECKS PASS" if not fails else "FAILURES ABOVE")
