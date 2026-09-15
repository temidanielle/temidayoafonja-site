# -*- coding: utf-8 -*-
"""Final verification of NEW V10 and V11, read back off disk."""
import os, sys, glob, hashlib, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
import v1011 as S, qa1011 as QA, geo1011 as G, spine1011 as SP
import frames1011 as F, shorts1011 as SH, publish1011 as PUB
from qa23 import _flat

R = []


def ck(name, ok, detail=""):
    R.append((name, bool(ok), detail))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


PKG = {10: "NEW_V10_First_90_Days_Production_Package",
       11: "NEW_V11_New_Job_Isnt_The_Job_Production_Package"}
ARCHIVE = ("YouTube_NEW_PUBLIC_V10-V11_FINAL_Production_Packages_"
           "2026-09-14.zip")

# ------------------------------------------------------------ the sources
ck("Handoff archive verified",
   sha256(os.path.join(OUT, "_source", "handoff.zip")) == S.HANDOFF_SHA,
   S.HANDOFF_SHA[:24])
for nm, want in sorted(S.FILE_SHA.items()):
    ck("Source verified: %s" % nm[:52],
       sha256(os.path.join(S.SRC, nm)) == want, "")

# ------------------------------------------------------------- the scripts
for n in S.VIDEOS:
    ok, det = S.blocks_match(n)
    ck("NEW V%d Thought-Block matches exactly and in order" % n, ok, det)
    ck("NEW V%d spoken word count matches the handoff" % n,
       S.word_count(n) == S.STATED_WORDS[n],
       "%s words" % format(S.word_count(n), ","))
    ck("NEW V%d no spoken wording added" % n, not QA._added_spoken(n),
       "every spoken paragraph traces to the FINAL script")
    ck("NEW V%d title exact" % n, S.title(n), S.title(n))
    ck("NEW V%d thumbnail exact" % n, S.thumbnail(n), S.thumbnail(n))
    ck("NEW V%d framework intact and in order" % n, QA._framework_order(n),
       " / ".join(QA.FRAMEWORK[n]))
    ck("NEW V%d no product named in the spoken script" % n,
       not QA._spoken_product(n), "the resource lives in the description")
    ck("NEW V%d exactly three Shorts" % n, len(SH.rows(n)) == 3, "three")
    ck("NEW V%d every Short line verbatim" % n, not SH.verify(n),
       "checked sentence by sentence")

# ------------------------------------------------------- packages on disk
results = {}
for n in S.VIDEOS:
    pkg = os.path.join(OUT, PKG[n])
    geo = G.check(n)[0]
    assets = sorted(glob.glob(os.path.join(pkg, "04_VISUAL_ASSETS", "*.png")))
    results[n] = QA.run(n, pkg, geo, assets)
    bad = [x for x in results[n] if not x[1]]
    ck("NEW V%d package checks all pass" % n, not bad,
       "%d checks" % len(results[n]))
    ck("NEW V%d geometry clean against the rendered DOM" % n, not geo,
       "%d problems" % len(geo))
    ck("NEW V%d teaching copy readable on its ground" % n,
       not QA.contrast(n), "measured, not assumed")
    ck("NEW V%d no former-roadmap number invented" % n,
       not QA._roadmap_claims(pkg), "both videos are new concepts")
    cam, full = SP.counts(n)
    ck("NEW V%d camera-led" % n, cam >= full,
       "%d camera stretches against %d cues" % (cam, full))

# ---------------------------------------------------------------- the locks
LOCKS = [
 (DELIV + "VIDEOS_4-21_STORY_LED/Videos_4-21_STORY_LED_FINAL_Production_"
          "Packages.zip",
  "da7c383d99aec2863d5d39afdfe290caaf5e658ef65cac0a2fa259b8be24d9e1",
  "Historical V4 to V21"),
 (DELIV + "VIDEOS_22-23/YouTube_V22-V23_FINAL_Production_Packages_"
          "2026-09-13_v3.zip",
  "1e88f4b86e1f6bb0db226aec28820d3121a8fe51f20c67b9a6a3e0d7b210efd4",
  "Locked V22 and V23"),
 (DELIV + "SPRINT_V4-V9/YouTube_NEW_PUBLIC_V4-V9_TWO_WEEK_SPRINT_FINAL_"
          "Production_Packages_2026-09-13.zip",
  "8009644b6a4e4aabb542bb99af39687b67003003f17866bc8512812dbbff810e",
  "Locked sprint V4 to V9"),
]
for p, want, name in LOCKS:
    ck("%s archive untouched" % name, sha256(p) == want, want[:24])

# ------------------------------------------------------- the outer archive
arc = os.path.join(OUT, ARCHIVE)
z = zipfile.ZipFile(arc)
names = z.namelist()
ck("Outer archive has 7 entries", len(names) == 7, "%d" % len(names))
ck("Outer checksum sidecar matches",
   open(arc + ".sha256").read().split()[0] == sha256(arc), sha256(arc))
ck("Checksum never inside its own archive",
   os.path.basename(arc) + ".sha256" not in names, "")
inner = [x for x in names if x.endswith(".zip")]
ck("Every nested package checksum validates",
   all(z.read(x + ".sha256").decode().split()[0]
       == hashlib.sha256(z.read(x)).hexdigest() for x in inner),
   "%d packages" % len(inner))

bad = [r for r in R if not r[1]]
for nm, ok, det in R:
    if not ok:
        print("FAIL  %s  ->  %s" % (nm, det))
print("\nfinal verification: %d of %d passed" % (len(R) - len(bad), len(R)))
tot = sum(len(r) for r in results.values())
ok = sum(1 for r in results.values() for _, o, _ in r if o)
print("package checks: %d run, %d passed, %d failed" % (tot, ok, tot - ok))
print("outer archive sha256 %s" % sha256(arc))
for n in S.VIDEOS:
    cam, full = SP.counts(n)
    lo, hi = S.estimate(n)
    print("  NEW V%d  %s words  %s to %s  %d cam / %d full  %d states"
          % (n, format(S.word_count(n), ","), lo, hi, cam, full,
             len(F.states(n))))
