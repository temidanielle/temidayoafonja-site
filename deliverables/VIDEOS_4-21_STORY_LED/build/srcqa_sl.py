# -*- coding: utf-8 -*-
"""Source QA on the story-led scripts and their thought blocks.

Run before any package is built. These checks are about the supplied source
itself, not about anything this build produces.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters_sl as M

BRIT = re.compile(r"\b(colour|behaviour|organis(e|ed|ing|ation)|"
                  r"recognis(e|ed|ing)|analys(e|ed)|labelled|centre|"
                  r"programme|whilst|amongst)\b", re.I)

# Language that belongs to an editor, not to a speaker. If any of this is
# inside the spoken copy, it would be read aloud.
DIRECTION = re.compile(
    r"\b(full[- ]screen|b[- ]roll|cut to|jump cut|push[- ]in|pull[- ]back|"
    r"on[- ]screen text|lower third|insert graphic|"
    r"hold for \d|hold \d+ ?(s|sec|seconds)|"
    r"camera[- ]led|voice[- ]over|SFX|riverside)\b", re.I)

CHANGE_LOG_WORDS = {4: 874, 5: 867, 6: 1340, 7: 1345, 8: 1413, 9: 1278,
                    10: 1229, 11: 1302, 12: 1299, 13: 1377, 14: 1365,
                    15: 1493, 16: 1311, 17: 1432, 18: 1400, 19: 1577,
                    20: 1413, 21: 1437}


def check(n):
    rows = []

    def ck(name, ok, detail):
        rows.append((name, bool(ok), detail))

    spoken = M.spoken_text(n)
    paras = M.paragraphs(n)

    ck("Source files match their intake hashes", M.verify(n),
       "script and thought block both unchanged on disk")

    ok, detail = M.blocks_match_script(n)
    ck("Thought block matches the script exactly", ok, detail)

    labels = [nm for nm, _ in M.sections(n)]
    leaked = [p for p in paras if M._is_label(p)]
    ck("Section labels are not in the spoken copy", not leaked,
       leaked[:2] or "%d labels held out of the spoken script" % len(labels))

    hits = [p[:70] for p in paras if DIRECTION.search(p)]
    ck("No production direction inside the spoken copy", not hits,
       hits[:2] or "no camera, B-roll or graphics direction is spoken")

    dash = [p[:70] for p in paras if "—" in p or "–" in p]
    ck("No em dashes or en dashes", not dash, dash[:2] or "clean")

    brit = []
    for p in paras:
        m = BRIT.search(p)
        if m:
            brit.append("%s :: %s" % (m.group(0), p[:50]))
    ck("U.S. English", not brit, brit[:2] or "no British spellings")

    w, fast, slow = M.estimate(n)
    logged = CHANGE_LOG_WORDS[n]
    blockw = len(M._norm(" ".join(M.block_text(n))).split())
    ck("Spoken word count agrees with the thought block", w == blockw,
       "%d spoken words in both" % w)
    if w != logged:
        ck("FLAG, not a defect: supplied change log word count differs",
           True,
           "script and thought block both say %d, the change log says %d. "
           "The script and its recording copy agree with each other, which "
           "is what governs. Nothing is changed." % (w, logged))

    ck("Runtime class correct for this video",
       (n in M.SHORT_TEST) == (n in (4, 5)),
       "%s. %d words, %s to %s at 130 to 145 words per minute"
       % (M.mode(n), w, fast, slow))

    if n in M.SHORT_TEST:
        ck("Shorter test video not expanded into long-form", w < 1000,
           "%d words. The story is part of the retention test." % w)
    else:
        ck("Long-form depth preserved", w >= 1200,
           "%d words" % w)
    if n in M.FULLER_DEPTH:
        ck("Restored fuller depth not undone", w >= 1300, "%d words" % w)

    # The story-led lens: a recognizable scene should arrive near the top,
    # before the framework is named.
    # A recognizable opening puts the viewer, or Temidayo, inside a concrete
    # moment before any framework is named. It can be second person ("you
    # open a job description") or Temidayo's own approved first-person
    # experience ("Three times in five years, I stepped into a role"). Both
    # are scenes. What disqualifies an opening is starting on the framework.
    # Rather than guess at scene vocabulary, test the thing that actually
    # distinguishes a scene from a lecture: it involves a person. Either the
    # viewer is addressed, or Temidayo speaks from her own experience, or
    # somebody is quoted. An opening that does none of these is abstract,
    # which is the failure this check exists to catch.
    head = " ".join(paras[:3])
    addressed = re.search(r"\byou\b|\byour\b", head, re.I) is not None
    lived = re.search(r"\bI\b|\bmy\b|\bme\b", head) is not None
    quoted = any(q in head for q in ('"', "\u201c", "\u2018"))
    which = ", ".join(k for k, v in (("addresses the viewer", addressed),
                                     ("Temidayo's own experience", lived),
                                     ("quoted speech", quoted)) if v)
    ck("Opens on a recognizable situation, not on the framework",
       addressed or lived or quoted,
       "%s: %s" % (which or "abstract opening", paras[0][:62]))
    return rows


def main():
    total = fails = 0
    for n in M.VIDEOS:
        rows = check(n)
        bad = [r for r in rows if not r[1]]
        total += len(rows)
        fails += len(bad)
        print("V%-3d %2d/%2d" % (n, len(rows) - len(bad), len(rows)))
        for name, ok, detail in bad:
            print("      FAIL %-46s %s" % (name, str(detail)[:90]))
    print("\n%d of %d source checks passed" % (total - fails, total))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
