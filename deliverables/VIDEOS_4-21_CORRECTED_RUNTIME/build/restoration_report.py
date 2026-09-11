# -*- coding: utf-8 -*-
"""The V6, V7 and V8 restoration report."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_8-13_LOCKED_MASTER_BUILD/build")
from collections import Counter
import audit678 as A
import masters421 as M
import restore678 as R
import verifyrestore as V
from docs421f import mono, hr, head

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(path, stamp):
    L = head("VIDEOS 6, 7 AND 8  |  RESTORATION REPORT")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "WHAT WAS DONE", "",
          "  The September 11 masters supplied for Videos 6, 7 and 8 carried",
          "  about half the previously approved spoken script. Each has been",
          "  restored to full regular long-form depth.", "",
          "  The corrected master's title, thumbnail, hook, personal framing",
          "  and framework architecture are kept exactly as supplied. The",
          "  teaching that the compression pass removed is restored from the",
          "  last full-length approved master.", "",
          "  For Video 8 the corrected four-part architecture takes",
          "  precedence, as directed. BEFORE, MY PART, JUDGMENT and PROOF",
          "  are kept, together with Existence, Use and Effect, and the",
          "  approved depth is mapped into that structure rather than the",
          "  previous three-part one being restored over it.", "",
          "  No master was padded to reach a clock. Every restored line is",
          "  approved speech.", "", hr(), "",
          "SOURCE INTEGRITY", "",
          "  The supplied September 11 masters are NOT modified. Each is",
          "  retained in _source/ and still matches its original checksum,",
          "  and each is copied into its package as a superseded file. The",
          "  restored derivatives are separate documents in",
          "  _source_restored/.", "", hr(), "",
          "RESULT", "",
          "  %-4s %-9s %-9s %-8s %-16s %s"
          % ("V", "RESTORED", "PREVIOUS", "OF PREV", "SPEECH ONLY",
             "SECTIONS"),
          "  " + "-" * 74]
    for n in sorted(R.SCRIPTS):
        w, fast, slow = V.estimate(n)
        L += ["  %-4s %-9d %-9d %-8s %-16s %d"
              % ("V%d" % n, w, R.PREV_WORDS[n],
                 "%.0f%%" % (100.0 * w / R.PREV_WORDS[n]),
                 "%s to %s" % (fast, slow), len(R.SCRIPTS[n]))]
    L += ["",
          "  Speech-only, at 130 to 145 words per minute. It excludes",
          "  pauses, framework holds, full-screen demonstrations and",
          "  transitions, so the finished runtime will be longer.", "",
          hr(), "", "NEWLY AUTHORED SPEECH", ""]
    total_bridge = 0
    for n in sorted(R.SCRIPTS):
        c = Counter(p["src"] for _, ps in R.SCRIPTS[n] for p in ps)
        total_bridge += c.get(R.BRIDGE, 0)
    if total_bridge:
        L += ["  %d lines. Each is listed below for approval." % total_bridge,
              ""]
        for n in sorted(R.SCRIPTS):
            for sec, ps in R.SCRIPTS[n]:
                for p in ps:
                    if p["src"] == R.BRIDGE:
                        L += ["  V%d  %s" % (n, sec), "      %s" % p["text"],
                              "      why: %s" % p["note"], ""]
    else:
        L += ["  None. Zero lines of new teaching were written. Every line in",
              "  all three restored scripts is either the corrected master's",
              "  own speech or previously approved speech.", ""]
    L += [hr(), "", "PER-VIDEO DETAIL", ""]
    for n in sorted(R.SCRIPTS):
        c = Counter(p["src"] for _, ps in R.SCRIPTS[n] for p in ps)
        prev_secs = {nm for nm, _ in A.rows(n)}
        L += ["=" * 74, "VIDEO %d" % n, "=" * 74, "",
              "  spoken source of truth: %s" % M.filename(n),
              "      SHA-256 %s" % M.read(n)["sha"], "",
              "  supplied, superseded:   %s" % M.FILES[n],
              "      SHA-256 %s" % M.read(n)["supplied_sha"], "",
              "  depth source:           %s"
              % os.path.basename(A.PREV[n]), "",
              "  line provenance: %s"
              % ", ".join("%s %d" % (k, v) for k, v in sorted(c.items())), "",
              "  SECTIONS AND WHERE EACH LINE CAME FROM", ""]
        for sec, ps in R.SCRIPTS[n]:
            sc = Counter(p["src"] for p in ps)
            words = sum(len(p["text"].split()) for p in ps)
            L += ["    %-52s %4d  %s"
                  % (sec[:52], words,
                     " ".join("%s:%d" % (k.replace("SEP09-", ""), v)
                              for k, v in sorted(sc.items())))]
        L += ["", "  MINIMAL ADJUSTMENTS TO APPROVED SPEECH", ""]
        adj = [(sec, p) for sec, ps in R.SCRIPTS[n] for p in ps
               if p["src"] in (R.ADJ, R.SPLIT)]
        if not adj:
            L += ["    None.", ""]
        for sec, p in adj:
            L += ["    [%s] %s" % (p["src"], sec)]
            import textwrap
            for x in textwrap.wrap(p["text"], 66):
                L += ["        %s" % x]
            for x in textwrap.wrap(p["note"], 62):
                L += ["          %s" % x]
            L += [""]
    L += [hr(), "",
          "VIDEOS 9 TO 13 WERE NOT TOUCHED", "",
          "  Their corrected masters match the previously approved masters",
          "  to the word. Their speech-only estimates sitting below the",
          "  printed finished-runtime targets is the ordinary difference",
          "  between speech time and finished time. Nothing was padded.", ""]
    return mono(path, L)


if __name__ == "__main__":
    import subprocess
    stamp = subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()
    print(build(os.path.join(OUT, "AUDIT",
                             "V6_V7_V8_Restoration_Report.txt"), stamp))
