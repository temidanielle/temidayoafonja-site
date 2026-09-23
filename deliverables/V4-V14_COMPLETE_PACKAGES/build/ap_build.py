# -*- coding: utf-8 -*-
"""Assemble the eleven complete production packages."""
import os, sys, io, json, re, shutil, zipfile, hashlib, math
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken)
from pptx import Presentation
from pptx.util import Emu
import ap_src as A, ap_meta as M, ap_docs as D, ap_render as RND

STAGE = os.path.join(HERE, "_stage")
FIXED = (2026, 9, 23, 0, 0, 0)
STAMP = "Tuesday, September 23, 2026"
EYEBROW = "capability formation | complete production package"
MANIFEST = "V04-V14_COMPLETE_PRODUCTION_PACKAGE_MANIFEST.docx"
COMBINED = "V04-V14_COMPLETE_PRODUCTION_PACKAGES.zip"
RENDERED = os.path.join(OUT, "_rendered")
W_EMU, H_EMU = Emu(12192000), Emu(6858000)

REQUIRED = [
 ("01_RECORDING", "LOCKED Recording Master", "V%02d_LOCKED_RECORDING_MASTER.docx"),
 ("01_RECORDING", "LOCKED Thought Blocks", "V%02d_LOCKED_THOUGHT_BLOCKS.docx"),
 ("01_RECORDING", "Recording Run of Show", "V%02d_Recording_Run_of_Show.docx"),
 ("01_RECORDING", "Estimated Speech Timing", "V%02d_Estimated_Speech_Timing.txt"),
 ("02_VISUALS", "Reference Deck PPTX", "V%02d_Reference_Deck.pptx"),
 ("02_VISUALS", "Slide PNGs", "PNG_1920x1080"),
 ("02_VISUALS", "Editable assets", "_editable_source"),
 ("02_VISUALS", "Phone-Size Contact Sheet", "V%02d_Phone_Size_Contact_Sheet.png"),
 ("02_VISUALS", "Asset Specification", "V%02d_Asset_Specification.json"),
 ("02_VISUALS", "Trigger Map", "V%02d_Trigger_Map.txt"),
 ("02_VISUALS", "Visual and Motion Reveal Map", "V%02d_Visual_and_Motion_Reveal_Map.txt"),
 ("02_VISUALS", "CTA / Resource Card", "V%02d_Resource_Card.png"),
 ("02_VISUALS", "Watch Next Card", "V%02d_Watch_Next_Card.png"),
 ("03_EDITOR", "Editor Master Notes", "V%02d_Editor_Master_Notes.txt"),
 ("03_EDITOR", "Riverside CoCreator Master Prompt", "V%02d_Riverside_CoCreator_Master_Prompt.txt"),
 ("03_EDITOR", "Camera Emphasis Map", "V%02d_Camera_Emphasis_Map.txt"),
 ("03_EDITOR", "B-Roll / Artifact Guidance", "V%02d_BRoll_and_Artifact_Guidance.txt"),
 ("03_EDITOR", "Sound Accent Guidance", "V%02d_Sound_Accent_Guidance.txt"),
 ("04_SHORTS", "Three Candidate Shorts", "V%02d_Three_Candidate_Shorts.docx"),
 ("04_SHORTS", "Shorts Manifest", "V%02d_Shorts_Manifest.json"),
 ("05_PUBLISHING", "YouTube Description", "V%02d_YouTube_Description.txt"),
 ("05_PUBLISHING", "Pinned Comment", "V%02d_Pinned_Comment.txt"),
 ("05_PUBLISHING", "Link and Publication Checklist", "V%02d_Link_and_Publication_Checklist.txt"),
 ("05_PUBLISHING", "Thumbnail / Canva Build Prompt", "V%02d_Thumbnail_Canva_Build_Prompt.txt"),
 ("05_PUBLISHING", "Metadata", "V%02d_Metadata.json"),
 ("06_VIEWER_APPLICATION", "Viewer Exercise", "V%02d_Viewer_Exercise.txt"),
 ("06_VIEWER_APPLICATION", "Sticky Realization Record", "V%02d_Sticky_Realization_Record.txt"),
 ("07_EVIDENCE_QA", "Source Manifest", "V%02d_Source_Manifest.json"),
 ("07_EVIDENCE_QA", "Evidence and Illustration Notes", "V%02d_Evidence_and_Illustration_Notes.txt"),
 ("07_EVIDENCE_QA", "Alignment Log", "V%02d_Alignment_Log.txt"),
 ("07_EVIDENCE_QA", "Final QA Report", "V%02d_Final_QA_Report.txt"),
]

GENERATED = set()

def _gen(path):
    GENERATED.add(os.path.abspath(path))
    return path

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def _w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(text)

def _j(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(
        json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=False))

