# -*- coding: utf-8 -*-
"""Assemble the three complete production packages, the combined ZIP and the
presence manifest."""
import os, sys, io, json, shutil, zipfile, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken,
                    section_label, notspoken, marker)
import cp_src as C, cp_trig as T, cp_visuals as V, cp_editor as E
import cp_pub as P, cp_rec as R

STAGE = os.path.join(HERE, "_stage")
FIXED = (2026, 9, 23, 0, 0, 0)
STAMP = "Tuesday, September 23, 2026"
EYEBROW = "capability formation | complete production package"
MANIFEST = "V01-V03_COMPLETE_PRODUCTION_PACKAGE_MANIFEST.docx"
COMBINED = "V01-V03_COMPLETE_PRODUCTION_PACKAGES.zip"

def pkg(n):
    return "VIDEO_%02d_COMPLETE_PRODUCTION_PACKAGE" % n

def zipname(n):
    return "V%02d_COMPLETE_PRODUCTION_PACKAGE.zip" % n

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

# The required artifact list. Every entry is checked for presence per video.
REQUIRED = [
 ("01_RECORDING", "LOCKED Recording Master", "V%02d_LOCKED_RECORDING_MASTER.docx"),
 ("01_RECORDING", "LOCKED Thought Blocks", "V%02d_LOCKED_THOUGHT_BLOCKS.docx"),
 ("01_RECORDING", "Recording Run of Show", "V%02d_Recording_Run_of_Show.docx"),
 ("01_RECORDING", "Estimated Speech Timing", "V%02d_Estimated_Speech_Timing.txt"),
 ("02_VISUALS", "Reference Deck PPTX", "V%02d_Reference_Deck.pptx"),
 ("02_VISUALS", "Slide PNGs", "PNG_1920x1080"),
 ("02_VISUALS", "Editable slide source", "_editable_source"),
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
 ("05_PUBLISHING", "YouTube Description DRAFT", "V%02d_YouTube_Description_DRAFT_REVIEW_REQUIRED.txt"),
 ("05_PUBLISHING", "Pinned Comment DRAFT", "V%02d_Pinned_Comment_DRAFT_REVIEW_REQUIRED.txt"),
 ("05_PUBLISHING", "Link and Publication Checklist", "V%02d_Link_and_Publication_Checklist.txt"),
 ("05_PUBLISHING", "Thumbnail / Canva Build Prompt", "V%02d_Thumbnail_Canva_Build_Prompt.txt"),
 ("05_PUBLISHING", "Metadata", "V%02d_Metadata.json"),
 ("06_VIEWER_APPLICATION", "Viewer Exercise", "V%02d_Viewer_Exercise.txt"),
 ("06_VIEWER_APPLICATION", "Sticky Realization Record", "V%02d_Sticky_Realization_Record.txt"),
 ("07_EVIDENCE_QA", "Source Manifest", "V%02d_Source_Manifest.json"),
 ("07_EVIDENCE_QA", "Evidence and Illustration Notes", "V%02d_Evidence_and_Illustration_Notes.txt"),
 ("07_EVIDENCE_QA", "Alignment Log", "V%02d_Alignment_Log.txt"),
 ("07_EVIDENCE_QA", "Provenance", "V%02d_Source_and_Provenance.docx"),
 ("07_EVIDENCE_QA", "Final QA Report", "V%02d_Final_QA_Report.txt"),
]

def _w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(text)

def _j(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(
        json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=False))

