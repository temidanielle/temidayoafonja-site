# -*- coding: utf-8 -*-
"""Assemble the V15-V22 final production pack."""
import os, sys, zipfile, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Every module in this pack is prefixed p6_ because the house document helpers
# insert their own build directories at the front of sys.path, which shadows bare
# names like build, shorts and packaging.

from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, section_label, rule)
import p6_docs as DP
import p6_blocks as B, p6_shorts as S, p6_production as PR, p6_descriptions as D
import p6_provenance as PV, p6_packaging as PK, p6_qa as QA, p6_checks_script as CH

STAGE = os.path.join(HERE, "_stage")
ZIPNAME = "YOUTUBE_V15-V22_FINAL_PRODUCTION_PACK.zip"
EYEBROW = DP.EYEBROW
STAMP = DP.STAMP

VIDEOS = tuple(range(15, 23))

FILES = {}
for n in VIDEOS:
    d_ = "V%d" % n
    FILES[(n, "master")] = "%s/%s_FINAL_RECORDING_MASTER.docx" % (d_, d_)
    FILES[(n, "blocks")] = "%s/%s_FINAL_THOUGHT_BLOCKS.docx" % (d_, d_)
    FILES[(n, "prod")]   = "%s/%s_FINAL_PRODUCTION_PACKAGE.docx" % (d_, d_)
    FILES[(n, "shorts")] = "%s/%s_FINAL_SHORTS.docx" % (d_, d_)
    FILES[(n, "desc")]   = "%s/%s_FINAL_DESCRIPTION_METADATA.docx" % (d_, d_)
    FILES[(n, "prov")]   = "%s/%s_FINAL_SOURCE_PROVENANCE.docx" % (d_, d_)

OVERVIEW = "00_V15-V22_FINAL_OVERVIEW.docx"
QADOC    = "00_V15-V22_FINAL_QA_REPORT.docx"
EVIDDOC  = "00_MISSING_RUNG_EVIDENCE_BOUNDARIES.docx"
THUMBDOC = "00_V20_THUMBNAIL_DECISION.docx"

# ------------------------------------------------------------------ extra documents

FUTURE = [
 ("V23", "MR5 absorbs the old V20",
  "Carry forward: design authority, escalation authority, the negotiation wording, the "
  "pattern-over-time and shock-absorber read, and constraint honesty. Do NOT carry the "
  "manager-side detour. MR5 is the stronger version of the old V20 and is the one to "
  "build from."),
 ("V24", "MR6 absorbs the old V21",
  "Carry forward: reversibility, and sample-the-work. Packaging is unresolved and is not "
  "decided here."),
 ("V25", "MR7 stands alone",
  "Do not rebuild V8's evidence teaching inside it. MR7's third column, what can I still "
  "prove outside this company, is evidence formation and routes to the existing video."),
 ("V26", "MR2 and MR8 merge",
  "They are one episode run twice. MR2's two roles are constructed and must be labelled "
  "the way V15, V19 and V22 label theirs. MR8's WATCH ME READ THE MOVE section label has "
  "to be renamed before it reaches a chapter title or a card."),
]

OPEN = [
 ("V20 thumbnail",
  "Three candidates and one recommendation are in 00_V20_THUMBNAIL_DECISION. Until "
  "Temidayo chooses, p6_script20.THUMB holds the literal string PENDING TEMIDAYO "
  "APPROVAL, so an unapproved line cannot reach a card or a render. The V20 title is "
  "locked and was not reopened."),
 ("Scripture wording",
  "Eight NLT references are recorded as intended references, not as verified wording. No "
  "authorized New Living Translation text exists anywhere in this workspace. This is the "
  "one item that blocks publishing."),
 ("Resource URLs",
  "career-evidence-starter, keep-the-proof and fieldkit are carried forward from the "
  "locked V12 to V14 pack. None was loaded in this pass to confirm it is live."),
 ("Card art",
  "Card copy and on-card labels are specified for all 50 full-screen cards. No PNG or "
  "SVG was rendered."),
]

