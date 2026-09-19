# -*- coding: utf-8 -*-
"""Regression fixtures for the reporting defects the review named.

Each delivered claim is replayed as text and must be caught, and each
corrected record must read the way the review asked. A check that cannot
be shown to fire is not a check.
"""
import os, re, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                   "V4-V11_EDIT_SYNC/build")
OUT = os.path.dirname(HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_22-23/build")
import recon as R
import packages as P
import events as EV
from qa23 import units, _flat

STALE = re.compile(r"no portability|portability language remains|"
                   r"cannot disagree|proposed instructions|"
                   r"30 seconds|those three hours|"
                   r"take someone three hours", re.I)
CORRECTED = re.compile(r"previously|old wording|claimed|was wrong|"
                       r"is corrected|no longer|superseded|re-pointed",
                       re.I)


def caught(text):
    return bool(STALE.search(text)) and not CORRECTED.search(text)


# The exact sentences the delivered archive carried.
DELIVERED_CLAIMS = [
 ("V5 changelog",
  "The reconciled V5 carries no portability or internal-system passage. "
  "That idea now lives in V9, not here."),
 ("V5 asset ledger", "No portability language remains in the reconciled "
                     "V5."),
 ("Riverside prompts", "New visuals are proposed instructions here, not "
                       "delivered slide files."),
 ("QA headline", "The maps cannot disagree because every one of them is "
                 "generated from a single table."),
 ("V4 evidence note", "The spoken opening states that AI can do in 30 "
                      "seconds what used to take someone three hours."),
]

# Sentences that name a superseded claim in order to correct it.
LEGITIMATE = [
 ("changelog finding",
  "The V5 changelog rationale claimed no portability passage remains in "
  "V5. The script carries two."),
 ("decisions record",
  "Two quoted the old wording and were re-pointed: the opening beat and "
  "S1's anchor, which contained those three hours."),
]


def main():
    fail = 0
    print("DELIVERED CLAIMS, REPLAYED\n")
    for where, text in DELIVERED_CLAIMS:
        ok = caught(text)
        print("  %-20s %s" % (where, "FIRES" if ok else "HELD  <-- missed"))
        fail += 0 if ok else 1

    print("\nCORRECTIONS THAT MUST NOT BE FLAGGED\n")
    for where, text in LEGITIMATE:
        ok = not caught(text)
        print("  %-20s %s" % (where, "allowed" if ok else
                              "FLAGGED  <-- too blunt"))
        fail += 0 if ok else 1

    print("\nTHE DELIVERED FILES NOW\n")
    docs = []
    for n in R.VIDEOS:
        pkg = os.path.join(OUT, "PACKAGES", P.PKG[n])
        for root, _, names in os.walk(pkg):
            for nm in sorted(names):
                if nm.endswith((".docx", ".txt")):
                    docs.append(os.path.join(root, nm))
    for nm in sorted(os.listdir(os.path.join(OUT, "SHARED"))):
        if nm.endswith(".docx"):
            docs.append(os.path.join(OUT, "SHARED", nm))
    bad = [(os.path.basename(f), u[:64]) for f in docs
           for u in units(f) if caught(u)]
    print("  %d documents scanned, %d superseded claims found"
          % (len(docs), len(bad)))
    for f, u in bad[:10]:
        print("     %s: %s" % (f, u))
    fail += len(bad)

    v5 = _flat(R.spoken_text(5))
    for phrase in ("harder to replace there without becoming much easier "
                   "to hire somewhere else",
                   "what parts of your experience travel"):
        ok = _flat(phrase) in v5
        print("  V5 still carries: %-52s %s" % (phrase[:52],
                                                "yes" if ok else "NO"))
        fail += 0 if ok else 1

    print("\nCOUNTS AND SIDECARS\n")
    tot = 0
    for n in R.VIDEOS:
        vis = os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS")
        png = [x for x in os.listdir(vis) if x.endswith(".png")]
        st = [x for x in png if "Contact_Sheet" not in x]
        sh = [x for x in png if "Contact_Sheet" in x]
        tot += len(st)
        # States come from the event list: one family can serve more
        # than one event, so a per-family sum misses the states that
        # belong to the second occurrence.
        ok = (len({x["name"] for e in EV.events(n)
                   for x in e["states"]}) == len(st)
              and len(sh) == 1)
        print("  V%-3d %3d states + %d contact sheet   %s"
              % (n, len(st), len(sh), "ok" if ok else "MISMATCH"))
        fail += 0 if ok else 1
    print("  %d teaching and end-card states in total" % tot)

    arc = os.path.join(OUT, P.ARCHIVE)
    z = zipfile.ZipFile(arc)
    side = [x for x in z.namelist() if x.endswith(".zip.sha256")]
    inner = [x for x in z.namelist() if x.endswith(".zip")]
    nested = [x for y in inner
              for x in zipfile.ZipFile(os.path.join(OUT, y)).namelist()
              if x.endswith(".sha256")]
    for name, ok in (("eight package sidecars in the outer delivery",
                      len(side) == len(R.VIDEOS)),
                     ("no sidecar inside the archive it describes",
                      not nested and os.path.basename(arc) + ".sha256"
                      not in z.namelist())):
        print("  %-48s %s" % (name, "ok" if ok else "FAIL"))
        fail += 0 if ok else 1

    print("\nfindings not caught: %d" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