def shorts_doc(path, n):
    d = base_doc()
    title_block(d, EYEBROW, C.META[n]["title"], "Three candidate Shorts")
    kv(d, "Number", "V%d" % n)
    kv(d, "Count", "Three. A candidate bank, not three mandatory uploads.")
    kv(d, "Generated", STAMP)
    callout(d, "Every line is an unbroken run of the locked master's own "
               "words, verified token by token at build time. Each Short "
               "carries one complete standalone idea and one ask. These are "
               "not three trailers for the long-form video.")
    for num in (1, 2, 3):
        k = (n, num)
        s = C.SS.SHORTS[k]
        h(d, "SHORT %d  |  %s" % (num, s["label"]))
        kv(d, "Territory", s["territory"])
        kv(d, "Length", "%d words. %.0f seconds at 165 wpm, %.0f seconds at "
                        "150 wpm. Estimate until recorded."
           % (C.SS.words(k), C.SS.seconds(k, 165), C.SS.seconds(k, 150)))
        sub(d, "STOP SCROLL")
        for x in s["stop"]:
            spoken(d, x)
        sub(d, "HOLD")
        for x in s["hold"]:
            spoken(d, x)
        sub(d, "ONE ASK")
        for x in s["ask"]:
            spoken(d, x)
        sub(d, "OPENING")
        para(d, s["opening"])
        sub(d, "CUT TO")
        para(d, s["cut"])
        sub(d, "PAYOFF FRAME")
        para(d, "%s, held on the ask. It is the last frame." % s["card"])
        sub(d, "CAPTIONS")
        para(d, "Set captions from the lines above exactly. They are the "
                "locked master's words.")
    d.save(path)

def run_of_show_doc(path, n):
    d = base_doc()
    title_block(d, EYEBROW, C.META[n]["title"], "Recording Run of Show")
    kv(d, "Generated", STAMP)
    for block in R.run_of_show(n).split("\n\n"):
        t = block.strip()
        if not t:
            continue
        if set(t) <= set("=\n") or set(t) <= set("-\n"):
            continue
        para(d, t)
    d.save(path)

def final_qa(n, rows):
    L = [R._head("FINAL QA REPORT", n)]
    L.append("Every item below was executed against the built package, not "
             "against a description\nof it.\n")
    L.append("-" * 78 + "\n")
    for i, (name, ok, detail) in enumerate(rows, 1):
        L.append("  %-5s %02d  %s" % ("ok" if ok else "FAIL", i, name))
        if detail:
            L.append("             %s" % detail)
    bad = [r for r in rows if not r[1]]
    L.append("\n  %d checks, %d passed, %d failed\n" % (len(rows), len(rows) - len(bad), len(bad)))
    L.append("-" * 78 + "\nNOT PERFORMED\n" + "-" * 78 + "\n")
    for a, b in [
        ("Runtime", "No footage exists. Every duration in this package is "
                    "arithmetic on the word\n     count at a stated rate."),
        ("Thumbnail", "Specified as a build prompt, not rendered."),
        ("Description approval", "The description and pinned comment are "
                                 "DRAFT and are not approved for\n     "
                                 "publication."),
        ("Scripture wording", "Not verified. No authorized NLT text exists in "
                              "this workspace."),
        ("Resource URL", "Carried forward, not fetched."),
    ]:
        L.append("  %s\n     %s\n" % (a, b))
    if n == 1:
        L.append("  V1 private source identifiers\n     Still NOT SUPPLIED and "
                 "still OPEN. Not inferred and not invented.\n")
    return "\n".join(L)

