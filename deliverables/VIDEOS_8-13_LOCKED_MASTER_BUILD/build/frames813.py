# -*- coding: utf-8 -*-
"""Teaching reference assets for Videos 8 to 13.

Seven teaching concepts per video plus a separate resource card and a separate
Watch Next card. These are reference frames for Riverside and Co-Creator, not a
presentation deck and not one slide per paragraph.

Every trigger is an exact sentence from the corresponding September 9 locked
master; the build fails if one is not found. Concepts were taken from the
earlier Attachment B asset specifications where they still clarify the new
teaching, and every anchor was remapped to the current script.

NOTHING HERE IS A RENDERED ASSET CARRIED OVER. No prior rendered V8 to V13
artwork exists, so every PNG in this batch is a new build from a reusable
concept.
"""
import lay813 as L
from rdeck import Card

ILLUSTRATION = "ILLUSTRATION, NOT A REAL CASE"
SYNTHETIC = "SYNTHETIC DATA  ·  PREPARED AI-ASSISTED EXAMPLE"

# --------------------------------------------------------------------- V8
V8 = [
 dict(id="MG01", file="V8_MG01_Now_It_Looks_Easy.png",
      concept="NORMAL_NOW, from the Attachment B spec. Anchor remapped to the "
              "new opening.",
      draw=lambda c: L.statement(c, None,
          "NOW IT\nLOOKS EASY.",
          "That is exactly why your contribution can become harder to see.",
          dark=True, size=112, support_size=50),
      onscreen="NOW IT LOOKS EASY. / That is exactly why your contribution can "
               "become harder to see.",
      trigger="And that is exactly why your contribution can become harder to see.",
      purpose="The thumbnail line and the whole problem, on screen inside the "
              "first thirty seconds.",
      mode="TRUE FULL SCREEN",
      reveal="Headline alone for 1.4s. Support line at 2.0s. Gentle fade, no "
             "movement.",
      emphasis="NOW IT LOOKS EASY dominates. The support line is secondary.",
      hold="6 to 7 seconds. The support line needs a full read.",
      exit="Cut back to camera for the review and interview scene.",
      captions="Suppress designed captions for the full hold.",
      sound="Optional: one soft whoosh on the headline.",
      label=None),

 dict(id="MG02", file="V8_MG02_Output_Versus_Problem.png",
      concept="DOCUMENTED_CASE, reshaped. The new script contrasts naming an "
              "output with showing the problem behind it.",
      draw=lambda c: L.duo(c, "The demonstration",
          "An output names a thing. It does not name the problem.",
          ("THE OUTPUT", "“I built a leadership framework.”"),
          ("THE PROBLEM BEHIND IT",
           "How broad expectations become usable in real decisions."),
          foot="Same work. Only one of these can be understood by a stranger.",
          mobile=True),
      onscreen="THE OUTPUT: I built a leadership framework / THE PROBLEM "
               "BEHIND IT: how broad expectations become usable in real "
               "decisions",
      trigger="It names an output. It does not tell you why that output was "
              "needed or what had to be worked out before it could exist.",
      purpose="Makes the central distinction concrete using the documented "
              "life-sciences account.",
      mode="TRUE FULL SCREEN",
      reveal="Left column while the weak sentence is read, held alone 2.0s. "
             "Right column on the reframe. Closing line 1.4s later.",
      emphasis="The right column carries more weight.",
      hold="9 to 10 seconds across both spoken versions.",
      exit="Cut back to camera for the self-introduction.",
      captions="Suppress.",
      sound="Optional: one restrained accent as the right column arrives.",
      label=None,
      evidence_note="This frame carries the DOCUMENTED life-sciences account. "
                    "It must stay separate from the hypothetical intake "
                    "example, which is labelled wherever it appears. No "
                    "manager count, baseline, improvement figure or "
                    "sole-person credit appears here or anywhere."),

 dict(id="MG03", file="V8_MG03_Reconstruct_The_Before.png",
      concept="BEFORE, from the Attachment B spec. Weak versus useful, using "
              "the script's own two sentences.",
      draw=lambda c: L.labeled_duo(c, ILLUSTRATION, None,
          "Reconstruct the before.",
          ("THE WEAK VERSION", "“It was chaos.”"),
          ("THE MORE USEFUL VERSION",
           "“There was no shared way to prioritize requests or decide when "
           "they needed escalation.”"),
          foot="Do not invent a number you never measured.",
          mobile=True),
      onscreen="THE WEAK VERSION: It was chaos / THE MORE USEFUL VERSION: "
               "there was no shared way to prioritize requests",
      trigger="The weak version is:",
      purpose="The first framework step, shown as the comparison the script "
              "performs out loud.",
      mode="TRUE FULL SCREEN",
      reveal="Weak version first, alone, 1.8s. Useful version on the reframe. "
             "Closing warning line at 4.0s.",
      emphasis="The useful version. The closing warning is the guard rail.",
      hold="10 to 11 seconds. The right column is a long sentence and needs "
           "the time.",
      exit="Cut back to camera for the sentence stem.",
      captions="Suppress.",
      sound="Optional: one soft click as the useful version arrives.",
      label=ILLUSTRATION,
      evidence_note="The intake process is hypothetical. The stamp must stay "
                    "readable. It is not another real Temidayo case."),

 dict(id="MG04", file="V8_MG04_Show_The_Judgment.png",
      concept="JUDGMENT, from the Attachment B spec, rewritten to the four "
              "questions the new script actually asks.",
      draw=lambda c: L.numbered(c, "Two | Show the judgment",
          ["What was not obvious at the start?",
           "What options existed?",
           "What did I recommend, decide, or bring into agreement?",
           "Which constraint made that choice difficult?"], size=46),
      onscreen="What was not obvious at the start? / What options existed? / "
               "What did I recommend, decide, or bring into agreement? / Which "
               "constraint made that choice difficult?",
      trigger="So ask:",
      purpose="The four questions that surface judgment. The viewer will "
              "screenshot this.",
      mode="TRUE FULL SCREEN",
      reveal="One question at a time, 1.1s apart, as each is spoken. Hold the "
             "complete set.",
      emphasis="Equal weight. This is a checklist, not a hierarchy.",
      hold="10 to 12 seconds. The longest hold in the video.",
      exit="Cut back to camera for the attribution warning.",
      captions="Suppress. This frame gets screenshotted.",
      sound="Optional: one soft accent per question, or none at all. Do not "
            "play four accents just because there are four questions.",
      label=None),

 dict(id="MG05", file="V8_MG05_Existence_Use_Effect.png",
      concept="PROOF_LEVEL, from the Attachment B spec. The evidence "
              "distinction the brief calls out as important.",
      draw=lambda c: L.trio(c, "Three | Keep the proof",
          "Three levels. Not interchangeable.",
          [("EXISTENCE", "It was created."),
           ("USE", "People actually used it."),
           ("EFFECT", "Evidence that something important changed.")],
          foot="Choose the strongest level your evidence actually supports."),
      onscreen="EXISTENCE: it was created / USE: people actually used it / "
               "EFFECT: evidence that something important changed",
      trigger="They are not interchangeable.",
      purpose="The distinction that keeps the whole video honest.",
      mode="TRUE FULL SCREEN",
      reveal="One level at a time, 1.2s apart. The closing line arrives after "
             "a clear beat, at display weight.",
      emphasis="The closing line. It is the instruction, not a footnote.",
      hold="11 to 12 seconds. Each level needs its definition read.",
      exit="Cut back to camera for the prevention-work passage.",
      captions="Suppress.",
      sound="Optional: one restrained click per level, then a single soft "
            "resolve on the closing line. Or fewer.",
      label=None,
      evidence_note="Adoption is not measured effect. Do not let any state "
                    "imply that creating a framework proves people became "
                    "more capable."),

 dict(id="MG06", file="V8_MG06_Four_Sentences.png",
      concept="ACCOUNT, from the Attachment B spec, using the script's exact "
              "four-sentence stem.",
      draw=lambda c: L.numbered(c, "Assemble",
          ["Before this work, this was missing.",
           "My part was this.",
           "The judgment involved this.",
           "What changed was this, and this is how I know."], size=50),
      onscreen="Before this work, this was missing. / My part was this. / The "
               "judgment involved this. / What changed was this, and this is "
               "how I know.",
      trigger="Now put it together:",
      purpose="The deliverable of the whole video, in four lines the viewer "
              "can copy.",
      mode="TRUE FULL SCREEN",
      reveal="One sentence at a time, 1.0s apart. Hold the complete set for a "
             "long beat.",
      emphasis="The fourth line. That is where the evidence boundary lives.",
      hold="11 to 13 seconds. This is the screenshot frame.",
      exit="Cut back to camera for the worked example.",
      captions="Suppress. This frame gets screenshotted.",
      sound="Optional: one accent as the set completes.",
      label=None),

 dict(id="MG07", file="V8_MG07_Where_The_Evidence_Ends.png",
      concept="SCOPE, from the Attachment B spec, focused on the script's own "
              "payoff line about the last sentence.",
      draw=lambda c: L.statement(c, "The worked example",
          "“ITS EFFECT HAD NOT\nYET BEEN ESTABLISHED.”",
          "That last sentence does not weaken the story. It tells the listener "
          "exactly where the evidence ends.",
          dark=True, size=68, support_size=46),
      onscreen="Its effect on turnaround time had not yet been established / "
               "That last sentence does not weaken the story",
      trigger="That last sentence does not weaken the story. It tells the "
              "listener exactly where the evidence ends.",
      purpose="Removes the fear that an honest boundary is a weak boundary.",
      mode="TRUE FULL SCREEN",
      reveal="Quoted line first, 1.8s. Explanation at 2.2s.",
      emphasis="The explanation, not the quotation.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the strip-the-acronyms test.",
      captions="Suppress.",
      sound="Optional: none. Let this one land dry.",
      label=None),

 dict(id="RES", file="V8_RESOURCE_Keep_The_Proof.png",
      concept="Separate resource card, per the brief. Not combined with Watch "
              "Next.",
      draw=lambda c: L.cta(c, "Keep the Proof",
          "The deeper evidence\nsystem and ledger.",
          "The four-sentence account from this video stands on its own.",
          "temidayoafonja.com/keep-the-proof"),
      onscreen="KEEP THE PROOF / temidayoafonja.com/keep-the-proof",
      trigger="Keep the Proof is linked below if you want the deeper evidence "
              "system and reusable ledger.",
      purpose="The single resource route, full screen, address readable on a "
              "phone.",
      mode="TRUE FULL SCREEN",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      emphasis="The URL.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the two closing lines.",
      captions="Suppress. Never cover the address.",
      sound="Optional: one warm accent on the URL.",
      label=None),

 dict(id="WN", file="V8_WATCH_NEXT_Change_Industries.png",
      concept="Separate Watch Next card. Final visual.",
      draw=lambda c: L.watch_next(c,
          "How to Change\nIndustries Without\nStarting Over"),
      onscreen="WATCH NEXT: HOW TO CHANGE INDUSTRIES WITHOUT STARTING OVER",
      trigger="Watch “How to Change Industries Without Starting Over” next.",
      purpose="Final visual. Right of frame kept clear for the clickable "
              "end-screen element.",
      mode="TRUE FULL SCREEN, FINAL",
      reveal="Static. No animation on the final card.",
      emphasis="The title.",
      hold="10 to 14 seconds, through the final spoken line and the "
           "intentional closing hold.",
      exit="NONE. This is the final visual. No camera return, no outro, "
           "nothing after it.",
      captions="Suppress.",
      sound="Optional: none, then a natural 1 to 2 second music fade.",
      label=None),
]

