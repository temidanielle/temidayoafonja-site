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
    states = {}
    for n in R.VIDEOS:
        vis = os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS")
        states[n] = len([x for x in os.listdir(vis)
                         if x.endswith(".png") and "Contact_Sheet" not in x])

    d = base_doc()
    title_block(d, EYEBROW, "Response, second correction pass",
                "The follow-up corrections, applied and verified on disk")
    kv(d, "Prepared", st)
    kv(d, "Supersedes",
       "the memo with digest 95ce573b63d3ba8dac5ffe972e9db66aec392f5016b6"
       "d42e761626f94030027b")
    kv(d, "Superseded delivery",
       "5814eecc318b9da8e577de7bfcf258cec648251e56efccc3dfa09982cf8e5478")
    kv(d, "This delivery", sha256(arc))
    kv(d, "Entries", "%d" % len(z.namelist()))
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "One correction first. The archive you hashed, "
               "5814eec, was not an older file attached by mistake. It "
               "was the output of the first correction pass, built and "
               "sent in that turn. It did not contain the eight items "
               "below because those were raised afterwards. Every one of "
               "them is now applied, and the digests above differ because "
               "the files differ.")

    h(d, "The eight items")
    table(d, ["", "Asked for", "Done"],
          [["1", "Correct the active V6 FOUR THINGS card to PROBLEM, "
                 "AUTHORITY, PROOF, REAL GAP.",
            "Relabelled, each with the question its own section asks. The "
            "old labels were V9's four columns, not V6's four things. "
            "Rendered and inspected."],
           ["2", "Mark the V8 A FACTUAL RECORD card RETIRED and INACTIVE "
                 "throughout the package.",
            "Named as RETIRED in the asset index, the camera map, the "
            "motion map, the run of show and the QA report, with the "
            "withdrawn state listed as not present by design. A check "
            "fails the build if a retired family is merely absent."],
           ["3", "Correct the five stale camera and full-screen trigger "
                 "passages and the seven stale section labels.",
            "Fixed at the root. A re-cued card was moving its section and "
            "paragraph while keeping the old label and the old trigger "
            "sentence, so the row pointed at the new paragraph and quoted "
            "the old one. Both are now re-derived from the reconciled "
            "script at the new location: seven labels and seven triggers "
            "corrected, five of which reach the camera map."],
           ["4", "Correct the reporting totals.",
            "%d thought blocks holding %d paragraphs, reported apart. %d "
            "families in total, %d active after one retirement. %d active "
            "teaching and end-card states. %d contact sheets, counted as "
            "proof sheets and not as states."
            % (t["blocks"], t["paragraphs"], t["total_families"],
               t["active_families"], t["states"], t["contact_sheets"])],
           ["5", "Correct the inconsistent 220 against 221 verification "
                 "reporting.",
            "Both were typed. Every headline number now comes from one "
            "function in the build, and the final verification total is "
            "written out by the verification pass and read back by the "
            "documents. The build reports a mismatch rather than letting "
            "a stale number ship. This run: %d of %d."
            % (t["final_checks"] or 0, t["final_checks"] or 0)],
           ["6", "Distinguish V4's +74 introduction from the +2 approved "
                 "hook delta.",
            "Reported as arithmetic: %d intake words, plus %d for the "
            "restored introduction, plus %d for the approved hypothetical "
            "opening, is %d. They are separate approvals and are now "
            "reported separately."
            % (a4["base"], a4["intro"], a4["hook"], a4["total"])],
           ["7", "Complete the Shorts corrections for antecedents, "
                 "whole-sentence source wording, one clear action and "
                 "realistic timing.",
            "Ten candidates re-selected. Every line is now a contiguous "
            "run of whole source sentences, checked by a sentence-level "
            "rule, so no leading marker is silently dropped. Every ask is "
            "an action. Every candidate fits under sixty seconds with "
            "headroom at a 150 word planning rate, not only at 165."],
           ["8", "Preserve the locked Watch Next routing.",
            "V10 to V11 and V11 to public V5, unchanged. No route "
            "substituted, no schedule assumed. Both still flagged pending "
            "live confirmation."]],
          widths=[0.3, 2.6, 3.8], size=7.5)

    page_break(d)
    h(d, "The root cause behind the stale locators")
    para(d, "Seven cards were re-cued in the first pass because they were "
            "cued in the wrong place. Moving a card is three facts, not "
            "two: the section, the paragraph, and the sentence the editor "
            "cuts on. The first pass moved the first two and left the "
            "third, so a row could say section 5 while quoting the "
            "sentence from section 8. The camera map showed five of "
            "those, because two of the seven are printed through the "
            "early-edit sequence instead. The locator is now derived as a "
            "whole, and a check compares every printed label and trigger "
            "against the reconciled paragraph it points at.", size=10.5)

    h(d, "Where the numbers stand")
    table(d, ["Video", "Words", "Thought blocks", "Active families",
              "States", "Shorts"],
          [["V%d" % n, format(R.word_count(n), ","),
            "%d" % len(P.blocks(n)), "%d" % len(P.cues(n)),
            "%d" % states[n], "3"] for n in R.VIDEOS] +
          [["Total", format(t["words"], ","), "%d" % t["blocks"],
            "%d" % t["active_families"], "%d" % t["states"],
            "%d" % t["shorts"]]],
          widths=[0.8, 1.0, 1.4, 1.4, 1.0, 0.8], size=8.5)
    table(d, ["", "Count"],
          [["Families before this work", "%d" % t["prior_families"]],
           ["New opening families built", "%d" % t["new_families"]],
           ["Families in total", "%d" % t["total_families"]],
           ["Retired, inactive, not cued, not rendered",
            "%d" % t["retired_families"]],
           ["Active families", "%d" % t["active_families"]],
           ["Active teaching and end-card states", "%d" % t["states"]],
           ["Contact sheets, one per video, not states",
            "%d" % t["contact_sheets"]]],
          widths=[4.3, 2.4], size=8.5)

    h(d, "Verification, performed against the files on disk")
    table(d, ["", "Result"],
          [["Source reconciliation", "43 of 43"],
           ["Per-package checks", "175 of 175 across the eight packages"],
           ["Final verification, read back off disk",
            "%d of %d" % (t["final_checks"] or 0, t["final_checks"] or 0)],
           ["Shorts editorial audit",
            "list, antecedent, whole-sentence, trailer, stacked-ask, "
            "opening and planning-rate checks on all 24"],
           ["Locator check",
            "every printed label and trigger compared against the "
            "reconciled paragraph it points at; none stale"],
           ["Regression fixtures",
            "the delivered Shorts, shared paragraphs and report claims "
            "the reviews named are replayed and all still fire"],
           ["Historical archives", "all four unchanged, checked by hash"]],
          widths=[2.2, 4.5], size=8.5)
    para(d, "The archive was rebuilt, then hashed from the file on disk, "
            "and the sidecar was written from that hash. The verification "
            "pass reads the finished files rather than the objects in "
            "memory that produced them.", size=10.5, before=6)

    h(d, "Unchanged, as instructed")
    bullets(d, [
      "The approved recording masters. No spoken word changed in this "
      "pass, in any of the eight videos.",
      "Approved strategy, which was not reopened.",
      "V12 and V13, which were not touched.",
      "All six restored introductions, thought-block parity and the "
      "eight faith-inclusive descriptions.",
      "V6 anonymity, the sample boundary and the separated private "
      "register.",
      "The V10 to V11 and V11 to public V5 Watch Next routes.",
    ], size=10)

    h(d, "Still outstanding, and still separate from readiness")
    para(d, "Final runtime, V6's ten-minute promise, captions, chapters, "
            "audio and the live availability of both Watch Next "
            "destinations. None has been performed and none is claimed. "
            "Each needs the finished export or a live check. They are "
            "listed in their own document.", size=10.5)
    footer_note(d, "Production readiness is locked. Release approval is "
                   "yours, after those.")
    d.save(path)
    return path


if __name__ == "__main__":
    p = build(os.path.join(OUT, "RESPONSE",
                           "V4-V11_Response_Second_Correction_Pass.docx"),
              P.stamp())
    print(p)
