# -*- coding: utf-8 -*-
"""Build the NEW PUBLIC V10 and V11 production packages."""
import os, sys, math, glob, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")

import rdeck
from rdeck import render_html, shoot
from PIL import Image
import svg23
import v1011 as S
import frames1011 as F
import spine1011 as SP
import geo1011 as G
import docs1011 as D
import riverside1011 as RIV
import shortsdocs1011 as SD
import shorts1011 as SH
import publish1011 as PUB
import evidence1011 as EV
import qa1011 as QA
from docs1011 import (base_doc, title_block, h, kv, para, callout, sub,
                      caption, table, bullets, footer_note, EYEBROW)

SUB = ["00_SOURCE_HIERARCHY", "01_RECORDING", "02_RUN_OF_SHOW",
       "03_RIVERSIDE", "04_VISUAL_ASSETS", "05_SHORTS", "06_PUBLISHING",
       "07_EVIDENCE", "08_QA"]
ZIP_DT = (2026, 9, 14, 0, 0, 0)
ARCHIVE = ("YouTube_NEW_PUBLIC_V10-V11_FINAL_Production_Packages_"
           "2026-09-14.zip")
PKG_NAME = {10: "NEW_V10_First_90_Days_Production_Package",
            11: "NEW_V11_New_Job_Isnt_The_Job_Production_Package"}


def pkg_name(n):
    return PKG_NAME[n]


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
    kv(d, "Former roadmap number", "None. This is a new concept.")
    kv(d, "Generated", st)
    ok = sum(1 for _, o, _ in rows if o)
    kv(d, "Checks run", "%d" % len(rows))
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (len(rows) - ok))
    kv(d, "Spoken words", format(S.word_count(n), ","))
    lo, hi = S.estimate(n)
    kv(d, "Arithmetic estimate", "%s to %s. Not a runtime." % (lo, hi))
    kv(d, "Thought-block match", S.blocks_match(n)[1])
    cam, full = SP.counts(n)
    kv(d, "Spine", "%d camera stretches against %d full-screen cues"
       % (cam, full))
    kv(d, "Visual assets", "%d PNG at 1920 x 1080, %d editable SVG, plus a "
                           "phone-size contact sheet"
       % (len(made), len(svgs)))
    kv(d, "Geometry", "%d problems against the rendered DOM" % len(geo))
    kv(d, "Shorts", "3, built from the script's own sentences")
    callout(d, "No spoken wording was changed. Every figure here is "
               "arithmetic on the approved script; nothing has been "
               "recorded, edited or exported.")
    h(d, "Every check")
    table(d, ["Check", "", "Detail"],
          [[nm, "pass" if o else "FAIL", str(dd)[:150]]
           for nm, o, dd in rows], widths=[2.7, 0.5, 3.5], size=8)
    h(d, "Final integrity checklist")
    bullets(d, [
      "The FINAL story-led script is the only spoken source.",
      "The supplied Thought-Block copy is included unchanged and matches "
      "the script word for word and in order.",
      "This is a new concept. No former-roadmap number exists and none "
      "was invented.",
      "The %s framework is intact and in the script's order."
      % " / ".join(QA.FRAMEWORK[n]),
      "Every Short line is verbatim from this script.",
      "Chapters and SRT are deferred to the final edit.",
      "The intended Watch Next destination is pending live availability "
      "until verified before upload.",
    ])
    d.save(path)
    return path


def package(n, st, sources):
    pkg = os.path.join(OUT, pkg_name(n))
    if os.path.isdir(pkg):
        shutil.rmtree(pkg)
    for s in SUB:
        os.makedirs(os.path.join(pkg, s))
    P = lambda a, b: os.path.join(pkg, a, b)

    EV.source_hierarchy(n, P("00_SOURCE_HIERARCHY",
                             "Source_Manifest_and_Number_Map.txt"), st,
                        sources)
    EV.claim_notes(n, P("00_SOURCE_HIERARCHY", "Claim_Boundary_Notes.docx"),
                   st)
    D.recording_master(n, P("01_RECORDING", "FINAL_Recording_Master.docx"),
                       st)
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

    SD.bank(n, P("05_SHORTS", "Three_Candidate_Shorts.docx"), st)
    ind = os.path.join(pkg, "05_SHORTS", "Individual")
    os.makedirs(ind)
    for r in SH.rows(n):
        SD.single(n, r, os.path.join(
            ind, "NEW_V%d_Short_%d.docx" % (n, r["num"])), st)
    SD.editor_notes(n, P("05_SHORTS", "Shorts_Editor_Notes.txt"))
    SD.boundary_notes(n, P("05_SHORTS", "Shorts_Evidence_Boundaries.docx"),
                      st)

    PUB.materials(n, P("06_PUBLISHING", "Publishing_Materials.docx"), st)
    EV.claim_notes(n, P("07_EVIDENCE", "Evidence_and_Boundary_Notes.docx"),
                   st)
    return pkg, made, svgs, sheet