# --------------------------------------------------------------------- V9
V9 = [
 dict(id="MG01", file="V9_MG01_Direct_Industry_Experience.png",
      concept="DESTINATION, from the Attachment B spec, rebuilt on the "
              "sentence the hook actually quotes.",
      draw=lambda c: L.statement(c, None,
          "“DIRECT INDUSTRY\nEXPERIENCE REQUIRED.”",
          "One sentence that can make a very experienced person feel like a "
          "beginner again.", dark=True, size=88, support_size=48),
      onscreen="DIRECT INDUSTRY EXPERIENCE REQUIRED",
      trigger="“Direct industry experience required.”",
      purpose="Puts the exact sentence from the job description on screen, "
              "which is the tension the whole video answers.",
      mode="TRUE FULL SCREEN",
      reveal="Quoted line alone for 1.6s. Support line at 2.2s.",
      emphasis="The quoted line.",
      hold="6 to 7 seconds.",
      exit="Cut back to camera for the two mistakes.",
      captions="Suppress.",
      sound="Optional: one soft impact as the quote lands.",
      label=None),

 dict(id="MG02", file="V9_MG02_Two_Mistakes.png",
      concept="New. The script names two opposite errors and no Attachment B "
              "asset carried both.",
      draw=lambda c: L.duo(c, "Do not make either mistake",
          "Both of these erase something true.",
          ("“I CAN ALREADY DO ALL OF THIS.”", "Erases the unfamiliar context."),
          ("“NONE OF MY EXPERIENCE COUNTS HERE.”",
           "Erases the work you can prove."),
          foot="Separate three things instead.", mobile=True),
      onscreen="I can already do all of this / None of my experience counts "
               "here",
      trigger="So do not make either mistake.",
      purpose="Names both failure modes before the framework, so the framework "
              "arrives as the alternative.",
      mode="TRUE FULL SCREEN",
      reveal="Left column on the first mistake, right column on the second. "
             "Closing line at 3.4s.",
      emphasis="The closing line leads into the framework.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the framework.",
      captions="Suppress.",
      sound="Optional: one restrained accent on the closing line.",
      label=None),

 dict(id="MG03", file="V9_MG03_Capability_Context_Credentials.png",
      concept="THREE_PART_READ, from the Attachment B spec. The hero "
              "framework.",
      draw=lambda c: L.numbered(c, "The three-part read",
          ["CAPABILITY", "CONTEXT", "CREDENTIALS"],
          foot="What can you prove? What changes here? What is actually a "
               "gate?", size=76),
      onscreen="CAPABILITY / CONTEXT / CREDENTIALS",
      trigger="Capability. Context. Credentials.",
      purpose="The hero framework. Returns briefly at each section change.",
      mode="TRUE FULL SCREEN",
      reveal="One word at a time, 0.9s apart. Closing line at 3.2s. Hold the "
             "complete set.",
      emphasis="Equal weight across the three.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      exit="Cut back to camera.",
      captions="Suppress.",
      sound="Optional: one accent per word, then a resolve. Or one resolve "
            "only.",
      label=None),

 dict(id="MG04", file="V9_MG04_Same_Verb_Different_Work.png",
      concept="New. The script's sharpest transfer warning and no Attachment B "
              "asset carried it.",
      draw=lambda c: L.labeled_duo(c, ILLUSTRATION, None,
          "The same verb does not prove the same work.",
          ("“APPROVE” IN ONE ROLE", "Checking a routine item."),
          ("“APPROVE” IN ANOTHER", "Accepting a consequential risk."),
          foot="Compare the scale, the consequences of being wrong, and the "
               "support around it.", mobile=True),
      onscreen="APPROVE: checking a routine item / APPROVE: accepting a "
               "consequential risk",
      trigger="“Approve” can mean checking a routine item in one role and "
              "accepting a consequential risk in another.",
      purpose="Stops the viewer from claiming equivalence off a shared verb.",
      mode="TRUE FULL SCREEN",
      reveal="Left column first, 1.6s. Right column with the weight. Closing "
             "line at 3.6s.",
      emphasis="The right column, then the closing line.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the capability sentence.",
      captions="Suppress.",
      sound="Optional: one accent as the right column arrives.",
      label=ILLUSTRATION,
      evidence_note="A constructed comparison, not a claim about any real "
                    "employer's approval rules."),

 dict(id="MG05", file="V9_MG05_What_Changes_With_The_Setting.png",
      concept="CONTEXT, from the Attachment B spec, using the script's own "
              "list.",
      draw=lambda c: L.numbered(c, "Two | Context",
          ["Customer or user", "Operating model",
           "Standards and approval routes", "Stakeholders",
           "Relationships", "Consequences of error"], size=50),
      onscreen="Customer or user / Operating model / Standards and approval "
               "routes / Stakeholders / Relationships / Consequences of error",
      trigger="Look at the unfamiliar elements:",
      purpose="Makes context concrete instead of a vague word.",
      mode="TRUE FULL SCREEN",
      reveal="Two at a time, 1.0s apart, then the closing line. Do not reveal "
             "six separate states.",
      emphasis="Even weight. The list is not a barrier count, and the "
               "spoken line that follows says so.",
      hold="10 to 11 seconds. Six items need real reading time.",
      exit="Cut back to camera for the better question to ask.",
      captions="Suppress.",
      sound="Optional: one accent when the list completes. Not one per item.",
      label=None,
      spec_note="Two deliberate reductions, both for phone legibility rather "
                "than for space. The script also names Tools, which is left "
                "off so the remaining six stay large, and it is still spoken. "
                "The follow-on line, not every difference is a barrier of "
                "equal size, is also spoken rather than set as a footer, "
                "because keeping it on the frame forced the type down."),

 dict(id="MG06", file="V9_MG06_Confirmed_Preferred_Unclear.png",
      concept="REQUIREMENTS, from the Attachment B spec. The credential "
              "triage.",
      draw=lambda c: L.trio(c, "Three | Credentials",
          "Write down which one it is.",
          [("CONFIRMED", "A requirement."),
           ("PREFERRED", "A qualification they would like."),
           ("STILL UNCLEAR", "Something you have assumed.")],
          foot="You do not argue a closed requirement open with better "
               "wording."),
      onscreen="CONFIRMED REQUIREMENT / PREFERRED QUALIFICATION / STILL "
               "UNCLEAR",
      trigger="Write down:",
      purpose="Turns a vague credential worry into three sortable buckets.",
      mode="TRUE FULL SCREEN",
      reveal="One row at a time, 1.1s apart. Closing line after a beat, at "
             "display weight.",
      emphasis="The closing line.",
      hold="10 to 11 seconds.",
      exit="Cut back to camera for the defensible introduction.",
      captions="Suppress.",
      sound="Optional: one flat accent per row, or one on the closing line "
            "only.",
      label=None),

 dict(id="MG07", file="V9_MG07_A_Defensible_Introduction.png",
      concept="DESTINATION_READ, from the Attachment B spec, reduced to the "
              "three-part shape the script names.",
      draw=lambda c: L.numbered(c, "The shape of the decision",
          ["RELEVANT EVIDENCE", "NAMED LEARNING", "VERIFIED REQUIREMENTS"],
          foot="Not a script to memorize.", size=62),
      onscreen="RELEVANT EVIDENCE / NAMED LEARNING / VERIFIED REQUIREMENTS",
      trigger="It shows the shape of the decision:",
      purpose="The deliverable. What a careful introduction contains.",
      mode="TRUE FULL SCREEN",
      reveal="One at a time, 1.0s apart. Closing line at 3.4s.",
      emphasis="The three terms.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the tradeoff questions.",
      captions="Suppress.",
      sound="Optional: one accent as the set completes.",
      label=None),

 dict(id="RES", file="V9_RESOURCE_Field_Kit.png",
      concept="Separate resource card.",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "An evidence-led read\nof what your work is building.",
          "It does not certify that an employer will accept your background.",
          "temidayoafonja.com/fieldkit"),
      onscreen="CAPABILITY FORMATION FIELD KIT / temidayoafonja.com/fieldkit",
      trigger="The Capability Formation Field Kit is linked below for a "
              "broader evidence-led read of what your current work is building "
              "and what you may be able to carry.",
      purpose="The single resource route.",
      mode="TRUE FULL SCREEN",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      emphasis="The URL.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the Watch Next bridge.",
      captions="Suppress. Never cover the address.",
      sound="Optional: one warm accent on the URL.",
      label=None,
      evidence_note="The support line is the script's own limit. Keep it."),

 dict(id="WN", file="V9_WATCH_NEXT_Before_A_Layoff.png",
      concept="Separate Watch Next card. Final visual.",
      draw=lambda c: L.watch_next(c,
          "Before a Layoff,\nKnow What You\nCan Still Prove"),
      onscreen="WATCH NEXT: BEFORE A LAYOFF, KNOW WHAT YOU CAN STILL PROVE",
      trigger="Watch “Before a Layoff, Know What You Can Still Prove” next.",
      purpose="Final visual. Right of frame kept clear for the end-screen "
              "element.",
      mode="TRUE FULL SCREEN, FINAL",
      reveal="Static.",
      emphasis="The title.",
      hold="10 to 14 seconds, through the final spoken line and the closing "
           "hold.",
      exit="NONE. Final visual. No camera return, no outro.",
      captions="Suppress.",
      sound="Optional: none, then a natural music fade.",
      label=None),
]

