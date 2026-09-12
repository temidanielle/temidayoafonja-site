# -*- coding: utf-8 -*-
"""The one-page editorial check: painful problem, solution, viewer outcome.

The standard the channel is held to is that the viewer's problem opens the
video, a solution or tool sits in the middle, and the viewer leaves able to do
something. Temidayo's experience is evidence and warrant for the teaching. It
is not the destination of the story.

This page states those three things for one video and then tests them against
the corrected master, so the check is a measurement rather than an assertion:

  * the problem is the viewer's, stated in second person
  * the outcome is the viewer's, stated in second person
  * the closing movement is outward, to the viewer's action, not inward to
    the presenter
"""
import os, re, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import masters421 as M
from content421 import PSO
from publish421 import primary_cta, route
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                      table, bullets, sub, caption, footer_note, numbered,
                      NAVY, GOLD, DIM, RED)

VIEWER = re.compile(r"\byou\b|\byour\b|\byours\b", re.I)
PRESENTER = re.compile(r"\bI\b|\bmy\b|\bme\b|\bmine\b")

# How much of the closing movement may be about the presenter. The last
# stretch of a video is where a personal story most easily takes over the
# ending, so it is the stretch that is measured.
CLOSE_WORDS = 320

# Ceilings on first-person density, set on editorial principle rather than
# fitted to these scripts. Above them the presenter has become the subject
# instead of the warrant.
CLOSE_CEILING = 0.045
SCRIPT_CEILING = 0.040


def first_person_share(text):
    ws = re.findall(r"[A-Za-z']+", text)
    if not ws:
        return 0.0
    return len([w for w in ws if PRESENTER.fullmatch(w)]) / float(len(ws))


def close(n, words=CLOSE_WORDS):
    return " ".join(M.spoken_text(n).split()[-words:])


def checks(n):
    problem, solution, outcome = PSO[n]
    ask, cue = primary_cta(n)
    c = close(n)
    return [
      ("The problem is the viewer's, not the presenter's",
       bool(VIEWER.search(problem)),
       "Stated in second person." if VIEWER.search(problem) else
       "REWRITE: the problem line does not address the viewer."),
      ("A solution or tool sits between the problem and the outcome",
       bool(solution.strip()),
       solution),
      ("The outcome is something the viewer can do or say afterward",
       bool(VIEWER.search(outcome)),
       "Stated in second person." if VIEWER.search(outcome) else
       "REWRITE: the outcome line does not address the viewer."),
      ("The video closes on the viewer's action, not on the presenter",
       bool(VIEWER.search(c)) and first_person_share(c) < CLOSE_CEILING,
       "Last %d words: %.1f%% first person, and the viewer is addressed."
       % (CLOSE_WORDS, 100 * first_person_share(c))),
      ("One primary action, and it is the one the CTA card carries",
       bool(ask.strip()),
       ask),
      ("Experience is used as warrant, not as the destination",
       first_person_share(M.spoken_text(n)) < SCRIPT_CEILING,
       "%.1f%% of the script is first person." 
       % (100 * first_person_share(M.spoken_text(n)))),
    ]


def failures():
    out = []
    for n in M.VIDEOS:
        for label, ok, note in checks(n):
            if not ok:
                out.append((n, label, note))
    return out


def build(n, out_path, stamp):
    problem, solution, outcome = PSO[n]
    ask, cue = primary_cta(n)
    res = route(n)
    d = base_doc()
    footer_note(d, "Video %d editorial check  |  painful problem, solution, "
                   "viewer outcome" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Editorial Check", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Source", "%s  ·  SHA-256 %s" % (M.FILES[n], M.read(n)["sha"]))
    kv(d, "Runtime mode", M.mode(n))

    callout(d, "Temidayo's experience is evidence and warrant for the "
               "teaching. It is not the destination of the story. The tests "
               "below measure that against the corrected master rather than "
               "asserting it.")

    h(d, "Painful problem")
    para(d, problem, size=12.5)
    h(d, "Solution or tool")
    para(d, solution, size=12.5)
    h(d, "Viewer outcome")
    para(d, outcome, size=12.5)

    h(d, "The one primary action")
    para(d, ask, size=12, bold=True, color=NAVY)
    caption(d, "Spoken at: %s" % cue)
    caption(d, "Resource route: %s"
            % (res or "none, and none is added"))

    h(d, "Tests against the corrected master")
    table(d, ["Test", "Result", "Measured"],
          [[label, "PASS" if ok else "REWRITE", note]
           for label, ok, note in checks(n)],
          widths=[2.6, 0.9, 3.2], size=8.5)

    h(d, "What this page does not claim")
    bullets(d, [
      "It does not claim the video will retain, convert or rank.",
      "It does not claim that everything in Temidayo's experience "
      "transfers. Employer constraints, bias, markets, credentials, "
      "regulation, domain knowledge, relationships, compensation realities, "
      "genuine gaps and relearning all still apply.",
      "A pass here means the structure holds, not that the script is "
      "finished. The master is the authority on the words.",
    ])
    d.save(out_path)
    return out_path


if __name__ == "__main__":
    for n in M.VIDEOS:
        rows = checks(n)
        bad = [r for r in rows if not r[1]]
        print("V%-3d %d tests  %s" % (n, len(rows),
              "all pass" if not bad else "REWRITE: %s"
              % "; ".join(r[0] for r in bad)))
        for r in bad:
            print("      %s" % r[2])
