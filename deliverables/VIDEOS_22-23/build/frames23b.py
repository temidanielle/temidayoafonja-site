# -*- coding: utf-8 -*-
"""V22 and V23 full-screen assets, re-anchored to the September 13 FINAL
story-led scripts.

The visual language is unchanged and every surviving concept keeps its
original key, so reuse and retirement stay traceable. What changed is the
anchor: only three of the previous thirty-seven trigger sentences survive the
new scripts, so the spine was rebuilt around the new section order rather
than renamed.

The new scripts are substantially shorter, so the cue count is lower. No
graphic is kept because it already existed, and none is added to fill a gap
the script does not have.
"""
import masters23b as M
import lay23 as L

CAPTURED = "captured september 12, 2026"
SYN = "synthetic example. not a client, an employer, or a researched posting."

# reuse / copy update / rebuild, asserted per family and checked in QA by
# comparing the rendered bytes against the previous package.
REUSE, COPY, REBUILD, NEW = "REUSE", "COPY UPDATE", "REBUILD", "NEW"


def P(n, i):
    return M.paragraphs(n)[i]


def F(key, n, para, purpose, layout, states, cls, svg=False, hold=None,
      sound=None, source=None, treatment="STATEMENT", build=None):
    return dict(key=key, video=n, trigger=P(n, para), para=para,
                mode="FULL SCREEN", purpose=purpose, layout=layout,
                states=states, svg=svg, cls=cls,
                build=build or ("SINGLE" if len(states) == 1 else "BUILD"),
                hold=hold or "Hold until the sentence lands, then cut back.",
                sound=sound or "No accent.", source=source,
                treatment=treatment)


# ===================================================================== V22
HCSC1 = "Sr Divisional Strategy Consultant, Governance"
XAI = "Member of Technical Staff, Governance Risk Compliance"
HCSC_ROWS = [("Role purpose", "Tracking strategic opportunities"),
             ("The verb", "Supporting the development of divisional "
                          "strategies"),
             ("Qualifications", "Business analytics. Microsoft Access.")]
HCSC_POINTS = [
    ("Problem", "A consistent way to evaluate opportunities, track them, and "
                "report on them."),
    ("Authority", "Supporting the development of strategies. Not setting "
                  "them."),
    ("Proof", "Access is unusually specific. The role may be far more "
              "hands-on than the title suggests."),
]
POSTURES = [("Leads", "Authorization work"),
            ("Advises", "Leadership"),
            ("Coordinates", "Across teams"),
            ("Operates as", "A subject-matter expert")]


def _hot(i):
    return lambda c: L.hotspot_artifact(c, "posting one", HCSC1, HCSC_ROWS,
                                        HCSC_POINTS, active=i,
                                        source=CAPTURED)


def _post(a):
    return lambda c: L.sequence(
        c, "posting five", "What the person was expected to do.", POSTURES,
        active=a)


