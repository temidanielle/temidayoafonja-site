# -*- coding: utf-8 -*-
"""Build the re-anchored V22 and V23 packages as version 2.

The prior archive is not overwritten. This writes V22_v2 and V23_v2 beside
it and a new outer archive with the _v2 name.
"""
import os, sys, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")

import rdeck
from rdeck import render_html, shoot
import masters23b as M
import frames23b as F
import spine23b as SP
import svg23
import geocheck23b as G
import reuse23b as RU
import recdocs23b as REC
import prodocs23b as PRO
import riverside23b as RIV
import shorts23b as SH
import shortsdocs23b as SD
import publish23b as PUB
import exercise23b as EX
import evidence23b as EV
import qa23b as QA
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, mono, hr, head)

SUB = ["00_Source_Hierarchy", "01_Recording", "02_Run_of_Show",
       "03_Riverside", "04_Visual_Assets", "05_Shorts", "06_Publishing",
       "07_Evidence", "08_QA"]
ZIP_DT = (2026, 9, 13, 0, 0, 0)
ARCHIVE = "YouTube_V22-V23_FINAL_Production_Packages_2026-09-13_v2.zip"
PRIOR = "YouTube_V22-V23_FINAL_Production_Packages_2026-09-13.zip"


def stamp():
    return subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def visuals(n, pkg):
    vis = os.path.join(pkg, "04_Visual_Assets")
    os.makedirs(vis, exist_ok=True)
    titles = PUB.watch_next_titles()
    wn = F.watch_next_cards(n, [(d, titles[d]) for d, _ in PUB.WATCH_NEXT[n]])
    cards, names = G.cards_for(n, wn)
    html = render_html(cards, os.path.join(vis, "_%d.html" % n), "V%d" % n)
    made = shoot(html, vis, names)
    os.remove(html)
    idx = {nm[:-4]: c for nm, c in zip(names, cards)}
    svgs = []
    for f in F.SETS[n]:
        if f["svg"]:
            s = f["states"][0]
            svgs.append(svg23.write(idx[s["name"]],
                                    os.path.join(vis, s["name"] + ".svg"),
                                    "%s  %s" % (M.title(n), s["name"])))
    return made, svgs, wn


def publishing(n, path, st):
    titles = PUB.watch_next_titles()
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Publishing materials")
    kv(d, "Final title", M.title(n))
    kv(d, "Locked thumbnail text", M.script_header_thumbnail(n))
    kv(d, "Playlist", PUB.PLAYLIST)
    kv(d, "Generated", st)
    callout(d, "Chapters: create after the final edit, from actual export "
               "timing. The script carries no timing markers to copy.  SRT: "
               "generate in Riverside after the final edit and verify "
               "against the final export. Neither exists in this package.")
    h(d, "Description")
    for line in PUB.description(n, titles):
        para(d, line, size=10.5, after=6)
    h(d, "Pinned comment")
    para(d, PUB.pinned(n), size=10.5)
    h(d, "Watch next")
    para(d, "Two existing destinations from V4 to V21, recommended for "
            "launch day. Neither needs a change to the spoken script: the "
            "Watch Next card is a silent full-screen end card.", size=10.5)
    table(d, ["Destination", "Title", "Why this one"],
          [["V%d" % dst, titles[dst], why]
           for dst, why in PUB.WATCH_NEXT[n]],
          widths=[0.8, 2.2, 3.7], size=8.5)
    if PUB.FUTURE[n]:
        dst, why = PUB.FUTURE[n]
        sub(d, "Future option")
        para(d, "V%d, %s. %s" % (dst, M.title(dst), why), size=10.5)
    h(d, "Search language")
    para(d, "Discovery input only. None of this changes the title, the "
            "thumbnail or a spoken line.", size=10)
    bullets(d, PUB.KEYWORDS[n], size=10)
    h(d, "Shorts selection bank")
    table(d, ["Candidate", "Stop scroll", "About"],
          [[r["key"].split("_", 2)[2].replace("_", " "), r["hook"],
            "0:%02d" % r["secs"]] for r in SH.rows(n)],
          widths=[2.4, 3.3, 0.9], size=8.5)
    caption(d, "Current cadence is about three Shorts per long-form video.")
    h(d, "Upload QA checklist")
    bullets(d, PUB.UPLOAD_QA, size=10)
    footer_note(d, "No public URL in this package is a live link except the "
                   "resource route, which the V4 to V21 system already "
                   "locked.")
    d.save(path)
    return path


