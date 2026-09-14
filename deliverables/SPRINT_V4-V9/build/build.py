# -*- coding: utf-8 -*-
"""Build the six NEW PUBLIC V4-V9 sprint production packages."""
import os, sys, math, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")

import rdeck
from rdeck import render_html, shoot
from PIL import Image
import svg23
import sprint as S
import frames as F
import spine as SP
import geocheck as G
import reuse as RU
import sdocs as D
import riverside as RIV
import sshorts as SH
import publish as PUB
import evidence as EV
import sqa as QA
from sdocs import (base_doc, title_block, h, kv, para, callout, sub, caption,
                   table, bullets, footer_note, EYEBROW)

SUB = ["00_SOURCE_HIERARCHY", "01_RECORDING", "02_RUN_OF_SHOW",
       "03_RIVERSIDE", "04_VISUAL_ASSETS", "05_SHORTS", "06_PUBLISHING",
       "07_EVIDENCE", "08_QA"]
ZIP_DT = (2026, 9, 13, 0, 0, 0)
ARCHIVE = ("YouTube_NEW_PUBLIC_V4-V9_TWO_WEEK_SPRINT_FINAL_Production_"
           "Packages_2026-09-13.zip")


def pkg_name(n):
    return "NEW_V%d_FORMER_V%d_Sprint_Production_Package" % (n, S.NUMBERS[n])


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