V22 = [
 F("V22_FS_01_TITLE_ONLY", 22, 0,
   "Let the title sit alone long enough for the viewer to form an assumption "
   "before anything contradicts it.",
   "Artifact. Nothing else on screen.",
   [dict(name="V22_FS_01_TITLE_ONLY", reveal="Single state. No build.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1,
             [("Employer", "Health Care Service Corporation"),
              ("Location", "Chicago, Illinois. Remote.")],
             source=CAPTURED, head_size=72))],
   REUSE,
   hold="Hold four to five seconds on the title alone. Do not reveal the "
        "range yet.",
   sound="One restrained reveal accent, then nothing.",
   source="A1. HCSC, requisition R0055598.", treatment="ARTIFACT"),

 F("V22_FS_02_THE_CONTRADICTION", 22, 3,
   "Break the assumption the title created, in two beats rather than one.",
   "Same artifact, two preserved lines, one active at a time.",
   [dict(name="V22_FS_02A_FLOOR",
         reveal="State A on the published range clause. The floor is active.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1,
             [("Published range", "$61,500 to $136,100"),
              ("Required qualifications",
               "The ability to accept direction and feedback")],
             active=0, source=CAPTURED)),
    dict(name="V22_FS_02B_FEEDBACK",
         reveal="State B on the required-qualifications clause of the same "
                "sentence. The requirement line becomes active.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1,
             [("Published range", "$61,500 to $136,100"),
              ("Required qualifications",
               "The ability to accept direction and feedback")],
             active=1, source=CAPTURED))],
   REUSE,
   hold="Both states sit inside one spoken sentence. Cut to B on 'and one of "
        "the required qualifications'. Return to camera on 'That is why I do "
        "not start with the title anymore.'",
   sound="One accent on A, one quieter on B.",
   source="A1. Preserved text, capture packet.", treatment="ARTIFACT"),

 F("V22_FS_03_THE_SAMPLE", 22, 6,
   "Put the denominator on screen the moment it is spoken, so every later "
   "claim is read against it.",
   "One figure held large with its own limit underneath.",
   [dict(name="V22_FS_03_THE_SAMPLE", reveal="Single state.",
         draw=lambda c: L.stat(
             c, "the evidence", "15", "POSTINGS. 11 EMPLOYERS.",
             support="Read for this research. A bounded sample, not the "
                     "labor market."))],
   COPY, sound="One accent."),

 F("V22_FS_05_PARP", 22, 8,
   "Name the method once, in the four words the script uses, before any "
   "section teaches one of them.",
   "Framework, established whole and left whole.",
   [dict(name="V22_FS_05_PARP_FRAMEWORK",
         reveal="Single state. Establish only. Each of the four is taught by "
                "its own section, so nothing is activated here.",
         draw=lambda c: L.framework(
             c, "the method", "The four things.",
             [("Problem", ""), ("Authority", ""), ("Proof", ""),
              ("Real gap", "")]))],
   COPY, svg=True,
   hold="Lands on 'The four things are:' and holds through the four words.",
   sound="One accent.", treatment="SEQUENCE"),

 F("V22_FS_04_THREE_QUESTIONS", 22, 11,
   "Three questions the viewer carries through the whole video, arriving one "
   "at a time so none is skimmed.",
   "Sequential reveal. Earlier questions stay but quiet.",
   [dict(name="V22_FS_04A_COULD_I_DO_IT", reveal="On 'Could I do this work?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=0)),
    dict(name="V22_FS_04B_CAN_I_PROVE_IT",
         reveal="On 'Can I prove relevant evidence?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=1)),
    dict(name="V22_FS_04C_DO_I_MEET_THE_GATES",
         reveal="On 'Do I meet the stated gates?' All three readable "
                "together.",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=2,
             foot="those are not the same question"))],
   COPY, build="ARRIVE",
   hold="Build across the one spoken paragraph, then hold through 'Those are "
        "not the same question.'",
   sound="One quiet accent per reveal.", treatment="SEQUENCE"),

 F("V22_FS_06_HCSC_WALKTHROUGH", 22, 15,
   "Run the method across one real posting, with the artifact large enough "
   "to read on a phone and only the point being taught explained beside it.",
   "Artifact with numbered teaching points, one active at a time. Three "
   "points now: the real gap is taught on a different posting.",
   [dict(name="V22_FS_06A_PROBLEM",
         reveal="Point 1 active, on the sentence that names what the "
                "division needed.", draw=_hot(0)),
    dict(name="V22_FS_06B_AUTHORITY",
         reveal="Point 2 active, on the sentence that names the verb.",
         draw=_hot(1)),
    dict(name="V22_FS_06C_PROOF",
         reveal="Point 3 active, on the sentence that lists the evidence.",
         draw=_hot(2))],
   COPY, svg=True, build="ARRIVE",
   hold="The three states are spread across the PROBLEM, AUTHORITY and PROOF "
        "sections. Cut away to camera between them; each returns to the same "
        "artifact.",
   sound="One quiet accent per point.",
   source="A1. Preserved text, capture packet.", treatment="ARTIFACT"),

 F("V22_FS_08_RULE01_READ_THE_VERBS", 22, 18,
   "Fix the second step in the viewer's memory in the words the script now "
   "uses.",
   "Rule card. Navy ground, one line.",
   [dict(name="V22_FS_08_RULE01_READ_THE_VERBS", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "rule one", "Rule one", "Read the verbs.",
             support="This is where job descriptions become much more "
                     "honest."))],
   COPY,
   hold="Hold through the next sentence, then cut back to camera.",
   sound="One restrained accent."),

 F("V22_FS_09_PREDEFINED_DECISIONS", 22, 25,
   "Show that the same employer writes a role near a quarter of a million "
   "dollars in bounded-decision language, without mocking the role.",
   "Artifact, establish then activate the requirement line.",
   [dict(name="V22_FS_09A_SAME_COMPANY",
         reveal="Establish on the title and range sentence.",
         draw=lambda c: L.artifact(
             c, "posting two", "Director of Enterprise Resilience",
             [("Same employer, different department",
               "Health Care Service Corporation"),
              ("Published range", "$133,400 to $247,700"),
              ("Requirement", "Work with executive leadership to make quick "
                              "decisions based on predefined decisions")],
             source=CAPTURED)),
    dict(name="V22_FS_09B_PREDEFINED",
         reveal="Activate the requirement line on the sentence that quotes "
                "it.",
         draw=lambda c: L.artifact(
             c, "posting two", "Director of Enterprise Resilience",
             [("Same employer, different department",
               "Health Care Service Corporation"),
              ("Published range", "$133,400 to $247,700"),
              ("Requirement", "Work with executive leadership to make quick "
                              "decisions based on predefined decisions")],
             active=2, source=CAPTURED))],
   REUSE,
   hold="Establish under the title sentence. Cut to B on the requirement "
        "sentence, then return to camera. The defense of the role is "
        "delivered on camera, not on a card.",
   sound="One accent on A, one on B.",
   source="A2. Claim limit: the posting establishes predefined decisions. It "
          "does not establish who created them, and nothing on screen says "
          "otherwise.", treatment="ARTIFACT"),

 F("V22_FS_17_REAL_GAP", 22, 43,
   "Show that a real gap is not always a skill gap, using the one posting "
   "that said so outright.",
   "Two stated constraints, the second added when it is spoken.",
   [dict(name="V22_FS_17A_GEOGRAPHIC",
         reveal="The geographic boundary, active.",
         draw=lambda c: L.lines(
             c, "posting six", "A real gap is not always a skill gap.",
             [("Stated in the posting",
               "Recruiting experience exclusively in one geographic context "
               "is unlikely to be a strong fit"),
              ("Stated in the posting",
               "At least three hours of overlap with East Africa Time")],
             active=0, foot=CAPTURED)),
    dict(name="V22_FS_17B_TIME_ZONE",
         reveal="The overlap requirement becomes active, with the script's "
                "own reading of it on the card.",
         draw=lambda c: L.lines(
             c, "posting six", "A real gap is not always a skill gap.",
             [("Stated in the posting",
               "Recruiting experience exclusively in one geographic context "
               "is unlikely to be a strong fit"),
              ("Stated in the posting",
               "At least three hours of overlap with East Africa Time")],
             active=1,
             foot="an operating constraint, not a skill gap"))],
   COPY,
   hold="A on the GiveDirectly sentence. B on the overlap sentence, held "
        "through 'It is an operating constraint.'",
   sound="One accent on each.",
   source="A6. GiveDirectly, named on camera, past tense as spoken. The "
          "posting states the overlap requirement; no local meeting time is "
          "stated or implied.", treatment="COMPARISON"),

 F("V22_FS_10_DIRECTOR_COMPARE", 22, 50,
   "Two roles that share a level word, read side by side so the difference "
   "is visible rather than asserted.",
   "Side-by-side comparison, scope revealed second.",
   [dict(name="V22_FS_10A_SAME_WORD",
         reveal="Establish. The two titles and their experience minimums.",
         draw=lambda c: L.compare(
             c, "two director roles", "Two different industries.",
             ("posting three", "Director, Talent Management",
              [("Employer", "Zeta Global"),
               ("Experience minimum", "5 to 7 years")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Employer", "Patriot Growth Insurance Services"),
               ("Experience minimum", "5 or more years")]),
             foot=CAPTURED)),
    dict(name="V22_FS_10B_SCOPE",
         reveal="Add scope and reporting relationship across the two "
                "sentences that describe them.",
         draw=lambda c: L.compare(
             c, "two director roles", "Two different industries.",
             ("posting three", "Director, Talent Management",
              [("Focus", "Operational execution"),
               ("Reports to", "A Senior Director")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Focus", "Runs a transformation office"),
               ("Partners with", "A Chief Transformation Officer")]),
             foot=CAPTURED))],
   COPY, svg=True,
   hold="Establish on the two-titles sentence. B builds across the two "
        "description sentences, then cut to camera for the four-line "
        "distinction.",
   sound="One accent on establish. Nothing on B.",
   source="A3 and A4. No compensation comparison is made: the script no "
          "longer draws one.", treatment="COMPARISON"),

 F("V22_FS_12_DIRECTOR_LESSON", 22, 55,
   "Land the section in the four beats the script actually speaks.",
   "Four short lines, arriving one at a time.",
   [dict(name="V22_FS_12A_SAME_WORD", reveal="On 'Same broad level word.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=0)),
    dict(name="V22_FS_12B_DIFFERENT_WORK", reveal="On 'Different work.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=1)),
    dict(name="V22_FS_12C_DIFFERENT_AUTHORITY",
         reveal="On 'Different authority.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=2)),
    dict(name="V22_FS_12D_DIFFERENT_CONTEXT",
         reveal="On 'Different context.' All four readable together.",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=3,
             foot="a title can help you find a posting"))],
   REBUILD, build="ARRIVE",
   hold="One beat per spoken line. Hold the fourth through the sentence "
        "about a title not finishing the read.",
   sound="One quiet accent per line.", treatment="SEQUENCE"),

 F("V22_FS_13_ACRONYM_WALL", 22, 62,
   "Let the unfamiliar title and the density of the language register before "
   "the reversal lands.",
   "Artifact, then the captured acronym line at full size.",
   [dict(name="V22_FS_13A_UNFAMILIAR_TITLE", reveal="Title alone, held.",
         draw=lambda c: L.artifact(
             c, "posting five", XAI,
             [("Employer", "xAI"),
              ("Location", "Palo Alto, California and Washington, DC")],
             source=CAPTURED, head_size=66)),
    dict(name="V22_FS_13B_ACRONYM_WALL",
         reveal="Add the acronym line, as captured and unedited.",
         draw=lambda c: L.artifact(
             c, "posting five", XAI,
             [("Employer", "xAI"),
              ("In the description",
               "FedRAMP.  ATO.  POAM.  3PAO.  STIG.")],
             active=1, source=CAPTURED, head_size=66, body_size=52))],
   REUSE,
   hold="A holds through 'The title tells you almost nothing about "
        "seniority.' B lands on the acronym sentence.",
   sound="One accent on B only.",
   source="A5. Acronyms shown as captured.", treatment="ARTIFACT"),

 F("V22_FS_14_AUTHORITY_POSTURES", 22, 65,
   "Four things the posting says the person does, arriving one at a time so "
   "none is read as the whole role.",
   "Numbered sequence, established whole, then activated one at a time.",
   [dict(name="V22_FS_14_AUTHORITY_POSTURES",
         reveal="Establish on 'But underneath that'.", draw=_post(None)),
    dict(name="V22_FS_14A_LEADS",
         reveal="Activate 1 on 'lead authorization work'.", draw=_post(0)),
    dict(name="V22_FS_14B_ADVISES",
         reveal="Activate 2 on 'advise leadership'.", draw=_post(1)),
    dict(name="V22_FS_14C_COORDINATES",
         reveal="Activate 3 on 'coordinate across teams'.", draw=_post(2)),
    dict(name="V22_FS_14D_SUBJECT_MATTER_EXPERT",
         reveal="Activate 4 on 'operate as a subject-matter expert'.",
         draw=_post(3))],
   COPY, svg=True, build="ESTABLISH",
   hold="One activation per clause inside the one spoken sentence. Do not "
        "show all four explanations at once.",
   sound="No accents on the activations.",
   source="A5. Preserved text. The old EXECUTES posture is retired: the new "
          "script does not say it.", treatment="SEQUENCE"),

 F("V22_FS_15_CEILING", 22, 66,
   "Hold the salary reveal to the end of the beat, and keep the sample "
   "boundary attached to the claim.",
   "One figure, then the claim with its limit stated on the same card.",
   [dict(name="V22_FS_15A_RANGE", reveal="The published range, alone.",
         draw=lambda c: L.stat(
             c, "posting five", "$180,000 to $440,000", "THE PUBLISHED RANGE",
             size=124,
             support="The range on this posting, revealed after the four "
                     "postures.")),
    dict(name="V22_FS_15B_IN_THIS_SAMPLE",
         reveal="The claim, with 'in the sample' on screen, never implied.",
         draw=lambda c: L.stat(
             c, "posting five", "$440,000",
             "HIGHEST PUBLISHED CEILING IN THE SAMPLE",
             support="Of the 15 postings read for this research. Not a claim "
                     "about the market."))],
   COPY,
   hold="A on the range sentence. B on the least-informative-title sentence.",
   sound="One accent on A, one on B.",
   source="A5. Claim bounded to the 15-posting sample."),

 F("V22_FS_16_RULE02_READ_THE_WORK", 22, 68,
   "The second rule, paired visually with the first.",
   "Rule card, same construction as rule one.",
   [dict(name="V22_FS_16_RULE02_READ_THE_WORK", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "rule two", "Rule two",
             "If a title confuses you, do not automatically skip the job.",
             support="Read the work."))],
   COPY, sound="One restrained accent."),

 F("V22_FS_18_WHAT_IT_WILL_NOT_DO", 22, 70,
   "Put the limits of the method on screen in the same weight as the method "
   "itself, and only the limits the script speaks.",
   "Six short lines, all visible. Spoken as one boundary passage.",
   [dict(name="V22_FS_18_WHAT_IT_WILL_NOT_DO", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "the boundary", "What this method will not tell you.",
             [("Who will get hired", ""),
              ("Whether the authority on paper exists in practice", ""),
              ("Whether a manager would flex on a requirement", ""),
              ("Whether bias will shape the decision", ""),
              ("Whether the team culture matches the posting", ""),
              ("That reading better guarantees a better outcome", "")],
             dark=True))],
   REBUILD,
   hold="Lands on the first boundary sentence and holds through 'Reading "
        "better does not guarantee a better outcome.' Cut to camera for 'It "
        "gives you a cleaner read.'",
   sound="No accent."),

 F("V22_FS_19_FOUR_THINGS", 22, 76,
   "Close on the recurring audit this channel returns to, in the script's "
   "own four phrases.",
   "Framework, established whole and left whole.",
   [dict(name="V22_FS_19_FOUR_THINGS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what you get", "A cleaner read on four things.",
             [("What may travel", ""), ("What may not", ""),
              ("What you can prove", ""),
              ("What you would still need to learn", "")]))],
   COPY, svg=True, sound="One accent.", treatment="SEQUENCE"),

 F("V22_FS_20_CTA", 22, 79,
   "One ask. No product, no comment ask, nothing stacked.",
   "Action card, navy ground. The verb instruction is added last.",
   [dict(name="V22_FS_20A_WRITE_FOUR_LINES",
         reveal="The four lines, on the sentence that names them.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one job description.",
             ["Problem.", "Authority.", "Proof.", "Real gap."])),
    dict(name="V22_FS_20B_STRONGEST_VERB",
         reveal="Add the closing instruction.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one job description.",
             ["Problem.", "Authority.", "Proof.", "Real gap."],
             resource=("Then find the strongest verb in the posting.", "")))],
   COPY,
   hold="A on 'Write four lines:'. B on 'Then find the strongest verb'. Hold "
        "B to the end of the spoken line.",
   sound="One accent on A, one on B.", treatment="CTA"),
]


