# -*- coding: utf-8 -*-
"""Every Watch Next card must display the destination video's exact title.

The card copy is written literally in frames421.py so the deck source stays
readable. That means it can drift when a destination master changes its
title, which is exactly what happened between September 10 and September 11.
This check reads the card copy back out of the source and compares it to the
corrected master, so the drift cannot survive a build.

Two classes of finding are reported separately:

  MISMATCH   the card names a title no corrected master carries. A defect.
  TYPOGRAPHY the card matches apart from quote or dash glyphs. Reported,
             never auto-corrected, because the difference originates between
             two approved masters and repairing it here would silently edit
             approved copy.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M

HERE = os.path.dirname(os.path.abspath(__file__))

# V14's ten assets are carried in byte-identical from the September 10 build,
# so its card copy lives in that batch's source and is scanned there.
SRC = (os.path.join(HERE, "frames421.py"),
       os.path.join(os.path.dirname(os.path.dirname(HERE)),
                    "VIDEOS_14-21_FINAL_PRODUCTION", "build",
                    "frames1421.py"))

CARD = re.compile(
    r'F\(key="v(\d+)_10_watch_next",\s*'
    r'draw=lambda c: X\.watch_next\(\s*c,\s*'
    r'((?:"(?:[^"\\]|\\.)*"\s*)+),\s*"Video (\d+)"\)', re.S)

FOLD = {"’": "'", "‘": "'", "“": '"', "”": '"',
        "–": "-", "—": "-"}


def _fold(s):
    for a, b in FOLD.items():
        s = s.replace(a, b)
    return s


def _joined(lit):
    return "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', lit)).replace('\\"', '"')


def cards():
    """[(source video, destination video, title drawn on the card)]

    Read from the rendered card, not from the source text that defines it.
    V14's ten frames are carried in from the September 10 build and one of
    them is overridden after import, so scanning source would report the
    card that was replaced rather than the card that ships.
    """
    import sys as _s
    _s.path.append("/home/user/temidayoafonja-site/deliverables/"
                   "riverside-build")
    import rdeck
    from frames421 import SETS
    out = []
    for n in M.VIDEOS:
        for i, f in enumerate(SETS[n], 1):
            if not f["key"].endswith("_watch_next"):
                continue
            c = rdeck.Card(i, f["key"] + ".png")
            f["draw"](c)
            lines = [p["text"] for el in c.els if el.get("t") == "text"
                     for p in el["paras"] if p.get("text")]
            # The card is: the WATCH NEXT label, the title, the destination.
            dest = [x for x in lines if re.fullmatch(r"Video \d+", x.strip())]
            title = [x for x in lines
                     if x.strip().upper() != "WATCH NEXT" and x not in dest]
            out.append((n, int(dest[0].split()[1]),
                        " ".join(" ".join(title).split())))
    out.sort()
    return out


def check():
    rows, bad, typo = [], [], []
    seen = {n for n, _, _ in cards()}
    for n, dest, shown in cards():
        want = M.title(dest)
        if shown == want:
            verdict = "OK"
        elif _fold(shown) == _fold(want):
            verdict = "TYPOGRAPHY"
            typo.append((n, dest, shown, want))
        else:
            verdict = "MISMATCH"
            bad.append((n, dest, shown, want))
        rows.append((n, dest, verdict, shown, want))
    missing = [n for n in M.VIDEOS if n not in seen]
    return rows, bad, typo, missing


def main():
    rows, bad, typo, missing = check()
    for n, dest, verdict, shown, want in rows:
        print("%-10s V%-2d -> Video %-2d  %s" % (verdict, n, dest, shown))
        if verdict != "OK":
            print("%-10s %s corrected master: %s" % ("", " " * 16, want))
    if missing:
        print("NO CARD PARSED for: %s" % missing)
    print("\n%d cards, %d mismatches, %d typographic variances, %d unparsed"
          % (len(rows), len(bad), len(typo), len(missing)))
    return 1 if (bad or missing) else 0


if __name__ == "__main__":
    raise SystemExit(main())
