# -*- coding: utf-8 -*-
"""Assemble the V12-V14 Phase 2 production pack."""
import os, sys, zipfile, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Every module in this pack is prefixed p2_ because the house document helpers
# insert their own build directories at the front of sys.path, which shadows bare
# names like build, shorts and packaging.

from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, section_label, rule)
import p2_docs as DP
import p2_blocks as B, p2_shorts as S, p2_production as PR, p2_descriptions as D
import p2_provenance as PV, p2_packaging as PK, p2_qa as QA, p2_checks_script as CH

STAGE = os.path.join(HERE, "_stage")
ZIPNAME = "YOUTUBE_V12-V14_PHASE2_PRODUCTION_PACK.zip"
EYEBROW = DP.EYEBROW
STAMP = DP.STAMP

FILES = {}
for n, tag in ((12, "V12"), (13, "V13"), (14, "V14_WORKING")):
    w = "_WORKING" if n == 14 else ""
    FILES[(n, "master")] = "%02d_%s/%s_RECORDING_MASTER%s.docx" % (n, "V%d" % n, "V%d" % n, w)
    FILES[(n, "blocks")] = "%02d_%s/%s_THOUGHT_BLOCKS%s.docx" % (n, "V%d" % n, "V%d" % n, w)
    FILES[(n, "prod")]   = "%02d_%s/%s_PRODUCTION_PACKAGE%s.docx" % (n, "V%d" % n, "V%d" % n, w)
    FILES[(n, "shorts")] = "%02d_%s/%s_SHORTS%s.docx" % (n, "V%d" % n, "V%d" % n, w)
    FILES[(n, "desc")]   = "%02d_%s/%s_DESCRIPTION_METADATA%s.docx" % (n, "V%d" % n, "V%d" % n, w)
    FILES[(n, "prov")]   = "%02d_%s/%s_SOURCE_PROVENANCE%s.docx" % (n, "V%d" % n, "V%d" % n, w)

OVERVIEW = "00_PHASE2_OVERVIEW.docx"
PACKDOC  = "14_V14/V14_PACKAGING_OPTIONS.docx"
QADOC    = "00_V12-V14_QA_CHECKLIST.docx"

# ------------------------------------------------------------------ extra documents
def overview(path):
    d = base_doc()
    title_block(d, EYEBROW, "V12, V13 and V14", "What is in this pack and how it was built")
    kv(d, "Generated", STAMP)
    kv(d, "Scope", "Three videos. V12 and V13 are complete. V14 is complete as a working script "
                   "with its packaging unresolved.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "V4 to V11 were not opened, renumbered, or changed. No historical source file was "
               "overwritten or deleted. This pack stops at V14.")

    h(d, "The three videos")
    rows = []
    for n in (12, 13, 14):
        m = DP.META[n]
        rows.append([m["number"], m["title"] + ("  [working]" if m["status"] else ""),
                     m["thumb"], "{:,}".format(DP.words(n)),
                     "%s to %s" % (DP.runtime(n, 145), DP.runtime(n, 130))])
    table(d, ["#", "Title", "Thumbnail", "Spoken words", "Speech-only estimate"], rows,
          widths=[0.5, 3.0, 1.35, 0.9, 0.95])
    caption(d, "Speech-only estimates are arithmetic on the word count at 145 and 130 words per "
               "minute. Nothing here has been recorded, so nothing here has been measured. The "
               "finished edit will run longer than these figures because of full-screen holds.")

    h(d, "What each video is doing")
    for n in (12, 13, 14):
        m = DP.META[n]
        sub(d, "%s  ·  %s" % (m["number"], m["title"]))
        kv(d, "Primary audit", m["audit"])
        kv(d, "Artifact", m["artifact"])
        kv(d, "Resource", D.RESOURCE[n][1])
        kv(d, "Watch next", D.WATCH_NEXT[n][0])
    callout(d, "V12 and V13 carry different resources on purpose, and V14 carries the free "
               "decision check rather than the Field Kit a second time. That keeps the same paid "
               "resource out of two consecutive slots, which the Phase 1.5 decision pack flagged "
               "as a pacing risk in this sequence.")

    h(d, "The ten-minute promise in V12")
    para(d, "The title promises ten minutes for the viewer's exercise, not a ten-minute video, and "
            "the script budgets those ten minutes out loud: two on what was true before, three on "
            "what was yours to decide, two on the call that was not obvious, three on what changed "
            "and how you know.")
    para(d, "The video itself was still written to fit the promise. At %s spoken words it runs "
            "%s at 145 words per minute and %s at 130. The planning target was a script that "
            "cannot embarrass the title once holds and pauses are added."
            % ("{:,}".format(DP.words(12)), DP.runtime(12, 145), DP.runtime(12, 130)))

    h(d, "Where the material came from")
    table(d, ["Video", "Primary source", "What changed"],
          [["V12", "Old roadmap V23, 895 spoken words",
            "Rewritten for voice. Restructured so the accomplishment is seen before it is improved. "
            "Added the artifact reaction, the ten-minute budget, and the proof-is-not-an-offer "
            "boundary. The four questions are never named as a framework."],
           ["V13", "Old V14 plus the 28-posting research record",
            "Rebuilt around three real postings that use the same two words. The old four named "
            "buckets were removed as a framework; the same distinctions now run through the "
            "analysis unlabelled. Every count is carried exactly."],
           ["V14", "Old roadmap V31, 694 spoken words",
            "Substantially rebuilt. Every assertion about what employers or hiring managers believe "
            "was cut. The episode is now a read of two specific postings, with a two-part verdict "
            "after each one."]],
          widths=[0.6, 2.1, 4.0])

    h(d, "What is not in this pack")
    bullets(d, [n + ". " + t for n, t in QA.NOT_DONE])
    footer_note(d, "Every figure in this document is read from the build at generation time.")
    d.save(path)