# ===================================================================== V23
FOURLINE = [
    ("Problem before",
     "Three depots ran their own dispatch. On-time delivery sat at 71 "
     "percent, and the depots counted lateness differently."),
    ("What was mine to decide",
     "I did not own the depots or the budget. I owned the definition of "
     "on-time and the order the three depots moved to it."),
    ("Judgment",
     "The obvious move was to convert all three at once. I put the worst "
     "depot last because converting it first would have made the numbers "
     "look worse before the fix took hold."),
    ("Proof and how I know",
     "On-time delivery reached 89 percent across all three within seven "
     "months, measured against one definition, with the baseline "
     "recalculated so the comparison was fair."),
]
UNANSWERED = ["What was broken before?", "What were you allowed to decide?",
              "What was hard?", "Where did the 18 percent come from?"]


def _four(a):
    return lambda c: L.lines(c, "the finished version", "", FOURLINE,
                             active=a, synthetic=True, size=34,
                             foot=None if a is not None else SYN)


def _unans(a):
    return lambda c: L.questions(c, "what it does not say", "", UNANSWERED,
                                 active=a, synthetic=True,
                                 foot=SYN if a == 3 else None)


V23 = [
 F("V23_FS_01_CLAIM", 23, 0,
   "Put the weak sentence on screen exactly as a reader would meet it.",
   "Claim card. One sentence, nothing to interpret it.",
   [dict(name="V23_FS_01_CLAIM", reveal="Single state.",
         draw=lambda c: L.claim_card(
             c, "the claim", "A strong resume sentence",
             "Led a cross-functional transformation that improved on-time "
             "delivery by 18 percent.", synthetic=True, foot=SYN))],
   COPY,
   hold="Hold through the three short sentences after it. Cut to camera on "
        "'And a stranger still cannot tell what you actually did.'",
   sound="One accent as it lands.",
   source="Synthetic example. Label carried because 18 percent is visible.",
   treatment="ARTIFACT"),

 F("V23_FS_02_UNANSWERED", 23, 4,
   "Show what the sentence leaves unanswered, one question at a time, in the "
   "four things the new hook names.",
   "Sequential reveal. Earlier questions stay but quiet.",
   [dict(name="V23_FS_02A_BROKEN_BEFORE",
         reveal="On 'what was broken before'.", draw=_unans(0)),
    dict(name="V23_FS_02B_ALLOWED_TO_DECIDE",
         reveal="On 'what you were allowed to decide'.", draw=_unans(1)),
    dict(name="V23_FS_02C_WHAT_WAS_HARD",
         reveal="On 'what was hard'.", draw=_unans(2)),
    dict(name="V23_FS_02D_WHERE_THE_NUMBER_CAME_FROM",
         reveal="On 'where the 18 percent came from'. All four readable "
                "together.", draw=_unans(3))],
   COPY, build="ARRIVE",
   hold="Build across the one spoken paragraph. Cut to camera for 'You did "
        "the work. I believe you. The sentence does not.' That is the "
        "strongest human moment in the video and must not be covered.",
   sound="One quiet accent per question.",
   source="Synthetic example. Label carried because 18 percent is visible.",
   treatment="SEQUENCE"),

 F("V23_FS_03_FOUR_LINE_PROOF", 23, 13,
   "Show the finished version first. The viewer sees what the framework "
   "produces before being asked to learn it.",
   "Completed four-line proof, then one line active at a time.",
   [dict(name="V23_FS_03_FOUR_LINE_PROOF",
         reveal="Establish. All four lines complete and readable.",
         draw=_four(None)),
    dict(name="V23_FS_03A_PROBLEM_BEFORE", reveal="Activate line 1.",
         draw=_four(0)),
    dict(name="V23_FS_03B_MINE_TO_DECIDE", reveal="Activate line 2.",
         draw=_four(1)),
    dict(name="V23_FS_03C_JUDGMENT", reveal="Activate line 3.",
         draw=_four(2)),
    dict(name="V23_FS_03D_PROOF_AND_HOW", reveal="Activate line 4.",
         draw=_four(3))],
   COPY, svg=True, build="ESTABLISH",
   hold="Establish on 'Let me show you the finished version first.' Then one "
        "activation per spoken line. Do not cut to camera between them.",
   sound="One accent on establish. None on the activations.",
   source="Synthetic example. 71 and 89 percent are both visible, so the "
          "label is persistent.", treatment="SEQUENCE"),

 F("V23_FS_04_CLAIM_VS_PROOF", 23, 19,
   "One claim beside one reconstructed proof, because the contrast is the "
   "whole teaching.",
   "Side-by-side contrast.",
   [dict(name="V23_FS_04_CLAIM_VS_PROOF", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "same accomplishment", "",
             ("claim", "Led a cross-functional transformation that improved "
                       "on-time delivery by 18 percent.",
              [("What another person can do with it", "Believe it, or not.")]),
             ("proof", "What was broken, what was yours, and the "
                       "measurement.",
              [("What another person can do with it",
                "Question it, test it, and understand it.")]),
             synthetic=True, foot=SYN))],
   COPY, hold="Hold through the sentence, then return to camera.",
   sound="One accent.",
   source="Synthetic example. 18 percent visible.", treatment="COMPARISON"),

 F("V23_FS_07_EXECUTION_CONTAINS_CHOICES", 23, 35,
   "Protect execution. The five questions are the script's own, and there "
   "are exactly five.",
   "Five short questions, all visible.",
   [dict(name="V23_FS_07_EXECUTION_CONTAINS_CHOICES", reveal="Single state.",
         draw=lambda c: L.questions(
             c, "execution still contains decisions", "",
             ["What did you sequence?", "What did you escalate?",
              "What did you challenge?", "What did you recommend?",
              "What tradeoff did you put in front of someone else?"],
             dark=True, size=52))],
   COPY,
   hold="Hold through the five questions, then cut to camera for the "
        "sentence about the postings.",
   sound="One accent.", treatment="SEQUENCE"),

 F("V23_FS_08_AUTHORITY_BOUNDARY", 23, 37,
   "Draw the boundary explicitly, so naming a decision is not read as "
   "claiming authority that was not there.",
   "Two sides of one distinction.",
   [dict(name="V23_FS_08_AUTHORITY_BOUNDARY", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the boundary", "",
             ("not this", "Pretending you had more authority than you did.",
              []),
             ("this", "Finding the decisions that were genuinely yours.",
              []),
             divider=""))],
   COPY,
   hold="Cut on 'So this is not about pretending' and hold through 'the "
        "decisions that were genuinely yours.'",
   sound="One accent.", treatment="COMPARISON"),

 F("V23_FS_10_THE_CALL", 23, 43,
   "Name the distinctive call after the viewer has felt it on camera, not "
   "before.",
   "Two sides of one decision. No figures.",
   [dict(name="V23_FS_10_THE_CALL", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the distinctive call", "",
             ("not the distinctive part", "Running the numbers.", []),
             ("the judgment", "Deciding not to start with the worst depot.",
              []),
             divider="", synthetic=True, foot=SYN))],
   COPY,
   hold="Cut only after the scene has played on camera. Hold through 'That "
        "call could have been wrong.'",
   sound="No accent. The beat should stay quiet.",
   source="Synthetic example. Label carried although no figure is shown.",
   treatment="COMPARISON"),

 F("V23_FS_12_TWO_HALVES", 23, 52,
   "Result and mechanism are two separate things. Show them joined, not "
   "opposed.",
   "Two-part card, filled with the example on the second state.",
   [dict(name="V23_FS_12A_TWO_HALVES",
         reveal="The two halves, named.",
         draw=lambda c: L.twopart(
             c, "proof", "",
             ("result", "What changed."),
             ("mechanism", "How you know it changed."))),
    dict(name="V23_FS_12B_FILLED",
         reveal="Fill both halves from the example, in the script's own "
                "words.",
         draw=lambda c: L.twopart(
             c, "proof", "",
             ("result", "On-time delivery reached 89 percent."),
             ("mechanism", "Measured against one shared definition, with the "
                           "baseline recalculated backward."),
             synthetic=True, foot=SYN))],
   COPY, svg=True,
   hold="A on 'Those are two separate things.' B across the two quoted "
        "sentences.",
   sound="One accent on A, one on B.",
   source="Synthetic example. 89 percent visible on B.",
   treatment="COMPARISON"),

 F("V23_FS_13_THE_PAYOFF", 23, 64,
   "The central editorial payoff of the video, given the screen.",
   "Statement.",
   [dict(name="V23_FS_13_THE_PAYOFF", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "what to remember",
             "Good proof does not make your role sound bigger than it was.",
             support="It makes what you actually carried easier to judge.",
             dark=True, size=68))],
   REUSE,
   hold="Cut on the sentence and hold through the one that follows it.",
   sound="One restrained accent."),

 F("V23_FS_16_REAL_GAP_REMAINS", 23, 71,
   "Close the video without implying that better evidence removes a real "
   "requirement.",
   "Four requirements the script names, all visible.",
   [dict(name="V23_FS_16_REAL_GAP_REMAINS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "the catch", "Another employer may still require:",
             [("Domain knowledge", ""), ("A credential", ""),
              ("Regulated experience", ""),
              ("Direct exposure you do not have", "")],
             dark=True))],
   COPY, hold="Hold through the sentence.", sound="No accent.",
   treatment="SEQUENCE"),

 F("V23_FS_18_CHANGE_THE_EMPHASIS", 23, 75,
   "The final distinction of the video, given its own card because it is the "
   "line that keeps the whole method honest.",
   "Statement.",
   [dict(name="V23_FS_18_CHANGE_THE_EMPHASIS", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the catch", "Change the emphasis, not the truth.",
             support="Do not rewrite history to fit the role.", size=86))],
   NEW, sound="One restrained accent."),

 F("V23_FS_17_CTA", 23, 79,
   "One action and one resource. Nothing stacked behind them.",
   "Action card, then the single resource line.",
   [dict(name="V23_FS_17A_FOUR_LINES",
         reveal="The four lines, on the sentence that names them.",
         draw=lambda c: L.action(
             c, "one thing to do", "Pick one accomplishment.",
             ["Problem before.", "What was mine to decide.", "Judgment.",
              "Proof and how I know."])),
    dict(name="V23_FS_17B_RESOURCE",
         reveal="Add the one resource, on the sentence that names it.",
         draw=lambda c: L.action(
             c, "one thing to do", "Pick one accomplishment.",
             ["Problem before.", "What was mine to decide.", "Judgment.",
              "Proof and how I know."],
             resource=("Career Evidence Starter",
                       "temidayoafonja.com/career-evidence-starter")))],
   COPY,
   hold="A on 'Write four lines:'. B on the resource sentence, held to the "
        "end of the spoken line.",
   sound="One accent on A, one on B.", treatment="CTA"),
]

