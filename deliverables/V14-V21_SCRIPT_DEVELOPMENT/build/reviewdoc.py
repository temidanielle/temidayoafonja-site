# -*- coding: utf-8 -*-
"""The editorial review summary for the V14 to V21 script-development batch."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import qa1421
from masterdoc import estimate, block_count
from docsx import (base_doc, para, title_block, rule, h, kv, callout, table,
                   bullets, sub, field, page_break, footer_note, numbered,
                   NAVY, GOLD, DIM, RED)

TITLE_ISSUES = [
 ("V15 thumbnail", "NO APPROVED COPY EXISTS",
  "The slot's previous line, UPDATE. DON'T ERASE., belongs to the after-40 "
  "topic and travels with it. Recommended after drafting: THE GAP UNDER THE "
  "SKILL, because the script's whole argument is that the visible skill is "
  "not the gap. Kept live: NOT A SKILLS GAP, and EXPERIENCE ISN'T THE SAME "
  "AS PRACTICE. Needs a decision before packaging."),
 ("V15 title", "PROPOSED, NOT APPROVED",
  "The Career Gaps You Don't See Until the Work Gets Harder. Carried from "
  "the refinement document unchanged. The title and thumbnail should be "
  "judged as a pair, which cannot happen until the thumbnail line is "
  "chosen."),
 ("V16 thumbnail", "CHANGED BY INSTRUCTION",
  "VALUED, BUT OVERLOOKED. The locked roadmap carries the hyphenated form, "
  "VALUED - BUT OVERLOOKED. The current instruction specifies the comma. "
  "Adopted, and recorded here as a copy decision rather than resolved "
  "silently."),
 ("V18 title", "VARIANCE RESOLVED",
  "Should You Stay an Individual Contributor or Become a Manager? The locked "
  "roadmap's hyphenated form is retired, no dash of any kind is used, and "
  "the refinement document's form is adopted as instructed."),
 ("V18 thumbnail", "FLAGGED FOR APPROVAL",
  "YOU DON'T HAVE TO MANAGE is carried from the roadmap, and the script is "
  "deliberately two-sided. The line leans one way and the script does not. "
  "Balanced alternatives offered for consideration: TWO DIFFERENT JOBS, and "
  "NOT A HIGHER VERSION. No change made without approval."),
 ("V14 title", "CONDITIONAL, UNCHANGED",
  "The planning title stands. The numerical, past-tense title is blocked "
  "until the coded record exists. WHAT REALLY TRANSFERS? is carried and was "
  "never the part under the gate."),
]

ROUTES = [
 ("V15", "UNDECIDED", "The Field Kit route on this slot was carried for the "
  "after-40 topic and does not transfer with the number. The Career "
  "Decision Evidence Check is the closer fit for a video that ends on "
  "naming one gap and one next step. No resource is spoken in the draft, so "
  "this can be decided without a rewrite."),
 ("V16", "Keep the Proof", "Carried. Mentioned once, after the teaching."),
 ("V17", "Keep the Proof", "Carried. Mentioned once, after the teaching."),
 ("V18", "Career Decision Evidence Check", "Carried. Mentioned once."),
 ("V19", "Career Decision Evidence Check", "Carried. Mentioned once."),
 ("V20", "Field Kit", "Carried. Mentioned once."),
 ("V21", "Field Kit", "Carried. Mentioned once."),
]

WATCHNEXT = [
 ("V15", "V16", "Adjacent problems with different causes, and V16 is next "
  "in sequence."),
 ("V16", "V8", "V8 is the deeper version of the contribution record V16 "
  "ends on. The thematic destination is V22, which does not exist yet."),
 ("V17", "V11", "The companion question. V11 asks what you are still paid "
  "for, V17 asks how it is evidenced."),
 ("V18", "V16", "Both concern how an organization allocates scope. The "
  "thematic destination is V24, which does not exist yet."),
 ("V19", "V13", "V19 ends on conditions to test. V13 is the testing "
  "method."),
 ("V20", "V4", "The return conversation and the career-story conversation "
  "use the same muscle."),
 ("V21", "V9", "V21 is the after, V9 is the before."),
]

OVERLAP = [
 ("V17 against V11", "HIGHEST RISK IN THE BATCH",
  "Both sit on AI changing the work. The separation held in the draft: V11 "
  "asks what remains valuable, V17 assumes the value and asks how it is "
  "evidenced. V17's own distinction is output versus contribution, and its "
  "artifact is a record rather than a reassurance. WATCH AT REVIEW: if V11's "
  "finished script drifts toward evidence, V17 loses its job. Read the two "
  "together before either is recorded."),
 ("V15 against V25 and V30", "MEDIUM",
  "V25 diagnoses a stalled career and V30 chooses assignments. V15 stays "
  "narrower: one kind of judgment the prior work did not require, and three "
  "causes that look identical. Neither V25 nor V30 is written, so this is a "
  "constraint on them rather than a problem with V15."),
 ("V16 against V8", "MEDIUM",
  "Both end on a contribution record. V8 proves foundational work that now "
  "looks easy. V16 is recognition inside one organization, and its record "
  "is deliberately shorter: three items, four lines. The Watch Next handoff "
  "makes the relationship explicit rather than hiding it."),
 ("V19 against V13", "LOW, BY DESIGN",
  "V19 borrows V13's testing discipline and hands off to it rather than "
  "repeating the thirty-day plan. The draft names the test in one short "
  "section and does not build a method."),
 ("V21 against V9 and V14", "LOW",
  "V9 is the decision, V14 is the comparison method, V21 is after arrival. "
  "V21 is the only one of the three that says plainly that real relearning "
  "is required, which is the job it does for the whole channel."),
 ("V18 against V22", "TO WATCH",
  "V22 is promotion timing and remains unwritten. V18 is the shape of the "
  "next role. When V22 is drafted, keep the timing question out of V18 and "
  "the role-shape question out of V22."),
]

RESEARCH_NEEDED = [
 ("V14", "BLOCKING", "The whole comparison. Design is ready, nothing is "
  "collected or coded. Approve the role family, the three industries and "
  "the geographic scope before anything begins."),
 ("V17", "BLOCKING IF A REAL TOOL IS USED", "The draft uses a labeled "
  "constructed illustration, which is deliverable as written. If Temidayo "
  "would rather show a real tool, that requires verification at scripting "
  "time, the date, the tool and model, and the preserved prompt and "
  "response. The substitution rule is in the master."),
 ("V21", "BLOCKING IF A SPECIFIC REGULATION IS NAMED", "The draft names no "
  "regulation, license or professional body, and says on camera that it is "
  "deliberately not doing so. Naming one requires current, dated "
  "verification from the body that sets it."),
 ("V20", "NOT BLOCKING", "The draft uses a labeled constructed illustration "
  "and no personal story. If Temidayo has a real return experience she "
  "wants to use, it replaces the illustration and the label changes. Any "
  "specific return program named at recording must be checked and dated."),
 ("V19", "NOT BLOCKING", "Employment-constraint content is kept generic and "
  "routed to qualified advice. Nothing needs verifying unless a specific "
  "clause type or jurisdiction gets named, which the draft avoids."),
]

NOT_YET = [
 ("V14", "The script itself. Blocked by the research gate, not by "
  "capacity."),
 ("V15", "The thumbnail decision. The title and thumbnail should be judged "
  "as a pair and one half does not exist."),
 ("V15", "The resource route. Undecided, and the draft speaks no resource, "
  "so this does not require a rewrite."),
 ("V17", "Only if a real tool demonstration is wanted instead of the "
  "labeled illustration. As drafted it is recordable."),
 ("V18", "Only if the thumbnail line is judged too one-sided against a "
  "deliberately two-sided script."),
]


def build(out_path, stamp, videos, qa_rows, qa_passed):
    d = base_doc()
    footer_note(d, "Capability Formation  |  V14 to V21 editorial review  |  "
                   "Script drafts. Not locked, not approved for production.")

    title_block(d, "Capability Formation  |  Videos 14 to 21",
                "Editorial Review Summary",
                "What was drafted, what is still conditional, and what needs "
                "a decision before anything is recorded")
    kv(d, "Created", stamp)
    kv(d, "Status", "V14 RESEARCH DESIGN READY. V15 to V21 SCRIPT DRAFTS "
                    "READY FOR EDITORIAL REVIEW.")
    kv(d, "Sources", "Videos_1421_Roadmap_Addendum.docx and "
                     "Videos_1421_Development_Briefs.docx, which were "
                     "checked against the copies already in this workspace "
                     "and found identical.")

    callout(d, "Nothing here is approved speech. Seven script drafts exist. "
               "No script is locked, no production asset was built, and no "
               "video in this range is ready to publish. Video 14 has no "
               "script at all, by design.")

    h(d, "What was drafted")
    rows = []
    for v in videos:
        w, fast, slow = estimate(v)
        rows.append(["V%d" % v["num"], v["title"],
                     "{:,}".format(w), "%s to %s" % (fast, slow),
                     str(block_count(v))])
    table(d, ["#", "Title", "Spoken words", "Speech-only estimate",
              "Thought blocks"], rows,
          widths=[0.42, 2.75, 0.85, 1.5, 0.75], size=8.5)
    para(d, "Estimates are arithmetic on the script at the roadmap's own 130 "
            "to 145 words per minute band, counting the spoken script only. "
            "They exclude pauses and visual holds. No recording has been "
            "timed. Nothing was padded to reach a target, and nothing was "
            "cut to reduce one.", size=9.5, color=DIM)

    h(d, "Video 14, which was deliberately not scripted")
    para(d, "V14 has a research design, a codebook, a collection template, "
            "an exclusion log template and a status file. It has no script, "
            "no finding, no coded posting and no number. The conditional "
            "title appears in those files only inside its own prohibition.")
    bullets(d, [
      "Nothing has been collected. Nothing has been coded. There is no "
      "findings section, because there is no finding.",
      "The role family, the three industries and the geographic scope are "
      "proposals marked FOR APPROVAL. Collection cannot begin until they "
      "are settled, because changing them later invalidates the sample.",
      "Any eventual number is the count of postings actually coded and "
      "retained. If 26 are retained, the title says 26.",
      "A weak or mixed comparison gets published as weak or mixed, or the "
      "video does not get made.",
    ])

    h(d, "Title and thumbnail decisions needed")
    table(d, ["Item", "Standing", "What needs deciding"],
          [[a, b, c] for a, b, c in TITLE_ISSUES],
          widths=[1.15, 1.35, 4.2], size=8.5)

    h(d, "Resource route proposals")
    para(d, "No new product or offer is proposed. Every route is one of the "
            "four that already exist, and each script mentions a resource at "
            "most once, after the teaching, never as a second ask.",
         size=10, color=DIM)
    table(d, ["#", "Proposed route", "Note"],
          [[a, b, c] for a, b, c in ROUTES],
          widths=[0.45, 1.85, 4.4], size=8.5)

    h(d, "Watch Next proposals")
    para(d, "Proposals only, settled with the publishing plan. One "
            "constraint worth stating: a Watch Next cannot point at a video "
            "that does not exist when this one publishes. Two of the "
            "thematically strongest destinations, V22 and V24, are unwritten, "
            "so the proposals below route to videos that will already be "
            "published and record the eventual destination separately.",
         size=10, color=DIM)
    table(d, ["From", "Proposed to", "Why"],
          [[a, b, c] for a, b, c in WATCHNEXT],
          widths=[0.65, 1.0, 5.05], size=8.5)

    h(d, "Overlap risks")
    table(d, ["Pair", "Risk", "How the drafts hold the separation"],
          [[a, b, c] for a, b, c in OVERLAP],
          widths=[1.35, 1.25, 4.1], size=8.5)

    h(d, "Factual research still needed")
    table(d, ["#", "Standing", "What is needed"],
          [[a, b, c] for a, b, c in RESEARCH_NEEDED],
          widths=[0.45, 1.8, 4.45], size=8.5)

    h(d, "Any reason a script should not yet be recorded")
    para(d, "Six of the seven drafts are recordable as written, once "
            "approved. The reasons below are decisions, not defects.",
         size=10, color=DIM)
    table(d, ["#", "What is outstanding"], [[a, b] for a, b in NOT_YET],
          widths=[0.5, 6.2], size=9)
    callout(d, "V14 is the only genuine block. Its script cannot be written "
               "without the comparison, and the comparison has not been "
               "started.")

    h(d, "What was preserved, unchanged")
    bullets(d, [
      "Videos 1 to 13: scripts, assets, thumbnails, Shorts, publishing copy "
      "and routing. Not touched.",
      "The reserved employer due-diligence brief, Before You Accept the Job, "
      "Find Out How the Company Actually Uses People Like You. Still "
      "reserved, still unnumbered, no script written. In this brief, people "
      "like you refers to the experience, capability, seniority and "
      "contribution someone brings, and never to a demographic identity.",
      "The after-40 topic, How to Stay Relevant After 40 Without Chasing "
      "Every Trend, preserved in the forward queue with its thumbnail "
      "direction UPDATE. DON'T ERASE. and its Field Kit route. Not deleted "
      "and not renumbered.",
      "V22 remains No Promotion? How to Know Whether to Wait or Move On.",
      "The job-security theme stays a separate future brief, distinguishing "
      "job continuity from the strength of someone's options if the job "
      "ends. It was not folded into any of these seven scripts.",
      "The when-to-leave theme stays research input for V25 or a separate "
      "future decision video. It does not repeat V3, V6 or V12 and it was "
      "not folded into these scripts.",
      "V23 to V30 and the V31 capstone keep their positions.",
    ])

    h(d, "Where the two source documents disagreed")
    para(d, "One point only, and it is not a contradiction between the "
            "sources. The roadmap addendum recorded the slot 18 title "
            "punctuation as a variance to resolve at packaging, and recorded "
            "the V16 thumbnail hyphen as a copy decision to record. The "
            "current instruction settles both. Neither was resolved by "
            "inventing a third direction, and both are listed in the title "
            "and thumbnail table above.")

    h(d, "Quality checks")
    para(d, "%d checks run against the built documents rather than against "
            "the build scripts, so a check cannot pass because of something "
            "that was true only in the source data. %d passed."
            % (len(qa_rows), qa_passed), size=10, color=DIM)
    table(d, ["Check", "Result", "What it looked at"],
          [[n, "PASS" if ok else "FAIL", detail[0] if detail else ""]
           for n, ok, detail in qa_rows],
          widths=[2.35, 0.6, 3.75], size=8)

    h(d, "Standing requirements recorded for the production step")
    para(d, "No production asset was built and none is approved. These are "
            "recorded here so they carry into the eventual Riverside "
            "instruction rather than being rediscovered then. The scripts "
            "were written to be compatible with all of it.",
         size=10, color=DIM)
    sub(d, "Captions, which is the rule most easily lost")
    bullets(d, [
      "No burned-in or open captions anywhere in a long-form video. Viewers "
      "use YouTube CC.",
      "The eventual Riverside instruction must require: a clean export with "
      "no persistent burned-in subtitles; a complete final transcript; names, "
      "frameworks, URLs and industry terms proofread; an SRT generated from "
      "the FINAL edited timeline rather than from the script; synchronization "
      "checked after jump cuts and removals; and the SRT delivered with the "
      "final export.",
      "Shorts and Reels may still use designed captions. That exception does "
      "not extend to long-form.",
    ])
    sub(d, "Camera, sound and structure, from Video 4 onward")
    bullets(d, [
      "Camera-led teaching, horizontal 16:9, minimum 1920 by 1080, "
      "intentional jump cuts.",
      "About 3 to 5 deliberate camera-emphasis beats in total, gentle "
      "push-ins with occasional pull-backs. Not a set added on top of "
      "another set.",
      "About 2 to 4 meaningful full-screen B-roll moments where useful. True "
      "full-screen substantive motion graphics, with large mobile-readable "
      "typography.",
      "About 4 to 7 restrained sound accents for the whole video, including "
      "the one visual Subscribe cue. That is the total budget, not a rate.",
      "Watch Next is full screen and final. No return to camera afterward.",
      "No new equipment. The current camera setup is not reopened.",
    ])
    sub(d, "Sound at a visual change, which is a post-recording rule")
    bullets(d, [
      "Use a subtle click, tick, tap, restrained whoosh or clean transition "
      "sound only where a meaningful visual change lands: a new item "
      "appearing, a comparison changing sides, a framework advancing, a card "
      "replacing another, one important word or result revealed.",
      "Pair the sound with a small visual action so both land together. Text "
      "appearing, a divider moving, a number changing, a phrase "
      "highlighting.",
      "Not on every bullet, cut, sentence or screen change. Keep every "
      "effect clearly quieter than the voice. If a sound does not improve "
      "the moment, leave it silent.",
      "The visual maps in the masters mark the hero moments, which is where "
      "these choices should be made from. They are not a shot list and they "
      "do not authorize an asset.",
    ])

    h(d, "What was deliberately not created")
    bullets(d, [
      "Final production packages, and final Riverside Co-Creator prompts.",
      "Shorts packages.",
      "Finished thumbnails, and any thumbnail artwork.",
      "Final YouTube descriptions, pinned comments and tags.",
      "Motion-graphic image packages, CTA cards and Watch Next cards.",
      "Chapters, SRT files and music attribution.",
      "A Video 14 script.",
    ])
    para(d, "These come after the scripts are reviewed and approved. The "
            "visual maps in the masters are planning guidance and reference "
            "for the eventual editor. They are not assets and they are not "
            "an approval to build any.", size=10, color=DIM)

    rule(d)
    para(d, "V14 RESEARCH DESIGN READY. V14 FINAL SCRIPT BLOCKED PENDING "
            "DOCUMENTED RESEARCH.", size=10.5, bold=True, color=RED)
    para(d, "V15 TO V21 SCRIPT DRAFTS READY FOR EDITORIAL REVIEW. NOT YET "
            "LOCKED. NOT YET APPROVED FOR PRODUCTION.",
         size=10.5, bold=True, color=RED)
    d.save(out_path)
    return out_path