def qa_report(n, path, st, rows, geo, made, svgs):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n), "QA report")
    kv(d, "Generated", st)
    ok = sum(1 for _, o, _ in rows if o)
    kv(d, "Checks run", "%d" % len(rows))
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (len(rows) - ok))
    kv(d, "Cards", "%d active families in %d states"
       % (len(F.SETS[n]), len(F.states(n))))
    kv(d, "Images", "%d PNG at 1920 x 1080, %d editable SVG"
       % (len(made), len(svgs)))
    kv(d, "Geometry", "%d problems against the rendered DOM" % len(geo))
    cam, full = SP.counts(n)
    kv(d, "Spine", "%d camera stretches against %d full-screen cues"
       % (cam, full))
    kv(d, "Spoken words", "%s by whitespace count, %s as supplied"
       % (format(M.word_count(n), ","), format(M.DECLARED_WORDS[n], ",")))
    callout(d, "No spoken wording was changed. Every figure here is "
               "arithmetic on the approved script; nothing has been "
               "recorded, edited or exported.")
    h(d, "Every check")
    table(d, ["Check", "", "Detail"],
          [[nm, "pass" if o else "FAIL", str(dd)[:150]]
           for nm, o, dd in rows],
          widths=[2.7, 0.5, 3.5], size=8)
    d.save(path)
    return path


def package(n, st, reuse_rows):
    pkg = os.path.join(OUT, "V%d_v2" % n)
    if os.path.isdir(pkg):
        shutil.rmtree(pkg)
    for s in SUB:
        os.makedirs(os.path.join(pkg, s))
    P = lambda s, f: os.path.join(pkg, s, f)
    prior = sha256(os.path.join(OUT, PRIOR)) if os.path.exists(
        os.path.join(OUT, PRIOR)) else "not present"

    EV.hierarchy(P("00_Source_Hierarchy",
                   "Source_Hierarchy_and_Manifest.txt"), st, prior)
    REC.master(n, P("01_Recording", "Recording_Master.docx"), st)
    REC.blocks(n, P("01_Recording", "Thought_Block_Recording_Copy.docx"), st)
    PRO.run_of_show(n, P("02_Run_of_Show", "Run_of_Show.docx"), st)
    RIV.prompt(n, P("03_Riverside",
                    "Riverside_CoCreator_Master_Prompt.txt"), st)
    PRO.camera_map(n, P("03_Riverside", "Camera_and_Full_Screen_Map.txt"))
    PRO.motion_map(n, P("03_Riverside", "Motion_and_Reveal_Map.txt"))
    PRO.sound_map(n, P("03_Riverside", "Audio_and_Sound_Cue_Map.txt"))
    PRO.broll(n, P("03_Riverside", "B_Roll_Recommendations.txt"))

    made, svgs, wn = visuals(n, pkg)
    PRO.asset_index(n, P("04_Visual_Assets", "Asset_Index.txt"),
                    [os.path.basename(x) for x in made + svgs], wn)

    SD.bank(n, P("05_Shorts", "Six_Candidate_Shorts.docx"), st)
    ind = os.path.join(pkg, "05_Shorts", "Individual")
    os.makedirs(ind)
    for r in SH.rows(n):
        SD.single(n, r, os.path.join(ind, r["key"] + ".docx"), st)
    SD.editor_notes(n, P("05_Shorts", "Shorts_Editor_Instructions.txt"))

    publishing(n, P("06_Publishing", "Publishing_Materials.docx"), st)
    EX.build(n, P("06_Publishing", "Viewer_Exercise.docx"), st)
    EV.source_notes(n, P("07_Evidence", "Source_and_Evidence_Notes.docx"), st)
    EV.claim_notes(n, P("07_Evidence", "Claim_Boundary_Notes.docx"), st)
    return pkg, made, svgs, wn


