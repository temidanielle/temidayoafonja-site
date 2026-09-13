# -*- coding: utf-8 -*-
"""Every full-screen asset for V22 and V23.

A frame is a family: one idea, one trigger sentence, and the reveal states an
editor actually cuts to. States exist because the brief asks for sequential
reveals and one active idea at a time, and a PNG cannot animate. Nothing here
invents teaching to justify a visual: every word on every card is either the
script's own wording or a preserved line from the capture packet.

Each trigger is a whole spoken paragraph of its own script, checked in QA.
"""
import masters23 as M
import lay23 as L

CAPTURED = "captured september 12, 2026"
SAMPLE = "fifteen postings, eleven employers, september 2026"


def P(n, i):
    return M.paragraphs(n)[i]


# How a multi-state family is built, which QA verifies against the drawn
# cards rather than taking on trust.
#   ESTABLISH   the whole structure first, then one component at a time
#   ARRIVE      items arrive one at a time; there is no whole to establish
#   BUILD       the same frame gains content across states, nothing activates
#   SINGLE      one state
def F(key, n, para, mode, purpose, layout, states, svg=False, hold=None,
      sound=None, source=None, note=None, treatment=None, build=None):
    return dict(key=key, video=n, trigger=P(n, para), para=para, mode=mode,
                build=build or ("SINGLE" if len(states) == 1 else "BUILD"),
                purpose=purpose, layout=layout, states=states, svg=svg,
                hold=hold or "Hold until the sentence lands, then cut back.",
                sound=sound or "No accent.", source=source, note=note,
                treatment=treatment or "STATEMENT")


# ===================================================================== V22
HCSC1_HEAD = "Sr Divisional Strategy Consultant, Governance"
XAI_HEAD = "Member of Technical Staff, Governance Risk Compliance"