SETS = {22: V22, 23: V23}

# Families the previous package carried that the new scripts no longer teach.
RETIRED = {
 "V22_FS_06D_REAL_GAP":
   "The new Real Gap section is taught on the GiveDirectly posting, not on "
   "the first HCSC posting, so the fourth walkthrough point has no spoken "
   "job.",
 "V22_FS_07_TITLE_VS_FILE":
   "The new script no longer teaches the internal Information Technology "
   "filing point.",
 "V22_FS_10C_FLOORS":
   "The new script draws no compensation comparison between the two Director "
   "roles.",
 "V22_FS_11_DIRECTOR_BOUNDARY":
   "With no compensation comparison there is no compensation boundary to "
   "state.",
 "V23_FS_05_WHY_THE_ROLE_EXISTS":
   "The new script does not make the fifteen-of-fifteen claim.",
 "V23_FS_06_KINDS_OF_AUTHORITY":
   "The new script does not list the authority verbs in V23.",
 "V23_FS_09_JUDGMENT_IS_NOT_ONLY_ANALYSIS":
   "The new judgment section teaches through the depot scene rather than "
   "through a list of forms of judgment.",
 "V23_FS_11_NINE_OF_FIFTEEN":
   "The new script states the research in bounded prose and makes no "
   "nine-of-fifteen claim.",
 "V23_FS_14_SAME_COMPANY":
   "The new script drops the same-company comparison entirely.",
 "V23_FS_15_DIFFERENT_DOOR":
   "With the comparison gone there is no different-door conclusion to land.",
}