def overview(path, rows):
    d = base_doc()
    title_block(d, EYEBROW, "V15 to V22 final production pack",
                "Eight videos built, what each one is bounded by, and what is still open")
    kv(d, "Generated", STAMP)
    kv(d, "Scope", "Eight videos, V15 through V22. Nothing before V15 was opened for edit and "
                   "nothing after V22 was built.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "V4 to V12 were not touched. V13 and V14 were changed only by the public-employer "
               "anonymization patch, which is already committed and is not reopened here. V23 to "
               "V26 are recorded as future work at the end of this document and were NOT built: "
               "no script, no card, no Short, no description and no provenance file exists for "
               "any of them.")

    h(d, "The eight videos")
    table(d, ["#", "Title", "Thumbnail", "Spoken words", "At 145 wpm", "At 130 wpm"],
          [[DP.META[n]["number"], DP.META[n]["title"], DP.META[n]["thumb"],
            "{:,}".format(DP.words(n)), DP.runtime(n, 145), DP.runtime(n, 130)]
           for n in VIDEOS], widths=[0.45, 2.5, 1.55, 0.8, 0.7, 0.7])
    caption(d, "Word counts are exact: whitespace-delimited tokens of the spoken stream, counted "
               "back off these built documents and cross-checked against the script modules. Both "
               "runtime columns are ESTIMATES. They are arithmetic on the word count, not "
               "measurements. Runtime stays an estimate until footage exists, and the finished "
               "edit will run longer because of full-screen holds.")
    para(d, "Total spoken words across the eight: %s. Every one is inside the locked band of 889 "
            "to 1,457." % "{:,}".format(sum(DP.words(n) for n in VIDEOS)))

    h(d, "Watch Next architecture")
    table(d, ["From", "To", "Built?"],
          [[DP.META[n]["number"], D.WATCH_NEXT[n][0],
            "locked V12" if n == 15 else
            ("locked V13" if n in (17, 22) else "in this pack")]
           for n in VIDEOS], widths=[0.7, 4.4, 1.6])
    callout(d, "V22 routes to the locked V13 and NOT to an unbuilt V23. That is a deliberate "
               "choice and it is the one worth reviewing: V22 is the structural diagnosis, and "
               "the episode that most naturally follows it is V23, which does not exist. Sending "
               "the viewer back to V13 keeps the promise honest, but it does route a viewer who "
               "has just been told the ladder is shorter toward a video about changing industry. "
               "If Temidayo would rather V22 close without a Watch Next at all, that is a one "
               "line change in the master, the card and the description.")

    h(d, "Resources, and where there is none")
    table(d, ["#", "Resource", "Why"],
          [[DP.META[n]["number"],
            D.RESOURCE[n][1] if n in D.RESOURCE else "None",
            {15: "One piece of work whose judgment left no record.",
             16: "The viewer leaves needing to tell two situations apart, not needing a product.",
             17: "The system is exactly the problem.",
             18: "Testing one destination.",
             19: "Naming which of three possibilities you have matches no offer.",
             20: "Recognition. Do not sell to somebody who has just been told there is no next role.",
             21: "Growth has to be redefined against a direction.",
             22: "Diagnosis. Give the read and stop."}[n]]
           for n in VIDEOS], widths=[0.5, 1.9, 4.3])
    para(d, D.URLS_CARRIED and "Four URLs are carried from the locked pack and three are used: "
            "career-evidence-starter, keep-the-proof and fieldkit. career-decisions is carried "
            "and unused, because no video here earns it out loud. Career Move Review still has "
            "no page and no URL anywhere in the workspace and is not referenced.")

    page_break(d)
    h(d, "What each video is bounded by")
    for n in VIDEOS:
        sub(d, "%s  \u00b7  %s" % (DP.META[n]["number"], DP.META[n]["title"]))
        for role, name, note in PV.SOURCES[n]:
            if role == "BOUNDARY":
                kv(d, "Boundary", name)
                para(d, note)

    page_break(d)
    h(d, "Claims deliberately removed or never made")
    bullets(d, [
      "No claim that AI is taking the value of experience. V15 refuses it on camera and the "
      "payroll evidence in the source of record runs the other way.",
      "No claim that middle management is dead or dying. The source of record says that "
      "overstates the case, and V20 and V22 both quote the phrase only in order to refuse it.",
      "No search-demand, search-volume or trend claim of any kind, in a title, a thumbnail, a "
      "tag, a description or a spoken line. Every search figure is Unknown in the source of "
      "record, and an Unknown stays unfilled.",
      "No skills-based-hiring claim. The source records that the practice changed fewer than one "
      "hire in 700 in 2023, so no video tells a viewer that a dropped degree requirement opens a "
      "door.",
      "No displacement-earnings figure in V17. It is true, it is cited, and it is of no use to "
      "somebody who was laid off this week. Recorded in the provenance as considered and set "
      "aside.",
      "No employer named in any public asset. No job posting is read in any of these eight "
      "videos, so the V13 and V14 situation does not arise.",
      "No new public framework. The three kinds in V18, the three possibilities in V19 and the "
      "seven things in V20 are never numbered on a card, never named and never boxed as a set.",
    ])

    h(d, "Evidence source of record")
    kv(d, "File", PV.EVIDENCE_OF_RECORD["name"])
    kv(d, "SHA-256", PV.EVIDENCE_OF_RECORD["sha"])
    kv(d, "Size", PV.EVIDENCE_OF_RECORD["size"])
    kv(d, "Shape", PV.EVIDENCE_OF_RECORD["shape"])
    para(d, PV.EVIDENCE_OF_RECORD["note"])
    caption(d, "The full class table and every claim considered and set aside are in "
               "00_MISSING_RUNG_EVIDENCE_BOUNDARIES.")

    h(d, "Scripture verification status")
    callout(d, PV.SCRIPTURE)

    h(d, "QA actually performed")
    kv(d, "Checks run against the built files",
       "%d" % sum(1 for r in rows if r["state"] == QA.PERFORMED))
    kv(d, "Passing", "%d" % sum(1 for r in rows if r["ok"]))
    kv(d, "Script-level checks run against the modules", "%d" % len(CH.FAILS))
    table(d, ["#", "Check", "Result"],
          [["%02d" % r["n"], r["name"], "pass" if r["ok"] else "FAIL"] for r in rows],
          widths=[0.45, 5.3, 0.95])
    para(d, "These ran against the documents in this pack, not against the source modules. The "
            "full detail, and the list of what was not performed, is in "
            "00_V15-V22_FINAL_QA_REPORT.")

    page_break(d)
    h(d, "Still requiring Temidayo's decision")
    for name, why in OPEN:
        sub(d, name)
        para(d, why)

    h(d, "Future roadmap: recorded, NOT built")
    callout(d, "Nothing below exists in this pack or anywhere in the workspace. It is written "
               "down so the next pass starts from a decision rather than from a fresh argument. "
               "The instruction for this build was to stop at V22, and it stopped at V22.")
    table(d, ["#", "What it becomes", "What carries, and what does not"],
          [[a, b, c] for a, b, c in FUTURE], widths=[0.5, 1.9, 4.3])
    callout(d, "Nothing in this pack is described as production ready. Four items above are open, "
               "and the scripture wording is the one that blocks publication.")
    footer_note(d, "Every figure in this report is read from the build at generation time.")
    d.save(path)