def contact_sheet(paths, path, cols=6, w=190):
    h_ = int(w * 1080 / 1920.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 10,
                           rows * h_ + (rows + 1) * 10), (236, 232, 224))
    for i, p in enumerate(paths):
        sh.paste(Image.open(p).convert("RGB").resize((w, h_), Image.LANCZOS),
                 (10 + (i % cols) * (w + 10), 10 + (i // cols) * (h_ + 10)))
    sh.save(path)
    return path


def visuals(n, pkg):
    vis = os.path.join(pkg, "04_VISUAL_ASSETS")
    os.makedirs(vis, exist_ok=True)
    cards, names = G.cards_for(n)
    html = render_html(cards, os.path.join(vis, "_v.html"), "NEW V%d" % n)
    made = shoot(html, vis, names)
    os.remove(html)
    idx = {nm[:-4]: c for nm, c in zip(names, cards)}
    svgs = []
    for f in F.SETS[n]:
        if f["svg"]:
            st = f["states"][0]
            svgs.append(svg23.write(
                idx[st["name"]], os.path.join(vis, st["name"] + ".svg"),
                "NEW V%d  %s" % (n, st["name"])))
    sheet = contact_sheet(made, os.path.join(
        vis, "Phone_Size_Contact_Sheet.png"))
    return made, svgs, sheet


def qa_report(n, path, st, rows, geo, made, svgs):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Package QA report")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
    kv(d, "Generated", st)
    ok = sum(1 for _, o, _ in rows if o)
    kv(d, "Checks run", "%d" % len(rows))
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (len(rows) - ok))
    kv(d, "Spoken words", format(S.word_count(n), ","))
    kv(d, "Thought-block match", S.blocks_match(n)[1])
    cam, full = SP.counts(n)
    kv(d, "Spine", "%d camera stretches against %d full-screen cues"
       % (cam, full))
    kv(d, "Visual assets", "%d PNG at 1920 x 1080, %d editable SVG, plus a "
                           "phone-size contact sheet" % (len(made),
                                                         len(svgs)))
    kv(d, "Geometry", "%d problems against the rendered DOM" % len(geo))
    kv(d, "Shorts", "3, as supplied")
    callout(d, "No spoken wording was changed. Every figure here is "
               "arithmetic on the approved script; nothing has been "
               "recorded, edited or exported.")
    h(d, "Every check")
    table(d, ["Check", "", "Detail"],
          [[nm, "pass" if o else "FAIL", str(dd)[:150]]
           for nm, o, dd in rows], widths=[2.7, 0.5, 3.5], size=8)
    h(d, "Final integrity checklist")
    bullets(d, [
      "The FINAL sprint script is the only spoken source.",
      "The supplied Thought-Block copy is included unchanged and matches "
      "the script word for word.",
      "Both numbers are stated: new public V%d and former roadmap V%d."
      % (n, S.NUMBERS[n]),
      "The historical locked V4 to V21 archive was not touched.",
      "Chapters and SRT are deferred to the final edit.",
      "The intended Watch Next destination is pending live availability "
      "until verified before upload.",
    ])
    d.save(path)
    return path


def package(n, st, zips, reuse_rows):
    pkg = os.path.join(OUT, pkg_name(n))
    if os.path.isdir(pkg):
        shutil.rmtree(pkg)
    for s in SUB:
        os.makedirs(os.path.join(pkg, s))
    P = lambda a, b: os.path.join(pkg, a, b)

    EV.source_hierarchy(n, P("00_SOURCE_HIERARCHY",
                             "Source_Manifest_and_Number_Map.txt"), st, zips)
    EV.claim_notes(n, P("00_SOURCE_HIERARCHY", "Claim_Boundary_Notes.docx"),
                   st)
    D.recording_master(n, P("01_RECORDING",
                            "FINAL_Sprint_Recording_Master.docx"), st)
    shutil.copy2(S.block_path(n),
                 P("01_RECORDING", os.path.basename(S.block_path(n))))
    D.run_of_show(n, P("02_RUN_OF_SHOW", "Run_of_Show.docx"), st)
    RIV.prompt(n, P("03_RIVERSIDE",
                    "Riverside_CoCreator_Master_Prompt.txt"), st)
    D.camera_map(n, P("03_RIVERSIDE", "Camera_and_Full_Screen_Map.txt"))
    D.motion_map(n, P("03_RIVERSIDE", "Motion_and_Reveal_Map.txt"))
    D.sound_map(n, P("03_RIVERSIDE", "Audio_and_Sound_Cue_Map.txt"))
    D.broll(n, P("03_RIVERSIDE", "B_Roll_Notes.txt"))

    made, svgs, sheet = visuals(n, pkg)
    D.asset_index(n, P("04_VISUAL_ASSETS", "Asset_Index.txt"),
                  [os.path.basename(x) for x in made + svgs])

    SH.bank(n, P("05_SHORTS", "Three_Candidate_Shorts.docx"), st)
    ind = os.path.join(pkg, "05_SHORTS", "Individual")
    os.makedirs(ind)
    for r in SH.rows(n):
        SH.single(n, r, os.path.join(
            ind, "NEW_V%d_Short_%d.docx" % (n, r["num"])), st)
    SH.editor_notes(n, P("05_SHORTS", "Shorts_Editor_Notes.txt"))
    SH.boundary_notes(n, P("05_SHORTS", "Shorts_Evidence_Boundaries.docx"),
                      st)

    PUB.materials(n, P("06_PUBLISHING", "Publishing_Materials.docx"), st)
    EV.claim_notes(n, P("07_EVIDENCE", "Evidence_and_Boundary_Notes.docx"),
                   st)
    return pkg, made, svgs, sheet


def master_hierarchy(path, st, zips):
    d = base_doc()
    title_block(d, EYEBROW, "Master source hierarchy and number map",
                "New public V4 to V9, two-week sprint")
    kv(d, "Generated", st)
    callout(d, "This is a NEW PUBLIC PUBLISHING LAYER. The historical locked "
               "V4 to V21 production archive is a separate layer and was not "
               "renamed, overwritten or modified. Former roadmap numbers are "
               "retained for traceability and source lineage only; they do "
               "not control the public publishing order.")
    h(d, "Number map")
    table(d, ["New public", "Former roadmap", "Title", "Thumbnail"],
          [["V%d" % n, "V%d" % S.NUMBERS[n], S.title(n), S.thumbnail(n)]
           for n in S.VIDEOS], widths=[0.8, 1.0, 3.0, 1.9], size=8.5)
    h(d, "Sprint editorial logic")
    table(d, ["Pair", "", "Videos"],
          [[name, "", ", ".join("NEW V%d  %s" % (v, S.title(v))
                                for v in vs)]
           for name, vs in S.PAIRS], widths=[1.6, 0.2, 4.9], size=8.5)
    h(d, "Order of authority")
    table(d, ["", "Source", "Authoritative for"],
          [["1", "FINAL sprint script files",
            "Spoken wording, new and former number, title, thumbnail, "
            "section order, long-form CTA, spoken Watch Next wording, three "
            "candidate Shorts, and the claim boundaries the script carries"],
           ["2", "Thought-Block Recording Copies",
            "Recording-format derivatives of the scripts above. Same spoken "
            "wording exactly. Where they disagree the script wins."],
           ["3", "Former roadmap numbers",
            "Traceability and source lineage only. Not the publishing "
            "order."]],
          widths=[0.4, 2.0, 4.3], size=8.5)
    h(d, "Source files")
    rows = [[nm, sha] for nm, sha in zips]
    for n in S.VIDEOS:
        rows.append([S.read(n)["file"], S.read(n)["sha"]])
        rows.append([os.path.basename(S.block_path(n)),
                     S.sha256(S.block_path(n))])
    table(d, ["File", "SHA-256"], rows, widths=[2.9, 3.8], size=7.5)
    h(d, "Word counts and thought-block verification")
    table(d, ["", "Spoken words", "Arithmetic estimate",
              "Thought-block match"],
          [["NEW V%d (former V%d)" % (n, S.NUMBERS[n]),
            format(S.word_count(n), ","), "%s to %s" % S.estimate(n),
            S.blocks_match(n)[1]] for n in S.VIDEOS],
          widths=[1.6, 0.9, 1.4, 2.8], size=8)
    caption(d, "Every estimate is arithmetic on the script at 130 to 145 "
               "words per minute. None is a runtime, a chapter time or an "
               "SRT time.")
    d.save(path)
    return path


def changelog(path, st, flags, reuse_rows):
    d = base_doc()
    title_block(d, EYEBROW, "Sprint production changelog",
                "What was built, from what, and what was flagged")
    kv(d, "Generated", st)
    callout(d, "No spoken wording was changed in any of the six scripts. The "
               "supplied Thought-Block copies were not rewritten, shortened "
               "or regenerated: each was verified against its script and "
               "copied into the package unchanged.")
    h(d, "What was built")
    table(d, ["", "Families", "States", "Camera stretches", "Full-screen "
              "cues", "Shorts"],
          [["NEW V%d (former V%d)" % (n, S.NUMBERS[n]),
            "%d" % len(F.SETS[n]), "%d" % len(F.states(n)),
            "%d" % SP.counts(n)[0], "%d" % SP.counts(n)[1],
            "%d" % len(S.shorts(n))] for n in S.VIDEOS],
          widths=[1.7, 0.8, 0.7, 1.3, 1.2, 0.7], size=8)

    h(d, "NEW V6, former roadmap V22")
    para(d, "The former V22 had substantial production work in a prior "
            "package. Eighteen of NEW V6's nineteen card families are "
            "carried over from it, and each was verified byte for byte "
            "against the file the locked V22 package shipped rather than "
            "assumed. The one new family is the Watch Next end card, which "
            "the sprint script adds a spoken line for and the former V22 "
            "did not have.", size=10.5)
    para(d, "The sprint script was not pushed backward to fit an older "
            "asset. Where the sprint script differs, the sprint script "
            "controls, and no card was kept because it already existed.",
        size=10.5, before=6)
    table(d, ["Reused family", "Verified"],
          [[k, det] for k, ok, det in reuse_rows],
          widths=[2.6, 4.1], size=7.5)

    h(d, "Flagged, not fixed")
    para(d, "A source-language integrity check reads every spoken script for "
            "unsupported claims about what people do, feel or struggle with. "
            "It reports; it never rewrites. Five sentences were flagged "
            "across the six scripts and none was changed.", size=10.5)
    table(d, ["Video", "The sentence", "Why it is flagged"],
          [["NEW V%d (former V%d)" % (n, S.NUMBERS[n]), sent, why]
           for n, sent, why in flags], widths=[1.3, 2.9, 2.5], size=8)
    callout(d, "The NEW V6 flag is a genuine conflict, not a style note. "
               "That exact sentence was replaced in the separately locked "
               "V22 package on the same day, by explicit authorization, for "
               "exactly this reason. The sprint script still carries the "
               "earlier wording, so the two layers now differ by one "
               "sentence. The FINAL sprint script is authoritative here and "
               "was not touched. This needs a decision, not a fix.")
    footer_note(d, "Runtime, chapters, SRT timing and thumbnail artwork are "
                   "all decided after the final edit.")
    d.save(path)
    return path


def qa_summary(path, st, results):
    d = base_doc()
    title_block(d, EYEBROW, "Sprint package QA summary",
                "Every check, and what it measured")
    kv(d, "Generated", st)
    tot = sum(len(r) for r in results.values())
    ok = sum(1 for r in results.values() for _, o, _ in r if o)
    kv(d, "Checks run", "%d" % tot)
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (tot - ok))
    for n in S.VIDEOS:
        h(d, "NEW V%d (former roadmap V%d)  %s" % (n, S.NUMBERS[n],
                                                   S.title(n)))
        table(d, ["Check", "", "Detail"],
              [[nm, "pass" if o else "FAIL", str(dd)[:180]]
               for nm, o, dd in results[n]],
              widths=[2.7, 0.5, 3.5], size=8)
    footer_note(d, "Every figure is arithmetic on the approved script. "
                   "Nothing here has been recorded, edited or exported.")
    d.save(path)
    return path


FLAGS = [
 (6, "Then ask the question people sometimes skip because they want the "
     "move to work:",
  "Asserts what people do and why. The separately locked V22 package "
  "replaced this exact sentence on September 13 by explicit authorization. "
  "The sprint script still carries it, so the two layers differ by one "
  "sentence. Not changed here: the FINAL sprint script is authoritative."),
 (8, "This happens because most people treat evidence like something they "
     "will collect later.",
  "Asserts what most people do. The teaching survives without the claim, "
  "but the sentence is approved source and was not touched."),
 (8, "People wait because collecting evidence can feel self-promotional "
     "while you are employed.",
  "Asserts a motive for a population. Not changed."),
 (9, "When people talk about changing industries, they usually ask one "
     "question:",
  "Asserts what people usually ask. Not changed."),
 (9, "And then there is the part people sometimes want to skip.",
  "Asserts what people want to do. Not changed."),
]


def main():
    st = stamp()
    print("stamp:", st)
    zips = [(nm, S.ZIP_SHA[nm]) for nm in sorted(S.ZIP_SHA)]
    for nm, want in zips:
        got = sha256(os.path.join(OUT, "_source", nm))
        print("  %s  %s" % (nm, "verified" if got == want else "MISMATCH"))
        if got != want:
            raise SystemExit("source archive mismatch")
    for n in S.VIDEOS:
        ok, det = S.blocks_match(n)
        if not ok:
            raise SystemExit("thought-block mismatch on NEW V%d: %s"
                             % (n, det))
    print("  six scripts, six thought-block copies, all match exactly")

    reuse_rows = RU.check(6)
    if not all(ok for _, ok, _ in reuse_rows):
        raise SystemExit("V6 reuse verification failed")
    print("  NEW V6: %d reused families verified against the locked V22 bytes"
          % len(reuse_rows))

    results, pkgs = {}, {}
    for n in S.VIDEOS:
        geo, _, _, _ = G.check(n)
        pkg, made, svgs, sheet = package(n, st, zips, reuse_rows)
        rr = reuse_rows if n == 6 else None
        QA.run(n, pkg, geo, made, rr)
        qa_report(n, os.path.join(pkg, "08_QA", "Package_QA_Report.docx"),
                  st, QA.run(n, pkg, geo, made, rr), geo, made, svgs)
        results[n] = QA.run(n, pkg, geo, made, rr)
        bad = [x for x in results[n] if not x[1]]
        print("NEW V%-2d (former V%-2d)  %2d/%2d checks   %2d png   %d svg   %s"
              % (n, S.NUMBERS[n], len(results[n]) - len(bad),
                 len(results[n]), len(made), len(svgs),
                 "OK" if not bad else "FAILURES"))
        for nm, o, dd in bad:
            print("      FAIL  %s  ->  %s" % (nm, dd))
        pkgs[n] = pkg

    shared = os.path.join(OUT, "_shared")
    if os.path.isdir(shared):
        shutil.rmtree(shared)
    os.makedirs(shared)
    docs = [
      master_hierarchy(os.path.join(
          shared, "NEW_V4-V9_SPRINT_MASTER_SOURCE_HIERARCHY_AND_NUMBER_"
                  "MAP.docx"), st, zips),
      qa_summary(os.path.join(
          shared, "NEW_V4-V9_SPRINT_PACKAGE_QA_SUMMARY.docx"), st, results),
      changelog(os.path.join(
          shared, "NEW_V4-V9_SPRINT_PRODUCTION_CHANGELOG.docx"), st, FLAGS,
          reuse_rows),
    ]

    # one archive per video, then the outer archive
    members = []
    for n in S.VIDEOS:
        zp = os.path.join(OUT, pkg_name(n) + ".zip")
        names = []
        for root, _, files in os.walk(pkgs[n]):
            for f_ in files:
                names.append(os.path.join(root, f_))
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED,
                             compresslevel=6) as z:
            for f_ in sorted(names):
                zi = zipfile.ZipInfo(
                    os.path.join(pkg_name(n),
                                 os.path.relpath(f_, pkgs[n])),
                    date_time=ZIP_DT)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                with open(f_, "rb") as fh:
                    z.writestr(zi, fh.read())
        with open(zp + ".sha256", "w") as f_:
            f_.write("%s  %s\n" % (sha256(zp), os.path.basename(zp)))
        members += [zp, zp + ".sha256"]
    members += docs

    zpath = os.path.join(OUT, ARCHIVE)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for p in sorted(members):
            zi = zipfile.ZipInfo(os.path.basename(p), date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(p, "rb") as fh:
                z.writestr(zi, fh.read())
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
    return passed == tot


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
