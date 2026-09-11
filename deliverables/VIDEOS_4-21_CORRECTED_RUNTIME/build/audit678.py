# -*- coding: utf-8 -*-
"""Source-to-source audit of V6, V7 and V8 against the last full-length
approved masters.

The question is not whether the corrected master says "regular long-form".
It is whether the script in it is the full-depth script. A runtime estimate
cannot answer that on its own, because an estimate derived from a compressed
file will simply report the compression as a fact. So the comparison is made
against the previously approved master itself: its word count, its sections,
and the teaching inside them.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_8-13_LOCKED_MASTER_BUILD/build")
from docx import Document
import masters421 as M
import masters813 as M8

DELIV = "/home/user/temidayoafonja-site/deliverables/"

PREV = {
 6: DELIV + ("VIDEO_6_Before_You_Take_An_Internal_Role_FINAL/"
             "V6_Recording_Master_LOCKED_2026-09-09.docx"),
 7: DELIV + ("VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL/"
             "V7_Recording_Master_LOCKED_2026-09-09.docx"),
 8: DELIV + ("VIDEOS_8-13_LOCKED_MASTER_BUILD/_source/"
             "Video_8_FINAL_Revised_Recording_Master.docx"),
}

# Where the spoken script begins in the September 9 V6 and V7 masters, and the
# headings that end it. Anything outside is production apparatus, not speech.
V67_START = "Recording Script"
V67_END = ("PRODUCTION NOTES", "EDITOR", "VISUAL", "QA", "SHORTS",
           "PUBLISHING", "END OF", "NOTES", "GUARDRAIL", "RESOURCE",
           "THUMBNAIL", "TITLE")

# The September 9 masters close with production apparatus set in title case,
# not in capitals, so an upper-case test walks straight past it and counts a
# visual map and a recording checklist as speech. These lines end the script.
V67_TAIL = ("Major Visual", "Motion-Graphic Map", "Recording Close Checklist",
            "Production Notes", "Editor Notes", "Visual Priorities")


def _is_heading(t):
    letters = [c for c in t if c.isalpha()]
    if not letters:
        return False
    upper = sum(1 for c in letters if c.isupper()) / float(len(letters))
    return upper > 0.85 and len(t) < 120


def prev_spoken(n):
    """(section name, [spoken paragraphs]) for a September 9 V6/V7 master."""
    if n == 8:
        raise ValueError("V8 is read through masters813")
    ps = [x.text.strip() for x in Document(PREV[n]).paragraphs
          if x.text.strip()]
    try:
        i = ps.index(V67_START) + 1
    except ValueError:
        raise SystemExit("V%d: cannot find where the script starts" % n)
    out, cur = [], None
    for t in ps[i:]:
        if any(t.startswith(x) for x in V67_TAIL):
            break
        if _is_heading(t):
            if any(t.upper().startswith(e) for e in V67_END):
                break
            cur = (t, [])
            out.append(cur)
            continue
        if cur is None:
            cur = ("(before the first heading)", [])
            out.append(cur)
        cur[1].append(t)
    return out


def prev_rows(n):
    if n == 8:
        secs = M8.sections(n)
        return [(s[0] if isinstance(s, tuple) else str(s),
                 s[1] if isinstance(s, tuple) and len(s) > 1 else [])
                for s in secs]
    return prev_spoken(n)


def words(paras):
    return sum(len(p.split()) for p in paras)


def prev_word_count(n):
    if n == 8:
        return M8.words(n)
    return sum(words(p) for _, p in prev_spoken(n))


def est(w, fast=145.0, slow=130.0):
    def mmss(x):
        return "%d:%02d" % (int(x) // 60, int(x) % 60)
    return mmss(w / fast * 60), mmss(w / slow * 60)


def rows(n):
    """(section name, spoken word count) for the previous approved master."""
    if n == 8:
        return [(s[0] if isinstance(s, tuple) else str(s),
                 sum(len(x.split()) for x in
                     (s[1] if isinstance(s, tuple) and len(s) > 1 else [])))
                for s in M8.sections(8)]
    return [(name, words(ps)) for name, ps in prev_spoken(n)]


def now_rows(n):
    return [(name, sum(len(x.split()) for x in ps))
            for name, ps in M.sections(n)]


def report(n):
    prev, now = rows(n), now_rows(n)
    pw, nw = sum(w for _, w in prev), M.word_count(n)
    return dict(video=n, prev_words=pw, now_words=nw,
                prev_est="%s to %s" % est(pw),
                now_est="%s to %s" % M.estimate(n)[1:],
                ratio=100.0 * nw / pw, prev_sections=prev, now_sections=now,
                source=os.path.basename(PREV[n]))


def verdict(n):
    r = report(n)
    if r["ratio"] >= 90:
        return "B", ("the corrected master carries the previous master's "
                     "full depth")
    return "C", ("the corrected master carries %.0f%% of the previously "
                 "approved spoken script" % r["ratio"])


def unchanged():
    """Videos whose corrected master matches the previous approved master's
    word count exactly. A parser that can reproduce five prior word counts to
    the word is not the reason another video measures short."""
    out = []
    for n in M8.VIDEOS:
        if n in PREV:
            continue
        out.append((n, M.word_count(n), M8.words(n),
                    M.word_count(n) == M8.words(n)))
    return out


if __name__ == "__main__":
    print("PARSER CONTROL: corrected master vs previous approved master")
    for n, a, b, ok in unchanged():
        print("  V%-3d now %-6d prev %-6d  %s"
              % (n, a, b, "identical" if ok else "DIFFERS"))
    print()
    for n in sorted(PREV):
        r = report(n)
        v, why = verdict(n)
        print("=" * 74)
        print("V%d  CASE %s: %s" % (n, v, why))
        print("  compared against: %s" % r["source"])
        print("  words     now %-6d prev %-6d  (%.0f%%)"
              % (r["now_words"], r["prev_words"], r["ratio"]))
        print("  speech    now %-14s prev %s"
              % (r["now_est"], r["prev_est"]))
        print("  sections  now %-6d prev %d"
              % (len(r["now_sections"]), len(r["prev_sections"])))
        print("  PREVIOUS SECTIONS")
        for name, w in r["prev_sections"]:
            print("      %-56s %4d" % (name[:56], w))
        print("  CURRENT SECTIONS")
        for name, w in r["now_sections"]:
            print("      %-56s %4d" % (name[:56], w))
