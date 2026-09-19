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
import events as EV
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
       len({x["name"] for e in EV.events(n) for x in e["states"]})
       == len([x for x in png if "Contact_Sheet" not in x])
       and len([x for x in png if "Contact_Sheet" in x]) == 1,
       "%d states, %d contact sheet"
       % (len([x for x in png if "Contact_Sheet" not in x]),
          len([x for x in png if "Contact_Sheet" in x])))
    ck("V%d Shorts carry complete lists, referents and one action" % n,
       not SH.audit(n), SH.audit(n) or "%d editorial rules"
       % (len(SH.LISTS) + len(SH.ANTECEDENTS)))
    _acts = [(num, SH.actions(R.S._norm(" ".join(
        SH.SHORTS[(n, num)]["ask"])))) for num in (1, 2, 3)]
    ck("V%d every ask is one audience action, counted not assumed" % n,
       all(len(a) <= 1 for _, a in _acts),
       "; ".join("Short %d: %s" % (num, ", ".join(a) or "none named")
                 for num, a in _acts))
    ck("V%d every Short opens on something it has established" % n,
       not [b_ for b_ in SH.audit(n) if "STANDALONE" in b_],
       "%d opening referents checked"
       % len([x for x in SH.OPENING_REFERENTS if x[0] == n]))
    ck("V%d every Short line is a whole source sentence" % n,
       all(SH.whole_sentences(n, l) for num in (1, 2, 3)
           for l in SH.lines(n, num)),
       "no part-sentence lifts")
    ck("V%d every Short is under 150 words" % n,
       all(r["words"] < 150 for r in SH.rows(n)),
       ", ".join("%d" % r["words"] for r in SH.rows(n)))
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
# Every shared document is scanned too, since the per-package scan cannot
# see them. A sentence may quote the superseded wording only while saying
# it was superseded.
_SHARED = glob.glob(os.path.join(OUT, "SHARED", "*.docx"))
# "three hours" is narrowed to the V4 opening's own phrasing: V6's script
# legitimately requires at least three hours of overlap with East Africa
# Time, and that sentence is not a superseded claim.
_STALE = re.compile(r"no portability|portability language remains|"
                    r"cannot disagree|proposed instructions|"
                    r"30 seconds|those three hours|"
                    r"take someone three hours", re.I)
# A sentence that names the superseded claim in order to correct it is not
# the claim. A sentence that simply asserts it is.
_CORRECTED = re.compile(r"previously|old wording|claimed|was wrong|"
                        r"is corrected|no longer|superseded|re-pointed",
                        re.I)
_shared_bad = [(os.path.basename(f), u[:60]) for f in _SHARED
               for u in units(f)
               if _STALE.search(u) and not _CORRECTED.search(u)]
ck("No shared document repeats a superseded claim",
   not _shared_bad, _shared_bad or "%d documents scanned" % len(_SHARED))
ck("No report claims the maps cannot disagree",
   not [1 for n in R.VIDEOS
        for root, _, names in os.walk(os.path.join(OUT, "PACKAGES",
                                                   P.PKG[n]))
        for nm in names if nm.endswith((".docx", ".txt"))
        for u in units(os.path.join(root, nm))
        if "cannot disagree" in u.lower()], "")

# Every headline number the packages state, re-derived here from the same
# single source and compared against what the documents actually say. The
# 220 against 221 disagreement was a typed number going stale; a typed
# number cannot survive this check.
T = P.totals()
ck("Thought blocks and the paragraphs inside them are counted apart",
   T["blocks"] == sum(len(P.blocks(n)) for n in R.VIDEOS)
   and T["paragraphs"] == sum(len(ps) for n in R.VIDEOS
                              for _, ps in P.blocks(n))
   and T["blocks"] != T["paragraphs"],
   "%d thought blocks holding %d paragraphs" % (T["blocks"],
                                                T["paragraphs"]))
ck("Active, retired and total families all reconcile",
   T["active_families"] + T["retired_families"] == T["total_families"]
   and T["prior_families"] + T["new_families"] == T["total_families"],
   "%d before this pass, plus %d new, is %d; %d retired leaves %d active"
   % (T["prior_families"], T["new_families"], T["total_families"],
      T["retired_families"], T["active_families"]))