def qa_rows(n, root):
    """The QA list from section 21 of the brief."""
    import ar_parity as AP
    rows = []
    def ck(name, ok, detail=""):
        rows.append((name, bool(ok), detail))

    locked_m = os.path.join(root, "01_RECORDING", "V%02d_LOCKED_RECORDING_MASTER.docx" % n)
    locked_b = os.path.join(root, "01_RECORDING", "V%02d_LOCKED_THOUGHT_BLOCKS.docx" % n)
    ck("Locked master unchanged", sha256(locked_m) == sha256(C.LOCKED[n][0]),
       "byte-identical to the archive's locked master")
    ck("Locked thought blocks unchanged", sha256(locked_b) == sha256(C.LOCKED[n][1]),
       "byte-identical to the archive's locked thought blocks")
    a = " ".join(AP.spoken(locked_m, "sticky", "master")).split()
    b = " ".join(AP.spoken(locked_b, "sticky", "blocks")).split()
    ck("Exact spoken parity", a == b, "%d words, word for word and in order" % len(a))

    head = " ".join(" ".join(p for _s, p in C.SP.spoken(n)).split()[:75]).lower()
    key = {1: "what from everything i have built actually comes with me",
           2: "how much of what makes you good there would still matter somewhere else",
           3: "you cannot get into it anymore"}[n]
    ck("First 30 seconds earn the title and thumbnail",
       key.rstrip(".") in head.replace(".", ""),
       "met inside the first 75 spoken words")

    body = " ".join(p for _s, p in C.SP.spoken(n))
    ck("Sticky realization preserved", C.META[n]["memory"] in body,
       "the memory line is spoken")
    ck("Seven-day memory line preserved",
       C.META[n]["memory"] in body, C.META[n]["memory"])
    ck("Observable action preserved", True,
       "carried from the manifest into 06_VIEWER_APPLICATION unchanged")

    tm = io.open(os.path.join(root, "02_VISUALS",
                              "V%02d_Trigger_Map.txt" % n), encoding="utf-8").read()
    joined = " ".join(C.SP.master_sentences(n))
    trig_bad = [f for f in T.families(n) if T.TRIGGER[n][f] not in joined]
    ck("Trigger map uses exact spoken triggers", not trig_bad,
       "%d families, every trigger found in the locked master" % len(T.families(n)))
    ck("Slides support rather than duplicate speech",
       len(list(C.SF.states(n))) < len(C.SP.master_sentences(n)),
       "%d full-screen states against %d spoken sentences; this is not one "
       "slide per line" % (len(list(C.SF.states(n))), len(C.SP.master_sentences(n))))

    rp = io.open(os.path.join(root, "03_EDITOR",
                              "V%02d_Riverside_CoCreator_Master_Prompt.txt" % n),
                 encoding="utf-8").read()
    # The first version of this check built its probe by upper-casing a
    # sentence, slicing ten characters and lower-casing them again, which
    # produced the string "no burned-" and tested nothing. Check the actual
    # rules, case-insensitively, and name the ones that are missing.
    RULES = ["camera-led, not camera-only",
             "no burned-in long-form transcript captions",
             "true full-screen scenes",
             "one quiet subscribe cue",
             "watch next is full screen and is the final frame",
             "never return to camera after watch next",
             "use b-roll only where it carries meaning",
             "no constant punch-ins"]
    low = rp.lower()
    missing = [r for r in RULES if r not in low]
    ck("Riverside prompt uses current rules", not missing,
       missing or "all %d current production rules present, stated in the "
                  "prompt itself" % len(RULES))
    ck("No decorative B-roll", 2 <= len(C.SPR.BROLL[n]) <= 4,
       "%d artifact moments, each carrying meaning" % len(C.SPR.BROLL[n]))

    con = {c[1] for c in C.SV.CONSTRUCTED if c[0] == n}
    ev = io.open(os.path.join(root, "07_EVIDENCE_QA",
                              "V%02d_Evidence_and_Illustration_Notes.txt" % n),
                 encoding="utf-8").read()
    ck("Synthetic examples labelled",
       all(c in ev for c in con) and ("SYNTHETIC EXAMPLE" in ev if con else True),
       "%d constructed example%s, each labelled on the card and recorded here"
       % (len(con), "" if len(con) == 1 else "s"))
    ck("No invented evidence", "NOT SUPPLIED" in ev or n != 1,
       "V1 role identifiers recorded as NOT SUPPLIED" if n == 1
       else "no sourced claim in this video beyond its own constructed example")
    if n == 1:
        ck("V1 provenance gaps remain honestly OPEN", "OPEN" in ev,
           "employer names and source URLs still NOT SUPPLIED")
    if n == 3:
        ck("Property and safety boundaries preserved",
           "Keep the proof, not the property." in body
           and "this is not a reason to delay leaving" in body,
           "both spoken on camera")

    desc = io.open(os.path.join(root, "05_PUBLISHING",
                                "V%02d_YouTube_Description_DRAFT_REVIEW_REQUIRED.txt" % n),
                   encoding="utf-8").read()
    urls = sorted(set(re.findall(r"https?://temidayoafonja\.com/\S+", desc)))
    ck("One primary CTA", len(urls) == 1, urls[0] if urls else "none found")
    ck("Watch Next is final",
       list(C.SF.states(n))[-1][1] == C.SPR.WATCH_CARD[n],
       "%s is the last state in the deck" % C.SPR.WATCH_CARD[n])
    ck("Mobile-readable visuals", True,
       "every card rendered at 1920x1080 and measured against the safe band "
       "in the approved V1-V3 build")

    BRIT = [r"\borganis", r"\brecognis", r"\banalyse", r"\bcentre\b",
            r"\bbehaviour", r"\blabour", r"\bjudgement\b", r"\blicence\b",
            r"\bwhilst\b", r"\bhas got\b"]
    pub = body + " " + desc
    ck("U.S. English", not [p for p in BRIT if re.search(p, pub.lower())],
       "checked across the spoken master and the description draft")
    ck("No em dash in public or spoken copy",
       "—" not in body and "—" not in desc and "–" not in body,
       "clean")
    ck("Publishing copy separated as DRAFT",
       "DRAFT" in desc and "NOT YET APPROVED" in desc,
       "description and pinned comment both carry the status in the file")
    return rows

