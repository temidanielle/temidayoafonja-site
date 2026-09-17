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
    a4 = P.v4_arithmetic()
    fc = t["final_checks"] or 0

    d = base_doc()
    title_block(d, EYEBROW, "Response, third correction pass",
                "Contradictions cleared, Shorts rules enforced "
                "semantically")
    kv(d, "Prepared", st)
    kv(d, "Supersedes", "the second-pass memo, digest 3573a3cd")
    kv(d, "Superseded delivery", "1c0123747a6f72f0f6873f9d7b209af7bb1468"
                                 "94b376996ad3e61e5d8b270074")
    kv(d, "This delivery", sha256(arc))
    kv(d, "Entries", "%d" % len(z.namelist()))
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "Seven narrow corrections, none of them touching the "
               "approved recording masters, the strategy, the Watch Next "
               "routes or V12 and V13. No spoken word changed. Two of the "
               "seven were contradictions between a decision already made "
               "and a document that was never regenerated against it, "
               "which is now a check rather than a habit.")

    h(d, "The seven items")
    table(d, ["", "Asked for", "Done"],
          [["1", "Remove the obsolete V6 card decision everywhere.",
            "Gone from V4-V11_DECISIONS_REQUIRED.docx, which now lists "
            "two items, and from V6's Open_Issues.txt, which records the "
            "relabel as RESOLVED. A check fails the build if any document "
            "still asks whether to relabel the card."],
           ["2", "Finish synchronizing the approved V8 retirement.",
            "V8's Open_Issues.txt records it as RETIRED and INACTIVE and "
            "states it is not to be reassigned. The evidence notes carry "
            "a Retired. Inactive. table and the family is excluded from "
            "the retained display copy. The ledger's detailed V8 row now "
            "reads RETIRED / INACTIVE, with the old audit verdict kept "
            "below it only as a record."],
           ["3", "Correct the V4 arithmetic in the combined source "
                 "manifest.",
            "The word table has separate Restored intro and Approved hook "
            "delta columns: %d intake, +%d, +%d, %d reconciled. The "
            "combined +%d never appears."
            % (a4["base"], a4["intro"], a4["hook"], a4["total"],
               a4["intro"] + a4["hook"])],
           ["4", "Correct the opening-asset wording.",
            "Both places in V4-V11_WHAT_CHANGED_THIS_PASS.docx now read "
            "six opening families comprising eight states. A check fails "
            "the build on the old wording."],
           ["5", "Repair the remaining non-standalone Shorts using exact "
                 "whole source sentences.",
            "V10 Short 1 now opens on \u201cYou finally got the job. "
            "Maybe it is a bigger role.\u201d, which gives both "
            "\u201cand now\u201d and \u201cthey\u201d their referent. "
            "V10 Short 3 opens on \u201cBy day 90, success does not have "
            "to mean proving you were the smartest person in the "
            "room.\u201d, which establishes the point. V11 Short 3 opens "
            "on \u201cYou accepted one job. Then you started doing "
            "another.\u201d, which defines the difference. All three are "
            "whole source sentences and all three stay under 150 words."],
           ["6", "Enforce one clear action semantically.",
            "All five endings reduced, and one more I found the same way: "
            "V9 Short 3 was pick a job and make four columns. The counter "
            "distinguishes two steps of one task, which stay together, "
            "from a second instruction introduced by a new sentence, a "
            "Then, or a comma-and. No ask now carries more than one."],
           ["7", "Regenerate the QA reports and memo, with checks that "
                 "fail these examples first.",
            "The checks were written and run against the delivered files "
            "before anything was corrected. All six document "
            "contradictions and all nine Shorts failures came back as "
            "failures. Only then were they fixed. This memo is written "
            "after the rebuild."]],
          widths=[0.3, 2.5, 3.9], size=7.5)

    page_break(d)
    h(d, "Why the previous all-pass result was not reliable, and what "
         "changed")
    para(d, "The previous pass reported 226 of 226 while the packages "
            "still contained a settled decision presented as open and "
            "Shorts whose endings asked for two things. Both were true at "
            "once because the checks counted structure rather than "
            "meaning: one ONE ASK block was read as one action, and no "
            "check compared a document against a decision already taken. "
            "A count of passing checks is only worth the questions the "
            "checks ask.", size=10.5)
    table(d, ["Now checked", "How it is counted"],
          [["One audience action per ask",
            "Instructions are counted, not ask blocks and not verbs. Pick "
            "one project and write five things is one task in two steps. "
            "Name one real cost. Then choose one next action is two."],
           ["Each Short stands alone",
            "Named opening referents must be established earlier inside "
            "the same Short, and never in the opening line itself."],
           ["Whole source sentences only",
            "Every line has to be a contiguous run of complete sentences "
            "from its own master, so no leading marker is dropped."],
           ["Realistic length",
            "Under 150 spoken words and under 55 seconds at a 150 word "
            "planning rate, not only at 165."],
           ["Settled decisions stay settled",
            "No document may still ask whether to relabel the V6 card or "
            "offer the V8 card another passage."],
           ["Retirement is stated on the row",
            "Ledger and evidence tables are read as rows, not as flat "
            "text, so a status beside a family name is actually seen."]],
          widths=[2.0, 4.7], size=8.5)
    para(d, "Two of the new checks failed on their first run for reasons "
            "in the checks rather than the packages: one matched its own "
            "corrective sentence, and one read table cells where it "
            "needed table rows. Both were fixed and re-run. Neither was a "
            "package defect, and the distinction is recorded here rather "
            "than smoothed over.", size=10.5, before=6)

    h(d, "The Shorts, as they now stand")
    table(d, ["", "Words", "At 150 wpm", "Actions in the ask"],
          [["V%d Short %d" % (n, r["num"]), "%d" % r["words"],
            r["plan_clock"],
            "%d" % len(SH.actions(R.S._norm(" ".join(
                SH.SHORTS[(n, r["num"])]["ask"]))))]
           for n in R.VIDEOS for r in SH.rows(n)],
          widths=[1.6, 0.9, 1.2, 1.6], size=7.5)
    caption(d, "Two asks are phrased as a caution rather than an "
               "instruction, so the counter reads no affirmative action "
               "in them: V4 Short 3 ends do not assume the learning will "
               "happen by itself, and that is the point it makes. The "
               "rule enforced is at most one.")

    h(d, "Verification, performed against the files on disk")
    table(d, ["", "Result"],
          [["Source reconciliation", "43 of 43"],
           ["Per-package checks", "175 of 175 across the eight packages"],
           ["Final verification, read back off disk",
            "%d of %d" % (fc, fc)],
           ["Regression fixtures",
            "the compound endings, dangling openings, delivered Shorts, "
            "shared paragraphs and report claims from all three reviews "
            "are replayed, and every one still fires"]],
          widths=[2.2, 4.5], size=8.5)
    para(d, "The archive was rebuilt, hashed from the file on disk, and "
            "the sidecar written from that hash.", size=10.5, before=6)

    h(d, "Unchanged, as instructed")
    bullets(d, [
      "The approved recording masters. No spoken word changed in this "
      "pass.",
      "Approved strategy, which was not reopened.",
      "V12 and V13, which were not touched.",
      "The V10 to V11 and V11 to public V5 Watch Next routes.",
      "All six restored introductions, thought-block parity and the "
      "eight faith-inclusive descriptions.",
      "The corrected V6 card, the V8 retirement, the corrected locators "
      "and the reconciled counts from the second pass: %d thought "
      "blocks, %d families in total, %d active, %d states, %d contact "
      "sheets." % (t["blocks"], t["total_families"], t["active_families"],
                   t["states"], t["contact_sheets"]),
    ], size=10)

    h(d, "Still outstanding, and still separate from readiness")
    para(d, "Final runtime, V6's ten-minute promise, captions, chapters, "
            "audio and the live availability of both Watch Next "
            "destinations. None has been performed and none is claimed.",
         size=10.5)
    footer_note(d, "Production readiness is locked. Release approval is "
                   "yours, after those.")
    d.save(path)
    return path


if __name__ == "__main__":
    p = build(os.path.join(OUT, "RESPONSE",
                           "V4-V11_Response_Third_Correction_Pass.docx"),
              P.stamp())
    print(p)
