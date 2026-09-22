# -*- coding: utf-8 -*-
"""Build the V15-V21 pre-rewrite editorial audit."""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Modules are prefixed a5_ because the house document helpers insert their own build
# directories at the front of sys.path, which shadows bare names.
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, rule)
import a5_data as D, a5_notes as N, a5_cross as C

EYEBROW = "capability formation | v15 to v21"
NAME = "V15-V21_PRE_REWRITE_EDITORIAL_AUDIT.docx"

def build(path):
    d = base_doc()
    title_block(d, EYEBROW, "V15 to V21 pre-rewrite editorial audit",
                "What to preserve, what to fix, and what has to be decided first")
    kv(d, "Generated", D.STAMP)
    kv(d, "Scope", "Audit only. Nothing was rewritten and no production asset was created.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "V4 to V14 are locked and were read only. Three of them make spoken promises into "
               "this slate, which is why three of the seven titles are not open even as a "
               "discussion.")

    h(d, "Executive read")
    bullets(d, D.EXEC)

    h(d, "V4 to V14 untouched")
    bullets(d, D.UNTOUCHED)

    page_break(d)
    h(d, "The slate")
    table(d, ["#", "Title", "Thumbnail", "Primary audit", "Source", "Revision"],
          [[v["n"], v["title"], v["thumb"], v["audit"], v["src"], v["level"]] for v in D.SLATE],
          widths=[0.4, 1.75, 1.05, 0.95, 1.65, 0.9])
    caption(d, "Revision levels are repeated on their own page at the end of this document.")

    for v in D.SLATE:
        page_break(d)
        h(d, "%s  |  %s" % (v["n"], v["title"]))
        kv(d, "Thumbnail", v["thumb"])
        kv(d, "Source", v["src"])
        kv(d, "Revision level", v["level"])
        for f in N.F:
            if f == "Revision level":
                continue
            sub(d, f.upper())
            items = N.NOTES[v["n"]][f]
            if len(items) == 1:
                para(d, items[0])
            else:
                bullets(d, items)

    page_break(d)
    h(d, "Watch-Me-Read and artifact map")
    table(d, ["#", "Artifact", "Does the read help", "What it would be"],
          [[a, b, c, e] for a, b, c, e in C.ARTIFACT_MAP], widths=[0.4, 1.5, 1.35, 3.45])
    caption(d, "Two of the seven earn an artifact outright. Two more earn one only if a lawful "
               "document can be sourced. Three are stronger camera-led, and forcing a card into "
               "them would decorate rather than teach.")

    h(d, "Voice risks")
    for name, why in C.VOICE_RISKS:
        sub(d, name)
        para(d, why)

    page_break(d)
    h(d, "Evidence and provenance issues")
    table(d, ["Issue", "Severity", "What it means"],
          [[a, b, c] for a, b, c in C.EVIDENCE], widths=[1.9, 1.15, 3.65])

    h(d, "CTA map")
    table(d, ["#", "Offer", "Change", "Why"],
          [[a, b, c, e] for a, b, c, e in C.CTA_MAP], widths=[0.4, 1.75, 1.35, 3.2])
    caption(d, "Three of the seven carry no commercial ask under these recommendations. That is "
               "the problem deciding, not a gap to fill.")

    page_break(d)
    h(d, "Packaging assessment")
    table(d, ["#", "Verdict", "Construction", "Note"],
          [[a, b, c, e] for a, b, c, e in C.PACKAGING], widths=[0.4, 1.35, 1.6, 3.35])
    para(d, C.PACKAGING_NOTE)

    h(d, "Sequence assessment")
    callout(d, C.SEQUENCE_VERDICT)
    for name, why in C.SEQUENCE:
        sub(d, name)
        para(d, why)

    page_break(d)
    h(d, "Recommended revision level")
    table(d, ["#", "Title", "Level", "The single reason"],
          [[v["n"], v["title"], v["level"], _reason(v["n"])] for v in D.SLATE],
          widths=[0.4, 1.95, 1.0, 3.35])

    h(d, "Decisions needed before rewriting")
    for name, state, why in C.DECISIONS:
        sub(d, "%s  ·  %s" % (name, state))
        para(d, why)
    callout(d, "Three of these are blocking. V17 cannot be written until its scope against locked "
               "V8 is settled, V19 cannot be shaped until the Learn, Practice, Prove question is "
               "answered, and V20 and V21 cannot be planned until the artifact sourcing question "
               "is answered.")
    footer_note(d, "Audit only. No V15 to V21 script was rewritten and no V4 to V14 file was "
                   "changed.")
    d.save(path)

REASONS = {
 "V15": "Two competing four-line structures to remove, a CTA that points at the wrong offer, and "
        "an employer-side read that is missing rather than wrong.",
 "V16": "The hinge is buried in the middle while the first half re-teaches locked V5 and V12.",
 "V17": "Most of the source is already locked V8's material. The episode has to be re-scoped, not "
        "revised.",
 "V18": "A named five-layer inventory, and an opening that re-teaches locked V13 before it starts.",
 "V19": "Excellent material carried on a named three-part structure, with one leg that is locked "
        "V12's whole video.",
 "V20": "A manager-side section that breaks the single-viewer address, plus a negotiation beat "
        "that overlaps locked V11.",
 "V21": "Strongest and most distinct source in the slate. De-frame the four questions and settle "
        "the CTA, and it is ready.",
}
def _reason(n):
    return REASONS[n]

def sha256(p):
    h_ = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h_.update(b)
    return h_.hexdigest()

if __name__ == "__main__":
    p = os.path.join(OUT, NAME)
    build(p)
    print(p)
    print(sha256(p))