def packaging_doc(path):
    d = base_doc()
    title_block(d, EYEBROW, "V14 packaging options",
                "Five title and thumbnail pairs. One recommendation. Nothing chosen.")
    kv(d, "Generated", STAMP)
    callout(d, "WORKING — PACKAGING PENDING TEMIDAYO APPROVAL. The V14 script in this pack is "
               "built on Option %d as a working assumption so that a complete episode exists to "
               "react to. That is not a decision." % PK.RECOMMENDED)
    for o in PK.OPTIONS:
        flag = "  — " + PK.RECOMMENDED_LABEL if o["n"] == PK.RECOMMENDED else (
               "  — runner-up" if o["n"] == PK.RUNNER_UP else "")
        h(d, "OPTION %d%s" % (o["n"], flag))
        kv(d, "Title", o["title"])
        kv(d, "Thumbnail", o["thumb"])
        kv(d, "Curiosity gap", o["gap"])
        sub(d, "Why it fits this actual video")
        para(d, o["fit"])
        sub(d, "What it costs")
        para(d, o["risk"])
    h(d, "The recommendation")
    para(d, PK.WHY)
    h(d, "What changes if a different option is chosen")
    bullets(d, PK.SWAP_POINTS)
    h(d, "Excluded")
    para(d, "“%s” was not developed, as instructed." % PK.BANNED[0])
    d.save(path)

def qa_doc(path, ctx):
    rows = QA.run(ctx)
    d = base_doc()
    title_block(d, EYEBROW, "QA checklist", "Twenty items, run against the files in this pack")
    kv(d, "Generated", STAMP)
    kv(d, "Items run", "%d of 20" % sum(1 for r in rows if r["state"] == QA.PERFORMED))
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
    footer_note(d, "%d of 20 checks ran and %d passed. The remaining work listed above is real and "
                   "is not covered by any result on this page."
                % (sum(1 for r in rows if r["state"] == QA.PERFORMED),
                   sum(1 for r in rows if r["ok"])))
    d.save(path)
    return rows

# ------------------------------------------------------------------ assemble

FIXED = (2026, 9, 21, 0, 0, 0)

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
    overview(full(OVERVIEW))
    packaging_doc(full(PACKDOC))
    ctx = QA.Ctx(STAGE, FILES)
    rows = qa_doc(full(QADOC), ctx)

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
    print("QA: %d of 20 run, %d passed, %d failed"
          % (sum(1 for r in rows if r["state"] == QA.PERFORMED),
             len(rows) - len(bad), len(bad)))