# -------------------------------------------------------------------- V10
V10 = [
 dict(id="MG01", file="V10_MG01_Access_Not_Experience.png",
      concept="CONTRIBUTION, from the Attachment B spec, rebuilt on the "
              "script's two-line payoff.",
      draw=lambda c: L.statement(c, None,
          "YOUR EXPERIENCE\nDID NOT DISAPPEAR.\n\nYOUR ACCESS TO THE\nEVIDENCE DID.",
          None, dark=True, size=62),
      onscreen="YOUR EXPERIENCE DID NOT DISAPPEAR. YOUR ACCESS TO THE EVIDENCE "
               "DID.",
      trigger="Your experience did not disappear.",
      purpose="The distinction the whole video rests on, at the end of the "
              "hook.",
      mode="TRUE FULL SCREEN",
      reveal="First statement alone for 1.8s, then the second at 2.4s with a "
             "soft impact.",
      emphasis="The second statement.",
      hold="7 to 8 seconds.",
      exit="Cut back to camera for the not-a-prediction line.",
      captions="Suppress.",
      sound="Optional: one soft impact as the second statement lands.",
      label=None),

 dict(id="MG02", file="V10_MG02_Preparation_Is_Not_Extraction.png",
      concept="PERMISSION, from the Attachment B spec. The compliance "
              "boundary, kept in its scripted position.",
      draw=lambda c: L.statement(c, "The boundary",
          "PREPARATION IS\nNOT EXTRACTION.",
          "No forwarding internal emails, downloading dashboards, copying "
          "customer information, or collecting employee records.",
          size=88, support_size=44),
      onscreen="PREPARATION IS NOT EXTRACTION / no forwarding internal emails, "
               "downloading dashboards, copying customer information, or "
               "collecting employee records",
      trigger="Access to a document does not mean you are entitled to keep it.",
      purpose="States the boundary plainly and early, exactly where the script "
              "places it.",
      mode="TRUE FULL SCREEN",
      reveal="Headline alone for 1.6s. The prohibition list at 2.2s, arriving "
             "as one block rather than four separate accusatory reveals.",
      emphasis="The headline. The list is supporting detail, not a countdown.",
      hold="9 to 10 seconds. The list must be readable.",
      exit="Cut back to camera for the get-guidance line.",
      captions="Suppress.",
      sound="Optional: none. This should not feel dramatic.",
      label=None,
      evidence_note="Never animate any of these actions as a recommended "
                    "behavior. This frame is a prohibition, and the B-roll "
                    "around it must not depict extraction. The script places "
                    "this boundary immediately after the stakes; keep that "
                    "placement."),

 dict(id="MG03", file="V10_MG03_Capture_Qualify_Retrieve.png",
      concept="New hero framework card. The Attachment B set had no single "
              "three-part frame.",
      draw=lambda c: L.numbered(c, "The evidence habit",
          ["CAPTURE THE CONTRIBUTION", "QUALIFY THE CLAIM",
           "MAKE IT RETRIEVABLE"], size=58),
      onscreen="CAPTURE THE CONTRIBUTION / QUALIFY THE CLAIM / MAKE IT "
               "RETRIEVABLE",
      trigger="It is a simple evidence habit:",
      purpose="The hero framework. Returns briefly at each section change.",
      mode="TRUE FULL SCREEN",
      reveal="One line at a time, 0.9s apart. Hold the complete set.",
      emphasis="Equal weight.",
      hold="9 to 10 seconds first time, 3 seconds on each return.",
      exit="Cut back to camera.",
      captions="Suppress.",
      sound="Optional: one accent per line, then a resolve. Or one resolve "
            "only.",
      label=None),

 dict(id="MG04", file="V10_MG04_Calendar_Versus_Contribution.png",
      concept="TASK_ACCOUNT, from the Attachment B spec, using the script's "
              "own two sentences.",
      draw=lambda c: L.labeled_duo(c, ILLUSTRATION, None,
          "One | Capture the contribution, not the calendar.",
          ("THE CALENDAR ENTRY", "“Attended weekly implementation meetings.”"),
          ("THE CONTRIBUTION",
           "“I identified conflicting completion criteria and helped the teams "
           "agree what needed to be true before handoff.”"),
          mobile=True),
      onscreen="THE CALENDAR ENTRY: attended weekly implementation meetings / "
               "THE CONTRIBUTION: I identified conflicting completion criteria",
      trigger="That is a calendar entry. It tells me where you spent time, not "
              "what you contributed.",
      purpose="The clearest before and after in the video.",
      mode="TRUE FULL SCREEN",
      reveal="Calendar entry alone for 2.0s. Contribution on the reframe.",
      emphasis="The right column.",
      hold="10 to 11 seconds. The right column is a long sentence.",
      exit="Cut back to camera for what the record does not claim.",
      captions="Suppress.",
      sound="Optional: one soft click as the contribution arrives.",
      label=ILLUSTRATION,
      evidence_note="Hypothetical. It does not claim delays fell, and the "
                    "frame must not add a number."),

 dict(id="MG05", file="V10_MG05_Confirmed_Qualified_Not_Verified.png",
      concept="CLAIM_STATUS, from the Attachment B spec. The three labels the "
              "brief calls out.",
      draw=lambda c: L.trio(c, "Two | Qualify the claim",
          "Put one label beside the result.",
          [("CONFIRMED", "You have a permitted basis for the statement."),
           ("QUALIFIED", "The result needs its scope attached."),
           ("NOT YET VERIFIED", "Do not present it as established.")],
          foot="Language that survives the next question.", size=46),
      onscreen="CONFIRMED / QUALIFIED / NOT YET VERIFIED",
      trigger="Now put one of three labels beside the result:",
      purpose="The heart of the video. Stops uncertainty disappearing when the "
              "story gets shortened.",
      mode="TRUE FULL SCREEN",
      reveal="One row at a time, 1.2s apart. Closing line after a beat.",
      emphasis="The closing line.",
      hold="11 to 12 seconds. Each definition needs reading.",
      exit="Cut back to camera for the attribution passage.",
      captions="Suppress.",
      sound="Optional: one flat accent per row, or one on the closing line.",
      label=None,
      evidence_note="These are labels for a private record, not a public "
                    "grading scheme. Keep the treatment neutral."),

 dict(id="MG06", file="V10_MG06_Name_It_By_The_Problem.png",
      concept="RETRIEVAL, from the Attachment B spec, using the script's own "
              "comparison.",
      draw=lambda c: L.duo(c, "Three | Make it retrievable",
          "Name the entry by the problem, not the project.",
          ("“PROJECT ALPHA”", "Means nothing outside the company."),
          ("“CONFLICTING HANDOFF CRITERIA”", "Means something to anyone."),
          foot="Add the period, plain-language tags, and the qualification you "
               "need to preserve.", mobile=True),
      onscreen="PROJECT ALPHA vs CONFLICTING HANDOFF CRITERIA",
      trigger="“Conflicting handoff criteria” is more useful than “Project "
              "Alpha,” especially to somebody outside the company.",
      purpose="Makes retrievability concrete in one comparison.",
      mode="TRUE FULL SCREEN",
      reveal="Left column first, 1.6s. Right column with the weight. Closing "
             "line at 3.6s.",
      emphasis="The right column.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the worked entry.",
      captions="Suppress.",
      sound="Optional: one accent as the right column arrives.",
      label=None),

 dict(id="MG07", file="V10_MG07_Two_Reasons_Evidence_Is_Thin.png",
      concept="MISSING, from the Attachment B spec. The distinction the script "
              "insists on.",
      draw=lambda c: L.duo(c, "When the evidence is thin",
          "Two very different problems.",
          ("YOU DID NOT CAPTURE IT", "This needs reconstruction."),
          ("YOU NEVER HAD THE OPPORTUNITY",
           "This needs an honest account of the experience you do and do not "
           "have."),
          foot="Do not solve both by writing a stronger sentence.",
          mobile=True),
      onscreen="YOU DID NOT CAPTURE IT: reconstruction / YOU NEVER HAD THE "
               "OPPORTUNITY: an honest account",
      trigger="Do not solve both problems by writing a stronger sentence.",
      purpose="Keeps the video honest about what a better record cannot fix.",
      mode="TRUE FULL SCREEN",
      reveal="Left column, right column at 1.8s, closing line at 3.6s.",
      emphasis="The closing line.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the already-laid-off passage.",
      captions="Suppress.",
      sound="Optional: one flat accent. This should not feel triumphant.",
      label=None),

 dict(id="RES", file="V10_RESOURCE_Keep_The_Proof.png",
      concept="Separate resource card.",
      draw=lambda c: L.cta(c, "Keep the Proof",
          "The deeper evidence\nsystem and ledger.",
          "You do not need to buy anything to create the first entry.",
          "temidayoafonja.com/keep-the-proof"),
      onscreen="KEEP THE PROOF / temidayoafonja.com/keep-the-proof",
      trigger="Keep the Proof is linked below. It gives you the deeper "
              "evidence system and reusable ledger.",
      purpose="The single resource route.",
      mode="TRUE FULL SCREEN",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      emphasis="The URL.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the two closing lines.",
      captions="Suppress. Never cover the address.",
      sound="Optional: one warm accent on the URL.",
      label=None,
      evidence_note="The support line is the script's own. Keep it."),

 dict(id="WN", file="V10_WATCH_NEXT_AI_Can_Do_The_Task.png",
      concept="Separate Watch Next card. Final visual.",
      draw=lambda c: L.watch_next(c,
          "AI Can Do the Task.\nWhat Are You\nStill Paid For?"),
      onscreen="WATCH NEXT: AI CAN DO THE TASK. WHAT ARE YOU STILL PAID FOR?",
      trigger="Watch “AI Can Do the Task. What Are You Still Paid For?” next.",
      purpose="Final visual. Right of frame kept clear for the end-screen "
              "element.",
      mode="TRUE FULL SCREEN, FINAL",
      reveal="Static.",
      emphasis="The title.",
      hold="10 to 14 seconds, through the final spoken line and the closing "
           "hold.",
      exit="NONE. Final visual. No camera return, no outro.",
      captions="Suppress.",
      sound="Optional: none, then a natural music fade.",
      label=None),
]

