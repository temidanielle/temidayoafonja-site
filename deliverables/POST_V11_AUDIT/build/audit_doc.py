# -*- coding: utf-8 -*-
"""Post-V11 strategic reconciliation and roadmap audit. Phase 1 only.

Nothing is rewritten here. This reads the current V4 to V11 masters, the
V12 to V21 story-led packages and the V22 to V38 roadmap extension, and
decides what deserves to exist after V11.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break)

EYEBROW = "capability formation | post-v11 audit"

# ---------------------------------------------------------------- V12-V21
LIB = [
 ("V12", "What to Do When You Can’t Quit Your Job Yet",
  "MOVE / HOLD, then LIGHT STRENGTHEN",
  "The constraint framing is real and it protects dignity: it starts "
  "from what the paycheck has to cover rather than from just leave. "
  "That is worth keeping. What it does not yet do is connect the "
  "constraint to portability. It plans around staying without asking "
  "what staying is still building, still preserving, or quietly "
  "costing. Move it later in the sequence and add that read. It needs "
  "no artifact and should carry no offer."),
 ("V13", "A 30-Day Plan to Test Your Next Career Move",
  "SUBSTANTIAL REVISION, or MERGE into V12",
  "This is the closest thing in the library to generic career advice. "
  "It structures activity: read, talk, sample. The evidence standard "
  "section and the safety boundary are what save it. Rebuild it around "
  "what thirty days can and cannot prove to an employer, which is the "
  "employer-side read, or fold the testing into the can-not-leave-yet "
  "episode where the constraint makes the test meaningful."),
 ("V14", "Which Parts of Your Experience Actually Transfer to Another "
         "Industry?",
  "KEEP, LIGHT STRENGTHEN",
  "The strongest episode in the library and the clearest Watch-Me-Read "
  "in existence. Three real postings, healthcare, financial services "
  "and technology, all saying manage risk and meaning different "
  "decisions. It already carries an employer-side section, an explicit "
  "what-not-to-claim boundary and a stated sample of 28 postings. Two "
  "items to resolve before production, both listed under risks."),
 ("V15", "The Career Gaps You Don’t See Until the Work Gets Harder",
  "LIGHT STRENGTHEN",
  "The hypothesis holds. The pivot is the question changing from can "
  "you do this to what do you think we should do, which is exactly "
  "knowing the work against being trusted to make the call. Three gaps "
  "and three responses is already a real read. Strengthen by naming "
  "what a decision-maker can recognize in each gap."),
 ("V16", "What to Do When Your Work Is Valued but You Are Overlooked",
  "LIGHT STRENGTHEN",
  "Relied on, then skipped is a precise situation and the script "
  "already refuses the obvious answer of becoming louder. The "
  "opportunity the note suggests is real: compare what being relied "
  "upon demonstrates with what the larger role actually requires. That "
  "comparison is the employer-side read and it is currently implied "
  "rather than shown."),
 ("V17", "How to Prove Your Value When AI Does More of the Task",
  "LIGHT STRENGTHEN",
  "So what did you actually do is the employer-side question, asked "
  "directly. The script already separates the visible output from the "
  "scarce part. Strengthen by naming which capability was being formed "
  "in the old version of the task, which keeps it distinct from "
  "current V4 rather than repeating it."),
 ("V18", "Should You Stay an Individual Contributor or Become a Manager?",
  "LIGHT STRENGTHEN",
  "Two jobs, not two levels is already the correct frame, and being "
  "congratulated before the job is described is a strong, ordinary "
  "hook. An artifact would materially help here: the actual management "
  "job description, read on camera, against what the person is being "
  "congratulated for."),
 ("V19", "Should You Become a Consultant? The Part Everyone Leaves Out",
  "LIGHT STRENGTHEN",
  "Twenty years of experience can still leave you with nothing a client "
  "knows how to buy is the distinction the note asks for, and it is "
  "already in the script. This is internal usefulness against "
  "externally legible capability. The best Career Move Review "
  "alignment in the library."),
 ("V20", "How to Return After a Career Break Without Starting at Zero",
  "LIGHT STRENGTHEN",
  "The maternity-leave opening is lived experience used as evidence "
  "rather than as destination, and it earns the emotional weight. The "
  "portability read the note asks for is partly there. Strengthen by "
  "separating what still travels, what evidence still holds, what "
  "changed in the field and what genuinely needs rebuilding."),
 ("V21", "What You Must Relearn When You Change Industries",
  "KEEP, LIGHT STRENGTHEN",
  "Core territory for experienced and new at the same time, and the "
  "phrase is already earned rather than asserted: you can still do the "
  "work, and the room has context you have not earned yet. This is the "
  "relearn column of the permanent audit, given a whole episode."),
]

# ---------------------------------------------------------------- V22-V38
EXT = [
 ("V22", "Decode a Job Description in 10 Minutes", "RETIRE / SUPERSEDED",
  "Made. This is current V6, same title, same thumbnail."),
 ("V23", "Turn One Accomplishment Into Proof in 10 Minutes",
  "KEEP. PROMOTE TO NEXT.",
  "Not made, and current V6 ends by promising it by name. That promise "
  "is locked, so this is the next video whatever else changes. It is "
  "artifact-led, it sits directly on the Career Evidence Starter and "
  "Keep the Proof path, and it is already written."),
 ("V24", "I’ve Seen Who Gets the Bigger Role and Why",
  "RETIRE / SUPERSEDED", "Made. This is current V7."),
 ("V25", "If Your Role Expands but Your Authority Doesn’t",
  "KEEP, LIGHT STRENGTHEN",
  "Survives the duplicate check. Current V11 reads expected against "
  "actual role; this isolates authority as the variable that did not "
  "move when responsibility did. It carries responsibility is not "
  "growth and exposure is not carrying the decision, both canonical."),
 ("V26", "AI Took the Task. Who Gets the Experience?",
  "RETIRE / SUPERSEDED", "Made. This is current V4."),
 ("V27", "Transferable Skills Advice Is Missing Something",
  "RETIRE / SUPERSEDED",
  "Made. This is current V9, which carries the canonical four "
  "questions."),
 ("V28", "What Disappears When Your Work Access Ends",
  "RETIRE / SUPERSEDED", "Made. This is current V8."),
 ("V29", "Career Ladders Don’t Work Like They Used To", "MOVE / HOLD",
  "The weakest portability specificity in the extension. It describes a "
  "change in career architecture rather than reading anyone’s "
  "experience, and there is no artifact in it. Hold until it can be "
  "anchored to a real internal role or a real promotion path."),
 ("V30", "Your AI Productivity Gain May Have a Career Cost",
  "MERGE into the V17 rebuild",
  "Four hours became forty minutes is the same opening move as current "
  "V4 and as V17. As its own episode it repeats. As a section inside "
  "the AI proof video it sharpens the distinction between faster and "
  "better."),
 ("V31", "The Experience Gap Hiring Managers Care About",
  "SUBSTANTIAL REVISION. PROMOTE.",
  "The purest employer-side concept in the whole library, and the one "
  "that most needs rebuilding. At present it asserts how employers "
  "read experience. Put two real postings on screen and read them, and "
  "it becomes the lane-defining episode. It must not claim a universal "
  "hiring rule."),
 ("V32", "Change Industries Without Direct Experience",
  "MERGE into V14 and V21",
  "Sits between two stronger episodes and duplicates both. Its "
  "credential and regulation protections are already present in V14’s "
  "what-not-to-claim and in V21’s relearning."),
 ("V33", "If Your Company Needs You but Won’t Grow You",
  "RETIRE / SUPERSEDED", "Made. This is current V5."),
 ("V34", "If AI Takes This Part of Your Job, Watch Closely",
  "MERGE into current V4’s territory, or HOLD",
  "Judgment-bearing work is the part to protect is current V4’s "
  "argument. Nothing here is wrong; there is just not a second episode "
  "in it yet."),
 ("V35", "A Layoff Can Take Your Job, Not Your Proof",
  "HOLD pending one decision",
  "Current V8 ends by promising Before a Layoff, Know What You Can "
  "Still Prove, which is an older script. This is the newer, better "
  "written treatment of the same ground. Which one carries that "
  "promise is a decision, not an audit finding. See risks."),
 ("V36", "If More Work Keeps Coming, Are You Growing?",
  "RETIRE / SUPERSEDED",
  "Duplicates current V5 and overlaps V25. It was written as a "
  "reserve entry point, and the entry point now exists."),
 ("V37", "Stop Asking Whether Your Skills Transfer", "RETIRE",
  "It runs on the superseded four questions: what problem have I "
  "solved, what judgment did I use, what proof do I have, what is "
  "specific to the new context. The permanent audit replaced that. The "
  "ideas about problem, judgment and context stay useful inside "
  "analysis, which is where V14 and V15 already use them."),
 ("V38", "What Happens When AI Removes the Junior Work?", "MOVE / HOLD",
  "Its audience is the employer and the talent pipeline, not the "
  "experienced professional. That makes it off-territory for the "
  "public front door. It may be stronger as writing than as an "
  "episode."),
]

# ------------------------------------------------------------ the sequence
SEQ = [
 dict(num="V12", src="from V23",
      title="Turn One Accomplishment Into Proof in 10 Minutes",
      thumb="CAN YOU PROVE IT?",
      problem="I know I did good work. I cannot say it in a way anyone "
              "outside my team can evaluate.",
      artifact="One accomplishment as the professional currently words "
               "it, on screen, then read line by line. Synthetic and "
               "labelled, as the existing script already does.",
      audit="What can you prove?",
      employer="What a decision-maker can recognize from the sentence as "
               "written, what they would still have to take on trust, "
               "and what they would need to see.",
      boundary="Proof is not the same as being hired. A clean record "
               "does not remove a credential gap, a market, or a "
               "hiring manager’s constraints.",
      tension="The gap between knowing you did it and being able to "
              "show it.",
      offer="Career Evidence Starter, then Keep the Proof where the "
            "record has to be reconstructed.",
      rel="Current V6 ends by promising this video by name. Current V8 "
          "supplies the reason the record has to exist before access "
          "ends.",
      level="LIGHT STRENGTHEN. Conversational cleanup and one "
            "employer-side pass."),
 dict(num="V13", src="from V14",
      title="Which Parts of Your Experience Actually Transfer to Another "
            "Industry?",
      thumb="SAME WORDS. DIFFERENT WORK.",
      problem="The postings in the industry I want look like the work I "
              "already do. I cannot tell whether that is true.",
      artifact="Three real postings, healthcare, financial services and "
               "technology, all saying manage risk. Read on camera "
               "against what the person would actually have to decide.",
      audit="What travels? What does not?",
      employer="What the same word is standing on top of in each "
               "posting, and what an employer in each industry would "
               "still require evidence for.",
      boundary="The postings show what these employers chose to write "
               "down. They do not show the work, predict a hiring "
               "decision or make two roles the same.",
      tension="Recognition that the familiar word was hiding a "
              "different decision.",
      offer="Field Kit. This is the video where what travels, what does "
            "not, what I can prove and what I must relearn becomes a "
            "real piece of work.",
      rel="Current V9 ends by promising this video by name. It is the "
          "applied version of V9’s argument.",
      level="LIGHT STRENGTHEN, with two items resolved first. See "
            "risks."),
 dict(num="V14", src="from V17, absorbing V30",
      title="How to Prove Your Value When AI Does More of the Task",
      thumb="SO WHAT DID YOU DO?",
      problem="The tool produces most of the output now. I cannot "
              "describe my own contribution without sounding like I did "
              "less.",
      artifact="A before-and-after of the same deliverable, with the "
               "decisions that were never in the output marked.",
      audit="What can you prove?",
      employer="What a reviewer can infer from an output that two "
               "people could now produce, and what would distinguish "
               "them.",
      boundary="Faster is not worse. The question is what record exists "
              "for the judgment, not whether the tool should be used.",
      tension="Being more productive and less legible at the same "
              "time.",
      offer="Career Evidence Starter.",
      rel="Current V4 ends by promising this video by name. V4 asks who "
          "gets the experience; this asks how the person shows what "
          "they still did.",
      level="LIGHT STRENGTHEN, plus the productivity-against-capability "
            "section absorbed from V30."),
 dict(num="V15", src="from V16",
      title="What to Do When Your Work Is Valued but You Are Overlooked",
      thumb="RELIED ON. STILL SKIPPED.",
      problem="They bring me the hard things and my name is still not "
              "in the room when the bigger work is allocated.",
      artifact="Optional. The role description for the work that was "
               "allocated elsewhere, against what the person is "
               "actually called for.",
      audit="What can you prove?",
      employer="What being the person everyone calls demonstrates, and "
               "what it does not demonstrate about the next level.",
      boundary="Access, sponsorship, timing and bias affect allocation. "
               "This is not a merit explanation.",
      tension="Being trusted with difficulty and still not considered "
              "for scope.",
      offer="Career Evidence Starter.",
      rel="Current V7 ends by promising this video by name. V7 reads "
          "the room; this reads the individual situation.",
      level="LIGHT STRENGTHEN. Add the comparison the note asks for."),
 dict(num="V16", src="decision required. V35 or the older layoff script",
      title="Before a Layoff, Know What You Can Still Prove",
      thumb="KEEP THE EVIDENCE",
      problem="If this ends suddenly, what can I still say about my own "
              "work?",
      artifact="Optional. The record itself, partially built.",
      audit="What can you prove?",
      employer="What survives as evidence when the system that held it "
               "does not.",
      boundary="Keep the proof, not the property. Lawful record of your "
               "own work, never employer files, customer data or "
               "confidential information.",
      tension="Preparing for something you hope will not happen, "
              "without living in fear of it.",
      offer="Keep the Proof.",
      rel="Current V8 ends by promising this exact title. Whichever "
          "script carries it must keep that title or the promise "
          "breaks.",
      level="DECISION FIRST, then SUBSTANTIAL REVISION. See risks."),
 dict(num="V17", src="from V21",
      title="What You Must Relearn When You Change Industries",
      thumb="EXPERIENCED AND NEW",
      problem="I can do the work. I keep missing things nobody thought "
              "to explain.",
      artifact="Optional. A decision that went a direction the person "
               "would not have predicted, unpacked.",
      audit="What must you relearn?",
      employer="What a new employer assumes is obvious, and what they "
               "would never think to say out loud.",
      boundary="The old experience did not disappear. The room has "
               "context that has not been earned yet.",
      tension="Experienced and new at the same time, genuinely earned "
              "rather than asserted.",
      offer="Field Kit.",
      rel="The relearn column of the permanent audit, given a whole "
          "episode. Pairs with V13.",
      level="LIGHT STRENGTHEN."),
 dict(num="V18", src="from V31, rebuilt",
      title="The Experience Gap Hiring Managers Care About",
      thumb="SIMILAR ISN’T THE SAME",
      problem="My background looks close enough to me. It keeps not "
              "looking close enough to them.",
      artifact="Two real postings that use the same language and "
               "require different judgment, read side by side.",
      audit="What does not travel? What can you prove?",
      employer="The whole episode. What is recognized, what is "
               "inferred, what is discounted, and what still requires "
               "evidence.",
      boundary="No universal hiring rule. Employers differ, and the "
               "postings are what these employers wrote down.",
      tension="Being told you are a strong candidate and not being "
              "moved forward.",
      offer="Field Kit, or Career Move Review where the move is "
            "consequential.",
      rel="Extends current V6 and current V9 into the employer-side "
          "lane. This is the lane-defining episode.",
      level="SUBSTANTIAL REVISION. It currently asserts what it should "
            "demonstrate."),
 dict(num="V19", src="from V15",
      title="The Career Gaps You Don’t See Until the Work Gets Harder",
      thumb="WHAT DO YOU RECOMMEND?",
      problem="I know the work. I froze when someone asked me what we "
              "should do.",
      artifact="Optional.",
      audit="What must you relearn?",
      employer="What a leader reads into an answer that explains "
               "instead of recommending.",
      boundary="Three different gaps need three different responses. "
               "Reading the wrong one costs a year.",
      tension="The question changing under you without warning.",
      offer="None, or Career Evidence Starter.",
      rel="Sits behind current V7 and V10: this is the capability the "
          "bigger role was asking for.",
      level="LIGHT STRENGTHEN."),
 dict(num="V20", src="from V25",
      title="If Your Role Expands but Your Authority Doesn’t",
      thumb="MORE SCOPE. SAME POWER.",
      problem="More of the outcome sits with me and none of the "
              "decisions do.",
      artifact="The role as described against the decisions the person "
               "can actually make.",
      audit="What can you prove?",
      employer="What expanded responsibility without expanded authority "
               "demonstrates, and what it cannot.",
      boundary="Responsibility is not growth. Exposure is not carrying "
               "the decision.",
      tension="Carrying the outcome without the authority to shape it.",
      offer="None.",
      rel="Distinct from current V11, which reads expected against "
          "actual. This isolates authority.",
      level="LIGHT STRENGTHEN."),
 dict(num="V21", src="from V18",
      title="Should You Stay an Individual Contributor or Become a "
            "Manager?",
      thumb="TWO JOBS. NOT TWO LEVELS.",
      problem="I was congratulated before anyone described the job.",
      artifact="The management job description, read on camera against "
               "what the person is being congratulated for.",
      audit="What travels? What must you relearn?",
      employer="What the organization is actually asking for, and what "
               "it will evaluate a year from now.",
      boundary="No recommendation. The right answer depends on a life "
               "and an organization that cannot be seen from here.",
      tension="A reward that is really a different job.",
      offer="Career Move Review.",
      rel="Follows V19’s gaps: this is one place the question "
          "changes permanently.",
      level="LIGHT STRENGTHEN, plus the artifact."),
]

RESERVE = [
 ("V19 consultant", "Should You Become a Consultant? The Part Everyone "
                    "Leaves Out",
  "Strongest Career Move Review alignment. Ready when the offer path "
  "needs it."),
 ("V20 career break", "How to Return After a Career Break Without "
                      "Starting at Zero",
  "Lived experience earned. Hold for a deliberate slot, not a gap "
  "filler."),
 ("V12 cannot leave yet", "What to Do When You Can’t Quit Your Job "
                          "Yet",
  "Hold until the portability read is added. Carries no offer."),
 ("V13 thirty days", "A 30-Day Plan to Test Your Next Career Move",
  "Hold pending the rebuild or the merge."),
 ("V29 ladders", "Career Ladders Don’t Work Like They Used To",
  "Hold until it can read something real."),
 ("V38 junior work", "What Happens When AI Removes the Junior Work?",
  "Employer-facing. Consider writing rather than an episode."),
]


def build(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Post-V11 reconciliation and roadmap audit",
                "Phase 1. Audit and architecture only. Nothing rewritten.")
    kv(d, "Prepared", st)
    kv(d, "Read", "Current V4 to V11 masters and maps, the ten V12 to "
                  "V21 story-led packages, the seventeen V22 to V38 "
                  "extension scripts and their editorial map, and the "
                  "unnumbered Video A and Video B masters with their "
                  "source capture packet.")
    kv(d, "Governing instruction", "September 20, 2026")
    kv(d, "Untouched", "Current V4 to V11. Nothing was opened, "
                       "renumbered, rewritten or moved.")

    h(d, "1. Executive diagnosis")
    para(d, "The channel changed what it is doing, and the library has "
            "not caught up. The older V4 to V11 were told from "
            "Temidayo’s own path: I was first in three new roles, "
            "I’ve worked across eight industries, it took me years "
            "to stop mistaking more work for growth. The current V4 to "
            "V11 are told from a situation the viewer is inside: a "
            "posting, a login that stops working, the first ninety days, "
            "a job that is not the job that was accepted. Temidayo "
            "became the reader rather than the subject.", size=10.5)
    para(d, "The V22 to V38 extension was built on the old ladder. Its "
            "own notes describe sequels to V7, V10, V11, V16 and V17 "
            "using the old numbering, and six of its concepts have since "
            "been made as current V4 to V11. So the extension is not a "
            "queue. It is an inventory with duplicates in it, and the "
            "duplicates are the easy part.", size=10.5, before=6)
    callout(d, "The harder finding is that the next slate is already "
               "largely committed. Watch Next intent is locked, and five "
               "of the eight current videos end by naming a destination "
               "that does not exist yet. Those promises decide the "
               "running order more than any preference would.")
    table(d, ["Ends by promising", "Which is", "Status"],
          [["V4 → How to Prove Your Value When AI Does More of the "
            "Task", "V17 in the library", "Written. Not made."],
           ["V6 → Turn One Accomplishment Into Proof in 10 Minutes",
            "V23 in the extension", "Written. Not made."],
           ["V7 → What to Do When Your Work Is Valued but You Are "
            "Overlooked", "V16 in the library", "Written. Not made."],
           ["V8 → Before a Layoff, Know What You Can Still Prove",
            "An older-numbered script", "Written in the superseded "
                                        "voice. See risks."],
           ["V9 → Which Parts of Your Experience Actually Transfer "
            "to Another Industry?", "V14 in the library",
            "Written. Not made."],
           ["V10 → V11, and V11 → V5", "Internal", "Made."]],
          widths=[3.0, 1.9, 1.8], size=8)
    para(d, "Two of those promises point at scripts written in the voice "
            "the channel has moved away from. That is the one place "
            "where a locked decision and the current positioning "
            "genuinely disagree, and it needs Temidayo rather than an "
            "audit.", size=10.5, before=6)

    h(d, "2. What changed strategically")
    table(d, ["Older roadmap", "Current V4 to V11"],
          [["Temidayo’s path as the spine. Titles begin with I.",
            "A situation the viewer is already inside. Temidayo reads "
            "it."],
           ["Transferable skills as the organizing idea.",
            "The permanent audit: what travels, what does not, what can "
            "you prove, what must you relearn."],
           ["Advice about what to do.",
            "A demonstrated way of reading, which the viewer can then "
            "apply."],
           ["Evidence used to support a point.",
            "Evidence put on screen early and read, with its "
            "denominator and its limits."],
           ["The professional’s own view of their experience.",
            "What an employer can reasonably recognize, infer, question "
            "or still require evidence for."],
           ["Sequels defined by topic adjacency.",
            "Sequels defined by what the last video promised."]],
          widths=[3.35, 3.35], size=8.5)
    para(d, "One consequence matters for this audit. Translation is not "
            "yet qualification is a boundary the older material does not "
            "always hold. Several extension scripts move from this "
            "travels to therefore you qualify without saying what the "
            "employer would still require. That is the single most "
            "common correction across the library, and it is usually one "
            "passage rather than a rebuild.", size=10.5, before=6)

    page_break(d)
    h(d, "3. V12 to V21 audit")
    table(d, ["", "Title", "Decision", "Why"],
          [[a, b[:46], c, e] for a, b, c, e in LIB],
          widths=[0.4, 1.7, 1.4, 3.2], size=7)

    page_break(d)
    h(d, "4. Old V22 to V38 reconciliation")
    table(d, ["", "Title", "Decision", "Why"],
          [[a, b[:44], c, e] for a, b, c, e in EXT],
          widths=[0.4, 1.6, 1.5, 3.2], size=7)

    h(d, "5. Duplicate and superseded map")
    table(d, ["Old concept", "Already exists as", "Evidence"],
          [["V22 Decode a Job Description in 10 Minutes", "Current V6",
            "Identical title and thumbnail."],
           ["V24 I’ve Seen Who Gets the Bigger Role and Why",
            "Current V7", "Identical title and thumbnail."],
           ["V26 AI Took the Task. Who Gets the Experience?",
            "Current V4", "Identical title and thumbnail."],
           ["V27 Transferable Skills Advice Is Missing Something",
            "Current V9", "Identical title and thumbnail."],
           ["V28 What Disappears When Your Work Access Ends",
            "Current V8", "Identical title and thumbnail."],
           ["V33 If Your Company Needs You but Won’t Grow You",
            "Current V5", "Identical title and thumbnail."],
           ["V36 If More Work Keeps Coming, Are You Growing?",
            "Current V5, and V25", "Written as a broader entry point to "
                                   "a video that now exists."],
           ["V30 Your AI Productivity Gain May Have a Career Cost",
            "Current V4, and V17", "Opens on the same move: the task "
                                   "that used to take hours."],
           ["V34 If AI Takes This Part of Your Job, Watch Closely",
            "Current V4", "Judgment-bearing work is the part to protect "
                          "is V4’s argument."],
           ["V32 Change Industries Without Direct Experience",
            "V14, and V21", "Sits between them and repeats both."],
           ["V37 Stop Asking Whether Your Skills Transfer",
            "Current V9", "And it runs on the superseded four "
                          "questions."]],
          widths=[2.5, 1.6, 2.6], size=7.5)
    caption(d, "Six were named in the instruction. Five more surfaced on "
               "reading. Nothing was retired for looking similar: each "
               "row is a title match or a shared opening argument.")

    page_break(d)
    h(d, "6. Recommended post-V11 sequence")
    para(d, "Obligations first, because they are locked, then the lane "
            "the channel most needs to own. Numbers are proposed, not "
            "applied. No file was renamed.", size=10.5)
    table(d, ["Slot", "Source", "Title", "Revision"],
          [[x["num"], x["src"][:22], x["title"][:44], x["level"][:26]]
           for x in SEQ], widths=[0.5, 1.4, 3.0, 1.8], size=7.5)
    para(d, "One tension worth naming. The first five slots are all "
            "promises, which is correct for trust and slow for "
            "positioning: the episode that most defines the "
            "employer-side lane sits at slot seven. A defensible "
            "variant moves it to slot three, after the two promises with "
            "the strongest commerce alignment, at the cost of delaying "
            "two others by one slot each.", size=10.5, before=6)

    for x in SEQ:
        page_break(d)
        h(d, "%s  |  %s" % (x["num"], x["title"]))
        kv(d, "Source", x["src"])
        kv(d, "Thumbnail", x["thumb"])
        kv(d, "Revision level", x["level"])
        table(d, ["", ""],
              [["Core viewer problem", x["problem"]],
               ["Artifact or situation read", x["artifact"]],
               ["Permanent-audit question", x["audit"]],
               ["Employer-side interpretation", x["employer"]],
               ["Boundary", x["boundary"]],
               ["Human tension", x["tension"]],
               ["Natural next offer", x["offer"]],
               ["Relationship to V4 to V11", x["rel"]]],
              widths=[1.8, 4.9], size=8.5)

    page_break(d)
    h(d, "7. The Watch-Me-Read episodes")
    para(d, "Where a real artifact materially improves the teaching, and "
            "where it does not. This is a content behaviour, not a "
            "framework, and it is not named on screen.", size=10.5)
    table(d, ["Video", "What goes on screen", "Why it earns it"],
          [["V13, transfer",
            "Three real postings saying manage risk.",
            "The whole point is that the same word sits on a different "
            "decision. It cannot be asserted; it has to be seen."],
           ["V18, the experience gap",
            "Two postings using the same language, side by side.",
            "This is the lane. Without the artifact it is an opinion "
            "about hiring managers."],
           ["V12, one accomplishment",
            "The sentence as the professional currently writes it.",
            "The rewrite only teaches if the first version is visible."],
           ["V21, IC or manager",
            "The management job description.",
            "Congratulated before the job is described is the hook. The "
            "description answers it."],
           ["V20, authority",
            "The role as written against the decisions actually owned.",
            "Authority is invisible until the two are put together."],
           ["V14, AI and proof",
            "Before and after of one deliverable.",
            "What the tool did and what the person did are only "
            "separable side by side."],
           ["V15, V17, V19",
            "Optional, and probably not.",
            "These turn on recognition and on a question changing. An "
            "artifact would decorate rather than teach."]],
          widths=[1.2, 2.2, 3.3], size=7.5)

    h(d, "8. Mostly conversational cleanup")
    bullets(d, [
      "V14, V15, V16, V17, V18, V19, V20 and V21 in the library. The "
      "thinking is sound and the structure holds. What they need is the "
      "current voice: shorter sentences where the written one shows, "
      "contractions, and no em dashes.",
      "V23 and V25 in the extension. Both are already close.",
    ], size=10)

    h(d, "9. Substantive rebuilding")
    bullets(d, [
      "V31, the experience gap. It asserts how employers read "
      "experience. It has to demonstrate it, on two real postings.",
      "V13, the thirty-day plan. Rebuild around what thirty days can "
      "and cannot prove to someone else, or merge it into V12.",
      "Whichever script carries the layoff promise. The title is fixed "
      "by V8; the script behind it is not current.",
    ], size=10)

    h(d, "10. Merge, hold and retire")
    table(d, ["Action", "Items"],
          [["Merge", "V30 into the AI proof episode. V32 into V13 and "
                     "V17. V34 into current V4’s territory. V13 "
                     "possibly into V12."],
           ["Hold", "V12, V13, V19, V20, V29, V38. Each for a stated "
                    "reason, none of them quality."],
           ["Retire", "V22, V24, V26, V27, V28, V33 as already made. "
                      "V36 as duplicated. V37 as framework-obsolete."]],
          widths=[1.2, 5.5], size=8.5)

    h(d, "11. CTA and offer alignment")
    table(d, ["Offer", "Where it belongs", "Where it would be forced"],
          [["Career Evidence Starter",
            "V12 proof, V14 AI proof, V15 overlooked.",
            "Anywhere the viewer has not yet seen that their evidence is "
            "thin."],
           ["Keep the Proof, $49",
            "V16 layoff. The problem is a missing record, which is "
            "exactly what it rebuilds.",
            "On videos where a record already exists."],
           ["Field Kit, $150",
            "V13 transfer, V17 relearn, V18 the experience gap.",
            "On videos with no specific destination in view."],
           ["Career Move Review, $500",
            "V21 IC or manager, and the consultant episode when it "
            "lands.",
            "On any video where the move is not yet consequential."],
           ["No offer",
            "V19 gaps, V20 authority, and the cannot-leave-yet episode.",
            "The last one especially. Selling into a constraint someone "
            "has just admitted they cannot escape would be the wrong "
            "instinct."]],
          widths=[1.5, 2.7, 2.5], size=8)

    page_break(d)
    h(d, "12. Risks and decisions that need Temidayo")
    table(d, ["", "Decision"],
          [["The layoff promise",
            "Current V8 ends by naming Before a Layoff, Know What You "
            "Can Still Prove. That script predates the current voice. "
            "V35 covers the same ground better but under a different "
            "title. Remake under the promised title, or change the "
            "destination and reopen a locked decision. I would remake "
            "under the promised title."],
           ["The other older promise",
            "Current V5 promises It Took Me Years to Stop Mistaking More "
            "Work for Career Growth, which is a biography-led title. The "
            "current OS says no opening biography. Same choice as "
            "above."],
           ["V14’s research provenance",
            "The script states 28 senior delivery postings across three "
            "industries. V6 has a capture packet with employer, "
            "requisition, access date and live status for every posting "
            "it uses. If no equivalent packet exists for the 28, the "
            "claims need one before production. This is the single "
            "biggest evidence question in the audit."],
           ["V14’s four-part structure",
            "It runs on what travels, what only looks similar, what must "
            "be learned, what must be experienced. That is close enough "
            "to the canonical audit to compete with it. Recommend "
            "keeping it as the analysis inside the episode and letting "
            "the permanent audit be the only named frame."],
           ["V37’s retirement",
            "Confirm. It is the only script still running the "
            "superseded four questions."],
           ["V31 and hiring claims",
            "The rebuilt episode must not state a universal rule about "
            "hiring managers. Employer variation has to stay visible."],
           ["V38’s audience",
            "It addresses employers about their pipeline. That is a "
            "different reader from the public front door. Confirm "
            "whether it becomes writing instead."],
           ["Sequence order",
            "Promises first, or the employer-side lane sooner. Both are "
            "defensible. This is a positioning call, not an audit "
            "finding."]],
          widths=[1.7, 5.0], size=8)

    h(d, "Reserve, with reasons")
    table(d, ["", "Title", "Why held"],
          [[a, b[:44], c] for a, b, c in RESERVE],
          widths=[1.5, 2.4, 2.8], size=7.5)

    h(d, "What this audit did not do")
    bullets(d, [
      "No script was rewritten, no package created, no file renumbered "
      "or deleted, and nothing in current V4 to V11 was touched.",
      "Historical archives were not modified. The V22 to V38 extension, "
      "the story-led packages and the source capture packet were read "
      "only.",
      "Runtimes, performance and audience response are not assessed. "
      "Word counts quoted in the old overview were not re-verified.",
    ], size=10)
    footer_note(d, "Phase 1 complete. Stopping before any rewriting, as "
                   "instructed.")
    d.save(path)
    return path


if __name__ == "__main__":
    import datetime
    st = "Sunday, September 20, 2026 | CT"
    print(build(os.path.join(OUT,
                             "V4-V38_Post_V11_Reconciliation_and_Roadmap_"
                             "Audit.docx"), st))
