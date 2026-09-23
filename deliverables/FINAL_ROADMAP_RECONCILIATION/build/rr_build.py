# -*- coding: utf-8 -*-
"""Build the V15-V21 x Missing Rung final roadmap reconciliation."""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Modules are prefixed rr_ because the house helpers insert their own build
# directories at the front of sys.path, which shadows bare names.
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import rr_data as D, rr_disp as R, rr_seq as S

EYEBROW = "capability formation | post-v14 architecture"
NAME = "V15-V21_X_MISSING_RUNG_FINAL_ROADMAP_RECONCILIATION.docx"

def build(path):
    d = base_doc()
    title_block(d, EYEBROW, "V15 to V21 and The Missing Rung",
                "One reconciliation, made with all eight masters in hand")
    kv(d, "Generated", D.STAMP)
    kv(d, "Scope", "Architecture only. No script rewritten, no asset created.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "The eight Missing Rung masters were read in full for the "
               "first time in this pass, and they changed two of my earlier "
               "recommendations. Where that happened it is said plainly "
               "rather than quietly corrected.")

    h(d, "Executive recommendation")
    bullets(d, D.EXEC)

    h(d, "Length, measured")
    table(d, ["Master", "Spoken words", "Speech-only at 145 to 130 wpm"],
          [["MR%d" % n, "%d" % w, "%.1f to %.1f min" % (w / 145.0, w / 130.0)]
           for n, w in sorted(D.MR_WORDS.items())] +
          [["All eight", "%d" % sum(D.MR_WORDS.values()), "about 18 to 21 min"]],
          widths=[1.2, 1.5, 4.0])
    caption(d, "Counted from each master with the four header lines and the "
               "section labels removed. The locked band is %s spoken words. "
               "Every master is between a fifth and a half of production "
               "length, which is why the revision level for all eight is "
               "SUBSTANTIAL before any editorial question is asked."
            % D.LOCKED_BAND)

    page_break(d)
    h(d, "What is now locked")
    table(d, ["Item", "Verdict", "Note"],
          [[a, b, c] for a, b, c in D.LOCKED], widths=[2.0, 1.5, 3.2])

    h(d, "V15 to V21 disposition")
    table(d, ["Video", "Disposition", "Revision", "Why"],
          [[a, b, c, e] for a, b, c, e in R.V], widths=[1.45, 1.35, 0.85, 3.05])

    page_break(d)
    h(d, "MR1 to MR8 disposition")
    table(d, ["Episode", "Disposition", "Revision", "Words", "Why"],
          [[a, b, c, str(w), e] for a, b, c, w, e in R.MR],
          widths=[1.4, 1.2, 0.85, 0.5, 2.75])

    page_break(d)
    h(d, "V20 against MR5, line by line")
    table(d, ["", "V20 source, old V25", "MR5 master", "Read"],
          [[a, b, c, e] for a, b, c, e in R.V20_MR5],
          widths=[0.95, 1.8, 1.8, 2.15])
    callout(d, R.V20_MR5_VERDICT)

    page_break(d)
    h(d, "V21 against MR2, MR6 and MR8")
    caption(d, "The unique job each episode performs, before any merge.")
    table(d, ["", "Title", "Viewer state", "What it teaches", "What is unique to it"],
          [[a, b, c, e, f] for a, b, c, e, f in R.IC_JOBS],
          widths=[0.5, 1.5, 1.3, 1.9, 1.5])
    for name, conf, why in R.IC_VERDICT:
        sub(d, "%s  ·  %s" % (name, conf))
        para(d, why)

    page_break(d)
    h(d, "Duplication map across V4 to V21 and the Missing Rung")
    table(d, ["Pair", "Verdict", "What it means"],
          [[a, b, c] for a, b, c in R.DUPES], widths=[2.1, 1.5, 3.1])

    page_break(d)
    h(d, "Recommended post-V14 public sequence")
    table(d, ["#", "Title", "Thumbnail", "Source", "Note"],
          [[s["n"], s["title"], s["thumb"], s["src"], s["note"]]
           for s in S.SEQ], widths=[0.55, 1.85, 1.25, 1.0, 2.05])

    h(d, "Missing Rung playlist order")
    table(d, ["Playlist", "Public", "Source", "Job in the journey"],
          [[a, b, c, e] for a, b, c, e in S.PLAYLIST],
          widths=[0.7, 0.7, 1.2, 4.1])
    para(d, S.PLAYLIST_NOTE)

    page_break(d)
    h(d, "Consecutive, interleaved, or tested")
    for name, why in S.CONSECUTIVE:
        sub(d, name)
        para(d, why)

    page_break(d)
    h(d, "Watch Next map")
    table(d, ["From", "To", "Why, and what changes"],
          [[a, b, c] for a, b, c in S.WATCH_NEXT], widths=[1.0, 0.9, 4.8])
    caption(d, "Three of the masters' own Watch Next lines break under the "
               "merges and are marked CHANGED above. Three inbound routes "
               "from locked audio cannot change at all.")

    h(d, "Artifact and Watch-Me-Read map")
    table(d, ["#", "Artifact", "What it would be"],
          [[a, b, c] for a, b, c in S.ARTIFACTS], widths=[0.5, 1.7, 4.5])
    para(d, S.ARTIFACT_NOTE)

    page_break(d)
    h(d, "Evidence and provenance gaps")
    table(d, ["Issue", "Severity", "What it means"],
          [[a, b, c] for a, b, c in S.EVIDENCE], widths=[2.0, 1.2, 3.5])

    h(d, "Commercial and CTA map")
    table(d, ["#", "Offer", "Why"],
          [[a, b, c] for a, b, c in S.CTA], widths=[0.5, 1.85, 4.35])
    para(d, S.CTA_NOTE)

    page_break(d)
    h(d, "Packaging conflicts")
    table(d, ["Conflict", "Status", "Recommendation"],
          [[a, b, c] for a, b, c in S.PACKAGING], widths=[1.9, 1.3, 3.5])

    h(d, "Named and countable structures to de-frame")
    table(d, ["Structure", "Verdict", "What to do"],
          [[a, b, c] for a, b, c in S.DEFRAME], widths=[2.0, 1.3, 3.4])

    page_break(d)
    h(d, "Revision level for every surviving future video")
    table(d, ["#", "Level", "The single reason"],
          [["V15", "MODERATE", "Two competing four-line structures to remove "
            "and a CTA pointed at the wrong offer."],
           ["V16", "MODERATE", "The hinge is buried while the first half "
            "re-teaches locked V5 and V12."],
           ["V17", "SUBSTANTIAL", "Most of the source is locked V8's "
            "material. Re-scope, do not revise."],
           ["V18", "MODERATE", "A named five-layer inventory and an opening "
            "that re-teaches locked V13."],
           ["V19", "MODERATE", "Excellent material on a named three-part "
            "structure, with one leg that is locked V12's whole video."],
           ["V20", "SUBSTANTIAL", "407 words against a %s band, minus the "
            "org-chart paragraph and the twelve-month question it gives up."
            % D.LOCKED_BAND],
           ["V21", "SUBSTANTIAL", "290 words, the shortest but one, and it "
            "also absorbs retired old V29's territory."],
           ["V22", "SUBSTANTIAL", "331 words, plus it gains the roadmap's "
            "most demanding artifact and MR1's structural paragraph."],
           ["V23", "SUBSTANTIAL", "262 words, the shortest in the series, "
            "merged with a 775-word source. The largest single build."],
           ["V24", "SUBSTANTIAL", "315 words merged with the strongest source "
            "in the V15 to V21 slate, which has to be de-framed on the way in."],
           ["V25", "SUBSTANTIAL", "295 words, and its evidence beat has to "
            "point at locked V8 rather than rebuild it."],
           ["V26", "SUBSTANTIAL", "A genuine merge of two masters into one "
            "recognition-to-decision arc, 768 words before de-duplication."]],
          widths=[0.5, 1.2, 5.0])
    caption(d, "Nothing is LIGHT. The V15 to V21 audit rated old V18, now "
               "inside V24, as LIGHT. Nothing else in either slate is.")

    h(d, "Decisions needed before rewriting")
    for name, state, why in S.DECISIONS:
        sub(d, "%s  ·  %s" % (name, state))
        para(d, why)
    callout(d, "Six are blocking. The three merges settle all downstream "
               "numbering, the test block settles the schedule, and nothing "
               "in the Missing Rung can be written until its source report is "
               "in the workspace.")
    footer_note(d, "Architecture only. No script rewritten, no V4 to V14 file "
                   "changed, no new research, no artifact or URL invented.")
    d.save(path)

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
