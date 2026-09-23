# -*- coding: utf-8 -*-
"""Assemble the V1, V2 and V3 production packages and one combined ZIP."""
import os, sys, zipfile, hashlib, shutil, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")

from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import st_docs as DP
import st_parse as P, st_frames as F, st_production as PR
import st_shorts as S, st_desc as D, st_prov as V, st_qa as QA
import st_render as R

STAGE = os.path.join(HERE, "_stage")
ZIPNAME = "CAPABILITY_FORMATION_V1-V3_REFRESH_PRODUCTION_PACK.zip"
EYEBROW, STAMP = DP.EYEBROW, DP.STAMP
VIDEOS = (1, 2, 3)

FIXED = (2026, 9, 23, 0, 0, 0)

def files(n):
    v = "V%d" % n
    return {
     "master": "%s/01_RECORDING/%s_FINAL_RECORDING_MASTER.docx" % (v, v),
     "blocks": "%s/01_RECORDING/%s_FINAL_THOUGHT_BLOCKS.docx" % (v, v),
     "prod":   "%s/02_PRODUCTION/%s_PRODUCTION_PACKAGE_AND_CUE_MAP.docx" % (v, v),
     "shorts": "%s/03_SHORTS/%s_THREE_CANDIDATE_SHORTS.docx" % (v, v),
     "desc":   "%s/05_PUBLISHING/%s_DESCRIPTION_AND_METADATA.docx" % (v, v),
     "prov":   "%s/06_PRIVATE/%s_SOURCE_AND_PROVENANCE.docx" % (v, v),
     "index":  "%s/04_VISUAL_ASSETS/%s_ASSET_INDEX.docx" % (v, v),
    }

OVERVIEW = "00_V1-V3_REFRESH_OVERVIEW.docx"
QADOC = "00_V1-V3_QA_REPORT.docx"

def overview(path, rows):
    d = base_doc()
    title_block(d, EYEBROW, "V1 to V3 refresh",
                "Built from the FINAL Sticky Realization masters")
    kv(d, "Generated", STAMP)
    kv(d, "Scope", "Three re-records. V4 and above were not opened for edit in "
                   "this build.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "The FINAL Sticky Realization masters supersede the earlier "
               "refreshed V1-V3 masters, and their thought blocks supersede "
               "the earlier blocks. The production build was not restarted: "
               "V1 reuses the approved flagship artifact sequence, and only "
               "the four card lines listed below were changed, each because "
               "the new spoken wording says something different.")

    h(d, "The three videos")
    table(d, ["#", "Title", "Thumbnail", "Spoken words", "145 wpm", "130 wpm"],
          [[DP.META[n]["number"], DP.META[n]["title"], DP.META[n]["thumb"],
            "{:,}".format(DP.words(n)), DP.runtime(n, 145), DP.runtime(n, 130)]
           for n in VIDEOS], widths=[0.4, 2.5, 1.5, 0.8, 0.75, 0.75])
    caption(d, "Word counts are exact, counted from the spoken stream of the "
               "supplied masters. Both runtime columns are ESTIMATES: they are "
               "arithmetic on the word count, not measurements. The finished "
               "edit will run longer because of full-screen holds.")

    h(d, "Seven-day memory architecture")
    caption(d, "Internal editorial QA. None of these four items is labelled or "
               "named in any video, on any card or in any description.")
    table(d, ["#", "Memory line, spoken", "Observable action"],
          [[DP.META[n]["number"], DP.MEMORY[n][0], DP.MEMORY[n][1]]
           for n in VIDEOS], widths=[0.4, 2.6, 3.7])

    h(d, "V1 reconciliation against the approved flagship sequence")
    para(d, "The eight flagship teaching slides are reused rather than "
            "replaced. Four card lines were changed, and only where the new "
            "spoken master says something the card did not.")
    table(d, ["Card", "Was", "Is now", "Why"],
          [[a, b, c, e] for a, b, c, e in F.V1_CARD_CHANGES],
          widths=[1.3, 1.8, 1.8, 1.8])

    h(d, "What is in each package")
    bullets(d, [
      "01_RECORDING: the final recording master with the editor cues inline, "
      "and the supplied thought blocks used exactly.",
      "02_PRODUCTION: the full cue map, every slide state with its pacing "
      "note, the run of show, and the CTA and Watch Next placement.",
      "03_SHORTS: three candidate Shorts, every line verbatim from the master.",
      "04_VISUAL_ASSETS: PNG for every state, SVG for the frames most likely "
      "to be re-timed, a phone-size contact sheet, and the asset index.",
      "05_PUBLISHING: description and metadata.",
      "06_PRIVATE: source checksums, provenance and evidence boundaries. Not "
      "for publication.",
    ])

    h(d, "Open items")
    for name, why in QA.NOT_DONE:
        sub(d, name)
        para(d, why)

    h(d, "QA actually performed")
    kv(d, "Checks run against the build", "%d" % len(rows))
    kv(d, "Passing", "%d" % sum(1 for r in rows if r["ok"]))
    table(d, ["#", "Check", "Result"],
          [["%02d" % r["n"], r["name"], "pass" if r["ok"] else "FAIL"]
           for r in rows], widths=[0.45, 5.3, 0.95])
    para(d, "Full detail, and the list of what was not performed, is in "
            "00_V1-V3_QA_REPORT.")
    footer_note(d, "Every figure in this report is read from the build at "
                   "generation time.")
    d.save(path)

