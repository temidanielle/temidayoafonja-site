# -*- coding: utf-8 -*-
"""The Markdown change log and the scoped, unapplied roadmap/tracker patch."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import baseline


def change_log(stamp):
    rm = baseline.roadmap_slots()
    rf = baseline.refinement_slots()
    L = []
    A = L.append
    A("# Videos 14 to 21: editorial development change log")
    A("")
    A("Created: %s" % stamp)
    A("")
    A("Planning and editorial-brief work only. No script, package, asset,")
    A("thumbnail, deck or routing decision was created, changed or approved.")
    A("")
    A("## What was produced")
    A("")
    A("| File | What it is |")
    A("|---|---|")
    A("| `Videos_14-21_Roadmap_Addendum.docx` | Scoped roadmap addendum: the "
      "one proposed slot change, the preserved slots, the overlap check, the "
      "forward queue, and the sources. |")
    A("| `Videos_14-21_Development_Briefs.docx` | Eight slot briefs plus the "
      "reserved employer due-diligence brief. |")
    A("| `CHANGE_LOG.md` | This file. |")
    A("| `ROADMAP_TRACKER_PATCH.md` | A scoped patch for the locked roadmap "
      "and the series tracker. **Not applied.** |")
    A("| `build/` | The scripts that generated the two documents, so both can "
      "be rebuilt from the same two sources. |")
    A("")
    A("## The single editorial change proposed")
    A("")
    A("Slot 15 substitution. Everything else in the range is preserved.")
    A("")
    A("| # | Locked September 9 entry | Proposed planning label | Change |")
    A("|---|---|---|---|")
    for n in range(14, 22):
        note = {
            14: "No topic change. Planning label reverts to the descriptive "
                "title, per the roadmap's own evidence gate.",
            15: "**CHANGED.** New topic proposed. After-40 topic moves to the "
                "forward queue, undeleted.",
            18: "No change. Title punctuation variance recorded, not resolved.",
        }.get(n, "No change.")
        A("| V%d | %s | %s | %s |" % (n, rm[n][0], rf[n][0], note))
    A("")
    A("## What was not touched")
    A("")
    A("- Videos 1 to 13: scripts, assets, thumbnails, Shorts, publishing copy, "
      "routing.")
    A("- The closed V4 to V7 September 9 synchronization.")
    A("- The existing V8 to V13 production files.")
    A("- The channel banner and every unrelated shared project file.")
    A("- The website, the book page, the products and the global styles.")
    A("- `deliverables/roadmap/YouTube_Roadmap_1-30_LOCKED_Sep09_2026.docx`. "
      "Read only. Its checksum still matches its own lock file:")
    A("  `%s`" % baseline.verify_roadmap())
    A("- V22, V23 to V30 and the V31 capstone. No later number is shifted, "
      "because the one change is a substitution inside slot 15, not an "
      "insertion.")
    A("")
    A("## What is deliberately absent")
    A("")
    A("Full recording scripts. Script-only recording copies. Shorts scripts. "
      "Final publishing copy. Final thumbnail artwork. Slide decks. "
      "Motion-graphic assets. Final Riverside production prompts. Final "
      "chapters or invented video URLs. None of these was requested, and none "
      "of these exists for Videos 14 to 21.")
    A("")
    A("## Claims deliberately not made")
    A("")
    A("- No script in this range is called locked, because none is written.")
    A("- The V14 research is **not** complete. What exists is a research plan "
      "inside the V14 brief.")
    A("- No search volume, competition level, trend direction or performance "
      "prediction is stated anywhere, from TubeBuddy or any other source.")
    A("- Nothing here claims that nobody covers a topic, that a video will own "
      "a search, that there is no competition, that a video will outperform, "
      "or that an audience-match score proves demand.")
    A("- The reserved employer due-diligence brief has **no** slot number, and "
      "none is proposed.")
    A("")
    A("## Open items handed back")
    A("")
    A("1. Approve or reject the slot 15 substitution.")
    A("2. If approved, decide the new slot 15 thumbnail copy. The existing "
      "line `UPDATE. DON’T ERASE.` travels with the after-40 topic and is not "
      "reassigned.")
    A("3. If approved, decide the new slot 15 resource route. The Field Kit "
      "route on that slot was carried for the previous topic.")
    A("4. Resolve the slot 18 title punctuation variance at packaging time.")
    A("5. Decide where the reserved employer due-diligence brief eventually "
      "sits, given that V22 and V23 keep their positions.")
    A("6. Decide whether the employer due-diligence brief needs a legal review "
      "pass before scripting.")
    A("")
    A("## Status")
    A("")
    A("V14 to V21 WORKING ROADMAP REFINEMENT DOCUMENTED. DEVELOPMENT BRIEFS "
      "READY FOR EDITORIAL REVIEW. SCRIPTS, FINAL PACKAGING, ROUTING, AND "
      "PRODUCTION ASSETS NOT YET APPROVED.")
    A("")
    return "\n".join(L)


def patch(stamp):
    rm = baseline.roadmap_slots()
    rf = baseline.refinement_slots()
    L = []
    A = L.append
    A("# Scoped roadmap and tracker patch for Videos 14 to 21")
    A("")
    A("Prepared: %s" % stamp)
    A("")
    A("**STATUS: NOT APPLIED.** This patch exists so the change can be "
      "reviewed before anything locked is edited. Applying it is a separate "
      "decision. Nothing in this file has been written into the roadmap or "
      "the tracker.")
    A("")
    A("Target files, neither of which was modified:")
    A("")
    A("- `deliverables/roadmap/YouTube_Roadmap_1-30_LOCKED_Sep09_2026.docx`")
    A("  SHA-256 `%s`" % baseline.verify_roadmap())
    A("- `deliverables/SERIES_STATUS_TRACKER.md`")
    A("")
    A("---")
    A("")
    A("## Patch 1. Roadmap section 2, the V14 and V15 rows")
    A("")
    A("Two rows change in the `Outlier-informed next run` table. Nothing else "
      "in that table moves.")
    A("")
    A("**Replace the V14 row**")
    A("")
    A("```")
    A("V14 | %s | %s | %s" % rm[14])
    A("```")
    A("")
    A("**with**")
    A("")
    A("```")
    A("V14 | %s | %s | Conditional on actual research; descriptive planning "
      "title retained" % (rf[14][0], rm[14][1]))
    A("```")
    A("")
    A("The topic does not change. This makes the printed label match the "
      "V14 EVIDENCE GATE box the same document already carries immediately "
      "after that table.")
    A("")
    A("**Replace the V15 row**")
    A("")
    A("```")
    A("V15 | %s | %s | %s" % rm[15])
    A("```")
    A("")
    A("**with**")
    A("")
    A("```")
    A("V15 | %s | thumbnail copy not yet decided | Proposed placement; "
      "direction under review" % rf[15][0])
    A("```")
    A("")
    A("`UPDATE. DON’T ERASE.` is not reassigned. It travels with the after-40 "
      "topic into the forward queue.")
    A("")
    A("## Patch 2. Roadmap section 5, the V15 treatment block")
    A("")
    A("The existing `VIDEO 15 | How to Stay Relevant After 40 Without Chasing "
      "Every Trend` treatment block is **kept, not deleted**, and relabeled as "
      "a forward-queue topic with no number assigned. A new treatment block "
      "for the proposed slot 15 topic is **not** written into the roadmap "
      "yet, because the placement is a proposal. The development brief in "
      "`Videos_14-21_Development_Briefs.docx` carries it in the meantime.")
    A("")
    A("## Patch 3. Roadmap resource-route sentence")
    A("")
    A("The carried sentence lists `V9, V11, V13, V14 and V15: Field Kit`. If "
      "the substitution is approved, V15 leaves that list and becomes "
      "undecided until the script exists. V14 stays.")
    A("")
    A("## Patch 4. Roadmap, new forward-queue paragraph")
    A("")
    A("Add after the reserved-capstone paragraph in section 4:")
    A("")
    A("> Forward queue, no numbers assigned: How to Stay Relevant After 40 "
      "Without Chasing Every Trend, displaced from slot 15 and preserved with "
      "its thumbnail line and Field Kit route. Before You Accept the Job, Find "
      "Out How the Company Actually Uses People Like You, the reserved "
      "employer due-diligence brief. A distinct job-security brief. A "
      "when-to-leave brief, or that theme used as research input to V25.")
    A("")
    A("## Patch 5. Series status tracker, new section")
    A("")
    A("Add a dated section recording that the V14 to V21 planning work exists, "
      "that it is a proposal, and that no script or asset was produced. "
      "Suggested text:")
    A("")
    A("> ### %s: Videos 14 to 21 editorial development" % stamp.split(" | ")[0])
    A(">")
    A("> Planning only. A scoped roadmap addendum and nine development briefs "
      "were prepared in `deliverables/V14-V21_EDITORIAL_DEVELOPMENT/`. One "
      "slot change is proposed: the judgment-gap topic at V15, with the "
      "after-40 topic preserved in the forward queue and no number reassigned. "
      "Videos 1 to 13 were not touched. No script, deck, Short, thumbnail, "
      "Riverside prompt or routing decision was created or changed. The V14 "
      "research gate is still open and the research has not been done.")
    A("")
    A("---")
    A("")
    A("## Also still unapplied, from the previous batch")
    A("")
    A("`deliverables/VIDEOS_8-13_LOCKED_MASTER_BUILD/V8-V13_ROADMAP_TRACKER_"
      "PATCH.md` remains prepared and unapplied, together with the stale "
      "tracker sentence that still calls V8 to V13 a draft batch. This task "
      "did not apply it, because applying it was not requested and it touches "
      "a closed batch's records.")
    A("")
    return "\n".join(L)