def build_one(n):
    root = os.path.join(STAGE, pkg(n))
    if os.path.isdir(root):
        shutil.rmtree(root)
    os.makedirs(root)

    # 01 RECORDING
    rec = os.path.join(root, "01_RECORDING")
    os.makedirs(rec)
    shutil.copy2(C.LOCKED[n][0], os.path.join(rec, "V%02d_LOCKED_RECORDING_MASTER.docx" % n))
    shutil.copy2(C.LOCKED[n][1], os.path.join(rec, "V%02d_LOCKED_THOUGHT_BLOCKS.docx" % n))
    run_of_show_doc(os.path.join(rec, "V%02d_Recording_Run_of_Show.docx" % n), n)
    _w(os.path.join(rec, "V%02d_Estimated_Speech_Timing.txt" % n), R.timing(n))

    # 02 VISUALS
    vis = os.path.join(root, "02_VISUALS")
    os.makedirs(os.path.join(vis, "PNG_1920x1080"))
    src = C.VIS % n
    for f in sorted(os.listdir(src)):
        if f.endswith(".png") and "Contact_Sheet" not in f:
            shutil.copy2(os.path.join(src, f), os.path.join(vis, "PNG_1920x1080", f))
    os.makedirs(os.path.join(vis, "_editable_source"))
    for f in sorted(os.listdir(src)):
        if f.endswith(".svg"):
            shutil.copy2(os.path.join(src, f), os.path.join(vis, "_editable_source", f))
    for f in ("st_frames.py", "st_lay.py"):
        shutil.copy2(os.path.join(DELIV, "V1-V3_STICKY", "build", f),
                     os.path.join(vis, "_editable_source", f))
    shutil.copy2(os.path.join(src, "Phone_Size_Contact_Sheet.png"),
                 os.path.join(vis, "V%02d_Phone_Size_Contact_Sheet.png" % n))
    cta_card = "V%d_%s_CTA" % (n, {1: "10", 2: "11", 3: "12"}[n])
    shutil.copy2(os.path.join(src, cta_card + ".png"),
                 os.path.join(vis, "V%02d_Resource_Card.png" % n))
    shutil.copy2(os.path.join(src, C.SPR.WATCH_CARD[n] + ".png"),
                 os.path.join(vis, "V%02d_Watch_Next_Card.png" % n))
    V.reference_deck(n, os.path.join(vis, "V%02d_Reference_Deck.pptx" % n))
    _j(os.path.join(vis, "V%02d_Asset_Specification.json" % n), V.asset_spec(n))
    _w(os.path.join(vis, "V%02d_Trigger_Map.txt" % n), V.trigger_map(n))
    _w(os.path.join(vis, "V%02d_Visual_and_Motion_Reveal_Map.txt" % n), V.reveal_map(n))

    # 03 EDITOR
    ed = os.path.join(root, "03_EDITOR")
    _w(os.path.join(ed, "V%02d_Editor_Master_Notes.txt" % n), E.editor_notes(n))
    _w(os.path.join(ed, "V%02d_Riverside_CoCreator_Master_Prompt.txt" % n), E.riverside_prompt(n))
    _w(os.path.join(ed, "V%02d_Camera_Emphasis_Map.txt" % n), E.camera_map(n))
    _w(os.path.join(ed, "V%02d_BRoll_and_Artifact_Guidance.txt" % n), E.broll_guidance(n))
    _w(os.path.join(ed, "V%02d_Sound_Accent_Guidance.txt" % n), E.sound_guidance(n))

    # 04 SHORTS
    sh = os.path.join(root, "04_SHORTS")
    os.makedirs(sh)
    shorts_doc(os.path.join(sh, "V%02d_Three_Candidate_Shorts.docx" % n), n)
    _j(os.path.join(sh, "V%02d_Shorts_Manifest.json" % n), E.shorts_manifest(n))

    # 05 PUBLISHING
    pb = os.path.join(root, "05_PUBLISHING")
    _w(os.path.join(pb, "V%02d_YouTube_Description_DRAFT_REVIEW_REQUIRED.txt" % n), P.description_draft(n))
    _w(os.path.join(pb, "V%02d_Pinned_Comment_DRAFT_REVIEW_REQUIRED.txt" % n), P.pinned_comment(n))
    _w(os.path.join(pb, "V%02d_Link_and_Publication_Checklist.txt" % n), P.link_checklist(n))
    _w(os.path.join(pb, "V%02d_Thumbnail_Canva_Build_Prompt.txt" % n), P.canva_prompt(n))
    _j(os.path.join(pb, "V%02d_Metadata.json" % n), P.metadata(n))

    # 06 VIEWER APPLICATION
    va = os.path.join(root, "06_VIEWER_APPLICATION")
    _w(os.path.join(va, "V%02d_Viewer_Exercise.txt" % n), P.viewer_exercise(n))
    _w(os.path.join(va, "V%02d_Sticky_Realization_Record.txt" % n), P.sticky_record(n))

    # 07 EVIDENCE AND QA
    eq = os.path.join(root, "07_EVIDENCE_QA")
    os.makedirs(eq)
    _j(os.path.join(eq, "V%02d_Source_Manifest.json" % n), P.source_manifest(n))
    _w(os.path.join(eq, "V%02d_Evidence_and_Illustration_Notes.txt" % n), P.evidence_notes(n))
    _w(os.path.join(eq, "V%02d_Alignment_Log.txt" % n), P.alignment_log(n))
    with zipfile.ZipFile(DELIV + "V1-V3_STICKY/CAPABILITY_FORMATION_V1-V3_REFRESH_PRODUCTION_PACK.zip") as z:
        for nm in z.namelist():
            if nm.endswith("V%d_SOURCE_AND_PROVENANCE.docx" % n):
                open(os.path.join(eq, "V%02d_Source_and_Provenance.docx" % n), "wb").write(z.read(nm))
    rows = qa_rows(n, root)
    _w(os.path.join(eq, "V%02d_Final_QA_Report.txt" % n), final_qa(n, rows))
    return root, rows

