# -*- coding: utf-8 -*-
"""Six candidate Shorts per video. A selection bank, not six uploads.

Current cadence is about three Shorts per long-form video, so these are
candidates to choose from. Every spoken line is drawn from the approved
script of its source video, in the script's own words, and every evidence
boundary travels with the line that needs it.
"""
import masters23 as M

P22 = M.paragraphs(22)
P23 = M.paragraphs(23)

# (key, hook label, [spoken lines], one ask, boundary carried, card note)
SHORTS = {
 22: [
  ("v22_s1_what_do_you_think_it_pays", "Stop scroll: the title",
   [P22[0], P22[1], P22[3], P22[4], P22[5]],
   "Read the verb before you trust the title.",
   "One posting, captured September 12, 2026. Not a claim about all "
   "employers.",
   "Open on the title card alone. Reveal the floor, then the requirement "
   "line. No generalization on screen."),

  ("v22_s2_read_the_verb", "Stop scroll: four authority-sounding words",
   [P22[22], P22[18], P22[19], P22[23]],
   "Take one job description and find the verb.",
   "One posting. The verb describes the authority posture in that document.",
   "Artifact card with the verb active. Rule one card to close."),

  ("v22_s3_predefined_decisions", "Stop scroll: a quarter-million-dollar role",
   [P22[26], P22[28], P22[29], P22[30], P22[31], P22[32]],
   "Read the verb before you assume the level.",
   "The posting establishes predefined decisions. It does not establish who "
   "created them, and the Short must not say or imply that it does.",
   "The defense of the role stays in. Execution under pressure is hard, and "
   "nothing on screen mocks the job."),

  ("v22_s4_director_did_not_tell_you_enough", "Stop scroll: same title word",
   [P22[34], P22[35], P22[36], P22[41], P22[42], P22[43]],
   "Read the rest of the posting, not the title.",
   "The compensation difference applies to these two jobs at these two "
   "employers. It is not a rule about Directors.",
   "The boundary card must follow the money reveal immediately, inside the "
   "Short. Do not cut the Short before it."),

  ("v22_s5_least_informative_title", "Stop scroll: the title that says nothing",
   [P22[45], P22[46], P22[53], P22[54], P22[55]],
   "A title that tells you very little is a reason to read.",
   "Highest published ceiling in this sample of fifteen postings. Never the "
   "market.",
   "The words IN THIS SAMPLE stay on screen with the figure, in the same "
   "card, for as long as the figure is visible."),

  ("v22_s6_gap_is_not_a_credential", "Stop scroll: the gap nobody mentions",
   [P22[56], P22[57], P22[59], P22[60]],
   "When a posting tells you what will not transfer, believe it.",
   "One posting out of fifteen was that direct. The 7 or 8 a.m. figure is "
   "for someone on Central Time and must carry that qualifier.",
   "GiveDirectly is named, in the past tense, as the script says it."),
 ],
 23: [
  ("v23_s1_the_sentence_does_not", "Stop scroll: a good resume sentence",
   [P23[0], P23[1], P23[2], P23[3], P23[4]],
   "Write what you decided, not just what moved.",
   "Synthetic example. The label travels with the 18 percent figure.",
   "Claim card, then the questions one at a time. SYNTHETIC EXAMPLE is on "
   "screen whenever 18 percent is."),

  ("v23_s2_what_was_mine_to_decide", "Stop scroll: the question we get wrong",
   [P23[16], P23[17], P23[18], P23[19]],
   "Ask what was mine to decide.",
   "The authority verbs are as the fifteen postings separated them. No claim "
   "about what employers generally want.",
   "Authority verbs card. Nothing on screen suggests formal authority is the "
   "valuable kind."),

  ("v23_s3_execution_contains_choices", "Stop scroll: I was just executing",
   [P23[20], P23[21], P23[22], P23[23]],
   "Name one choice that was yours.",
   "No synthetic figures appear, so no figure label is needed.",
   "The three questions card. The Short must not imply that execution means "
   "no judgment."),

  ("v23_s4_nine_of_fifteen", "Stop scroll: what the postings actually asked",
   [P23[31], P23[32], P23[33], P23[34]],
   "Give the result and the mechanism.",
   "Nine of fifteen. Not most employers, not the market.",
   "The denominator card. 9 OF 15 stays on screen with the claim."),

  ("v23_s5_good_proof", "Stop scroll: the part people get backwards",
   [P23[39], P23[40], P23[41]],
   "Be precise about what you carried.",
   "No figures on screen.",
   "The payoff card. This is the editorial centre of the video and the "
   "strongest Short candidate."),

  ("v23_s6_different_door", "Stop scroll: same sentence, different door",
   [P23[42], P23[43], P23[44], P23[45], P23[46], P23[49]],
   "Reconstruct once, then decide what to emphasize.",
   "The employer stays anonymous. No name, no logo, no URL, no identifying "
   "styling.",
   "Anonymized comparison card, then the statement. The closing line about "
   "a real gap stays in."),
 ],
}

WPM = 165


def rows(n):
    out = []
    for key, hook, lines, ask, boundary, note in SHORTS[n]:
        words = sum(len(l.split()) for l in lines) + len(ask.split())
        secs = int(round(words / float(WPM) * 60))
        out.append(dict(key=key, hook=hook, lines=lines, ask=ask,
                        boundary=boundary, note=note, words=words,
                        secs=secs))
    return out


def verify(n):
    """Every spoken line must be a whole paragraph of the source script."""
    bad = []
    for r in rows(n):
        for l in r["lines"]:
            if not M.trigger_ok(n, l):
                bad.append((r["key"], l[:52]))
    return bad


if __name__ == "__main__":
    for n in M.VIDEOS:
        print("V%d" % n)
        for r in rows(n):
            print("   %-42s %3d words  ~0:%02d" % (r["key"], r["words"],
                                                   r["secs"]))
        print("   lines not found in the script:", verify(n) or "none")