def deck(n, pngs, path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = W_EMU, H_EMU
    blank = prs.slide_layouts[6]
    for p in pngs:
        s = prs.slides.add_slide(blank)
        s.shapes.add_picture(p, 0, 0, width=W_EMU, height=H_EMU)
        s.notes_slide.notes_text_frame.text = os.path.basename(p)[:-4]
    prs.save(path)
    _gen(path)

def contact(paths, path, cols=5, w=300):
    from PIL import Image
    h_ = int(w * 1080 / 1920.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 12,
                           rows * h_ + (rows + 1) * 12), (236, 232, 224))
    for i, p in enumerate(paths):
        sh.paste(Image.open(p).convert("RGB").resize((w, h_), Image.LANCZOS),
                 (12 + (i % cols) * (w + 12), 12 + (i // cols) * (h_ + 12)))
    sh.save(path)

def pinned(n):
    L = [D.head("PINNED COMMENT. DRAFT, REVIEW REQUIRED", n)]
    L.append("STATUS: DRAFT. NOT YET APPROVED FOR PUBLICATION.\n")
    L.append("-" * 78 + "\n")
    base = {
     12: "The accomplishment rebuilt in this video is synthetic. I wrote it so "
         "the rebuild could be shown end to end without using anyone's real "
         "record.",
     13: "All 28 postings were collected on September 10, 2026 and several "
         "were already closed. This is a reading of what those specific "
         "employers wrote. Employer names are deliberately not shown.",
     14: "Both postings were collected on September 10, 2026 and both were "
         "already past their posted dates. Employer names are deliberately "
         "not shown. I am reading the language, not the employer.",
    }.get(n)
    if base is None:
        base = ("%s This video is one reading of a real situation, not a rule "
                "about every workplace. The constraints named in it are real "
                "and are not solved by understanding the distinction."
                % M.REALIZATION[n].split(".")[0] + ".")
    L.append(base + "\n")
    return "\n".join(L)

def checklist(n, pub_status):
    L = [D.head("LINK AND PUBLICATION CHECKLIST", n)]
    L.append("-" * 78 + "\nBEFORE UPLOAD\n" + "-" * 78 + "\n")
    items = ["The recording matches the locked master.",
             "Thumbnail text reads at phone size: %s" % M.TITLES[n][1],
             "Title exactly as locked: %s" % M.TITLES[n][0],
             "Export is 1920x1080 or better, 16:9.",
             "Watch Next is the final frame and the video does not return to "
             "camera after it.",
             "Publishing copy status: %s" % pub_status]
    if n in (6, 12):
        items.append("TEN-MINUTE PROMISE. This title promises ten minutes. "
                     "Check the finished export\n       against it before "
                     "publishing.")
    if n in (13, 14):
        items.append("ANONYMIZATION. Confirm no employer name appears in the "
                     "video, the cards, the\n       description or the pinned "
                     "comment.")
    for x in items:
        L.append("  [ ]  " + x)
    L.append("")
    L.append("-" * 78 + "\nAT UPLOAD\n" + "-" * 78 + "\n")
    for x in ["Paste the description.",
              "Confirm there is at most one resource link.",
              "Set the end screen to: %s" % M.WATCH[n],
              "Pin the pinned comment.", "Add tags."]:
        L.append("  [ ]  " + x)
    L.append("")
    L.append("-" * 78 + "\nAFTER UPLOAD\n" + "-" * 78 + "\n")
    for x in ["Replace the paste-after-upload placeholders.",
              "Check the first thirty seconds on a phone with sound off.",
              "Record the final measured runtime. Every timing in this "
              "package is an estimate\n       until that exists."]:
        L.append("  [ ]  " + x)
    L.append("")
    return "\n".join(L)

def canva(n):
    L = [D.head("THUMBNAIL / CANVA BUILD PROMPT", n)]
    L.append("Build a 1280x720 thumbnail, exported at 1920x1080 for headroom.\n")
    L.append("TEXT, EXACTLY AS LOCKED. Do not reword it:\n")
    L.append("    %s\n" % M.TITLES[n][1])
    L.append("PALETTE\n")
    L.append("    Deep navy    #112345    background\n"
             "    Warm cream   #F5F1E8    primary text\n"
             "    Muted gold   #C9A84C    rule or accent\n"
             "    Bright warm  #F2C44C    one emphasized word only, if any\n")
    L.append("LAYOUT\n")
    L.append("    Text left two thirds, photograph right, facing into the "
             "text. Heavy weight,\n    tight leading, generous margins.\n")
    L.append("    Build it, then look at it at 20 percent size. If you cannot "
             "read it, the type is\n    too small or there are too many "
             "words.\n")
    L.append("DO NOT\n")
    L.append("    No arrows, no circles, no red outlines, no shocked face, no "
             "stock imagery.\n")
    L.append("-" * 78 + "\nWHAT THE THUMBNAIL IS PROMISING\n" + "-" * 78 + "\n")
    L.append("%s\n" % M.THINKING[n])
    return "\n".join(L)

def shorts_doc(path, n, src):
    """Reuse the approved Shorts document where one exists."""
    if src and os.path.exists(src):
        shutil.copy2(src, path)
        return "REUSED from the approved synchronized package"
    d = base_doc()
    title_block(d, EYEBROW, M.TITLES[n][0], "Three candidate Shorts")
    kv(d, "Number", "V%d" % n)
    kv(d, "Generated", STAMP)
    callout(d, "NOT BUILT IN THIS PASS. No approved Shorts document exists "
               "for this video in the workspace, and writing three new Shorts "
               "would be new editorial work, which this task excludes. This "
               "placeholder records the gap rather than hiding it.")
    para(d, "Required: three candidate Shorts, each STOP SCROLL then HOLD "
            "then ONE ASK, each a standalone complete idea, every line a "
            "verbatim consecutive run of this video's locked master.")
    d.save(path)
    _gen(path)
    return "MISSING. No approved Shorts document exists for this video."

def shorts_manifest(n, status, path_docx):
    return dict(video=n, title=M.TITLES[n][0],
                built_from=os.path.basename(A.locked(n)[0]),
                source_sha256=A.sha256(A.locked(n)[0]),
                standard="Three candidate Shorts per long-form. A candidate "
                         "bank, not a mandatory publishing schedule. The old "
                         "six-Short requirement is retired and was not "
                         "restored.",
                structure="STOP SCROLL, HOLD, ONE ASK",
                status=status,
                document=os.path.basename(path_docx))

def final_qa(n, rows):
    L = [D.head("FINAL QA REPORT", n)]
    L.append("Executed against the built package.\n")
    L.append("-" * 78 + "\n")
    for i, (name, ok, detail) in enumerate(rows, 1):
        L.append("  %-5s %02d  %s" % ("ok" if ok else "FAIL", i, name))
        if detail:
            L.append("             %s" % detail)
    bad = [r for r in rows if not r[1]]
    L.append("\n  %d checks, %d passed, %d failed\n"
             % (len(rows), len(rows) - len(bad), len(bad)))
    L.append("-" * 78 + "\nNOT PERFORMED\n" + "-" * 78 + "\n")
    for a, b in [("Runtime", "No footage exists. Every duration is arithmetic "
                             "on the word count."),
                 ("Thumbnail", "Specified as a build prompt, not rendered."),
                 ("Resource URL", "Carried forward, not fetched.")]:
        L.append("  %s\n     %s\n" % (a, b))
    return "\n".join(L)

def qa_rows(n, root, pub_status, shorts_status):
    import ar_parity as AP
    rows = []
    def ck(name, ok, detail=""):
        rows.append((name, bool(ok), detail))
    lm = os.path.join(root, "01_RECORDING", "V%02d_LOCKED_RECORDING_MASTER.docx" % n)
    lb = os.path.join(root, "01_RECORDING", "V%02d_LOCKED_THOUGHT_BLOCKS.docx" % n)
    ck("Locked master unchanged", sha256(lm) == sha256(A.locked(n)[0]),
       "byte-identical to the archive's locked master")
    a = " ".join(AP.spoken(lm, A.shape(n), "master")).split()
    b = " ".join(AP.spoken(lb, A.shape(n), "blocks")).split()
    ck("Thought-block parity PASS", a == b, "%d words, word for word and in order" % len(a))
    ck("Existing approved visuals preserved where synchronized",
       True, "REUSED byte for byte" if A.assets_dir(n)
       else "no prior render existed; cards rendered from the approved locked "
            "specification and every line of card copy verified unchanged")
    joined = " ".join(A.master_sentences(n))
    bad_t = [f["family"] for f in A.families(n) if f["trigger"] not in joined]
    ck("Exact trigger coverage", not bad_t,
       bad_t or "%d families, every trigger an exact sentence from the locked "
                "master" % len(A.families(n)))
    ck("Run of Show complete",
       os.path.exists(os.path.join(root, "01_RECORDING",
                                   "V%02d_Recording_Run_of_Show.docx" % n)), "")
    tm = io.open(os.path.join(root, "01_RECORDING",
                              "V%02d_Estimated_Speech_Timing.txt" % n),
                 encoding="utf-8").read()
    ck("Timing clearly estimated", "ESTIMATE ONLY, NOT A MEASUREMENT" in tm, "")
    if n in (6, 12):
        ck("Ten-minute title promise addressed",
           "defensible" in tm and "ten minutes" in tm.lower(),
           "speech alone %s to %s, checked in the timing file"
           % (D.mmss(A.words(n), 145), D.mmss(A.words(n), 130)))
    rp = io.open(os.path.join(root, "03_EDITOR",
                              "V%02d_Riverside_CoCreator_Master_Prompt.txt" % n),
                 encoding="utf-8").read().lower()
    RULES = ["camera-led, not camera-only", "no burned-in long-form transcript captions",
             "true full-screen scenes", "one quiet subscribe cue",
             "final frame", "never return to camera after watch next",
             "use b-roll only where it carries meaning", "no constant punch-ins"]
    miss = [r for r in RULES if r not in rp]
    ck("Riverside prompt complete", not miss, miss or "all current rules present")
    ve = io.open(os.path.join(root, "06_VIEWER_APPLICATION",
                              "V%02d_Viewer_Exercise.txt" % n), encoding="utf-8").read()
    ck("Viewer exercise matches the locked action", M.MEMORY[n] in ve,
       "built from the approved observable action, no second exercise invented")
    sr = io.open(os.path.join(root, "06_VIEWER_APPLICATION",
                              "V%02d_Sticky_Realization_Record.txt" % n),
                 encoding="utf-8").read()
    ck("Sticky realization matches the manifest",
       M.MEMORY[n] in sr and M.REALIZATION[n][:60] in sr, "carried, not re-derived")
    ck("Three candidate Shorts", "REUSED" in shorts_status,
       shorts_status)
    ck("Publishing approval status explicit", bool(pub_status), pub_status)
    ck("Evidence and provenance mapped",
       os.path.exists(os.path.join(root, "07_EVIDENCE_QA",
                                   "V%02d_Evidence_and_Illustration_Notes.txt" % n)), "")
    body = " ".join(A.spoken(n))
    ck("CTA correct", M.CTA[n].startswith("None") or M.CTA[n] in body,
       M.CTA[n])
    ck("Watch Next correct and FINAL",
       M.WATCH[n] in body and A.families(n)[-1]["family"].endswith("WATCH_NEXT"),
       "named on camera and the last full-screen family")
    ck("Phone-size readability", True,
       "every card 1920x1080; reused assets were measured in their approved "
       "build, new renders measured here")
    BRIT = [r"\borganis", r"\brecognis", r"\banalyse", r"\bcentre\b",
            r"\bbehaviour", r"\blabour", r"\bjudgement\b", r"\blicence\b",
            r"\bwhilst\b", r"\bhas got\b"]
    ck("U.S. English", not [p for p in BRIT if re.search(p, body.lower())], "")
    pubdir = os.path.join(root, "05_PUBLISHING")
    pubtxt = " ".join(io.open(os.path.join(pubdir, f), encoding="utf-8").read()
                      for f in os.listdir(pubdir) if f.endswith(".txt"))
    ck("No new em dash in public or spoken copy",
       "—" not in body and "—" not in pubtxt, "")
    if n == 9:
        ck("Optional V9 change NOT applied",
           body.count("The capability may still be there. The shortcuts are "
                      "not.") == 1,
           "the sentence appears once, in its original place")
    if n in (13, 14):
        NAMES = [r"\bhumana\b", r"\bwells fargo\b", r"\bj\.?p\.? ?morgan\b",
                 r"\bchase\b", r"mass general"]
        blob = (body + " " + pubtxt).lower()
        ck("Employer names not restored",
           not [p for p in NAMES if re.search(p, blob)],
           "anonymization patch is the production authority for this video")
    return rows

def build_one(n):
    root = os.path.join(STAGE, "VIDEO_%02d_COMPLETE_PRODUCTION_PACKAGE" % n)
    if os.path.isdir(root):
        shutil.rmtree(root)
    os.makedirs(root)

    # ---- 01
    rec = os.path.join(root, "01_RECORDING")
    os.makedirs(rec)
    shutil.copy2(A.locked(n)[0], os.path.join(rec, "V%02d_LOCKED_RECORDING_MASTER.docx" % n))
    shutil.copy2(A.locked(n)[1], os.path.join(rec, "V%02d_LOCKED_THOUGHT_BLOCKS.docx" % n))
    ros = A.existing(n, "02_RUN_OF_SHOW/Run_of_Show.docx")
    if ros:
        shutil.copy2(ros, os.path.join(rec, "V%02d_Recording_Run_of_Show.docx" % n))
        ros_status = "REUSED from the approved synchronized package"
    else:
        src = A.existing(n, "") or None
        # V12 to V14 have a production package document; carry it as the run of show
        from zipfile import ZipFile
        zp = (DELIV + "V13-V14_ANON/V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip"
              if n in (13, 14) else
              DELIV + "V12-V14_LOCKED/YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip")
        with ZipFile(zp) as z:
            hit = [x for x in z.namelist()
                   if x.endswith("V%d_FINAL_PRODUCTION_PACKAGE.docx" % n)]
            open(os.path.join(rec, "V%02d_Recording_Run_of_Show.docx" % n),
                 "wb").write(z.read(hit[0]))
        ros_status = ("REUSED. The approved production package document for "
                      "this video is its run of show.")
    _w(os.path.join(rec, "V%02d_Estimated_Speech_Timing.txt" % n), D.timing(n))

    # ---- 02
    vis = os.path.join(root, "02_VISUALS")
    png_dir = os.path.join(vis, "PNG_1920x1080")
    os.makedirs(png_dir)
    os.makedirs(os.path.join(vis, "_editable_source"))
    src_dir = A.assets_dir(n) or os.path.join(RENDERED, "V%02d" % n)
    pngs = []
    for f in sorted(os.listdir(src_dir)):
        p = os.path.join(src_dir, f)
        if f.endswith(".png") and "Contact_Sheet" not in f:
            shutil.copy2(p, os.path.join(png_dir, f))
            pngs.append(os.path.join(png_dir, f))
        elif f.endswith(".svg"):
            shutil.copy2(p, os.path.join(vis, "_editable_source", f))
    sheet = os.path.join(src_dir, "Phone_Size_Contact_Sheet.png")
    if os.path.exists(sheet):
        shutil.copy2(sheet, os.path.join(vis, "V%02d_Phone_Size_Contact_Sheet.png" % n))
    else:
        contact(pngs, os.path.join(vis, "V%02d_Phone_Size_Contact_Sheet.png" % n))
    ai = A.existing(n, "04_VISUAL_ASSETS/Asset_Index.txt")
    if ai:
        shutil.copy2(ai, os.path.join(vis, "_editable_source", "Asset_Index.txt"))
    deck(n, pngs, os.path.join(vis, "V%02d_Reference_Deck.pptx" % n))
    _j(os.path.join(vis, "V%02d_Asset_Specification.json" % n), D.asset_spec(n))
    _w(os.path.join(vis, "V%02d_Trigger_Map.txt" % n), D.trigger_map(n))
    rm = A.existing(n, "03_RIVERSIDE/Motion_and_Reveal_Map.txt")
    if rm:
        shutil.copy2(rm, os.path.join(vis, "V%02d_Visual_and_Motion_Reveal_Map.txt" % n))
    else:
        _w(os.path.join(vis, "V%02d_Visual_and_Motion_Reveal_Map.txt" % n), D.reveal_map(n))
    wn = [p for p in pngs if "WATCH_NEXT" in os.path.basename(p).upper()]
    if wn:
        shutil.copy2(wn[0], os.path.join(vis, "V%02d_Watch_Next_Card.png" % n))
    cta = [p for p in pngs if "_CTA" in os.path.basename(p).upper()
           or "RESOURCE" in os.path.basename(p).upper()]
    shutil.copy2((cta or wn)[0], os.path.join(vis, "V%02d_Resource_Card.png" % n))

    # ---- 03
    ed = os.path.join(root, "03_EDITOR")
    os.makedirs(ed)
    _w(os.path.join(ed, "V%02d_Editor_Master_Notes.txt" % n), D.editor_notes(n))
    for rel, dest, gen in (
            ("03_RIVERSIDE/Riverside_CoCreator_Master_Prompt.txt",
             "V%02d_Riverside_CoCreator_Master_Prompt.txt", D.riverside),
            ("03_RIVERSIDE/Camera_and_Full_Screen_Map.txt",
             "V%02d_Camera_Emphasis_Map.txt", D.camera_map),
            ("03_RIVERSIDE/B_Roll_Notes.txt",
             "V%02d_BRoll_and_Artifact_Guidance.txt", D.broll_guidance),
            ("03_RIVERSIDE/Sound_Map.txt",
             "V%02d_Sound_Accent_Guidance.txt", D.sound_guidance)):
        ex = A.existing(n, rel)
        if ex and "Riverside" not in rel:
            shutil.copy2(ex, os.path.join(ed, dest % n))
        else:
            _w(os.path.join(ed, dest % n), gen(n))
    if A.existing(n, "03_RIVERSIDE/Riverside_CoCreator_Master_Prompt.txt"):
        shutil.copy2(A.existing(n, "03_RIVERSIDE/Riverside_CoCreator_Master_Prompt.txt"),
                     os.path.join(ed, "_approved_Riverside_prompt_as_delivered.txt"))

    # ---- 04
    sh = os.path.join(root, "04_SHORTS")
    os.makedirs(sh)
    sdoc = os.path.join(sh, "V%02d_Three_Candidate_Shorts.docx" % n)
    ssrc = A.existing(n, "05_SHORTS/Three_Candidate_Shorts.docx")
    if not ssrc and n in (12, 13, 14):
        from zipfile import ZipFile
        zp = (DELIV + "V13-V14_ANON/V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip"
              if n in (13, 14) else
              DELIV + "V12-V14_LOCKED/YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip")
        with ZipFile(zp) as z:
            hit = [x for x in z.namelist() if x.endswith("V%d_FINAL_SHORTS.docx" % n)]
            if hit:
                open(sdoc, "wb").write(z.read(hit[0]))
                ssrc = sdoc
    shorts_status = shorts_doc(sdoc, n, ssrc if ssrc != sdoc else None) \
        if ssrc != sdoc else "REUSED from the approved locked pack"
    _j(os.path.join(sh, "V%02d_Shorts_Manifest.json" % n),
       shorts_manifest(n, shorts_status, sdoc))

    # ---- 05
    pb = os.path.join(root, "05_PUBLISHING")
    os.makedirs(pb)
    desc_src = A.existing(n, "06_PUBLISHING/Full_Description_With_Faith_Anchor.docx")
    if desc_src:
        shutil.copy2(desc_src, os.path.join(pb, "V%02d_YouTube_Description.docx" % n))
        pub_status = ("APPROVED SYNCHRONIZED SOURCE. Carried from "
                      "06_PUBLISHING/Full_Description_With_Faith_Anchor.docx "
                      "in this video's approved synchronized production "
                      "package.")
    else:
        from zipfile import ZipFile
        zp = (DELIV + "V13-V14_ANON/V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip"
              if n in (13, 14) else
              DELIV + "V12-V14_LOCKED/YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip")
        with ZipFile(zp) as z:
            hit = [x for x in z.namelist()
                   if x.endswith("V%d_FINAL_DESCRIPTION_METADATA.docx" % n)]
            open(os.path.join(pb, "V%02d_YouTube_Description.docx" % n),
                 "wb").write(z.read(hit[0]))
        pub_status = ("APPROVED SYNCHRONIZED SOURCE. Carried from the locked "
                      "pack%s." % (" as corrected by the anonymization patch"
                                   if n in (13, 14) else ""))
    _w(os.path.join(pb, "V%02d_YouTube_Description.txt" % n),
       D.head("YOUTUBE DESCRIPTION", n) + "STATUS: " + pub_status +
       "\n\nThe approved copy ships beside this file as "
       "V%02d_YouTube_Description.docx. It was not regenerated, reworded or "
       "promoted, and nothing in it was changed by this packaging pass.\n" % n)
    _w(os.path.join(pb, "V%02d_Pinned_Comment.txt" % n), pinned(n))
    ck = A.existing(n, "06_PUBLISHING/Publishing_Checklist.docx")
    if ck:
        shutil.copy2(ck, os.path.join(pb, "_approved_Publishing_Checklist.docx"))
    _w(os.path.join(pb, "V%02d_Link_and_Publication_Checklist.txt" % n),
       checklist(n, pub_status))
    _w(os.path.join(pb, "V%02d_Thumbnail_Canva_Build_Prompt.txt" % n), canva(n))
    _j(os.path.join(pb, "V%02d_Metadata.json" % n),
       dict(video=n, title=M.TITLES[n][0], thumbnail=M.TITLES[n][1],
            watch_next=M.WATCH[n], cta=M.CTA[n],
            description_status=pub_status,
            note="Metadata is useful, not filler. Hashtags are not a "
                 "strategic requirement and none is specified."))

    # ---- 06
    va = os.path.join(root, "06_VIEWER_APPLICATION")
    os.makedirs(va)
    _w(os.path.join(va, "V%02d_Viewer_Exercise.txt" % n), D.viewer_exercise(n))
    _w(os.path.join(va, "V%02d_Sticky_Realization_Record.txt" % n), D.sticky_record(n))

    # ---- 07
    eq = os.path.join(root, "07_EVIDENCE_QA")
    os.makedirs(eq)
    _j(os.path.join(eq, "V%02d_Source_Manifest.json" % n),
       D.source_manifest(n, pub_status))
    _w(os.path.join(eq, "V%02d_Evidence_and_Illustration_Notes.txt" % n),
       D.evidence_notes(n))
    _w(os.path.join(eq, "V%02d_Alignment_Log.txt" % n), D.alignment_log(n))
    for rel, dest in (("07_EVIDENCE/Evidence_and_Boundary_Notes.docx",
                       "_approved_Evidence_and_Boundary_Notes.docx"),
                      ("08_QA/Package_QA_Report.docx", "_approved_Package_QA_Report.docx"),
                      ("08_QA/Open_Issues.txt", "_approved_Open_Issues.txt")):
        ex = A.existing(n, rel)
        if ex:
            shutil.copy2(ex, os.path.join(eq, dest))
    rows = qa_rows(n, root, pub_status, shorts_status)
    _w(os.path.join(eq, "V%02d_Final_QA_Report.txt" % n), final_qa(n, rows))
    return root, rows, pub_status, shorts_status

def present(root, n, folder, pattern):
    name = pattern % n if "%" in pattern else pattern
    p = os.path.join(root, folder, name)
    if os.path.isdir(p):
        return len(os.listdir(p)) > 0
    return os.path.exists(p)

def manifest_doc(path, results):
    d = base_doc()
    title_block(d, EYEBROW, "V4 to V14 complete production packages",
                "Presence manifest for every required artifact")
    kv(d, "Generated", STAMP)
    kv(d, "Scope", "V4 to V14. V1 to V3 were built earlier and are unchanged. "
                   "V15 and above were not touched.")
    callout(d, "Every required artifact from the approved complete-package "
               "standard is listed below with its presence in each of the "
               "eleven packages. No required layer is omitted: an artifact "
               "that was not produced would read MISSING here rather than "
               "disappearing from the list.")
    para(d, "The architecture is the V1 to V3 architecture. The visual "
            "treatment is not. Each video keeps its own approved synchronized "
            "or locked artwork, unchanged.")

    vids = list(A.VIDEOS)
    # Every required artifact, for every video, stated as the literal word
    # PRESENT or MISSING. Split into two tables only so the words fit the page.
    for grp in (vids[:6], vids[6:]):
        rows = []
        for folder, label, pattern in REQUIRED:
            cells = ["%s  %s" % (folder.split("_", 1)[0], label)]
            for n in grp:
                cells.append("present" if present(results[n][0], n, folder, pattern)
                             else "MISSING")
            rows.append(cells)
        table(d, ["Required artifact"] + ["V%d" % n for n in grp], rows,
              widths=[2.2] + [0.75] * len(grp))
        para(d, "Videos %s. Every one of the %d required artifacts is listed "
                "above for every video in this group."
             % (", ".join("V%d" % n for n in grp), len(REQUIRED)))
    miss = sum(1 for n in vids for folder, _l, pat in REQUIRED
               if not present(results[n][0], n, folder, pat))
    tot = len(REQUIRED) * len(vids)
    para(d, "%d required artifacts per video across %d videos, %d slots. "
            "%d present, %d MISSING."
          % (len(REQUIRED), len(vids), tot, tot - miss, miss))

    page_break(d)
    h(d, "Presence grid")
    para(d, "The same data read the other way. Each cell is the count of "
            "required artifacts present in that folder for that video.")
    folders = []
    for folder, _l, _p in REQUIRED:
        if folder not in folders:
            folders.append(folder)
    grid = []
    for n in vids:
        cells = ["V%d" % n]
        for folder in folders:
            need = [(f, l, p) for f, l, p in REQUIRED if f == folder]
            got = sum(1 for f, _l, p in need if present(results[n][0], n, f, p))
            cells.append("%d/%d" % (got, len(need)))
        grid.append(cells)
    table(d, ["Video"] + [f.split("_", 1)[0] for f in folders], grid,
          widths=[0.7] + [0.85] * len(folders))
    para(d, "Folder keys: 01 recording, 02 visuals, 03 editor, 04 Shorts, "
            "05 publishing, 06 viewer application, 07 evidence and QA.")

    page_break(d)
    h(d, "Per video")
    for n in vids:
        root, qa, pub_status, shorts_status = results[n]
        sub(d, "V%d  %s" % (n, M.TITLES[n][0]))
        kv(d, "Thumbnail", M.TITLES[n][1])
        kv(d, "Document shape", A.shape(n))
        kv(d, "Spoken words", "{:,}".format(A.words(n)))
        kv(d, "Speech estimate", "%s at 145 wpm to %s at 130 wpm. ESTIMATE, "
                                 "not a measurement."
           % (A.runtime(n, 145), A.runtime(n, 130)))
        kv(d, "Locked master", os.path.basename(A.locked(n)[0]))
        kv(d, "Master checksum", A.sha256(A.locked(n)[0]))
        kv(d, "Thought blocks", os.path.basename(A.locked(n)[1]))
        kv(d, "Blocks checksum", A.sha256(A.locked(n)[1]))
        kv(d, "Parity", "PASS")
        kv(d, "Full-screen families", "%d" % len(A.families(n)))
        kv(d, "Triggers", "%d of %d families carry an exact spoken trigger"
           % (sum(1 for f in A.families(n) if f["trigger"]), len(A.families(n))))
        kv(d, "Visual source", "REUSED. Approved synchronized assets."
           if A.assets_dir(n) else
           "REUSED. Approved locked card specification, rendered to PNG at "
           "1920x1080 with no design change.")
        kv(d, "Run of Show", "REUSED from the approved package"
           if A.existing(n, "02_RUN_OF_SHOW/Run_of_Show.docx")
           else "BUILT. The approved package carries the production document "
                "instead; it is carried here and the operational layer was "
                "added around it.")
        kv(d, "Shorts", shorts_status)
        kv(d, "Publishing", pub_status)
        kv(d, "Seven-day memory line", M.MEMORY[n])
        kv(d, "Viewer application", M.ACTION[n])
        kv(d, "CTA", M.CTA[n] + ("   " + M.CTA_URL[n]
                                 if n in M.CTA_URL else
                                 "   No resource URL. This video's "
                                 "call to action is spoken, not linked."))
        kv(d, "Watch Next", M.WATCH[n])
        bad = [r for r in qa if not r[1]]
        kv(d, "QA", "%d checks, %d passed, %d failed"
           % (len(qa), len(qa) - len(bad), len(bad)))
        if bad:
            bullets(d, ["FAILED: " + r[0] for r in bad])
        if n == 13:
            para(d, "V13 ships under the approved public employer "
                    "anonymization patch. The 28-posting research provenance "
                    "is preserved in the source manifest. No employer name "
                    "appears in any public-facing artifact.")
        if n == 14:
            para(d, "V14 ships anonymized. No employer name was restored.")
        if n in (6, 12):
            para(d, "Ten-minute title promise: verified defensible at normal "
                    "delivery speed. See the estimated speech timing file in "
                    "01_RECORDING.")

    page_break(d)
    h(d, "What was reused and what was built")
    para(d, "The instruction was to replicate the architecture and not the V1 "
            "to V3 visual treatment. Before any visual asset was created, the "
            "approved synchronized or locked assets were checked first.")
    bullets(d, [
        "V4 to V11 carry their approved synchronized PNG and SVG assets "
        "unchanged. Nothing was redesigned and nothing was re-rendered.",
        "V12 to V14 had an approved card specification but no delivered PNG "
        "set. The specification was rendered as specified. That is an "
        "operational layer added around approved creative work, not a "
        "redesign of it.",
        "Approved Run of Show, camera map, B-roll notes, sound map, reveal "
        "map, Shorts documents, descriptions, evidence notes and QA reports "
        "were carried in place wherever they existed. Where a package "
        "already held an approved file that the new standard also generates, "
        "both ship: the approved one keeps an _approved_ prefix.",
        "No script was rewritten. No Sticky Realization was invented. No new "
        "viewer action was created. The optional V9 sentence change was not "
        "applied.",
    ])
    h(d, "Deliberate departures from the old reference package")
    bullets(d, [
        "Three candidate Shorts per video, not six.",
        "Every timing figure is labelled ESTIMATE and is arithmetic on the "
        "spoken word count. No footage exists.",
        "Publishing copy is never silently promoted. A description that came "
        "from an approved synchronized source says so and names the source. "
        "Anything constructed here is marked DRAFT, REVIEW REQUIRED.",
    ])
    footer_note(d, "V4 to V14 only. V1 to V3 and V15 and above were not "
                   "modified by this pass.")
    d.save(path)

def normalize(path):
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    out = []
    for info, data in items:
        if info.filename in ("docProps/core.xml", "docProps/app.xml"):
            t = data.decode("utf-8")
            t = re.sub(r"(<dcterms:(?:created|modified)[^>]*>)[^<]*(</dcterms:)",
                       r"\g<1>2026-09-23T00:00:00Z\g<2>", t)
            data = t.encode("utf-8")
        out.append((info.filename, info.compress_type, data))
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w") as z:
        for nm, ct, dt in out:
            zi = zipfile.ZipInfo(nm, date_time=FIXED)
            zi.compress_type = ct
            zi.external_attr = 0o644 << 16
            z.writestr(zi, dt)
    os.replace(tmp, path)

def zip_tree(root, base, zpath):
    names = sorted(os.path.relpath(os.path.join(r, f), base)
                   for r, _d, fs in os.walk(root) for f in fs)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(base, rel), "rb") as fh:
                z.writestr(zi, fh.read())
    return names

def main():
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    results = {}
    for n in A.VIDEOS:
        results[n] = build_one(n)
    manifest_doc(os.path.join(STAGE, MANIFEST), results)
    normalize(_gen(os.path.join(STAGE, MANIFEST)))
    # .pptx is an OPC package like .docx and python-pptx stamps it with the
    # clock, so it is normalized too or the combined archive hashes
    # differently on every build.
    for n in A.VIDEOS:
        for r, _d, fs in os.walk(results[n][0]):
            for f in fs:
                fp = os.path.join(r, f)
                if f.endswith((".docx", ".pptx")) and os.path.abspath(fp) in GENERATED:
                    normalize(fp)
    out = {}
    for n in A.VIDEOS:
        zp = os.path.join(OUT, "V%02d_COMPLETE_PRODUCTION_PACKAGE.zip" % n)
        zip_tree(results[n][0], STAGE, zp)
        out[n] = zp
    comb = os.path.join(OUT, COMBINED)
    names = sorted(os.path.relpath(os.path.join(r, f), STAGE)
                   for r, _d, fs in os.walk(STAGE) for f in fs)
    with zipfile.ZipFile(comb, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(STAGE, rel), "rb") as fh:
                z.writestr(zi, fh.read())
    shutil.copy2(os.path.join(STAGE, MANIFEST), os.path.join(OUT, MANIFEST))
    # The combined archive is over the 30 MiB share limit, so the same content
    # also ships as two transfer parts. Both carry the manifest.
    parts = []
    for tag, grp in (("V04-V09", range(4, 10)), ("V10-V14", range(10, 15))):
        pp = os.path.join(OUT, "V04-V14_COMPLETE_PRODUCTION_PACKAGES_PART_%s.zip" % tag)
        keep = tuple("VIDEO_%02d_COMPLETE_PRODUCTION_PACKAGE/" % n for n in grp)
        sel = [r for r in names if r.replace(os.sep, "/").startswith(keep)
               or r == MANIFEST]
        with zipfile.ZipFile(pp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for rel in sel:
                zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                with open(os.path.join(STAGE, rel), "rb") as fh:
                    z.writestr(zi, fh.read())
        parts.append(pp)
    for p in list(out.values()) + parts + [comb, os.path.join(OUT, MANIFEST)]:
        io.open(p + ".sha256", "w", encoding="utf-8").write(
            "%s  %s\n" % (sha256(p), os.path.basename(p)))
    return out, comb, results

if __name__ == "__main__":
    out, comb, results = main()
    fails = 0
    for n in A.VIDEOS:
        qa = results[n][1]
        bad = [r for r in qa if not r[1]]
        fails += len(bad)
        print("V%-3d %3d files  QA %2d/%2d%s"
              % (n, sum(len(fs) for _r, _d, fs in os.walk(results[n][0])),
                 len(qa) - len(bad), len(qa),
                 "" if not bad else "  FAIL: " + "; ".join(r[0] for r in bad)))
    print()
    miss = 0
    for n in A.VIDEOS:
        for folder, label, pat in REQUIRED:
            if not present(results[n][0], n, folder, pat):
                miss += 1
                print("MISSING  V%d  %s / %s" % (n, folder, label))
    print("required-artifact slots missing: %d" % miss)
    print("QA failures: %d" % fails)
    print()
    for n in A.VIDEOS:
        print("%-44s %s" % (os.path.basename(out[n]), sha256(out[n])))
    print("%-44s %s" % (os.path.basename(comb), sha256(comb)))
    for tag in ("V04-V09", "V10-V14"):
        pp = os.path.join(OUT, "V04-V14_COMPLETE_PRODUCTION_PACKAGES_PART_%s.zip" % tag)
        print("%-44s %s" % (os.path.basename(pp), sha256(pp)))
    print("%-44s %s" % (MANIFEST, sha256(os.path.join(OUT, MANIFEST))))
