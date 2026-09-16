# -*- coding: utf-8 -*-
"""Final verification of the synchronized set, read back off disk."""
import os, sys, json, re, glob, hashlib, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")
sys.path.insert(0, DELIV + "V4-V11_EDIT_SYNC/build")
import recon as R, shortsync as SH, packages as P, briefs as B
import sequencing as Q, locate as LOC
import src916 as S916
from qa23 import units, _flat
from PIL import Image

Rw = []


def ck(n, ok, d=""):
    Rw.append((n, bool(ok), d))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


EMP = re.compile(r"\b(GiveDirectly|HCSC|Health Care Service|Zeta Global|"
                 r"Patriot Growth|xAI)\b", re.I)

for n in R.VIDEOS:
    pkg = os.path.join(OUT, "PACKAGES", P.PKG[n])
    ck("V%d package exists" % n, os.path.isdir(pkg))
    # source
    ok, det = True, ""
    if n in R.HAS_INTRO:
        ip = R.intro_paragraphs(n)
        cnt = sum(1 for p in R.paragraphs(n) if p in ip)
        ok, det = cnt == len(ip), "%d of %d paragraphs, once each" % (cnt,
                                                                      len(ip))
    else:
        det = "intentionally none"
    ck("V%d approved intro restored exactly once" % n, ok, det)
    base = [R.S._norm(p) for p in S916.paragraphs(n)]
    now = [R.S._norm(p) for p in R.paragraphs(n)]
    old4 = R.S._norm(R.V4_OPENING[0])
    new4 = R.S._norm(R.V4_OPENING[1])
    kept = [p for p in base if not (n == 4 and p == old4)]
    ck("V%d BEAST MODE body preserved" % n, all(p in now for p in kept),
       "%d paragraphs" % len(kept))
    want = [R.S._norm(p) for p in R.intro_paragraphs(n)]
    if n == 4:
        want = [new4] + want
    ck("V%d only the approved intro and opening added" % n,
       sorted([p for p in now if p not in base]) == sorted(want), "")
    if n == 4:
        ck("V4 opening is the approved hypothetical",
           new4 in now and old4 not in now, "word for word")
    ck("V%d thought-block stream matches exactly and in order" % n,
       [R.S._norm(x) for x in R.paragraphs(n)]
       == [R.S._norm(x) for lab, ps in P.blocks(n) for x in ps],
       "%d paragraphs" % len(R.paragraphs(n)))
    # assets
    vis = os.path.join(pkg, "04_VISUAL_ASSETS")
    png = sorted(x for x in os.listdir(vis) if x.endswith(".png"))
    ck("V%d every mapped state exists" % n,
       all(s + ".png" in png for c in P.cues(n) for s in c["states"]),
       "%d states" % sum(len(c["states"]) for c in P.cues(n)))
    ck("V%d all long-form assets 1920x1080" % n,
       all(Image.open(os.path.join(vis, x)).size == (1920, 1080)
           for x in png if "Contact_Sheet" not in x), "%d png" % len(png))
    ck("V%d phone-size contact sheet present" % n,
       os.path.exists(os.path.join(vis, "Phone_Size_Contact_Sheet.png")))
    ck("V%d every cue resolves to one location" % n,
       all(c["section"] is not None for c in P.cues(n)),
       "%d families" % len(P.cues(n)))
    ck("V%d all brief triggers resolve" % n, not B.verify(n), "")
    ck("V%d every trigger resolves by section and purpose" % n,
       all(LOC.resolve(n, x["trigger"], x["head"])
           for x in B.read(n)["beats"] if x["trigger"]),
       "numbered against the reconciled script")
    ck("V%d no paragraph carries two cards without a sequence" % n,
       not [k for k in Q.shared(n) if not Q.SUBRANGE.get((n, k[0], k[1]))],
       "%d sequenced paragraphs" % len(Q.shared(n)))
    ck("V%d Watch Next owns the closing passage alone" % n,
       not [c for c in P.cues(n)
            if c["key"] != "NEW_V%d_WATCH_NEXT" % n
            and [w for w in P.cues(n)
                 if w["key"] == "NEW_V%d_WATCH_NEXT" % n
                 and (w["section"], w["para"]) == (c["section"],
                                                   c["para"])]], "")
    ck("V%d every early cutaway has a rendered state" % n,
       all(not e["asset"] or all(x + ".png" in png for x in e["states"])
           for e in Q.EARLY.get(n, [])),
       "%d opening steps" % len(Q.EARLY.get(n, [])))
    ck("V%d early entry and exit words are in their paragraphs" % n,
       not [b_ for b_ in Q.verify() if b_.startswith("V%d early" % n)], "")
    ck("V%d teaching states counted apart from the contact sheet" % n,
       sum(len(c["states"]) for c in P.cues(n))
       == len([x for x in png if "Contact_Sheet" not in x]),
       "%d states, %d contact sheet"
       % (len([x for x in png if "Contact_Sheet" not in x]),
          len([x for x in png if "Contact_Sheet" in x])))
    ck("V%d Shorts carry complete lists, referents and one action" % n,
       not SH.audit(n), SH.audit(n) or "%d editorial rules"
       % (len(SH.LISTS) + len(SH.ANTECEDENTS)))
    # shorts
    ck("V%d exactly three Shorts" % n, len(SH.rows(n)) == 3)
    ck("V%d every Short line verbatim" % n, not SH.verify(n), "")
    # publishing
    us = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                us.extend(units(os.path.join(root, nm)))
    body = _flat(" ".join(us))
    ck("V%d title matches the locked map" % n,
       _flat(P.LOCKED[n][0]) in body, P.LOCKED[n][0])
    ck("V%d thumbnail matches the locked map" % n,
       _flat(P.LOCKED[n][1]) in body, P.LOCKED[n][1])
    if n == 10:
        ck("V10 uses the longer approved thumbnail",
           "SPEND YOUR FIRST 90 DAYS" in body
           and "PROVE YOURSELF YET" not in body, P.LOCKED[10][1])
    ck("V%d description present with faith anchor" % n,
       "A faith anchor" in body and "New Living Translation" in body, "")
    want = P.RESOURCE[n]
    urls = set(re.findall(r"https://temidayoafonja\.com/[a-z0-9\-]+", body))
    if want is None:
        ck("V4 carries no resource block", not urls, "none, intentionally")
    else:
        ck("V%d carries its one approved resource" % n,
           _flat(want) in body and len(urls) == 1,
           "%s, %d URL" % (want, len(urls)))
    # anonymity: public-facing parts only
    pub = []
    for sub in ("01_RECORDING", "02_RUN_OF_SHOW", "03_RIVERSIDE",
                "04_VISUAL_ASSETS", "05_SHORTS", "06_PUBLISHING"):
        d_ = os.path.join(pkg, sub)
        for root, _, names in os.walk(d_):
            for nm in sorted(names):
                if nm.endswith((".docx", ".txt")):
                    pub.extend(units(os.path.join(root, nm)))
    hits = sorted({m.group(0) for u in pub for m in EMP.finditer(u)})
    ck("V%d no employer name in any public-facing document" % n,
       not hits, hits or "clean")
    ck("V%d no visual is described as proposed rather than delivered" % n,
       not [u for u in us if P._proposed(u)],
       "every named visual is a rendered state")
    if n == 4:
        ck("V4 no document still carries the old opening",
           not [u for u in us
                if "three hours" in u or "30 seconds" in u],
           "master, blocks, maps, Shorts, publishing and QA checked")
    if n == 5:
        ck("V5 portability passage is intact in the master",
           "harder to replace there without becoming much easier to hire"
           in _flat(R.spoken_text(5))
           and "what parts of your experience travel"
           in _flat(R.spoken_text(5)),
           "A SIMPLE EXAMPLE and WHEN TO BUILD OPTIONS")
        ck("V5 no record claims that passage is gone",
           not [u for u in us
                if "no portability" in u.lower()
                or "portability language remains" in u.lower()
                and "previously" not in u.lower()],
           "the rationale is corrected wherever it appeared")

