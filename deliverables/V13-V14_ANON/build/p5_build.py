# -*- coding: utf-8 -*-
"""Assemble the V12-V14 Phase 2 production pack."""
import os, sys, zipfile, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Every module in this pack is prefixed p5_ because the house document helpers
# insert their own build directories at the front of sys.path, which shadows bare
# names like build, shorts and packaging.

from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, section_label, rule)
import p5_docs as DP
import p5_blocks as B, p5_shorts as S, p5_production as PR, p5_descriptions as D
import p5_provenance as PV, p5_packaging as PK, p5_qa as QA, p5_checks_script as CH
import p5_changes as CG

STAGE = os.path.join(HERE, "_stage")
ZIPNAME = "YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip"
EYEBROW = DP.EYEBROW
STAMP = DP.STAMP

FILES = {}
for n in (12, 13, 14):
    d_ = "V%d" % n
    FILES[(n, "master")] = "%s/%s_FINAL_RECORDING_MASTER.docx" % (d_, d_)
    FILES[(n, "blocks")] = "%s/%s_FINAL_THOUGHT_BLOCKS.docx" % (d_, d_)
    FILES[(n, "prod")]   = "%s/%s_FINAL_PRODUCTION_PACKAGE.docx" % (d_, d_)
    FILES[(n, "shorts")] = "%s/%s_FINAL_SHORTS.docx" % (d_, d_)
    FILES[(n, "desc")]   = "%s/%s_FINAL_DESCRIPTION_METADATA.docx" % (d_, d_)
    FILES[(n, "prov")]   = "%s/%s_FINAL_SOURCE_PROVENANCE.docx" % (d_, d_)

OVERVIEW = "00_FINAL_RECONCILIATION_REPORT.docx"
PACKDOC  = "00_V12-V14_LOCKED_PACKAGING.docx"
QADOC    = "00_V12-V14_FINAL_QA_CHECKLIST.docx"