# -------------------------------------------------------------------- V11
V11 = [
 dict(id="MG01", file="V11_MG01_Can_We_Reduce_The_Team.png",
      concept="OUTPUT_DECISION, from the Attachment B spec, rebuilt on the "
              "manager's question the hook quotes.",
      draw=lambda c: L.statement(c, None,
          "“DOES THIS MEAN WE\nCAN REDUCE THE TEAM?”",
          "That is the moment the job changes.", dark=True, size=76,
          support_size=50),
      onscreen="DOES THIS MEAN WE CAN REDUCE THE TEAM?",
      trigger="“Does this mean we can reduce the team?”",
      purpose="The stakes, in the manager's own words, inside the first thirty "
              "seconds.",
      mode="TRUE FULL SCREEN",
      reveal="Question alone for 1.8s. Support line at 2.4s.",
      emphasis="The question.",
      hold="7 to 8 seconds.",
      exit="Cut back to camera for the reframe.",
      captions="Suppress.",
      sound="Optional: one soft impact on the question.",
      label=None),

 dict(id="MG02", file="V11_MG02_The_Headline_Rate.png",
      concept="TOTAL_RATE, from the Attachment B spec. Built from the supplied "
              "synthetic rows and independently recomputed.",
      draw=lambda c: L.labeled_duo(c, SYNTHETIC, None,
          "The headline looks better.",
          ("PERIOD 1", "60 of 100 met the target.  60%"),
          ("PERIOD 2", "80 of 100 met the target.  80%"),
          foot="An increase of 20 percentage points.", mobile=True),
      onscreen="PERIOD 1: 60 of 100, 60% / PERIOD 2: 80 of 100, 80% / an "
               "increase of 20 percentage points",
      trigger="Sixty percent to eighty percent.",
      purpose="Shows the number that looks like an improvement, before the "
              "mix is separated out.",
      mode="TRUE FULL SCREEN",
      reveal="Period 1 alone for 1.6s, Period 2 at 2.0s, the percentage-point "
             "line at 3.4s.",
      emphasis="The closing line. It is percentage points, not relative "
               "growth.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the separation into categories.",
      captions="Suppress.",
      sound="Optional: one accent as Period 2 arrives.",
      label=SYNTHETIC,
      evidence_note="Every figure recomputed from "
                    "V11_Demonstration/synthetic_service_report.csv and "
                    "reconciled with the supplied Arithmetic_Check.json. The "
                    "rise is 20 PERCENTAGE POINTS. Relative growth would be "
                    "33.3 percent, which is why the frame says percentage "
                    "points. Invented teaching numbers, not customer data and "
                    "not a result from Temidayo's career."),

 dict(id="MG03", file="V11_MG03_The_Mix_Changed.png",
      concept="CASE_MIX, from the Attachment B spec. The core of the "
              "demonstration.",
      draw=lambda c: L.labeled_readings(c, SYNTHETIC, None,
          "The rates did not move. The mix did.",
          [("ROUTINE", "90% in both periods."),
           ("COMPLEX", "40% in both periods."),
           ("THE MIX", "Routine went from 40% of cases to 80%.")]),
      onscreen="ROUTINE 90% both periods / COMPLEX 40% both periods / THE MIX: "
               "routine went from 40% of cases to 80%",
      trigger="What changed was the mix. The second period had far more "
              "routine cases and fewer complex ones.",
      purpose="The whole point of the demonstration, in one frame.",
      mode="TRUE FULL SCREEN",
      reveal="Routine, then Complex, 1.2s apart, so the viewer sees both rates "
             "hold. Then the mix row at 3.0s with the accent.",
      emphasis="The mix row. It is the explanation.",
      hold="11 to 12 seconds. Do not rush this one.",
      exit="Cut back to camera for the AI-assisted summary passage.",
      captions="Suppress.",
      sound="Optional: one restrained accent on the mix row only.",
      label=SYNTHETIC,
      evidence_note="Recomputed: routine 36/40 and 72/80 both 90 percent; "
                    "complex 24/60 and 8/20 both 40 percent; routine share 40 "
                    "percent then 80 percent. Do not stage an AI failure: the "
                    "prepared AI-assisted summary correctly identifies this "
                    "distinction, and the script says so."),

 dict(id="MG04", file="V11_MG04_Produce_Interpret_Decide.png",
      concept="THREE_JOBS, from the Attachment B spec. The hero framework.",
      draw=lambda c: L.numbered(c, "The framework",
          ["PRODUCE", "INTERPRET", "DECIDE"],
          foot="And verify across all three.", size=76),
      onscreen="PRODUCE / INTERPRET / DECIDE / and verify across all three",
      trigger="Produce. Interpret. Decide.",
      purpose="The hero framework. Returns briefly at each section change.",
      mode="TRUE FULL SCREEN",
      reveal="One word at a time, 0.9s apart. The verify line at 3.2s, "
             "spanning all three rather than arriving as a fourth item.",
      emphasis="The verify line runs through the whole framework.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      exit="Cut back to camera.",
      captions="Suppress.",
      sound="Optional: one accent per word, then a resolve. Or one resolve "
            "only.",
      label=None),

 dict(id="MG05", file="V11_MG05_What_It_Does_Not_Establish.png",
      concept="DECISION_CONTEXT, from the Attachment B spec, using the "
              "script's own two-sided statement.",
      draw=lambda c: L.labeled_duo(c, SYNTHETIC, None,
          "What the summary supports, and what it does not.",
          ("IT SUPPORTS",
           "The rate rose while the mix shifted toward the higher-rate "
           "category."),
          ("IT DOES NOT ESTABLISH",
           "That removing experienced staff would preserve the result."),
          foot="This evidence does not settle that decision.", mobile=True),
      onscreen="IT SUPPORTS: the rate rose while the mix shifted / IT DOES "
               "NOT ESTABLISH: that removing experienced staff would preserve "
               "the result",
      trigger="It means this evidence does not settle that decision.",
      purpose="The boundary between a useful analysis and a consequential "
              "decision.",
      mode="TRUE FULL SCREEN",
      reveal="Left column 2.0s, right column on the reframe, closing line at "
             "4.0s.",
      emphasis="The closing line.",
      hold="11 to 12 seconds. Both columns are full sentences.",
      exit="Cut back to camera for the questions to investigate.",
      captions="Suppress.",
      sound="Optional: one flat accent on the closing line.",
      label=SYNTHETIC,
      evidence_note="The rows do not establish that reducing staffing is safe "
                    "or unsafe, future demand, or work outside the measure. "
                    "Those stay questions to investigate, exactly as the "
                    "master explains. Do not claim humans uniquely notice the "
                    "caveat. The script's other non-finding, that people "
                    "became more effective within each category, is carried "
                    "by MG03, where both rates are shown holding at 90 and 40 "
                    "percent. It is left off this frame so both columns stay "
                    "phone-readable."),

 dict(id="MG06", file="V11_MG06_Who_Owns_The_Consequence.png",
      concept="New. The script's five decision-process questions had no "
              "single Attachment B asset.",
      draw=lambda c: L.numbered(c, "Three | Decide",
          ["Who is authorized to make the change?",
           "Which risks must be accepted or reduced?",
           "What alternatives are available?",
           "What would trigger a review or reversal?",
           "Who will monitor what happens after?"], size=44),
      onscreen="Who is authorized? / Which risks? / What alternatives? / What "
               "would trigger a review? / Who will monitor after?",
      trigger="It is a decision process.",
      purpose="Turns the manager's question into an organizational "
              "responsibility rather than a better report.",
      mode="TRUE FULL SCREEN",
      reveal="One question at a time, 1.0s apart. Hold the complete set.",
      emphasis="Equal weight.",
      hold="11 to 12 seconds. Five questions need real reading time.",
      exit="Cut back to camera for the do-not-take-responsibility line.",
      captions="Suppress. This frame gets screenshotted.",
      sound="Optional: one accent when the set completes. Not one per "
            "question.",
      label=None),

 dict(id="MG07", file="V11_MG07_Map_Your_Role.png",
      concept="ROLE_MAP, from the Attachment B spec. The viewer's exercise.",
      draw=lambda c: L.trio(c, "Map one recurring output",
          "Three columns, one verification question each.",
          [("PRODUCE", "What can an approved tool help produce?"),
           ("INTERPRET", "What must be established before anyone relies on it?"),
           ("DECIDE", "What decision does it inform, and who owns it?")],
          foot="Not your whole profession. One output.", size=44),
      onscreen="PRODUCE / INTERPRET / DECIDE, each with its verification "
               "question",
      trigger="Then put a verification question under each.",
      purpose="The deliverable. What the viewer builds after watching.",
      mode="TRUE FULL SCREEN",
      reveal="One row at a time, 1.2s apart. Closing line after a beat.",
      emphasis="The closing line. Scope control.",
      hold="11 to 13 seconds. This is the screenshot frame.",
      exit="Cut back to camera for the honest-map passage.",
      captions="Suppress. This frame gets screenshotted.",
      sound="Optional: one soft click per row, or one on the closing line.",
      label=None),

 dict(id="RES", file="V11_RESOURCE_Field_Kit.png",
      concept="Separate resource card.",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "A broader read of what\nyour work is building.",
          "Not an AI certification and not a job-security prediction.",
          "temidayoafonja.com/fieldkit"),
      onscreen="CAPABILITY FORMATION FIELD KIT / temidayoafonja.com/fieldkit",
      trigger="The Capability Formation Field Kit is linked below for a "
              "broader read of what your current work is building and where "
              "your options may be expanding or narrowing.",
      purpose="The single resource route.",
      mode="TRUE FULL SCREEN",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      emphasis="The URL.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the closing line.",
      captions="Suppress. Never cover the address.",
      sound="Optional: one warm accent on the URL.",
      label=None,
      evidence_note="The support line is the script's own limit. Keep it."),

 dict(id="WN", file="V11_WATCH_NEXT_Cant_Quit_Yet.png",
      concept="Separate Watch Next card. Final visual.",
      draw=lambda c: L.watch_next(c,
          "What to Do When\nYou Can’t Quit\nYour Job Yet"),
      onscreen="WATCH NEXT: WHAT TO DO WHEN YOU CAN’T QUIT YOUR JOB YET",
      trigger="Watch “What to Do When You Can’t Quit Your Job Yet” next.",
      purpose="Final visual. Right of frame kept clear for the end-screen "
              "element.",
      mode="TRUE FULL SCREEN, FINAL",
      reveal="Static.",
      emphasis="The title.",
      hold="10 to 14 seconds, through the final spoken line and the closing "
           "hold.",
      exit="NONE. Final visual. No camera return, no outro.",
      captions="Suppress.",
      sound="Optional: none, then a natural music fade.",
      label=None),
]

