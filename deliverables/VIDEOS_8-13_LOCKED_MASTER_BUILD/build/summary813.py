# -*- coding: utf-8 -*-
"""Delivery summary and a scoped V8 to V13 roadmap/tracker patch.

The patch is written as its own file rather than applied to the shared tracker,
so this batch never writes to a file the V4 to V7 task also owns.
"""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, DELIV + "riverside-build")
sys.path.insert(0, DELIV + "new-videos-4-5/build")
sys.path.insert(0, HERE)
import masters813 as M, frames813 as F, shorts813 as SH, publish813 as P
import build813 as B
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)

PENDING = [
 ("Thumbnail artwork, all six videos",
  "The WORDING is locked and is in every package. No artwork was created, no "
  "portrait was selected, and Temidayo's face was not regenerated or altered. "
  "Each 06_Publishing folder has a Canva brief ready to hand over. Artwork and "
  "portrait approval are PENDING."),
 ("YouTube URLs and the playlist URL",
  "No video ID and no playlist URL was supplied to this build, so none is "
  "invented. Every Watch Next link and the playlist line is a marked "
  "placeholder. The playlist is Make Your Next Move Without Starting Over; do "
  "not assume an older shortened identifier is correct."),
 ("Watch Next scheduling dependency",
  "Each video's Watch Next destination must be publicly accessible to viewers "
  "when that video publishes. A scheduled destination that is still private is "
  "not publicly accessible. V13 routes back to V9, so V9 must be public before "
  "V13 goes out. Flag the dependency rather than changing the approved spoken "
  "handoff."),
 ("V11 live demonstration capture",
  "Optional and separate. The prepared AI-assisted summary supplied in the "
  "components archive was used as a designed reconstruction and is labelled as "
  "one. If Temidayo wants a real capture, she runs the supplied CSV and prompt "
  "in her approved account, saves the actual response, date and model shown, "
  "screen-records it, and the script is reconciled to that real response. Not "
  "required to complete these reference assets."),
 ("Music",
  "No track, artist or license code appears anywhere. Add attribution only "
  "when the real track and license from the finished project are known."),
 ("Chapters",
  "None supplied. Build them from the actual final export."),
]

FLAGGED = [
 ("Speech-only estimates sit below every printed cover target",
  "Not a defect, but worth seeing before the recording day. The printed "
  "targets were expectations set before the scripts were finalized. At 130 to "
  "145 words per minute the six scripts estimate roughly one to two minutes "
  "short of their printed ranges. Holds on full-screen graphics, B-roll and "
  "pauses will close some of that, and narration continuing underneath a "
  "visual overlaps rather than adds. Nothing was padded and no removed "
  "material was restored."),
 ("Video 12's title uses a typographic apostrophe",
  "The locked master spells it What to Do When You Can’t Quit Your Job Yet "
  "with a curly apostrophe. Every title field, Watch Next reference and the "
  "V11 Watch Next card was aligned to the master's exact typography rather "
  "than a straight apostrophe. Worth knowing when the title is pasted into "
  "YouTube."),
]


def rows():
    out = []
    for n in M.VIDEOS:
        m = P.META[n]
        w, fast, slow = M.estimate(n)
        out.append((n, m, w, fast, slow))
    return out


