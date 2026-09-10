# -*- coding: utf-8 -*-
"""Hero visual specifications for Videos 14 to 21.

Every asset is a support and reference card for the Riverside editor. This is
not a deck that covers the script paragraph by paragraph.

Each entry carries the fields the build brief requires:

  key       semantic filename stem
  draw      how it is rendered
  trigger   the EXACT spoken sentence that cues it. Verified at build time to
            exist inside a single thought block of the locked master, so a cue
            can never be built from words that span two takes.
  purpose   what the frame is for
  mode      FULL SCREEN or SHORT CALLOUT OVER CAMERA
  reveal    the reveal sequence
  emphasis  what carries the emphasis
  hold      reading and hold guidance
  captions  caption treatment
  sound     OPTIONAL sound candidate. Candidates are not cumulative: the whole
            video keeps a budget of about 4 to 7 restrained accents including
            the Subscribe cue, so the editor picks only the strongest.
  after     what happens when the frame ends
  status    REUSE / REORDER / COPY UPDATE / REBUILD / REMOVE / NEW, judged
            against the superseded development package
  why       why that classification
"""
import lay1421 as X

# The development package that these are audited against contained written
# visual maps and concepts only. No rendered production asset existed for any
# video in this range, so nothing here can honestly be called byte-identical
# reuse. NEW means the concept did not exist there at all. REUSE means the
# concept did exist and survives the final master unchanged, though the render
# itself is built here for the first time.
CONCEPT_ONLY = ("The superseded package held written concepts, never rendered "
                "assets, so no frame here is byte-identical reuse.")


def F(**kw):
    kw.setdefault("mode", "FULL SCREEN")
    kw.setdefault("captions", "No burned-in captions. Suppress any designed "
                              "caption for the whole hold.")
    kw.setdefault("after", "Return to camera on the next spoken line.")
    kw.setdefault("sound", None)
    return kw


SETS = {}

# ------------------------------------------------------------------- V14
SETS[14] = [
 F(key="v14_01_same_words_different_work",
   draw=lambda c: X.shared_then_split(
     c, "The same sentence, three industries",
     ["HEALTHCARE", "FINANCIAL SERVICES", "TECHNOLOGY"],
     "MANAGE RISK",
     ["A project slips.",
      "Financial-crimes and regulatory-compliance programs.",
      "Patient movement during an infectious-disease surge."],
     dark=True),
   trigger="All three appeared to ask for the same thing:",
   purpose="The whole argument in one frame. The words are shared. The "
           "consequence underneath them is not.",
   reveal="Three industry headings together. Hold. MANAGE RISK appears "
          "beneath all three. Hold long. Then the three consequence lines "
          "appear one at a time, left to right.",
   emphasis="MANAGE RISK is the largest element and stays on screen while "
            "the three consequences arrive under it.",
   hold="Hold the shared line for at least 2 seconds alone. Give each "
        "consequence line about 2 seconds. This frame can run long.",
   sound="Strongest candidate in the video. One soft tick as MANAGE RISK "
         "lands, and optionally one as the third consequence appears.",
   after="Stay on the frame through the consequence list, then return to "
         "camera.",
   status="NEW",
   why="The superseded draft had no research and therefore no same-word "
       "comparison. The final master's opening argument requires it."),

 F(key="v14_02_research_base",
   draw=lambda c: X.statfacts(
     c, "The research base  ·  senior program and project delivery roles",
     "28", "RETAINED POSTINGS",
     [("Healthcare", "10"), ("Financial services", "10"),
      ("Technology", "8")],
     "All collected September 10, 2026.",
     dark=True),
   trigger="So I went through 28 senior project and program delivery job "
           "descriptions across those three industries to answer a question "
           "experienced professionals often get wrong in both directions:",
   purpose="State the sample plainly and let the viewer read it. Deliberately "
           "not a research table.",
   reveal="28 first, alone. Then the unit line. Then the three rows "
          "together. Then the date line.",
   emphasis="28 is the dominant element. The three-way split is secondary and "
            "the date is last.",
   hold="Hold at least 3 seconds after the date line appears. This is the "
        "frame viewers will pause on.",
   sound="Candidate: one soft tick as 28 lands. Nothing on the breakdown "
         "rows.",
   status="NEW",
   why="The research did not exist when the earlier package was built."),

 F(key="v14_03_two_question_test",
   draw=lambda c: X.two_questions(
     c, "The test",
     "What would this person actually have to decide?",
     "What happens if they decide badly?",
     "If the answers are comparable, the underlying work is real overlap. "
     "If only the noun matches, it is apparent overlap.",
     dark=True),
   trigger="For any requirement that looked similar across industries, I "
           "asked two questions:",
   purpose="The method of the whole video, given at full size so it can be "
           "photographed.",
   reveal="First question with its rule. Hold. Second question with its "
          "rule. Hold. Then the interpretation line.",
   emphasis="Both questions at equal weight. Neither is a subtitle of the "
            "other.",
   hold="At least 2 seconds per question, then 3 seconds on the complete "
        "frame.",
   sound="Candidate: one light tap as the second question lands.",
   status="REUSE",
   why="The two-question test was the core of the earlier research design "
       "and survives into the final master unchanged. " + CONCEPT_ONLY),

 F(key="v14_04_what_travels",
   draw=lambda c: X.ladder(
     c, "What travels", None,
     [("End-to-end delivery ownership", None),
      ("Influence without direct authority", None),
      ("Risk and issue mechanics", None),
      ("Executive communication and governance", None),
      ("Delivery-method discipline", None)],
     foot="Credible candidates for portable capability when you can support "
          "them with evidence from your own work.",
     size=58),
   trigger="So what did travel across the sample?",
   purpose="Name the shared spine so the viewer can claim it specifically "
           "rather than saying transferable skills.",
   reveal="One item at a time, in the order spoken. Each stays on screen.",
   emphasis="The list builds. Nothing is highlighted over anything else.",
   hold="About 2 seconds per item as it is named. Hold the complete list 3 "
        "seconds before leaving.",
   sound="Candidate, but the video has stronger moments. If used, one tick "
         "on the first item only, never one per item.",
   status="NEW",
   why="The five capabilities come from the completed research and are named "
       "in the final master."),

 F(key="v14_05_same_word_different_decision",
   draw=lambda c: X.word_vs_work(
     c, "Same word, different decision", "GOVERNANCE",
     "In one posting", "An auditable control environment.",
     "In another", "An executive decision cadence."),
   trigger="“Governance” sounded portable until one posting meant "
           "an auditable control environment and another meant an executive "
           "decision cadence.",
   purpose="One example at a time, as the master instructs. Governance is "
           "the clearest single-frame version.",
   reveal="The word alone. Hold. Then the left reading. Then the right "
          "reading.",
   emphasis="The word is largest and stays. The two readings are equal.",
   hold="2 seconds on the word, then about 2 seconds per side.",
   sound="Candidate: one tick as the second reading replaces the emphasis.",
   status="NEW",
   why="Grounded in the research and named in the final master."),

 F(key="v14_06_four_bucket_audit",
   draw=lambda c: X.four_bucket(
     c, "The audit", None,
     [("TRAVELS", "Underlying capability you can already prove."),
      ("LOOKS SIMILAR", "Familiar language, materially different decision."),
      ("MUST BE LEARNED",
       "Knowledge you can acquire through study or structured preparation."),
      ("MUST BE EXPERIENCED",
       "Context requiring exposure, access, authority, or practice.")]),
   trigger="Then sort the answer into four buckets.",
   purpose="The framework the viewer takes away. The most photographed frame "
           "in the video.",
   reveal="One bucket at a time, in the spoken order, each with its line.",
   emphasis="The four labels are equal. No bucket is styled as the good one.",
   hold="About 2 to 3 seconds per bucket, then 4 seconds on the complete "
        "grid.",
   sound="Candidate: one tick on the first bucket. Do not tick all four.",
   status="NEW",
   why="The four-bucket audit is the final master's framework and did not "
       "exist in the superseded draft."),

 F(key="v14_07_employers_disagree",
   draw=lambda c: X.duo(
     c, "Employers disagree", None,
     ("One healthcare posting",
      "Wants someone comfortable entering new projects with limited content "
      "knowledge."),
     ("One wealth-management posting",
      "Makes years of financial-services experience a hard requirement and "
      "project-management background only preferred."),
     foot="Transferability is partly something an employer decides how much "
          "to trust."),
   trigger="One of the most useful findings was that employers themselves "
           "disagreed.",
   purpose="Stop the viewer generalizing in either direction.",
   reveal="Left side. Hold. Right side. Hold. Then the foot line.",
   emphasis="Neither side is styled as correct.",
   hold="About 3 seconds per side. The right side needs the longer read.",
   sound="Not a candidate. Let this one land in silence.",
   status="NEW",
   why="A research finding. Employers are described by type on screen; the "
       "named sources stay in the production archive."),

 F(key="v14_08_research_boundary",
   draw=lambda c: X.two_questions(
     c, "What this does not prove",
     "Job descriptions show what was written.",
     "They do not prove who gets hired.",
     "28 postings are a convenience sample. They do not represent the U.S. "
     "labor market.",
     dark=True),
   trigger="This research does not prove that two roles are interchangeable.",
   purpose="The limitation, at full size, in the video rather than only in "
           "the notes.",
   reveal="Headline, then the support line.",
   emphasis="The headline. The support carries the sample limitation and "
            "must be readable, not a footnote.",
   hold="At least 4 seconds. This frame is the honesty of the whole video "
        "and should not be rushed.",
   sound="Not a candidate. Silence is the correct treatment here.",
   status="NEW",
   why="The final master speaks the boundary and the research requires it "
       "to be visible."),

 F(key="v14_09_cta",
   draw=lambda c: X.cta_action(
     c, "One usable test", "Start with one requirement.",
     "Not the title. One requirement in the role you want.",
     "What would I have to decide? What happens if I decide badly?"),
   trigger="If you do one thing after this video, do not start with the "
           "title.",
   purpose="The single spoken action. This master names no resource, so none "
           "is shown.",
   reveal="Headline, support, then the question line.",
   emphasis="The question line in gold.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound as the card enters.",
   after="Stay on the card through the close, then move to Watch Next.",
   status="COPY UPDATE",
   why="A CTA card existed as a concept in the superseded package with a "
       "different action. The final master's action replaces it, and no "
       "resource is added because the master names none."),

 F(key="v14_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "The Career Gaps You Don’t See Until the Work Gets Harder",
     "Video 15"),
   trigger="Watch “The Career Gaps You Don’t See Until the Work "
           "Gets Harder” next.",
   purpose="The final visual.",
   reveal="Label, rule, title, then the video number.",
   emphasis="The title.",
   hold="Hold to the end of the video. Copy stays left so a YouTube end "
        "screen can sit on the right.",
   sound="Candidate: one restrained transition sound on entry, then let the "
         "music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="A Watch Next card was planned. The destination is confirmed by the "
       "final master and the title string is taken from it."),
]

