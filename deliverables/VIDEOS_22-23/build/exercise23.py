# -*- coding: utf-8 -*-
"""The viewer exercise. Included only where it is genuinely useful.

Both videos end on an action the viewer is asked to take, so each exercise is
that action laid out to be done once, using the video's own four questions
and nothing added.
"""
import masters23 as M
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, table,
                    bullets, footer_note, caption)

STEPS = {
 22: [("Problem", "What can this organization not do right now?"),
      ("Authority", "What do the verbs say this person may govern, decide, "
                    "negotiate, recommend, influence, support, or execute?"),
      ("Proof", "What evidence would make the employer believe you can do "
                "this work?"),
      ("Real gap", "What requirement is mandatory, specific, and tied to "
                   "their world rather than yours?")],
 23: [("Problem before", "What was true before you touched it?"),
      ("What was mine to decide", "What was actually yours, and what was "
                                  "not?"),
      ("Judgment", "What was not obvious?"),
      ("Proof and how I know", "What changed, and how does anyone know it "
                               "changed?")],
}

CLOSE = {
 22: "This will not tell you who gets hired, and it will not tell you "
     "whether the authority on paper exists in practice. It gives you a "
     "cleaner read on what travels, what does not, what you can prove, and "
     "what you would have to relearn.",
 23: "Good proof does not make your role sound bigger than it was. It makes "
     "what you actually carried easier to judge. And sometimes there is a "
     "real gap you still have to learn, earn, or experience. Better proof "
     "does not erase that.",
}

OPEN = {
 22: "Take one job description you are actually considering. Not a role you "
     "are curious about. One you would apply to.",
 23: "Pick one thing you did. Not your best thing. Just one you remember "
     "clearly.",
}


def build(n, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Viewer exercise")
    kv(d, "Generated", stamp)
    para(d, OPEN[n], size=12)
    h(d, "Four questions")
    table(d, ["", "Question", "Your answer"],
          [[a, b, ""] for a, b in STEPS[n]],
          widths=[1.4, 2.8, 2.5], size=9.5)
    h(d, "Before you stop")
    bullets(d, [
      "If a line is vague, the missing piece is usually context, judgment, "
      "credit, or evidence." if n == 23 else
      "If you cannot find the verb, you have not found the authority yet.",
      "Two sentences is often enough for any one line."
      if n == 23 else
      "A gap is not always a credential. It may be geography, a time zone, "
      "or a stated gate that has nothing to do with your skill.",
    ])
    callout(d, CLOSE[n])
    footer_note(d, "One exercise, done once, is worth more than the whole "
                   "framework read twice.")
    d.save(path)
    return path