def build_doc():
    doc = base_doc()
    title_block(doc, "Capability Formation  |  Videos 8 to 13",
                "Production Build Delivery Summary",
                "Built from the locked final Recording Masters")
    kv(doc, "Date", "September 9, 2026")
    kv(doc, "Scope", "Videos 8, 9, 10, 11, 12 and 13")
    kv(doc, "Primary source",
       "YouTube_Videos_8-13_Final_Recording_Masters, six final masters")
    kv(doc, "Secondary source",
       "Videos_8-13_Recording_and_Production_Components_v1.0, used for "
       "concepts and drafts only")
    kv(doc, "Batch directory", "deliverables/VIDEOS_8-13_LOCKED_MASTER_BUILD/")
    callout(doc, "This is the FIRST Code production build for Videos 8 to 13. "
                 "No earlier V8 to V13 build prompt was executed, and no "
                 "previously rendered V8 to V13 asset existed. The scripts, "
                 "titles and thumbnail wording are locked and approved; "
                 "nothing here reopens editorial strategy.")

    h(doc, "1. How the locked masters were handled")
    para(doc, "Each master's SHA-256 was recorded before anything was "
              "generated, and an unchanged copy sits in each video's "
              "01_Recording_Master folder. The build reads those files and "
              "never writes to them: the reading copy, the run of show, the "
              "trigger map and the word counts are all generated from the "
              "locked text, so there is no transcription step in which a line "
              "could drift.", size=11, after=8)
    para(doc, "The spoken section is taken between RECORDING SCRIPT STARTS "
              "HERE and END OF SPOKEN SCRIPT. Section headings, production "
              "labels and the closing instruction about not reading the line "
              "are excluded from the spoken word count and are marked as "
              "production notes in the reading copy.", size=11, after=8)
    for n, m, w, fast, slow in rows():
        kv(doc, "V%d  %s" % (n, M.FILE[n]), "SHA-256 %s" % M.sha256(n))

    h(doc, "2. The six videos as built")
    for n, m, w, fast, slow in rows():
        para(doc, "VIDEO %d  ·  %s" % (n, m["title"]), size=12, bold=True,
             color=NAVY, before=14, after=5, keep=True)
        kv(doc, "Thumbnail wording", "%s   (artwork PENDING)" % m["thumb"])
        kv(doc, "Framework", m["framework"])
        kv(doc, "Resource, one route", "%s   %s" % m["resource"])
        kv(doc, "Watch Next", "Video %d, %s" % m["watch_next"])
        kv(doc, "Spoken words", "%d" % w)
        kv(doc, "Speech-only estimate",
           "%s to %s at 130 to 145 wpm. Estimate, not a measurement." % (fast, slow))
        kv(doc, "Printed cover target",
           "%s. An expectation, not a measured length."
           % M.header(n).get("TARGET LENGTH", ""))
        kv(doc, "Built", "%d teaching concepts, a resource card and a Watch "
                         "Next card. 6 dedicated Shorts, 4 Priority A and 2 "
                         "Priority B." % (len(F.SETS[n]) - 2))

    h(doc, "3. Routing and packaging corrections")
    para(doc, "Routing is V8 to V9 to V10 to V11 to V12 to V13, and V13 back "
              "to V9. This is specified in the new approved masters.",
         size=11, after=8)
    para(doc, P.SUPERSEDED, size=10.5, color=DIM, after=8)
    para(doc, "The corrected V9 title was propagated into V8's and V13's Watch "
              "Next cards, descriptions, prompts and manifests. None of the "
              "superseded lines appears as active packaging anywhere; each "
              "survives only in the record that documents its replacement, "
              "which the QA allows by design.", size=11, after=8)

    h(doc, "4. Assets are new builds, not carried-over artwork")
    para(doc, "No prior rendered V8 to V13 artwork exists. All 54 PNGs in this "
              "batch are new builds from reusable concepts taken from the "
              "earlier components archive, with every anchor remapped to the "
              "locked script. The earlier asset specifications were proposed "
              "build specifications, not finished graphics, and are not "
              "presented as such.", size=11, after=8)
    para(doc, "Eight frames carry a required on-screen label: SYNTHETIC DATA "
              "and PREPARED AI-ASSISTED EXAMPLE on the three Video 11 data "
              "frames, ILLUSTRATION, NOT A REAL CASE on the four hypothetical "
              "examples, and A WORK SAMPLE, NOT PROFESSIONAL EXPERIENCE on "
              "Video 13's third-week frame. Each is a full-width stamp rather "
              "than a footer, so it stays readable at phone size.",
         size=11, after=8)

    h(doc, "5. The Video 11 arithmetic")
    para(doc, "Recomputed independently from the supplied synthetic rows and "
              "reconciled with the supplied Arithmetic_Check.json. The "
              "aggregate rate rises from 60 percent to 80 percent, a rise of "
              "20 PERCENTAGE POINTS. Relative growth would be 33.3 percent, "
              "which is why every asset says percentage points. Routine cases "
              "hold at 90 percent and complex cases at 40 percent in both "
              "periods; the routine share moves from 40 percent to 80 percent.",
         size=11, after=8)
    para(doc, "The prepared AI-assisted summary correctly identifies the "
              "changed mix, and the package says so. No AI failure is staged, "
              "no claim is made that humans uniquely notice the caveat, and no "
              "live benchmark, product interface, model name or speed result "
              "is fabricated.", size=11, after=8)

    h(doc, "6. QA is split")
    kv(doc, "Package checks completed now", "20 per video, all passing")
    kv(doc, "Final-export checks still pending", "12 per video, none claimed")
    para(doc, "Mobile readability was inspected, not asserted: every frame was "
              "measured against the rendered DOM for overlap, caption-zone and "
              "safe-edge violations, then rendered into a 390-point-wide "
              "contact sheet in each 03_Visuals folder and read at that size.",
         size=11, after=8)
    para(doc, "No earlier draft-bundle QA is reused as evidence, and the "
              "earlier script-approval-pending status does not apply.",
         size=11, after=8)

    h(doc, "7. Videos 1 to 7 were not touched")
    para(doc, "This batch writes only inside VIDEOS_8-13_LOCKED_MASTER_BUILD. "
              "It uses the shared render engine read-only and adds no "
              "parameter to it; batch-specific layouts live in the batch. "
              "Verified: all 39 V4 to V7 assets still re-render "
              "byte-identically, and no file in the V4 to V7 packages, the "
              "Videos 1 to 3 slide folders, or the shared render engine was "
              "modified.", size=11, after=8)

    h(doc, "8. Still pending")
    for name, body in PENDING:
        kv(doc, name, body)

    h(doc, "9. Flagged for your attention")
    for name, body in FLAGGED:
        kv(doc, name, body)

    h(doc, "10. Deliverables")
    for n in M.VIDEOS:
        kv(doc, "V%d_Production_Package.zip" % n,
           open(os.path.join(ROOT, "V%d_Production_Package.zip.sha256" % n)
                ).read().split()[0])
    kv(doc, "Videos_8-13_Production_Packages.zip",
       open(os.path.join(ROOT, "Videos_8-13_Production_Packages.zip.sha256")
            ).read().split()[0])
    kv(doc, "V8-V13_BATCH_MANIFEST.md", "Batch manifest")
    kv(doc, "V8-V13_ROADMAP_TRACKER_PATCH.md",
       "A scoped patch for the shared roadmap and tracker, prepared as its own "
       "file rather than written into the shared documents, so this batch "
       "never writes to a file the V4 to V7 task also owns.")

    rule(doc)
    para(doc, "V8 TO V13 PRODUCTION PACKAGES BUILT AGAINST LOCKED FINAL "
              "MASTERS.", size=12, bold=True, color=NAVY, before=10, after=4)
    para(doc, "READY FOR RECORDING AND RIVERSIDE PRODUCTION.", size=12,
         bold=True, color=NAVY, after=4)
    para(doc, "FINAL-EXPORT QA AND THUMBNAIL ARTWORK APPROVAL PENDING.",
         size=12, bold=True, color=RED, after=8)
    p = os.path.join(ROOT, "V8-V13_DELIVERY_SUMMARY.docx")
    doc.save(p)
    return p