# ------------------------------------------------------------------- V15
SETS[15] = [
 F(key="v15_01_the_question_changes",
   draw=lambda c: X.struck(
     c, "The question changes", None,
     "What happened here?",
     "What do you recommend we do?"),
   trigger="Then someone turns to you and asks, \"What do you recommend we "
           "do?\"",
   purpose="The moment the whole video sits on. The first question is "
           "answerable. The second is a different job.",
   reveal="First question. Hold. Struck through. Second question appears "
          "beneath it.",
   emphasis="The second question, at full weight, after the strike lands.",
   hold="2 seconds on the first, then at least 3 on the second.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="REBUILD",
   why="The concept existed in the superseded draft as a quote swap. The "
       "final master's wording differs, so the frame is built to the "
       "master's exact sentence."),

 F(key="v15_02_three_gaps",
   draw=lambda c: X.trio(
     c, "Three gaps, three responses", None,
     [("LEARN", "Something you genuinely do not know yet."),
      ("PRACTICE", "You know how the decision should be made, but you have "
                   "never been allowed to own it."),
      ("PROVE", "You already know how, but nobody can see enough proof.")],
     foot="Different problems. Different next moves."),
   trigger="Learn. Practice. Prove. Those are different problems, and they "
           "need different next moves.",
   purpose="The framework, named early as the master's early payoff.",
   reveal="One column at a time in spoken order. All three stay.",
   emphasis="Equal weight. None is the good outcome.",
   hold="About 2 seconds per column, then 3 on the complete set.",
   sound="Candidate: one tick on the third column as the set completes.",
   status="COPY UPDATE",
   why="The three-gap concept survives from the superseded draft; the "
       "labels and lines are replaced with the final master's wording."),

 F(key="v15_03_learn_test",
   draw=lambda c: X.statement(
     c, "Test one", "If someone competent walked you through the method, "
     "would that meaningfully close the gap?",
     "If yes, this may be a learning gap.", size=68, support_size=42),
   trigger="Start with the simplest test: if someone competent walked you "
           "through the method, would that meaningfully close the gap?",
   purpose="Give the viewer the first test as a sentence they can apply.",
   reveal="Question, then the reading line.",
   emphasis="The question.",
   hold="At least 3 seconds. It is meant to be answered on screen.",
   status="NEW",
   why="The final master states each test as a distinct question. The "
       "superseded draft folded them into prose."),

 F(key="v15_04_course_limit",
   draw=lambda c: X.duo(
     c, "What a course can and cannot do", None,
     ("A course can", "Teach a method."),
     ("A course cannot",
      "Give you the history of having made a consequential decision with "
      "incomplete information and lived with what happened next."),
     foot="More learning can make you better informed without making you "
          "more practiced."),
   trigger="A course can teach a method.",
   purpose="The most misread part of the topic. Stop the viewer buying "
           "training for a problem training does not solve.",
   reveal="Left side. Hold. Right side. Then the foot line.",
   emphasis="The right side is longer on purpose and carries the point.",
   hold="At least 3 seconds on the right side.",
   sound="Not a candidate.",
   status="NEW",
   why="Named explicitly in the final master and required by the brief's "
       "boundary."),

 F(key="v15_05_practice_question",
   draw=lambda c: X.statement(
     c, "Test two", "Have I ever been the person who actually had to decide?",
     "Not in the meeting. Not preparing the analysis. The person whose name "
     "was on the call.", size=68, support_size=42),
   trigger="Now ask a harder question: have I ever been the person who "
           "actually had to decide?",
   purpose="The distinction between being near a decision and carrying one.",
   reveal="Question, then the qualifying line.",
   emphasis="The question.",
   hold="At least 3 seconds.",
   status="NEW",
   why="The final master separates the three tests into distinct questions."),

 F(key="v15_06_knowing_isnt_owning",
   draw=lambda c: X.statement(
     c, None, "Knowing the work and owning the decision are not the same "
     "thing.", None, dark=True, size=88),
   trigger="You can understand a decision very well and still never have "
           "carried one.",
   purpose="The line the thumbnail is built from, at full size.",
   reveal="Single state. No build.",
   emphasis="The whole frame is the emphasis.",
   hold="At least 3 seconds in silence.",
   sound="Strong candidate: one clean transition sound as it enters.",
   status="NEW",
   why="The final master's thumbnail wording changed to KNOWING ISN'T "
       "OWNING, so the video needs the spoken line on screen."),

 F(key="v15_07_three_reads",
   draw=lambda c: X.trio(
     c, "Same discomfort, three diagnoses", None,
     [("LEARN", "She was never taught to structure a decision under "
                "uncertainty."),
      ("PRACTICE", "She understands the tradeoff but has never owned the "
                   "call."),
      ("PROVE", "She has made comparable calls quietly, and the room does "
                "not know.")],
     foot="ILLUSTRATION. A constructed example, not a real case."),
   trigger="Same discomfort. Three completely different next moves.",
   purpose="Show the three gaps producing three readings of one moment.",
   reveal="One reading at a time, matching the spoken order.",
   emphasis="The three labels tie back to the framework frame.",
   hold="About 2 seconds per reading, 3 on the complete set.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="The superseded draft had a similar example. The final master's "
       "version is shorter and is what the frame now carries."),

 F(key="v15_08_one_gap_one_step",
   draw=lambda c: X.readings(
     c, "One gap, one step", None,
     [("Do I need to learn this?", "Learn"),
      ("Have I ever genuinely practiced this?", "Practice"),
      ("Can I prove that I already have?", "Prove")]),
   trigger="Ask three questions.",
   purpose="The take-away pairing. Each question matched to its own step.",
   reveal="One pair at a time.",
   emphasis="The pairing, not the list.",
   hold="About 2 seconds per pair, 3 on the complete frame.",
   sound="Candidate: one tick as the third pair completes.",
   status="COPY UPDATE",
   why="The pairing concept survives; the questions are the master's."),

 F(key="v15_09_cta",
   draw=lambda c: X.cta(
     c, "One gap, one step", "Name the gap you are actually looking at.",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="If you want a structured way to decide what the next move "
           "actually requires, the Career Decision Evidence Check is linked "
           "below.",
   purpose="The single resource route named by the master.",
   reveal="Label, headline, resource name, then the URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="The route matches the master. " + CONCEPT_ONLY),

 F(key="v15_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "What to Do When Your Work Is Valued but You Are Overlooked",
     "Video 16"),
   trigger="Knowing the work and owning the decision are not the same thing.",
   purpose="The final visual, entering on the last spoken line.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="Destination taken from the final master."),
]

# ------------------------------------------------------------------- V16
SETS[16] = [
 F(key="v16_01_called_then_skipped",
   draw=lambda c: X.duo(
     c, "Relied on, then skipped", None,
     ("They call you", "When it is urgent. When it breaks. When someone new "
                       "needs to understand how the work really works."),
     ("They skip you", "When the interesting assignment is handed out. When "
                       "the promotion list comes around. When the bigger "
                       "scope is discussed."),
     foot="That is not the same problem as being invisible.",
     dark=True),
   trigger="When something is urgent, they call you.",
   purpose="Land the specific frustration in the first fifteen seconds.",
   reveal="Left column builds line by line as the three calls are spoken. "
          "Then the right column. Then the foot line.",
   emphasis="The imbalance between the two columns is the point.",
   hold="Build with the speech, then hold the complete frame 3 seconds.",
   sound="Candidate: one soft tick as the right column appears.",
   status="REBUILD",
   why="The superseded draft had a split-screen concept with different "
       "copy. The final master's three-call opening replaces it."),

 F(key="v16_02_four_separations",
   draw=lambda c: X.ladder(
     c, "Before you change how you behave", None,
     [("Is the work seen?", None),
      ("Is it attributed to you?", None),
      ("Trusted to deliver, or considered for scope?", None),
      ("Is the obstacle one you can remove?", None)],
     size=54),
   trigger="Before you change how you behave, separate four things: is the "
           "work seen, is it attributed to you, are you trusted for delivery "
           "or considered for larger scope, and is the obstacle one you can "
           "actually remove?",
   purpose="The structure of the video, given at full size.",
   reveal="One question at a time, in spoken order.",
   emphasis="All four equal.",
   hold="About 2 seconds each, 3 on the complete set.",
   sound="Candidate: one tick on the fourth as the set completes.",
   status="COPY UPDATE",
   why="The four separations existed in the superseded draft as a concept. "
       "The wording is now the master's."),

 F(key="v16_03_where_work_disappears",
   draw=lambda c: X.trio(
     c, "Where good work disappears", None,
     [("INTO A PROCESS", "That now runs smoothly."),
      ("INTO A TEAM RESULT", "Where everyone delivered it."),
      ("INTO PREVENTION", "Where the evidence is that the problem did not "
                          "happen.")],
     foot="The better the system works, the easier it is for the work that "
          "made it work to become invisible."),
   trigger="It disappears into a process that now runs smoothly.",
   purpose="Explain why the information problem exists without blaming "
           "anyone.",
   reveal="One column at a time. Prevention appears last and is the one "
          "worth holding.",
   emphasis="Prevention. The absence is the hardest to point at.",
   hold="2 seconds per column, then 3 on the foot line.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="The concept survives; the copy is the master's."),

 F(key="v16_04_delivery_vs_scope",
   draw=lambda c: X.duo(
     c, "Two different judgments", None,
     ("Trusted to deliver", "You are the reason a difficult area runs "
                            "smoothly."),
     ("Considered for scope", "A separate judgment, made by the same people, "
                              "about the same person."),
     foot="That can make indispensability feel like recognition while "
          "functioning like a ceiling."),
   trigger="Delivery and scope are different judgments.",
   purpose="The most surprising point in the video.",
   reveal="Left, then right, then the foot line.",
   emphasis="The foot line, which is the insight.",
   hold="At least 3 seconds on the foot line.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="Concept retained, copy replaced with the master's wording."),

 F(key="v16_05_the_hinge",
   draw=lambda c: X.duo(
     c, "The hinge", None,
     ("Does not know", "An information problem. Frustrating, but it may be "
                       "fixable."),
     ("Knows and does not act",
      "Not an information problem. More explanation is probably not the "
      "missing ingredient."),
     foot="You cannot know which situation you are in until the information "
          "problem is gone.",
     dark=True),
   trigger="This is the distinction I most want you to keep: a manager who "
           "does not know is a completely different situation from a manager "
           "who knows and does not act.",
   purpose="The pivot of the video and the most quotable frame.",
   reveal="Left. Hold. Right. Hold. Then the foot line.",
   emphasis="The two sides are different problems, not degrees of one.",
   hold="At least 3 seconds per side and 3 on the foot line.",
   sound="Strong candidate: one soft tick as the right side lands.",
   status="REUSE",
   why="The hinge distinction was the strongest idea in the superseded "
       "draft and the final master keeps it. " + CONCEPT_ONLY),

 F(key="v16_06_what_remains",
   draw=lambda c: X.quad(
     c, "What a clearer record does not fix", None,
     [("BIAS", "It does not override it."),
      ("A ROLE THAT DOES NOT EXIST", "It does not create one."),
      ("A BUDGET YOU DO NOT CONTROL", "It does not move it."),
      ("A MANAGER WHO HAS DECIDED", "It does not change them.")],
     foot="What it does is remove the obstacle you can remove, so that "
          "whatever remains becomes easier to see."),
   trigger="A clearer record does not override bias.",
   purpose="Keep the video honest. The record has a limit and the limit is "
           "said out loud.",
   reveal="All four appear together, then the foot line.",
   emphasis="The foot line.",
   hold="At least 4 seconds. Do not rush the honesty frame.",
   sound="Not a candidate. Let this land in silence.",
   status="NEW",
   why="The final master states the limits as a list. The superseded draft "
       "carried them as prose."),

 F(key="v16_07_three_pieces_four_lines",
   draw=lambda c: X.ladder(
     c, "Three pieces of work. Four lines each.", None,
     [("What was true before", None),
      ("What you decided", None),
      ("What changed", None),
      ("What evidence supports the account", None)],
     foot="Do not rely on everyone knows I am strong. Make the work "
          "inspectable.",
     size=56),
   trigger="For each, write four lines: what was true before, what you "
           "decided, what changed, and what evidence supports the account.",
   purpose="The artifact the viewer builds.",
   reveal="One line at a time in spoken order.",
   emphasis="The fourth line, which is what makes it inspectable.",
   hold="2 seconds per line, 4 on the complete frame. Viewers will pause "
        "here.",
   sound="Candidate: one tick as the fourth line lands.",
   status="COPY UPDATE",
   why="The four-line record survives from the superseded draft with the "
       "master's revised fourth line."),

 F(key="v16_08_needed_not_considered",
   draw=lambda c: X.statement(
     c, None, "Being needed is not the same as being considered for what "
     "comes next.", None, dark=True, size=84),
   trigger="Being needed is not the same as being considered for what comes "
           "next.",
   purpose="The final spoken line at full size.",
   reveal="Single state.",
   emphasis="The whole frame.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   after="Move to the CTA card, then Watch Next.",
   status="NEW",
   why="The final master's closing line differs from the superseded draft."),

 F(key="v16_09_cta",
   draw=lambda c: X.cta(
     c, "Start smaller", "Write one decision you made and what it changed.",
     "Keep the Proof", "temidayoafonja.com/keep-the-proof"),
   trigger="Keep the Proof is linked below if you want the deeper evidence "
           "system.",
   purpose="The single resource route named by the master, after the value "
           "has been delivered.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Route matches the master. " + CONCEPT_ONLY),

 F(key="v16_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Show Your Impact at Work When You Built It From Scratch",
     "Video 8"),
   trigger="Being needed is not the same as being considered for what comes "
           "next.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REBUILD",
   why="The superseded draft proposed V8 as a Watch Next and the final "
       "master confirms it. The card is built to the master's string."),
]

# ------------------------------------------------------------------- V17
SETS[17] = [
 F(key="v17_01_two_days_forty_minutes",
   draw=lambda c: X.duo(
     c, "The visible part got easier", None,
     ("Before", "The report used to take you two days."),
     ("Now", "A tool produces most of it in forty minutes."),
     foot="That sounds like progress. Until someone asks what you actually "
          "did.",
     dark=True),
   trigger="The report used to take you two days.",
   purpose="The hook, stated without celebration or alarm.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line turns the frame.",
   hold="2 seconds per side, 3 on the foot line.",
   sound="Candidate: one soft tick as the right side lands.",
   status="COPY UPDATE",
   why="The comparison existed in the superseded draft. The master's "
       "wording replaces the copy."),

 F(key="v17_02_what_did_you_actually_do",
   draw=lambda c: X.statement(
     c, None, "So what did you actually do?", None, dark=True, size=110),
   trigger="Until someone asks, \"So what did you actually do?\"",
   purpose="The thumbnail line as a one-beat card.",
   reveal="Single state, entering hard.",
   emphasis="The whole frame.",
   hold="About 2 seconds. This one should be short and land.",
   sound="Strong candidate: one clean transition sound on entry.",
   status="NEW",
   why="The final master's thumbnail wording changed to WHAT DID YOU "
       "ACTUALLY DO?, so the line needs its own frame."),

 F(key="v17_03_record_moved",
   draw=lambda c: X.duo(
     c, "Where the record lives", None,
     ("It used to be", "Attached to the artifact."),
     ("It now has to be", "Attached to the decisions around the artifact."),
     foot="As production gets easier, the artifact is a weaker proxy for "
          "contribution."),
   trigger="The record used to be attached to the artifact. It now has to be "
           "attached to the decisions around the artifact.",
   purpose="The reframe, in one comparison.",
   reveal="Left, then right, then the foot line.",
   emphasis="The right side.",
   hold="3 seconds on the right side.",
   sound="Candidate: one tick as the right side lands.",
   status="NEW",
   why="The final master states the move explicitly."),

 F(key="v17_04_four_lines",
   draw=lambda c: X.ladder(
     c, "The four lines", None,
     [("What were you actually asked to get right?",
       "Not just what you were asked to produce."),
      ("What did you check, and why did you check that?", None),
      ("What did you conclude that the initial output did not establish?",
       None),
      ("What were you accountable for if the result was wrong?", None)],
     size=46),
   trigger="For one AI-assisted piece of work, keep four lines.",
   purpose="The framework and the artifact. The most photographed frame.",
   reveal="One line at a time in spoken order.",
   emphasis="Line two, which the next frame enlarges.",
   hold="About 3 seconds per line, 4 on the complete frame.",
   sound="Candidate: one tick on the first line only.",
   status="REUSE",
   why="The four-line record was the superseded draft's framework and the "
       "final master keeps it with revised wording. " + CONCEPT_ONLY),

 F(key="v17_05_line_two",
   draw=lambda c: X.statement(
     c, "Line two", "What did you check, and why did you check that?",
     "The reason can come from history, pattern recognition, domain "
     "knowledge, a previous failure, or a consequence the output does not "
     "display.", dark=True, size=76, support_size=40),
   trigger="The second line is often the one people forget fastest.",
   purpose="Enlarge the single line that carries the contribution.",
   reveal="Question, then the support line.",
   emphasis="The question.",
   hold="At least 4 seconds.",
   sound="Strong candidate: one soft tick as the question lands.",
   status="REUSE",
   why="Line two was already the emphasis in the superseded draft and the "
       "master preserves it. " + CONCEPT_ONLY),

 F(key="v17_06_speed_pressure",
   draw=lambda c: X.statement(
     c, "Speed changes the pressure",
     "The checking time becomes easier to squeeze because it is harder to "
     "see.",
     "That does not mean the work should stay slow. It means the "
     "organization should be clear about what the checking is buying and who "
     "still owns the consequence.", size=66, support_size=40),
   trigger="The checking time becomes easier to squeeze because it is harder "
           "to see.",
   purpose="Name the second-order effect without turning it into a "
           "complaint.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds. The support line needs real reading time.",
   sound="Not a candidate.",
   status="REUSE",
   why="This beat was added to the superseded draft for the same reason and "
       "the master carries it. " + CONCEPT_ONLY),

 F(key="v17_07_constructed_example",
   draw=lambda c: X.readings(
     c, "ILLUSTRATION  ·  CONSTRUCTED EXAMPLE, NOT A CAPTURED MODEL TEST",
     None,
     [("Asked to get right",
       "That leadership does not leave with a misleading picture."),
      ("Checked, and why",
       "Whether an improvement is only a timing effect, and whether one "
       "customer distorts the trend."),
      ("Concluded", "The headline needs qualification."),
      ("Accountable for", "The number going into the planning "
                          "discussion.")]),
   trigger="Here is a constructed illustration, not a captured model test.",
   purpose="Show the four lines filled in. The label is spoken and on "
           "screen for the whole hold.",
   reveal="One row at a time in spoken order. The label never leaves.",
   emphasis="The second row, which is the longest and the point.",
   hold="About 3 seconds per row, 4 on the complete frame.",
   sound="Not a candidate. The label needs to be read, not decorated.",
   status="COPY UPDATE",
   why="The superseded draft had a similar constructed case. The master's "
       "version is shorter and replaces the copy. The illustration label is "
       "required and is not a footer."),

 F(key="v17_08_workflow_or_contribution",
   draw=lambda c: X.statement(
     c, None, "The workflow is not the whole contribution.", None,
     dark=True, size=88),
   trigger="The workflow is not the whole contribution.",
   purpose="The final spoken line at full size.",
   reveal="Single state.",
   emphasis="The whole frame.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   after="Move to the CTA card, then Watch Next.",
   status="NEW",
   why="The final master's closing line differs from the superseded draft."),

 F(key="v17_09_cta",
   draw=lambda c: X.cta(
     c, "Capture what you checked", "Write what you checked and why.",
     "Keep the Proof", "temidayoafonja.com/keep-the-proof"),
   trigger="Keep the Proof is linked below if you want the broader evidence "
           "system.",
   purpose="The single resource route named by the master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Route matches the master. " + CONCEPT_ONLY),

 F(key="v17_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "AI Can Do the Task. What Are You Still Paid For?", "Video 11"),
   trigger="The workflow is not the whole contribution.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="The superseded draft proposed V11 and the final master confirms "
       "it. " + CONCEPT_ONLY),
]

# ------------------------------------------------------------------- V18
SETS[18] = [
 F(key="v18_01_congratulated",
   draw=lambda c: X.statement(
     c, "How the offer arrives",
     "They congratulate you before they describe the job.",
     "Management is often offered as a reward. But it is not a reward. It is "
     "a different job.", dark=True, size=76, support_size=42),
   trigger="And before they explain what the job actually is, they "
           "congratulate you.",
   purpose="The opening observation, recognizable immediately.",
   reveal="Headline. Hold. Then the support line.",
   emphasis="The headline.",
   hold="3 seconds on the headline, 3 on the support.",
   sound="Candidate: one soft tick as the support line lands.",
   status="COPY UPDATE",
   why="The concept existed in the superseded draft. The master's wording "
       "replaces the copy."),

 F(key="v18_02_two_different_jobs",
   draw=lambda c: X.duo(
     c, "Not a higher and a lower version of one career", None,
     ("Senior individual work", "Different days. Different skills. Different "
                                "hard parts."),
     ("Management", "Different days. Different skills. Different hard "
                    "parts."),
     foot="TWO DIFFERENT JOBS. Side by side, not a ladder."),
   trigger="They are different jobs, with different days, different skills, "
           "and different hard parts.",
   purpose="The reframe. The horizontal arrangement is the argument.",
   reveal="Both columns together, then the foot line.",
   emphasis="Neither column is above the other. Do not stack them.",
   hold="At least 4 seconds.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="The final master's thumbnail is TWO DIFFERENT JOBS, so the frame "
       "carries that argument directly."),

 F(key="v18_03_five_variables",
   draw=lambda c: X.ladder(
     c, "Five things that do not move together", None,
     [("Scope", None), ("Responsibility", None), ("Compensation", None),
      ("Authority", None), ("People management", None)],
     foot="A role can increase your responsibility without increasing your "
          "authority.",
     size=56),
   trigger="Five things often get bundled together: scope, responsibility, "
           "compensation, authority, and people management.",
   purpose="Break the bundle. The teaching of the middle of the video.",
   reveal="All five appear, then each shifts independently as the foot line "
          "is spoken. Do not animate them as one bar.",
   emphasis="The independence, not the list.",
   hold="3 seconds on the list, 3 on the foot line.",
   sound="Candidate: one tick as the foot line lands.",
   status="REUSE",
   why="The five variables were the superseded draft's framework and the "
       "final master keeps them. " + CONCEPT_ONLY),

 F(key="v18_04_four_questions",
   draw=lambda c: X.ladder(
     c, "Four questions before you answer", None,
     [("What does the job consume?", None),
      ("Does the other path really exist here?", None),
      ("What authority comes with it?", None),
      ("Can you come back?", None)],
     size=58),
   trigger="But before you answer the offer, ask four questions: what does "
           "the job consume, does the other path really exist, what "
           "authority comes with it, and can you come back?",
   purpose="The frame viewers photograph. All four together, large.",
   reveal="All four together on the close, since the master speaks them as "
          "one list.",
   emphasis="Equal weight.",
   hold="At least 5 seconds. This is the take-away frame.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="The four questions survive from the superseded draft with the "
       "master's wording. " + CONCEPT_ONLY),

 F(key="v18_05_what_the_job_consumes",
   draw=lambda c: X.quad(
     c, "What actually fills the calendar", None,
     [("ONE-TO-ONES", "And hiring."),
      ("PERFORMANCE CONVERSATIONS", "And planning."),
      ("REPORTING UPWARD", "And absorbing pressure."),
      ("DECIDING", "On work you will not personally do.")],
     foot="Ask two managers what their last ordinary week actually "
          "contained."),
   trigger="One-to-ones, hiring, performance conversations, planning, "
           "reporting upward, absorbing pressure, deciding on work you will "
           "not personally do.",
   purpose="Make the job concrete rather than abstract.",
   reveal="All four together, then the foot line, which is the instruction.",
   emphasis="The foot line, because it is what the viewer does.",
   hold="4 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept retained from the superseded draft with the master's list."),

 F(key="v18_06_ask_for_names",
   draw=lambda c: X.statement(
     c, "Does the other path really exist here?", "Ask for names.",
     "Ask what those people are trusted to decide. Ask how their scope and "
     "compensation compare with management at the same level.",
     dark=True, size=96, support_size=40),
   trigger="Ask for names.",
   purpose="The single most practical instruction in the video.",
   reveal="The instruction alone. Hold. Then the support line.",
   emphasis="Ask for names, at maximum size.",
   hold="2 seconds alone, then 4 with the support.",
   sound="Strong candidate: one soft tick as the two words land.",
   status="REUSE",
   why="The instruction was in the superseded draft and survives "
       "verbatim in the master. " + CONCEPT_ONLY),

 F(key="v18_07_responsibility_vs_authority",
   draw=lambda c: X.duo(
     c, "Compare the two lists", None,
     ("What you can decide without asking",
      "Budget. Hiring. Prioritization. Saying no. Changing scope."),
     ("What you will be answerable for",
      "If this list is much longer, name that before you accept."),
     foot="Responsibility without enough authority is not a small detail of "
          "the job."),
   trigger="If the responsibility list is much longer than the authority "
           "list, name that before you accept.",
   purpose="The trap, made checkable.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot line.",
   sound="Candidate: one tick as the foot line lands.",
   status="REUSE",
   why="The comparison survives from the superseded draft with the "
       "master's wording. " + CONCEPT_ONLY),

 F(key="v18_08_neither_is_brave",
   draw=lambda c: X.statement(
     c, "Neither answer is the brave one",
     "Pick the path whose hard parts you would rather have.",
     "Inside the organization you actually work in.", size=80,
     support_size=42),
   trigger="Pick the path whose hard parts you would rather have, inside the "
           "organization you actually work in.",
   purpose="Hold the video two-sided at the point where it would be easiest "
           "to take a side.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="REUSE",
   why="The two-sidedness was the superseded draft's requirement and the "
       "master states it in one sentence. " + CONCEPT_ONLY),

 F(key="v18_09_cta",
   draw=lambda c: X.cta(
     c, "Do not choose the title", "Choose the work.",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="The Career Decision Evidence Check is linked below if you want a "
           "structured way to think through the choice.",
   purpose="The single resource route named by the master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Route matches the master. " + CONCEPT_ONLY),

 F(key="v18_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "What to Do When Your Work Is Valued but You Are Overlooked",
     "Video 16"),
   trigger="Do not choose the title. Choose the work.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="The superseded draft proposed V16 and the final master confirms "
       "it. " + CONCEPT_ONLY),
]

# ------------------------------------------------------------------- V19
SETS[19] = [
 F(key="v19_01_you_should_consult",
   draw=lambda c: X.statement(
     c, "The compliment", "“You should consult.”",
     "It usually happens right after you solve something difficult, which is "
     "why it feels flattering and why almost nobody examines it.",
     dark=True, size=104, support_size=40),
   trigger="It usually happens right after you solve something difficult, "
           "which is why it feels flattering and why almost nobody examines "
           "it.",
   purpose="The way in. The compliment on screen, then the reason nobody "
           "checks it.",
   reveal="The quote alone. Hold. Then the support line.",
   emphasis="The quote.",
   hold="2 seconds alone, then 3 with the support.",
   sound="Candidate: one soft tick as the support line lands.",
   status="COPY UPDATE",
   why="Concept retained from the superseded draft with the master's "
       "wording."),

 F(key="v19_02_experience_is_not_an_offer",
   draw=lambda c: X.duo(
     c, "Two different questions", None,
     ("Your experience tells you", "What you know."),
     ("It does not tell you", "What somebody will buy."),
     foot="Twenty years of experience can still leave you with nothing a "
          "client knows how to buy."),
   trigger="Your experience tells you what you know. It does not "
           "automatically tell you what somebody will buy.",
   purpose="The reversal, and the thumbnail line's argument.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="2 seconds per side, 4 on the foot line.",
   sound="Strong candidate: one soft tick as the right side lands.",
   status="REUSE",
   why="The separation was the superseded draft's reversal and the master "
       "keeps it. " + CONCEPT_ONLY),

 F(key="v19_03_four_things",
   draw=lambda c: X.four_bucket(
     c, "Four things people call consulting", None,
     [("EXPERTISE", "What you know and can do."),
      ("AN OFFER", "A defined thing somebody receives, with a beginning and "
                   "an end."),
      ("A BUYER", "The person or organization that has the problem and can "
                  "release money to solve it."),
      ("REPEATABILITY", "Being able to deliver again without rebuilding the "
                        "service from nothing.")]),
   trigger="Separate four things.",
   purpose="The framework. Most people have the first and are missing the "
           "other three.",
   reveal="One bucket at a time in spoken order.",
   emphasis="The gap after the first bucket.",
   hold="About 3 seconds per bucket, 4 on the complete grid.",
   sound="Candidate: one tick on the first bucket only.",
   status="COPY UPDATE",
   why="The four-part separation survives; the master renames the third "
       "and fourth, so the copy is replaced."),

 F(key="v19_04_who_signs_it",
   draw=lambda c: X.duo(
     c, "The buyer question", None,
     ("Not who suffers from it", "Almost everybody has problems."),
     ("Who actually pays somebody to solve it now",
      "And if a budget exists, who signs it."),
     foot="The person with the problem and the person who releases the money "
          "may not be the same person.",
     dark=True),
   trigger="Not who suffers from it. Who actually pays somebody to solve it "
           "now?",
   purpose="The question that decides whether anything else applies.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="3 seconds per side, 3 on the foot line.",
   sound="Candidate: one tick as the right side lands.",
   status="REUSE",
   why="The buyer question was the superseded draft's spine and the master "
       "keeps it. " + CONCEPT_ONLY),

 F(key="v19_05_expertise_vs_deliverable",
   draw=lambda c: X.struck(
     c, "Turn expertise into a deliverable", None,
     "“I advise on risk.”",
     "A bounded review, a decision workshop, a diagnostic, a written "
     "recommendation, a defined implementation sprint."),
   trigger="“I advise on risk” is expertise. It is not yet an "
           "offer.",
   purpose="The strongest single comparison in the video. Unbuyable sentence "
           "beside buyable ones.",
   reveal="The unbuyable sentence. Hold. Struck. Then the alternatives.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="COPY UPDATE",
   why="The concept existed in the superseded draft with a different "
       "example. The master's example replaces it."),

 F(key="v19_06_what_is_not_included",
   draw=lambda c: X.statement(
     c, "State what is not included",
     "Scope is part of the offer.",
     "Not a legal footnote you discover after the work expands.", size=88,
     support_size=42),
   trigger="Scope is part of the offer, not a legal footnote you discover "
           "after the work expands.",
   purpose="The line that protects a fixed fee.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 3 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept retained, copy replaced with the master's wording."),

 F(key="v19_07_one_page",
   draw=lambda c: X.ladder(
     c, "Write one page", None,
     [("The problem", None), ("The buyer", None), ("The deliverable", None),
      ("The scope", None),
      ("The conditions that would need to be true", None)],
     foot="You are not testing whether you are talented. You are testing "
          "whether the thing you described is recognized as worth buying.",
     size=54),
   trigger="Then write one page: the problem, the buyer, the deliverable, "
           "the scope, and the conditions that would need to be true before "
           "this is viable.",
   purpose="The artifact.",
   reveal="One line at a time in spoken order.",
   emphasis="The fifth line, which tells the viewer where they are.",
   hold="2 seconds per line, 4 on the complete frame.",
   sound="Candidate: one tick on the fifth line.",
   status="COPY UPDATE",
   why="The one-page proposal survives from the superseded draft with the "
       "master's field list."),

 F(key="v19_08_raw_material",
   draw=lambda c: X.statement(
     c, None, "Experience can be the raw material. It is not the offer.",
     None, dark=True, size=84),
   trigger="Experience can be the raw material. It is not the offer.",
   purpose="The final spoken line at full size.",
   reveal="Single state.",
   emphasis="The whole frame.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   after="Move to the CTA card, then Watch Next.",
   status="NEW",
   why="The final master's closing line differs from the superseded draft."),

 F(key="v19_09_cta",
   draw=lambda c: X.cta(
     c, "One sentence", "What would somebody receive from you, and by when?",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="The Career Decision Evidence Check is linked below if you want a "
           "structured way to test the decision.",
   purpose="The single resource route named by the master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Route matches the master. " + CONCEPT_ONLY),

 F(key="v19_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "A 30-Day Plan to Test Your Next Career Move", "Video 13"),
   trigger="Experience can be the raw material. It is not the offer.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="The superseded draft proposed V13 and the final master confirms "
       "it. " + CONCEPT_ONLY),
]

# ------------------------------------------------------------------- V20
SETS[20] = [
 F(key="v20_01_the_gap_is_not_the_whole_return",
   draw=lambda c: X.statement(
     c, "The return", "The explanation matters. But it is not the whole "
     "return.",
     "What from before is still current, what needs updating, and what do I "
     "genuinely need to rebuild?", dark=True, size=76, support_size=42),
   trigger="The explanation matters. But it is not the whole return.",
   purpose="The reframe, close to the opening.",
   mode="SHORT CALLOUT OVER CAMERA for the headline, then FULL SCREEN for "
        "the support line.",
   reveal="Headline as a short callout while Temidayo is on camera, then go "
          "full screen for the three-part question.",
   emphasis="The three-part question.",
   hold="2 seconds on the callout, 4 on the full-screen question.",
   sound="Candidate: one soft tick as the full-screen question lands.",
   after="Return to camera. The opening is a real personal account and "
         "should stay camera-led around this frame.",
   status="NEW",
   why="The final master opens with Temidayo's real maternity-leave return, "
       "which the superseded draft did not have and explicitly forbade "
       "inventing. The frame is built so the opening stays camera-led."),

 F(key="v20_02_three_buckets",
   draw=lambda c: X.trio(
     c, "Sort it into three buckets", None,
     [("STILL CURRENT", "Capability that survives time away."),
      ("NEEDS UPDATING", "Decay, and change in the field."),
      ("NEEDS REBUILDING", "The part that does not travel automatically.")],
     foot="Instead of treating your whole career as current or obsolete."),
   trigger="Still current. Needs updating. Needs rebuilding.",
   purpose="The framework named by the master.",
   reveal="One column at a time in spoken order.",
   emphasis="Equal weight. None is the failure column.",
   hold="2 seconds per column, 4 on the complete set.",
   sound="Candidate: one tick as the third column completes the set.",
   status="REBUILD",
   why="The superseded draft used a six-category sort. The final master "
       "uses three buckets with six things attended to inside them, so the "
       "frame is rebuilt to the master's structure."),

 F(key="v20_03_six_things",
   draw=lambda c: X.ladder(
     c, "Inside those buckets, pay attention to six things", None,
     [("What stayed current", None), ("What decayed", None),
      ("What changed in the field", None),
      ("What changed in your circumstances", None),
      ("What is unproven rather than absent", None),
      ("What genuinely has to be rebuilt", None)],
     size=46),
   trigger="Inside those buckets, pay attention to six things: what stayed "
           "current, what decayed, what changed in the field, what changed "
           "in your circumstances, what is unproven rather than absent, and "
           "what genuinely has to be rebuilt.",
   purpose="The detail under the three buckets, without replacing them.",
   reveal="All six appear together, since the master speaks them as one "
          "list. The fifth is the one the next frame enlarges.",
   emphasis="The fifth item.",
   hold="At least 5 seconds. Six items need real reading time.",
   sound="Not a candidate. The next frame is the stronger moment.",
   status="COPY UPDATE",
   why="The six categories existed in the superseded draft as the primary "
       "structure. Here they are secondary to the master's three buckets."),

 F(key="v20_04_unproven_is_not_absent",
   draw=lambda c: X.statement(
     c, None, "Unproven is not the same as absent.",
     "You may still know how to do something and simply have no recent "
     "evidence that another person can inspect.", dark=True, size=96,
     support_size=42),
   trigger="This is the distinction I want you to remember most: unproven is "
           "not the same as absent.",
   purpose="The distinction that saves the most viewers. The largest frame "
           "in the video.",
   reveal="Headline alone. Hold. Then the support line.",
   emphasis="The headline, at maximum size.",
   hold="3 seconds alone, then 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands.",
   status="REUSE",
   why="The distinction was the superseded draft's strongest frame and the "
       "master keeps it as the stated emphasis. " + CONCEPT_ONLY),

 F(key="v20_05_unproven_response",
   draw=lambda c: X.duo(
     c, "If it is unproven", None,
     ("The response is not", "To relearn it from the beginning."),
     ("The response may be",
      "To create a current instance. A bounded project, a permitted work "
      "sample, a short contract, volunteer work, refreshed training."),
     foot="If it is genuinely absent, that belongs in the third bucket."),
   trigger="If it is unproven, the response is not automatically to relearn "
           "it from the beginning.",
   purpose="Turn the distinction into an action.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="2 seconds left, 4 right, 2 on the foot line.",
   sound="Not a candidate.",
   status="NEW",
   why="The master gives a specific list of ways to create a current "
       "instance that the superseded draft did not carry."),

 F(key="v20_06_constructed_example",
   draw=lambda c: X.readings(
     c, "ILLUSTRATION  ·  CONSTRUCTED EXAMPLE, NOT A REAL CASE", None,
     [("Still current",
       "How to structure an analysis and challenge a number."),
      ("Needs updating", "The reporting system and newer automation."),
      ("Unproven", "Complex reconciliations, with no recent example."),
      ("Needs rebuilding", "One regulatory area that changed "
                           "substantially.")]),
   trigger="Imagine someone returning to a finance role after several years "
           "away.",
   purpose="Show the sort done once. The label stays for the whole hold.",
   reveal="One row at a time in spoken order. The label never leaves.",
   emphasis="The unproven row.",
   hold="About 3 seconds per row, 4 on the complete frame.",
   sound="Not a candidate. The label needs to be read.",
   status="COPY UPDATE",
   why="The superseded draft had a six-category sort for the same "
       "illustration. The master's four-row version replaces it. This is a "
       "constructed illustration and is labeled as one, which the real "
       "maternity-leave opening is not."),

 F(key="v20_07_framing_and_bias",
   draw=lambda c: X.statement(
     c, "Market reality",
     "A better explanation does not make every employer fair.",
     "What a stronger return record does is keep you from arguing for the "
     "wrong thing.", size=72, support_size=42),
   trigger="Bias against career breaks exists, and a better explanation does "
           "not make every employer fair.",
   purpose="Keep the video honest about what framing can and cannot do.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate. Let this land in silence.",
   status="REUSE",
   why="The superseded draft carried the same limit and the master states "
       "it plainly. " + CONCEPT_ONLY),

 F(key="v20_08_current_and_rebuilding",
   draw=lambda c: X.duo(
     c, "Two short lists", None,
     ("What is current now", "With evidence for each item."),
     ("What you are rebuilding now", "With a date attached."),
     foot="Started in September and will complete in November is a different "
          "signal from I plan to refresh this.",
     dark=True),
   trigger="A date matters because 'I plan to refresh this' and 'I started "
           "this in September and will complete it in November' are "
           "different signals.",
   purpose="The artifact and the single action.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The date on the right.",
   hold="3 seconds per side, 4 on the foot line.",
   sound="Candidate: one tick as the date lands.",
   status="COPY UPDATE",
   why="The two-part record survives from the superseded draft with the "
       "master's wording."),

 F(key="v20_09_cta",
   draw=lambda c: X.cta(
     c, "Today", "Choose one thing you are rebuilding and put a date on it.",
     "Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="The Field Kit is linked below if you want a broader "
           "evidence-led read of what still counts and what needs "
           "rebuilding.",
   purpose="The single resource route named by the master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Route matches the master. " + CONCEPT_ONLY),

 F(key="v20_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Explain a Career That Looks All Over the Place", "Video 4"),
   trigger="A career break is part of the story. It is not the whole measure "
           "of what you can carry forward.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="The superseded draft proposed V4 and the final master confirms "
       "it. " + CONCEPT_ONLY),
]

# ------------------------------------------------------------------- V21
SETS[21] = [
 F(key="v21_01_the_room_is_different",
   draw=lambda c: X.statement(
     c, "After the change", "You can still do the work.",
     "What keeps catching you are the things nobody thought to explain.",
     dark=True, size=96, support_size=42),
   trigger="And the surprising part is that you can still do the work.",
   purpose="The hook. The surprise is not incompetence, it is context.",
   mode="SHORT CALLOUT OVER CAMERA for the headline, then FULL SCREEN for "
        "the support line.",
   reveal="Headline as a callout over camera, then full screen for the "
          "support line.",
   emphasis="The support line.",
   hold="2 seconds on the callout, 3 on the support.",
   sound="Candidate: one soft tick as the frame goes full screen.",
   status="COPY UPDATE",
   why="Concept retained from the superseded draft with the master's "
       "wording."),

 F(key="v21_02_what_does_travel",
   draw=lambda c: X.ladder(
     c, "Name what came with you", None,
     [("How you break a problem into parts", None),
      ("How you judge whether work is good", None),
      ("How you handle ambiguity", None),
      ("How you work with difficult people", None),
      ("The patterns you have learned to notice", None)],
     foot="That is real experience. It can give you a starting point. It is "
          "also not everything.",
     size=50),
   trigger="Before we talk about relearning, name what came with you.",
   purpose="Say what travels clearly and early, so the video reads as a map "
           "rather than a warning.",
   reveal="One item at a time, then the foot line.",
   emphasis="The foot line, which sets up the rest.",
   hold="About 2 seconds per item, 3 on the foot line.",
   sound="Not a candidate. The licensing frame is the stronger moment.",
   status="COPY UPDATE",
   why="The superseded draft named what travels; the master's list "
       "replaces the copy."),

 F(key="v21_03_five_layers",
   draw=lambda c: X.ladder(
     c, "The five-layer inventory", None,
     [("Domain knowledge", None),
      ("Regulation and credentials", None),
      ("Systems and tooling", None),
      ("Relationships and internal history", None),
      ("How decisions get made here", None)],
     foot="Which layer will block useful contribution first in this specific "
          "role?",
     size=54),
   trigger="I would sort the relearning into five layers: domain knowledge, "
           "regulation and credentials, systems and tooling, relationships "
           "and internal history, and how decisions get made here.",
   purpose="The framework of the video.",
   reveal="One layer at a time in spoken order. Then the foot question.",
   emphasis="The foot question, because the order matters less than it.",
   hold="About 2 seconds per layer, 5 on the complete frame.",
   sound="Candidate: one tick as the foot question lands.",
   status="REUSE",
   why="The five layers were the superseded draft's framework and the "
       "master keeps them. " + CONCEPT_ONLY),

 F(key="v21_04_licensing_is_not_a_mindset",
   draw=lambda c: X.statement(
     c, None, "A licensing requirement is not a mindset issue.",
     "If a role requires a license, registration, or qualification you do "
     "not hold, adjacent experience does not erase that requirement.",
     dark=True, size=88, support_size=42),
   trigger="A licensing requirement is not a mindset issue.",
   purpose="The line that protects the whole channel from sounding like it "
           "claims everything transfers.",
   reveal="Headline alone. Hold. Then the support line.",
   emphasis="The headline, at maximum size.",
   hold="3 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands. This is the "
         "single most important beat in the video.",
   status="REUSE",
   why="The line survives verbatim from the superseded draft into the "
       "master. " + CONCEPT_ONLY),

 F(key="v21_05_easiest_layer_trap",
   draw=lambda c: X.statement(
     c, "Systems and tooling",
     "Do not spend all your preparation time on the easiest-to-name layer.",
     "While the harder context remains untouched.", size=76,
     support_size=44),
   trigger="Do not spend all your preparation time on the easiest-to-name "
           "layer while the harder context remains untouched.",
   purpose="The most common preparation mistake.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 3 seconds.",
   sound="Not a candidate.",
   status="REUSE",
   why="The observation was in the superseded draft and the master keeps "
       "it. " + CONCEPT_ONLY),

 F(key="v21_06_has_anyone_tried_this",
   draw=lambda c: X.statement(
     c, "Relationships and internal history",
     "Has anyone tried this before, and what happened?",
     "The most useful early question in a new environment.", dark=True,
     size=80, support_size=42),
   trigger="A useful early question is: has anyone tried this before, and "
           "what happened?",
   purpose="One practical instruction the viewer can use in week one.",
   reveal="The question, then the support line.",
   emphasis="The question.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="The question survives from the superseded draft into the "
       "master. " + CONCEPT_ONLY),

 F(key="v21_07_read_it_or_practice_it",
   draw=lambda c: X.duo(
     c, "Two ways this gets learned", None,
     ("Some parts can be read",
      "Requirements, documentation, domain facts, formal processes."),
     ("Some parts need practice",
      "Relationships, exception logic, and local decision-making."),
     foot="Do not treat the second group as proof that you made the wrong "
          "move simply because it takes time to learn."),
   trigger="Some parts can be read. Requirements, documentation, domain "
           "facts, formal processes.",
   purpose="Set expectations about pace without inventing a timeline.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 4 on the foot line.",
   sound="Candidate: one tick as the foot line lands.",
   status="REUSE",
   why="The read-or-practice split was in the superseded draft and the "
       "master keeps it. " + CONCEPT_ONLY),

 F(key="v21_08_order_by_what_blocks_you",
   draw=lambda c: X.statement(
     c, "Application", "What stops me contributing usefully first?",
     "That is a better sequence than starting with whatever course looks "
     "easiest to buy.", size=84, support_size=42),
   trigger="Then reorder the list by one question: what stops me "
           "contributing usefully first?",
   purpose="The ordering rule, which is the useful part of the inventory.",
   reveal="Question, then the support line.",
   emphasis="The question.",
   hold="At least 4 seconds.",
   sound="Candidate: one tick as the question lands.",
   status="REUSE",
   why="The ordering rule was the superseded draft's application step and "
       "the master keeps it. " + CONCEPT_ONLY),

 F(key="v21_09_cta",
   draw=lambda c: X.cta(
     c, "One destination", "Not an entire industry.",
     "Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="The Field Kit is linked below if you want a structured way to "
           "separate what travels from what still needs rebuilding.",
   purpose="The single resource route named by the master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Route matches the master. " + CONCEPT_ONLY),

 F(key="v21_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Change Industries Without Starting Over", "Video 9"),
   trigger="Being experienced in a new field can be true at the same time as "
           "having real things left to learn.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="The superseded draft proposed V9 with the older roadmap title. The "
       "final master's string matches the title the built V9 package "
       "actually uses, so the card takes the master's string."),
]
