# -*- coding: utf-8 -*-
"""The eight core slides and their reveal states.

Employer names appear nowhere in this file. Role A and Role B are the only
public identifiers. Every line of posting language is rephrased for mobile
readability and mapped back to its source in FLAGSHIP_JD_PROVENANCE.md.
"""
import fl_lay as L

TITLE = "How to Change Careers After 10+ Years Without Starting Over"
THUMB = "WHAT ACTUALLY TRANSFERS?"
PREFIX = "FLAG"

A_LABEL = "CURRENT / ADJACENT ROLE"
B_LABEL = "DESTINATION ROLE"
# The same source line carries slides 1, 2 and 5. The correction pass named
# slide 1; it is applied to all three so the deck does not run two different
# source lines, and that decision is flagged in the correction report.
SOURCE_FOOT = ("Two real U.S. job postings. Company names removed so we can "
               "focus on the work.")

# Slide 2, first read. Rows sit in the same order on both sides so the eye
# can travel across them. match marks where the language is the same or
# adjacent, which is not a claim that the work is the same.
S2_LEFT = ("Role A", "Senior Manager", [
    (None, "Complex programs"), (None, "Governance"),
    (None, "Risk and dependencies"), (None, "Budgets"),
    (None, "Executive updates"), (None, "Cross-functional influence")])
S2_RIGHT = ("Role B", "Director", [
    (None, "Enterprise transformation"), (None, "Governance"),
    (None, "Enterprise risk and dependencies"), (None, "Budget tracking"),
    (None, "Executive and board reporting"), (None, "C-suite alignment")])
S2_MATCH = (0, 1, 2, 3, 4, 5)

S4_ROWS = [
    ("Cross-functional influence",
     "Moving work across people you do not directly control"),
    ("Program judgment",
     "Managing risk, dependencies and complex execution"),
    ("Executive communication",
     "Turning work into decisions for senior leaders"),
    ("Governance rhythm",
     "Milestones, escalation, reporting and accountability"),
]

S5_LEFT = ("Role A", "Seniority shows up through", [
    (None, "People leadership"), (None, "Program delivery"),
    (None, "Team development"), (None, "Execution governance")])
S5_RIGHT = ("Role B", "Seniority shows up through", [
    (None, "Enterprise judgment"), (None, "C-suite alignment"),
    (None, "Operating infrastructure"), (None, "Controls and reporting"),
    (None, "Board-level communication")])

# The prompt offers two bottom lines for slide 5 and says to prefer the
# second if uncertain. Role A asks for 8+ years at Senior Manager and Role B
# asks for 10+ at Director, so these are not the same career level and the
# first line would be inaccurate. The second is used.
S5_BANNER = "A higher title doesn't just mean more of the same work."

S6_GAPS = [
    "PE or public-company operating context",
    "Financial reporting and controls",
    "Major corporate milestones and audits",
    "Finance, accounting and legal partnership",
    "Board-level operating rhythm",
]

S7_CELLS = [
    ("What travels?", ["Cross-functional influence", "Program governance",
                       "Risk and dependency management",
                       "Executive communication",
                       "Complex program delivery"]),
    ("What doesn't just come with you?",
     ["Internal relationships", "Company-specific systems",
      "Existing reputation", "Positional authority",
      "What made you senior there"]),
    ("What can you prove?", ["Programs owned", "Decisions made",
                             "Risks managed", "Stakeholders influenced",
                             "Outcomes delivered"]),
    ("What may need to be learned or built?",
     ["Enterprise controls", "Financial-reporting rigor",
      "Public or PE operating context", "Audit and milestone readiness",
      "Board-level operating rhythm"]),
]


def _s1(c):
    L.compare_rows(c, "THE MOVE", None,
                   (A_LABEL, "Senior Manager", [(None, "Program Management")]),
                   (B_LABEL, "Director", [(None, "Enterprise Transformation")]),
                   divider="→", foot=SOURCE_FOOT, dark=False)


def _s2(shown, match, banner):
    def draw(c):
        L.compare_rows(c, "FIRST READ", "A lot of this looks familiar.",
                       S2_LEFT, S2_RIGHT, match=match, banner=banner,
                       dark=True, divider=None, shown=shown,
                       foot=None if banner else SOURCE_FOOT)
    return draw


def _s3(c):
    L.beat(c, "THE RE-HOOK", "Matching words aren't enough.",
           "What decision sits under the word?", dark=True)


def _s4(active):
    def draw(c):
        L.framework(c, "WHAT TRAVELS?", None, S4_ROWS, active=active,
                    foot="Real overlap. Not the same work.",
                    dark=False)
    return draw


