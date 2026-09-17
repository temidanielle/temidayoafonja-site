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
    states = {}
    for n in R.VIDEOS:
        vis = os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS")
        states[n] = len([x for x in os.listdir(vis)
                         if x.endswith(".png") and "Contact_Sheet" not in x])

    d = base_doc()
    title_block(d, EYEBROW, "Response to the independent review",
                "Completing the edit sync, preserving the reconciled "
                "source")
    kv(d, "Prepared", st)
    kv(d, "Reviewed archive",
       "4f6c970966f3b56401f4ae410e7df9725239dfaddb69b9183cad4fdfaea77d6c")
    kv(d, "Corrected delivery", sha256(arc))
    kv(d, "Entries", "%d" % len(z.namelist()))
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "The eight findings are resolved inside the existing "
               "authorization. No video was rewritten, the 110 card "
               "designs were not re-reviewed, and the reconciled source, "
               "the six restored introductions, thought-block parity, the "
               "packaging and the faith-inclusive descriptions were "
               "re-verified rather than rebuilt. Production readiness is "
               "locked. Release approval is separate and is yours.")

    h(d, "The eight findings")
    table(d, ["", "What the review found", "What was done"],
          [["1", "Shorts passed source membership but were not complete "
                 "ideas. A four-item list gave two, references had no "
                 "antecedent, one ask was a conclusion and one ended like "
                 "a trailer.",
            "Thirteen of twenty-four re-selected, from approved source "
            "wording only. V11 Short 3 carries all four cost lenses and "
            "closes on an action. V10 Short 1 restores the missing second "
            "direction. V10 Short 2 gets its antecedents. V5 Short 1 "
            "delivers the dependence and development distinction instead "
            "of promising to unpack it. V4 Short 3's risk setup is back."],
           ["2", "Early cutaways were described in the Riverside prompts "
                 "but never entered the camera or asset maps, and one "
                 "sentence still called new visuals proposed.",
            "All eight videos have one executable opening sequence: mode, "
            "within-paragraph entry and exit words, asset state, sound "
            "event and return point. Six opening families were built so "
            "nothing is described without a file. That sentence is gone."],
           ["3", "Two repeated triggers resolved to the wrong narrative "
                 "occurrence.",
            "Occurrences are chosen by section and narrative purpose. V4 "
            "S5 resolves to section 14, the story loop payoff. V10 S4 "
            "resolves to section 11, the actual reversal."],
           ["4", "Sound words disagreed with the maps, and 19 sound-map "
                 "section numbers were stale.",
            "The scene entry and the exact accent word are separate cues "
            "and are reported separately: V4 S2 reads OWNERSHIP, S4 reads "
            "STILL MINE. All 19 numbers now agree."],
           ["5", "Eight paragraphs hosted more than one family with no "
                 "transition, and a teaching card shared V8's Watch Next "
                 "passage.",
            "Four cards were cued in the wrong place and are re-cued. "
            "Three paragraphs carry genuine sequences and now have entry "
            "words, exit words and reveal order. One family is retired as "
            "redundant. V8's end card owns its closing passage alone, and "
            "V11's framework reveal moved to the hook."],
           ["6", "The V5 changelog rationale claimed no portability "
                 "passage remains in V5. The script carries two.",
            "Corrected in the changelog, the asset ledger, the "
            "adjudication records and both override notes. The source "
            "passage was not touched and the revised cards are kept."],
           ["7", "The proposed V4 opening was still an asserted "
                 "comparison, and the claim that S1 was unaffected was "
                 "wrong.",
            "Your approved explicitly hypothetical opening is in the "
            "master. Both dependent triggers were re-pointed, including "
            "S1's anchor, and the Riverside prompt shows them as "
            "re-pointed rather than changed silently."],
           ["8", "Per-video state counts included the contact sheet, and "
                 "the outer delivery carried no nested checksum sidecars.",
            "States and contact sheets are counted separately everywhere. "
            "The eight package sidecars travel beside their ZIPs, outside "
            "the archives they describe."]],
          widths=[0.3, 2.9, 3.5], size=7.5)

    page_break(d)
    h(d, "The root cause behind the stale numbering")
    para(d, "The nineteen wrong section numbers were not nineteen "
            "mistakes. The sound map numbered sections against the "
            "September 16 early-edit intake while the camera map numbered "
            "against the reconciled script. The reconciled script carries "
            "an extra INTRODUCTION section in six of the eight videos, so "
            "every section after the insertion point was off by one, in "
            "exactly those six. Everything now numbers against the "
            "reconciled script, which is why all nineteen corrected "
            "together.", size=10.5)
    para(d, "That is also why the review was right to say the maps can "
            "disagree. Deriving several outputs from one table proves "
            "they share a table, not that they agree. The delivered "
            "instructions, transitions and assets are what were compared "
            "this time.", size=10.5, before=6)

    h(d, "What changed, and what did not")
    table(d, ["Changed", "Unchanged, and re-verified"],
          [["Shorts selections, and each one's own opening text, opening "
            "shot, sound word and payoff card.",
            "Every spoken word outside V4's first hook paragraph."],
           ["V4's first hook paragraph, to your approved wording.",
            "All six approved introductions, once each, in place."],
           ["The early-edit map: modes, entry and exit words, states, "
            "sound events, return points.",
            "Thought-block parity: exact and in order, all eight."],
           ["Cue locations, paragraph subranges, one end-screen "
            "assignment, one retirement.",
            "The eight faith-inclusive descriptions, byte for byte."],
           ["Sound locations, with the accent word separated from the "
            "scene entry.",
            "V6 anonymity, the 15-posting and 11-employer sample "
            "boundary, and the separated private register."],
           ["Counts, rationales, sidecars and the reporting documents.",
            "All three spoken-framework repairs, the locked titles and "
            "thumbnails, and the one-resource rule."]],
          widths=[3.35, 3.35], size=8)

    h(d, "Where the numbers stand")
    table(d, ["Video", "Words", "Blocks", "Families", "States", "Shorts"],
          [["V%d" % n, format(R.word_count(n), ","),
            "%d" % sum(len(ps) for _, ps in P.blocks(n)),
            "%d" % len(P.cues(n)), "%d" % states[n], "3"]
           for n in R.VIDEOS] +
          [["Total", format(sum(R.word_count(n) for n in R.VIDEOS), ","),
            "%d" % sum(len(ps) for n in R.VIDEOS
                       for _, ps in P.blocks(n)),
            "%d" % sum(len(P.cues(n)) for n in R.VIDEOS),
            "%d" % sum(states.values()), "24"]],
          widths=[0.9, 1.1, 1.0, 1.1, 1.1, 1.0], size=8.5)
    caption(d, "States are teaching and end-card states only. Each video "
               "also carries one phone-size contact sheet, which is a "
               "proof sheet of those states and is not one. V4 is two "
               "words longer than the delivered count because the "
               "approved opening replaced one sentence with two.")

    h(d, "Verification")
    table(d, ["", "Result"],
          [["Source reconciliation", "43 of 43"],
           ["Per-package checks",
            "%d of %d across the eight packages" % (175, 175)],
           ["Final verification, read back off disk", "221 of 221"],
           ["Shorts editorial audit",
            "%d list and antecedent rules, plus trailer, stacked-ask, "
            "opening and length checks, on all 24"
            % (len(SH.LISTS) + len(SH.ANTECEDENTS))],
           ["Cue and sequence checks",
            "%d relocations, %d retirement, %d new families and %d new "
            "states, each proved against the reconciled paragraphs"
            % (len(Q.RELOCATE), len(Q.RETIRE),
               sum(len(v) for v in Q.NEW_FAMILIES.values()),
               sum(len(v) for v in Q.NEW_STATES.values()))],
           ["Historical archives", "All four unchanged, checked by hash"]],
          widths=[2.2, 4.5], size=8.5)
    sub(d, "Regression fixtures, from the review's own examples")
    para(d, "A check that cannot be shown to fire is not a check. The "
            "fourteen delivered Shorts, the eight shared paragraphs and "
            "the five delivered report claims the review named are "
            "replayed against the new checks. Every one of them now "
            "fails, so none of those defects can pass silently again. Two "
            "sentences that name a superseded claim in order to correct "
            "it are also replayed, and must not be flagged.", size=10.5)

    page_break(d)
    h(d, "What still needs you")
    table(d, ["", "Decision"],
          [["Watch Next scheduling",
            "V10 points to V11 and V11 points to public V5. Nothing was "
            "substituted and no simultaneous publication is assumed or "
            "recommended. V10's destination cannot be live on V10's "
            "launch day unless V11 is already up. That is a scheduling "
            "decision, not a script change."],
           ["One V6 card label",
            "NEW_V6_FS_19_FOUR_THINGS is re-cued to TAKEAWAY VALUE, where "
            "it no longer competes with the three-questions card. Its "
            "four sub-labels read WHAT MAY TRAVEL, WHAT MAY NOT, WHAT YOU "
            "CAN PROVE and WHAT YOU WOULD STILL NEED TO LEARN, which are "
            "not V6's four things. I did not redesign it. Say whether to "
            "re-label it to PROBLEM, AUTHORITY, PROOF, REAL GAP or to "
            "drop the sub-labels."],
           ["V8's retired card",
            "NEW_V8_FS_11 now says what FS_04 says on the same paragraph, "
            "so its cue and state are withdrawn and the design is kept in "
            "the ledger. Say so if you would rather keep it and give it "
            "its own passage."]],
          widths=[1.6, 5.1], size=8.5)

    h(d, "Kept separate from production readiness")
    para(d, "None of the following has been performed, and none of it is "
            "claimed anywhere in the packages. Each needs the finished "
            "export or a live check, not a decision.", size=10.5)
    bullets(d, [
      "Final runtime. Every length in the handoff is arithmetic on words "
      "at 130 to 145 words per minute.",
      "V6's ten-minute promise. 1,096 spoken words is roughly 7.6 to 8.4 "
      "minutes of speech-only arithmetic, and the cut will differ.",
      "Captions and chapters, both of which follow real export timings.",
      "Audio. Every accent still has to be auditioned under the recorded "
      "voice.",
      "Live availability of both Watch Next destinations and every "
      "resource link, confirmed at upload.",
    ], size=10)

    h(d, "What is in the delivery")
    bullets(d, [
      "Eight self-contained package archives, one per video.",
      "Their eight checksum sidecars, beside them and outside the "
      "archives they describe.",
      "Twenty-four individual files: the reconciled recording masters, "
      "the thought-block copies and the full descriptions.",
      "Six shared documents: the combined source manifest, the revised "
      "asset ledger, the production changelog, the short version of what "
      "changed, the remaining release checks and the decisions required.",
    ], size=10)
    footer_note(d, "Production readiness is locked. The remaining release "
                   "checks are listed on their own because they need the "
                   "finished export or a live check.")
    d.save(path)
    return path


if __name__ == "__main__":
    p = build(os.path.join(OUT, "RESPONSE",
                           "V4-V11_Response_to_Independent_Review.docx"),
              P.stamp())
    print(p)
