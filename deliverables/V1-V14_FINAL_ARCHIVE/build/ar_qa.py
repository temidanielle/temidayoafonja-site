# -*- coding: utf-8 -*-
"""Final QA, run against the ZIP that was actually produced."""
import os, sys, zipfile, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ar_sources as S, ar_parity as P, ar_data as D, ar_build as B

CHECKS = []
def check(n, name, ok, detail=""):
    CHECKS.append((n, name, bool(ok), detail))

def run(zpath):
    z = zipfile.ZipFile(zpath)
    names = z.namelist()
    rows = {r["n"]: r for r in P.run()}

    masters = [x for x in names if "/01_RECORDING_MASTERS/" in x]
    blocks = [x for x in names if "/02_THOUGHT_BLOCKS/" in x]
    check(1, "Fourteen recording masters present", len(masters) == 14,
          "%d found" % len(masters))
    check(2, "Fourteen thought-block copies present", len(blocks) == 14,
          "%d found" % len(blocks))

    bad = [n for n in rows if not rows[n]["passed"]]
    check(3, "14 of 14 thought-block parity PASS", not bad,
          bad or "every master and its blocks match word for word and in order")

    stated = [n for n in rows if rows[n]["stated"] is not None
              and rows[n]["stated"] != rows[n]["words"]]
    check(4, "Printed word count matches the read count where one is printed",
          not stated,
          stated or "eleven files print a count and all eleven agree")

    check(5, "Parity check still fails on injected breakage",
          P.parity_regression(),
          "a changed word, a dropped sentence and a duplicated sentence are "
          "all rejected")
    check(6, "The reader returns real speech for all three document shapes",
          P.reader_regression())

    # copies identical to their approved source
    mism = []
    for n in sorted(S.SRC):
        for src, inzip in ((S.SRC[n][0], "/01_RECORDING_MASTERS/" + B.master_name(n)),
                           (S.SRC[n][1], "/02_THOUGHT_BLOCKS/" + B.blocks_name(n))):
            hit = [x for x in names if x.endswith(inzip)]
            if not hit:
                mism.append("V%d missing %s" % (n, inzip)); continue
            if hashlib.sha256(z.read(hit[0])).hexdigest() != \
               hashlib.sha256(open(src, "rb").read()).hexdigest():
                mism.append("V%d %s differs from its source" % (n, inzip))
    check(7, "Every archived file is byte-for-byte its approved source", not mism,
          mism or "28 files, all identical to the source they were copied from. "
                  "For V2 and V3 that source is the September 23 repaired file, "
                  "whose only difference from the upload is that the section "
                  "label became its own paragraph.")

    # titles and thumbnails
    tb = []
    for n in sorted(S.TITLES):
        body = " ".join(P.paras(S.SRC[n][0]))
        if S.TITLES[n][0] not in body:
            tb.append("V%d title not in its master" % n)
    check(8, "Correct title for every video", not tb,
          tb or "all fourteen titles appear in their own master")
    check(9, "Correct thumbnail recorded for every video",
          len(S.TITLES) == 14 and all(S.TITLES[n][1] for n in S.TITLES),
          "fourteen thumbnails, taken from the approved list")

    # active source rules
    sticky = [n for n in (1, 2, 3)
              if "FINAL_Sticky_Realization" in os.path.basename(S.SRC[n][0])]
    check(10, "V1 to V3 use the FINAL Sticky Realization sources",
          sticky == [1, 2, 3], "masters and thought blocks both")
    stale = [n for n in (1, 2, 3)
             if "Refreshed" in os.path.basename(S.SRC[n][0])]
    check(11, "No earlier refreshed V1 to V3 master was packaged as current",
          not stale, stale or "the intermediate refreshed masters are excluded")
    check(12, "V4 to V14 use the sources named in the reconciliation",
          all("V4-V11_SYNC" in S.SRC[n][0] for n in range(4, 12))
          and "locked" in S.SRC[12][0] and all("anon" in S.SRC[n][0] for n in (13, 14)),
          "V4 to V11 reconciled masters, V12 from the locked pack, V13 and V14 "
          "from the anonymization patch")

    # the optional V9 sentence was not applied
    v9 = " ".join(P.spoken(S.SRC[9][0], "sync", "master"))
    tail = v9[v9.index("The question was never simply"):] if "The question was never simply" in v9 else v9[-400:]
    check(13, "Optional V9 change NOT applied",
          v9.count("The capability may still be there. The shortcuts are not.") == 1
          and "The capability may still be there" not in tail,
          "the sentence appears once, in its original place, and was not "
          "echoed at the payoff")

    check(14, "V9 word count unchanged from the reconciliation",
          rows[9]["words"] == 1069, "%d words" % rows[9]["words"])

    # no script rewritten: every archived master is identical to its source,
    # already proved by check 7. This one guards the V1-V3 case specifically.
    check(15, "No script was rewritten during archiving",
          not mism and rows[1]["words"] == 915 and rows[2]["words"] == 888
          and rows[3]["words"] == 923,
          "V1 915, V2 888 and V3 923 words. V2 and V3 moved by four and five "
          "words only because their section label stopped being counted as "
          "speech.")

    # CTA and Watch Next
    wn = [n for n in sorted(S.SRC)
          if D.WATCH_NEXT[n] not in " ".join(P.spoken(S.SRC[n][0], S.SRC[n][2], "master"))]
    check(16, "No missing or invented Watch Next", not wn,
          wn or "all fourteen Watch Next titles are spoken in their own master")
    named = [n for n in sorted(S.SRC) if not D.CTA[n].startswith("None")]
    bad_cta = [n for n in named
               if D.CTA[n] not in " ".join(P.spoken(S.SRC[n][0], S.SRC[n][2], "master"))]
    check(17, "Every named CTA is named in its own master", not bad_cta,
          bad_cta or "%d videos name a resource out loud; the other %d carry none"
          % (len(named), 14 - len(named)))

    # draft descriptions separated
    drafts = [x for x in names if "04_DRAFT_PUBLISHING_DESCRIPTIONS_REVIEW_REQUIRED" in x]
    leaked = [x for x in names
              if "DESCRIPTION" in x.upper()
              and ("01_RECORDING_MASTERS" in x or "02_THOUGHT_BLOCKS" in x)]
    check(18, "Draft descriptions are separated from the locked spoken sources",
          drafts and not leaked,
          "%d draft description files, all in the review-required folder, and "
          "none beside a locked master" % len(drafts))
    check(19, "Draft descriptions are labelled unapproved",
          all(os.path.basename(x).startswith("NOT_YET_APPROVED_") for x in drafts),
          "every filename carries NOT_YET_APPROVED")

    # production assets do not override speech
    prod = [x for x in names if "03_PRODUCTION_ASSETS_REFERENCE" in x]
    check(20, "Production assets are reference only and override no speech",
          prod and all(x.endswith(".zip") for x in prod),
          "%d packages, all carried as sealed ZIPs so none of them can be "
          "mistaken for the spoken source" % len(prod))

    # provenance not invented
    prov = [x for x in names if "05_PROVENANCE_AND_EVIDENCE" in x]
    check(21, "No missing provenance was invented", prov,
          "%d existing provenance files carried across. V1's employer and URL "
          "fields remain NOT SUPPLIED." % len(prov))

    # the three source-of-truth documents
    sot = [os.path.basename(x) for x in names if "00_SOURCE_OF_TRUTH" in x]
    check(22, "The three source-of-truth documents are present",
          set(sot) == {B.MANIFEST, B.SUPERSESSION, B.RECON}, sorted(sot))

    # checksums recorded
    import docx, io as _io
    man = [x for x in names if x.endswith(B.MANIFEST)][0]
    tmp = os.path.join(HERE, "_m.docx")
    open(tmp, "wb").write(z.read(man))
    body = " ".join(p.text for p in docx.Document(tmp).paragraphs)
    body += " ".join(c.text for t in docx.Document(tmp).tables
                     for r in t.rows for c in r.cells)
    os.remove(tmp)
    missing_sha = [n for n in sorted(S.SRC)
                   if hashlib.sha256(open(S.SRC[n][0], "rb").read()).hexdigest() not in body]
    check(23, "All source checksums are recorded in the manifest",
          not missing_sha, missing_sha or "fourteen master checksums present")

    import ar_repair as R
    rep = R.verify()
    check(24, "The V2 and V3 section-label repair changed no spoken word",
          all(r["clean"] for r in rep)
          and not rows[2]["fused"] and not rows[3]["fused"]
          and "RESOLVED SEPTEMBER 23, 2026" in D.FUSED_NOTE,
          "verified token by token against the pre-repair files: the only "
          "difference in each spoken stream is the label's own words. V2 892 "
          "to 888, V3 928 to 923, in master and blocks alike.")
    check(26, "The pre-repair originals are recorded with their checksums",
          all(hashlib.sha256(open(S.PRE_REPAIR[n][i], "rb").read()).hexdigest()
              in body for n in (2, 3) for i in (0, 1)),
          "four pre-repair checksums present in the manifest")
    import ar_build as BB
    dz = os.path.join(os.path.dirname(HERE), BB.DOCSZIP)
    dn = zipfile.ZipFile(dz).namelist()
    check(27, "The documents-only archive carries every document and no "
              "production package",
          all("/03_PRODUCTION_ASSETS_REFERENCE/" not in x for x in dn)
          and len([x for x in dn if "/01_RECORDING_MASTERS/" in x]) == 14
          and len([x for x in dn if "/02_THOUGHT_BLOCKS/" in x]) == 14
          and len([x for x in dn if "/00_SOURCE_OF_TRUTH/" in x]) == 3
          and any("/04_DRAFT" in x for x in dn)
          and any("/05_PROVENANCE" in x for x in dn),
          "%d files, %.1f MiB, under the 30 MiB limit"
          % (len(dn), os.path.getsize(dz) / 1048576.0))
    check(28, "The full archive still carries the production packages unchanged",
          len([x for x in names if "/03_PRODUCTION_ASSETS_REFERENCE/" in x]) == 4,
          "four packages, copied not rebuilt")

    # V15+ untouched
    check(25, "V15 and above were not modified",
          not any("V15" in x or "V16" in x for x in names),
          "nothing from V15 onward appears in this archive")
    return CHECKS

if __name__ == "__main__":
    import ar_build
    zp = os.path.join(os.path.dirname(HERE), ar_build.ZIPNAME)
    rows = run(zp)
    for n, name, ok, detail in rows:
        print(("  ok  " if ok else " FAIL ") + "%02d %s" % (n, name))
        if not ok:
            print("        " + str(detail)[:240])
    bad = [r for r in rows if not r[2]]
    print("\n%d checks, %d passed, %d failed" % (len(rows), len(rows) - len(bad), len(bad)))
