# -*- coding: utf-8 -*-
"""The viewer exercise, re-anchored to the new scripts."""
import masters23b as M
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, table,
                    bullets, footer_note)

STEPS = {
 22: [("Problem", "What can this organization not do right now?"),
      ("Authority", "Does the person govern, decide, negotiate, recommend, "
                    "influence, support, or execute?"),
      ("Proof", "What evidence would make this employer believe you can do "
                "the work?"),
      ("Real gap", "What requirement is specific enough to matter in this "
                   "employer's world?")],
 23: [("Problem before", "What was true before you stepped in?"),
      ("What was mine to decide", "What was genuinely yours?"),
      ("Judgment", "What was not obvious?"),
      ("Proof and how I know", "What changed, and how do you know?")],
}
OPEN = {
 22: "Take one job description you are actually considering. Do not start "
     "with the title.",
 23: "Pick one accomplishment you remember clearly. Not your best one. Just "
     "one.",
}
EXTRA = {
 22: ["A real gap is not just something you have not done before. It is a "
      "requirement specific enough to matter in this employer's world.",
      "Some constraints are not skill gaps at all. An overlap requirement is "
      "an operating constraint."],
 23: ["Execution still contains decisions. What did you sequence, escalate, "
      "challenge, or recommend?",
      "Two sentences is usually enough for any one line."],
}
CLOSE = {
 22: "This will not tell you who will get hired, whether the authority "
     "described on paper exists in practice, whether a manager would flex, "
     "or whether bias will shape the decision. Reading better does not "
     "guarantee a better outcome. It gives you a cleaner read on what may "
     "travel, what may not, what you can prove, and what you would still "
     "need to learn.",
 23: "Good proof does not make your role sound bigger than it was. It makes "
     "what you actually carried easier to judge. And where an employer still "
     "requires domain knowledge, a credential, regulated experience or "
     "direct exposure, that stays true. Change the emphasis, not the truth.",
}
LAST = {22: "Then find the strongest verb in the posting.",
        23: "The second line usually takes the longest. That is the point."}


def build(n, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Viewer exercise")
    kv(d, "Generated", stamp)
    para(d, OPEN[n], size=12)
    h(d, "Four lines")
    table(d, ["", "Question", "Your answer"],
          [[a, b, ""] for a, b in STEPS[n]],
          widths=[1.5, 2.7, 2.5], size=9.5)
    para(d, LAST[n], size=11, before=10)
    h(d, "Before you stop")
    bullets(d, EXTRA[n])
    callout(d, CLOSE[n])
    footer_note(d, "One exercise, done once, is worth more than the whole "
                   "framework read twice.")
    d.save(path)
    return path