def changelog(path, st, reuse_rows, prior):
    d = base_doc()
    title_block(d, "capability formation | v22 and v23",
                "Master changelog and source hierarchy",
                "Synchronization pass against the September 13 FINAL scripts")
    kv(d, "Generated", st)
    kv(d, "Prior archive", PRIOR)
    kv(d, "Prior SHA-256", prior)
    callout(d, "No spoken wording was changed in either script. This is a "
               "synchronization pass: the production layer was re-anchored "
               "to the new spoken text, not rewritten editorially.")
    h(d, "What superseded what")
    table(d, ["", "Was", "Now"],
          [["V22 title", "How to Decode a Job Description", M.title(22)],
           ["V22 thumbnail", "IGNORE THE TITLE",
            M.script_header_thumbnail(22)],
           ["V22 spoken words", "1,345", "%d by whitespace count, %d as "
            "supplied" % (M.word_count(22), M.DECLARED_WORDS[22])],
           ["V23 title", "Turn One Accomplishment Into Career Proof",
            M.title(23)],
           ["V23 thumbnail", "YOU DID IT. CAN YOU PROVE IT?",
            M.script_header_thumbnail(23)],
           ["V23 spoken words", "1,132", "%d" % M.word_count(23)]],
          widths=[1.2, 2.6, 2.9], size=8.5)
    caption(d, "The wording in the Was column is recorded here because this "
               "is the changelog. It appears in no active production "
               "document, which QA checks.")

    h(d, "Why the production layer was re-anchored rather than renamed")
    para(d, "Only 3 of the previous 37 full-screen trigger sentences survive "
            "the new scripts verbatim. The section order changed materially "
            "in V22, where the real-gap section now comes before the "
            "Director comparison and the reversal. The spine was rebuilt "
            "around the new order and every cue re-anchored to a sentence "
            "the new script actually speaks.", size=10.5)

    h(d, "Assets, by what actually happened to the bytes")
    for cls in (F.REUSE, F.COPY, F.REBUILD, F.NEW):
        rows = [r for r in reuse_rows if r[3] == cls]
        if not rows:
            continue
        sub(d, "%s  (%d)" % (cls, len(rows)))
        table(d, ["V", "Family", "Measured"],
              [["V%d" % r[0], r[1], r[4]] for r in rows],
              widths=[0.5, 2.4, 3.8], size=8)
    sub(d, "RETIRED  (%d)" % len(F.RETIRED))
    table(d, ["Family", "Why it has no cue in the new script"],
          [[k, v] for k, v in sorted(F.RETIRED.items())],
          widths=[2.4, 4.3], size=8)
    caption(d, "A family is REUSE only if every state renders byte for byte "
               "identical to the file the previous package shipped. REBUILD "
               "means the layout function changed, which is measured by "
               "watching which layout each family draws with.")

    h(d, "Decisions recorded rather than resolved")
    bullets(d, [
      "The supplied word counts are V22 982 and V23 895. Whitespace "
      "tokenization gives V22 978 and V23 895. The V22 difference is exactly "
      "the four currency figures in the script, counted as two tokens each "
      "when the symbol is separated from the numeral. V23 has no currency "
      "figure, which is why the two methods agree there. Nothing was "
      "changed and both figures are carried.",
      "The capture packet quotes an earlier draft under 'exact lines used in "
      "the script'. The September 13 FINAL script is the wording of record. "
      "The packet's evidence, presentation rules and boundaries all still "
      "govern, and neither source was edited.",
      "The V23 same-employer comparison is retired from the active edit "
      "because the new script does not use it. The evidence is preserved in "
      "the evidence notes, still anonymized.",
    ])
    footer_note(d, "Runtime, chapters, SRT timing and thumbnail artwork are "
                   "all decided after the final edit, not here.")
    d.save(path)
    return path


