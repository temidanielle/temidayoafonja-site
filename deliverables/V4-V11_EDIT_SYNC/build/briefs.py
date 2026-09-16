# -*- coding: utf-8 -*-
"""The eight Early-Curiosity / Outcome editing briefs, parsed.

The brief is production direction only. It supplies exact spoken triggers,
editorial display copy, five sound accents, four camera-emphasis beats and
the viewer outcome. It never supplies spoken wording, and nothing here is
copied into a script.

Every "Exact spoken trigger" is checked against the current September 16
script rather than trusted, because a trigger that no longer exists in the
script cannot cue anything.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src916 as S

TRIG = re.compile(r"^Exact spoken trigger:\s*(.+)$")
DISP = re.compile(r"^Display copy:\s*(.+)$")
NUM = re.compile(r"^(\d+)\.\s+(.+)$")
WATCH = re.compile(r"^Exact Watch Next:\s*(.+)$", re.S)
FIELDS = ("OUTCOME", "CURIOSITY", "WHY THIS METHOD", "OBSERVABLE TAKEAWAY")


def _strip_quotes(t):
    t = t.strip()
    for a, b in (("“", "”"), ('"', '"')):
        if t.startswith(a) and t.rstrip(".").endswith(b):
            t = t.rstrip(".").strip()
        if t.startswith(a):
            t = t[1:]
        if t.endswith(b):
            t = t[:-1]
    return t.strip()


def read(n):
    out = dict(video=n, outcome={}, beats=[], camera=[], sound=[],
               watch_next=None, boundary=None)
    section = None
    cur = None
    for kind, v in S.brief(n):
        if kind != "p":
            continue
        t = v.strip()
        for f in FIELDS:
            if t.startswith(f + ":"):
                out["outcome"][f] = t.split(":", 1)[1].strip()
        if t in ("Opening treatment | first spoken beats",
                 "Make the teaching usable", "Sound plan",
                 "Camera emphasis | four proposed beats",
                 "Public boundary to preserve",
                 "Final sequence and one primary ask"):
            section = t
            continue
        if t.startswith("• "):
            if section and section.startswith("Camera emphasis"):
                out["camera"].append(t[2:].strip())
            continue
        m = NUM.match(t)
        if m and section in ("Opening treatment | first spoken beats",
                             "Make the teaching usable"):
            cur = dict(n=int(m.group(1)), head=m.group(2).strip(),
                       phase=("opening" if section.startswith("Opening")
                              else "teaching"),
                       trigger=None, display=None, note=[])
            out["beats"].append(cur)
            continue
        m = TRIG.match(t)
        if m and cur is not None:
            cur["trigger"] = _strip_quotes(m.group(1))
            continue
        m = DISP.match(t)
        if m and cur is not None:
            cur["display"] = m.group(1).strip()
            continue
        if t.startswith("TRUE FULL-SCREEN") or t.startswith("CAMERA, THEN"):
            if cur is not None and not cur["display"]:
                cur["display"] = t
            continue
        m = WATCH.match(t)
        if m:
            out["watch_next"] = _strip_quotes(m.group(1))
            continue
        if section == "Public boundary to preserve" and not out["boundary"]:
            out["boundary"] = t
        if cur is not None and section in (
                "Opening treatment | first spoken beats",
                "Make the teaching usable"):
            cur["note"].append(t)
    return out


def verify(n):
    """Every exact trigger must still exist in the current script."""
    b = read(n)
    body = S._norm(S.spoken_text(n)).lower()
    bad = []
    for x in b["beats"]:
        if not x["trigger"]:
            bad.append((x["n"], "no trigger parsed", ""))
            continue
        if S._norm(x["trigger"]).lower() not in body:
            bad.append((x["n"], "trigger not in script", x["trigger"][:66]))
    return bad


def occurrences(n, trigger):
    """Which spoken paragraphs contain this trigger, by section."""
    q = S._norm(trigger).lower()
    hits = []
    for li, (lab, ps) in enumerate(S.sections(n)):
        for pi, p in enumerate(ps):
            if q in S._norm(p).lower():
                hits.append((li, lab, pi, p))
    return hits


if __name__ == "__main__":
    total_bad = 0
    for n in S.VIDEOS:
        b = read(n)
        bad = verify(n)
        total_bad += len(bad)
        amb = [x for x in b["beats"] if x["trigger"]
               and len(occurrences(n, x["trigger"])) > 1]
        print("V%-2d  %d beats (%d opening, %d teaching)  %d camera beats  "
              "%s"
              % (n, len(b["beats"]),
                 sum(1 for x in b["beats"] if x["phase"] == "opening"),
                 sum(1 for x in b["beats"] if x["phase"] == "teaching"),
                 len(b["camera"]),
                 "all triggers verified" if not bad else "%d PROBLEM" % len(bad)))
        for x in bad:
            print("       beat %s: %s  %s" % x)
        for x in amb:
            print("       beat %d: trigger appears %d times, section plus "
                  "parent passage resolves it"
                  % (x["n"], len(occurrences(n, x["trigger"]))))
    print("\ntotal trigger problems: %d" % total_bad)
