# -*- coding: utf-8 -*-
"""Final verification of the corrected sprint set, read off disk."""
import os, sys, glob, hashlib, zipfile, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
import sprint as S, sqa as QA, geocheck as G, reuse as RU
from qa23 import units, _flat, BRITISH, EM_DASH

R = []


def ck(name, ok, detail=""):
    R.append((name, bool(ok), detail))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def pkg_dir(n):
    return glob.glob(os.path.join(
        OUT, "NEW_V%d_*_Sprint_Production_Package" % n))[0]


# ------------------------------------------------- the five corrections
changed = []
for n in S.VIDEOS:
    pre, now = S.pre_paragraphs(n), S.paragraphs(n)
    ck("NEW V%d paragraph count unchanged" % n, len(pre) == len(now),
       "%d" % len(now))
    d = [(a, b) for a, b in zip(pre, now) if a != b]
    changed += [(n, a, b) for a, b in d]
# Five source-language corrections on September 13, plus one public
# employer anonymization in NEW V6 on September 14.
ck("Exactly six spoken sentences changed, all authorized", len(changed) == 6,
   "%d changed" % len(changed))
for n in (4, 5, 7):
    ck("NEW V%d spoken script unchanged" % n,
       not [x for x in changed if x[0] == n], "identical to the supplied "
                                              "source")
for n in (6, 8, 9):
    want = len(S.CORRECTIONS[n])
    got = len([x for x in changed if x[0] == n])
    ck("NEW V%d corrected" % n, got == want, "%d of %d" % (got, want))
for n, old, new in changed:
    ck("NEW V%d replacement is verbatim as authorized" % n,
       any(_flat(o) == _flat(old) and _flat(nw) == _flat(new)
           for o, nw in S.CORRECTIONS[n]), new[:60])

# ------------------------------------------- thought blocks, exact match
for n in S.VIDEOS:
    ok, det = S.blocks_match(n)
    ck("NEW V%d Thought-Block matches its script exactly" % n, ok, det)

# ------------------------------------------------------ nothing else moved
for n in S.VIDEOS:
    ck("NEW V%d title unchanged" % n,
       S.title(n) == S.TITLES_AT_ACCEPTANCE[n], S.title(n))
    ck("NEW V%d thumbnail unchanged" % n,
       S.thumbnail(n) == S.THUMBNAILS_AT_ACCEPTANCE[n], S.thumbnail(n))
    ck("NEW V%d former roadmap mapping unchanged" % n,
       S.NUMBERS[n] == S.NUMBERS_AT_ACCEPTANCE[n], "V%d" % S.NUMBERS[n])
    ck("NEW V%d still has three Shorts" % n, len(S.shorts(n)) == 3, "three")
ck("Publishing order unchanged", S.VIDEOS == (4, 5, 6, 7, 8, 9),
   "V4 V5 V6 V7 V8 V9")

# ------------------------------------------- no Short carried a sentence
for n in S.VIDEOS:
    bad = []
    for sh in S.shorts(n):
        blob = _flat(sh["hook"] + " " + sh["body"]).lower()
        for m in S.CORRECTIONS.get(n, ()):
            for t in m:
                if _flat(t).lower() in blob:
                    bad.append(sh["num"])
    ck("NEW V%d Shorts untouched by the correction" % n, not bad,
       bad or "no Short contains a corrected sentence")

# --------------------------------------------------- packages and archives
results, rr, ar = {}, RU.check(6), RU.anonymized(6)
for n in S.VIDEOS:
    pkg = pkg_dir(n)
    geo = G.check(n)[0]
    assets = sorted(glob.glob(os.path.join(pkg, "04_VISUAL_ASSETS", "*.png")))
    results[n] = QA.run(n, pkg, geo, assets, rr if n == 6 else None,
                        ar if n == 6 else None)
    bad = [x for x in results[n] if not x[1]]
    ck("NEW V%d package checks all pass" % n, not bad,
       "%d checks" % len(results[n]))
    ck("NEW V%d geometry clean against the rendered DOM" % n, not geo,
       "%d problems" % len(geo))
    us = QA.all_units(pkg)
    ck("NEW V%d U.S. English" % n, not QA._british(n, us),
       QA._british(n, us) or "clean")
    ck("NEW V%d no em dashes" % n, not QA._emdash(n, us),
       QA._emdash(n, us) or "clean")
    ck("NEW V%d no chapter timings" % n, not QA._chapter_lists(pkg), "none")
    ck("NEW V%d no unsupported audience-behavior phrasing" % n,
       not (QA.language(S.spoken_text(n)) + QA.language(QA.authored_copy(n))),
       "clean")

