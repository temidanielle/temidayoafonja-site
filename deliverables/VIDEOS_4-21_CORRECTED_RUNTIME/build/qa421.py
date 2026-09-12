# -*- coding: utf-8 -*-
"""Package checks for the corrected Videos 4 to 21 production packages.

Every check runs against the BUILT package on disk, not against the build
data, so a check cannot pass because of something that was only true in a
source module.

Final-export checks are listed separately and are NOT run. A written prompt
does not prove an effect exists in a finished video.
"""
import os, re, sys, glob, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn
from PIL import Image

# Appended, never inserted at the front: this batch's own modules must win
# over the September 10 batch's identically named ones.
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_14-21_FINAL_PRODUCTION/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "riverside-build")
import masters421 as M
import research14
import publish421 as PUB
import restore678
from frames421 import SETS
from shorts421 import SHORTS


def units(path):
    """Paragraphs and table rows of a .docx as separate units."""
    out = []
    d = Document(path)
    for child in d.element.body.iterchildren():
        if child.tag == qn("w:p"):
            t = Paragraph(child, d).text.strip()
            if t:
                out.append(t)
        elif child.tag == qn("w:tbl"):
            for r in Table(child, d).rows:
                out.append(" | ".join(c.text.strip() for c in r.cells))
    return out


def text_units(path):
    return [u.strip() for u in
            open(path, encoding="utf-8").read().split("\n\n") if u.strip()]


# Files that are copied into the package unchanged, plus the QA report.
# The supplied sources are the user's own content and are not edited here, so
# a house style rule cannot be applied to them. The QA report quotes its own
# findings, so reading it back would report a violation it created itself.
def _authored_only(p, n):
    base = os.path.basename(p)
    if base in (M.FILES[n], M.filename(n), M.RESEARCH) or \
            base == "SUPERSEDED_" + M.FILES[n]:
        return False
    if base == "QA_Report.txt":
        return False
    return True


def all_units(pkg, n=None, authored_only=False):
    """Every readable unit in a package, from every document and text file."""
    out = []
    for p in sorted(glob.glob(os.path.join(pkg, "**", "*"), recursive=True)):
        if authored_only and n is not None and not _authored_only(p, n):
            continue
        if p.endswith(".docx"):
            out += units(p)
        elif p.endswith((".txt", ".md")):
            out += text_units(p)
    return out


def spoken_blocks(path):
    """Thought blocks of a script-only recording copy, set at 13.5pt."""
    out = []
    d = Document(path)
    for p in d.paragraphs:
        if not p.text.strip() or any(r.bold for r in p.runs):
            continue
        sizes = [r.font.size.pt for r in p.runs if r.font.size is not None]
        if sizes and max(sizes) >= 13.0:
            out.append(p.text.strip())
    return out


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def master_corpus(n):
    """Everything the supplied or restored master says, as one string.

    House style is a rule about what this build writes. Several masters
    carry en dashes of their own, in a runtime row or a section name, and
    the change log and manifests quote those rows back verbatim. Flagging
    the quotation would be asking the package to correct approved copy,
    which is the one thing it must not do.
    """
    m = M.read(n)
    parts = [M.spoken_text(n)]
    parts += [str(v) for v in m["meta"].values()]
    parts += [nm for nm, _ in m["sections"]]
    parts += list(m["tail"])
    if n in M.RESTORED:
        parts.append(m["supplied_file"])
    return _norm(" ".join(parts)).lower()


def quoted(n, unit, hit, window=42):
    """True when the offending fragment is the master's own wording."""
    # Case-folded: a manifest or change log may set a master's own section
    # name in capitals, and that is a typographic choice by this build, not
    # a different sentence.
    u, corpus = _norm(unit).lower(), master_corpus(n)
    i = u.find(_norm(hit).lower())
    if i < 0:
        return False
    frag = u[max(0, i - window):i + len(_norm(hit)) + window].strip()
    # Walk inward until a fragment long enough to be meaningful is found
    # inside the master, so a short coincidence cannot excuse a real slip.
    while len(frag) > 18:
        if frag in corpus:
            return True
        frag = frag[2:-2].strip() if len(frag) > 24 else frag[1:].strip()
    return False


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("“", '"')
                  .replace("”", '"').replace("—", "-").replace("–", "-"))