def _s5(shown, banner):
    def draw(c):
        L.compare_rows(c, "THE DIFFERENCE", None, S5_LEFT, S5_RIGHT,
                       banner=banner, dark=True, divider=None, shown=shown,
                       foot=None if banner else SOURCE_FOOT)
    return draw


def _s6(n):
    def draw(c):
        items = [(g, None) for g in S6_GAPS[:n]]
        if not items:
            L.beat(c, "THE REAL GAP", "This is not\na wording problem.",
                   None, dark=True)
            return
        L.framework(c, "THE REAL GAP", "This is not a wording problem.",
                    items, active=None, dark=True,
                    foot=("Better resume language doesn't create experience "
                          "you haven't had." if n == len(S6_GAPS)
                          else "Context the destination role is built around."))
    return draw


def _s7(shown):
    def draw(c):
        L.matrix(c, "NOW WE CAN READ THE MOVE.", None, S7_CELLS,
                 shown=shown, dark=False,
                 foot=("One move, four columns." if shown == 4 else None))
    return draw


def _s8(c):
    L.beat(c, "THE POINT",
           "You can be experienced\nand new at the same time.",
           "Not starting from zero. Not pretending everything transfers.",
           dark=True)


# (family, [(state name, draw, pacing note)])
SETS = [
 ("FLAG_01_THE_MOVE", [
   ("FLAG_01_THE_MOVE", _s1, "Slide 1 complete. One state. The viewer sees "
    "the move before any conclusion.")]),
 ("FLAG_02_FIRST_READ", [
   ("FLAG_02A_ROLE_A", _s2(1, (), None), "Role A alone, while the spoken "
    "line describes the work already being done."),
   ("FLAG_02B_ROLE_B", _s2(2, (), None), "Role B added. The viewer compares "
    "before being told what to see."),
   ("FLAG_02C_MATCHING", _s2(2, S2_MATCH, None), "Matching and adjacent "
    "language marked, on the line about finding matching words everywhere."),
   ("FLAG_02D_WHERE_ADVICE_STOPS", _s2(2, S2_MATCH,
    "This is where “transferable skills” advice often stops."),
    "The statement lands only after the viewer has already seen the overlap.")]),
 ("FLAG_03_RE_HOOK", [
   ("FLAG_03_MATCHING_WORDS", _s3, "One short beat. Held while the question "
    "is asked, then straight back to camera.")]),
 ("FLAG_04_WHAT_TRAVELS", [
   ("FLAG_04_ESTABLISH", _s4(None), "The four together, so the viewer sees "
    "the shape before any one row is taught."),
   ("FLAG_04A_INFLUENCE", _s4(0), "One row at a time as each capability is "
    "named."),
   ("FLAG_04B_JUDGMENT", _s4(1), "As above."),
   ("FLAG_04C_COMMUNICATION", _s4(2), "As above."),
   ("FLAG_04D_GOVERNANCE", _s4(3), "As above.")]),
 ("FLAG_05_THE_DIFFERENCE", [
   ("FLAG_05A_ROLE_A", _s5(1, None), "Role A alone, on how seniority shows "
    "up in the current role."),
   ("FLAG_05B_ROLE_B", _s5(2, None), "Role B added. The split becomes "
    "visible without narration."),
   ("FLAG_05C_HIGHER_TITLE", _s5(2, S5_BANNER), "The distinction, after the "
    "viewer has read both columns.")]),
 ("FLAG_06_THE_REAL_GAP", [
   ("FLAG_06A_HEADLINE", _s6(0), "Headline alone. The beat before the list."),
   ("FLAG_06B_FIRST_TWO", _s6(2), "The first two context items."),
   ("FLAG_06C_ALL_GAPS", _s6(5), "All five, with the payoff line."),
   ]),
 ("FLAG_07_THE_FULL_READ", [
   ("FLAG_07A_TRAVELS", _s7(1), "One column at a time, matching the spoken "
    "order of the four questions."),
   ("FLAG_07B_DOES_NOT", _s7(2), "As above."),
   ("FLAG_07C_PROVE", _s7(3), "As above."),
   ("FLAG_07D_COMPLETE", _s7(4), "The complete read. The visual payoff of "
    "the sequence and the frame the viewer photographs.")]),
 ("FLAG_08_THE_POINT", [
   ("FLAG_08_EXPERIENCED_AND_NEW", _s8, "Slide 8 complete. One state, held.")]),
]


def states():
    for fam, sts in SETS:
        for name, draw, note in sts:
            yield fam, name, draw, note