# ------------------------------------------- only the corrected rebuilt
def git_sha(rel):
    try:
        b = subprocess.check_output(["git", "show", "HEAD:" + rel],
                                    cwd="/home/user/temidayoafonja-site",
                                    stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return None
    return hashlib.sha256(b).hexdigest()


for n in S.VIDEOS:
    zp = glob.glob(os.path.join(
        OUT, "NEW_V%d_*_Sprint_Production_Package.zip" % n))[0]
    ck("NEW V%d archive matches its sidecar" % n,
       open(zp + ".sha256").read().split()[0] == sha256(zp), "")

# ------------------------------------------ public employer anonymization
import audit_public as AP
import descsrc as DS
ck("No employer name is drawn on any public card, any video",
   not [h for n in S.VIDEOS for h in AP.scan(n)], "all six audited off the "
                                                  "drawn card")
ck("No employer name in any spoken stream",
   not [1 for n in S.VIDEOS if AP.RX.search(S.spoken_text(n))], "clean")
ck("No employer name in any Short",
   not [1 for n in S.VIDEOS for sh in S.shorts(n)
        if AP.RX.search(sh["hook"] + sh["body"] + sh["ask"])], "clean")
ck("NEW V6 carries exactly two authorized replacements",
   len(S.CORRECTIONS[6]) == 2, "one correction, one anonymization")
ck("NEW V6 spoken word count", S.word_count(6) == 1010, "1,010")
ck("NEW V6 stays under the ten-minute promise",
   S.word_count(6) / 130.0 < 10, "%.1f minutes at the slow end"
   % (S.word_count(6) / 130.0))

# --------------------------------------------------- approved descriptions
ck("Approved description package verified", DS.sha256() == DS.SHA, DS.SHA[:24])
for n in S.VIDEOS:
    pkg = pkg_dir(n)
    us = QA.all_units(pkg)
    ok, det = QA._description(n, us)
    ck("NEW V%d description is the approved copy, verbatim" % n, ok, det)
    ok, det = QA._resource(n, us)
    ck("NEW V%d resource assignment correct" % n, ok, det)

# ------------------------------------------------------------- the locks
ck("Historical V4 to V21 archive untouched",
   sha256(QA.HISTORICAL) == QA.HISTORICAL_SHA, QA.HISTORICAL_SHA[:24])
v23 = ("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/"
       "YouTube_V22-V23_FINAL_Production_Packages_2026-09-13_v3.zip")
ck("Locked V22/V23 archive untouched",
   sha256(v23) == open(v23 + ".sha256").read().split()[0], "")

# ---------------------------------------------------- the outer archive
arc = os.path.join(OUT, "YouTube_NEW_PUBLIC_V4-V9_TWO_WEEK_SPRINT_FINAL_"
                        "Production_Packages_2026-09-13.zip")
z = zipfile.ZipFile(arc)
names = z.namelist()
ck("Outer archive has 15 entries", len(names) == 15, "%d" % len(names))
ck("Outer checksum sidecar matches",
   open(arc + ".sha256").read().split()[0] == sha256(arc), sha256(arc))
ck("Checksum is never inside its own archive",
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
print("\nfinal spoken word counts")
for n in S.VIDEOS:
    w = S.word_count(n)
    print("  NEW V%d  %4d words   %d:%02d to %d:%02d"
          % (n, w, w / 145.0 * 60 // 60, w / 145.0 * 60 % 60,
             w / 130.0 * 60 // 60, w / 130.0 * 60 % 60))
tot = sum(len(r) for r in results.values())
ok = sum(1 for r in results.values() for _, o, _ in r if o)
print("\npackage checks: %d run, %d passed, %d failed" % (tot, ok, tot - ok))
print("outer archive sha256 %s" % sha256(arc))