def qa_doc(path, rows):
    d = base_doc()
    title_block(d, EYEBROW, "QA report",
                "%d checks, run against the build" % len(rows))
    kv(d, "Generated", STAMP)
    kv(d, "Items run", "%d" % len(rows))
    kv(d, "Items passing", "%d" % sum(1 for r in rows if r["ok"]))
    callout(d, "These checks were executed against the parsed masters, the "
               "rendered cards and the built copy, not against a description "
               "of them. Anything not performed is listed at the end instead "
               "of being counted here. Nothing in this pack is described as "
               "production ready.")
    table(d, ["#", "Check", "Result", "Detail"],
          [["%02d" % r["n"], r["name"], "pass" if r["ok"] else "FAIL", r["detail"]]
           for r in rows], widths=[0.4, 1.9, 0.55, 3.85])
    h(d, "Not performed, and why")
    for name, why in QA.NOT_DONE:
        sub(d, name)
        para(d, why)
    footer_note(d, "%d checks ran and %d passed. The work listed above is real "
                   "and is not covered by any result on this page."
                % (len(rows), sum(1 for r in rows if r["ok"])))
    d.save(path)

def normalize(path):
    """Rewrite a .docx so two builds of the same content produce the same bytes."""
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    stamp = "2026-09-23T00:00:00Z"
    out = []
    for info, data in items:
        if info.filename == "docProps/core.xml":
            t = data.decode("utf-8")
            t = re.sub(r"(<dcterms:(?:created|modified)[^>]*>)[^<]*(</dcterms:)",
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
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)

    def full(rel):
        q = os.path.join(STAGE, rel)
        os.makedirs(os.path.dirname(q), exist_ok=True)
        return q

    for n in VIDEOS:
        f = files(n)
        DP.recording_master(full(f["master"]), n)
        DP.thought_blocks(full(f["blocks"]), n)
        DP.production_package(full(f["prod"]), n)
        DP.shorts_doc(full(f["shorts"]), n)
        DP.description_doc(full(f["desc"]), n)
        DP.provenance_doc(full(f["prov"]), n)
        # visual assets are rendered into the deliverable tree, then copied in
        vis = R.vis_dir(n)
        pngs = sorted(os.path.join(vis, x) for x in os.listdir(vis)
                      if x.endswith(".png") and "Contact_Sheet" not in x)
        svgs = sorted(os.path.join(vis, x) for x in os.listdir(vis)
                      if x.endswith(".svg"))
        sheet = os.path.join(vis, "Phone_Size_Contact_Sheet.png")
        DP.asset_index(full(f["index"]), n, pngs, svgs, sheet)
        for src in pngs + svgs + [sheet]:
            shutil.copy2(src, full("V%d/04_VISUAL_ASSETS/%s"
                                   % (n, os.path.basename(src))))
        # editable source: the frame module that draws this video's cards
        shutil.copy2(os.path.join(HERE, "st_frames.py"),
                     full("V%d/04_VISUAL_ASSETS/_editable_source/st_frames.py" % n))
        shutil.copy2(os.path.join(HERE, "st_lay.py"),
                     full("V%d/04_VISUAL_ASSETS/_editable_source/st_lay.py" % n))

    rows = QA.run(None)
    qa_doc(full(QADOC), rows)
    overview(full(OVERVIEW), rows)

    names = sorted(os.path.relpath(os.path.join(r, fn), STAGE)
                   for r, _d, fs in os.walk(STAGE) for fn in fs)
    for rel in names:
        if rel.endswith(".docx"):
            normalize(os.path.join(STAGE, rel))
    zpath = os.path.join(OUT, ZIPNAME)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(STAGE, rel), "rb") as fh:
                z.writestr(zi, fh.read())
    with open(zpath + ".sha256", "w") as fh:
        fh.write("%s  %s\n" % (sha256(zpath), ZIPNAME))
    return zpath, names, rows

if __name__ == "__main__":
    zp, names, rows = main()
    bad = [r for r in rows if not r["ok"]]
    for r in bad:
        print(" FAIL %02d %s\n      %s" % (r["n"], r["name"], r["detail"][:200]))
    print("%d files" % len(names))
    print("%s\n%s" % (zp, sha256(zp)))
    print("QA: %d run, %d passed, %d failed" % (len(rows), len(rows) - len(bad), len(bad)))
