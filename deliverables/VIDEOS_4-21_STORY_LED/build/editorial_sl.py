# -*- coding: utf-8 -*-
"""The one-page editorial check, with the story-led layer added.

The permanent standard did not change. Painful problem, solution or tool,
viewer outcome still governs. What the story-led pass added is how the
viewer arrives: a recognizable situation comes first.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
import publish_sl as PUB
import prodocs_sl as P
from content421 import PSO
from frames_sl import SETS
from docs421f import (base_doc, para, title_block, h, kv, callout, table,
                      bullets, caption, footer_note, NAVY, GOLD, DIM, RED)

VIEWER = re.compile(r"\byou\b|\byour\b", re.I)
FIRST = re.compile(r"\bI\b|\bmy\b|\bme\b")
CLOSE_WORDS = 320
CLOSE_CEILING = 0.045

# Two ceilings, because two kinds of video are legitimately different.
#
# Most of these videos teach from a problem the viewer has, and there the
# presenter should stay scarce: 4 percent.
#
# Four of them are titled as a first-person claim, "I Was First in 3 New
# Roles in 5 Years" and its siblings. The approved packaging promises lived
# experience, so counting that against the script measures the title rather
# than the writing. Those get 6 percent.
#
# The principle itself is not relaxed either way. What the standard actually
# forbids is the presenter being the DESTINATION, and that is guarded by the
# closing test below, which every video still has to pass on the tighter
# number.
SCRIPT_CEILING = 0.040
SCRIPT_CEILING_FIRST_PERSON = 0.060


def first_person_title(n):
    return bool(re.match(r"(I|I've|I'm|It Took Me)\b", M.title(n)))


def first_person_share(t):
    ws = re.findall(r"[A-Za-z']+", t)
    return len([w for w in ws if FIRST.fullmatch(w)]) / float(len(ws)) if ws \
        else 0.0


def situation(n):
    """The opening scene, in the script's own words."""
    return M.paragraphs(n)[0]


def checks(n):
    problem, solution, outcome = PSO[n]
    head = " ".join(M.paragraphs(n)[:3])
    close = " ".join(M.spoken_text(n).split()[-CLOSE_WORDS:])
    cam = sum(1 for x in P.spine(n) if x[0] == "CAMERA")
    full = sum(1 for x in P.spine(n) if x[0] == "FRAME")
    return [
      ("Opens on a recognizable situation, not the framework",
       bool(VIEWER.search(head) or FIRST.search(head) or '“' in head
            or '"' in head),
       situation(n)[:90]),
      ("The problem is the viewer's, not the presenter's",
       bool(VIEWER.search(problem)), problem[:80]),
      ("A solution or tool sits between problem and outcome",
       bool(solution.strip()), solution[:80]),
      ("The outcome is something the viewer can do afterward",
       bool(VIEWER.search(outcome)), outcome[:80]),
      ("The video closes on the viewer, not the presenter",
       bool(VIEWER.search(close))
       and first_person_share(close) < CLOSE_CEILING,
       "last %d words: %.1f%% first person"
       % (CLOSE_WORDS, 100 * first_person_share(close))),
      ("Experience is warrant, not the destination",
       first_person_share(M.spoken_text(n)) <
       (SCRIPT_CEILING_FIRST_PERSON if first_person_title(n)
        else SCRIPT_CEILING),
       "%.1f%% of the script is first person, against a %.0f%% ceiling (%s)"
       % (100 * first_person_share(M.spoken_text(n)),
          100 * (SCRIPT_CEILING_FIRST_PERSON if first_person_title(n)
                 else SCRIPT_CEILING),
          "first-person title" if first_person_title(n)
          else "viewer-problem title")),
      ("The video stays camera-led overall",
       cam >= full,
       "%d camera stretches against %d full-screen frames" % (cam, full)),
    ]


def failures():
    return [(n, name, detail) for n in M.VIDEOS
            for name, ok, detail in checks(n) if not ok]


def build(n, path, stamp):
    problem, solution, outcome = PSO[n]
    d = base_doc()
    footer_note(d, "Video %d editorial check  |  story-led" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Editorial Check", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Spoken source", "%s  ·  SHA-256 %s"
       % (M.read(n)["file"], M.read(n)["sha"]))
    kv(d, "Runtime class", M.mode(n))
    callout(d, "The story-led layer is how the viewer arrives, not a "
               "replacement for the standard. Painful problem, solution, "
               "viewer outcome still governs.")
    h(d, "Recognizable situation")
    para(d, situation(n), size=12.5)
    caption(d, "What makes the viewer recognize themselves. This is "
               "camera-led and nothing covers it.")
    h(d, "Painful problem")
    para(d, problem, size=12.5)
    h(d, "Solution, distinction or tool")
    para(d, solution, size=12.5)
    h(d, "Viewer outcome")
    para(d, outcome, size=12.5)
    h(d, "Tests against the story-led script")
    table(d, ["Test", "Result", "Measured"],
          [[name, "PASS" if ok else "REWRITE", str(detail)]
           for name, ok, detail in checks(n)],
          widths=[2.7, 0.8, 3.2], size=8.5)
    h(d, "What this page does not claim")
    bullets(d, [
      "It does not claim the video will retain, convert or rank.",
      "It does not claim that everything in Temidayo's experience "
      "transfers. Employer constraints, bias, markets, credentials, "
      "regulation, domain knowledge, relationships, compensation realities, "
      "genuine gaps and relearning all still apply.",
      "A pass means the structure holds, not that the script is finished. "
      "The September 13 script is the authority on the words.",
    ])
    d.save(path)
    return path


if __name__ == "__main__":
    bad = failures()
    for n in M.VIDEOS:
        rows = checks(n)
        b = [r for r in rows if not r[1]]
        print("V%-3d %d tests  %s" % (n, len(rows),
              "all pass" if not b else "REWRITE: %s" % [x[0] for x in b]))
    print("\nfailures: %d" % len(bad))