def evidence_doc(path):
    d = base_doc()
    title_block(d, EYEBROW, "Missing Rung evidence boundaries",
                "What the source supports, what it does not, and what stays unfilled")
    kv(d, "Generated", STAMP)
    kv(d, "Applies to", "V15 to V22. Nothing here authorizes a claim in any other video.")
    callout(d, PV.CLASS_NOTE)

    h(d, "The classes, in the source report's own words")
    table(d, ["Class", "The report's definition"],
          [[a, b] for a, b in PV.CLASS_DEFINITIONS], widths=[1.3, 5.4])

    h(d, "Evidence source of record")
    kv(d, "File", PV.EVIDENCE_OF_RECORD["name"])
    kv(d, "Where", PV.EVIDENCE_OF_RECORD["where"])
    kv(d, "SHA-256", PV.EVIDENCE_OF_RECORD["sha"])
    kv(d, "Size", PV.EVIDENCE_OF_RECORD["size"])
    kv(d, "Shape", PV.EVIDENCE_OF_RECORD["shape"])
    para(d, PV.EVIDENCE_OF_RECORD["note"])

    page_break(d)
    h(d, "Every claim this pack takes from the report")
    caption(d, "The class beside each claim is the class the REPORT gave it. Nothing here "
               "upgrades one class into another.")
    for c in PV.CLAIMS:
        sub(d, "%s  \u00b7  %s  \u00b7  %s" % (
            c["id"], c["report_class"],
            ("spoken in " + ", ".join("V%d" % x for x in c["spoken"]))
            if c["spoken"] else "NOT SPOKEN"))
        para(d, c["claim"])
        kv(d, "Cited by the report as", c["source"])
        para(d, c["carried"])

    page_break(d)
    h(d, "What the source could not establish")
    table(d, ["Area", "What the report says"],
          [[a, b] for a, b in PV.UNKNOWNS], widths=[1.8, 4.9])
    callout(d, PV.UNKNOWN_RULE)

    h(d, "Constructed artifacts")
    para(d, PV.CONSTRUCTED_NOTE)
    table(d, ["Video", "Card", "On-card label"],
          [["V%d" % n, cid, label] for n, cid, _desc, label, _note in PV.CONSTRUCTED],
          widths=[0.6, 2.6, 3.5])

    h(d, "Employers")
    para(d, PV.EMPLOYERS)

    h(d, "Viewer-facing scope")
    para(d, PV.VIEWER_FACING_SCOPE)

    h(d, "URLs")
    para(d, PV.URLS)

    h(d, "What this evidence cannot establish")
    bullets(d, PV.LIMITS)
    footer_note(d, "%d claims carried, %d of them spoken. %d areas recorded as Unknown and left "
                   "unfilled." % (len(PV.CLAIMS),
                                  sum(1 for c in PV.CLAIMS if c["spoken"]), len(PV.UNKNOWNS)))
    d.save(path)

