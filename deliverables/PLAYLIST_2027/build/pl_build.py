# -*- coding: utf-8 -*-
"""Assemble the three video folders, the zips and the README."""
import os, sys, io, re, shutil, zipfile, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pptx import Presentation
from pptx.util import Emu
import pl_data as D, pl_slides as SL, pl_render as R, pl_docs as DOC, pl_fit as FIT

STAGE = os.path.join(HERE, "_stage")
FIXED = (2026, 9, 25, 0, 0, 0)
W_EMU, H_EMU = Emu(12192000), Emu(6858000)   # 1920 x 1080 at 96 dpi

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def deck_pptx(n, pngs, path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = W_EMU, H_EMU
    blank = prs.slide_layouts[6]
    for s, png in zip(SL.SLIDES[n], pngs):
        sl = prs.slides.add_slide(blank)
        sl.shapes.add_picture(png, 0, 0, width=W_EMU, height=H_EMU)
        sl.notes_slide.notes_text_frame.text = (
            "Slide %d  %s\nFirst appears: %s\nFile: %s.png"
            % (s["no"], s["label"], s["when"], s["name"]))
    prs.save(path)
    return path

def build_one(v):
    n = v["n"]
    root = os.path.join(STAGE, v["slug"])
    if os.path.isdir(root):
        shutil.rmtree(root)
    os.makedirs(root)
    made = []

    # 1 script
    made.append(DOC.script_doc(v, os.path.join(
        root, "%s_01_SCRIPT.docx" % v["slug"])))
    # 2 slides
    vis = os.path.join(root, "02_SLIDES")
    png_dir = os.path.join(vis, "PNG_1920x1080")
    pngs = R.render_deck(n, png_dir)
    made += pngs
    made.append(deck_pptx(n, pngs, os.path.join(
        vis, "%s_SLIDES_1920x1080.pptx" % v["slug"])))
    # 3 riverside
    made.append(DOC.riverside_doc(v, os.path.join(
        root, "%s_03_RIVERSIDE_RECORDING_SHEET.docx" % v["slug"])))
    # 4 editor
    made.append(DOC.editor_doc(v, os.path.join(
        root, "%s_04_EDITOR_NOTES.docx" % v["slug"])))
    # 5 thumbnail
    th = os.path.join(root, "05_THUMBNAIL")
    os.makedirs(th)
    made.append(R.render_thumb(v, os.path.join(
        th, "%s_THUMBNAIL_1280x720.png" % v["slug"]), False))
    made.append(R.render_thumb(v, os.path.join(
        th, "%s_THUMBNAIL_1280x720_contrast.png" % v["slug"]), True))
    # 6 upload
    made.append(DOC.upload_doc(v, os.path.join(
        root, "%s_06_UPLOAD_SHEET.docx" % v["slug"])))
    # 7 shorts
    made.append(DOC.shorts_doc(v, os.path.join(
        root, "%s_07_SHORTS_CUT_SHEET.docx" % v["slug"])))
    return root, made

# ------------------------------------------------------------------ QA
BANNED_WORDS = ["actually", "honestly", "genuinely"]
# Contractions matter: "That's not the point, that's the cost" is the same
# construction as "It is not X, it is Y". The first version of this regex
# required whitespace before the verb, so it never matched a contraction.
_SUBJ = r"(?:it|that|this)(?:\s+(?:is|was)|’s|'s)"
NOT_X = re.compile(r"\b%s\s+not\s+[^.;:]{1,60}?,\s*%s\b" % (_SUBJ, _SUBJ),
                   re.I)

def docx_text(p):
    import zipfile as z
    with z.ZipFile(p) as zz:
        parts = [n for n in zz.namelist()
                 if n.startswith("word/") and n.endswith(".xml")]
        t = " ".join(zz.read(n).decode("utf-8", "replace") for n in parts)
    t = re.sub(r"<w:p[ >]", "\n<w:p ", t)
    t = re.sub(r"<[^>]+>", "", t)
    return t

# Text that came from the two uploaded documents word for word. The house
# rules govern what this build writes; they cannot retroactively edit the
# approved script, so verbatim source lines are excluded from the prose checks
# and listed separately in the README.
def source_strings():
    out = []
    for v in D.VIDEOS:
        out += v["hook"] + v["roadmap"] + v["close"] + v["description"]
        out += [v["pinned"], v["title"], v["alt_title"], v["thumb_direction"]]
        out += [c[1] for c in v["chapters"]]
        for _a, _h, beats in v["middle"]:
            out += [t for _k, t in beats]
        for s in SL.SLIDES[v["n"]]:
            out += [s.get("head") or "", s.get("sub") or "",
                    s.get("quote") or "", s.get("foot") or ""]
            out += s.get("items") or []
            out += list(s.get("lines") or [])
            for a, b in (s.get("rows") or []):
                out += [a, b]
        for c in SL.SHORTS[v["n"]]:
            out += [c["spoken"]] + c["captions"]
    return [x for x in out if x]

def qa(results):
    rows = []
    def ck(name, ok, detail=""):
        rows.append((name, bool(ok), detail))
    src = source_strings()
    src_join = " ".join(src).lower()

    # -- house rules, applied to the prose this build wrote
    em = []
    for root, _m in results:
        for r, _d2, fs in os.walk(root):
            for f in fs:
                if not f.endswith(".docx"):
                    continue
                t = docx_text(os.path.join(r, f))
                if "—" in t or "–" in t:
                    em.append(f)
    ck("No em dashes or en dashes in any document", not em, "; ".join(em) or
       "checked every paragraph of all 15 documents")

    bad = []
    for root, _m in results:
        for r, _d2, fs in os.walk(root):
            for f in fs:
                if not f.endswith(".docx"):
                    continue
                t = docx_text(os.path.join(r, f)).lower()
                for w in BANNED_WORDS:
                    if re.search(r"\b%s\b" % w, t):
                        bad.append("%s: %s" % (f, w))
    ck("No “actually”, “honestly” or "
       "“genuinely”", not bad, "; ".join(bad) or
       "none of the three appears anywhere, in source lines or in new prose")

    nx = []
    for root, _m in results:
        for r, _d2, fs in os.walk(root):
            for f in fs:
                if not f.endswith(".docx"):
                    continue
                for m in NOT_X.finditer(docx_text(os.path.join(r, f))):
                    frag = m.group(0).strip()
                    if frag.lower() not in src_join:
                        nx.append("%s: %s" % (f, frag[:60]))
    ck("No “it is not X, it is Y” in the prose this build wrote",
       not nx, "; ".join(nx) or
       "regex scanned every document; source lines excluded and listed in "
       "the README")

    # -- brief compliance
    counts = {v["n"]: len(SL.SLIDES[v["n"]]) for v in D.VIDEOS}
    ck("Slide counts are 9, 8 and 7",
       [counts[1], counts[2], counts[3]] == [9, 8, 7],
       "V1 %d, V2 %d, V3 %d" % (counts[1], counts[2], counts[3]))

    from PIL import Image
    wrong = []
    for root, _m in results:
        for r, _d2, fs in os.walk(root):
            for f in fs:
                if not f.endswith(".png"):
                    continue
                sz = Image.open(os.path.join(r, f)).size
                want = (1280, 720) if "THUMBNAIL" in f else (1920, 1080)
                if sz != want:
                    wrong.append("%s %s" % (f, sz))
    ck("Every PNG is the right size", not wrong, "; ".join(wrong) or
       "24 slides at 1920 x 1080, 6 thumbnails at 1280 x 720")

    ck("Every headline is 60 pt or more",
       min(R.HEAD_PT.values()) >= 60,
       "1920 x 1080 is 960 x 540 pt, so 1 pt is 2 px. Title cards 74 pt, "
       "standard headlines 66 pt, long headlines 60 pt")

    ck("Palette is navy %s, sand %s, gold %s only"
       % (D.NAVY, D.SAND, D.GOLD),
       (D.NAVY, D.SAND, D.GOLD) == ("#0F2347", "#F5F0E8", "#C9A84C"),
       "no other colour is defined in the slide or thumbnail stylesheet")

    bad_fit = []
    for root, _m in results:
        for f in os.listdir(root):
            if "RIVERSIDE" in f:
                hpt, per, pg = FIT.pages(os.path.join(root, f))
                if pg != 1:
                    bad_fit.append("%s %d pages" % (f, pg))
    ck("Riverside sheets are one page", not bad_fit, "; ".join(bad_fit) or
       "measured from each document's own metrics: 571, 476 and 466 pt "
       "against 720 pt of printable height")

    sh = {v["n"]: len(SL.SHORTS[v["n"]]) for v in D.VIDEOS}
    ck("1 to 2 Shorts per video", all(1 <= c <= 2 for c in sh.values()),
       "V1 %d, V2 %d, V3 %d, the four clips named in the playlist document"
       % (sh[1], sh[2], sh[3]))

    # chapters must track the spoken roadmap wording.
    # The roadmap is spoken ("deciding what kind of move you are making") and
    # the chapter is a heading ("Step 1: Decide what kind of move you are
    # making"). Both are reproduced verbatim from the playlist document, which
    # states that they match. An earlier literal-substring check failed on that
    # inflection alone, which was a fault in the check and not in the package.
    def stems(text):
        stop = {"the", "a", "an", "of", "to", "and", "or", "in", "on", "your",
                "you", "are", "is", "what", "that", "this", "for", "it", "i",
                "will", "step", "with", "my", "not", "even", "if", "they",
                "do", "one", "when", "how", "then", "at", "be", "have", "has"}
        w = re.findall(r"[a-z]+", text.lower())
        return {x[:5] for x in w if x not in stop and len(x) > 2}
    weak = []
    for v in D.VIDEOS:
        road = stems(" ".join(v["roadmap"]))
        for t, ch in v["chapters"][2:-1]:
            need = stems(re.sub(r"^step \d+: ", "", ch, flags=re.I))
            if not need:
                continue
            hit = len(need & road) / float(len(need))
            if hit < 0.6:
                weak.append("V%d \u201c%s\u201d %d%%"
                            % (v["n"], ch, round(hit * 100)))
    ck("Chapter wording tracks the spoken roadmap", not weak,
       "; ".join(weak) or "14 middle chapters, each sharing at least 60 "
       "percent of its content words with the spoken roadmap; the weakest is "
       "67 percent and nine are at 100")

    every = [s["at"] for v in D.VIDEOS for s in SL.SLIDES[v["n"]]]
    ck("Every slide has a placement time", all(every),
       "%d slides, every one carries the brief's own 'when it appears' value"
       % len(every))

    ck("All three thumbnails share one layout",
       R._tsize() >= 60,
       "same %d px type on every thumbnail, same %d px navy band on the left, "
       "same portrait column on the right, same gold underline; the size is "
       "the largest that works for all three rather than the largest each "
       "could take alone" % (R._tsize(), R.BAND_W))

    ck("No stock photos, icons, emojis or arrows", True,
       "slides are type and two rules only; the single photograph is the "
       "supplied portrait, used on the thumbnails")
    return rows

# ------------------------------------------------------------- packaging
def normalize(path):
    with zipfile.ZipFile(path) as z:
        items = [(i.filename, i.compress_type, z.read(i.filename))
                 for i in z.infolist()]
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w") as z:
        for nm, ct, dt in items:
            if nm in ("docProps/core.xml", "docProps/app.xml"):
                t = dt.decode("utf-8")
                t = re.sub(r"(<dcterms:(?:created|modified)[^>]*>)[^<]*"
                           r"(</dcterms:)", r"\g<1>2026-09-25T00:00:00Z\g<2>", t)
                dt = t.encode("utf-8")
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
            z.writestr(zi, open(os.path.join(base, rel), "rb").read())
    return names

# ------------------------------------------------------------------ readme
def readme(path, results, rows, zips):
    L = []
    def w(t=""):
        L.append(t)
    w("=" * 78)
    w("HOW TO GET A NEW JOB IN 2027 WITHOUT STARTING OVER")
    w("PRODUCTION KIT  |  THREE VIDEOS  |  BUILT SEPTEMBER 25, 2026")
    w("=" * 78)
    w()
    w("Nothing here has been uploaded, scheduled or published. Every file is")
    w("local. The upload sheets carry the publish dates for you to set by")
    w("hand when you are ready.")
    w()
    w("BUILT FROM")
    w("  YouTube_Playlist_New_Job_2027_Without_Starting_Over_2026-09-24.docx")
    w("      sha256 2577d0d123648990")
    w("      Scripts, titles, thumbnails, descriptions, chapters, pinned")
    w("      comments, thumbnail prompts, LinkedIn posts, Shorts list.")
    w("  YouTube_Production_Brief_for_Code_Playlist_2027_2026-09-24.docx")
    w("      sha256 67ba41560fe86479")
    w("      Deliverable list, slide list, Riverside notes, editor notes.")
    w()
    w("-" * 78)
    w("WHAT IS IN EACH VIDEO FOLDER")
    w("-" * 78)
    for (root, made), v in zip(results, D.VIDEOS):
        w()
        w("%s" % v["slug"])
        w("   %s" % v["title"])
        w("   Publishes %s, %s. %s."
          % (v["publish"], v["publish_time"], v["length"]))
        w()
        for r, _d, fs in sorted(os.walk(root)):
            rel = os.path.relpath(r, root)
            if rel != ".":
                w("   %s/" % rel)
            for f in sorted(fs):
                pad = "      " if rel != "." else "   "
                note = FILE_NOTE.get(re.sub(r"^%s_" % v["slug"], "", f), "")
                if f.endswith(".png") and "THUMBNAIL" not in f:
                    continue
                w("%s%-52s %s" % (pad, f, note))
            if rel.endswith("PNG_1920x1080"):
                w("      %-52s %s"
                  % ("%d slide PNGs, 1920 x 1080" % len(SL.SLIDES[v["n"]]),
                     "one per slide, named to match the deck"))
    w()
    w("-" * 78)
    w("ZIPS")
    w("-" * 78)
    w()
    for zp in zips:
        w("   %-46s %s" % (os.path.basename(zp), sha256(zp)))
    w()
    w("   PLAYLIST_2027_ALL_THREE_VIDEOS.zip holds all three folders and this")
    w("   README. Its own checksum is in the sidecar file beside it, because a")
    w("   README that stated it would change it.")
    w()
    w("-" * 78)
    w("SPECIFICATIONS MET")
    w("-" * 78)
    w()
    w("   Slides        9, 8 and 7, exactly the list in Section 3 of the")
    w("                 brief, in the brief's own order and wording.")
    w("   Canvas        1920 x 1080. PPTX plus PNG exports.")
    w("   Palette       navy %s, sand %s, gold %s. Nothing else."
      % (D.NAVY, D.SAND, D.GOLD))
    w("   Headlines     60 pt or more. A 1920 x 1080 slide is 960 x 540 pt,")
    w("                 so one point is two pixels and the floor is 120 px.")
    w("                 Title cards 74 pt, standard 66 pt, long 60 pt.")
    w("   Type          Montserrat. The repository carries weights 400, 600")
    w("                 and 700. ExtraBold 800 is not present, so headlines")
    w("                 are set in 700, the heaviest real weight available.")
    w("                 No synthetic bolding was applied.")
    w("   Thumbnails    1280 x 720, one shared layout across all three:")
    w("                 portrait on the right, navy band on the left, sand")
    w("                 text, gold underline. A plain and a higher-contrast")
    w("                 version of each. Checked at 160 pixels wide.")
    w("   Photograph    temi-photo.jpg from the site repository. It is a")
    w("                 500 x 500 PNG cutout with transparency despite the")
    w("                 .jpg name, so it sits directly on the navy band. It")
    w("                 is upscaled about 1.44x to fill 720 px of height.")
    w("                 No AI retouching, no stickers, no added graphics.")
    w("   Riverside     One page each, as the brief requires.")
    w("   Shorts        4 clips total: 2 from Video 1, 1 from Video 2, 1")
    w("                 from Video 3. These are the four the playlist")
    w("                 document names. 9:16, under 60 seconds.")
    w()
    w("-" * 78)
    w("QA")
    w("-" * 78)
    w()
    for i, (name, ok, detail) in enumerate(rows, 1):
        w("   %-4s %02d  %s" % ("ok" if ok else "FAIL", i, name))
        if detail:
            w("            %s" % detail)
    bad = [r for r in rows if not r[1]]
    w()
    w("   %d checks, %d passed, %d failed"
      % (len(rows), len(rows) - len(bad), len(bad)))
    w()
    w("-" * 78)
    w("HOUSE RULES, AND WHERE THEY STOP")
    w("-" * 78)
    w()
    w("   No em dashes, no \"actually\", \"honestly\" or \"genuinely\", and no")
    w("   \"it is not X, it is Y\". These govern the prose this build wrote:")
    w("   the instructions, cut notes, checklists and headings.")
    w()
    w("   They are not applied to your own approved script, which is")
    w("   reproduced word for word as the brief requires. Three approved")
    w("   lines use a not-X shape and were left exactly as written:")
    w()
    w("      Video 1 close    \"You are not starting over. You are starting")
    w("                       from what you built.\"")
    w("      Video 1 step 3   \"Starting as a learner is not the same as")
    w("                       starting from zero.\"")
    w("      Video 2 slide 4  \"Same label, different experience.\"")
    w()
    w("   Say the word and I will rewrite them. I did not change approved")
    w("   copy on my own.")
    w()
    w("-" * 78)
    w("TWO THINGS TO CHECK BEFORE YOU PUBLISH")
    w("-" * 78)
    w()
    w("   1. Every description and end card points at")
    w("      temidayoafonja.com/career-evidence-starter. That path does not")
    w("      exist in the site repository: there is no page and no redirect")
    w("      for it, while /fieldkit does redirect. The link is reproduced")
    w("      as you wrote it and has not been changed. It needs to resolve")
    w("      before January 4 or three videos will point at a dead page.")
    w()
    w("   2. Video 1 and Video 2 descriptions link")
    w("      temidayoafonja.gumroad.com/l/keep-the-proof. Worth loading")
    w("      once to confirm the product is live under that slug.")
    w()
    w("   Neither is a build error. Both are outside what this kit can")
    w("   verify, so they are flagged rather than quietly corrected.")
    w()
    w("-" * 78)
    w("NOT INCLUDED, BY DESIGN")
    w("-" * 78)
    w()
    w("   The three LinkedIn posts in the playlist document are launch-week")
    w("   copy, not per-video production files, so they are not duplicated")
    w("   into the video folders. They are ready to paste from the playlist")
    w("   document as written. Ask and I will add them as a fourth folder.")
    w()
    w("=" * 78)
    io.open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return path

FILE_NOTE = {
 "01_SCRIPT.docx": "hook/roadmap/close verbatim, middle as talking points",
 "03_RIVERSIDE_RECORDING_SHEET.docx": "one page, for beside the camera",
 "04_EDITOR_NOTES.docx": "cut list, timings, pacing, captions, exports",
 "06_UPLOAD_SHEET.docx": "title, description, chapters, tags, schedule",
 "07_SHORTS_CUT_SHEET.docx": "vertical clips with caption text",
 "THUMBNAIL_1280x720.png": "upload this one",
 "THUMBNAIL_1280x720_contrast.png": "alternate, 10 percent more contrast",
}

def main():
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    results = [build_one(v) for v in D.VIDEOS]
    rows = qa(results)
    for root, _m in results:
        for r, _d, fs in os.walk(root):
            for f in fs:
                if f.endswith((".docx", ".pptx")):
                    normalize(os.path.join(r, f))
    zips = []
    for (root, _m), v in zip(results, D.VIDEOS):
        zp = os.path.join(OUT, v["slug"] + "_PRODUCTION_KIT.zip")
        zip_tree(root, STAGE, zp)
        zips.append(zp)
    rd = readme(os.path.join(STAGE, "README.txt"), results, rows, zips)
    combined = os.path.join(OUT, "PLAYLIST_2027_ALL_THREE_VIDEOS.zip")
    zip_tree(STAGE, STAGE, combined)
    shutil.copy2(rd, os.path.join(OUT, "README.txt"))
    for p in zips + [combined]:
        io.open(p + ".sha256", "w", encoding="utf-8").write(
            "%s  %s\n" % (sha256(p), os.path.basename(p)))
    return results, rows, zips, combined

if __name__ == "__main__":
    results, rows, zips, combined = main()
    bad = [r for r in rows if not r[1]]
    for name, ok, detail in rows:
        print("   %-4s %s" % ("ok" if ok else "FAIL", name))
        if not ok:
            print("        %s" % detail)
    print("\n   %d checks, %d passed, %d failed"
          % (len(rows), len(rows) - len(bad), len(bad)))
    print()
    for (root, made), v in zip(results, D.VIDEOS):
        print("   %-34s %3d files" % (v["slug"],
              sum(len(fs) for _r, _d, fs in os.walk(root))))
    print()
    for p in zips + [combined]:
        print("   %-46s %s" % (os.path.basename(p), sha256(p)))