V22 = [

 F("V22_FS_01_TITLE_ONLY", 22, 0, "FULL SCREEN",
   "Let the title sit alone long enough for the viewer to form an "
   "assumption about the level and the pay before anything contradicts it.",
   "Artifact. Nothing else on screen.",
   [dict(name="V22_FS_01_TITLE_ONLY",
         reveal="Single state. No build.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1_HEAD,
             [("Employer", "Health Care Service Corporation"),
              ("Location", "Chicago, Illinois. Remote.")],
             source=CAPTURED, head_size=72))],
   hold="Hold four to five seconds on the title alone. The silence is the "
        "point. Do not reveal the range yet.",
   sound="One restrained reveal accent as the card lands, then nothing.",
   source="A1. HCSC, requisition R0055598.", treatment="ARTIFACT"),

 F("V22_FS_02_THE_CONTRADICTION", 22, 3, "FULL SCREEN",
   "Break the assumption the title created, in two beats rather than one.",
   "Same artifact, two preserved lines, one active at a time.",
   [dict(name="V22_FS_02A_FLOOR",
         reveal="State A on the range sentence. The floor is active.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1_HEAD,
             [("Published range", "$61,500 to $136,100"),
              ("Required qualifications",
               "The ability to accept direction and feedback")],
             active=0, source=CAPTURED)),
    dict(name="V22_FS_02B_FEEDBACK",
         reveal="State B on the next sentence. The requirement line becomes "
                "active and the floor quiets.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1_HEAD,
             [("Published range", "$61,500 to $136,100"),
              ("Required qualifications",
               "The ability to accept direction and feedback")],
             active=1, source=CAPTURED))],
   hold="Two seconds on A, then cut to B on 'And buried in the required "
        "qualifications'. Return to camera on 'That is a real posting.'",
   sound="One accent on A. One quieter accent on B.",
   source="A1. Preserved text, capture packet.", treatment="ARTIFACT"),

 F("V22_FS_03_THE_SAMPLE", 22, 6, "FULL SCREEN",
   "Put the denominator on screen the moment it is spoken, so every later "
   "claim is read against it.",
   "One figure held large with its own limit underneath.",
   [dict(name="V22_FS_03_THE_SAMPLE",
         reveal="Single state.",
         draw=lambda c: L.stat(
             c, "the evidence", "15", "POSTINGS. 11 EMPLOYERS.",
             support="Read in September 2026. A bounded sample, not the "
                     "labor market."))],
   sound="One accent.", treatment="STATEMENT"),

 F("V22_FS_04_THREE_QUESTIONS", 22, 8, "FULL SCREEN",
   "Three questions the viewer will carry through the whole video, arriving "
   "one at a time so none of them is skimmed.",
   "Sequential reveal. Earlier questions stay but quiet.",
   [dict(name="V22_FS_04A_COULD_I_DO_IT",
         reveal="State A on 'Could I do this work?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=0)),
    dict(name="V22_FS_04B_CAN_I_PROVE_IT",
         reveal="State B on 'Can I prove relevant evidence?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=1)),
    dict(name="V22_FS_04C_DO_I_MEET_THE_GATES",
         reveal="State C on 'Do I meet the stated gates?' All three are now "
                "readable together.",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=2,
             foot="the title does not answer any of them"))],
   hold="Build across the sentence. Hold C through the next line, then cut "
        "back to camera.",
   sound="One accent per reveal, quiet.", treatment="SEQUENCE", build="ARRIVE"),

 F("V22_FS_05_PARP", 22, 10, "FULL SCREEN",
   "Establish the whole method once, then teach one component at a time so "
   "four ideas never compete while one is being explained.",
   "Framework established whole, then activated one row at a time.",
   [dict(name="V22_FS_05_PARP_FRAMEWORK",
         reveal="Establish. All four visible, none emphasized.",
         draw=lambda c: L.framework(
             c, "the method", "Four things, every time.",
             [("Problem", "What can this organization not do right now?"),
              ("Authority", "What do the verbs say this person may govern, "
                            "decide, negotiate, recommend, influence, "
                            "support, or execute?"),
              ("Proof", "What evidence would make the employer believe you "
                        "can do this work?"),
              ("Real gap", "What requirement is mandatory, specific, and "
                           "tied to their world rather than yours?")])),
    dict(name="V22_FS_05A_PROBLEM", reveal="Activate 1 on 'Problem.'",
         draw=lambda c: L.framework(
             c, "the method", "Four things, every time.",
             [("Problem", "What can this organization not do right now?"),
              ("Authority", "What do the verbs say this person may govern, "
                            "decide, negotiate, recommend, influence, "
                            "support, or execute?"),
              ("Proof", "What evidence would make the employer believe you "
                        "can do this work?"),
              ("Real gap", "What requirement is mandatory, specific, and "
                           "tied to their world rather than yours?")],
             active=0)),
    dict(name="V22_FS_05B_AUTHORITY", reveal="Activate 2 on 'Authority.'",
         draw=lambda c: L.framework(
             c, "the method", "Four things, every time.",
             [("Problem", "What can this organization not do right now?"),
              ("Authority", "What do the verbs say this person may govern, "
                            "decide, negotiate, recommend, influence, "
                            "support, or execute?"),
              ("Proof", "What evidence would make the employer believe you "
                        "can do this work?"),
              ("Real gap", "What requirement is mandatory, specific, and "
                           "tied to their world rather than yours?")],
             active=1)),
    dict(name="V22_FS_05C_PROOF", reveal="Activate 3 on 'Proof.'",
         draw=lambda c: L.framework(
             c, "the method", "Four things, every time.",
             [("Problem", "What can this organization not do right now?"),
              ("Authority", "What do the verbs say this person may govern, "
                            "decide, negotiate, recommend, influence, "
                            "support, or execute?"),
              ("Proof", "What evidence would make the employer believe you "
                        "can do this work?"),
              ("Real gap", "What requirement is mandatory, specific, and "
                           "tied to their world rather than yours?")],
             active=2)),
    dict(name="V22_FS_05D_REAL_GAP", reveal="Activate 4 on 'Real gap.'",
         draw=lambda c: L.framework(
             c, "the method", "Four things, every time.",
             [("Problem", "What can this organization not do right now?"),
              ("Authority", "What do the verbs say this person may govern, "
                            "decide, negotiate, recommend, influence, "
                            "support, or execute?"),
              ("Proof", "What evidence would make the employer believe you "
                        "can do this work?"),
              ("Real gap", "What requirement is mandatory, specific, and "
                           "tied to their world rather than yours?")],
             active=3))],
   svg=True,
   hold="Establish lands on 'I use four things every time.' Each activation "
        "lands on its own sentence. Cut back to camera on 'Let me show you "
        "what that looks like.'",
   sound="One accent on establish. No accent on the activations.",
   treatment="SEQUENCE", build="ESTABLISH"),

 F("V22_FS_06_HCSC_WALKTHROUGH", 22, 17, "FULL SCREEN",
   "Run the method across one real posting, with the artifact large enough "
   "to read on a phone and only the point being taught explained beside it.",
   "Artifact with numbered teaching points, one active at a time.",
   [dict(name="V22_FS_06A_PROBLEM",
         reveal="Point 1 active on the problem sentence.",
         draw=lambda c: L.hotspot_artifact(
             c, "posting one", HCSC1_HEAD,
             [("Role purpose", "Tracking strategic opportunities"),
              ("The verb", "Supporting the development of divisional "
                           "strategies"),
              ("Qualifications", "Business analytics. Microsoft Access."),
              ("Experience required", "Healthcare or consulting")],
             [("Problem", "No consistent way to track or report the "
                          "division's strategic opportunities."),
              ("Authority", "Supporting. Not setting. Not approving."),
              ("Proof", "Access is unusually specific. The reporting work "
                        "may be very hands-on."),
              ("Real gap", "The clearest stated gate in the document.")],
             active=0, source=CAPTURED)),
    dict(name="V22_FS_06B_AUTHORITY",
         reveal="Point 2 active on 'Now look at authority.'",
         draw=lambda c: L.hotspot_artifact(
             c, "posting one", HCSC1_HEAD,
             [("Role purpose", "Tracking strategic opportunities"),
              ("The verb", "Supporting the development of divisional "
                           "strategies"),
              ("Qualifications", "Business analytics. Microsoft Access."),
              ("Experience required", "Healthcare or consulting")],
             [("Problem", "No consistent way to track or report the "
                          "division's strategic opportunities."),
              ("Authority", "Supporting. Not setting. Not approving."),
              ("Proof", "Access is unusually specific. The reporting work "
                        "may be very hands-on."),
              ("Real gap", "The clearest stated gate in the document.")],
             active=1, source=CAPTURED)),
    dict(name="V22_FS_06C_PROOF",
         reveal="Point 3 active on 'Now proof.'",
         draw=lambda c: L.hotspot_artifact(
             c, "posting one", HCSC1_HEAD,
             [("Role purpose", "Tracking strategic opportunities"),
              ("The verb", "Supporting the development of divisional "
                           "strategies"),
              ("Qualifications", "Business analytics. Microsoft Access."),
              ("Experience required", "Healthcare or consulting")],
             [("Problem", "No consistent way to track or report the "
                          "division's strategic opportunities."),
              ("Authority", "Supporting. Not setting. Not approving."),
              ("Proof", "Access is unusually specific. The reporting work "
                        "may be very hands-on."),
              ("Real gap", "The clearest stated gate in the document.")],
             active=2, source=CAPTURED)),
    dict(name="V22_FS_06D_REAL_GAP",
         reveal="Point 4 active on 'Then the real gap.'",
         draw=lambda c: L.hotspot_artifact(
             c, "posting one", HCSC1_HEAD,
             [("Role purpose", "Tracking strategic opportunities"),
              ("The verb", "Supporting the development of divisional "
                           "strategies"),
              ("Qualifications", "Business analytics. Microsoft Access."),
              ("Experience required", "Healthcare or consulting")],
             [("Problem", "No consistent way to track or report the "
                          "division's strategic opportunities."),
              ("Authority", "Supporting. Not setting. Not approving."),
              ("Proof", "Access is unusually specific. The reporting work "
                        "may be very hands-on."),
              ("Real gap", "The clearest stated gate in the document.")],
             active=3, source=CAPTURED))],
   svg=True,
   hold="One state per method sentence. Between points 2 and 3 the script "
        "interprets the verb; hold point 2 rather than cutting to camera.",
   sound="One quiet accent per point.",
   source="A1. Preserved text, capture packet.", treatment="ARTIFACT", build="ARRIVE"),

 F("V22_FS_07_TITLE_VS_FILE", 22, 22, "FULL SCREEN",
   "Land the first example as three facts the viewer can hold at once.",
   "Three short lines, all visible, no build.",
   [dict(name="V22_FS_07_TITLE_VS_FILE", reveal="Single state.",
         draw=lambda c: L.lines(
             c, "posting one", "What the document actually says.",
             [("In the title", "Four authority-sounding words"),
              ("Published floor", "$61,500"),
              ("Filed internally under", "Information Technology")],
             foot=CAPTURED))],
   sound="One accent.", source="A1.", treatment="ARTIFACT"),

 F("V22_FS_08_RULE01_VERB_BEFORE_TITLE", 22, 23, "FULL SCREEN",
   "Fix the first rule in the viewer's memory in the words the script uses.",
   "Rule card. Navy ground, one line.",
   [dict(name="V22_FS_08_RULE01_VERB_BEFORE_TITLE", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "rule one", "Rule one",
             "Read the verb before you trust the title.",
             support="The verb describes the authority posture."))],
   hold="Hold through the sentence, then cut to camera for the transition.",
   sound="One restrained accent.", treatment="STATEMENT"),

 F("V22_FS_09_PREDEFINED_DECISIONS", 22, 25, "FULL SCREEN",
   "Show that the same employer writes a quarter-million-dollar role in "
   "execution language, without mocking the role.",
   "Artifact, establish then activate the requirement line.",
   [dict(name="V22_FS_09A_SAME_COMPANY",
         reveal="Establish on the title sentence. Same employer, different "
                "department, and the published range.",
         draw=lambda c: L.artifact(
             c, "posting two", "Director of Enterprise Resilience",
             [("Same employer, different department",
               "Health Care Service Corporation"),
              ("Published range", "$133,400 to $247,700"),
              ("Requirement", "Work with executive leadership to make quick "
                              "decisions based on predefined decisions")],
             source=CAPTURED)),
    dict(name="V22_FS_09B_PREDEFINED",
         reveal="Activate the requirement line on 'Predefined decisions.'",
         draw=lambda c: L.artifact(
             c, "posting two", "Director of Enterprise Resilience",
             [("Same employer, different department",
               "Health Care Service Corporation"),
              ("Published range", "$133,400 to $247,700"),
              ("Requirement", "Work with executive leadership to make quick "
                              "decisions based on predefined decisions")],
             active=2, source=CAPTURED))],
   hold="Establish under the title sentence and the range sentence. Cut to "
        "B on the two-word paragraph, hold two seconds, then return to "
        "camera. The defense of the role is delivered on camera, not on a "
        "card.",
   sound="One accent on A. One on B.",
   source="A2. Claim limit: the posting establishes predefined decisions. "
          "It does not establish who created them, and nothing on screen "
          "says otherwise.", treatment="ARTIFACT"),

 F("V22_FS_10_DIRECTOR_COMPARE", 22, 37, "FULL SCREEN",
   "Two roles that share a title word, read side by side so the difference "
   "is visible rather than asserted.",
   "Side-by-side comparison, three reveals in the same frame.",
   [dict(name="V22_FS_10A_SAME_WORD",
         reveal="Establish. Titles and experience floors only.",
         draw=lambda c: L.compare(
             c, "postings three and four",
             "Same title word. So what is actually different?",
             ("posting three", "Director, Talent Management",
              [("Employer", "Zeta Global"),
               ("Experience required", "5 to 7 years")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Employer", "Patriot Growth Insurance Services"),
               ("Experience required", "5 or more years")]),
             foot=CAPTURED)),
    dict(name="V22_FS_10B_SCOPE",
         reveal="Add scope, reporting relationship and authority language "
                "across the two script sentences that describe them.",
         draw=lambda c: L.compare(
             c, "postings three and four",
             "Same title word. So what is actually different?",
             ("posting three", "Director, Talent Management",
              [("Scope", "Leads operational execution of the employee "
                         "lifecycle"),
               ("Reports to", "A Senior Director")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Scope", "Runs the transformation office"),
               ("Partners with", "The Chief Transformation Officer"),
               ("Authority language", "Comfortable influencing executives "
                                      "without relying only on formal "
                                      "authority")]),
             foot=CAPTURED)),
    dict(name="V22_FS_10C_FLOORS",
         reveal="Reveal both compensation floors together, last.",
         draw=lambda c: L.compare(
             c, "postings three and four",
             "Same title word. So what is actually different?",
             ("posting three", "Director, Talent Management",
              [("Scope", "Leads operational execution of the employee "
                         "lifecycle"),
               ("Reports to", "A Senior Director"),
               ("Published floor", "$135,000")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Scope", "Runs the transformation office"),
               ("Partners with", "The Chief Transformation Officer"),
               ("Published floor", "$200,000")]),
             foot="these two jobs at these two employers"))],
   svg=True,
   hold="Establish on 'So what is actually different?' B builds across the "
        "two description sentences. C lands on the floors sentence and must "
        "be followed immediately by the boundary card.",
   sound="One accent on establish. One on the floors reveal. Nothing on B.",
   source="A3 and A4.", treatment="COMPARISON"),

 F("V22_FS_11_DIRECTOR_BOUNDARY", 22, 42, "FULL SCREEN",
   "State the limit of the comparison on screen, immediately after the "
   "money, so the number cannot be carried away on its own.",
   "Statement. Navy ground.",
   [dict(name="V22_FS_11_DIRECTOR_BOUNDARY", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the limit",
             "This does not tell you who is more senior.",
             support="It tells you what these two employers will pay for "
                     "these two jobs.", dark=True, size=72))],
   hold="Cut on 'And I want to be precise here.' Hold through the sentence.",
   sound="No accent. The line should feel like a correction, not a reveal.",
   treatment="STATEMENT"),

 F("V22_FS_12_DIRECTOR_LESSON", 22, 43, "FULL SCREEN",
   "The lesson of the pair, in four words.",
   "Statement.",
   [dict(name="V22_FS_12_DIRECTOR_LESSON", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "posting three and four", "Director did not tell you enough.",
             support="You had to read the rest.", size=86))],
   sound="One accent.", treatment="STATEMENT"),

 F("V22_FS_13_ACRONYM_WALL", 22, 45, "FULL SCREEN",
   "Let the unfamiliar title and the density of the language register "
   "before the reversal lands.",
   "Artifact, then the captured acronym line at full size.",
   [dict(name="V22_FS_13A_UNFAMILIAR_TITLE",
         reveal="Title alone, held.",
         draw=lambda c: L.artifact(
             c, "posting five", XAI_HEAD,
             [("Employer", "xAI"),
              ("Location", "Palo Alto, California and Washington, DC")],
             source=CAPTURED, head_size=66)),
    dict(name="V22_FS_13B_ACRONYM_WALL",
         reveal="Add the acronym line, as captured and unedited.",
         draw=lambda c: L.artifact(
             c, "posting five", XAI_HEAD,
             [("Employer", "xAI"),
              ("In the description",
               "FedRAMP.  ATO.  POAM.  3PAO.  STIG.")],
             active=1, source=CAPTURED, head_size=66, body_size=52))],
   hold="A holds through 'That title tells you almost nothing about level.' "
        "B lands on the acronym sentence and holds through 'somebody "
        "else's world.'",
   sound="One accent on B only.",
   source="A5. Acronyms shown as captured.", treatment="ARTIFACT"),

 F("V22_FS_14_AUTHORITY_POSTURES", 22, 49, "FULL SCREEN",
   "Four authority postures in one document, arriving one at a time so none "
   "of them is read as the whole role.",
   "Numbered sequence, established whole, then activated one at a time.",
   [dict(name="V22_FS_14_AUTHORITY_POSTURES",
         reveal="Establish on 'Authority is mixed.'",
         draw=lambda c: L.sequence(
             c, "posting five",
             "Four different authority postures in one document.",
             [("Executes", "Compliance work"),
              ("Leads", "The authorization process"),
              ("Advises", "Leadership, as the expert in the room"),
              ("Works across teams", "")])),
    dict(name="V22_FS_14A_EXECUTES", reveal="Activate 1.",
         draw=lambda c: L.sequence(
             c, "posting five",
             "Four different authority postures in one document.",
             [("Executes", "Compliance work"),
              ("Leads", "The authorization process"),
              ("Advises", "Leadership, as the expert in the room"),
              ("Works across teams", "")], active=0)),
    dict(name="V22_FS_14B_LEADS", reveal="Activate 2.",
         draw=lambda c: L.sequence(
             c, "posting five",
             "Four different authority postures in one document.",
             [("Executes", "Compliance work"),
              ("Leads", "The authorization process"),
              ("Advises", "Leadership, as the expert in the room"),
              ("Works across teams", "")], active=1)),
    dict(name="V22_FS_14C_ADVISES", reveal="Activate 3.",
         draw=lambda c: L.sequence(
             c, "posting five",
             "Four different authority postures in one document.",
             [("Executes", "Compliance work"),
              ("Leads", "The authorization process"),
              ("Advises", "Leadership, as the expert in the room"),
              ("Works across teams", "")], active=2)),
    dict(name="V22_FS_14D_ACROSS_TEAMS", reveal="Activate 4.",
         draw=lambda c: L.sequence(
             c, "posting five",
             "Four different authority postures in one document.",
             [("Executes", "Compliance work"),
              ("Leads", "The authorization process"),
              ("Advises", "Leadership, as the expert in the room"),
              ("Works across teams", "")], active=3))],
   svg=True,
   hold="One activation per clause inside the authority sentence. Do not "
        "show all four explanations at once.",
   sound="No accents on the activations.",
   source="A5. Preserved text.", treatment="SEQUENCE", build="ESTABLISH"),

 F("V22_FS_15_CEILING", 22, 53, "FULL SCREEN",
   "Hold the salary reveal to the end of the beat, and keep the sample "
   "boundary attached to the claim.",
   "One figure, then the claim with its limit stated on the same card.",
   [dict(name="V22_FS_15A_RANGE",
         reveal="The published range, alone.",
         draw=lambda c: L.stat(
             c, "posting five", "$180,000 to $440,000", "THE PUBLISHED RANGE",
             size=124,
             support="The range on this posting, revealed after the "
                     "authority postures.")),
    dict(name="V22_FS_15B_IN_THIS_SAMPLE",
         reveal="The claim, with 'in this sample' on screen, never implied.",
         draw=lambda c: L.stat(
             c, "posting five", "$440,000",
             "HIGHEST PUBLISHED CEILING IN THIS SAMPLE",
             support="Of the fifteen postings I read. Not a claim about the "
                     "market."))],
   hold="A lands on the range sentence. B lands on 'The least informative "
        "title in this sample.' Hold B through the sentence.",
   sound="One accent on A. One on B.",
   source="A5. Claim is bounded to the fifteen-posting sample.",
   treatment="STATEMENT"),

 F("V22_FS_16_RULE02_READ_DONT_SKIP", 22, 55, "FULL SCREEN",
   "The second rule, paired visually with the first.",
   "Rule card, same construction as rule one.",
   [dict(name="V22_FS_16_RULE02_READ_DONT_SKIP", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "rule two", "Rule two",
             "A title that tells you very little is a reason to read, not a "
             "reason to skip.", support="Read it before you decide it is "
                                        "somebody else's world."))],
   sound="One restrained accent.", treatment="STATEMENT"),

 F("V22_FS_17_REAL_GAP", 22, 57, "FULL SCREEN",
   "Show that a real gap is not always a credential, using the one posting "
   "that said so outright.",
   "Two stated constraints, the second added when it is spoken.",
   [dict(name="V22_FS_17A_GEOGRAPHIC",
         reveal="The geographic constraint, active.",
         draw=lambda c: L.lines(
             c, "posting six", "A gap is not always a credential.",
             [("Stated in the posting",
               "Recruiting experience exclusively in one geographic context "
               "is unlikely to be a strong fit"),
              ("Stated in the posting",
               "At least three hours of overlap with East Africa Time")],
             active=0, foot=CAPTURED)),
    dict(name="V22_FS_17B_TIME_ZONE",
         reveal="The time-zone gate becomes active. The Central Time "
                "qualifier is on screen with it and never without it.",
         draw=lambda c: L.lines(
             c, "posting six", "A gap is not always a credential.",
             [("Stated in the posting",
               "Recruiting experience exclusively in one geographic context "
               "is unlikely to be a strong fit"),
              ("Stated in the posting",
               "At least three hours of overlap with East Africa Time")],
             active=1,
             foot="for someone on central time, that can mean recurring "
                  "7 or 8 a.m. meetings"))],
   hold="A lands on the GiveDirectly sentence. B lands on the overlap "
        "sentence. This beat runs about 45 seconds and must not expand.",
   sound="One accent on each.",
   source="A6. GiveDirectly, named on camera, past tense as spoken. The "
          "7 or 8 a.m. figure is locality-dependent and carries the Central "
          "Time qualifier.", treatment="COMPARISON"),

 F("V22_FS_18_WHAT_IT_WILL_NOT_DO", 22, 63, "FULL SCREEN",
   "Put the limits of the method on screen in the same weight as the method "
   "itself.",
   "Three lines, all visible. No build, because they are spoken as one list.",
   [dict(name="V22_FS_18_WHAT_IT_WILL_NOT_DO", reveal="Single state.",
         draw=lambda c: L.lines(
             c, "the boundary", "What a posting cannot tell you.",
             [("One", "Who will get hired"),
              ("Two", "Whether the authority described on paper exists in "
                      "practice"),
              ("Three", "What the manager is like, or whether the employer "
                        "would stretch for the right person")],
             dark=True, size=40))],
   hold="Hold through the list, then cut to camera for 'It improves your "
        "aim.' That line stays on Temidayo.",
   sound="No accent.", treatment="STATEMENT"),

 F("V22_FS_19_FOUR_THINGS", 22, 65, "FULL SCREEN",
   "Close on the recurring audit this channel returns to, in the script's "
   "own four phrases.",
   "Framework, established whole and left whole.",
   [dict(name="V22_FS_19_FOUR_THINGS", reveal="Single state, no activation.",
         draw=lambda c: L.framework(
             c, "what you get", "A cleaner read on four things.",
             [("What travels", ""), ("What does not", ""),
              ("What you can prove", ""),
              ("What you would have to relearn", "")]))],
   svg=True, sound="One accent.", treatment="SEQUENCE"),

 F("V22_FS_20_CTA", 22, 69, "FULL SCREEN",
   "One ask. No product, no second offer.",
   "Action card, navy ground. The comment ask is added last.",
   [dict(name="V22_FS_20A_RUN_THE_FOUR",
         reveal="The four questions, on the sentence that names them.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one job description.",
             ["Problem.", "Authority.", "Proof.", "Real gap."])),
    dict(name="V22_FS_20B_FIND_THE_VERB",
         reveal="Add the single ask.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one job description.",
             ["Problem.", "Authority.", "Proof.", "Real gap.",
              "Find the verb."],
             resource=("Tell me in the comments what the verb said.", "")))],
   hold="A on the four-questions sentence. B on 'Find the verb.' Hold B to "
        "the end of the spoken line.",
   sound="One accent on A, one on B.", treatment="CTA"),
]