# private provenance separated
pv = os.path.join(OUT, "PACKAGES", P.PKG[6], "07_EVIDENCE", "PRIVATE",
                  "V6_Internal_Posting_Register_DO_NOT_PUBLISH.docx")
ck("V6 named provenance preserved, and separated", os.path.exists(pv)
   and any(EMP.search(u) for u in units(pv)), "07_EVIDENCE/PRIVATE")

for p, want, name in P.HIST:
    ck("%s archive unchanged" % name,
       os.path.exists(p) and sha256(p) == want, want[:20])

arc = os.path.join(OUT, P.ARCHIVE)
z = zipfile.ZipFile(arc)
ck("Combined archive present", os.path.exists(arc),
   "%d entries" % len(z.namelist()))
ck("Outer checksum sidecar matches",
   open(arc + ".sha256").read().split()[0] == sha256(arc), sha256(arc))
ck("Checksum sidecar outside its own archive",
   os.path.basename(arc) + ".sha256" not in z.namelist())
# Sidecars sit beside the archives they describe, never inside them, so
# each one is checked on disk against the archive it names.
side = sorted(glob.glob(os.path.join(OUT, "*.zip.sha256")))
ck("A checksum sidecar exists for every archive",
   len(side) == len(R.VIDEOS) + 1, "%d sidecars" % len(side))