# -------------------------------------------------------------------- V12
V12 = [
 dict(id="MG01", file="V12_MG01_Constraint_Versus_Conclusion.png",
      concept="CONSTRAINT, from the Attachment B spec. The distinction the "
              "whole video runs on.",
      draw=lambda c: L.duo(c, None,
          "These are not the same thing.",
          ("“I CANNOT LEAVE YET.”", "That is a constraint."),
          ("“NOTHING CAN CHANGE.”", "That is a conclusion."),
          dark=True, mobile=True),
      onscreen="I CANNOT LEAVE YET: a constraint / NOTHING CAN CHANGE: a "
               "conclusion",
      trigger="They are not the same thing.",
      purpose="The reframe the entire video depends on, in the hook.",
      mode="TRUE FULL SCREEN",
      reveal="Left column alone for 2.0s. Right column on the second "
             "sentence. Headline last.",
      emphasis="The two labels, constraint and conclusion.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the no-second-full-time-job line.",
      captions="Suppress.",
      sound="Optional: one soft accent as the conclusion column arrives.",
      label=None),

 dict(id="MG02", file="V12_MG02_Protection_First.png",
      concept="New. The script puts safety before the career exercise and the "
              "Attachment B set had no dedicated frame for it.",
      draw=lambda c: L.statement(c, "First",
          "PROTECTION BEFORE\nCAREER STRATEGY.",
          "If health, safety, harassment, discrimination, or another urgent "
          "issue is involved, appropriate support comes first.",
          size=80, support_size=44),
      onscreen="PROTECTION BEFORE CAREER STRATEGY",
      trigger="This is not a request to tolerate an unsafe or harmful "
              "situation.",
      purpose="Places the safety boundary where the script places it, before "
              "any planning.",
      mode="TRUE FULL SCREEN",
      reveal="Headline alone for 1.8s. Support line at 2.4s.",
      emphasis="The headline.",
      hold="8 to 9 seconds. The support line must be readable.",
      exit="Cut back to camera for the cannot-interpret line.",
      captions="Suppress.",
      sound="Optional: none. This must not feel dramatic.",
      label=None,
      evidence_note="This video does not interpret an employment agreement, "
                    "benefits arrangement, immigration rules or a health "
                    "decision. Do not let the frame imply otherwise."),

 dict(id="MG03", file="V12_MG03_Protect_Bound_Prepare.png",
      concept="New hero framework card.",
      draw=lambda c: L.numbered(c, "What you can actually do",
          ["PROTECT WHAT MUST HOLD", "BOUND WHAT YOU CAN",
           "PREPARE ONE POSSIBLE NEXT STEP"], size=54),
      onscreen="PROTECT WHAT MUST HOLD / BOUND WHAT YOU CAN / PREPARE ONE "
               "POSSIBLE NEXT STEP",
      trigger="You need to protect what must hold, put boundaries where you "
              "can, and prepare one possible next step.",
      purpose="The hero framework. Returns briefly at each section change.",
      mode="TRUE FULL SCREEN",
      reveal="One line at a time, 0.9s apart. Hold the complete set.",
      emphasis="Equal weight.",
      hold="9 to 10 seconds first time, 3 seconds on each return.",
      exit="Cut back to camera.",
      captions="Suppress.",
      sound="Optional: one accent per line, then a resolve. Or one resolve "
            "only.",
      label=None),

 dict(id="MG04", file="V12_MG04_What_Must_Hold.png",
      concept="PROTECT, from the Attachment B spec, using the script's own "
              "sentence stem.",
      draw=lambda c: L.statement(c, "One | Protect what must hold",
          "“FOR NOW, ANY CHANGE\nNEEDS TO PROTECT…”",
          "Finish it with the constraint you actually have. This is a private "
          "planning exercise.", dark=True, size=72, support_size=44),
      onscreen="FOR NOW, ANY CHANGE NEEDS TO PROTECT...",
      trigger="Write one sentence:",
      purpose="The first deliverable. One sentence the viewer writes down.",
      mode="TRUE FULL SCREEN",
      reveal="Stem alone for 2.0s. Support line at 2.6s.",
      emphasis="The stem.",
      hold="9 to 10 seconds. The viewer is writing.",
      exit="Cut back to camera for the second step.",
      captions="Suppress.",
      sound="Optional: one soft accent on the stem.",
      label=None,
      evidence_note="You do not have to justify the answer to strangers. The "
                    "pinned comment must not ask viewers to disclose it."),

 dict(id="MG05", file="V12_MG05_Make_The_Tradeoff_Visible.png",
      concept="PRIORITY, from the Attachment B spec, using the script's own "
              "two versions.",
      draw=lambda c: L.duo(c, "Two | Bound what you can",
          "Describe the cost concretely.",
          ("THE FEELING", "“This job is impossible.”"),
          ("THE SPECIFIC ASK",
           "“I can carry A and B at the agreed level. With C added, what "
           "should change in priority, scope, support, or timing?”"),
          foot="Use the conversation only where it is safe and appropriate.",
          mobile=True),
      onscreen="THE FEELING: this job is impossible / THE SPECIFIC ASK: what "
               "should change in priority, scope, support, or timing?",
      trigger="That makes the tradeoff visible.",
      purpose="Gives the viewer a sentence to use, with the safety caveat "
              "attached to the same frame.",
      mode="TRUE FULL SCREEN",
      reveal="Left column 1.8s, right column on the reframe, caveat at 4.0s.",
      emphasis="The right column, then the caveat.",
      hold="11 to 12 seconds. The right column is a long sentence.",
      exit="Cut back to camera for the no-room-to-negotiate passage.",
      captions="Suppress.",
      sound="Optional: one soft click as the specific ask arrives.",
      label=None,
      evidence_note="Not a guarantee of a reasonable response, and not advice "
                    "to refuse work in a way that could put someone at risk. "
                    "The caveat stays on the frame."),

 dict(id="MG06", file="V12_MG06_Question_Not_Activity.png",
      concept="PREPARE, from the Attachment B spec, using the script's own "
              "comparison.",
      draw=lambda c: L.duo(c, "Three | Prepare one possible next step",
          "Choose a question before you choose an activity.",
          ("AN ACTIVITY WITHOUT A TEST", "“I should be on LinkedIn more.”"),
          ("A QUESTION",
           "“What would I need to prove to be considered for that role?”"),
          foot="A small step should answer a useful question or preserve an "
               "option.", mobile=True),
      onscreen="AN ACTIVITY WITHOUT A TEST vs A QUESTION",
      trigger="Choose a question before you choose an activity.",
      purpose="Stops the viewer converting a constraint into busywork.",
      mode="TRUE FULL SCREEN",
      reveal="Activity first, 1.6s. Question on the reframe. Closing line at "
             "3.8s.",
      emphasis="The question column.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the exchange-not-add passage.",
      captions="Suppress.",
      sound="Optional: one accent as the question arrives.",
      label=None),

 dict(id="MG07", file="V12_MG07_The_Four_Lines.png",
      concept="FOUR_LINES, from the Attachment B spec. The deliverable.",
      draw=lambda c: L.numbered(c, "The plan",
          ["What must hold for now?",
           "What part of the current situation can I influence safely?",
           "What one question would make the next option clearer?",
           "When will I review this again?"], size=44),
      onscreen="What must hold for now? / What can I influence safely? / What "
               "one question would make the next option clearer? / When will I "
               "review this again?",
      trigger="Put four lines on a page:",
      purpose="The private plan. The viewer will screenshot this.",
      mode="TRUE FULL SCREEN",
      reveal="One line at a time, 1.1s apart. Hold the complete set.",
      emphasis="The fourth line. The review point is what makes for now real.",
      hold="11 to 13 seconds. This is the screenshot frame.",
      exit="Cut back to camera for the limited-capacity passage.",
      captions="Suppress. This frame gets screenshotted.",
      sound="Optional: one accent when the set completes.",
      label=None,
      evidence_note="If capacity is extremely limited, the script says take "
                    "only the first line and the review point. Do not let the "
                    "frame imply all four are mandatory."),

 dict(id="RES", file="V12_RESOURCE_Career_Decision_Evidence_Check.png",
      concept="Separate resource card.",
      draw=lambda c: L.cta(c, "Free Career Decision Evidence Check",
          "Read the evidence behind\nstaying, moving, or leaving.",
          "It does not replace the guidance a high-stakes decision may "
          "require.", "temidayoafonja.com/career-decisions"),
      onscreen="FREE CAREER DECISION EVIDENCE CHECK / "
               "temidayoafonja.com/career-decisions",
      trigger="The free Career Decision Evidence Check is linked below.",
      purpose="The single resource route.",
      mode="TRUE FULL SCREEN",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      emphasis="The URL.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the closing line.",
      captions="Suppress. Never cover the address.",
      sound="Optional: one warm accent on the URL.",
      label=None,
      evidence_note="The support line is the script's own limit. Keep it."),

 dict(id="WN", file="V12_WATCH_NEXT_Thirty_Day_Plan.png",
      concept="Separate Watch Next card. Final visual.",
      draw=lambda c: L.watch_next(c,
          "A 30-Day Plan\nto Test Your Next\nCareer Move"),
      onscreen="WATCH NEXT: A 30-DAY PLAN TO TEST YOUR NEXT CAREER MOVE",
      trigger="Watch “A 30-Day Plan to Test Your Next Career Move” next.",
      purpose="Final visual. Right of frame kept clear for the end-screen "
              "element.",
      mode="TRUE FULL SCREEN, FINAL",
      reveal="Static.",
      emphasis="The title.",
      hold="10 to 14 seconds, through the final spoken line and the closing "
           "hold.",
      exit="NONE. Final visual. No camera return, no outro.",
      captions="Suppress.",
      sound="Optional: none, then a natural music fade.",
      label=None),
]

