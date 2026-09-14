# -*- coding: utf-8 -*-
"""The Riverside / Co-Creator master prompt for each sprint video."""
import sprint as S
import frames as F
import spine as SP
from sdocs import mono, hr, head, _wrap

PER_VIDEO = {
 4: ("Do not frame this video as AI equals threat, job loss, or bad. The "
     "teaching question is what developmental work changes and what "
     "replaces it. Use AI imagery only where it is substantive; this video "
     "needs none. No glowing robots, no futuristic stock."),
 5: ("Do not imply that being needed is inherently bad, and do not imply "
     "the organization owes an automatic promotion. The tension is whether "
     "dependence is increasing while portable growth is not."),
 6: ("The ten-minute promise must stay real. Do not add spoken material, do "
     "not expand the script, do not add editor narration, and do not add a "
     "second spoken CTA. The sprint script is the only spoken source. Cards "
     "carried over from the former V22 package are reused only where the "
     "sprint script still teaches the same thing."),
 7: ("Temidayo's experience is warrant, not destination. Do not turn this "
     "into why she succeeded. The viewer remains the subject, and bias, "
     "politics, sponsorship, access, timing, manager behavior and "
     "organizational constraint stay visible."),
 8: ("Never depict taking a file, a screenshot, a download, or any "
     "circumvention of access control. No fake internal system appears "
     "anywhere. Keep the proof, not the property, is the rule the visuals "
     "protect."),
 9: ("This is not an anti-transferability video. The four-part audit is the "
     "centre and all four questions appear together before any one is "
     "emphasized. Do not overweight NOT EVERYTHING TRAVELS to the point "
     "that the nuance disappears."),
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
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  RIVERSIDE CO-CREATOR MASTER "
             "PROMPT" % (n, S.NUMBERS[n]))
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