def thumbnail_doc(path):
    d = base_doc()
    title_block(d, EYEBROW, "V20 thumbnail decision",
                "Three candidates, one recommendation, pending approval")
    kv(d, "Generated", STAMP)
    kv(d, "Video", PK.V20_TITLE)
    kv(d, "Title status", "LOCKED. Not reopened in this document.")
    callout(d, PK.STATUS)

    h(d, "Candidates")
    table(d, ["#", "Line", "Why it works", "What it risks"],
          [[str(c["rank"]), c["line"], c["why"], c["risk"]] for c in PK.CANDIDATES],
          widths=[0.35, 1.5, 2.6, 2.25])
    for c in PK.CANDIDATES:
        sub(d, "%d.  %s" % (c["rank"], c["line"]))
        kv(d, "Why", c["why"])
        kv(d, "Risk", c["risk"])

    h(d, "Recommendation")
    callout(d, PK.RECOMMENDATION)

    h(d, "Ruled out, and why")
    for line, why in PK.RULED_OUT:
        sub(d, line)
        para(d, why)

    h(d, "Scope of this document")
    para(d, PK.NOT_REOPENED)
    footer_note(d, "Three candidates. One recommendation. No fourth option was developed, and no "
                   "other packaging decision is open in this pack.")
    d.save(path)

def qa_doc(path, ctx):
    rows = QA.run(ctx)
    d = base_doc()
    title_block(d, EYEBROW, "QA report",
                "%d items, run against the files in this pack" % len(QA.ITEMS))
    kv(d, "Generated", STAMP)
    kv(d, "Items run", "%d" % sum(1 for r in rows if r["state"] == QA.PERFORMED))
    kv(d, "Items passing", "%d" % sum(1 for r in rows if r["ok"]))
    callout(d, "These checks were actually executed against the built documents on disk, "
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

FIXED = (2026, 9, 23, 0, 0, 0)

def normalize(path):
    """Rewrite a .docx so two builds of the same content produce the same bytes.

    python-docx stamps each entry with the current time and sets core properties from
    the clock, so an untouched pack would hash differently every run. Entry order is
    preserved; only the timestamps are fixed.
    """
    import re as _re, shutil, tempfile
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    stamp = "2026-09-23T00:00:00Z"
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
    import shutil
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE, exist_ok=True)

    def full(rel):
        q = os.path.join(STAGE, rel)
        os.makedirs(os.path.dirname(q) or STAGE, exist_ok=True)
        return q

    for n in VIDEOS:
        DP.recording_master(full(FILES[(n, "master")]), n)
        DP.thought_blocks(full(FILES[(n, "blocks")]), n)
        DP.production_package(full(FILES[(n, "prod")]), n)
        DP.shorts_doc(full(FILES[(n, "shorts")]), n)
        DP.description_doc(full(FILES[(n, "desc")]), n)
        DP.provenance_doc(full(FILES[(n, "prov")]), n)
    evidence_doc(full(EVIDDOC))
    thumbnail_doc(full(THUMBDOC))
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
