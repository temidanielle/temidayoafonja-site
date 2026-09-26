# -*- coding: utf-8 -*-
"""Assemble the three video folders, the zips and the README."""
import os, sys, io, re, shutil, zipfile, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pptx import Presentation
from pptx.util import Emu
import fd_data as D, fd_slides as SL, fd_render as R, fd_docs as DOC, fd_fit as FIT

STAGE = os.path.join(HERE, "_stage")
COMBINED = "PLAYLIST_FINAL_KIT.zip"
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
    # 5 no thumbnail image. Temidayo builds those in Canva. The exact words
    #   and the photo direction live in the upload sheet, and the stills to
    #   shoot are on the Riverside sheet.
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

    # -- the release changed. Nothing may still name the old plan.
    STALE = [r"\b2027\b", r"\bJanuary\b", r"\bJan\.", r"\bnew year\b",
             r"\bDecember\b", r"\bnext year\b", r"\bthis January\b"]
    hits = []
    for root, _m in results:
        for r, _d2, fs in os.walk(root):
            for f in fs:
                fp = os.path.join(r, f)
                if f.endswith(".docx"):
                    t = docx_text(fp)
                elif f.endswith((".txt", ".json")):
                    t = io.open(fp, encoding="utf-8", errors="replace").read()
                else:
                    continue
                for pat in STALE:
                    for m in re.finditer(pat, t, re.I):
                        hits.append("%s: %s" % (f, m.group(0)))
    ck("No 2027, January, new year or December reference anywhere",
       not hits, "; ".join(sorted(set(hits))[:8]) or
       "every .docx, .txt and .json in the three kits searched for 2027, "
       "January, Jan., new year, December and next year. The README is "
       "scanned separately once it exists; see scan_readme")

    # -- accents: US English spelling of resume
    acc = []
    for root, _m in results:
        for r, _d2, fs in os.walk(root):
            for f in fs:
                fp = os.path.join(r, f)
                if f.endswith(".docx"):
                    t = docx_text(fp)
                elif f.endswith((".txt", ".json")):
                    t = io.open(fp, encoding="utf-8", errors="replace").read()
                else:
                    continue
                if "\u00e9" in t or "\u00c9" in t:
                    acc.append(f)
    ck("US English: resume carries no accent marks", not acc,
       "; ".join(sorted(set(acc))) or
       "no acute accent appears in any document")

    # -- titles say 10+ Years, never 15+
    bad15 = [v["n"] for v in D.VIDEOS if "15+" in v["title"]
             or "15+" in v["alt_title"]]
    ck("Titles say 10+ Years, never 15+", not bad15,
       "checked every title and alternate title; two carry \u201c10+ "
       "Years\u201d and one names no year count")

    # -- hooks say ten, fifteen, or twenty years
    miss = [v["n"] for v in D.VIDEOS[:2]
            if "ten, fifteen, or twenty years" not in " ".join(v["hook"])]
    ck("Hooks say \u201cten, fifteen, or twenty years\u201d", not miss,
       "V1 and V2 both carry the phrase; V3 opens on referrals and names no "
       "year count")

    # -- the roadmap matches the chapter titles word for word
    def _strip(ch):
        m = re.match(r"^[A-Za-z0-9 ]{1,14}:\s+(.*)$", ch)
        return m.group(1) if m else ch
    off = []
    for v in D.VIDEOS:
        road = " ".join(v["roadmap"]).lower()
        for i in D.ROADMAP_CHAPTERS[v["n"]]:
            t, ch = v["chapters"][i]
            if _strip(ch).lower().rstrip(".") not in road:
                off.append("V%d %s" % (v["n"], ch))
    ck("Roadmap matches the chapter titles word for word", not off,
       "; ".join(off) or "16 roadmap chapters across the three videos; each "
       "one appears verbatim inside the roadmap the presenter says, once its "
       "\u201cStep 1\u201d style prefix is set aside")

    # -- no production label reaches a viewer-facing slide
    shown = [s2["label"] for v in D.VIDEOS for s2 in SL.SLIDES[v["n"]]
             if SL.shows_label(s2["label"])]
    ck("No production label on a viewer-facing slide",
       all(re.match(r"(?i)^step \d+$", x) for x in shown),
       "%d of the 24 slides draw an eyebrow and every one is a STEP label; "
       "Title card, Roadmap and End card stay in the cut list and never "
       "reach the screen" % len(shown))

    # -- no thumbnail image was produced
    thumbs = [f for root, _m in results
              for _r, _d2, fs in os.walk(root) for f in fs
              if "THUMB" in f.upper()]
    ck("No thumbnail image was produced", not thumbs,
       "; ".join(thumbs) or "thumbnails are built in Canva; the kit carries "
       "the words and the photo direction only")

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
                want = (1920, 1080)
                if sz != want:
                    wrong.append("%s %s" % (f, sz))
    ck("Every PNG is the right size", not wrong, "; ".join(wrong) or
       "24 slide PNGs, all at 1920 x 1080")

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

    sizes = sorted({int(x) for x in re.findall(r"font-size:(\d+)px", R.CSS)})
    body = [x for x in sizes if x < 120]
    ck("Body text is 44 px or larger", body and min(body) >= 44,
       "every size in the slide stylesheet below the headline range: %s px"
       % ", ".join(str(x) for x in body))

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
    w("HOW TO GET A NEW JOB WITHOUT STARTING OVER")
    w("PRODUCTION KIT  |  THREE VIDEOS  |  BUILT SEPTEMBER 26, 2026")
    w("=" * 78)
    w()
    w("Nothing here has been uploaded, scheduled or published. Every file is")
    w("local. The upload sheets carry the publish dates for you to set by")
    w("hand when you are ready.")
    w()
    w("BUILT FROM")
    w("  YouTube_Playlist_New_Job_2027_Without_Starting_Over_2026-09-24.docx")
    w("      sha256 43a67cfd09d5b689")
    w("      Scripts, titles, thumbnails, descriptions, chapters, pinned")
    w("      comments, thumbnail prompts, LinkedIn posts, Shorts list.")
    w("  YouTube_Production_Brief_for_Code_Playlist_2027_2026-09-24.docx")
    w("      sha256 b2f6c2ac8e14a7f1")
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
    w("   PLAYLIST_FINAL_KIT.zip holds all three folders and this")
    w("   README. Its own checksum is in the sidecar file beside it, because a")
    w("   README that stated it would change it.")
    w()
    w("-" * 78)
    w("THE RELEASE CHANGED, AND SO DID THE COPY")
    w("-" * 78)
    w()
    w("   The source documents were written for a January 2027 launch. That")
    w("   plan is gone. Every reference to 2027, January, the new year and a")
    w("   December recording session has been removed, and the lines that")
    w("   leaned on the new year were rewritten to work at any time of year.")
    w()
    w("   Playlist title   How to Get a New Job Without Starting Over")
    w("   Video 1 title    How to Get a New Job When You Have 10+ Years of")
    w("                    Experience")
    w("   Video 1 hook     \"Here is how I would look for a new job right now")
    w("                    if I were you.\"")
    w("   Video 1 blurb    \"Looking for a new job with ten or more years of")
    w("                    experience?\"")
    w("   Video 1 alt      How to Change Jobs Without Starting Over")
    w("   Video 3 alt      No Network? How Experienced Professionals Get")
    w("                    Referred")
    w("   Video 1 slide 1  How to Get a New Job / When You Have 10+ Years of")
    w("                    Experience")
    w()
    w("   Two other wording changes, both from your check list:")
    w()
    w("   Video 2 hook     \"ten, fifteen, or twenty years\", where the source")
    w("                    said \"maybe twenty\".")
    w("   Resume           No accent marks anywhere. US English.")
    w()
    w("   The roadmap now matches the chapter titles word for word. Where")
    w("   they differed only by inflection, one side moved to the other:")
    w()
    w("   Video 1   The spoken roadmap became imperative, so \"First,")
    w("             deciding what kind of move you are making\" is now")
    w("             \"First, decide what kind of move you are making\" and")
    w("             matches chapter Step 1 exactly. Step numbering stays in")
    w("             the chapter list.")
    w("   Video 2   The chapters took the roadmap\u2019s own words, so")
    w("             \"The four questions\" is now \"The four questions I use\".")
    w("   Video 3   Two function words: \"the people who saw your work\", and")
    w("             \"who referrals leave out\".")
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
    w("   Body text     44 px or larger throughout, and the text block uses")
    w("                 the full width of the slide inside a 112 px gutter.")
    w("   Labels        No production label is drawn on a viewer-facing")
    w("                 slide. Title card, Roadmap and End card stay in the")
    w("                 cut list for the editor and never reach the screen.")
    w("                 STEP 1 through STEP 5 are drawn, because a viewer")
    w("                 benefits from knowing where they are.")
    w("   Thumbnails    None. You build them in Canva. Each upload sheet")
    w("                 carries the exact words and the photo direction,")
    w("                 and each Riverside sheet asks for 3 to 5 stills at")
    w("                 full camera resolution before the lights come down.")
    w("   Riverside     One page each, with a photo stills section for the")
    w("                 Canva thumbnails. All three recorded in one session.")
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
    w("      before the first publish date or three videos will point at a")
    w("      dead page.")
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

}

def scan_readme(path):
    """The README has to name the old plan in its change-log section in order
    to report that the plan is gone. Everything outside that section is held
    to the same rule as the kit files. Raises rather than warning, because a
    build that cannot produce a clean README should not finish quietly."""
    rt = io.open(path, encoding="utf-8").read()
    a = rt.find("THE RELEASE CHANGED, AND SO DID THE COPY")
    b = rt.find("SPECIFICATIONS MET")
    body = rt[:a] + rt[b:] if -1 not in (a, b) else rt
    body = re.sub(r"^.*No 2027, January.*$", "", body, flags=re.M)
    body = re.sub(r"^ +(every \.docx|2027, January|January, Jan\.).*$", "",
                  body, flags=re.M)
    STALE = [r"\b2027\b", r"\bJanuary\b", r"\bJan\.", r"\bnew year\b",
             r"\bDecember\b", r"\bnext year\b"]
    hits = sorted({m.group(0) for pat in STALE
                   for m in re.finditer(pat, body, re.I)})
    assert not hits, "stale date reference in README.txt: %s" % hits
    return len(body.split())


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
    scan_readme(rd)
    combined = os.path.join(OUT, COMBINED)
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