def master_hierarchy(path, st, sources):
    d = base_doc()
    title_block(d, EYEBROW, "Master source hierarchy and number map",
                "New public V10 and V11")
    kv(d, "Generated", st)
    callout(d, "Both videos are NEW CONCEPTS. Neither came from the earlier "
               "roadmap, so neither has a former-roadmap number and none "
               "was invented. V10 follows NEW PUBLIC V9. V11 follows NEW "
               "PUBLIC V10.")
    h(d, "Number map")
    table(d, ["New public", "Former roadmap", "Title", "Thumbnail"],
          [["V%d" % n, "None. New concept.", S.title(n), S.thumbnail(n)]
           for n in S.VIDEOS], widths=[0.8, 1.2, 2.8, 1.9], size=8.5)
    h(d, "Pair logic")
    table(d, ["", "What the video does"],
          [["NEW V10", "Entering a new context well when you are "
                       "experienced but new to the environment. It ends on "
                       "a ROLE CHECK, which is the bridge into V11."],
           ["NEW V11", "Evaluating material drift between the role "
                       "accepted and the role that actually exists."]],
          widths=[1.0, 5.7], size=8.5)
    caption(d, "They are a pair, not one topic. V10 asks what the 90 days "
               "taught you about the job. V11 is what to do with that "
               "answer.")
    h(d, "Order of authority")
    table(d, ["", "Source", "Authoritative for"],
          [["1", "FINAL story-led recording scripts",
            "Spoken wording, title, thumbnail, framework, section order, "
            "CTA and Watch Next wording, and the claim boundaries the "
            "script carries."],
           ["2", "Thought-Block Recording Copies",
            "Recording-format derivatives of the scripts above. Same "
            "spoken wording exactly and in order. Where they disagree the "
            "script wins."],
           ["3", "Advisor and Code Handoff",
            "Production architecture, visual language, resource mapping, "
            "Shorts strategy and boundaries. Not spoken wording."]],
          widths=[0.4, 2.0, 4.3], size=8.5)
    h(d, "Source files")
    table(d, ["File", "SHA-256"], [[nm, sha] for nm, sha in sources],
          widths=[2.9, 3.8], size=7.5)
    h(d, "Word counts and thought-block verification")
    table(d, ["", "Spoken words", "Arithmetic estimate",
              "Thought-block match"],
          [["NEW V%d" % n, format(S.word_count(n), ","),
            "%s to %s" % S.estimate(n), S.blocks_match(n)[1]]
           for n in S.VIDEOS], widths=[0.9, 1.1, 1.6, 3.1], size=8)
    caption(d, "Every estimate is arithmetic on the script at 130 to 145 "
               "words per minute. None is a runtime. Both counts match the "
               "counts supplied with the handoff exactly.")
    footer_note(d, "Runtime, chapters, SRT timing, upload date, public "
                   "URLs and performance are all decided after the final "
                   "edit. None appears in this package.")
    d.save(path)
    return path


def qa_summary(path, st, results):
    d = base_doc()
    title_block(d, EYEBROW, "Package QA summary",
                "Every check, and what it measured")
    kv(d, "Generated", st)
    tot = sum(len(r) for r in results.values())
    ok = sum(1 for r in results.values() for _, o, _ in r if o)
    kv(d, "Checks run", "%d" % tot)
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (tot - ok))
    for n in S.VIDEOS:
        h(d, "NEW PUBLIC V%d  %s" % (n, S.title(n)))
        table(d, ["Check", "", "Detail"],
              [[nm, "pass" if o else "FAIL", str(dd)[:180]]
               for nm, o, dd in results[n]],
              widths=[2.7, 0.5, 3.5], size=8)
    footer_note(d, "Every figure is arithmetic on the approved script. "
                   "Nothing here has been recorded, edited or exported.")
    d.save(path)
    return path