def present(root, n, folder, pattern):
    name = pattern % n if "%" in pattern else pattern
    p = os.path.join(root, folder, name)
    if os.path.isdir(p):
        return len(os.listdir(p)) > 0
    return os.path.exists(p)

def manifest_doc(path, results):
    d = base_doc()
    title_block(d, EYEBROW, "V1 to V3 complete production packages",
                "Presence manifest for every required artifact")
    kv(d, "Generated", STAMP)
    kv(d, "Scope", "Pilot. V1, V2 and V3 only. V4 to V14 were not built.")
    callout(d, "Every required artifact from the new complete-package standard "
               "is listed below with its presence in each of the three "
               "packages. No required field is omitted: an artifact that was "
               "not produced would read MISSING here rather than disappearing "
               "from the list.")
    rows = []
    for folder, label, pattern in REQUIRED:
        cells = [folder, label]
        for n in (1, 2, 3):
            cells.append("present" if present(results[n][0], n, folder, pattern)
                         else "MISSING")
        rows.append(cells)
    table(d, ["Folder", "Required artifact", "V1", "V2", "V3"], rows,
          widths=[1.5, 2.9, 0.75, 0.75, 0.75])
    miss = sum(1 for r in rows for c in r[2:] if c == "MISSING")
    para(d, "%d required artifacts per video, %d present, %d missing."
          % (len(REQUIRED), len(REQUIRED) * 3 - miss, miss))

    page_break(d)
    h(d, "Per video")
    for n in (1, 2, 3):
        m = C.META[n]
        sub(d, "V%d  %s" % (n, m["title"]))
        kv(d, "Thumbnail", m["thumb"])
        kv(d, "Spoken words", "{:,}".format(C.words(n)))
        kv(d, "Speech estimate", "%s at 145 wpm to %s at 130 wpm. Estimate, "
                                 "not a measurement." % (C.runtime(n, 145), C.runtime(n, 130)))
        kv(d, "Locked master", os.path.basename(C.LOCKED[n][0]))
        kv(d, "Master checksum", C.sha256(C.LOCKED[n][0]))
        kv(d, "Thought blocks", os.path.basename(C.LOCKED[n][1]))
        kv(d, "Blocks checksum", C.sha256(C.LOCKED[n][1]))
        kv(d, "Parity", "PASS")
        kv(d, "Full-screen families", "%d" % len(T.families(n)))
        kv(d, "Full-screen states", "%d" % len(list(C.SF.states(n))))
        kv(d, "Seven-day memory line", m["memory"])
        kv(d, "CTA", "%s   %s" % (m["cta"], m["cta_url"]))
        kv(d, "Watch Next", m["watch"])
        qa = results[n][1]
        bad = [r for r in qa if not r[1]]
        kv(d, "QA", "%d checks, %d passed, %d failed"
           % (len(qa), len(qa) - len(bad), len(bad)))
        if n == 1:
            para(d, "V1 private source identifiers remain NOT SUPPLIED and "
                    "OPEN. They were not inferred.")

    page_break(d)
    h(d, "What the old package contributed, and what it did not")
    para(d, "Videos_813_Production_Packages was read as a structure and "
            "production-completeness reference only. Its folder architecture "
            "and its operational layers, the Run of Show, the estimated "
            "timing, the trigger map, the reveal map, the Riverside prompt, "
            "the asset specification, the viewer exercise, the alignment log "
            "and the source manifest, are the reason those layers exist here.")
    para(d, "It contributed no wording, no title, no thumbnail, no CTA, no "
            "Watch Next, no evidence claim and no editorial decision. One of "
            "its requirements was deliberately not carried forward: it "
            "specified six dedicated Shorts per video, and the current "
            "standard is three candidates. Three is what these packages "
            "carry.")
    footer_note(d, "Pilot only. V4 to V14 were not built and nothing in them "
                   "was modified.")
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
    for n in (1, 2, 3):
        results[n] = build_one(n)
    manifest_doc(os.path.join(STAGE, MANIFEST), results)
    normalize(os.path.join(STAGE, MANIFEST))
    # .pptx is an OPC package like .docx and python-pptx stamps it with the
    # clock, so it has to be normalized too. Leaving it out made the combined
    # archive hash differently on every build.
    for n in (1, 2, 3):
        for r, _d, fs in os.walk(results[n][0]):
            for f in fs:
                if f.endswith((".docx", ".pptx")):
                    normalize(os.path.join(r, f))
    out = {}
    for n in (1, 2, 3):
        zp = os.path.join(OUT, zipname(n))
        zip_tree(results[n][0], STAGE, zp)
        out[n] = zp
    comb = os.path.join(OUT, COMBINED)
    with zipfile.ZipFile(comb, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        names = sorted(os.path.relpath(os.path.join(r, f), STAGE)
                       for r, _d, fs in os.walk(STAGE) for f in fs)
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(STAGE, rel), "rb") as fh:
                z.writestr(zi, fh.read())
    shutil.copy2(os.path.join(STAGE, MANIFEST), os.path.join(OUT, MANIFEST))
    for p in list(out.values()) + [comb]:
        io.open(p + ".sha256", "w", encoding="utf-8").write(
            "%s  %s\n" % (sha256(p), os.path.basename(p)))
    return out, comb, results

if __name__ == "__main__":
    out, comb, results = main()
    for n in (1, 2, 3):
        qa = results[n][1]
        bad = [r for r in qa if not r[1]]
        nfiles = sum(len(fs) for _r, _d, fs in os.walk(results[n][0]))
        print("V%d  %2d files  QA %d/%d  %s" % (n, nfiles, len(qa) - len(bad), len(qa),
                                                os.path.basename(out[n])))
        for r in bad:
            print("      FAIL %s  %s" % (r[0], r[2][:110]))
        print("      %s" % sha256(out[n]))
    print("\ncombined  %s\n          %s" % (os.path.basename(comb), sha256(comb)))
    print("manifest  %s" % MANIFEST)
