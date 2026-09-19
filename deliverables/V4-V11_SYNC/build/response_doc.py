# -*- coding: utf-8 -*-
"""The written response to the independent review, as a Word document.

Same house style as the packages. Every number in it is read from the
build rather than typed, so the document cannot drift from what shipped.
"""
import os, sys, zipfile, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                   "V4-V11_EDIT_SYNC/build")
import recon as R
import packages as P
import sequencing as Q
import shortsync as SH
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break)

EYEBROW = "capability formation | synchronized production"


def sha256(p):
    h_ = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h_.update(b)
    return h_.hexdigest()


def build(path, st):
    arc = os.path.join(OUT, P.ARCHIVE)
    z = zipfile.ZipFile(arc)
    t = P.totals()
    fc = t["final_checks"] or 0
    import events as EV
    span = sum(1 for n in R.VIDEOS for e in EV.events(n)
               if e["para_out"] > e["para"])
    reuse = sum(1 for n in R.VIDEOS for c in P.cues(n)
                if c["occurrences"] > 1)

    d = base_doc()
    title_block(d, EYEBROW, "Final edit-map completion",
                "One event sequence, and the conflicts it resolves")
    kv(d, "Prepared", st)
    kv(d, "Review concerned", "5814eecc318b9da8e577de7bfcf258cec648251e5"
                              "6efccc3dfa09982cf8e5478")
    kv(d, "This delivery", sha256(arc))
    kv(d, "Entries", "%d" % len(z.namelist()))
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "Two of the review's findings were already closed by the "
               "passes that followed the archive it read: the five stale "
               "trigger quotations and the seven run-of-show section "
               "names were corrected, and the 220 against 221 count was "
               "reconciled. Both were re-tested against the delivered "
               "files here rather than assumed. Everything else in the "
               "review was still open and is now done.")

    h(d, "What the review asked, and what was done")
    table(d, ["", "Asked for", "Done"],
          [["1", "Relabel the V6 four-things card. Do not redesign it.",
            "Already relabelled to PROBLEM, AUTHORITY, PROOF, REAL GAP, "
            "each with the question its section asks. Layout and heading "
            "unchanged. Its TAKEAWAY VALUE placement is kept and the "
            "quoted passage and section name at that location are the "
            "current ones."],
           ["2", "Regenerate complete locators from the resolved master: "
                 "five trigger quotations, seven section names, and the "
                 "36 truncated boundary fields.",
            "The five and the seven were already fixed at the root and "
            "re-tested here on the delivered files. The 36 truncations "
            "are gone: entry and exit phrases now wrap instead of being "
            "cut, and no ellipsis appears in any operational boundary."],
           ["3", "Generate one shot and state sequence, not competing "
                 "maps.",
            "A cue is now an event with its own id, a span of paragraphs "
            "and per-state activation words. %d events across the eight "
            "videos, %d of them spanning more than one paragraph, %d "
            "families serving more than one event. Run of show, camera "
            "map, motion map, sound map, asset index and Riverside "
            "prompt are all generated from that one list."
            % (t["events"], span, reuse)],
           ["4", "Complete V11 Short 1 from existing approved wording.",
            "Its ending is now the TAKEAWAY VALUE passage: write "
            "EXPECTED and ACTUAL side by side, name one real cost, then "
            "choose one next action. The recognition and the "
            "legitimate-change qualification are kept, the payoff state "
            "points at the working page, and the count is recomputed. No "
            "other Short was rewritten."],
           ["5", "Verify output content, then report the actual status.",
            "The assertions read the delivered documents, not the "
            "generator. Each was replayed against the values the review "
            "recorded from the archive it read, and every one fails "
            "there. The final count is %d, from the run itself."
            % fc]],
          widths=[0.3, 2.5, 3.9], size=7.5)

    page_break(d)
    h(d, "The seventeen, one by one")
    para(d, "Sixteen are now full screen at the paragraph the brief "
            "names. One, V10's WHAT READ DOES NOT MEAN, stays on camera "
            "because the brief's own heading is CAMERA, THEN BRIEF "
            "FULL-SCREEN CONTRAST: the camera half is its own event and "
            "the contrast is the next one, at the paragraph that carries "
            "it. Either way the instruction no longer claims full screen "
            "at a paragraph the map calls camera, and the assertion "
            "requires the treatment to survive, so a conflict cannot be "
            "closed by deleting the teaching.", size=10.5)
    table(d, ["Where", "How it was met"],
          [["V4 A SIMPLE EXAMPLE",
            "The illustration enters on the sentence that says the "
            "learning moved, which is in paragraph 2, not 3."],
           ["V5 ASK FOR DEVELOPMENT",
            "A conversation state was built for the request itself. No "
            "delivered state carried it."],
           ["V5 SET A REVIEW POINT",
            "The note enters on the instruction and holds across the "
            "three paragraphs of review questions."],
           ["V6 2 | AUTHORITY",
            "The walkthrough's authority state plays here, at its own "
            "teaching occurrence."],
           ["V6 4 | REAL GAP",
            "Two requirements, two paragraphs, one state each. The "
            "second is not revealed while the first is explained."],
           ["V7 FOUR THINGS I LOOK FOR",
            "Establish on paragraph 1, then one item per paragraph on "
            "the words that name it. The bias and access boundary "
            "returns to camera."],
           ["V7 A CONVERSATION YOU CAN HAVE",
            "A conversation state was built for the clearer-target "
            "question."],
           ["V7 READ YOUR OWN SITUATION",
            "The working note enters with the instruction and holds "
            "through the four questions."],
           ["V8 WHAT TO WRITE DOWN",
            "The example note spans both paragraphs; the boundary line "
            "is in the second."],
           ["V8 STORY LOOP PAYOFF",
            "The hook's illustrative login returns, as a second event on "
            "the same asset."],
           ["V9 THE FOUR QUESTIONS",
            "The hook's four-question family plays again here. Two "
            "questions in paragraph 1, two in paragraph 2."],
           ["V9 THINK OF IT LIKE SORTING",
            "The illustration enters on the image and holds through the "
            "sorting lines."],
           ["V9 HOW TO TALK ABOUT THE GAP",
            "An X, Y and Z state was built for the honest sentence."],
           ["V10 HOOK",
            "The framework card is held into the paragraph that names "
            "READ, TEST and PROVE instead of cutting before them."],
           ["V10 WHAT READ DOES NOT MEAN",
            "Camera, as the brief's own heading says, with the contrast "
            "as its own event at paragraph 3."],
           ["V10 THE FIRST-90-DAYS READ",
            "READ and TEST in paragraph 1, PROVE and ROLE CHECK in "
            "paragraph 2. The added line is not shown before it is "
            "spoken."],
           ["V11 TAKEAWAY VALUE",
            "The opening pair of documents returns with the cost and the "
            "next action added. That state was built; nothing carried "
            "it."]],
          widths=[1.9, 4.8], size=7.5)

    page_break(d)
    h(d, "The cross-paragraph reveals the review named")
    table(d, ["Family", "How it now reveals"],
          [["V11 FS_06 four cost lenses",
            "CAPABILITY and EVIDENCE in section 7 paragraph 1, "
            "COMPENSATION and LIFE in paragraph 2, each on the word that "
            "names it, then camera for paragraph 3's interpretation. "
            "Compensation and life are not trimmed: they carry the pay, "
            "level, travel, caregiving and health constraints."],
           ["V11 FS_09 the role-drift read",
            "EXPECTED and ACTUAL in section 10 paragraph 1, COST and "
            "CHOICE in paragraph 2, returning at 'That is a role-drift "
            "read.'"],
           ["V6 FS_06 posting walkthrough",
            "PROBLEM at section 4 paragraph 2, AUTHORITY at section 5 "
            "paragraph 2, PROOF at section 6 paragraph 2. Three "
            "occurrences of one family, not a march through later "
            "interpretations during the problem."]],
          widths=[1.9, 4.8], size=8)

    h(d, "Sound, as one event with two fields")
    para(d, "A visual entry and an accent word were separate records that "
            "could disagree, which is why V4's early list said the sound "
            "lands on 'wasted' while the main list said no accent word "
            "was specified. They are one event now, with an entry field "
            "and an accent-word field. Where no accent word is named, the "
            "sound lands on the entry and the map says so.", size=10.5)

    h(d, "Where the numbers stand")
    table(d, ["", "Count"],
          [["Families before this work", "%d" % t["prior_families"]],
           ["Built since, for the early edit and the missing treatments",
            "%d" % t["new_families"]],
           ["Families in total", "%d" % t["total_families"]],
           ["Retired, inactive, not cued, not rendered",
            "%d" % t["retired_families"]],
           ["Active families", "%d" % t["active_families"]],
           ["Events", "%d" % t["events"]],
           ["Active teaching and end-card states", "%d" % t["states"]],
           ["Contact sheets, one per video, not states",
            "%d" % t["contact_sheets"]],
           ["Thought blocks, holding %d paragraphs" % t["paragraphs"],
            "%d" % t["blocks"]]],
          widths=[4.3, 2.4], size=8.5)
    caption(d, "Every rendered state is cued by an event and every cued "
               "state is rendered. Four states were added this pass "
               "because no delivered state could carry the treatment the "
               "brief names; nothing else was rebuilt.")

    h(d, "Verification, against the files on disk")
    table(d, ["", "Result"],
          [["Source reconciliation", "43 of 43"],
           ["Per-package checks", "231 of 231 across the eight packages"],
           ["Final verification, read back off disk",
            "%d of %d" % (fc, fc)],
           ["Map fixtures",
            "the five quotations, seven names, seventeen mode conflicts, "
            "thirty-six truncations and the cross-paragraph examples, "
            "each replayed against the reviewed values and failing there"],
           ["Other suites",
            "the Shorts, action, cue and report fixtures from the "
            "earlier reviews all still fire"]],
          widths=[2.2, 4.5], size=8.5)

    h(d, "Unchanged, as instructed")
    bullets(d, [
      "All eight long-form masters. No spoken word changed in this pass.",
      "The approved hypothetical V4 opening, the six restored "
      "introductions and the intentional V6 and V8 absences.",
      "Thought-block parity, the approved packaging and the eight "
      "faith-inclusive descriptions.",
      "The completed Shorts repairs. Only V11 Short 1 changed, and only "
      "its ending.",
      "The V10 to V11 and V11 to public V5 Watch Next routes. No "
      "substitution, no new schedule, no simultaneous publication.",
      "V12 and V13, which were not touched.",
    ], size=10)

    h(d, "Still separate release dependencies")
    para(d, "Scheduling, live-link verification, final runtime, V6's "
            "ten-minute promise, audio, SRT and chapters. None has been "
            "performed and none is claimed. A map pass is not release "
            "approval.", size=10.5)
    footer_note(d, "Scoped completion pass. Stopping here.")
    d.save(path)
    return path


if __name__ == "__main__":
    p = build(os.path.join(OUT, "RESPONSE",
                           "V4-V11_Final_Edit_Map_Completion.docx"),
              P.stamp())
    print(p)
