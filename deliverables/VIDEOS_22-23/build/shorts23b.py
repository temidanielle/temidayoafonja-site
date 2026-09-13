# -*- coding: utf-8 -*-
"""Six candidate Shorts per video, rebuilt from the new scripts.

A selection bank, not six uploads. Every spoken line is a whole paragraph of
the new approved script of its source video, in the script's own words, and
every evidence boundary travels with the line that needs it. No Short from
the previous package survives whose source wording disappeared.
"""
import masters23b as M

P22 = M.paragraphs(22)
P23 = M.paragraphs(23)

SHORTS = {
 22: [
  ("v22_s1_what_the_person_actually_owns",
   "Stop scroll: what does this person actually own?",
   [P22[0], P22[1], P22[3], P22[4]],
   "Do not start with the title.",
   "One posting, captured September 12, 2026. Not a claim about all "
   "employers.",
   "Open on the title card alone. Reveal the floor, then the requirement "
   "line. No generalization on screen."),

  ("v22_s2_read_the_verbs", "Stop scroll: read the verbs",
   [P22[18], P22[19], P22[21], P22[22], P22[23]],
   "Find the verb before you judge the level.",
   "One posting. The verb tells you where the authority appears to sit in "
   "that document.",
   "Artifact card with the verb active, then the rule card. Nothing claims "
   "the role is unimportant."),

  ("v22_s3_predefined_decisions",
   "Stop scroll: a Director who does not own every decision",
   [P22[25], P22[26], P22[27], P22[28], P22[29]],
   "Ask what this person is actually trusted to decide.",
   "The posting establishes predefined decisions. It does not establish who "
   "created them, and the Short must not say or imply that it does.",
   "The line about a serious role under pressure stays in. Nothing on screen "
   "mocks the job."),

  ("v22_s4_same_word_different_work",
   "Stop scroll: same title, different job",
   [P22[49], P22[52], P22[55], P22[56], P22[57], P22[58]],
   "A title can help you find a posting. It cannot finish the read.",
   "Two postings from two employers. No compensation comparison is drawn: "
   "the script no longer makes one.",
   "The comparison card, then the four-beat distinction. Do not add a money "
   "reveal."),

  ("v22_s5_least_informative_title",
   "Stop scroll: the title that tells you nothing",
   [P22[62], P22[63], P22[64], P22[66], P22[67], P22[69]],
   "Read the work.",
   "Highest published ceiling in the sample of 15 postings. Never the "
   "market.",
   "The words IN THE SAMPLE stay on screen with the figure, in the same "
   "card, for as long as the figure is visible."),

  ("v22_s6_operating_constraint",
   "Stop scroll: the gap that is not a skill gap",
   [P22[43], P22[45], P22[46], P22[47]],
   "Read the constraints, not just the requirements.",
   "One posting in the sample. The posting states the overlap requirement; "
   "no local meeting time is stated or implied.",
   "GiveDirectly is named, in the past tense, as the script says it. No "
   "time-of-day figure appears on screen."),
 ],
 23: [
  ("v23_s1_the_sentence_does_not",
   "Stop scroll: a strong resume sentence",
   [P23[0], P23[1], P23[3], P23[5], P23[6], P23[7]],
   "Write what you decided, not just what moved.",
   "Synthetic example. The label travels with the 18 percent figure.",
   "Claim card, then the questions one at a time. SYNTHETIC EXAMPLE is on "
   "screen whenever 18 percent is."),

  ("v23_s2_what_was_mine_to_decide",
   "Stop scroll: the question we answer wrong",
   [P23[28], P23[29], P23[30], P23[31], P23[32]],
   "Ask what was mine to decide.",
   "No synthetic figure appears, so no figure label is needed.",
   "Camera-led. The harder question lands on screen, nothing else."),

  ("v23_s3_execution_contains_decisions",
   "Stop scroll: I was just executing",
   [P23[33], P23[34], P23[35], P23[37], P23[38]],
   "Name one decision that was genuinely yours.",
   "Several senior roles in the postings described support or execution "
   "postures. Nothing is claimed beyond that.",
   "The five questions card, then the boundary card. The Short must not "
   "imply that execution means no judgment."),

  ("v23_s4_what_was_not_obvious",
   "Stop scroll: what was not obvious?",
   [P23[40], P23[41], P23[43], P23[44], P23[47], P23[48]],
   "Find the call that could have been wrong.",
   "Synthetic example. Label carried because the card describes the "
   "invented scenario.",
   "Let the scene play on camera before the card names the call."),

  ("v23_s5_result_versus_mechanism",
   "Stop scroll: the number is only half of it",
   [P23[51], P23[52], P23[53], P23[54], P23[55]],
   "Give the result and the mechanism.",
   "Synthetic example. 89 percent is visible, so the label is on screen. "
   "The research is stated only as the script states it.",
   "The two-part card. Do not add a denominator the script does not say."),

  ("v23_s6_change_the_emphasis",
   "Stop scroll: do not rewrite history",
   [P23[67], P23[71], P23[72], P23[73], P23[74], P23[75]],
   "Change the emphasis, not the truth.",
   "Domain knowledge, credentials, regulated experience and direct exposure "
   "stay named as real requirements.",
   "The catch card, then the closing statement. No employer comparison "
   "appears: the script no longer makes one."),
 ],
}

WPM = 165


def rows(n):
    out = []
    for key, hook, lines, ask, boundary, note in SHORTS[n]:
        words = sum(len(l.split()) for l in lines) + len(ask.split())
        out.append(dict(key=key, hook=hook, lines=lines, ask=ask,
                        boundary=boundary, note=note, words=words,
                        secs=int(round(words / float(WPM) * 60))))
    return out


def verify(n):
    """Every spoken line must be a whole paragraph of the new source script."""
    return [(r["key"], l[:52]) for r in rows(n) for l in r["lines"]
            if not M.trigger_ok(n, l)]


if __name__ == "__main__":
    for n in M.VIDEOS:
        print("V%d" % n)
        for r in rows(n):
            print("   %-40s %3d words  ~0:%02d" % (r["key"], r["words"],
                                                   r["secs"]))
        print("   lines not found in the new script:", verify(n) or "none")