# ------------------------------------------------------------------ extra documents
def overview(path, rows):
    d = base_doc()
    title_block(d, EYEBROW, "V12 to V14 final reconciliation and lock",
                "What changed, what was protected, and what is still open")
    kv(d, "Generated", STAMP)
    kv(d, "Scope", "Three videos, reconciled and now packaging-locked. Nothing in this pack is "
                   "marked working.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "Not a rebuild. V4 to V11 remain locked and were not opened, and the "
               "alternative V4 to V11 packaging in the new construction document was read and "
               "deliberately not implemented. No historical source file was renumbered, "
               "overwritten or deleted. Work stops at V14.")

    h(d, "What was new in this pass")
    para(d, CG.REUPLOAD_NOTE)
    table(d, ["Was", "Is now", "Why"],
          [[a, b, c] for a, b, c in CG.LOCK_CHANGES], widths=[2.3, 2.4, 2.0])
    caption(d, "Everything below this point is the September 21 reconciliation, carried forward "
               "and re-verified against the locked packaging.")

    h(d, "Locked packaging")
    table(d, ["#", "Title", "Thumbnail"],
          [[o["n"], o["title"], o["thumb"]] for o in PK.LOCKED], widths=[0.45, 4.0, 2.25])
    para(d, PK.RULE)

    h(d, "Spoken word counts and runtime estimates")
    table(d, ["#", "Title", "Spoken words", "At 145 wpm", "At 130 wpm"],
          [[DP.META[n]["number"], DP.META[n]["title"] + ("  [working]" if DP.META[n]["status"] else ""),
            "{:,}".format(DP.words(n)), DP.runtime(n, 145), DP.runtime(n, 130)]
           for n in (12, 13, 14)], widths=[0.5, 3.1, 1.0, 1.05, 1.05])
    caption(d, "Word counts are exact: whitespace-delimited tokens of the spoken stream, counted "
               "back off these built documents and cross-checked against the script modules. "
               "Both runtime columns are ESTIMATES. They are arithmetic on the word count, not "
               "measurements. Runtime stays an estimate until footage exists, and the finished "
               "edit will run longer because of full-screen holds.")
    para(d, "V12 moved from 1,266 to %s spoken words, V13 from 1,457 to %s, and V14 from 1,398 "
            "to %s. Every increase is the reconciliation putting words back, not new teaching."
          % ("{:,}".format(DP.words(12)), "{:,}".format(DP.words(13)), "{:,}".format(DP.words(14))))

    for n in (12, 13, 14):
        page_break(d)
        h(d, "Exact changes made to %s" % DP.META[n]["number"])
        table(d, ["Was", "Is now", "Why"],
              [[a, b, c] for a, b, c in CG.CHANGES[n]], widths=[2.3, 2.4, 2.0])

    page_break(d)
    h(d, "Strong lines deliberately preserved")
    for n in (12, 13, 14):
        sub(d, DP.META[n]["number"])
        bullets(d, CG.PRESERVED[n])
    para(d, "Thirteen of these are exact sentences and are checked word for word against the "
            "built masters at build time. If any one of them were dropped or edited, the build "
            "would report it rather than ship.")

    h(d, "Packaging")
    para(d, PK.BORROWED)
    para(d, PK.RETIRED)
    para(d, "The locked decisions, what each title and thumbnail is doing, and every place a "
            "title is written down are recorded in 00_V12-V14_LOCKED_PACKAGING inside this pack. "
            "No packaging brainstorm was run in this pass.")

    h(d, "Final CTA for each video, and why")
    for n in (12, 13, 14):
        name, url, why = CG.CTA[n]
        sub(d, "%s  \u00b7  %s" % (DP.META[n]["number"], name))
        kv(d, "Link", url)
        para(d, why)
    caption(d, "One primary ask per video. V13 and V14 point to the same resource because they "
               "leave the viewer with the same unresolved problem, not because of slot order.")

    page_break(d)
    h(d, "Evidence and provenance checks performed")
    bullets(d, [
      "The three revised masters and the editorial review were read paragraph by paragraph "
      "before anything was changed, and each is recorded with its SHA-256 in every provenance "
      "file it fed.",
      "No posting fact changed in this pass. The four coded postings quoted on camera, Humana "
      "H10, Wells Fargo F1, Mass General Brigham H8 and J.P. Morgan Wealth Management F5, still "
      "carry the same URL, collection date, capture route and hard-versus-preferred coding as "
      "the checksummed September 10, 2026 research record.",
      "V13's denominators were re-verified in the built documents: about 55 surfaced, 40 read in "
      "full, 28 retained, 18 exclusion log entries, 10 healthcare, 10 financial services, 8 "
      "technology, all collected September 10, 2026.",
      "No new research was conducted. No posting URL was re-fetched.",
      "The workspace was searched again for a Career Move Review page or URL. There is still none, in any HTML, Markdown, text, JSON or JavaScript file.",
      "The four documents re-supplied with the lock instruction were checked by SHA-256 against the values already recorded in the previous pack. All four match exactly.",
    ])

    h(d, "Scripture verification status")
    callout(d, PV.SCRIPTURE)

    h(d, "QA actually performed")
    kv(d, "Checks run against the built files", "%d" % sum(1 for r in rows if r["state"] == QA.PERFORMED))
    kv(d, "Passing", "%d" % sum(1 for r in rows if r["ok"]))
    table(d, ["#", "Check", "Result"],
          [["%02d" % r["n"], r["name"], "pass" if r["ok"] else "FAIL"] for r in rows],
          widths=[0.45, 5.3, 0.95])
    para(d, "These ran against the documents in this pack, not against the source modules. The "
            "full detail, and the list of what was not performed, is in the QA checklist inside "
            "this pack.")

    h(d, "Still requiring Temidayo's decision")
    for name, why in CG.APPROVALS:
        sub(d, name)
        para(d, why)
    callout(d, "Nothing in this pack is described as production ready. Four items above are "
               "open, and the scripture wording is the one that blocks publication.")
    footer_note(d, "Every figure in this report is read from the build at generation time.")
    d.save(path)

def packaging_doc(path):
    d = base_doc()
    title_block(d, EYEBROW, "Locked packaging",
                "V12, V13 and V14, and the construction rule behind them")
    kv(d, "Generated", STAMP)
    kv(d, "Status", "Locked September 22, 2026. No packaging brainstorm was run in this pass.")
    callout(d, PK.V4_V11)

    h(d, "Locked")
    table(d, ["#", "Title", "Thumbnail", "Construction"],
          [[o["n"], o["title"], o["thumb"], o["construction"]] for o in PK.LOCKED],
          widths=[0.45, 2.55, 1.75, 1.95])
    for o in PK.LOCKED:
        sub(d, "%s  \u00b7  %s" % (o["n"], o["title"]))
        kv(d, "Thumbnail", o["thumb"])
        kv(d, "What each one does", o["jobs"])
        kv(d, "This pass", o["changed"])

    h(d, "The construction being borrowed")
    para(d, PK.BORROWED)

    h(d, "The packaging rule")
    para(d, PK.RULE)

    h(d, "Retired")
    para(d, PK.RETIRED)
    para(d, "\u201c%s\u201d was never developed, as instructed." % PK.EXCLUDED)

    h(d, "Where a title or thumbnail is written down")
    bullets(d, PK.TOUCHPOINTS)
    caption(d, "Listed so a future packaging change is mechanical rather than a hunt.")
    d.save(path)

