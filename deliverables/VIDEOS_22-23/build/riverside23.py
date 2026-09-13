# -*- coding: utf-8 -*-
"""The Riverside / Co-Creator master editing prompt.

Nothing in here says "add a graphic". Every cue carries its exact trigger
sentence, its mode, what the visual is for, its layout, its exact short copy,
its reveal order and emphasis state, how long to hold, whether it takes a
sound accent, its asset filename and its source note.
"""
import masters23 as M
import frames23 as F
import spine23 as SP
from docs23 import mono, hr, head

STANDING = [
 ("Camera-led",
  "Story, recognition, consequence and interpretation stay on Temidayo. Do "
  "not cover a strong human opening with a graphic because an asset exists."),
 ("True full screen",
  "Frameworks, comparisons, substantive examples and meaningful source "
  "evidence take the whole screen. No presenter moving behind them, no "
  "corner placement, no semi-transparent overlay for substantive teaching."),
 ("One active idea at a time",
  "Establish a structure whole, then activate one component, teach it, and "
  "move on. Never leave four components competing while one is explained."),
 ("Sequential reveals, not buttons",
  "A numbered point is a reading order. YouTube is not interactive and "
  "nothing should look clickable."),
 ("Restraint",
  "No constant zooming, no pulsing the frame, no accent on every reveal, no "
  "animating every line. Stillness is allowed when the viewer needs to read."),
 ("Captions",
  "No burned-in captions in the long-form video. Generate the SRT in "
  "Riverside after the final edit and verify it against the final export."),
 ("Watch Next",
  "The Watch Next card is full screen and final. There is no return to "
  "camera after it. The card is silent and no spoken line introduces it."),
]


def prompt(n, path, stamp):
    cam, full = SP.counts(n)
    L = head("VIDEO %d  |  RIVERSIDE CO-CREATOR MASTER EDITING PROMPT" % n)
    L += [M.title(n),
          "Thumbnail: %s" % M.thumbnail(n),
          "Generated %s" % stamp, "",
          "%s spoken words. %d camera stretches against %d full-screen cues."
          % (format(M.word_count(n), ","), cam, full),
          "Runtime is observed at Temidayo's delivery pace. No figure in",
          "this prompt is a measured runtime, a chapter or an SRT time.",
          "", hr(), "", "HOW TO USE THIS", "",
          "  Work down the spine. Where it says CAMERA, stay on Temidayo",
          "  for the whole stretch. Where it says FULL SCREEN, cut to the",
          "  named asset on the exact trigger sentence and follow the",
          "  reveal order. The copy on each card is already final; do not",
          "  retype it, and do not add teaching that is not in the script.",
          "", hr(), "", "STANDING RULES", ""]
    for k, v in STANDING:
        L += ["  %s" % k.upper()]
        L += ["      %s" % line for line in _wrap(v, 68)]
        L.append("")
    L += [hr(), "", "THE SPINE", ""]

    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            mk, label = rest
            L += ["", hr(), "%s  %s" % (mk, label.upper()), hr(), ""]
        elif kind == "CAMERA":
            ps = rest[0]
            L += ["  MODE:  CAMERA",
                  "  Stay on Temidayo for %d paragraph%s, %d words."
                  % (len(ps), "" if len(ps) == 1 else "s",
                     sum(len(p.split()) for p in ps)),
                  "  FROM:  %s" % _clip(ps[0]),
                  "  TO:    %s" % _clip(ps[-1]), ""]
        else:
            f, p = rest
            L += ["  MODE:     FULL SCREEN",
                  "  TRIGGER:  %s" % f["trigger"],
                  "  PURPOSE:"]
            L += ["      %s" % x for x in _wrap(f["purpose"], 68)]
            L += ["  LAYOUT:"]
            L += ["      %s" % x for x in _wrap(f["layout"], 68)]
            L += ["  REVEAL ORDER:"]
            for i, s in enumerate(f["states"], 1):
                L.append("      %d. ASSET: %s.png" % (i, s["name"]))
                L += ["         %s" % x for x in _wrap(s["reveal"], 62)]
            L += ["  EMPHASIS:",
                  "      Active item in the bright warm yellow wash with the",
                  "      rust rule. Everything else quiet. Never two active.",
                  "  HOLD:"]
            L += ["      %s" % x for x in _wrap(f["hold"], 68)]
            L += ["  SOUND:"]
            L += ["      %s" % x for x in _wrap(f["sound"], 68)]
            if f["source"]:
                L += ["  SOURCE NOTE:"]
                L += ["      %s" % x for x in _wrap(f["source"], 68)]
            L.append("")
    L += [hr(), "", "AFTER THE EDIT", "",
          "  Generate the SRT in Riverside and verify it against the final",
          "  export. Create chapters from real export timing. Neither exists",
          "  in this package and neither should be invented before the cut.",
          ""]
    return mono(path, L)


def _wrap(text, width):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if len(t) > width and cur:
            out.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        out.append(cur)
    return out


def _clip(s, n=64):
    return s if len(s) <= n else s[:n].rstrip() + "..."
