# -*- coding: utf-8 -*-
"""Build the eighteen story-led production packages."""
import os, sys, json, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")

import importlib.util


def _local(name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


for _n in ("masters_sl", "recdocs_sl", "publish_sl"):
    _local(_n)

import masters_sl as M
import packaging_sl as PK
import recdocs_sl, prodocs_sl, riverside_sl, editorial_sl, publish_sl
import shorts_sl, qa_sl, geocheck_sl, visualdir_sl, wncheck_sl, srcqa_sl
import exercise_sl
import shortsdocs_sl as shortsdocs
from frames_sl import SETS, REMOVED
from shorts421 import SHORTS
from docs421f import mono, hr, head
from rdeck import shoot, render_pptx
from PIL import Image

SUB = ["01_Recording_Master", "02_Recording", "03_Visuals", "04_Riverside",
       "05_Shorts", "06_Publishing", "07_Viewer_Exercise",
       "08_Sources_and_QA"]
ZIP_DT = (2026, 9, 13, 0, 0, 0)
ARCHIVE = "Videos_4-21_STORY_LED_FINAL_Production_Packages.zip"
BASELINE_SHA = ("7dbf2d56add4a91fd50f4f1f75c15908ec996a5932d70128bf7db190f8"
                "e0dfcb")


def stamp():
    return subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def pkg_dir(n):
    return os.path.join(OUT, "VIDEO_%d_STORY_LED_PACKAGE" % n)


def contact_sheet(pngs, path, phone_w=393, cols=2, pad=18):
    tiles = []
    for p in pngs:
        im = Image.open(p).convert("RGB")
        tiles.append(im.resize((phone_w,
                                int(round(im.height * phone_w / im.width))),
                               Image.LANCZOS))
    rows = (len(tiles) + cols - 1) // cols
    tw, th = phone_w, tiles[0].height
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * pad,
                              rows * th + (rows + 1) * pad), (24, 26, 30))
    for i, t in enumerate(tiles):
        sheet.paste(t, (pad + (i % cols) * (tw + pad),
                        pad + (i // cols) * (th + pad)))
    sheet.save(path)
    return path


def zip_dir(src, zpath):
    if os.path.exists(zpath):
        os.remove(zpath)
    files = []
    for root, _, names in os.walk(src):
        for nm in names:
            p = os.path.join(root, nm)
            files.append((os.path.relpath(p, os.path.dirname(src)), p))
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for rel, p in sorted(files):
            info = zipfile.ZipInfo(rel, date_time=ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(p, "rb") as f:
                z.writestr(info, f.read())
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), os.path.basename(zpath)))
    return zpath, len(files)


def build_one(n, s):
    pkg = pkg_dir(n)
    if os.path.exists(pkg):
        shutil.rmtree(pkg)
    for x in SUB:
        os.makedirs(os.path.join(pkg, x))
    d = lambda x: os.path.join(pkg, x)

    recdocs_sl.copy_sources(n, d(SUB[0]))
    recdocs_sl.reading_reference(
        n, os.path.join(d(SUB[0]), "Reading_Reference.docx"), s)

    prodocs_sl.run_of_show(
        n, os.path.join(d(SUB[1]), "Recording_Run_of_Show.docx"), s)

    prodocs_sl.trigger_map(
        n, os.path.join(d(SUB[2]), "Camera_and_Full_Screen_Map.txt"))
    prodocs_sl.visual_build_map(
        n, os.path.join(d(SUB[2]), "Visual_Build_and_Motion_Reveal_Map.txt"))
    probs, html, cards, names = geocheck_sl.check(n)
    if probs:
        raise SystemExit("V%d geometry: %s" % (n, probs))
    png = os.path.join(d(SUB[2]), "Support_Reference_PNG")
    shoot(os.path.abspath(html), png, names)
    render_pptx(cards, os.path.join(d(SUB[2]),
                                    "V%d_Reference_Deck.pptx" % n))
    contact_sheet([os.path.join(png, x) for x in names],
                  os.path.join(d(SUB[2]),
                               "V%d_Phone_Size_Contact_Sheet.png" % n))
    for f in SETS[n]:
        if f["key"].endswith("_cta"):
            shutil.copy2(os.path.join(png, f["key"] + ".png"),
                         os.path.join(d(SUB[2]), "Resource_Card.png"))
        if f["key"].endswith("_watch_next"):
            shutil.copy2(os.path.join(png, f["key"] + ".png"),
                         os.path.join(d(SUB[2]), "Watch_Next_Card.png"))

    riverside_sl.build(n, os.path.join(
        d(SUB[3]), "Riverside_CoCreator_Master_Prompt.txt"))

    shortsdocs.combined(n, os.path.join(
        d(SUB[4]), "Video_%d_Six_Short_Form_Scripts.docx" % n), s)
    ind = os.path.join(d(SUB[4]), "Individual")
    os.makedirs(ind, exist_ok=True)
    for sh in SHORTS[n]:
        shortsdocs.individual(n, sh, os.path.join(ind, sh["slug"] + ".docx"))
    L = head("VIDEO %d  |  SHORTS AUDIT AGAINST THE STORY-LED SCRIPT" % n)
    L += [M.title(n), "",
          "A Short is a standalone idea. It is not rebuilt because the "
          "long-form",
          "reworded a supporting sentence. It is changed when the framework "
          "it rests",
          "on is gone, or its hook no longer matches the story-led "
          "approach.", "", hr(), ""]
    for sh, state, ov, why in shorts_sl.audit(n):
        L += ["  %-34s %s" % (sh["slug"], state),
              "      priority %s, %s" % (sh["priority"], sh["source"]),
              "      support against the story-led script: %.2f" % ov]
        L += ["      %s" % why, ""]
    mono(os.path.join(d(SUB[4]), "Shorts_Story_Led_Audit.txt"), L)

    publish_materials(n, os.path.join(d(SUB[5]),
                                      "Publishing_Materials.docx"), s)

    exercise_sl.build(n, os.path.join(d(SUB[6]), "Viewer_Exercise.docx"), s)
    editorial_sl.build(n, os.path.join(d(SUB[6]), "Editorial_Check.docx"), s)

    source_manifest(n, pkg, s)
    change_log(n, os.path.join(d(SUB[7]), "Change_Log.txt"), s)
    with open(os.path.join(d(SUB[7]), "Source_Hashes.txt"), "w") as f:
        f.write("%s  %s\n" % (M.read(n)["sha"], os.path.basename(M.path(n))))
        f.write("%s  %s\n" % (M.sha256(M.path(n, True)),
                              os.path.basename(M.path(n, True))))
    rows = srcqa_sl.check(n)
    mono(os.path.join(d(SUB[7]), "Source_QA.txt"),
         head("VIDEO %d  |  SOURCE QA" % n)
         + ["  [%s] %s" % ("PASS" if ok else "FAIL", nm) + "\n         %s"
            % dt for nm, ok, dt in rows])
    return pkg


def publish_materials(n, path, s):
    from docs421f import (base_doc, para, title_block, h, kv, callout, table,
                          bullets, caption, footer_note, numbered,
                          NAVY, GOLD, DIM, RED)
    a = publish_sl.audit(n)
    res = a["route"]
    wn_n, wn_t, wn_src = publish_sl.watch_next(n)
    d = base_doc()
    footer_note(d, "Video %d publishing materials  |  story-led" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Publishing Materials", M.title(n))
    kv(d, "Generated", s)
    kv(d, "Spoken source", "%s  ·  SHA-256 %s"
       % (M.read(n)["file"], M.read(n)["sha"]))
    callout(d, "Title wording is taken from the story-led script header. "
               "Thumbnail wording of record comes from the locked V4 to V21 "
               "roadmap. No URL, chapter timestamp, music credit or "
               "performance claim is invented anywhere in this document.")
    h(d, "YouTube title")
    para(d, M.title(n), size=13, bold=True, color=NAVY)
    h(d, "Thumbnail text")
    para(d, PK.thumbnail(n), size=13, bold=True, color=NAVY)
    if PK.is_exception(n):
        caption(d, "Unchanged from the locked roadmap. The story-led script "
                   "document header carries %r as non-spoken metadata. That "
                   "metadata is not packaging authority and does not "
                   "override the roadmap. The source document was not "
                   "edited and its hash is unchanged."
                   % PK.script_header_thumbnail(n))
    h(d, "Description")
    for b in publish_sl.DESC[n].split("\n\n"):
        para(d, b)
    if res:
        para(d, "RESOURCE LINE, paste as the last block:", size=9, bold=True,
             color=GOLD, before=10, after=4)
        para(d, "%s: https://%s" % (res, publish_sl.ROUTES[res]), size=11,
             bold=True)
    else:
        para(d, "This video names no resource. Do not add one.", size=11,
             bold=True, color=RED)
    para(d, "WATCH NEXT LINE: Video %d: %s" % (wn_n, wn_t), size=10,
         color=DIM)
    para(d, "[PLACEHOLDER] Insert the Watch Next URL after that video is "
            "published. Do not invent a URL.", size=10, color=RED)
    h(d, "Pinned comment")
    for b in publish_sl.PINNED[n].split("\n\n"):
        para(d, b)
    if a["copy_changed"]:
        caption(d, "The %s was updated by the story-led pass, because the "
                   "script changed the hook framing it described. Nothing "
                   "else in this video's publishing copy was rewritten."
                   % a["copy_changed"])
    h(d, "Tags")
    para(d, ", ".join(publish_sl.TAGS[n]))
    h(d, "Hashtags")
    para(d, "  ".join(publish_sl.HASH[n]), size=12, bold=True)
    h(d, "Resource route")
    if res:
        table(d, ["Resource", "Where it lives", "How it is used"],
              [[res, publish_sl.ROUTES[res],
                "Spoken once, after the teaching. One primary CTA. No second "
                "offer is added."]], widths=[1.9, 2.1, 2.7], size=9)
    else:
        para(d, "None. This script names no resource route.", color=RED,
             bold=True)
    h(d, "Watch Next and playlist")
    table(d, ["Field", "Value"], [
      ["Watch Next", "Video %d: %s" % (wn_n, wn_t)],
      ["Where that comes from", wn_src],
      ["Playlist", publish_sl.PLAYLIST],
      ["End screen", "Watch Next is the final full-screen visual. Copy sits "
                     "left so an end screen can sit right. No return to "
                     "camera afterward."],
    ], widths=[1.35, 5.35], size=9)
    h(d, "Publication checklist")
    numbered(d, [
      "Thumbnail artwork approved separately, checked at 200 px wide. "
      "Artwork is NOT rebuilt by this pass.",
      ("Title matches the story-led script header; thumbnail wording "
       "matches the locked V4 to V21 roadmap."
       if PK.is_exception(n) else
       "Title and thumbnail wording match the story-led script header."),
      "Description resource link tested while signed out." if res else
      "No resource link appears anywhere, because the script names none.",
      "Watch Next URL inserted once that video is published. Not before.",
      "Captions: no burned-in subtitles. SRT from the final edited timeline.",
      "Chapters written from the actual final export. None exist yet.",
      "Music attribution from the actual track used. None is recorded here.",
    ])
    d.save(path)
    return path


def source_manifest(n, pkg, s):
    from collections import Counter
    m = M.read(n)
    w, fast, slow = M.estimate(n)
    data = {
      "video": n, "title": M.title(n), "thumbnail": PK.thumbnail(n),
      "thumbnail_source": "locked V4 to V21 roadmap",
      "script_header_thumbnail": PK.script_header_thumbnail(n),
      "thumbnail_metadata_exception": PK.is_exception(n),
      "thumbnail_note": (PK.EXCEPTION_NOTE if PK.is_exception(n)
                         else "The script header and the locked roadmap "
                              "agree for this video."),
      "generated": s,
      "spoken_source_of_truth": {
        "script": m["file"], "script_sha256": m["sha"],
        "thought_block": os.path.basename(M.path(n, True)),
        "thought_block_sha256": M.sha256(M.path(n, True)),
        "note": "Both copied unchanged into 01_Recording_Master and never "
                "written to. They override the pre-story-led package."},
      "pre_story_led_baseline": {
        "archive": "Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip",
        "sha256": BASELINE_SHA,
        "status": "Preserved and auditable. Not modified, not overwritten, "
                  "and no longer the active production handoff."},
      "runtime": {
        "class": M.mode(n), "spoken_words": w,
        "estimated_speech": "%s to %s at 130 to 145 words per minute"
                            % (fast, slow),
        "note": "Arithmetic on the script. Not a runtime and not a target. "
                "The actual length is observed at Temidayo's natural pace."},
      "assets": [{"file": f["key"] + ".png", "status": f["status"],
                  "treatment": visualdir_sl.treatment(f["key"])[0],
                  "mode": "FULL SCREEN", "why": f["why"],
                  "cue": f["trigger"]} for f in SETS[n]],
      "assets_removed": [{"file": k + ".png", "why": v}
                         for k, v in REMOVED.items() if k.startswith("v%d_" % n)],
      "asset_classification": dict(Counter(f["status"] for f in SETS[n])),
      "shorts": [{"slug": sh["slug"], "state": st, "support": round(ov, 2)}
                 for sh, st, ov, _ in shorts_sl.audit(n)],
      "not_verified": [
        "Nothing here has been recorded, edited or exported.",
        "Runtime figures are arithmetic, not measured.",
        "No thumbnail artwork exists or is approved.",
        "No chapters, SRT or music attribution exists.",
        "No public link has been checked."],
    }
    p = os.path.join(pkg, "08_Sources_and_QA", "Source_Manifest_V%d.json" % n)
    with open(p, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return p


def change_log(n, path, s):
    from collections import Counter
    cnt = Counter(f["status"] for f in SETS[n])
    w, fast, slow = M.estimate(n)
    L = head("VIDEO %d  |  STORY-LED SYNCHRONIZATION CHANGE LOG" % n)
    L += [M.title(n), "", "Generated: %s" % s, "", hr(), "",
          "WHAT CHANGED", "",
          "  The delivery changed, not the architecture. The viewer now "
          "meets a",
          "  recognizable situation first, then gets help making sense of "
          "it, then",
          "  gets the framework.", "",
          "  This is not a framework rebuild, a runtime-strategy rebuild, "
          "an offer",
          "  rebuild or a roadmap rebuild.", "", hr(), "",
          "SPOKEN SOURCE", "",
          "  %s" % M.read(n)["file"],
          "  SHA-256 %s" % M.read(n)["sha"], "",
          "  %s" % os.path.basename(M.path(n, True)),
          "  SHA-256 %s" % M.sha256(M.path(n, True)), "",
          "  %d spoken words. Estimated speech %s to %s at 130 to 145 words "
          "per" % (w, fast, slow),
          "  minute, which is arithmetic and not a runtime.", "", hr(), "",
          "VISUAL ASSETS", ""]
    for k in ("REUSE", "COPY UPDATE", "REBUILD", "NEW", "REMOVE"):
        if cnt.get(k):
            L += ["    %-14s %d" % (k, cnt[k])]
    L += [""]
    for f in SETS[n]:
        if f["status"] != "REUSE":
            L += ["  %s  %s" % (f["key"], f["status"])]
            L += ["      %s" % x for x in _wrap(f["why"], 68)]
            L += [""]
    gone = [(k, v) for k, v in REMOVED.items() if k.startswith("v%d_" % n)]
    if gone:
        L += ["  REMOVED", ""]
        for k, v in gone:
            L += ["  %s" % k] + ["      %s" % x for x in _wrap(v, 68)] + [""]
    L += [hr(), "", "WHAT DID NOT CHANGE", "",
          "  The approved frameworks, evidence boundaries, real-world "
          "constraints,",
          "  CTA intent, resource route and Watch Next destination are all "
          "preserved.",
          "  The title is unchanged. No spoken wording was edited at the "
          "production",
          "  layer, and no graphic introduces teaching the script does not "
          "carry.", "", hr(), "",
          "THE PRE-STORY-LED BASELINE", "",
          "  Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip",
          "  SHA-256 %s" % BASELINE_SHA, "",
          "  Preserved and auditable. Not modified and not overwritten. It "
          "is no",
          "  longer the active production handoff.", ""]
    return mono(path, L)


def _wrap(s, w):
    out, line = [], ""
    for word in s.split():
        if len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


# ======================================================== batch deliverables
def source_hierarchy(path, s):
    L = head("VIDEOS 4 TO 21  |  STORY-LED SOURCE HIERARCHY MANIFEST")
    L += ["Generated: %s" % s, "", hr(), "", "THE RULE", "",
          "  The September 13 story-led script and its matching thought-block "
          "copy",
          "  are the spoken source of truth. Where the pre-story-led package "
          "differs,",
          "  the story-led script wins.", "",
          "  They control the opening, the scene order, the bridges, where "
          "the",
          "  framework lands, the examples, the application moments, the "
          "closing,",
          "  the CTA wording and the Watch Next intent.", "", hr(), "",
          "WHAT THE SCRIPT LAYER DOES NOT CONTROL", "",
          "  The script document header also carries title and thumbnail "
          "metadata.",
          "  That metadata is NOT spoken, and it is NOT packaging authority. "
          "The",
          "  separately locked V4 to V21 roadmap decides thumbnail wording. "
          "Where the",
          "  two differ, the roadmap is the thumbnail of record and the "
          "header value",
          "  is carried below as a known metadata exception.", ""]
    if PK.exceptions():
        for n, hdr, rec in PK.exceptions():
            L += ["  V%-3d script header metadata  %r" % (n, hdr),
                  "        thumbnail of record    %r  (locked roadmap)" % rec]
    else:
        L += ["  There are currently no exceptions."]
    L += ["", "  No source document was edited to resolve this, and every "
              "source hash",
          "  below is unchanged.", "", hr(), "",
          "PRIMARY, AND DEFINITIVE", ""]
    for n in M.VIDEOS:
        L += ["  V%-2d %s" % (n, M.read(n)["file"]),
              "      SHA-256 %s" % M.read(n)["sha"],
              "      %s" % os.path.basename(M.path(n, True)),
              "      SHA-256 %s" % M.sha256(M.path(n, True))]
    L += ["", "  V4-V21_Storytelling_Lens_Change_Log_and_QA.docx",
          "      SHA-256 %s" % M.sha256(os.path.join(M.SRC, M.CHANGELOG)),
          "", hr(), "", "SECONDARY PRODUCTION BASELINE", "",
          "  Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip",
          "  SHA-256 %s" % BASELINE_SHA, "",
          "  Used for package structure, existing visual assets, asset "
          "mechanics,",
          "  Shorts structure, publishing structure, QA infrastructure and "
          "reusable",
          "  reference graphics. PRESERVED AND AUDITABLE, not modified and "
          "not",
          "  overwritten. It is no longer the active production handoff.", "",
          hr(), "", "WHAT EACH PACKAGE COPIES UNCHANGED", "",
          "  01_Recording_Master holds the story-led script and its thought "
          "block,",
          "  both copied byte for byte and never written to. No "
          "pre-story-led master",
          "  is present in that folder, so two files can never appear "
          "equally current.",
          ""]
    return mono(path, L)


def asset_table(path, s):
    from collections import Counter
    rows = [(n, f) for n in M.VIDEOS for f in SETS[n]]
    cnt = Counter(f["status"] for _, f in rows)
    L = head("VIDEOS 4 TO 21  |  ASSET REUSE AND CHANGE TABLE")
    L += ["Generated: %s" % s, "", hr(), "", "THE TEST", "",
          "  An asset is not rebuilt because a sentence was reworded. Each "
          "existing",
          "  visual was checked against the story-led script and classified "
          "by what",
          "  the evidence supports.", "", hr(), "", "CLASSIFICATION", ""]
    for k in ("REUSE", "COPY UPDATE", "REBUILD", "NEW"):
        if cnt.get(k):
            L += ["    %-14s %d" % (k, cnt[k])]
    L += ["    %-14s %d" % ("REMOVE", len(REMOVED)), "", hr(), "",
          "EVERY ASSET", "",
          "  %-36s %-13s %-12s %s" % ("ASSET", "STATUS", "TREATMENT", "CUE"),
          "  " + "-" * 112]
    for n, f in rows:
        L += ["  %-36s %-13s %-12s %s"
              % (f["key"], f["status"], visualdir_sl.treatment(f["key"])[0],
                 f["trigger"][:44])]
    L += ["", hr(), "", "WHY EACH CHANGED ASSET CHANGED", ""]
    for n, f in rows:
        if f["status"] != "REUSE":
            L += ["  V%-3d %s  [%s]" % (n, f["key"], f["status"])]
            L += ["        %s" % x for x in _wrap(f["why"], 70)]
            L += [""]
    L += [hr(), "", "REMOVED, AND WHY", ""]
    for k, v in REMOVED.items():
        L += ["  %s" % k] + ["      %s" % x for x in _wrap(v, 70)] + [""]
    L += [hr(), "", "SHORTS", ""]
    sc = Counter(st for _, (_, st, _, _) in
                 [(n, r) for n in M.VIDEOS for r in shorts_sl.audit(n)])
    for k, v in sc.items():
        L += ["    %-14s %d" % (k, v)]
    L += ["", "  No Short was rebuilt or removed. Every framework a Short "
          "rests on is",
          "  still taught in the story-led script; where the long-form "
          "reworded the",
          "  supporting lines, the Short's wording was brought to the "
          "current script.",
          ""]
    return mono(path, L)


def superseded_index(path, s):
    L = head("VIDEOS 4 TO 21  |  SUPERSEDED MATERIALS INDEX")
    L += ["Generated: %s" % s, "", hr(), "",
          "PRE-STORY-LED PRODUCTION BASELINE", "",
          "  Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip",
          "  SHA-256 %s" % BASELINE_SHA, "",
          "  Superseded as the active handoff by this pass. PRESERVED and "
          "auditable.",
          "  Not modified and not overwritten. Use it for history, not for "
          "recording.",
          "", hr(), "", "SUPERSEDED RECORDING MASTERS", "",
          "  Every pre-story-led recording master for V4 to V21, including "
          "the",
          "  September 11 corrected masters and the September 12 restored "
          "V6, V7 and",
          "  V8 derivatives. All remain in the previous package. None is "
          "active.",
          "", hr(), "", "SUPERSEDED THOUGHT BLOCKS", "",
          "  Every pre-story-led thought-block document for V4 to V21. The "
          "story-led",
          "  ZIP supplies their replacements, and no second parallel set is "
          "made.",
          "", hr(), "", "SUPERSEDED VISUAL ASSETS", ""]
    for k, v in REMOVED.items():
        L += ["  %s.png" % k] + ["      %s" % x for x in _wrap(v, 70)] + [""]
    L += [hr(), "", "SUPERSEDED THUMBNAIL WORDING", ""]
    if publish_sl.THUMB_CHANGED:
        for n, was in publish_sl.THUMB_CHANGED.items():
            L += ["  V%-3d was %r" % (n, was),
                  "        now %r" % PK.thumbnail(n), ""]
    else:
        L += ["  None. Every thumbnail of record is the locked V4 to V21",
              "  roadmap wording, unchanged by this pass.", ""]
    L += [hr(), "", "THUMBNAIL METADATA EXCEPTIONS", ""]
    if PK.exceptions():
        L += ["  %s" % x for x in _wrap(PK.EXCEPTION_NOTE, 70)] + [""]
        for n, hdr, rec in PK.exceptions():
            L += ["  V%-3d script header metadata  %r" % (n, hdr),
                  "        thumbnail of record    %r" % rec, ""]
    else:
        L += ["  None in this package.", ""]
    L += [hr(), "", "SUPERSEDED PUBLISHING COPY", ""]
    for n, what in publish_sl.CHANGED.items():
        L += ["  V%-3d the %s, because the story-led script changed the hook "
              "framing" % (n, what),
              "        it described. No other publishing copy was "
              "rewritten.", ""]
    return mono(path, L)


def change_log_batch(path, s):
    from collections import Counter
    cnt = Counter(f["status"] for n in M.VIDEOS for f in SETS[n])
    L = head("VIDEOS 4 TO 21  |  STORY-LED SYNCHRONIZATION CHANGE LOG")
    L += ["Generated: %s" % s, "", hr(), "",
          "PREVIOUS DELIVERY", "",
          "  Clearer, simplified, production-synchronized teaching.", "",
          "NEW DELIVERY", "",
          "  Story-led conversational teaching.", "",
          "WHAT THE CHANGE IS", "",
          "  A delivery and sequencing layer that helps the viewer recognize "
          "the",
          "  situation before receiving the framework.", "",
          "WHAT THE CHANGE IS NOT", "",
          "  Not a framework rebuild. Not a runtime-strategy rebuild. Not an "
          "offer",
          "  rebuild. Not a roadmap rebuild.", "", hr(), "",
          "RUNTIME", "",
          "  %-4s %-14s %-8s %s" % ("V", "CLASS", "WORDS", "ESTIMATED "
                                    "SPEECH"),
          "  " + "-" * 56]
    for n in M.VIDEOS:
        w, fast, slow = M.estimate(n)
        L += ["  %-4s %-14s %-8d %s to %s"
              % ("V%d" % n, "SHORTER TEST" if n in M.SHORT_TEST
                 else "LONG-FORM", w, fast, slow)]
    L += ["",
          "  Every figure is arithmetic on the script at 130 to 145 words "
          "per minute.",
          "  None is a runtime and none is a target. Videos 4 and 5 have no "
          "locked",
          "  five-minute target: that predates the September 13 expansion. "
          "Actual",
          "  runtime is observed at Temidayo's natural delivery pace.", "",
          "  Nothing was compressed. Every script grew.", "", hr(), "",
          "WHICH VISUAL MAPS CHANGED", "",
          "  All eighteen. The trigger map is now a camera and full-screen "
          "spine that",
          "  marks every stretch of the video, because a map that lists only "
          "graphics",
          "  cannot show where the camera-led moments are.", "",
          "WHICH RIVERSIDE PROMPTS CHANGED", "",
          "  All eighteen, rewritten rather than renamed. Each one now "
          "states where to",
          "  stay on camera, and specifies what every graphic actually is "
          "rather than",
          "  asking for a visual.", "", "WHICH SHORTS CHANGED", ""]
    sc = Counter(st for n in M.VIDEOS for _, st, _, _ in shorts_sl.audit(n))
    for k, v in sc.items():
        L += ["    %-14s %d" % (k, v)]
    L += ["", "WHICH PUBLISHING MATERIALS CHANGED", ""]
    for n, what in publish_sl.CHANGED.items():
        L += ["    V%-3d %s" % (n, what)]
    if publish_sl.THUMB_CHANGED:
        for n, was in publish_sl.THUMB_CHANGED.items():
            L += ["    V%-3d thumbnail wording, from %r to %r"
                  % (n, was, PK.thumbnail(n))]
    else:
        L += ["    No thumbnail wording changed. Every thumbnail of record "
              "is the",
              "    locked V4 to V21 roadmap wording."]
    L += ["", "THUMBNAIL METADATA EXCEPTIONS", ""]
    for n, hdr, rec in PK.exceptions():
        L += ["    V%-3d script header says %r" % (n, hdr),
              "         thumbnail of record  %r" % rec]
    L += ["", "    The script layer is authoritative for spoken wording and "
              "recording",
          "    delivery. Its header thumbnail text is non-spoken metadata "
          "and is not",
          "    packaging authority. No source document was edited and no "
          "source hash",
          "    changed."]
    L += ["", "WHICH ASSETS REMAINED BYTE-IDENTICAL", "",
          "    %d of %d carried across with the card unchanged."
          % (cnt.get("REUSE", 0), sum(cnt.values())),
          "", "WHICH ASSETS WERE REMOVED BECAUSE THEY INTERRUPTED STORY-LED "
          "DELIVERY", ""]
    for k, v in REMOVED.items():
        L += ["    %s" % k] + ["        %s" % x for x in _wrap(v, 68)] + [""]
    L += [hr(), "", "ASSET CLASSIFICATION", ""]
    for k in ("REUSE", "COPY UPDATE", "REBUILD", "NEW"):
        if cnt.get(k):
            L += ["    %-14s %d" % (k, cnt[k])]
    L += ["    %-14s %d" % ("REMOVE", len(REMOVED)), "", hr(), "",
          "VISUAL DIRECTION ADDED BY THIS PASS", ""]
    for s_ in visualdir_sl.STANDING:
        L += ["  %s" % x for x in _wrap(s_, 72)] + [""]
    L += [hr(), "", "THE PRE-STORY-LED BASELINE", "",
          "  Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip",
          "  SHA-256 %s" % BASELINE_SHA, "",
          "  Preserved and auditable. Not modified, not overwritten, and no "
          "longer",
          "  the active production handoff.", ""]
    return mono(path, L)


def sha_manifest(path, s, results):
    L = head("VIDEOS 4 TO 21  |  STORY-LED SHA-256 MANIFEST")
    L += ["Generated: %s" % s, "", hr(), "", "SPOKEN SOURCE OF TRUTH", ""]
    for n in M.VIDEOS:
        L += ["  %s  %s" % (M.read(n)["sha"], os.path.basename(M.path(n)))]
        L += ["  %s  %s" % (M.sha256(M.path(n, True)),
                            os.path.basename(M.path(n, True)))]
    L += ["", hr(), "", "PACKAGE ARCHIVES", ""]
    for n in M.VIDEOS:
        L += ["  %s  %s" % (results[n]["sha"],
                            os.path.basename(results[n]["zip"]))]
    L += ["", hr(), "", "EVERY FILE IN EVERY PACKAGE", ""]
    for n in M.VIDEOS:
        pkg = results[n]["pkg"]
        L += ["  VIDEO %d" % n, ""]
        for root, _, files in sorted(os.walk(pkg)):
            for fn in sorted(files):
                p = os.path.join(root, fn)
                L += ["    %s  %s" % (sha256(p), os.path.relpath(p, pkg))]
        L += [""]
    L += [hr(), "",
          "  The combined archive's checksum is written beside it in a "
          "sibling file,",
          "  never inside it.", ""]
    return mono(path, L)


def qa_summary(path, s, results):
    L = head("VIDEOS 4 TO 21  |  STORY-LED PACKAGE QA SUMMARY")
    total = sum(r["total"] for r in results.values())
    passed = sum(r["passed"] for r in results.values())
    L += ["Generated: %s" % s, "",
          "%d package checks. %d passed, %d failed."
          % (total, passed, total - passed), "",
          "Every check ran against the built package on disk, not against "
          "build data,",
          "so a check cannot pass because of something that was true only "
          "in a module.",
          "", hr(), ""]
    for n in M.VIDEOS:
        r = results[n]
        L += ["VIDEO %d   %d of %d" % (n, r["passed"], r["total"]), ""]
        for name, ok, detail in r["rows"]:
            L += ["  [%s] %s" % ("PASS" if ok else "FAIL", name)]
            d = detail if isinstance(detail, str) else "; ".join(map(str, detail))
            L += ["         %s" % d]
        L += [""]
    L += [hr(), "", "FINAL-EXPORT QA, STILL PENDING", "",
          "  Not complete and not claimed. These cannot be checked until the "
          "video has",
          "  been recorded, edited and exported.", ""]
    for x in ("Actual recorded runtime", "Actual pacing", "Executed jump cuts",
              "Executed push-ins and pull-backs", "Final graphics",
              "B-roll placement", "Audio clarity", "Final loudness",
              "Music and effects balance", "Final picture quality",
              "Final SRT synchronization", "Chapter timestamps",
              "Final Watch Next hold", "Thumbnail artwork",
              "Public URL verification", "Clean final export ending"):
        L += ["  [ PENDING ] %s" % x]
    L += [""]
    return mono(path, L)


def main():
    s = stamp()
    print("stamp:", s)
    M.verify_all()
    print("all 36 story-led source files verified against intake hashes")

    src_fail = [(n, nm) for n in M.VIDEOS for nm, ok, _ in srcqa_sl.check(n)
                if not ok]
    if src_fail:
        raise SystemExit("source QA failed: %s" % src_fail)
    print("source QA: all pass")

    ed = editorial_sl.failures()
    if ed:
        raise SystemExit("editorial check failed: %s" % ed)
    print("editorial check: 18 videos, all pass")

    rows, bad, typo = wncheck_sl.check()
    if bad:
        raise SystemExit("Watch Next mismatch: %s" % bad)
    print("Watch Next: %d cards, 0 mismatches" % len(rows))

    # A correction pass rebuilds only the packages its corrections
    # invalidate. Every other package is left exactly as it is on disk, and
    # QA still runs against it, so the check count covers all eighteen
    # whether or not they were rewritten this run.
    only = os.environ.get("REBUILD_ONLY", "").strip()
    rebuild = ({int(x) for x in only.replace(",", " ").split()} if only
               else set(M.VIDEOS))
    if only:
        print("rebuilding only: %s" % ", ".join("V%d" % n
                                                for n in sorted(rebuild)))
        print("every other package is left untouched and re-checked in place")

    results = {}
    for n in M.VIDEOS:
        zp = os.path.join(OUT, "Video_%d_Story_Led_Package.zip" % n)
        if n in rebuild:
            pkg = build_one(n, s)
            qa_rows = qa_sl.run(n, pkg)
            z, cnt = zip_dir(pkg, zp)
            mark = ""
        else:
            pkg = os.path.join(OUT, "VIDEO_%d_STORY_LED_PACKAGE" % n)
            qa_rows = qa_sl.run(n, pkg)
            z = zp
            cnt = sum(len(f) for _, _, f in os.walk(pkg))
            mark = "  unchanged"
        passed = sum(1 for _, ok, _ in qa_rows if ok)
        results[n] = dict(pkg=pkg, zip=z, files=cnt, rows=qa_rows,
                          passed=passed, total=len(qa_rows), sha=sha256(z))
        print("V%-3d %2d/%2d checks  %3d files%s" % (n, passed, len(qa_rows),
                                                     cnt, mark))
        for name, ok, detail in qa_rows:
            if not ok:
                print("        FAIL %s :: %s" % (name, detail))

    batch = [
      source_hierarchy(os.path.join(OUT, "Source_Hierarchy_Manifest.txt"), s),
      change_log_batch(os.path.join(
          OUT, "Story_Led_Synchronization_Change_Log.txt"), s),
      asset_table(os.path.join(OUT, "Asset_Reuse_and_Change_Table.txt"), s),
      superseded_index(os.path.join(OUT, "Superseded_Materials_Index.txt"), s),
      qa_summary(os.path.join(OUT, "QA_Summary.txt"), s, results),
      sha_manifest(os.path.join(OUT, "SHA256_Manifest.txt"), s, results),
    ]

    zpath = os.path.join(OUT, ARCHIVE)
    if os.path.exists(zpath):
        os.remove(zpath)
    members = []
    for n in M.VIDEOS:
        members += [results[n]["zip"], results[n]["zip"] + ".sha256"]
    members += batch
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for p in sorted(members):
            info = zipfile.ZipInfo(os.path.basename(p), date_time=ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(p, "rb") as f:
                z.writestr(info, f.read())
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), ARCHIVE))

    total = sum(r["total"] for r in results.values())
    passed = sum(r["passed"] for r in results.values())
    print()
    print("  %-58s %d entries" % (ARCHIVE, len(members)))
    print("  sha256 %s" % sha256(zpath))
    print("  package checks: %d of %d passed" % (passed, total))
    return results


if __name__ == "__main__":
    main()