PATCH = """# V8 to V13 roadmap and tracker patch

**Scoped to the V8 to V13 entries only.** Prepared as its own file and
deliberately NOT written into `SERIES_STATUS_TRACKER.md` or
`roadmap/README.md`, so this batch never writes to a shared file the V4 to V7
task also owns. Apply it when convenient.

## Proposed tracker section

### September 9, 2026 — Videos 8 to 13 production packages built

First Code production build for Videos 8 to 13, from the six supplied final
Recording Masters. Scripts, titles and thumbnail wording were already approved
and locked; this build wrapped production packages around them and did not
reopen editorial strategy.

| # | Title | Thumbnail | Resource | Watch Next | Words | Speech-only estimate |
|---|---|---|---|---|---|---|
%s

Routing: **V8 to V9 to V10 to V11 to V12 to V13, and V13 back to V9**, as
specified in the approved masters.

**Packaging corrections applied.** V9's primary title is now *How to Change
Industries Without Starting Over*, replacing *Before You Change Industries,
Know What Still Counts*, and the change was propagated into V8's and V13's
Watch Next cards and copy. V11's thumbnail is **THE TASK ISN'T THE JOB**,
replacing *WHAT STILL NEEDS YOU?*. V12's is **WHAT CAN CHANGE NOW?**, replacing
*STUCK FOR NOW?*. No numbering changed.

**Assets are new builds.** No prior rendered V8 to V13 artwork existed, so all
54 PNGs are new builds from reusable concepts, not byte-identical reuse.

**QA** is 20 package checks per video completed now, all passing, and 12
final-export checks per video listed as pending and not claimed.

**Pending:** thumbnail artwork and portrait selection for all six; YouTube and
playlist URLs; the Watch Next scheduling dependency, with V9 needing to be
public before V13 publishes; the optional V11 live demonstration capture;
music; chapters.

**V8 TO V13 PRODUCTION PACKAGES BUILT AGAINST LOCKED FINAL MASTERS. READY FOR
RECORDING AND RIVERSIDE PRODUCTION. FINAL-EXPORT QA AND THUMBNAIL ARTWORK
APPROVAL PENDING.**

## Roadmap entries to update

Only the V8 to V13 rows. **V14's research condition and every later roadmap
decision are preserved unchanged**: V14 remains conditional on research being
actually completed and documented, V13 remains a plan rather than a completed
experiment, and V11's tool and task-capability claims remain subject to
verification before scripting. V14 to V30 were not started and are not
affected.
"""


def patch_rows():
    out = []
    for n in M.VIDEOS:
        m = P.META[n]
        w, fast, slow = M.estimate(n)
        out.append("| **V%d** | %s | %s | %s | Video %d | %d | %s to %s |"
                   % (n, m["title"], m["thumb"], m["resource"][0],
                      m["watch_next"][0], w, fast, slow))
    return "\n".join(out)


if __name__ == "__main__":
    p = build_doc()
    print("wrote", p)
    q = os.path.join(ROOT, "V8-V13_ROADMAP_TRACKER_PATCH.md")
    open(q, "w").write(PATCH % patch_rows())
    print("wrote", q)
