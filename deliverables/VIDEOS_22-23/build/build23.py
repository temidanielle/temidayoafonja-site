# -*- coding: utf-8 -*-
"""Build the V22 and V23 production packages."""
import os, sys, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")

import rdeck
from rdeck import render_html, shoot
import masters23 as M
import frames23 as F
import spine23 as SP
import svg23
import geocheck23 as G
import recdocs23 as REC
import prodocs23 as PRO
import riverside23 as RIV
import shorts23 as SH
import shortsdocs23 as SD
import publish23 as PUB
import exercise23 as EX
import evidence23 as EV
import qa23 as QA
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, mono, hr, head)

SUB = ["00_Source_Hierarchy", "01_Recording", "02_Run_of_Show",
       "03_Riverside", "04_Visual_Assets", "05_Shorts", "06_Publishing",
       "07_Evidence", "08_QA"]
ZIP_DT = (2026, 9, 13, 0, 0, 0)
ARCHIVE = "YouTube_V22-V23_FINAL_Production_Packages_2026-09-13.zip"


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


def zip_dir(src, path):
    names = []
    for root, _, files in os.walk(src):
        for f in files:
            names.append(os.path.join(root, f))
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(names):
            zi = zipfile.ZipInfo(os.path.relpath(f, os.path.dirname(src)),
                                 date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(f, "rb") as fh:
                z.writestr(zi, fh.read())
    return path


def visuals(n, pkg, st):
    """Render every state to PNG, and to SVG where a designer may need it."""
    vis = os.path.join(pkg, "04_Visual_Assets")
    os.makedirs(vis, exist_ok=True)
    titles = PUB.watch_next_titles()
    wn = F.watch_next_cards(n, [(dst, titles[dst])
                                for dst, _ in PUB.WATCH_NEXT[n]])
    cards, names = G.cards_for(n)
    for f in wn:
        for stt in f["states"]:
            c = rdeck.Card(len(cards) + 1, stt["name"] + ".png")
            stt["draw"](c)
            cards.append(c)
            names.append(stt["name"] + ".png")
    html = render_html(cards, os.path.join(vis, "_%d_preview.html" % n),
                       "V%d assets" % n)
    made = shoot(html, vis, names)
    os.remove(html)
    svgs = []
    idx = {nm[:-4]: c for nm, c in zip(names, cards)}
    for f in F.SETS[n]:
        if not f["svg"]:
            continue
        s = f["states"][0]
        svgs.append(svg23.write(idx[s["name"]],
                                os.path.join(vis, s["name"] + ".svg"),
                                "%s  %s" % (M.title(n), s["name"])))
    return made, svgs, wn


def package(n, st):
    pkg = os.path.join(OUT, "V%d" % n)
    if os.path.isdir(pkg):
        shutil.rmtree(pkg)
    for s in SUB:
        os.makedirs(os.path.join(pkg, s))
    P = lambda s, f: os.path.join(pkg, s, f)

    EV.hierarchy(P("00_Source_Hierarchy", "Source_Hierarchy_and_Manifest.txt"),
                 st)
    REC.master(n, P("01_Recording", "Recording_Master.docx"), st)
    REC.blocks(n, P("01_Recording", "Thought_Block_Recording_Copy.docx"), st)
    PRO.run_of_show(n, P("02_Run_of_Show", "Run_of_Show.docx"), st)
    RIV.prompt(n, P("03_Riverside",
                    "Riverside_CoCreator_Master_Prompt.txt"), st)
    PRO.camera_map(n, P("03_Riverside", "Camera_and_Full_Screen_Map.txt"))
    PRO.motion_map(n, P("03_Riverside", "Motion_and_Reveal_Map.txt"))
    PRO.sound_map(n, P("03_Riverside", "Audio_and_Sound_Cue_Map.txt"))
    PRO.broll(n, P("03_Riverside", "B_Roll_Recommendations.txt"))

    made, svgs, wn = visuals(n, pkg, st)
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


def qa_report(n, path, st, results, geo, made, svgs):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "QA report")
    kv(d, "Generated", st)
    ok = sum(1 for _, o, _ in results if o)
    kv(d, "Checks run", "%d" % len(results))
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (len(results) - ok))
    kv(d, "Cards", "%d in %d states" % (len(F.SETS[n]), len(F.states(n))))
    kv(d, "Images", "%d PNG at 1920 x 1080, %d editable SVG"
       % (len(made), len(svgs)))
    kv(d, "Geometry", "%d problems against the rendered DOM" % len(geo))
    cam, full = SP.counts(n)
    kv(d, "Spine", "%d camera stretches against %d full-screen cues"
       % (cam, full))
    kv(d, "Spoken words", format(M.word_count(n), ","))
    callout(d, "No spoken wording was changed. Every figure here is "
               "arithmetic on the approved script; nothing has been "
               "recorded, edited or exported.")
    h(d, "Every check")
    table(d, ["Check", "", "Detail"],
          [[nm, "pass" if o else "FAIL", str(dd)[:150]]
           for nm, o, dd in results],
          widths=[2.7, 0.5, 3.5], size=8)
    footer_note(d, "Runtime, chapters, SRT timing and thumbnail artwork are "
                   "decided after the final edit.")
    d.save(path)
    return path


