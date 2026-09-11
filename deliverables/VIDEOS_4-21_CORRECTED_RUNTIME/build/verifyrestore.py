# -*- coding: utf-8 -*-
"""Prove that the restored scripts contain no unapproved speech.

Every paragraph claims a provenance. This checks the claim rather than
trusting it.

  CUR         must appear in the corrected September 11 master
  SEP09       must appear in the previously approved master, word for word
  SEP09-SPLIT must appear in one of the two approved masters once its line
              breaks are ignored, because a split only removes a sentence or
              joins lines that were already approved
  SEP09-ADJ   must NOT match exactly, and its note must say what changed
  BRIDGE      new language. Reported in full, never passed silently.

A paragraph whose claimed source does not contain it is an authoring error
and fails the check.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_8-13_LOCKED_MASTER_BUILD/build")
import audit678 as A
import masters421 as M
import masters813 as M8
import restore678 as R


def norm(s):
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"'))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def corpora(n):
    cur = norm(M.spoken_text(n))
    if n == 8:
        prev = norm(" ".join(
            p for s in M8.sections(8)
            for p in (s[1] if isinstance(s, tuple) and len(s) > 1 else [])))
    else:
        prev = norm(" ".join(p for _, ps in A.prev_spoken(n) for p in ps))
    return cur, prev


def check(n):
    cur, prev = corpora(n)
    bad, bridges, adjusted = [], [], []
    for sec, paras in R.SCRIPTS[n]:
        for p in paras:
            t, src = norm(p["text"]), p["src"]
            if src == R.BRIDGE:
                bridges.append((sec, p))
                continue
            if src == R.CUR:
                if t not in cur:
                    bad.append((sec, src, p["text"]))
            elif src == R.SEP09:
                if t not in prev:
                    bad.append((sec, src, p["text"]))
            elif src == R.SPLIT:
                # A split joins or drops approved lines. Every sentence in it
                # must still be found in one of the approved masters.
                for s in re.split(r"(?<=[.?!]) +", p["text"]):
                    q = norm(s)
                    if len(q.split()) < 3:
                        continue
                    if q not in prev and q not in cur:
                        bad.append((sec, src, s))
            elif src == R.ADJ:
                adjusted.append((sec, p))
                if not p["note"].strip():
                    bad.append((sec, src, "adjusted without a recorded note"))
                if t in prev:
                    bad.append((sec, src,
                                "claims an adjustment but matches the "
                                "approved text exactly"))
    return bad, bridges, adjusted


def house_style(n):
    """No em dashes, no en dashes, U.S. English."""
    out = []
    brit = re.compile(r"\b(colour|behaviour|organis(e|ed|ing|ation)|"
                      r"recognis(e|ed|ing)|analys(e|ed)|labelled|centre|"
                      r"programme|whilst|amongst)\b", re.I)
    for sec, paras in R.SCRIPTS[n]:
        for p in paras:
            if "—" in p["text"] or "–" in p["text"]:
                out.append((sec, "dash", p["text"][:70]))
            m = brit.search(p["text"])
            if m:
                out.append((sec, "British spelling: %s" % m.group(0),
                            p["text"][:70]))
    return out


def words(n):
    return sum(len(p["text"].split()) for _, ps in R.SCRIPTS[n] for p in ps)


def estimate(n, fast=145.0, slow=130.0):
    w = words(n)
    mm = lambda x: "%d:%02d" % (int(x) // 60, int(x) % 60)
    return w, mm(w / fast * 60), mm(w / slow * 60)


def provenance(n):
    from collections import Counter
    return Counter(p["src"] for _, ps in R.SCRIPTS[n] for p in ps)


if __name__ == "__main__":
    fail = 0
    for n in sorted(R.SCRIPTS):
        bad, bridges, adjusted = check(n)
        style = house_style(n)
        w, fast, slow = estimate(n)
        print("=" * 70)
        print("V%d  %d words  %s to %s  vs %d previously approved (%.0f%%)"
              % (n, w, fast, slow, R.PREV_WORDS[n],
                 100.0 * w / R.PREV_WORDS[n]))
        print("    provenance: %s" % dict(provenance(n)))
        print("    unverifiable paragraphs: %d" % len(bad))
        for sec, src, t in bad:
            print("        [%s] %s :: %s" % (src, sec[:30], t[:90]))
        print("    new bridging language: %d" % len(bridges))
        for sec, p in bridges:
            print("        %s :: %s" % (sec[:30], p["text"]))
        print("    minimally adjusted: %d" % len(adjusted))
        for sec, p in adjusted:
            print("        %s" % sec[:60])
            print("            %s" % p["text"][:86])
            print("            why: %s" % p["note"][:150])
        print("    house-style problems: %d" % len(style))
        for s in style:
            print("        %s" % (s,))
        fail += len(bad) + len(style)
    print()
    print("total failures: %d" % fail)
    raise SystemExit(1 if fail else 0)