def changelog(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Production changelog",
                "What was built, from what, and what was decided")
    kv(d, "Generated", st)
    callout(d, "No spoken wording was changed in either script. Both "
               "Thought-Block copies were verified against their scripts "
               "and copied into the packages unchanged. Both spoken-word "
               "counts match the counts supplied with the handoff exactly.")
    h(d, "What was built")
    table(d, ["", "Families", "States", "Camera stretches",
              "Full-screen cues", "Shorts"],
          [["NEW V%d" % n, "%d" % len(F.SETS[n]), "%d" % len(F.states(n)),
            "%d" % SP.counts(n)[0], "%d" % SP.counts(n)[1],
            "%d" % len(SH.rows(n))] for n in S.VIDEOS],
          widths=[1.0, 0.9, 0.8, 1.4, 1.3, 0.8], size=8.5)

    h(d, "The Shorts")
    para(d, "Neither FINAL script carries a Shorts section, and the "
            "handoff is explicit that no spoken wording may be invented "
            "for one. So every line of all six Shorts is a whole sentence "
            "lifted verbatim from its parent video, and that is checked "
            "sentence by sentence against the script rather than asserted.",
         size=10.5)
    table(d, ["", "#", "Angle", "Words", "At 165 wpm"],
          [["NEW V%d" % n, "%d" % r["num"], r["title"],
            format(r["words"], ","), "0:%02d" % r["secs"]]
           for n in S.VIDEOS for r in SH.rows(n)],
          widths=[0.9, 0.3, 3.0, 0.8, 1.0], size=8)

    h(d, "One decision worth flagging")
    para(d, "The handoff gives the muted gold as C9A34A and the bright "
            "warm yellow as F2C94C. The established house values, used by "
            "every locked Capability Formation package, are C9A84C and "
            "F2C44C. The difference is a couple of hex digits and is not "
            "visible on screen, but adopting the new values would have "
            "made V10 and V11 render microscopically differently from V4 "
            "to V9 sitting beside them in the same playlist.", size=10.5)
    para(d, "The house values were kept, on the handoff's own instruction "
            "to use the established house style. Navy and cream match the "
            "handoff exactly. If the new values were intended literally, "
            "say so and both packages rebuild in one pass.", size=10.5,
        before=6)

    h(d, "What this build did not do")
    bullets(d, [
      "No former-roadmap number was invented for either video. Both are "
      "new concepts and every document says so.",
      "No runtime, chapter timing, SRT timing, upload date, public URL, "
      "thumbnail result, retention figure or music license appears "
      "anywhere.",
      "No research was invented. Neither video cites any, and the "
      "evidence notes say that plainly rather than implying a study.",
      "No second spoken CTA was added. Neither script names a product, so "
      "the resource lives in the description only.",
      "The Shorts bank was not expanded to six.",
      "lay23.py, the shared layout toolkit, was not edited. The two "
      "shapes this pair needed were added in a batch-local module so "
      "every locked package still renders byte for byte.",
    ], size=10)
    footer_note(d, "Runtime, chapters, SRT timing and thumbnail artwork "
                   "are all decided after the final edit.")
    d.save(path)
    return path


def main():
    st = stamp()
    print("stamp:", st)
    src = os.path.join(OUT, "_source", "handoff.zip")
    got = sha256(src)
    print("  handoff.zip  %s" % ("verified" if got == S.HANDOFF_SHA
                                 else "MISMATCH"))
    if got != S.HANDOFF_SHA:
        raise SystemExit("handoff archive mismatch")
    sources = [("handoff.zip", S.HANDOFF_SHA)]
    for nm, want in sorted(S.FILE_SHA.items()):
        p = os.path.join(S.SRC, nm)
        if sha256(p) != want:
            raise SystemExit("source mismatch: %s" % nm)
        sources.append((nm, want))
    print("  five source documents verified against their intake hashes")

    for n in S.VIDEOS:
        ok, det = S.blocks_match(n)
        if not ok:
            raise SystemExit("thought-block mismatch on NEW V%d: %s"
                             % (n, det))
        if S.word_count(n) != S.STATED_WORDS[n]:
            raise SystemExit("NEW V%d word count %d, handoff states %d"
                             % (n, S.word_count(n), S.STATED_WORDS[n]))
    print("  two scripts, two thought-block copies, all match exactly")
    for n in S.VIDEOS:
        bad = SH.verify(n)
        if bad:
            raise SystemExit("NEW V%d Short wording not verbatim: %s"
                             % (n, bad))
    print("  six Shorts, every line verbatim from its parent script")

    results, pkgs = {}, {}
    for n in S.VIDEOS:
        geo, _, _, _ = G.check(n)
        pkg, made, svgs, sheet = package(n, st, sources)
        qa_report(n, os.path.join(pkg, "08_QA", "Package_QA_Report.docx"),
                  st, QA.run(n, pkg, geo, made), geo, made, svgs)
        results[n] = QA.run(n, pkg, geo, made)
        bad = [x for x in results[n] if not x[1]]
        print("NEW V%-2d  %2d/%2d checks   %2d png   %d svg   %s"
              % (n, len(results[n]) - len(bad), len(results[n]),
                 len(made), len(svgs), "OK" if not bad else "FAILURES"))
        for nm, o, dd in bad:
            print("      FAIL  %s  ->  %s" % (nm, dd))
        pkgs[n] = pkg

    shared = os.path.join(OUT, "_shared")
    if os.path.isdir(shared):
        shutil.rmtree(shared)
    os.makedirs(shared)
    docs = [
      master_hierarchy(os.path.join(
          shared, "NEW_V10-V11_MASTER_SOURCE_HIERARCHY_AND_NUMBER_MAP.docx"),
          st, sources),
      qa_summary(os.path.join(
          shared, "NEW_V10-V11_PACKAGE_QA_SUMMARY.docx"), st, results),
      changelog(os.path.join(
          shared, "NEW_V10-V11_PRODUCTION_CHANGELOG.docx"), st),
    ]

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
    ok = sum(1 for r in results.values() for _, o, _ in r if o)
    print("\n  %s" % ARCHIVE)
    print("  sha256 %s" % digest)
    print("  %d entries" % len(zipfile.ZipFile(zpath).namelist()))
    print("  package checks: %d of %d passed" % (ok, tot))


if __name__ == "__main__":
    main()