def states(n):
    return [(f, s) for f in SETS[n] for s in f["states"]]


def watch_next_cards(n, picks):
    out = []
    for i, (dst, title) in enumerate(picks, 1):
        out.append(dict(
            key="V%d_WN_%02d_V%d" % (n, i, dst), video=n, trigger=None,
            para=None, mode="FULL SCREEN", build="SINGLE", cls=REUSE,
            purpose="Watch Next candidate. Full screen and final. Nothing "
                    "returns to camera after it.",
            layout="Watch Next card, house layout.",
            treatment="WATCH NEXT", svg=False,
            hold="Cut here after the CTA card and end the video on it.",
            sound="No accent.",
            source="Destination is Video %d of the locked V4 to V21 set."
                   % dst,
            states=[dict(name="V%d_WN_%02d_V%d" % (n, i, dst),
                         reveal="Single state. Final card.",
                         draw=(lambda t: (lambda c: L.watch_next(c, t)))(
                             title))]))
    return out


if __name__ == "__main__":
    from collections import Counter
    for n in M.VIDEOS:
        st = states(n)
        print("V%d  %2d families  %2d states  %d svg"
              % (n, len(SETS[n]), len(st),
                 sum(1 for f in SETS[n] if f["svg"])))
        print("    classes:   ", dict(Counter(f["cls"] for f in SETS[n])))
        print("    treatments:", dict(Counter(f["treatment"]
                                              for f in SETS[n])))
        bad = [f["key"] for f in SETS[n] if not M.trigger_ok(n, f["trigger"])]
        print("    triggers not unique whole paragraphs:", bad or "none")
        lab = [f["key"] for f in SETS[n] if M.is_label(f["trigger"])]
        print("    cues landing on a section label:", lab or "none")
    print("\nretired from the active edit:", len(RETIRED))