# ===================================================================== V23
SYN = "synthetic example. not a client, an employer, or a researched posting."
FOURLINE = [
    ("Problem before",
     "Three depots ran their own dispatch. On-time sat at 71 percent, and "
     "nobody could say which depot was causing the misses."),
    ("What was mine to decide",
     "I did not own the depots or the budget. I owned the definition of "
     "on-time and the order the three depots moved to it."),
    ("Judgment",
     "I put the worst depot last, because converting it first would have "
     "made the reported numbers drop before the fix took hold."),
    ("Proof and how I know",
     "On-time reached 89 percent inside seven months, measured against the "
     "single definition I wrote."),
]

V23 = [

 F("V23_FS_01_CLAIM", 23, 0, "FULL SCREEN",
   "Put the weak sentence on screen exactly as a reader would meet it.",
   "Claim card. One sentence, nothing to interpret it.",
   [dict(name="V23_FS_01_CLAIM", reveal="Single state.",
         draw=lambda c: L.claim_card(
             c, "the claim", "A good resume sentence",
             "Led a cross-functional transformation that improved on-time "
             "delivery by 18 percent.", synthetic=True, foot=SYN))],
   hold="Hold through the opening line and the three short sentences after "
        "it. Cut to camera on 'And it proves almost nothing.'",
   sound="One accent as it lands.",
   source="Synthetic example. The label is on screen because 18 percent is "
          "visible.", treatment="ARTIFACT"),

 F("V23_FS_02_UNANSWERED", 23, 3, "FULL SCREEN",
   "Show what the sentence leaves unanswered, one question at a time, so "
   "each one is felt rather than skimmed.",
   "Sequential reveal. Earlier questions stay but quiet.",
   [dict(name="V23_FS_02A_WHAT_DID_YOU_DECIDE",
         reveal="On 'what you decided'.",
         draw=lambda c: L.questions(
             c, "what it does not say", "",
             ["What did you decide?", "18 percent from what?",
              "Measured how?", "Compared to what?"], active=0,
             synthetic=True)),
    dict(name="V23_FS_02B_FROM_WHAT",
         reveal="On 'Eighteen percent from what?'",
         draw=lambda c: L.questions(
             c, "what it does not say", "",
             ["What did you decide?", "18 percent from what?",
              "Measured how?", "Compared to what?"], active=1,
             synthetic=True)),
    dict(name="V23_FS_02C_MEASURED_HOW",
         reveal="On 'Measured how?'",
         draw=lambda c: L.questions(
             c, "what it does not say", "",
             ["What did you decide?", "18 percent from what?",
              "Measured how?", "Compared to what?"], active=2,
             synthetic=True)),
    dict(name="V23_FS_02D_COMPARED_TO_WHAT",
         reveal="On 'Compared to what?' All four readable together.",
         draw=lambda c: L.questions(
             c, "what it does not say", "",
             ["What did you decide?", "18 percent from what?",
              "Measured how?", "Compared to what?"], active=3,
             synthetic=True, foot=SYN))],
   hold="Build across the sentence. Cut to camera for 'You did the work. I "
        "believe you. The sentence does not.' That line is the strongest "
        "human moment in the video and must not be covered.",
   sound="One quiet accent per question.",
   source="Synthetic example. Label carried because 18 percent is visible.",
   treatment="SEQUENCE", build="ARRIVE"),

 F("V23_FS_03_FOUR_LINE_PROOF", 23, 5, "FULL SCREEN",
   "Show the finished version first. The viewer sees what the framework "
   "produces before being asked to learn it.",
   "Completed four-line proof, then one line active at a time.",
   [dict(name="V23_FS_03_FOUR_LINE_PROOF",
         reveal="Establish. All four lines complete and readable.",
         draw=lambda c: L.lines(c, "the finished version", "",
                                FOURLINE, synthetic=True, size=36, foot=SYN)),
    dict(name="V23_FS_03A_PROBLEM_BEFORE", reveal="Activate line 1.",
         draw=lambda c: L.lines(c, "the finished version", "", FOURLINE,
                                active=0, synthetic=True, size=36)),
    dict(name="V23_FS_03B_MINE_TO_DECIDE", reveal="Activate line 2.",
         draw=lambda c: L.lines(c, "the finished version", "", FOURLINE,
                                active=1, synthetic=True, size=36)),
    dict(name="V23_FS_03C_JUDGMENT", reveal="Activate line 3.",
         draw=lambda c: L.lines(c, "the finished version", "", FOURLINE,
                                active=2, synthetic=True, size=36)),
    dict(name="V23_FS_03D_PROOF_AND_HOW", reveal="Activate line 4.",
         draw=lambda c: L.lines(c, "the finished version", "", FOURLINE,
                                active=3, synthetic=True, size=36))],
   svg=True,
   hold="Establish on 'I want to show you the finished version first.' Then "
        "one activation per spoken line. Do not cut to camera between them.",
   sound="One accent on establish. None on the activations.",
   source="Synthetic example. 71 and 89 percent are both visible in this "
          "beat, so the label is persistent.", treatment="SEQUENCE", build="ESTABLISH"),

 F("V23_FS_04_CLAIM_VS_PROOF", 23, 10, "FULL SCREEN",
   "One claim beside one reconstructed proof, because the contrast is the "
   "whole teaching.",
   "Side-by-side contrast.",
   [dict(name="V23_FS_04_CLAIM_VS_PROOF", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "same accomplishment", "",
             ("claim", "Led a cross-functional transformation that improved "
                       "on-time delivery by 18 percent.",
              [("What a stranger can do with it", "Believe it, or not.")]),
             ("proof", "Four lines. The before state, the decision, the "
                       "judgment, and how it was measured.",
              [("What a stranger can do with it",
                "Question it, test it, and understand it.")]),
             synthetic=True, foot=SYN))],
   hold="Hold through the sentence, then return to camera.",
   sound="One accent.",
   source="Synthetic example. 18 percent visible.", treatment="COMPARISON"),

 F("V23_FS_05_WHY_THE_ROLE_EXISTS", 23, 14, "FULL SCREEN",
   "Keep the denominator visible when the research is cited.",
   "One figure with its own limit underneath.",
   [dict(name="V23_FS_05_WHY_THE_ROLE_EXISTS", reveal="Single state.",
         draw=lambda c: L.stat(
             c, "the research", "15", "OF 15 JOB DESCRIPTIONS",
             support="Each was written around something the organization "
                     "could not do. This is the sample I read, not the "
                     "market."))],
   sound="One accent.",
   source="The fifteen-posting sample. No generalization beyond it.",
   treatment="STATEMENT"),

 F("V23_FS_06_KINDS_OF_AUTHORITY", 23, 19, "FULL SCREEN",
   "Show that authority has several shapes, so the viewer does not read "
   "formal authority as the only valuable kind.",
   "One row of the words the postings actually separate.",
   [dict(name="V23_FS_06_KINDS_OF_AUTHORITY", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "in the postings i read",
             "Different kinds of authority.",
             [("Govern", ""), ("Negotiate", ""), ("Co-own", ""),
              ("Recommend", ""), ("Influence", ""), ("Support", ""),
              ("Execute", "")],
             foot="one role can contain more than one. none of these is the "
                  "valuable one."))],
   svg=True,
   hold="Hold through the sentence that lists them, then cut back.",
   sound="One accent.",
   source="Authority verbs as separated in the fifteen-posting sample.",
   treatment="SEQUENCE"),

 F("V23_FS_07_EXECUTION_CONTAINS_CHOICES", 23, 22, "FULL SCREEN",
   "Protect execution. The three questions are the script's own, and there "
   "are exactly three.",
   "Three short questions, all visible.",
   [dict(name="V23_FS_07_EXECUTION_CONTAINS_CHOICES",
         reveal="Single state.",
         draw=lambda c: L.questions(
             c, "execution still contains choices", "",
             ["What did you sequence?", "What did you escalate?",
              "What evidence did you challenge?"], dark=True))],
   hold="Hold through the three questions, then cut to camera for the line "
        "about not owning the whole program.",
   sound="One accent.", treatment="SEQUENCE"),

 F("V23_FS_08_AUTHORITY_BOUNDARY", 23, 23, "FULL SCREEN",
   "Draw the authority boundary explicitly, so naming a decision is not "
   "read as claiming the program.",
   "Side-by-side, using the example already on screen.",
   [dict(name="V23_FS_08_AUTHORITY_BOUNDARY", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the boundary", "Name what was yours. Not more than that.",
             ("what i owned", "The definition of on-time, and the order the "
                              "three depots moved to it.", []),
             ("what i did not own", "The depots. The budget. The final "
                                    "decision.", []),
             divider="", synthetic=True, foot=SYN))],
   hold="Cut on 'Those choices are not the same as owning the whole "
        "program.' Hold through 'Name one.'",
   sound="One accent.",
   source="Synthetic example, no figures shown. The label is carried anyway "
          "because the card describes the invented scenario.",
   treatment="COMPARISON"),

 F("V23_FS_09_JUDGMENT_IS_NOT_ONLY_ANALYSIS", 23, 27, "FULL SCREEN",
   "Widen judgment past analysis, using only the forms the postings showed.",
   "Five short forms, all visible, with the sample named on the card.",
   [dict(name="V23_FS_09_JUDGMENT_IS_NOT_ONLY_ANALYSIS",
         reveal="Single state.",
         draw=lambda c: L.framework(
             c, "judgment", "Not only spreadsheets and tradeoff matrices.",
             [("Negotiating", ""), ("Sequencing", ""),
              ("Knowing what to escalate", ""),
              ("Getting a stakeholder to agree", ""),
              ("Committing to an interpretation",
               "when the information was not perfectly clear")],
             foot="as judgment showed up in the postings i read"))],
   sound="One accent.",
   source="Sample-bounded. No categories added beyond the script's list.",
   treatment="SEQUENCE"),

 F("V23_FS_10_THE_CALL", 23, 28, "FULL SCREEN",
   "Name the distinctive call after the viewer has felt it on camera, not "
   "before.",
   "Two sides of one decision. No figures.",
   [dict(name="V23_FS_10_THE_CALL", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the distinctive call", "",
             ("the technically clean move",
              "Convert all three depots at once, in the slow quarter.", []),
             ("what it risked",
              "A drop in the reported numbers before the fix took hold, and "
              "the loss of executive support.", []),
             divider="", synthetic=True, foot=SYN))],
   hold="Cut only after the scene has played on camera. Hold through "
        "'They had a reason. They could have been wrong.'",
   sound="No accent. The beat should stay quiet.",
   source="Synthetic example. Label carried although no figure is shown.",
   treatment="COMPARISON"),

 F("V23_FS_11_NINE_OF_FIFTEEN", 23, 32, "FULL SCREEN",
   "Keep the denominator on screen where the research claim is strongest.",
   "One figure with the denominator in the label, never implied.",
   [dict(name="V23_FS_11_NINE_OF_FIFTEEN", reveal="Single state.",
         draw=lambda c: L.stat(
             c, "the research", "9", "OF 15 ASKED FOR THE MECHANISM",
             support="Business cases with benefit tracking, cost-benefit "
                     "analysis, defined KPIs, metrics used to drive "
                     "decisions, value realization."))],
   hold="Hold through the list of mechanisms.",
   sound="One accent.",
   source="Nine of fifteen. Not most employers, not the market.",
   treatment="STATEMENT"),

 F("V23_FS_12_TWO_HALVES", 23, 34, "FULL SCREEN",
   "Proof has two halves. Show them joined, not opposed.",
   "Two-part card, filled with the example on the second state.",
   [dict(name="V23_FS_12A_TWO_HALVES",
         reveal="The two halves, empty of example.",
         draw=lambda c: L.twopart(
             c, "proof", "",
             ("what changed", "The result itself."),
             ("how do you know?", "The mechanism behind it."))),
    dict(name="V23_FS_12B_FILLED",
         reveal="Fill both halves from the example.",
         draw=lambda c: L.twopart(
             c, "proof", "",
             ("what changed", "On-time reached 89 percent."),
             ("how do you know?", "Measured against one shared definition, "
                                  "with the baseline recalculated backward "
                                  "so the comparison was fair."),
             synthetic=True, foot=SYN))],
   hold="A on 'proof has two halves'. B on the sentence that fills them.",
   sound="One accent on A, one on B.",
   source="Synthetic example. 89 percent visible on B.",
   treatment="COMPARISON"),

 F("V23_FS_13_THE_PAYOFF", 23, 40, "FULL SCREEN",
   "The central editorial payoff of the video, given the screen.",
   "Statement.",
   [dict(name="V23_FS_13_THE_PAYOFF", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "what to remember",
             "Good proof does not make your role sound bigger than it was.",
             support="It makes what you actually carried easier to judge.",
             dark=True, size=68))],
   hold="Cut on 'This is the part I want you to remember.' Hold through "
        "both sentences. Do not cut away early.",
   sound="One restrained accent.", treatment="STATEMENT"),

 F("V23_FS_14_SAME_COMPANY", 23, 44, "FULL SCREEN",
   "Two near-identical postings whose requirements diverge. The employer is "
   "not named, shown, or styled.",
   "Side-by-side, anonymized, with the divergence revealed second.",
   [dict(name="V23_FS_14A_NEAR_IDENTICAL",
         reveal="Establish the overlap only.",
         draw=lambda c: L.compare(
             c, "same company. same level.", "Near-identical language.",
             ("posting one", "Make tradeoffs in a highly ambiguous "
                             "environment.", []),
             ("posting two", "Make tradeoffs in a highly ambiguous "
                             "environment.", []),
             divider="", foot="employer not named. " + CAPTURED)),
    dict(name="V23_FS_14B_DIFFERENT_DOOR",
         reveal="Reveal the requirement that actually differs.",
         draw=lambda c: L.compare(
             c, "same company. same level.", "Near-identical language.",
             ("posting one", "Make tradeoffs in a highly ambiguous "
                             "environment.",
              [("Required", "Years of experience with card products")]),
             ("posting two", "Make tradeoffs in a highly ambiguous "
                             "environment.",
              [("Required", "Years on directly regulated financial "
                            "products")]),
             divider="", foot="employer not named. " + CAPTURED))],
   svg=True,
   hold="A on the sentence about reading two descriptions. B on the "
        "sentence that names the two requirements.",
   sound="One accent on B only.",
   source="B1 and B2. Anonymized by closed editorial decision: no employer "
          "name, no logo, no URL, no identifying styling.",
   treatment="COMPARISON"),

 F("V23_FS_15_DIFFERENT_DOOR", 23, 46, "FULL SCREEN",
   "Land the catch in five words.",
   "Statement.",
   [dict(name="V23_FS_15_DIFFERENT_DOOR", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the catch", "Same sentence. Different door.", size=96))],
   sound="One accent.", treatment="STATEMENT"),

 F("V23_FS_16_REAL_GAP_REMAINS", 23, 49, "FULL SCREEN",
   "Close the video without implying that better evidence removes a real "
   "requirement.",
   "Three words, and the limit stated under them.",
   [dict(name="V23_FS_16_REAL_GAP_REMAINS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "the limit",
             "Sometimes there is a real gap you still have to:",
             [("Learn", ""), ("Earn", ""), ("Experience", "")],
             foot="better proof does not erase that", dark=True))],
   hold="Hold through both sentences.",
   sound="No accent.", treatment="STATEMENT"),

 F("V23_FS_17_CTA", 23, 51, "FULL SCREEN",
   "One action and one resource. Nothing stacked behind them.",
   "Action card, then the single resource line.",
   [dict(name="V23_FS_17A_FOUR_LINES",
         reveal="The four lines, on the sentence that names them.",
         draw=lambda c: L.action(
             c, "one thing to do", "Pick one thing you did.",
             ["Problem before.", "What was mine to decide.", "Judgment.",
              "Proof and how I know."])),
    dict(name="V23_FS_17B_RESOURCE",
         reveal="Add the one resource, on the sentence that names it.",
         draw=lambda c: L.action(
             c, "one thing to do", "Pick one thing you did.",
             ["Problem before.", "What was mine to decide.", "Judgment.",
              "Proof and how I know."],
             resource=("Career Evidence Starter",
                       "temidayoafonja.com/career-evidence-starter")))],
   hold="A on the four-lines sentence. Hold A through 'It is a harder "
        "question than it looks.' B on the resource sentence, and hold to "
        "the end of the spoken line.",
   sound="One accent on A, one on B.", treatment="CTA"),
]