def publishing(n, path, st):
    titles = PUB.watch_next_titles()
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Publishing materials")
    kv(d, "Final title", M.title(n))
    kv(d, "Locked thumbnail text", M.thumbnail(n))
    kv(d, "Playlist", PUB.PLAYLIST)
    kv(d, "Generated", st)
    callout(d, "Chapters: create after the final edit, from actual export "
               "timing.  SRT: generate in Riverside after the final edit and "
               "verify against the final export. Neither exists in this "
               "package.")
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


def shared(st, results, archives):
    sh = os.path.join(OUT, "Shared")
    if os.path.isdir(sh):
        shutil.rmtree(sh)
    os.makedirs(sh)
    EV.hierarchy(os.path.join(sh, "Source_Hierarchy.txt"), st)
    changelog(os.path.join(sh,
              "V22-V23_MASTER_CHANGELOG_AND_SOURCE_HIERARCHY.docx"), st)
    qa_summary(os.path.join(sh, "V22-V23_PACKAGE_QA_SUMMARY.docx"), st,
               results)
    return sh


def changelog(path, st):
    d = base_doc()
    title_block(d, "capability formation | v22 and v23",
                "Master changelog and source hierarchy",
                "What was built, from what, and what was left alone")
    kv(d, "Generated", st)
    kv(d, "Input archive", "V22_V23_CODE_BUILD_INPUTS_2026-09-13.zip")
    kv(d, "Input SHA-256", M.INPUT_ZIP_SHA)
    callout(d, "No spoken wording was changed in either script. Every "
               "conflict between a source and the production layer was "
               "resolved in the production layer.")
    h(d, "Order of authority")
    table(d, ["", "Source", "Authoritative for"],
          [["1", "V22 UPDATED 50CHAR script",
            "V22 title, thumbnail, spoken wording, editorial sequence, CTA"],
           ["2", "V23 UPDATED 50CHAR script", "The same, for V23"],
           ["3", "V22 and V23 Advisor Overview",
            "Editorial rationale, the distinction between the videos, and "
            "preserved boundaries. Never the exact spoken wording."],
           ["4", "Internal Source Capture Packet",
            "Provenance, employer evidence, research boundaries, source "
            "presentation, anonymization, synthetic-example rules"],
           ["5", "Visual reference screenshots",
            "Information-design principles only"]],
          widths=[0.4, 2.3, 4.0], size=8.5)
    h(d, "Superseded, and absent from everything built")
    bullets(d, list(M.SUPERSEDED_TITLES)
            + ["Thumbnail: %s" % M.SUPERSEDED_THUMBNAIL,
               "Older Video A and Video B scripts as current spoken source"])
    h(d, "What the two videos do")
    table(d, ["", "V22", "V23"],
          [["Title", M.title(22), M.title(23)],
           ["Thumbnail", M.thumbnail(22), M.thumbnail(23)],
           ["Editorial job", "Read the destination more accurately",
            "Reconstruct your evidence more accurately"],
           ["Method", "Problem. Authority. Proof. Real gap.",
            "Problem before. What was mine to decide. Judgment. Proof and "
            "how I know."],
           ["Spoken words", format(M.word_count(22), ","),
            format(M.word_count(23), ",")],
           ["CTA", "One ask. No product.",
            "One action and one resource."]],
          widths=[1.1, 2.8, 2.8], size=8.5)
    h(d, "What was taken from the visual references")
    bullets(d, [
      "A large artifact beside a narrow explainer panel, with the panel "
      "carrying only the idea being taught at that moment.",
      "Numbered teaching points revealed one at a time, warm when active "
      "and quiet when not.",
      "Side-by-side contrast used only where the contrast teaches.",
      "One active idea at a time, after the whole structure is established.",
    ])
    h(d, "What was not taken")
    bullets(d, [
      "No branding, color system, product interface, icon set, layout or "
      "visual identity from the references.",
      "No fake buttons, progress bars, quiz interfaces or dashboards. The "
      "reveals are sequential because YouTube is not interactive.",
    ])
    h(d, "Decisions recorded rather than resolved")
    bullets(d, [
      "The capture packet quotes the pre-advisor draft under 'exact lines "
      "used in the script'. The updated 50CHAR script is the wording of "
      "record. The evidence in the packet, its presentation rules and its "
      "boundaries all still govern. Neither source was edited.",
      "The script describes several employers generically while the packet "
      "and the build brief require them named on camera. The spoken wording "
      "was left exactly as approved and the employer names appear on the "
      "artifact cards, which is the production layer doing the work.",
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
              [[nm, "pass" if o else "FAIL",
                str(dd)[:180]] for nm, o, dd in results[n]],
              widths=[2.7, 0.5, 3.5], size=8)
    footer_note(d, "Every figure in this package is arithmetic on the "
                   "approved script. Nothing here has been recorded, edited "
                   "or exported.")
    d.save(path)
    return path


def main():
    st = stamp()
    print("stamp:", st)
    for rel, sha, _ in M.manifest():
        pass
    print("input archive sha256 verified:",
          M.INPUT_ZIP_SHA == sha256(os.path.join(
              OUT, "_source", "V22_V23_CODE_BUILD_INPUTS_2026-09-13.zip")))

    results, pkgs, archives = {}, {}, []
    for n in M.VIDEOS:
        geo, _, _, _ = G.check(n)
        pkg, made, svgs, wn = package(n, st)
        QA.run(n, pkg, geo, made)                 # first pass, before report
        qa_report(n, os.path.join(pkg, "08_QA", "QA_Report.docx"), st,
                  QA.run(n, pkg, geo, made), geo, made, svgs)
        results[n] = QA.run(n, pkg, geo, made)    # final pass, report included
        bad = [x for x in results[n] if not x[1]]
        print("V%-3d %2d/%2d checks   %2d png   %d svg   %s"
              % (n, len(results[n]) - len(bad), len(results[n]),
                 len(made), len(svgs),
                 "OK" if not bad else "FAILURES"))
        for nm, o, dd in bad:
            print("      FAIL  %s  ->  %s" % (nm, dd))
        pkgs[n] = pkg

    sh = shared(st, results, archives)

    zpath = os.path.join(OUT, ARCHIVE)
    tmp = os.path.join(OUT, "_stage")
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)
    for n in M.VIDEOS:
        shutil.copytree(pkgs[n], os.path.join(tmp, "V%d" % n))
    shutil.copytree(sh, os.path.join(tmp, "Shared"))
    names = []
    for root, _, files in os.walk(tmp):
        for f in files:
            names.append(os.path.join(root, f))
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for f in sorted(names):
            zi = zipfile.ZipInfo(os.path.relpath(f, tmp), date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(f, "rb") as fh:
                z.writestr(zi, fh.read())
    shutil.rmtree(tmp)
    digest = sha256(zpath)
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (digest, ARCHIVE))

    tot = sum(len(r) for r in results.values())
    ok = sum(1 for r in results.values() for _, o, _ in r if o)
    with zipfile.ZipFile(zpath) as z:
        entries = len(z.namelist())
    print("\n  %s" % ARCHIVE)
    print("  sha256 %s" % digest)
    print("  %d entries" % entries)
    print("  package checks: %d of %d passed" % (ok, tot))
    return ok == tot


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
