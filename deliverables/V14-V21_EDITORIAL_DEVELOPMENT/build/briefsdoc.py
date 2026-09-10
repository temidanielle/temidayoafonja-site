# -*- coding: utf-8 -*-
"""The Word document carrying all nine editorial development briefs.

Eight slot briefs for Videos 14 to 21, plus the reserved employer
due-diligence brief. Every brief uses the same field order so a reviewer can
compare them without re-reading the structure each time.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import baseline
from docs1421 import (base_doc, para, title_block, rule, h, kv, callout, table,
                      bullets, sub, field, page_break, footer_note,
                      NAVY, GOLD, DIM, RED)
from briefs import BRIEFS, OFFERS


def _brief(d, b, locked):
    num = b["num"]
    head = "VIDEO %s" % num[1:] if num.startswith("V") else "RESERVED BRIEF"
    para(d, head, size=9, bold=True, color=GOLD, before=0, after=3)
    para(d, b["label"], size=16, bold=True, color=NAVY, after=4, keep=True)
    para(d, b["status"], size=9.5, color=RED, after=8)
    rule(d, after=10)

    if locked:
        lt, lth, lst = locked
        para(d, "Locked roadmap entry for this slot: “%s”  |  thumbnail %s  |  "
                "%s" % (lt, lth, lst), size=9, color=DIM, after=10)

    sub(d, "The viewer's problem")
    para(d, b["problem"])

    sub(d, "The one job this video does")
    para(d, b["job"])

    sub(d, "What it has to separate")
    bullets(d, b["separate"])

    sub(d, "Proposed opening territory")
    para(d, b["opening"])

    sub(d, "Proposed shape")
    bullets(d, b["shape"])

    sub(d, "Research and evidence to gather before scripting")
    bullets(d, b["research"])

    sub(d, "What must be said out loud")
    bullets(d, b["honesty"])

    sub(d, "Evidence gaps that stay open")
    para(d, "These gaps are not to be filled with an invented personal story, "
            "result, quotation, employer example or metric. Constructed "
            "examples are labeled as illustrations on screen.",
         size=9.5, color=DIM, after=5)
    bullets(d, b["nofill"])

    sub(d, "What the viewer leaves with")
    para(d, b["outcome"])

    sub(d, "Boundary against the neighboring slots")
    para(d, b["boundary"])

    sub(d, "Proposed packaging and routing")
    field(d, "Resource route", b["route"])
    field(d, "Watch Next", b["watchnext"])
    field(d, "Thumbnail copy", b["thumb"])

    sub(d, "Carried prohibitions")
    bullets(d, b["donot"])

    sub(d, "Open for editorial review")
    bullets(d, b["open"])


def build(out_path, stamp):
    rm = baseline.roadmap_slots()
    d = base_doc()
    footer_note(d, "Capability Formation  |  V14 to V21 development briefs  |  "
                   "Proposals for editorial review. Not scripts, not approved "
                   "speech.")

    title_block(d, "Capability Formation  |  Editorial Development",
                "Videos 14 to 21: Development Briefs",
                "Eight slot briefs and one reserved brief, prepared for "
                "editorial review before any script is written")
    kv(d, "Created", stamp)
    kv(d, "Status", "Proposals. No script, publishing copy, thumbnail, deck, "
                    "motion asset, Riverside prompt or chapter list exists for "
                    "any of these videos.")
    kv(d, "Companion", "Videos_14-21_Roadmap_Addendum.docx, which carries the "
                       "slot table, the overlap check and the forward queue.")

    callout(d, "Nothing in this document is approved speech. Openings, "
               "frameworks, CTAs and routing are proposals. A brief being "
               "ready for review is not the same as a script being approved, "
               "and no video in this range has a locked script.")

    h(d, "How to read a brief")
    table(d, ["Field", "What it is"], [
      ["The viewer's problem", "The recognizable moment the video opens from."],
      ["The one job", "The single job this slot does that no other slot does."],
      ["What it has to separate",
       "The distinctions that make the video useful rather than general."],
      ["Proposed opening territory",
       "A direction for the opening. Not a hook, and not approved speech."],
      ["Proposed shape", "A structure for the teaching, open to revision."],
      ["Research and evidence",
       "What has to be gathered, verified or documented before scripting."],
      ["What must be said out loud",
       "The honesty requirements. Leaving these out would overpromise."],
      ["Evidence gaps that stay open",
       "Gaps that must not be closed by invention. These are hard limits."],
      ["What the viewer leaves with", "The artifact or the sentence."],
      ["Boundary", "Separation from the neighboring slots, by number."],
      ["Proposed packaging and routing",
       "Resource route, Watch Next and thumbnail copy. All proposals, settled "
       "with the finished script."],
      ["Carried prohibitions",
       "The specific instructions attached to this slot, carried verbatim in "
       "substance."],
      ["Open for editorial review", "What still needs a decision."],
    ], widths=[1.85, 4.85], size=8.5)

    h(d, "The nine briefs")
    table(d, ["#", "Working title", "Standing"], [
      [b["num"], b["label"],
       "Proposed slot" if b["num"] == "V15" else
       ("Reserved, unassigned" if b["num"] == "RESERVED" else
        ("Conditional on research" if b["num"] == "V14" else "Unchanged slot"))]
      for b in BRIEFS
    ], widths=[0.75, 4.0, 1.95], size=8.5)

    h(d, "Resource routes referenced")
    para(d, "No new product or offer is proposed. Only these four existing "
            "routes are referenced, and none of them is described as doing "
            "something it does not do.", size=10, color=DIM)
    table(d, ["Existing offer", "Where it lives", "What it is"],
          [[a, b, c] for a, b, c in OFFERS], widths=[1.9, 2.25, 2.55], size=8.5)

    for b in BRIEFS:
        page_break(d)
        locked = None
        if b["num"].startswith("V"):
            locked = rm.get(int(b["num"][1:]))
        _brief(d, b, locked)

    page_break(d)
    h(d, "What is deliberately not in this document")
    bullets(d, [
      "Full recording scripts, and script-only recording copies.",
      "Shorts scripts.",
      "Final publishing copy: titles, descriptions, pinned comments, tags.",
      "Final thumbnail artwork.",
      "Slide decks and motion-graphic assets.",
      "Final Riverside production prompts.",
      "Final chapters, and any video URL.",
    ])
    para(d, "None of these were requested for this task, and producing them "
            "now would misrepresent unwritten scripts as ready work.",
         size=10, color=DIM)

    h(d, "Standing production rules that apply when these are eventually made")
    bullets(d, [
      "No burned-in or open captions anywhere in long-form YouTube videos. A "
      "complete SRT matched to the actual final edit is delivered for YouTube "
      "CC. Shorts and Reels may use designed captions.",
      "Natural delivery, paragraph and thought-block recording, intentional "
      "cuts, restrained camera movement, full-screen teaching visuals, and a "
      "final Watch Next.",
      "No new equipment. The current camera setup is not reopened.",
    ])

    rule(d)
    para(d, "V14 to V21 WORKING ROADMAP REFINEMENT DOCUMENTED. DEVELOPMENT "
            "BRIEFS READY FOR EDITORIAL REVIEW. SCRIPTS, FINAL PACKAGING, "
            "ROUTING, AND PRODUCTION ASSETS NOT YET APPROVED.",
         size=10.5, bold=True, color=RED)

    d.save(out_path)
    return out_path