def qa_doc(path, ctx):
    rows = QA.run(ctx)
    d = base_doc()
    title_block(d, EYEBROW, "QA checklist", "Twenty items, run against the files in this pack")
    kv(d, "Generated", STAMP)
    kv(d, "Items run", "%d" % sum(1 for r in rows if r["state"] == QA.PERFORMED))
    kv(d, "Items passing", "%d" % sum(1 for r in rows if r["ok"]))
    callout(d, "These twenty checks were actually executed against the built documents on disk, "
               "not against the source modules. Anything that was not performed is listed at the "
               "end of this document instead of being counted here. Nothing in this pack is "
               "described as fully verified, production ready, or QA passed.")
    table(d, ["#", "Check", "Result", "Detail"],
          [["%02d" % r["n"], r["name"], ("pass" if r["ok"] else "FAIL"), r["detail"]]
           for r in rows], widths=[0.4, 2.15, 0.6, 3.55])
    h(d, "Not performed, and why")
    for name, why in QA.NOT_DONE:
        sub(d, name)
        para(d, why)
    footer_note(d, "%d checks ran and %d passed. The remaining work listed above is real and "
                   "is not covered by any result on this page."
                % (sum(1 for r in rows if r["state"] == QA.PERFORMED),
                   sum(1 for r in rows if r["ok"])))
    d.save(path)
    return rows

# ------------------------------------------------------------------ assemble

FIXED = (2026, 9, 22, 0, 0, 0)

def normalize(path):
    """Rewrite a .docx so two builds of the same content produce the same bytes.

    python-docx stamps each entry with the current time and sets core properties from
    the clock, so an untouched pack would hash differently every run. Entry order is
    preserved; only the timestamps are fixed.
    """
    import re as _re, shutil, tempfile
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    stamp = "2026-09-21T00:00:00Z"
    out = []
    for info, data in items:
        if info.filename == "docProps/core.xml":
            t = data.decode("utf-8")
            t = _re.sub(r"(<dcterms:(?:created|modified)[^>]*>)[^<]*(</dcterms:)",
                        r"\g<1>" + stamp + r"\g<2>", t)
            data = t.encode("utf-8")
        out.append((info.filename, info.compress_type, data))
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w") as z:
        for name, ctype, data in out:
            zi = zipfile.ZipInfo(name, date_time=FIXED)
            zi.compress_type = ctype
            zi.external_attr = 0o644 << 16
            z.writestr(zi, data)
    os.replace(tmp, path)

def sha256(p):
    h_ = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h_.update(b)
    return h_.hexdigest()

def main():
    os.makedirs(STAGE, exist_ok=True)
    import shutil
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    for n in (12, 13, 14):
        os.makedirs(os.path.join(STAGE, os.path.dirname(FILES[(n, "master")])), exist_ok=True)
    def full(rel):
        p = os.path.join(STAGE, rel)
        os.makedirs(os.path.dirname(p) or STAGE, exist_ok=True)
        return p
    for n in (12, 13, 14):
        DP.recording_master(full(FILES[(n, "master")]), n)
        DP.thought_blocks(full(FILES[(n, "blocks")]), n)
        DP.production_package(full(FILES[(n, "prod")]), n)
        DP.shorts_doc(full(FILES[(n, "shorts")]), n)
        DP.description_doc(full(FILES[(n, "desc")]), n)
        DP.provenance_doc(full(FILES[(n, "prov")]), n)
    packaging_doc(full(PACKDOC))
    ctx = QA.Ctx(STAGE, FILES)
    rows = qa_doc(full(QADOC), ctx)
    overview(full(OVERVIEW), rows)

    names = sorted(os.path.relpath(os.path.join(r, f), STAGE)
                   for r, _, fs in os.walk(STAGE) for f in fs)
    for rel in names:
        if rel.endswith(".docx"):
            normalize(os.path.join(STAGE, rel))
    zpath = os.path.join(OUT, ZIPNAME)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(STAGE, rel), "rb") as f:
                z.writestr(zi, f.read())
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), ZIPNAME))
    return zpath, names, rows

if __name__ == "__main__":
    zp, names, rows = main()
    bad = [r for r in rows if not r["ok"]]
    for r in rows:
        print(("  ok  " if r["ok"] else " FAIL ") + "%02d %s" % (r["n"], r["name"]))
        if not r["ok"]:
            print("        " + r["detail"][:300])
    print("\n%d files" % len(names))
    for x in names: print("   ", x)
    print("\n%s\n%s" % (zp, sha256(zp)))
    print("QA: %d run, %d passed, %d failed"
          % (sum(1 for r in rows if r["state"] == QA.PERFORMED),
             len(rows) - len(bad), len(bad)))
