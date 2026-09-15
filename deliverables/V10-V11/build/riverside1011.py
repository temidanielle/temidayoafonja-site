# -*- coding: utf-8 -*-
"""The Riverside / Co-Creator master prompt for NEW V10 and V11."""
import v1011 as S
import frames1011 as F
import spine1011 as SP
from docs1011 import mono, hr, head, _wrap

PER_VIDEO = {
 10: ("Keep the opening on camera until the pressure to prove yourself has "
      "actually landed. Do not reveal READ / TEST / PROVE before Temidayo "
      "names it. The reversal, THEY ARE NOT THE ONLY ONES EVALUATING, is "
      "the one moment in this video that should feel like the ground "
      "moving: cut to camera, hold a brief pause, let the sound shift "
      "under it, then go full screen. Return to Temidayo for the "
      "interpretation. Do not require a theatrical quick win anywhere in "
      "the edit, and do not let any card imply that every manager "
      "evaluates the same things."),
 11: ("Keep the opening on camera until the mismatch is recognizable. Do "
      "not begin with the framework. The employer and the manager are "
      "never the villain in this edit: no card, no B-roll and no sound "
      "choice may frame the organization as having lied. Bait-and-switch "
      "appears once, in the script, as the reading Temidayo asks the "
      "viewer to slow down, and it is never used as a label. Keep the "
      "legitimate reasons a role changes and the real constraints that "
      "shape what is possible on screen wherever the script puts them."),
}

STANDING = [
 ("Camera-led",
  "Story, recognition, consequence, tension and interpretation stay on "
  "Temidayo. Do not cover a strong human moment with a graphic because an "
  "asset exists. These scripts are short and carry few cues on purpose."),
 ("True full screen",
  "Frameworks, comparisons, meaningful evidence and multi-step teaching take "
  "the whole screen. No presenter moving behind them, no corner placement, "
  "no semi-transparent overlay for substantive teaching."),
 ("One active idea at a time",
  "Establish a structure whole, then activate one component, teach it, and "
  "move on. Never leave several components competing while one is "
  "explained."),
 ("Sequential reveals, not buttons",
  "A numbered point is a reading order. YouTube is not interactive and "
  "nothing should look clickable."),
 ("Restraint",
  "No constant zooming, no pulsing the frame, no accent on every reveal, no "
  "animating every line. Stillness is allowed when the viewer needs to "
  "read."),
 ("Captions",
  "No burned-in captions in the long-form video. Generate the SRT in "
  "Riverside after the final edit and verify it against the final export."),
 ("Watch Next",
  "Full screen and final. There is no return to camera after it. The spoken "
  "line that introduces it is the script's own and was not changed."),
]


def prompt(n, path, stamp):
    cam, full = SP.counts(n)
    L = head("NEW PUBLIC V%d  |  RIVERSIDE CO-CREATOR MASTER PROMPT" % n)
    L += [S.title(n),
          "Thumbnail: %s" % S.thumbnail(n),
          "Generated %s" % stamp, "",
          "%s spoken words. %d camera stretches against %d full-screen cues,"
          % (format(S.word_count(n), ","), cam, full),
          "and %d of the spoken words are delivered on camera."
          % SP.on_camera_words(n),
          "This script carries no timing markers, so nothing in it can be",
          "mistaken for a runtime, a chapter or an SRT time.",
          "", hr(), "", "HOW TO USE THIS", "",
          "  Work down the spine. Where it says CAMERA, stay on Temidayo",
          "  for the whole stretch. Where it says FULL SCREEN, cut to the",
          "  named asset on the exact trigger sentence and follow the",
          "  reveal order. The copy on each card is final; do not retype",
          "  it, and do not add teaching that is not in the script.",
          "", hr(), "", "THIS VIDEO SPECIFICALLY", ""]
    L += ["  %s" % x for x in _wrap(PER_VIDEO[n], 68)]
    L += ["", hr(), "", "STANDING RULES", ""]
    for k, v in STANDING:
        L += ["  %s" % k.upper()]
        L += ["      %s" % x for x in _wrap(v, 68)]
        L.append("")
    L += [hr(), "", "THE SPINE", ""]
    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            seq, lab = rest
            L += ["", hr(), "SECTION %d  %s" % (seq, lab.upper()), hr(), ""]
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
                  "  CLASS:    %s" % f["cls"],
                  "  TRIGGER:  %s" % " ".join(f["trigger"].split()),
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
    wn = [f for f in F.SETS[n] if f["treatment"] == "WATCH NEXT"][0]
    L += ["", hr(), "", "WATCH NEXT  |  FULL SCREEN AND FINAL", "",
          "  ASSET:        %s.png" % wn["key"],
          "  SPOKEN LINE:  %s" % " ".join(S.paragraphs(n)[-1].split()),
          "  DESTINATION:  %s" % S.watch_next(n),
          "  The spoken wording above is the script's own and was not",
          "  changed. Cut to the card on that line and end the video on it.",
          "  Nothing returns to camera afterward.",
          "",
          "  Before upload, confirm the destination is publicly live. If it",
          "  is not, the publishing materials carry an EDITORIAL FALLBACK",
          "  REQUIRED flag for approval. Do not invent a fallback here.",
          "", hr(), "", "AFTER THE EDIT", "",
          "  Generate the SRT in Riverside and verify it against the final",
          "  export. Create chapters from real export timing. Neither exists",
          "  in this package and neither should be invented before the cut.",
          ""]
    return mono(path, L)


def _clip(s, n=64):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n].rstrip() + "..."
