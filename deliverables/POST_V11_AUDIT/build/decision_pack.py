# -*- coding: utf-8 -*-
"""Phase 1.5 decision pack. Decisions, options, and what needs Temidayo."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break)

EYEBROW = "capability formation | post-v11 phase 1.5"

PACK = [
 ("A", "What Your Background Proves, and What It Only Suggests",
  "PROVES / SUGGESTS",
  "Splits the viewer’s own history into two piles they have never "
  "separated, so they want to know which pile theirs is in."),
 ("B", "Close Enough for You. Not Yet Close Enough for Them.",
  "STILL NOT CLOSE ENOUGH",
  "Names the exact gap between the viewer’s confidence and the "
  "employer’s hesitation without blaming either."),
 ("C", "Adjacent Isn’t the Same as Qualified", "ADJACENT. NOT YET.",
  "States the distinction flatly, which makes the viewer ask which side "
  "of it their own experience sits on."),
 ("D", "I Read Two Job Postings the Way a Decision-Maker Might",
  "SAME WORDS. DIFFERENT JUDGMENT.",
  "Promises the read itself rather than a conclusion, and the hedge in "
  "might is doing real work: it refuses a universal rule."),
 ("E", "The Part of Your Experience They Can’t Verify Yet",
  "WHAT THEY CAN’T SEE",
  "Points at something specific and missing, and yet keeps it fixable."),
 ("F", "Same Words. Different Judgment.", "SIMILAR ISN’T THE SAME",
  "The shortest version. Reads fast on a phone and sets up the "
  "comparison before the video starts."),
 ("G", "What Happens When Your Experience Is Read by Someone Who "
       "Wasn’t There", "THEY WEREN’T IN THE ROOM",
  "Reframes the whole problem: the reader is missing context, not "
  "judgment, which protects the viewer’s dignity."),
]

REJECTED = [
 ("What a Hiring Manager Can Actually Tell From Your Experience",
  "Implies one universal hiring mind, which is the claim we are "
  "specifically avoiding, and it sounds like recruiter content."),
 ("The Experience Gap Hiring Managers Care About",
  "The current working title. Same universality problem, and gap is "
  "vaguer than the idea deserves."),
 ("Why Similar Experience Still Gets a No",
  "Asserts an outcome the evidence cannot support. The postings do not "
  "show hiring decisions."),
]

A = [
 ("V12", "V23", "Turn One Accomplishment Into Proof in 10 Minutes",
  "CAN YOU PROVE IT?", "Fulfils V6", "no",
  "The promise is explicit and by name, and it is the strongest "
  "commerce alignment in the library."),
 ("V13", "V14", "Which Parts of Your Experience Actually Transfer to "
                "Another Industry?", "SAME WORDS. DIFFERENT WORK.",
  "Fulfils V9", "no",
  "The applied version of V9, and the research behind it is now "
  "verified."),
 ("V14", "V17", "How to Prove Your Value When AI Does More of the Task",
  "SO WHAT DID YOU DO?", "Fulfils V4", "no",
  "Clears the AI promise and keeps the evidence thread running."),
 ("V15", "V16", "What to Do When Your Work Is Valued but You Are "
                "Overlooked", "RELIED ON. STILL SKIPPED.", "Fulfils V7",
  "no", "Clears the fourth promise and gives the slate a recognition "
        "episode after three evidence ones."),
 ("V16", "V35 rebuilt", "Before a Layoff, Know What You Can Still Prove",
  "KEEP THE EVIDENCE", "Fulfils V8", "no",
  "Clears the last promise. Title fixed by V8."),
 ("V17", "V21", "What You Must Relearn When You Change Industries",
  "EXPERIENCED AND NEW", "none", "n/a",
  "First unpromised slot. Pairs with V13."),
 ("V18", "V31 rebuilt", "Employer-read episode. Title to be chosen.",
  "See packaging options", "none", "n/a",
  "The lane-defining episode, arriving seventh."),
 ("V19", "V15", "The Career Gaps You Don’t See Until the Work Gets "
                "Harder", "WHAT DO YOU RECOMMEND?", "none", "n/a",
  "Capability behind the bigger role."),
 ("V20", "V25", "If Your Role Expands but Your Authority Doesn’t",
  "MORE SCOPE. SAME POWER.", "none", "n/a",
  "Isolates authority."),
 ("V21", "V18", "Should You Stay an Individual Contributor or Become a "
                "Manager?", "TWO JOBS. NOT TWO LEVELS.", "none", "n/a",
  "Decision episode, Career Move Review."),
]

B = [
 ("V12", "V23", "Turn One Accomplishment Into Proof in 10 Minutes",
  "CAN YOU PROVE IT?", "Fulfils V6", "no",
  "Unchanged. The most explicit promise goes first in both options."),
 ("V13", "V14", "Which Parts of Your Experience Actually Transfer to "
                "Another Industry?", "SAME WORDS. DIFFERENT WORK.",
  "Fulfils V9", "no",
  "Unchanged, and it becomes the setup for the next slot rather than a "
  "standalone."),
 ("V14", "V31 rebuilt", "Employer-read episode. Title to be chosen.",
  "See packaging options", "none", "n/a",
  "Moved forward four slots. It sits immediately after the transfer "
  "read because it is the same artifact behaviour turned around: V13 "
  "asks what travels, this asks what a reader can see."),
 ("V15", "V17", "How to Prove Your Value When AI Does More of the Task",
  "SO WHAT DID YOU DO?", "Fulfils V4", "one slot",
  "Delayed one slot. V4 is the oldest of the outstanding promises, so "
  "this is the delay most likely to be noticed."),
 ("V16", "V16", "What to Do When Your Work Is Valued but You Are "
                "Overlooked", "RELIED ON. STILL SKIPPED.", "Fulfils V7",
  "one slot", "Delayed one slot. Low risk."),
 ("V17", "V35 rebuilt", "Before a Layoff, Know What You Can Still Prove",
  "KEEP THE EVIDENCE", "Fulfils V8", "one slot",
  "Delayed one slot. Low risk, and the rebuild needs the time anyway."),
 ("V18", "V21", "What You Must Relearn When You Change Industries",
  "EXPERIENCED AND NEW", "none", "n/a",
  "Now follows three employer-side and evidence episodes, which makes "
  "the relearning feel earned rather than discouraging."),
 ("V19", "V15", "The Career Gaps You Don’t See Until the Work Gets "
                "Harder", "WHAT DO YOU RECOMMEND?", "none", "n/a",
  "Unchanged position relative to Option A."),
 ("V20", "V25", "If Your Role Expands but Your Authority Doesn’t",
  "MORE SCOPE. SAME POWER.", "none", "n/a", "Unchanged."),
 ("V21", "V18", "Should You Stay an Individual Contributor or Become a "
                "Manager?", "TWO JOBS. NOT TWO LEVELS.", "none", "n/a",
  "Unchanged."),
]

SPEC = {
 "V23": ("What can you prove?",
         "One accomplishment as currently written, read line by line. "
         "Synthetic and labelled.",
         "What a reader can recognize from the sentence, what they must "
         "take on trust, and what they would need to see.",
         "Proof is not hiring. A clean record does not remove a "
         "credential gap or a market.",
         "Career Evidence Starter, then Keep the Proof."),
 "V14": ("What travels? What does not?",
         "Three real postings that all say manage risk.",
         "What the same word is standing on in each posting, and what "
         "each employer would still require evidence for.",
         "The postings show what these employers wrote. Counts are "
         "facts about the 28, not about any industry.",
         "Field Kit."),
 "V17": ("What can you prove?",
         "Before and after of one deliverable, with the decisions that "
         "were never in the output marked.",
         "What a reviewer can infer from an output two people could now "
         "produce.",
         "Faster is not worse. The question is what record exists for "
         "the judgment.",
         "Career Evidence Starter."),
 "V16v": ("What can you prove?",
          "Optional. The role description for work allocated elsewhere.",
          "What being the person everyone calls demonstrates, and what "
          "it does not demonstrate about the next level.",
          "Access, sponsorship, timing and bias affect allocation. Not "
          "a merit explanation.",
          "Career Evidence Starter."),
 "V35": ("What can you prove?",
         "Optional. The record itself, partly built.",
         "What survives as evidence when the system that held it does "
         "not.",
         "Keep the proof, not the property. Lawful record of your own "
         "work only. Never employer files, customer information, "
         "confidential material or proprietary documents.",
         "Keep the Proof."),
 "V21v": ("What must you relearn?",
          "Optional. A decision that went a direction the person would "
          "not have predicted.",
          "What a new employer assumes is obvious and never says out "
          "loud.",
          "The old experience did not disappear. The room has context "
          "not yet earned.",
          "Field Kit."),
 "V31": ("What does not travel? What can you prove?",
         "Two real postings using the same language and requiring "
         "different judgment, side by side.",
         "The whole episode. What is recognized, what is inferred, what "
         "is discounted, and what still requires evidence.",
         "No universal hiring rule. These employers wrote these words. "
         "Other employers read differently.",
         "Field Kit, or Career Move Review where the move is "
         "consequential."),
 "V15v": ("What must you relearn?", "Optional, and probably not.",
          "What a leader reads into an answer that explains instead of "
          "recommending.",
          "Three gaps need three responses. Reading the wrong one costs "
          "a year.",
          "None, or Career Evidence Starter."),
 "V25": ("What can you prove?",
         "The role as written against the decisions actually owned.",
         "What expanded responsibility without expanded authority "
         "demonstrates, and what it cannot.",
         "Responsibility is not growth. Exposure is not carrying the "
         "decision.", "None."),
 "V18v": ("What travels? What must you relearn?",
          "The management job description, read against what the person "
          "is being congratulated for.",
          "What the organization is asking for, and what it will "
          "evaluate a year from now.",
          "No recommendation. The right answer depends on a life and an "
          "organization not visible from here.",
          "Career Move Review."),
}
KEY = {"V23": "V23", "V14": "V14", "V17": "V17", "V16": "V16v",
       "V35 rebuilt": "V35", "V21": "V21v", "V31 rebuilt": "V31",
       "V15": "V15v", "V25": "V25", "V18": "V18v"}


def seq_pages(d, rows, label):
    h(d, label)
    table(d, ["Slot", "Source", "Title", "Thumbnail", "Promise",
              "Delay"],
          [[a, b, c[:40], t[:22], p, dl] for a, b, c, t, p, dl, w in rows],
          widths=[0.5, 1.0, 2.2, 1.3, 0.9, 0.8], size=7)
    for a, b, c, t, p, dl, w in rows:
        k = KEY.get(b)
        s = SPEC.get(k) if k else None
        sub(d, "%s  |  %s" % (a, c))
        rowdata = [["Why this slot", w],
                   ["Fulfils", p if p != "none" else
                    "No outstanding promise."],
                   ["Delay cost", "None." if dl in ("no", "n/a") else
                    "Delayed %s. %s" % (dl, w)]]
        if s:
            rowdata += [["Primary audit question", s[0]],
                        ["Artifact", s[1]],
                        ["Employer-side read", s[2]],
                        ["Boundary", s[3]],
                        ["Natural offer", s[4]]]
        table(d, ["", ""], rowdata, widths=[1.7, 5.0], size=8)


def build(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Post-V11 final architecture decision pack",
                "Phase 1.5. Decisions, two sequences, and what needs you.")
    kv(d, "Prepared", st)
    kv(d, "Scope", "Decision and reconciliation only. No script "
                   "rewritten, no package built, V4 to V11 untouched.")
    kv(d, "Headline", "The 28-posting denominator is verified and can be "
                      "carried. Provenance is stronger than expected.")

    h(d, "1. Locked from Phase 1")
    bullets(d, [
      "The central diagnosis, with the amendment that story remains the "
      "vehicle. Lived experience stays for recognition, warrant, "
      "authority, connection and evidence. It is not the destination.",
      "One canonical audit: what travels, what does not, what can you "
      "prove, what must you relearn. No second public framework.",
      "V37 retires as a standalone. Its thinking about problem, "
      "judgment, evidence and context survives inside other analyses.",
      "Watch-Me-Read is a behaviour, not a format. Artifacts where they "
      "teach, nowhere they decorate.",
      "The layoff episode keeps V8’s promised title and is rebuilt "
      "from the strongest treatment, including the V35 material. V8 is "
      "not reopened. Keep the proof, not the property stays explicit.",
      "The transfer episode keeps its real-posting comparison. Its "
      "internal four-part structure stays inside the analysis and is "
      "never named as a framework.",
      "Ten retirements confirmed: six made as current V4 to V11, plus "
      "V36, V30, V34 and V32 folded or held, plus V37.",
    ], size=10)

    h(d, "2. Still unresolved")
    table(d, ["", "Status"],
          [["The employer-read title",
            "Seven options below. Not locked."],
           ["Sequence", "Two options below. Yours to choose."],
           ["V14 employer naming",
            "The research names Wells Fargo, Humana, CVS, Gilead and "
            "others. V6 anonymized its employers. New decision, because "
            "the claims here are about role language rather than pay."],
           ["The older V5 promise",
            "V5 still promises a biography-led title. Same shape as the "
            "V8 decision you just made. My reading is that the same "
            "answer applies: keep the promised title, rebuild the "
            "treatment. Not assumed."],
           ["V12 and V13",
            "Held. The constraint episode needs its portability read; "
            "the thirty-day episode needs a rebuild or a merge. Neither "
            "blocks the slate."]],
          widths=[1.8, 4.9], size=8.5)

    page_break(d)
    h(d, "3. The 28 postings: verified")
    callout(d, "A full coded research record exists in the workspace and "
               "supports the denominator. It was not reconstructed, and "
               "no new research was done.")
    table(d, ["", "What the record contains"],
          [["Where", "VIDEOS_14-21_FINAL_PRODUCTION/_source/"
                     "what-really-transfers-research.md, with copies in "
                     "the V14 package and the corrected-runtime build."],
           ["Sample", "About 55 surfaced, 40 fetched and evaluated in "
                      "full, 28 retained, 18 excluded with a logged "
                      "reason. Healthcare 10, financial services 10, "
                      "technology 8."],
           ["Per posting", "Employer, exact title, URL, collection date, "
                           "requisition or window dates, and whether the "
                           "text came from the employer page or a "
                           "mirror. Coded across capability, domain, "
                           "credential, tool and stated experience, with "
                           "hard against preferred marked."],
           ["Collection date", "September 10, 2026, for every posting."],
           ["Limits", "A limitations section that already refuses the "
                      "overclaims: cannot show roles are "
                      "interchangeable, cannot predict hiring, cannot "
                      "show the posting reflects the job, not "
                      "representative of any industry, every count is a "
                      "count within these 28."]],
          widths=[1.4, 5.3], size=8)
    para(d, "One conflict worth naming. A status note dated September 10 "
            "at 12:23 in the afternoon says no postings had been "
            "collected and the script was blocked. The research file "
            "records collection on the same day. The research is the "
            "later artifact and it contains the evidence, so it governs. "
            "The status note is stale rather than contradictory.",
         size=10.5, before=6)
    sub(d, "Two production notes, not blockers")
    bullets(d, [
      "Six postings carry 2025 or early 2026 dates and several "
      "technology postings show no longer accepting applications. The "
      "record discloses this. The script must not imply the postings are "
      "live, only that the text was captured on the collection date.",
      "The employer-naming decision above. The record names employers; "
      "the on-screen treatment is a separate choice.",
    ], size=10)
    para(d, "Consequence for the sequence: the employer-read episode can "
            "be built on this same verified record rather than needing "
            "new research. That materially lowers the cost of moving it "
            "forward, which is the main practical argument for Option "
            "B.", size=10.5, before=6)

    page_break(d)
    h(d, "4. Employer-read packaging options")
    para(d, "Seven directions. Each shows the read rather than announcing "
            "a rule about hiring managers.", size=10.5)
    table(d, ["", "Title", "Thumbnail", "Curiosity gap"],
          [[a, b, c, e] for a, b, c, e in PACK],
          widths=[0.3, 2.2, 1.4, 2.8], size=7.5)
    sub(d, "Considered and set aside")
    table(d, ["Title", "Why not"],
          [[a, b] for a, b in REJECTED], widths=[2.4, 4.3], size=7.5)
    para(d, "On the thumbnail: SIMILAR ISN’T THE SAME still reads "
            "well and pairs with several titles. It is not assumed "
            "final. ADJACENT. NOT YET. and SAME WORDS. DIFFERENT "
            "JUDGMENT. both carry more of the actual distinction, and "
            "PROVES / SUGGESTS is the most specific of the set.",
         size=10.5, before=6)

    page_break(d)
    seq_pages(d, A, "5. Option A. Promise-first.")
    page_break(d)
    seq_pages(d, B, "6. Option B. Positioning-first, promises protected.")

    page_break(d)
    h(d, "7. Tradeoffs, side by side")
    table(d, ["", "Option A", "Option B"],
          [["All promises cleared by", "Slot 5", "Slot 6"],
           ["Promises delayed", "None",
            "Three, by one slot each: V4, V7 and V8"],
           ["Lane-defining episode arrives", "Slot 7", "Slot 3"],
           ["Hardest build sits at", "Slot 7, with six slots of runway",
            "Slot 3, with two"],
           ["First three slots are",
            "Proof, transfer, AI proof. All evidence.",
            "Proof, transfer, employer read. Evidence, then the turn."],
           ["Thematic flow",
            "Clean but conventional: the channel finishes what it "
            "started, then changes gear.",
            "Stronger: the transfer episode asks what travels and the "
            "next one asks what a reader can see. Same artifact, turned "
            "around."],
           ["Trust risk",
            "Lowest. Nobody waits.",
            "Low but real. A viewer who watched V4 waits one more "
            "release."],
           ["Schedule risk",
            "Low. Four of the first five need cleanup, not rebuilding.",
            "Higher. A substantial revision lands third. Reduced by the "
            "verified research being reusable."],
           ["Commerce pacing",
            "Field Kit at slot 2, then Career Evidence Starter twice.",
            "Field Kit at slots 2 and 3 back to back, which is either "
            "focus or repetition depending on the CTA wording."],
           ["What it signals",
            "We keep our word.", "We keep our word, and here is what "
                                 "this channel is for."]],
          widths=[1.6, 2.5, 2.6], size=8)
    para(d, "The honest summary: Option A is safer and slower to say "
            "what the channel is. Option B says it third, costs three "
            "viewers one release each, and concentrates the hardest "
            "build early. The verified research makes B more feasible "
            "than it looks. I am not choosing.", size=10.5, before=6)

    h(d, "8. Where the artifact is essential")
    table(d, ["Essential", "Optional", "Would decorate"],
          [["The transfer episode. Three postings saying manage risk. "
            "The point cannot be asserted.",
            "The overlooked episode. The role description for work "
            "allocated elsewhere.",
            "The career-gaps episode. It turns on a question changing."],
           ["The employer-read episode. Without two postings on screen "
            "it is an opinion about hiring.",
            "The layoff episode. A partly built record.",
            "The relearn episode. The feeling is the teaching."],
           ["One accomplishment. The rewrite only teaches if the first "
            "version is visible.",
            "The authority episode. Role as written against decisions "
            "owned.", ""],
           ["IC or manager. The management job description answers the "
            "hook directly.",
            "The AI proof episode. Before and after of one deliverable.",
            ""]],
          widths=[2.4, 2.2, 2.1], size=7.5)

    h(d, "9. Offer check")
    table(d, ["Offer", "Where", "Where it would be forced"],
          [["Career Evidence Starter",
            "One accomplishment, AI proof, overlooked.",
            "Before the viewer has seen that their evidence is thin."],
           ["Keep the Proof, $49", "The layoff episode.",
            "Where a record already exists."],
           ["Field Kit, $150",
            "Transfer, employer read, relearn.",
            "With no destination in view."],
           ["Career Move Review, $500", "IC or manager. Consultant "
                                        "later.",
            "Where the move is not yet consequential."],
           ["None", "Career gaps, authority, and the cannot-leave-yet "
                    "episode.",
            "The last especially. Selling into a constraint someone has "
            "just admitted they cannot escape would be the wrong "
            "instinct."]],
          widths=[1.5, 2.6, 2.6], size=8)
    para(d, "One pacing note for Option B: Field Kit lands at slots 2 "
            "and 3 consecutively. Either vary the wording or let the "
            "employer-read episode carry Career Move Review instead.",
         size=10.5, before=6)

    page_break(d)
    h(d, "10. Decisions needed before Phase 2")
    table(d, ["", "Decision"],
          [["1. Sequence", "Option A or Option B."],
           ["2. Employer-read title",
            "One of the seven, or a direction to keep working."],
           ["3. Employer-read thumbnail",
            "SIMILAR ISN’T THE SAME, or one of the alternatives."],
           ["4. V14 employer naming",
            "Name the employers as the research does, or anonymize as V6 "
            "does."],
           ["5. The V5 promise",
            "Keep the promised biography-led title and rebuild the "
            "treatment, as you decided for V8, or change it."],
           ["6. V12 and V13",
            "Hold both, rebuild V13, or merge V13 into V12."],
           ["7. Consultant and career-break slots",
            "Both are ready and neither is scheduled. Confirm they wait."],
           ["8. Phase 2 scope",
            "Whether Phase 2 covers the whole ten-slot slate or only the "
            "first three."]],
          widths=[1.5, 5.2], size=8.5)
    footer_note(d, "Phase 1.5 complete. Nothing rewritten, nothing built, "
                   "V4 to V11 untouched. Stopping for your decision.")
    d.save(path)
    return path


if __name__ == "__main__":
    print(build(os.path.join(
        OUT, "POST-V11_FINAL_ARCHITECTURE_DECISION_PACK.docx"),
        "Monday, September 21, 2026 | CT"))