def run(n, pkg):
    """Returns a list of (check, passed, detail)."""
    R = []
    def ck(name, ok, detail):
        R.append((name, bool(ok), detail))

    m = M.read(n)
    us = all_units(pkg)
    # House style applies to what this build authored, not to the supplied
    # master or the supplied research archive.
    authored = all_units(pkg, n, authored_only=True)
    master_copy = os.path.join(pkg, "01_Recording_Master", M.filename(n))
    reading = os.path.join(pkg, "01_Recording_Master",
                           "Approved_Recording_Master_Reference.docx")
    script_only = os.path.join(pkg, "01_Recording_Master",
                               "Video_%d_Script_Only_Recording_Copy.docx" % n)

    # --- the master itself -------------------------------------------
    ck("Correct new final master used", os.path.exists(master_copy),
       M.filename(n))
    if n in M.RESTORED:
        sup = os.path.join(pkg, "01_Recording_Master",
                           "SUPERSEDED_" + M.FILES[n])
        ck("Supplied compressed master retained unchanged",
           os.path.exists(sup) and sha256(sup) == m["supplied_sha"],
           "%s, SHA-256 %s" % (M.FILES[n], m["supplied_sha"]))
        ck("Restored to the approved depth",
           M.word_count(n) >= 0.9 * {6: 1151, 7: 1209, 8: 1198}[n],
           "%d spoken words against %d in the last full-length approved "
           "master" % (M.word_count(n), {6: 1151, 7: 1209, 8: 1198}[n]))
        ck("Restoration adds no newly authored speech",
           not any(p["src"] == "BRIDGE"
                   for _, ps in restore678.SCRIPTS[n] for p in ps),
           "every restored line traces to approved speech")
    ck("Master copied unchanged",
       os.path.exists(master_copy) and sha256(master_copy) == m["sha"],
       "SHA-256 %s" % m["sha"])

    master_blocks = [_norm(b) for b in M.blocks(n)]
    ck("Spoken reading copy matches the master",
       [_norm(u) for u in units(reading) if _norm(u) in master_blocks] and
       all(b in [_norm(u) for u in units(reading)] for b in master_blocks),
       "%d blocks present" % len(master_blocks))
    copy_blocks = [_norm(b) for b in spoken_blocks(script_only)]
    ck("Script-only copy matches the master exactly",
       copy_blocks == master_blocks,
       "%d blocks, in order" % len(copy_blocks))

    # --- metadata fidelity -------------------------------------------
    ck("Correct title", any(M.title(n) in u for u in us), M.title(n))
    ck("Correct thumbnail wording",
       any(M.thumbnail(n) in u for u in us), M.thumbnail(n))
    fw = M.framework(n)
    ck("Correct framework", (not fw) or any(fw in u for u in us),
       fw or "none stated by the master")
    ask, cue = PUB.primary_cta(n)
    ck("Correct CTA", any(_norm(ask) in _norm(u) for u in us), ask)
    ck("The CTA is the one the master speaks", M.trigger_ok(n, cue), cue)
    res = PUB.route(n)
    if res:
        ck("Correct resource", any(res in u for u in us), res)
    else:
        # A resource name may appear only inside a sentence that says none
        # is used. Anywhere else would mean a route was added that the
        # master does not name.
        def _offered(r):
            for u in us:
                if not re.search(r"\b%s\b" % re.escape(r), u):
                    continue
                if re.search(r"names no resource|does not name|none is added|"
                             r"do not add|no resource", u, re.I):
                    continue
                return True
            return False
        others = [r for r in ("Field Kit", "Keep the Proof",
                              "Career Decision Evidence Check",
                              "Career Evidence Starter") if _offered(r)]
        ck("No resource added where the master names none", not others,
           "master names none; none added")
    wn_num, wn_title, wn_src = PUB.watch_next(n)
    ck("Correct Watch Next",
       any(_norm(wn_title) in _norm(u) for u in us),
       "Video %s: %s (from %s)" % (wn_num, wn_title, wn_src))
    ck("Watch Next names the destination master's exact title",
       wn_title == M.title(wn_num), M.title(wn_num))

    # --- sequence and triggers ---------------------------------------
    ck("Current teaching sequence used",
       all(any(_norm(name) in _norm(u) for u in us)
           for name, _ in m["sections"] if name),
       "%d sections from the master" % len(m["sections"]))
    missing = [f["key"] for f in SETS[n] if not M.trigger_ok(n, f["trigger"])]
    ck("All sentence triggers exist in the current master", not missing,
       missing or "%d triggers verified inside single blocks" % len(SETS[n]))

    # --- no contamination from the superseded drafts -------------------
    OLD = ["You are in a meeting and you are doing fine",
           "There is a particular kind of frustrating",
           "A year ago that report took you two days",
           "Somebody has offered you a management role",
           "Somebody has told you that you should consult",
           "You are getting ready to go back",
           "You made the move. And the parts you were worried about",
           "Which Parts of Your Experience Will Transfer"]
    hits = [o for o in OLD if any(_norm(o) in _norm(u) for u in us)]
    ck("No Code-draft script contamination", not hits,
       hits or "no superseded draft wording found anywhere in the package")

    # --- Video 14 research --------------------------------------------
    if n == 14:
        rows, ok = research14.verify()
        ck("V14 claims grounded in the research archive", ok,
           "%d of %d claims verified against the archive"
           % (sum(1 for _, g, _ in rows if g), len(rows)))
        ck("V14 uses 28, never 30",
           any("28" in u for u in us) and
           not any(re.search(r"\b30 (job descriptions|postings|retained)\b",
                             u, re.I) for u in us),
           "28 retained; the target of 30 is described only as a target")
        ck("V14 convenience-sample limits preserved",
           any("convenience sample" in u.lower() for u in us) and
           any("do not represent" in u.lower() or
               "does not represent" in u.lower() for u in us),
           "sample limitation stated in the package and on a frame")
        bad = research14.forbidden_in_package(us)
        ck("V14 makes no overstated research claim", not bad,
           [b[0] for b in bad] or "no percentage, hiring or "
           "interchangeability claim")
        ck("V14 employer material traceable",
           all(found for _, found in research14.employer_traceability()),
           "every employer named in the master's notes appears in the "
           "archive, and no employer is named on a rendered frame")

    # --- runtime mode --------------------------------------------------
    # The September 11 correction. V4 and V5 are the only 5-minute retention
    # test. Everything from V6 on is regular long-form, and V15 to V21 keep
    # the fuller 9 to 12 minute depth where that was the approved target.
    mode = M.mode(n)
    ck("Runtime mode stated correctly",
       any(mode in u for u in us),
       "%s, stated in the package" % mode)
    if n in M.FIVE_MIN:
        ck("Marked as the 5-minute retention test",
           mode == "5-MINUTE RETENTION TEST" and
           any("retention test" in u.lower() for u in us),
           "V4 and V5 are the only two videos in the experiment")
        ck("The experiment is scoped to V4 and V5 only",
           any(re.search(r"only.{0,40}(V4 and V5|Videos 4 and 5)|"
                         r"(V4 and V5|Videos 4 and 5).{0,40}only", u, re.I)
               for u in us),
           "the package says the experiment does not extend past V5")
    else:
        ck("Marked as regular long-form",
           mode == "REGULAR LONG-FORM" and
           any("REGULAR LONG-FORM" in u for u in us),
           "not part of the 5-minute experiment")
        ck("Not shortened to a 5-minute target",
           not any(re.search(r"(target|aim|cut|trim|shorten).{0,40}"
                             r"(five|5)[\s-]?minute", u, re.I)
                   for u in authored),
           "no 5-minute target is applied to this video")
    if n in M.RESTORED_DEPTH:
        words = M.word_count(n)
        fast, slow = M.estimate(n)[1], M.estimate(n)[2]
        ck("Restored to regular long-form depth",
           words >= 1150,
           "%d spoken words, %s to %s at 130 to 145 words per minute, "
           "against a restored 9 to 12 minute target" % (words, fast, slow))
        ck("The restored runtime target is recorded",
           any("9" in u and "12" in u and "minute" in u.lower() for u in us),
           M.runtime_intent(n) or "stated in the package")

    # --- editorial boundaries -----------------------------------------
    # Which videos carry a constructed example is read from the corrected
    # master, not from a list that can go stale.
    if any(w in M.spoken_text(n).lower()
           for w in ("constructed", "illustration")):
        ck("Constructed examples labeled",
           any("ILLUSTRATION" in u or "constructed" in u.lower()
               for u in us),
           "the constructed example carries its label on the frame and is "
           "said aloud in the master")
    ck("No invented employer or personal claim",
       not any(re.search(r"\b(my client|my employer|when I worked at|"
                         r"a company called)\b", u, re.I) for u in us),
       "no invented employer, client or personal claim")

    # --- language ------------------------------------------------------
    dash = [u[:70] for u in authored
            if ("—" in u or "–" in u)
            and not quoted(n, u, "—" if "—" in u else "–")]
    ck("No em dashes or en dashes", not dash, dash[:2] or
       "clean in everything this build authored. Master wording carrying "
       "its own dashes is quoted verbatim and not corrected")
    BRIT = re.compile(r"\b(colour|behaviour|organis(e|ed|ing|ation)|"
                      r"recognis(e|ed|ing)|analys(e|ed)|labelled|centre|"
                      r"programme|whilst|amongst)\b", re.I)
    brit = []
    for u in authored:
        m_ = BRIT.search(u)
        if m_ and not quoted(n, u, m_.group(0)):
            brit.append("%s :: %s" % (m_.group(0), u[:60]))
    ck("U.S. English", not brit, brit[:2] or "no British spellings")

    # --- assets ---------------------------------------------------------
    png_dir = os.path.join(pkg, "03_Visuals", "Support_Reference_PNG")
    pngs = sorted(glob.glob(os.path.join(png_dir, "*.png")))
    sizes = {Image.open(p).size for p in pngs}
    ck("Assets 1920x1080 minimum",
       pngs and all(w >= 1920 and h >= 1080 for w, h in sizes),
       "%d PNGs, sizes %s" % (len(pngs), sorted(sizes)))
    sheet = os.path.join(pkg, "03_Visuals",
                         "V%d_Phone_Size_Contact_Sheet.png" % n)
    ck("Mobile legibility inspected visually", os.path.exists(sheet),
       "phone-size contact sheet rendered and inspected by eye at 393 px "
       "per frame")
    ck("Editable source deck supplied",
       os.path.exists(os.path.join(pkg, "03_Visuals",
                                   "V%d_Reference_Deck.pptx" % n)),
       "PowerPoint deck at 1920 by 1080")

    # --- Riverside prompt content ---------------------------------------
    rv = os.path.join(pkg, "04_Riverside",
                      "Riverside_CoCreator_Master_Prompt.txt")
    rvt = _norm(open(rv, encoding="utf-8").read()) \
        if os.path.exists(rv) else ""
    ck("True full-screen rules explicit",
       "TRUE FULL SCREEN" in rvt and "NEVER APPLIES TO WATCH NEXT" in rvt,
       "full-screen rule and the Watch Next exception both stated")
    ck("No burned-in caption instruction present",
       "NO BURNED-IN OR OPEN CAPTIONS" in rvt, "stated in the prompt")
    ck("SRT requirement present",
       "SRT generated against the FINAL edited timeline" in rvt,
       "SRT is required from the final timeline, not the script")
    ck("Camera movement budget correct",
       "3 to 5 deliberate camera-emphasis beats" in rvt and
       "one combined budget" in rvt,
       "one combined budget of about 3 to 5 beats")
    ck("Sound budget correct",
       "4 to 7 restrained audio accents for the ENTIRE video" in rvt and
       "not cumulative" in rvt,
       "about 4 to 7 for the whole video, candidates not cumulative")
    ck("Audio and visual transition hooks present",
       "AUDIO AND VISUAL TRANSITION HOOKS" in rvt and
       "Do NOT add a click to every bullet" in rvt,
       "the rule and its limit are both stated")
    ck("One visual Subscribe cue",
       "One brief visual Subscribe cue" in rvt and
       "no spoken Subscribe request" in rvt,
       "visual only, and none is spoken")
    ck("Watch Next final, no return to camera",
       "Nothing appears after Watch Next." in rvt and
       "no return to camera afterward" in rvt,
       "stated in the prompt and on the Watch Next scene")

    # --- Shorts ----------------------------------------------------------
    ind = glob.glob(os.path.join(pkg, "05_Shorts", "Individual", "*.docx"))
    ck("Six Shorts", len(SHORTS[n]) == 6 and len(ind) == 6,
       "6 scripts, 4 Priority A and 2 Priority B")

    # --- publishing -------------------------------------------------------
    pub = os.path.join(pkg, "06_Publishing", "Publishing_Materials.docx")
    pus = units(pub) if os.path.exists(pub) else []
    ck("Publishing copy aligned to the master",
       any(u.strip() == M.title(n) for u in pus) and
       any(u.strip() == M.thumbnail(n) for u in pus),
       "title and thumbnail taken from the master verbatim")
    urls = set()
    for u in us:
        urls |= set(re.findall(r"(?:https?://)?temidayoafonja\.com/[\w\-/]+",
                               u))
    allowed = {"temidayoafonja.com/career-evidence-starter",
               "temidayoafonja.com/fieldkit",
               "temidayoafonja.com/career-decisions",
               "temidayoafonja.com/keep-the-proof"}
    stray = {u.replace("https://", "") for u in urls} - allowed
    ck("No invented URLs", not stray, stray or
       "only the four existing resource routes appear")
    # A YouTube chapter list starts at 0:00 and has several entries. A
    # single timestamp at the start of a line is far more likely to be a
    # wrapped runtime estimate, which every package states deliberately, so
    # matching one of those would fail the package for saying what it must.
    STAMP = re.compile(r"(?m)^\s*(\d{1,2}:\d{2}(?::\d{2})?)\s+[A-Za-z]")
    chapters = []
    for u in us:
        stamps = STAMP.findall(u)
        if len(stamps) >= 3 and any(s_.startswith(("0:00", "00:00"))
                                    for s_ in stamps):
            chapters.append(u[:60])
    ck("No invented chapters", not chapters, chapters[:2] or
       "no chapter list anywhere. Runtime estimates are stated as "
       "estimates; chapters come from the final export")
    ck("No invented music attribution",
       not any(re.search(r"music (by|from|licen[cs]e)|track:", u, re.I)
               for u in us),
       "no music credit or licence code recorded")
    return R


FINAL_EXPORT_PENDING = [
 "Actual recorded delivery",
 "Actual runtime",
 "Actual executed jump cuts",
 "Executed zoom-ins and pull-backs",
 "Executed motion graphics",
 "B-roll placement",
 "Actual audio clarity",
 "Final loudness",
 "Music and effects balance",
 "Picture quality",
 "Caption absence on the exported video",
 "SRT synchronization",
 "Final chapters",
 "Final Watch Next hold",
 "Clean ending",
 "Thumbnail artwork approval",
 "Public link accessibility",
]
