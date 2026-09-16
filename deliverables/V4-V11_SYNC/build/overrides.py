# -*- coding: utf-8 -*-
"""The five copy updates, applied batch-locally.

Each replaces a line the reconciled script no longer supports with wording
the reconciled script does carry. The design, layout and reveal structure
of every card is kept: only the words change, and only the affected states
are re-rendered.

The archived sprint build is never edited. These overrides are applied to
the frame set in memory at render time, so the locked packages keep
rendering exactly as they shipped.
"""

# family key -> (state name, replacement draw, what changed and its source)
def build(L):
    """L is the batch's layout module, so the house design is unchanged."""
    return {
     "NEW_V4_FS_02_INEFFICIENT_AND_DEVELOPMENTAL": (
       "NEW_V4_FS_02_INEFFICIENT_AND_DEVELOPMENTAL",
       lambda c: L.twopart(
           c, "the tension", "A task can be both.",
           ("boring", "Doing the same kind of work again and again."),
           ("developmental", "It taught you what good looked like."),
           joiner="+"),
       "'Slow, repetitive, sometimes wrong.' replaced with 'Doing the same "
       "kind of work again and again.' from THE PROBLEM, which now reads: "
       "a task can be boring and still teach you something."),

     "NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT": (
       "NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT",
       lambda c: L.framework(
           c, "what the work taught", "",
           [("Repetition", "Pattern recognition"),
            ("Fixing mistakes", "Judgment"),
            ("Seeing enough examples", "Learning the pattern")]),
       "'Seeing ten bad examples / Why the eleventh one is different' "
       "replaced with 'Seeing enough examples / Learning the pattern' from "
       "THREE THINGS TO WATCH: does the person still see enough examples "
       "to learn the pattern?"),

     "NEW_V5_FS_05_INDISPENSABLE_AND_LESS_PORTABLE": (
       "NEW_V5_FS_05_INDISPENSABLE_AND_LESS_PORTABLE",
       lambda c: L.twopart(
           c, "story", "At the same time.",
           ("more indispensable", "Fewer people can operate without you."),
           ("harder to move", "Harder for a team to imagine moving you."),
           joiner="+"),
       "'Your experience becomes tied to the internal system.' replaced "
       "with 'Harder for a team to imagine moving you.' from THE TRAP. "
       "The reconciled V5 never names an internal system. It does carry "
       "portability, in A SIMPLE EXAMPLE and in WHEN TO BUILD OPTIONS, so "
       "the earlier rationale that no portability passage remains was "
       "wrong. The card is kept and re-anchored to the wording the script "
       "actually uses."),

     "NEW_V5_FS_10_CTA": (
       "NEW_V5_FS_10_CTA",
       lambda c: L.action(
           c, "one question to ask", "Is it also helping you become:",
           ["More capable.", "More visible.", "More useful somewhere else."],
           resource=("If not, being useful may be part of why you feel "
                     "stuck.", "")),
       "'More portable.' replaced with 'More useful somewhere else.' and "
       "the foot line aligned to the CLOSE, which reads: more capable, "
       "more visible, or more useful somewhere else. If not, being useful "
       "may be part of why you feel stuck. The word portable is what the "
       "CLOSE does not use; the idea of experience travelling is still in "
       "V5, in A SIMPLE EXAMPLE and WHEN TO BUILD OPTIONS."),

     "NEW_V8_FS_11_A_FACTUAL_RECORD": (
       "NEW_V8_FS_11_A_FACTUAL_RECORD",
       lambda c: L.compare(
           c, "why people wait", "",
           ("not", "The company's property.", []),
           ("this", "A lawful record of your own work.", []), divider=""),
       "'An award nomination every month.' replaced. The contrast is "
       "recast on THE IMPORTANT BOUNDARY, which reads: the goal is not to "
       "keep the company's files, the goal is to keep a lawful record of "
       "your own work. No award or nomination appears in the reconciled "
       "V8."),
    }


def apply(SETS, L):
    """Swap the affected draw functions in, and report what was changed."""
    table = build(L)
    done = []
    for n, fams in SETS.items():
        for f in fams:
            if f["key"] in table:
                state_name, draw, why = table[f["key"]]
                for st in f["states"]:
                    if st["name"] == state_name:
                        st["draw"] = draw
                        done.append((n, f["key"], why))
    return done
