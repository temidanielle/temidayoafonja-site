# -*- coding: utf-8 -*-
"""One video, one primary CTA. A resource may go on screen only if spoken.

Several corrected masters route a resource to the description and the pinned
comment and say in the same row that it is not a second spoken CTA. A
full-screen card carrying that resource's URL would put a second ask in front
of the viewer with no narration behind it, which is the thing the row forbids.

The rule enforced here:

  a CTA card may draw a resource URL only when the corrected spoken script
  actually names that resource.

The script is the test, not the metadata row, because the row can be silent
where the script is explicit and the other way round.
"""
import os, re, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import rdeck
import masters421 as M
from frames421 import SETS

URL = re.compile(r"temidayoafonja\.com/[a-z0-9\-/]+")

# The spoken name of each route, as the scripts say it.
SPOKEN_NAME = {
    "temidayoafonja.com/fieldkit": ("field kit",),
    "temidayoafonja.com/keep-the-proof": ("keep the proof",),
    "temidayoafonja.com/career-decisions": ("career decision evidence check",
                                            "decision evidence check"),
    "temidayoafonja.com/career-evidence-starter": ("career evidence starter",),
}


def drawn(n, i, f):
    c = rdeck.Card(i, f["key"] + ".png")
    f["draw"](c)
    out = []
    for el in c.els:
        if el.get("t") == "text":
            out += [p["text"] for p in el["paras"] if p.get("text")]
    return " ".join(out)


def check():
    bad, rows = [], []
    for n in M.VIDEOS:
        script = M.spoken_text(n).lower()
        for i, f in enumerate(SETS[n], 1):
            text = drawn(n, i, f)
            for u in set(URL.findall(text.lower())):
                names = SPOKEN_NAME.get(u)
                if names is None:
                    bad.append((n, f["key"], u, "unknown route"))
                    rows.append((n, f["key"], u, "UNKNOWN"))
                    continue
                if any(x in script for x in names):
                    rows.append((n, f["key"], u, "SPOKEN"))
                else:
                    bad.append((n, f["key"], u, "never spoken in the script"))
                    rows.append((n, f["key"], u, "SILENT"))
    return rows, bad


def main():
    rows, bad = check()
    for n, key, u, verdict in rows:
        print("%-8s V%-2d %-24s %s" % (verdict, n, key, u))
    print("\n%d on-screen resource URLs, %d unsupported by the spoken script"
          % (len(rows), len(bad)))
    for n, key, u, why in bad:
        print("  DEFECT V%d %s: %s, %s" % (n, key, u, why))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
