# -*- coding: utf-8 -*-
"""The Word roadmap addendum for Videos 14 to 21.

Scoped. It records proposed changes to eight slots and leaves the locked
September 9 roadmap file untouched. Every locked slot line printed here is read
from that file at build time by baseline.py.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import baseline
from docs1421 import (base_doc, para, title_block, rule, h, kv, callout, table,
                      bullets, sub, field, page_break, footer_note,
                      NAVY, GOLD, DIM, RED)
from briefs import OFFERS

TW = 6.7  # text width in inches at 0.9in side margins on US Letter

# The overlap check the instruction asks for: every proposed or preserved slot
# in this range against the slots the locked roadmap keeps unchanged.
OVERLAP = [
 ("V14", "V9, V21, V28", "Medium",
  "V9 decides the change. V14 is the comparison method before deciding. V21 "
  "is after arrival. V28 is the long-horizon version. Keep one transfer "
  "lesson per slot."),
 ("V15 (proposed)", "V25, V30, V24", "High",
  "V25 diagnoses a stalled career. V30 chooses assignments. V24 asks what "
  "growth looks like past senior. V15 is narrower: one kind of judgment the "
  "prior work did not require, and three causes that look identical."),
 ("V15 (proposed)", "V2, V7, V26", "Low",
  "V2 is marketability. V7 tests whether more work is growth. V26 is "
  "developmental work under AI. The refinement document names these "
  "separations and this addendum keeps them."),
 ("V16", "V5, V8, V22, V27", "Medium",
  "V5 makes a career legible. V8 proves foundational work. V22 is the "
  "wait-or-move decision. V27 is the organizational failure. V16 stays with "
  "recognition inside one organization."),
 ("V17", "V11, V26", "High",
  "The locked roadmap's own separation rule already governs these three and "
  "is carried unchanged: V11 present value, V17 evidence of contribution, "
  "V26 learning and developmental work."),
 ("V18", "V22, V24", "Medium",
  "V18 is the shape of the next role. V22 is the timing of a promotion "
  "decision. V24 is growth once already senior."),
 ("V19", "V12, V13", "Low",
  "V12 is the present constraint. V13 is a thirty-day test of a destination. "
  "V19 examines one destination on its own terms."),
 ("V20", "V4, V9", "Low",
  "V4 explains a scattered career. V9 is the industry decision. V20 is the "
  "interruption and the return."),
 ("V21", "V9, V14, V29", "Medium",
  "V21 is after arrival. V29 is expertise that has become too narrow inside "
  "one place."),
 ("Reserved employer brief", "V9, V13, V22, V27", "Medium",
  "The reserved brief checks a destination before accepting an offer. It is "
  "not the industry decision, the thirty-day test, the internal wait-or-move "
  "decision, or the organizational-failure video."),
]

QUEUE = [
 ("How to Stay Relevant After 40 Without Chasing Every Trend",
  "Displaced from slot 15 by this proposal. NOT deleted.",
  "No number assigned. Its September 9 thumbnail line UPDATE. DON’T ERASE. "
  "and its Field Kit route travel with the topic and are not reassigned to "
  "the new slot 15 topic."),
 ("Before You Accept the Job, Find Out How the Company Actually Uses People "
  "Like You",
  "Reserved brief. Developed in the companion briefs document.",
  "No number assigned, as previously agreed. Do not place it in an occupied "
  "slot."),
 ("Job security, as a distinct future brief",
  "Approved theme. Not placed.",
  "Must distinguish the continuity of the current role from the person's "
  "options if that role ends. Portable evidence cannot establish that a job "
  "is safe."),
 ("When to leave, as research input or a distinct future decision brief",
  "Approved theme. Not placed.",
  "Feeds the later V25 growth and stall topic, or a separate decision brief. "
  "Do not repeat V3, V6 or V12, and do not equate limited growth with an "
  "instruction to resign."),
]


def build(out_path, stamp):
    rm = baseline.roadmap_slots()
    rf = baseline.refinement_slots()
    roadmap_hash = baseline.verify_roadmap()
    ref_hash = baseline.sha256(baseline.REFINEMENT)

    d = base_doc()
    footer_note(d, "Capability Formation  |  V14 to V21 roadmap addendum  |  "
                   "Proposal for editorial review, not a production approval")

    title_block(d, "Capability Formation  |  YouTube Roadmap",
                "Videos 14 to 21: Scoped Roadmap Addendum",
                "A proposed one-slot change, the preserved slots around it, "
                "and the overlap check against the locked sequence")
    kv(d, "Created", stamp)
    kv(d, "Scope", "Videos 14 to 21, plus the forward-topic queue. "
                   "Videos 1 to 13, V22, V23 to V30 and the V31 capstone are "
                   "not changed by this document.")
    kv(d, "Nature", "A planning and editorial-brief update. It proposes. It "
                    "does not lock, approve or produce anything.")

    callout(d, "This addendum does not overwrite YouTube_Roadmap_1-30_LOCKED_"
               "Sep09_2026.docx. That file is unchanged on disk and its "
               "checksum still matches its own lock file. This is a scoped "
               "patch to be applied only if the proposal is accepted.")

    h(d, "What this is, and what it is not")
    bullets(d, [
      "It IS a proposed refinement of the next eight slots, an overlap check "
      "against the slots that stay as they are, and a record of where the "
      "displaced topic went.",
      "It is NOT a rebuild of Videos 1 to 13, a change to any approved "
      "recording master, a request to generate scripts, a slide deck, a "
      "motion-graphic asset, a thumbnail, or a channel-wide numbering swap.",
      "Every outline, opening idea, framework, CTA and routing suggestion in "
      "this addendum and its companion briefs document is a proposal. None of "
      "it is approved speech.",
    ])

    h(d, "The recommendation, in one line")
    para(d, "Make one change to the next eight slots: put the judgment-gap "
            "topic at V15 and keep the other seven topics in place. Preserve "
            "the after-40 topic in the forward queue, and develop employer due "
            "diligence as the next reserved brief.",
         size=11.5, bold=True, color=NAVY)

    h(d, "Slot by slot: locked baseline against the proposal")
    para(d, "The LOCKED column is read from the September 9 roadmap file at "
            "build time, so it cannot drift from the source. The PROPOSED "
            "column is this addendum's recommendation.", size=10, color=DIM)
    rows = []
    for n in range(14, 22):
        locked_title, locked_thumb, locked_status = rm[n]
        prop_title, treatment = rf[n]
        if n == 14:
            change = ("No topic change. Planning label reverts to the "
                      "descriptive title, which is what the locked roadmap's "
                      "own evidence gate instructs.")
        elif n == 15:
            change = ("CHANGED. New topic proposed for this slot. The after-40 "
                      "topic moves to the forward queue, undeleted.")
        elif n == 18:
            change = ("No change. One copy variance in the title punctuation, "
                      "recorded below and not silently resolved.")
        else:
            change = "No change. Locked entry preserved."
        rows.append(["V%d" % n, locked_title, prop_title, change])
    table(d, ["#", "Locked September 9 entry", "Proposed planning label",
              "Change"], rows,
          widths=[0.42, 2.05, 2.05, 2.18], size=8.5)

    h(d, "Status labels for these eight slots")
    table(d, ["#", "Proposed status", "What that means here"], [
      ["V14", "Direction approved. CONDITIONAL.",
       "The topic stands. The numerical, past-tense title is gated on research "
       "that has not been done."],
      ["V15", "PROPOSED placement. Direction under review.",
       "The theme is an approved editorial input. The slot, the outline and "
       "the title are proposals. No script exists."],
      ["V16 to V21", "Unchanged. Direction approved.",
       "The prior roadmap decision is preserved. A development brief now "
       "exists for each, which is not the same as an approved script."],
    ], widths=[0.75, 2.0, 3.95], size=9)

    h(d, "What is preserved without change")
    bullets(d, [
      "Videos 1 to 13: scripts, assets, thumbnails, Shorts, publishing copy "
      "and routing. Untouched.",
      "The closed V4 to V7 September 9 synchronization. Untouched.",
      "The existing V8 to V13 production files. Untouched.",
      "V22, No Promotion? How to Know Whether to Wait or Move On, keeps its "
      "slot and its position on promotion timing.",
      "V23 to V30 keep their existing slots, titles, thumbnail directions and "
      "resource routes.",
      "V31, How to Choose Your Next Career Move Without Wasting Your "
      "Experience, remains the reserved capstone.",
      "No later number is shifted by this proposal. The one change is a "
      "substitution inside slot 15, not an insertion.",
    ])

    page_break(d)
    h(d, "The displaced topic and the forward queue")
    para(d, "Nothing is deleted. The after-40 topic keeps its September 9 "
            "working title and waits for a number.", size=10, color=DIM)
    table(d, ["Topic", "Position", "Conditions carried"],
          [[a, b, c] for a, b, c in QUEUE],
          widths=[2.35, 1.6, 2.75], size=8.5)

    h(d, "Overlap check against the unchanged slots")
    para(d, "Every proposed or preserved slot in this range, checked against "
            "the slots the locked roadmap keeps. The risk column is an "
            "editorial judgment about repetition, not a performance estimate.",
         size=10, color=DIM)
    table(d, ["Slot", "Checked against", "Risk", "Separation rule to hold"],
          [[a, b, c, e] for a, b, c, e in OVERLAP],
          widths=[1.15, 1.1, 0.6, 3.85], size=8.5)

    h(d, "Thumbnail copy: one position that has to be settled")
    para(d, "UPDATE. DON’T ERASE. was written for the after-40 topic. If that "
            "topic moves to the forward queue, the line moves with it, and the "
            "proposed slot 15 topic has no approved thumbnail copy at all. "
            "Copy options are offered in the briefs document as proposals for "
            "review. No artwork is requested, produced or approved here, and "
            "no existing thumbnail is changed.")
    callout(d, "Every other thumbnail line in this range is carried from the "
               "locked roadmap unchanged. Carrying a line is a copy decision, "
               "not a statement that finished artwork exists.",
            color=NAVY)

    h(d, "One copy variance, recorded rather than resolved")
    para(d, "The locked roadmap writes slot 18 as “%s”. The refinement "
            "document writes it as “%s”. The topic is identical and "
            "neither form is adopted here. Resolve it when the slot is "
            "packaged." % (rm[18][0], rf[18][0]))

    h(d, "V14 research condition, carried forward in full")
    para(d, "The descriptive title is the planning label. “I Compared 30 "
            "Job Descriptions Across 3 Industries” can be used only after "
            "that documented research has actually been completed. Use the "
            "real sample size, and explain sample selection and limits.")
    bullets(d, [
      "Do not use past tense or a numerical claim as active publishing copy "
      "before the research is completed and documented.",
      "The actual sample size determines any eventual numerical title. A "
      "target is not a result.",
      "Similar language across job descriptions does not establish equivalent "
      "roles, applicant readiness, or hiring acceptance.",
      "Research has not been completed. What exists after this addendum is a "
      "research plan, in the V14 brief.",
    ])

    h(d, "How the TubeBuddy input was used")
    para(d, "The five themes are approved editorial inputs. The screenshots "
            "supply suggested topics and tool-generated claims. This addendum "
            "does not establish search volume, competition, trend direction or "
            "likely performance, and no such figure appears anywhere in these "
            "deliverables.")
    callout(d, "Not claimed, and not to be claimed on the basis of this input: "
               "that nobody covers this, that the first video will own the "
               "search, that there is no competition, that this will "
               "outperform, or that an audience-match score proves demand.")
    para(d, "TubeBuddy remains a language and problem-discovery input, as the "
            "locked roadmap already states. It is not the editorial "
            "strategist.", size=10, color=DIM)

    h(d, "The five themes and where each one goes")
    table(d, ["Theme", "Proposed handling"],
          [[t, hnd] for t, hnd in baseline.refinement_themes()],
          widths=[1.85, 4.85], size=8.5)
    para(d, "The handling column is quoted from the refinement document.",
         size=9, color=DIM)

    h(d, "Resource routes: carried, not expanded")
    para(d, "No new product, download or offer is proposed anywhere in this "
            "addendum or its briefs. The four existing routes are the only "
            "ones referenced.")
    table(d, ["Existing offer", "Where it lives", "What it is"],
          [[a, b, c] for a, b, c in OFFERS], widths=[1.9, 2.25, 2.55], size=8.5)
    para(d, "Slot routes carried from the locked roadmap for this range: V14 "
            "and V15 Field Kit; V16 and V17 Keep the Proof; V18 and V19 "
            "Decision Check; V20 and V21 Field Kit. One consequence of the "
            "slot 15 substitution: the Field Kit route on that slot was "
            "carried for the after-40 topic, so the route for a new slot 15 "
            "topic is an open proposal, not an inherited decision.")

    h(d, "Production rules that continue to apply, unchanged")
    bullets(d, [
      "No burned-in or open captions anywhere in long-form YouTube videos. "
      "Deliver a complete SRT matched to the actual final edit for YouTube CC. "
      "Shorts and Reels may use designed captions.",
      "Keep the established natural delivery, paragraph and thought-block "
      "recording, intentional cuts, restrained camera movement, full-screen "
      "teaching visuals, and a final Watch Next.",
      "No new equipment is prescribed and the current camera setup is not "
      "reopened.",
      "These standing rules do not trigger a rebuild of any completed package.",
    ])

    h(d, "Decision order for every slot in this range")
    para(d, "Research the viewer's problem, decide whether it strengthens "
            "Temidayo's intended association, then write the script. Final "
            "title and thumbnail pairing and Watch Next routing are settled "
            "with the actual script and publishing plan. No full script, new "
            "thumbnail, or rendered production asset is approved by this "
            "addendum.")

    h(d, "Sources")
    table(d, ["Source", "Use", "SHA-256"], [
      ["YouTube_Roadmap_1-30_LOCKED_Sep09_2026.docx",
       "Baseline. Every locked slot line in this document is read from it at "
       "build time. Checksum matched against its own lock file before use. "
       "The file is not modified.",
       roadmap_hash],
      [baseline.REFINEMENT_NAME,
       "The September 9 TubeBuddy-informed refinement proposal supplied for "
       "this task. Read only. There is no prior lock file for it, so its "
       "checksum is recorded here rather than matched.",
       ref_hash],
    ], widths=[1.85, 3.35, 1.5], size=8)
    para(d, "This addendum adds editorial recommendations. It is not new "
            "external research, and it does not independently validate any "
            "external performance example.", size=9.5, color=DIM)

    rule(d)
    para(d, "V14 to V21 WORKING ROADMAP REFINEMENT DOCUMENTED. DEVELOPMENT "
            "BRIEFS READY FOR EDITORIAL REVIEW. SCRIPTS, FINAL PACKAGING, "
            "ROUTING, AND PRODUCTION ASSETS NOT YET APPROVED.",
         size=10.5, bold=True, color=RED)

    d.save(out_path)
    return out_path