def qa_summary(path, st, results):
    d = base_doc()
    title_block(d, "capability formation | v22 and v23",
                "Package QA summary", "Every check, and what it measured")
    kv(d, "Generated", st)
    tot = sum(len(r) for r in results.values())
    ok = sum(1 for r in results.values() for _, o, _ in r if o)
    kv(d, "Checks run", "%d" % tot)
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (tot - ok))
    for n in M.VIDEOS:
        h(d, "V%d  %s" % (n, M.title(n)))
        table(d, ["Check", "", "Detail"],
              [[nm, "pass" if o else "FAIL", str(dd)[:180]]
               for nm, o, dd in results[n]],
              widths=[2.7, 0.5, 3.5], size=8)
    footer_note(d, "Every figure in this package is arithmetic on the "
                   "approved script. Nothing here has been recorded, edited "
                   "or exported.")
    d.save(path)
    return path


def main():
    st = stamp()
    print("stamp:", st)
    ok, bad = M.verify_counts()
    print("supplied word counts reproduced by whitespace count:", ok,
          "" if ok else bad)
    reuse_rows = RU.run()
    mm = [r for r in reuse_rows if r[2] != r[3]]
    print("reuse classes measured against the previous package: %d families, "
          "%d mismatches" % (len(reuse_rows), len(mm)))
    if mm:
        for r in mm:
            print("   ", r)
        raise SystemExit("reuse classification mismatch")

    prior = sha256(os.path.join(OUT, PRIOR))
    results, pkgs = {}, {}
    for n in M.VIDEOS:
        geo, _, _, _ = G.check(n)
        pkg, made, svgs, wn = package(n, st, reuse_rows)
        QA.run(n, pkg, geo, made, reuse_rows)
        qa_report(n, os.path.join(pkg, "08_QA", "QA_Report.docx"), st,
                  QA.run(n, pkg, geo, made, reuse_rows), geo, made, svgs)
        results[n] = QA.run(n, pkg, geo, made, reuse_rows)
        f = [x for x in results[n] if not x[1]]
        print("V%-3d %2d/%2d checks   %2d png   %d svg   %s"
              % (n, len(results[n]) - len(f), len(results[n]), len(made),
                 len(svgs), "OK" if not f else "FAILURES"))
        for nm, o, dd in f:
            print("      FAIL  %s  ->  %s" % (nm, dd))
        pkgs[n] = pkg

    sh = os.path.join(OUT, "Shared_v2")
    if os.path.isdir(sh):
        shutil.rmtree(sh)
    os.makedirs(sh)
    EV.hierarchy(os.path.join(sh, "Source_Hierarchy.txt"), st, prior)
    changelog(os.path.join(
        sh, "V22-V23_MASTER_CHANGELOG_AND_SOURCE_HIERARCHY.docx"), st,
        reuse_rows, prior)
    qa_summary(os.path.join(sh, "V22-V23_PACKAGE_QA_SUMMARY.docx"), st,
               results)

    tmp = os.path.join(OUT, "_stage_v2")
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)
    for n in M.VIDEOS:
        shutil.copytree(pkgs[n], os.path.join(tmp, "V%d" % n))
    shutil.copytree(sh, os.path.join(tmp, "Shared"))
    names = []
    for root, _, files in os.walk(tmp):
        for f_ in files:
            names.append(os.path.join(root, f_))
    zpath = os.path.join(OUT, ARCHIVE)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for f_ in sorted(names):
            zi = zipfile.ZipInfo(os.path.relpath(f_, tmp), date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(f_, "rb") as fh:
                z.writestr(zi, fh.read())
    shutil.rmtree(tmp)
    digest = sha256(zpath)
    with open(zpath + ".sha256", "w") as f_:
        f_.write("%s  %s\n" % (digest, ARCHIVE))

    tot = sum(len(r) for r in results.values())
    passed = sum(1 for r in results.values() for _, o, _ in r if o)
    with zipfile.ZipFile(zpath) as z:
        entries = len(z.namelist())
    print("\n  %s" % ARCHIVE)
    print("  sha256 %s" % digest)
    print("  %d entries" % entries)
    print("  package checks: %d of %d passed" % (passed, tot))
    print("  prior archive preserved at %s" % prior)
    return passed == tot


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