# Watch Next candidate cards. Two per video, one for each recommended
# destination, so whichever the editor chooses already has a real asset. They
# are silent full-screen end cards: no spoken line introduces them and none
# was added to the script to make them work.
def watch_next_cards(n, picks):
    out = []
    for i, (dst, title) in enumerate(picks, 1):
        out.append(dict(
            key="V%d_WN_%02d_V%d" % (n, i, dst),
            video=n, trigger=None, para=None, mode="FULL SCREEN",
            build="SINGLE",
            purpose="Watch Next candidate. Full screen and final. Nothing "
                    "returns to camera after it.",
            layout="Watch Next card, house layout.",
            treatment="WATCH NEXT", svg=False,
            hold="Cut here after the CTA card and end the video on it.",
            sound="No accent.",
            source="Destination is Video %d of the locked V4 to V21 set."
                   % dst,
            note=None,
            states=[dict(name="V%d_WN_%02d_V%d" % (n, i, dst),
                         reveal="Single state. Final card.",
                         draw=(lambda t: (lambda c: L.watch_next(c, t)))(
                             title))]))
    return out


SETS = {22: V22, 23: V23}


def states(n):
    return [(f, s) for f in SETS[n] for s in f["states"]]


def all_states():
    return [(n, f, s) for n in M.VIDEOS for f, s in states(n)]


if __name__ == "__main__":
    from collections import Counter
    for n in M.VIDEOS:
        st = states(n)
        print("V%d  %2d frames  %2d states  %d svg"
              % (n, len(SETS[n]), len(st),
                 sum(1 for f in SETS[n] if f["svg"])))
        print("    treatments:", dict(Counter(f["treatment"]
                                              for f in SETS[n])))
        bad = [f["key"] for f in SETS[n] if not M.trigger_ok(n, f["trigger"])]
        print("    triggers not unique whole paragraphs:", bad or "none")