# -------------------------------------------------------------------- V13
V13 = [
 dict(id="MG01", file="V13_MG01_Activity_Is_Not_A_Decision.png",
      concept="PLAN_NOT_RESULT, from the Attachment B spec, rebuilt on the "
              "hook's own payoff.",
      draw=lambda c: L.statement(c, None,
          "CAREER ACTIVITY CAN\nMAKE YOU FEEL PRODUCTIVE\nWITHOUT ANSWERING\nTHE DECISION.",
          None, dark=True, size=62),
      onscreen="CAREER ACTIVITY CAN MAKE YOU FEEL PRODUCTIVE WITHOUT ANSWERING "
               "THE DECISION",
      trigger="It can make you feel productive without answering the decision.",
      purpose="Names the problem the plan solves, in the hook.",
      mode="TRUE FULL SCREEN",
      reveal="Two lines, then two lines at 1.8s.",
      emphasis="The final two lines.",
      hold="7 to 8 seconds.",
      exit="Cut back to camera for the thirty-day proposal.",
      captions="Suppress.",
      sound="Optional: one soft impact as the second half lands.",
      label=None),

 dict(id="MG02", file="V13_MG02_Define_Investigate_Try_Decide.png",
      concept="New hero framework card. The four phases.",
      draw=lambda c: L.numbered(c, "The plan",
          ["DEFINE", "INVESTIGATE", "TRY", "DECIDE"],
          foot="And “not this option” is allowed to be a good result.",
          size=68),
      onscreen="DEFINE / INVESTIGATE / TRY / DECIDE",
      trigger="The plan is simple:",
      purpose="The hero framework. Returns briefly at each weekly phase.",
      mode="TRUE FULL SCREEN",
      reveal="One word at a time, 0.9s apart. Closing line at 4.0s.",
      emphasis="The closing line. Permission to get an inconvenient answer.",
      hold="10 to 11 seconds first time, 3 seconds on each return.",
      exit="Cut back to camera for the setup.",
      captions="Suppress.",
      sound="Optional: one accent per word, then a resolve. Or one resolve "
            "only.",
      label=None),

 dict(id="MG03", file="V13_MG03_One_Destination_One_Hypothesis.png",
      concept="HYPOTHESIS, from the Attachment B spec, using the script's own "
              "hypothesis stem.",
      draw=lambda c: L.labeled_duo(c, ILLUSTRATION, None,
          "Choose a destination specific enough to test.",
          ("TOO VAGUE", "“Something strategic.”"),
          ("TESTABLE",
           "“An internal operations-improvement role that uses my cross-team "
           "problem solving and keeps predictable hours.”"), mobile=True),
      onscreen="TOO VAGUE: something strategic / TESTABLE: an internal "
               "operations-improvement role",
      trigger="“Something strategic” is too vague.",
      purpose="Turns a vague ambition into something a month can actually "
              "test.",
      mode="TRUE FULL SCREEN",
      reveal="Vague version 1.6s, testable version on the reframe, closing "
             "line at 4.0s.",
      emphasis="The testable column.",
      hold="11 to 12 seconds. The right column is long and the whole point is "
           "that it is specific, so it gets the time rather than a smaller "
           "size.",
      exit="Cut back to camera for the self-introduction.",
      captions="Suppress.",
      sound="Optional: one soft click as the testable version arrives.",
      label=ILLUSTRATION,
      evidence_note="The operations-improvement destination is the script's "
                    "stated illustration. It is not a real participant story.",
      spec_note="The follow-on line, then write what would change your mind, "
                "is spoken rather than set as a footer. Keeping it on the "
                "frame pushed the stack past the caption-safe line, and "
                "shrinking the testable column would have defeated the "
                "frame's purpose."),

 dict(id="MG04", file="V13_MG04_Days_1_7_Define.png",
      concept="WEEK1, from the Attachment B spec, using the script's four map "
              "questions.",
      draw=lambda c: L.numbered(c, "Days 1 to 7 | Define",
          ["What does the role need?",
           "What evidence do I already have?",
           "What context would be new?",
           "What requirement still needs verification?"], size=48),
      onscreen="What does the role need? / What evidence do I have? / What "
               "context would be new? / What still needs verification?",
      trigger="Build a simple map:",
      purpose="The first week, as four questions rather than a reading list.",
      mode="TRUE FULL SCREEN",
      reveal="One at a time, 1.0s apart. Hold the complete set.",
      emphasis="Equal weight.",
      hold="10 to 11 seconds.",
      exit="Cut back to camera for the do-not-buy-a-qualification warning.",
      captions="Suppress.",
      sound="Optional: one accent when the set completes.",
      label=None),

 dict(id="MG05", file="V13_MG05_Days_8_14_Investigate.png",
      concept="WEEK2, from the Attachment B spec, using the three questions "
              "the script gives verbatim.",
      draw=lambda c: L.numbered(c, "Days 8 to 14 | Investigate",
          ["“What is a difficult ordinary week in this role?”",
           "“Where do people with an adjacent background tend to need "
           "support?”",
           "“Which decisions distinguish someone who is ready?”"], size=42),
      onscreen="What is a difficult ordinary week? / Where do adjacent "
               "backgrounds need support? / Which decisions distinguish "
               "someone who is ready?",
      trigger="Ask about the work.",
      purpose="Replaces asking for reassurance with asking about the work.",
      mode="TRUE FULL SCREEN",
      reveal="One question at a time, 1.2s apart.",
      emphasis="Equal weight.",
      hold="11 to 12 seconds. Three long questions.",
      exit="Cut back to camera for the nobody-owes-you-access line.",
      captions="Suppress.",
      sound="Optional: one accent when the set completes. Not one per "
            "question.",
      label=None,
      evidence_note="A pleasant conversation is not an offer. Nobody owes "
                    "access, and silence is not proof of rejection. Both stay "
                    "spoken."),

 dict(id="MG06", file="V13_MG06_Days_15_21_Work_Sample.png",
      concept="WEEK3, from the Attachment B spec. Carries the required "
              "labelling boundary.",
      draw=lambda c: L.labeled(c, "A WORK SAMPLE, NOT PROFESSIONAL EXPERIENCE",
          None, "TRY ONE\nBOUNDED PIECE.",
          "Public, synthetic, or otherwise permitted material. Set a time "
          "limit before you begin.", dark=True, size=88, support_size=44),
      onscreen="TRY ONE BOUNDED PIECE / a work sample, not professional "
               "experience",
      trigger="Use public, synthetic, or otherwise permitted material.",
      purpose="The third week, with the boundary attached to the same frame "
              "rather than left to a footnote.",
      mode="TRUE FULL SCREEN",
      reveal="Headline alone 1.8s, support line at 2.4s. The stamp is present "
             "from the first frame.",
      emphasis="The stamp and the headline together.",
      hold="9 to 10 seconds.",
      exit="Cut back to camera for the one-page recommendation questions.",
      captions="Suppress.",
      sound="Optional: none.",
      label="A WORK SAMPLE, NOT PROFESSIONAL EXPERIENCE",
      evidence_note="Do not recreate a confidential employer process and do "
                    "not turn the exercise into unpaid operational work for a "
                    "prospective employer. A simulation shows a way of "
                    "thinking; it cannot prove results with real customers, "
                    "real stakes, or a team never led."),

 dict(id="MG07", file="V13_MG07_Continue_Modify_Stop.png",
      concept="WEEK4, from the Attachment B spec, with the inconclusive "
              "outcome the brief requires be kept available.",
      draw=lambda c: L.trio(c, "Days 22 to 30 | Decide",
          "Choose one of three.",
          [("CONTINUE", "Now supported by evidence."),
           ("MODIFY", "An adjacent role, a different setting, more time."),
           ("STOP", "The investigation gave you a reason not to keep "
                    "investing here right now.")],
          foot="And if the evidence is not enough, call it inconclusive.",
          size=44),
      onscreen="CONTINUE / MODIFY / STOP / and if the evidence is not enough, "
               "inconclusive",
      trigger="Then choose one of three decisions:",
      purpose="The decision payoff, with inconclusive kept on the frame so it "
              "stays a real option.",
      mode="TRUE FULL SCREEN",
      reveal="One row at a time, 1.2s apart. The inconclusive line arrives "
             "last, at display weight, after a clear beat.",
      emphasis="The inconclusive line. It is not a footnote.",
      hold="12 to 13 seconds.",
      exit="Cut back to camera for the illustration outcomes.",
      captions="Suppress.",
      sound="Optional: one flat accent per row, or one on the closing line.",
      label=None,
      evidence_note="Do not turn uncertainty into a yes because thirty days "
                    "were spent on it. Inconclusive must remain available."),

 dict(id="RES", file="V13_RESOURCE_Field_Kit.png",
      concept="Separate resource card.",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "An evidence-led read\nof your current position.",
          "Not a thirty-day placement program.",
          "temidayoafonja.com/fieldkit"),
      onscreen="CAPABILITY FORMATION FIELD KIT / temidayoafonja.com/fieldkit",
      trigger="The Capability Formation Field Kit is linked below for a "
              "broader evidence-led read of your current position.",
      purpose="The single resource route.",
      mode="TRUE FULL SCREEN",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      emphasis="The URL.",
      hold="8 to 9 seconds.",
      exit="Cut back to camera for the two closing lines.",
      captions="Suppress. Never cover the address.",
      sound="Optional: one warm accent on the URL.",
      label=None,
      evidence_note="The support line is the script's own limit. It does not "
                    "promise that a destination will accept your background."),

 dict(id="WN", file="V13_WATCH_NEXT_Change_Industries.png",
      concept="Separate Watch Next card. Final visual. Routes to V9, not to "
              "unfinished V14 research.",
      draw=lambda c: L.watch_next(c,
          "How to Change\nIndustries Without\nStarting Over"),
      onscreen="WATCH NEXT: HOW TO CHANGE INDUSTRIES WITHOUT STARTING OVER",
      trigger="For a closer look at separating useful experience from "
              "unfamiliar context and actual requirements, watch “How to "
              "Change Industries Without Starting Over” next.",
      purpose="Final visual. Closes the batch loop back to V9.",
      mode="TRUE FULL SCREEN, FINAL",
      reveal="Static.",
      emphasis="The title.",
      hold="10 to 14 seconds, through the final spoken line and the closing "
           "hold.",
      exit="NONE. Final visual. No camera return, no outro.",
      captions="Suppress.",
      sound="Optional: none, then a natural music fade.",
      label=None),
]

SETS = {8: V8, 9: V9, 10: V10, 11: V11, 12: V12, 13: V13}


def build_cards(n):
    from rdeck import Card
    out = []
    for i, s in enumerate(SETS[n], start=1):
        c = Card(i, s["file"])
        s["draw"](c)
        c.notes = ("%s  (%s)\n\nMode: %s\n\nOn screen: %s\n\nTrigger: %s\n\n"
                   "Purpose: %s\nHold: %s\nExit: %s"
                   % (s["file"], s["id"], s["mode"], s["onscreen"],
                      s["trigger"], s["purpose"], s["hold"], s["exit"]))
        out.append(c)
    return out
