# -*- coding: utf-8 -*-
"""Build the post-V14 Missing Rung roadmap reconciliation."""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Modules are prefixed mr_ because the house helpers insert their own build directories
# at the front of sys.path, which shadows bare names.
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import mr_data as D, mr_recon as R, mr_cross as C

EYEBROW = "capability formation | post-v14 architecture"
NAME = "POST_V14_MISSING_RUNG_ROADMAP_RECONCILIATION.docx"

def build(path):
    d = base_doc()
    title_block(d, EYEBROW, "The Missing Rung and the post-V14 roadmap",
                "One reconciliation. Territory locked, duplication resolved, nothing rewritten.")
    kv(d, "Generated", D.STAMP)
    kv(d, "Scope", "Architecture only. No script was rewritten and no production asset created.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "V4 to V14 were read only and not changed. One instruction in the strategic update "
               "cannot be followed without breaking that lock, and it is raised as a decision "
               "rather than resolved.")

    h(d, "What was available to read")
    table(d, ["Input", "Checksum", "Size", "Status", "What it supplied"],
          [[a, b, c, e, f] for a, b, c, e, f in D.INPUTS], widths=[1.6, 1.0, 0.8, 0.95, 2.35])
    callout(d, D.LIMIT)

    h(d, "Executive recommendation")
    bullets(d, D.EXEC)

    page_break(d)
    h(d, "What is now strategically locked")
    table(d, ["Item", "Verdict", "Note"],
          [[a, b, c] for a, b, c in D.LOCKED], widths=[2.1, 1.35, 3.25])

    h(d, "V15 to V21 reconciliation")
    table(d, ["Video", "Verdict", "Confidence", "Why"],
          [[a, b, c, e] for a, b, c, e in R.V15_21], widths=[1.35, 1.2, 0.95, 3.2])

    page_break(d)
    h(d, "MR1 to MR8 reconciliation")
    table(d, ["Episode", "Verdict", "Confidence", "Why"],
          [[a, b, c, e] for a, b, c, e in R.MR], widths=[1.45, 1.2, 0.75, 3.3])

    h(d, "Duplicate and overlap map against the locked catalogue")
    table(d, ["Pair", "Verdict", "What it means"],
          [[a, b, c] for a, b, c in R.LOCKED_CHECKS], widths=[2.25, 1.35, 3.1])
    caption(d, "Eight to seven. Four planned videos and three Missing Rung episodes collapse into "
               "three, and one old roadmap episode retires.")

    page_break(d)
    h(d, "Recommended post-V14 public sequence")
    table(d, ["#", "Title", "Thumbnail", "Source"],
          [[s["n"], s["title"], s["thumb"], s["src"]] for s in C_seq()],
          widths=[0.4, 2.5, 1.55, 2.25])
    caption(d, "V15 to V19 are the existing plan unchanged. The Missing Rung playlist is V20 to "
               "V26. Every retained episode keeps its position relative to the others; the merges "
               "land at the later of the two original positions rather than being reordered.")

    for s in C_seq():
        sub(d, "%s  ·  %s" % (s["n"], s["title"]))
        kv(d, "Thumbnail", s["thumb"])
        kv(d, "Source concept", s["src"])
        kv(d, "Core viewer problem", s["problem"])
        kv(d, "Artifact", s["artifact"])
        kv(d, "Primary audit question", s["audit"])
        kv(d, "Boundary", s["boundary"])
        kv(d, "Relationship to adjacent video", s["adj"])
        kv(d, "Natural next offer", s["offer"])

    page_break(d)
    h(d, "Missing Rung playlist order")
    table(d, ["Playlist position", "Public number", "Title"],
          [[str(i + 1), s["n"], s["title"]] for i, s in enumerate(C_seq()[5:])],
          widths=[1.2, 1.2, 4.3])
    para(d, "Seven episodes, not eight. MR5 merged into V23, MR6 into V24, and MR2 with MR8 into "
            "V26. The journey logic is intact: recognition, redefine growth, read the structure, "
            "the authority consequence, the management decision, the loss, and the deliberate "
            "move.")

    h(d, "Consecutive or interleaved")
    for name, why in C.CONSECUTIVE:
        sub(d, name)
        para(d, why)

    page_break(d)
    h(d, "Watch Next map")
    table(d, ["From", "To", "Why"],
          [[a, b, c] for a, b, c in C.WATCH_NEXT], widths=[1.1, 1.0, 4.6])
    caption(d, "Three inbound routes are already recorded in locked audio and cannot change. Two "
               "of the twelve route back into existing episodes rather than forward, which keeps "
               "V12, V13 and V18 alive in the catalogue.")

    h(d, "Watch-Me-Read and artifact map")
    table(d, ["#", "Artifact", "What it would be"],
          [[a, b, c] for a, b, c in C.ARTIFACTS], widths=[0.45, 1.75, 4.5])
    para(d, C.ARTIFACT_NOTE)

    page_break(d)
    h(d, "Evidence and provenance requirements")
    table(d, ["Issue", "Severity", "What it means"],
          [[a, b, c] for a, b, c in C.EVIDENCE], widths=[1.85, 1.2, 3.65])

    h(d, "CTA map")
    table(d, ["#", "Offer", "Why"],
          [[a, b, c] for a, b, c in C.CTA], widths=[0.45, 1.85, 4.4])
    para(d, C.CTA_NOTE)

    page_break(d)
    h(d, "Revision level for every retained episode")
    table(d, ["#", "Level", "The single reason"],
          [[a, b, c] for a, b, c in C.LEVELS], widths=[0.45, 1.35, 4.9])
    caption(d, "PROVISIONAL means the level is an estimate because the underlying master could "
               "not be read. Those five firm up the day the MR scripts arrive.")

    h(d, "Titles and thumbnails requiring a decision")
    table(d, ["#", "Situation", "Recommendation"],
          [[a, b, c] for a, b, c in C.PACKAGING], widths=[1.35, 1.5, 3.85])

    h(d, "Decisions needed before script rebuilding")
    for name, state, why in C.DECISIONS:
        sub(d, "%s  ·  %s" % (name, state))
        para(d, why)
    callout(d, "Six are blocking. Nothing in the Missing Rung can be written until the source "
               "report is in the workspace, and nothing downstream of the three merges can be "
               "numbered until they are confirmed.")
    footer_note(d, "Architecture only. No script rewritten, no V4 to V14 file changed, no new "
                   "research conducted, no URL invented.")
    d.save(path)

def C_seq():
    return R.SEQ

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
