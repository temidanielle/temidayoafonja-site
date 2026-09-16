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
    ck("V%d BEAST MODE body preserved" % n, all(p in now for p in base),
       "%d paragraphs" % len(base))
    ck("V%d only the approved intro added" % n,
       [p for p in now if p not in base]
       == [R.S._norm(p) for p in R.intro_paragraphs(n)], "")
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
ck("No sidecar is inside the archive it describes",
   not [x for x in z.namelist() if x.endswith(".sha256")], "")

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