ck("Every sidecar matches the archive it names",
   all(open(x).read().split()[0] == sha256(x[:-7]) for x in side),
   "%d checked on disk" % len(side))
inner = [x for x in z.namelist() if x.endswith(".zip")]
ck("Combined archive carries the eight package archives",
   len(inner) == len(R.VIDEOS), "%d packages" % len(inner))
ck("The eight package sidecars travel in the outer delivery",
   len([x for x in z.namelist() if x.endswith(".zip.sha256")])
   == len(R.VIDEOS),
   "%d beside their archives"
   % len([x for x in z.namelist() if x.endswith(".zip.sha256")]))
ck("No sidecar is inside the archive it describes",
   not [x for y in inner
        for x in zipfile.ZipFile(os.path.join(OUT, y)).namelist()
        if x.endswith(".sha256")]
   and os.path.basename(arc) + ".sha256" not in z.namelist(), "")
ck("Every cue map, sound map and asset index agrees on placement",
   not Q.verify(), Q.verify() or "compared as delivered outputs, not "
                                 "assumed from a shared table")
ck("No report claims the maps cannot disagree",
   not [1 for n in R.VIDEOS
        for root, _, names in os.walk(os.path.join(OUT, "PACKAGES",
                                                   P.PKG[n]))
        for nm in names if nm.endswith((".docx", ".txt"))
        for u in units(os.path.join(root, nm))
        if "cannot disagree" in u.lower()], "")

bad = [r for r in Rw if not r[1]]
for nm, o, d in Rw:
    if not o:
        print("FAIL  %s  ->  %s" % (nm, d))
print("\nfinal verification: %d of %d passed" % (len(Rw) - len(bad),
                                                 len(Rw)))
print("outer archive sha256 %s" % sha256(arc))
print("\n%-5s %9s %9s %8s %8s %7s" % ("", "words", "blocks", "families",
                                      "states", "shorts"))
for n in R.VIDEOS:
    vis = os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS")
    png = [x for x in os.listdir(vis)
           if x.endswith(".png") and "Contact_Sheet" not in x]
    print("V%-4d %9s %9d %8d %8d %7d"
          % (n, format(R.word_count(n), ","), len(P.blocks(n)),
             len(P.cues(n)), len(png), len(SH.rows(n))))