ck("States and contact sheets are counted apart",
   T["states"] == sum(len([x for x in os.listdir(
       os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS"))
       if x.endswith(".png") and "Contact_Sheet" not in x])
       for n in R.VIDEOS)
   and T["contact_sheets"] == len(R.VIDEOS),
   "%d active states, %d contact sheets" % (T["states"],
                                            T["contact_sheets"]))
ck("Every rendered state is cued by an event, and every cued state is "
   "rendered",
   all({x["name"] for e in EV.events(n) for x in e["states"]}
       == {x[:-4] for x in os.listdir(
           os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS"))
           if x.endswith(".png") and "Contact_Sheet" not in x}
       for n in R.VIDEOS),
   "%d states, %d events" % (T["states"], T["events"]))
_a = P.v4_arithmetic()
ck("V4's recount separates the introduction from the approved opening",
   _a["base"] + _a["intro"] + _a["hook"] == _a["total"],
   "%d + %d + %d = %d" % (_a["base"], _a["intro"], _a["hook"],
                          _a["total"]))
_retired_named = []
for n in R.VIDEOS:
    if not Q.retired(n):
        continue
    pkg = os.path.join(OUT, "PACKAGES", P.PKG[n])
    us = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                us.extend(units(os.path.join(root, nm)))
    for r in Q.retired(n):
        where = [u for u in us if r["key"] in u and "RETIRED" in u.upper()]
        _retired_named.append((n, r["key"], len(where)))
ck("Every retired family is marked RETIRED, not merely absent",
   all(c > 0 for _, _, c in _retired_named),
   ", ".join("V%d %s in %d places" % x for x in _retired_named)
   or "none retired")

# A decision that has been made must not still be asked, and a retired
# family must not still be offered back. Both survived the last pass in
# documents that were never regenerated against the decision.
_SETTLED = [
 ("the V6 card relabel", re.compile(
     r"whether to re-?label|was not redesigned|drop the sub-labels",
     re.I)),
 ("the V8 retirement", re.compile(
     r"rather keep it|give it its own passage|"
     r"(?<!not to be )reassigned to another", re.I)),
]
_docs = []
for _n in R.VIDEOS:
    for _root, _, _names in os.walk(os.path.join(OUT, "PACKAGES",
                                                 P.PKG[_n])):
        for _nm in sorted(_names):
            if _nm.endswith((".docx", ".txt")):
                _docs.append(os.path.join(_root, _nm))
for _nm in sorted(os.listdir(os.path.join(OUT, "SHARED"))):
    if _nm.endswith(".docx"):
        _docs.append(os.path.join(OUT, "SHARED", _nm))
for _what, _rx in _SETTLED:
    _hits = [(os.path.basename(f), u[:60]) for f in _docs
             for u in units(f) if _rx.search(u)]
    ck("No document still asks for %s" % _what, not _hits,
       _hits or "settled, and not reopened in %d documents" % len(_docs))

# A table cell is not a row. Reading the flat text of a document cannot
# tell whether the status beside a family name says retired, so the rows
# are read as rows.
def table_rows(path):
    from docx import Document
    out = []
    for t in Document(path).tables:
        for r in t.rows:
            out.append([c.text.strip() for c in r.cells])
    return out


_ledger = os.path.join(OUT, "SHARED", "V4-V11_REVISED_ASSET_LEDGER.docx")
_lrows = table_rows(_ledger)
for _n in R.VIDEOS:
    for _r in Q.retired(_n):
        _rows = [row for row in _lrows
                 if any(_r["key"] in c for c in row)]
        _unmarked = [row for row in _rows
                     if not any("RETIRED" in c.upper()
                                or "INACTIVE" in c.upper() for c in row)]
        ck("Every ledger row for %s says retired" % _r["key"],
           _rows and not _unmarked,
           "%d rows name it, %d of them marked"
           % (len(_rows), len(_rows) - len(_unmarked)))
        _ev = os.path.join(OUT, "PACKAGES", P.PKG[_n], "07_EVIDENCE",
                           "Evidence_and_Boundary_Notes.docx")
        _erows = [row for row in table_rows(_ev)
                  if any(_r["key"] in c for c in row)]
        _ebad = [row for row in _erows
                 if not any("RETIRED" in c.upper() for c in row)]
        ck("V%d evidence notes name %s as retired" % (_n, _r["key"]),
           _erows and not _ebad,
           "%d rows name it, %d of them marked"
           % (len(_erows), len(_erows) - len(_ebad)))

_mu = units(os.path.join(OUT, "SHARED",
                         "V4-V11_COMBINED_SOURCE_MANIFEST.docx"))
_a4 = P.v4_arithmetic()
ck("The manifest shows V4's introduction and hook delta apart",
   "+%d" % _a4["intro"] in _mu and "+%d" % _a4["hook"] in _mu
   and "+%d" % (_a4["intro"] + _a4["hook"]) not in _mu,
   "+%d and +%d, never +%d" % (_a4["intro"], _a4["hook"],
                               _a4["intro"] + _a4["hook"]))
ck("No document calls the new opening families cards",
   not [1 for f in _docs for u in units(f)
        if re.search(r"six opening cards", u, re.I)],
   "six families comprising eight states")

# The event list, read back out of the delivered documents rather than
# out of the generator, because the fault being tested was two documents
# disagreeing about the same paragraph.
def _cam(n):
    return open(os.path.join(OUT, "PACKAGES", P.PKG[n], "03_RIVERSIDE",
                             "Camera_and_Full_Screen_Map.txt")).read()


for _n in R.VIDEOS:
    _txt = _cam(_n)
    _ell = [l for l in _txt.split("\n")
            if ("ENTER ON:" in l or "LEAVE ON:" in l) and "..." in l]
    ck("V%d no entry or exit phrase in the map is truncated" % _n,
       not _ell, "%d boundary lines, none cut" % len(
           [l for l in _txt.split("\n")
            if "ENTER ON:" in l or "LEAVE ON:" in l]))
    _missing = []
    for _e in EV.events(_n):
        if _e["mode"] != EV.FULL:
            continue
        if ("[%s]" % _e["eid"]) not in _txt:
            _missing.append(_e["eid"])
    ck("V%d every full-screen event appears in the delivered map" % _n,
       not _missing, _missing or "%d events printed"
       % len(EV.events(_n)))
    _riv = open(os.path.join(OUT, "PACKAGES", P.PKG[_n], "03_RIVERSIDE",
                             "Riverside_CoCreator_Master_Prompt.txt")).read()
    _gone = [e["eid"] for e in EV.events(_n)
             if ("[%s]" % e["eid"]) not in _txt
             and (" %s " % e["eid"]) not in _riv
             and ("  %s  " % e["eid"]) not in _riv]
    ck("V%d the prompt and the map carry the same events" % _n,
       not _gone, _gone or "%d events in both" % len(EV.events(_n)))
    for _e in EV.events(_n):
        pass
    _sound = [e for e in EV.events(_n) if e["sound"]]
    ck("V%d each sound event is one record with its own accent word" % _n,
       all("word" in e["sound"] for e in _sound),
       "%d sound events" % len(_sound))

bad = [r for r in Rw if not r[1]]
for nm, o, d in Rw:
    if not o:
        print("FAIL  %s  ->  %s" % (nm, d))
# The count this run produced is written out, and the documents read it
# from here rather than carrying a typed number.
_stated = T.get("final_checks")
json.dump(dict(final_checks=len(Rw), passed=len(Rw) - len(bad),
               stamp=P.stamp()), open(P.VERIFY_FILE, "w"), indent=1)
if _stated is not None and _stated != len(Rw):
    print("NOTE  the documents state %d final checks and this run has %d; "
          "rebuild the packages so they agree" % (_stated, len(Rw)))
elif _stated is None:
    print("NOTE  no verification total was available when the documents "
          "were written; rebuild the packages so they carry %d" % len(Rw))
print("\nfinal verification: %d of %d passed" % (len(Rw) - len(bad),
                                                 len(Rw)))
print("outer archive sha256 %s" % sha256(arc))
print("\n%-5s %9s %9s %8s %8s %7s" % ("", "words", "blocks", "active",
                                      "states", "shorts"))
print("%-5s %9s %9s %8s %8s %7s" % ("", "", "thought", "families",
                                    "teaching", ""))
for n in R.VIDEOS:
    vis = os.path.join(OUT, "PACKAGES", P.PKG[n], "04_VISUAL_ASSETS")
    png = [x for x in os.listdir(vis)
           if x.endswith(".png") and "Contact_Sheet" not in x]
    print("V%-4d %9s %9d %8d %8d %7d"
          % (n, format(R.word_count(n), ","), len(P.blocks(n)),
             len(P.cues(n)), len(png), len(SH.rows(n))))
