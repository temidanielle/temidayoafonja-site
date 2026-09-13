# -*- coding: utf-8 -*-
"""Package checks for the story-led packages.

Every check runs against the built package on disk, not against build data,
so a check cannot pass because of something that was only true in a module.
"""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
import masters_sl as M
import publish_sl as PUB
import prodocs_sl as P
import visualdir_sl as V
import editorial_sl as ED
import shorts_sl as SH
import wncheck_sl as WN
from frames_sl import SETS

BRIT = re.compile(r"\b(colour|behaviour|organis(e|ed|ing|ation)|"
                  r"recognis(e|ed|ing)|analys(e|ed)|labelled|centre|"
                  r"programme|whilst|amongst)\b", re.I)


def units(path):
    out = []
    d = Document(path)
    for c in d.element.body.iterchildren():
        if c.tag == qn("w:p"):
            t = "".join(x.text or "" for x in c.iter(qn("w:t"))).strip()
            if t:
                out.append(t)
        elif c.tag == qn("w:tbl"):
            from docx.table import Table
            for r in Table(c, d).rows:
                for cell in r.cells:
                    if cell.text.strip():
                        out.append(cell.text.strip())
    return out


def all_units(pkg, authored_only=False, n=None):
    out = []
    for p in glob.glob(os.path.join(pkg, "**", "*"), recursive=True):
        if p.endswith(".docx"):
            if authored_only and os.path.basename(p) in (
                    os.path.basename(M.path(n)),
                    os.path.basename(M.path(n, True))):
                continue
            out += units(p)
        elif p.endswith(".txt"):
            out += [x for x in open(p, encoding="utf-8").read().split("\n\n")
                    if x.strip()]
    return out


def sha256(p):
    import hashlib
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def run(n, pkg):
    R = []

    def ck(name, ok, detail):
        R.append((name, bool(ok), detail))

    us = all_units(pkg)
    authored = all_units(pkg, True, n)
    rec = os.path.join(pkg, "01_Recording_Master")
    script = os.path.join(rec, os.path.basename(M.path(n)))
    blocks = os.path.join(rec, os.path.basename(M.path(n, True)))

    # ---- source and script integrity
    ck("Story-led script copied unchanged",
       os.path.exists(script) and sha256(script) == M.read(n)["sha"],
       "SHA-256 %s" % M.read(n)["sha"])
    ck("Story-led thought block copied unchanged",
       os.path.exists(blocks) and sha256(blocks) == M.sha256(M.path(n, True)),
       os.path.basename(M.path(n, True)))
    ok, detail = M.blocks_match_script(n)
    ck("Thought block matches the script exactly", ok, detail)
    ck("No superseded pre-story-led master is active in this folder",
       not glob.glob(os.path.join(rec, "*FINAL_Revised*"))
       and not glob.glob(os.path.join(rec, "*RESTORED*")),
       "only the story-led pair is present")

    # ---- packaging
    ck("Correct title", any(M.title(n) == u.strip() for u in us),
       M.title(n))
    ck("Correct thumbnail wording",
       any(M.thumbnail(n) == u.strip() for u in us), M.thumbnail(n))

    # ---- triggers
    miss = [f["key"] for f in SETS[n] if not M.trigger_ok(n, f["trigger"])]
    ck("Every visual cue exists in the story-led script", not miss,
       miss or "%d cues verified inside single spoken paragraphs"
       % len(SETS[n]))
    lab = [f["key"] for f in SETS[n] if M._is_label(f["trigger"])]
    ck("No visual cue is a section label", not lab,
       lab or "labels are production aids and cue nothing")

    # ---- camera and full screen
    cam = sum(1 for x in P.spine(n) if x[0] == "CAMERA")
    full = sum(1 for x in P.spine(n) if x[0] == "FRAME")
    ck("The video stays camera-led overall", cam >= full,
       "%d camera stretches against %d full-screen frames" % (cam, full))
    tmap = os.path.join(pkg, "03_Visuals", "Camera_and_Full_Screen_Map.txt")
    tt = open(tmap, encoding="utf-8").read() if os.path.exists(tmap) else ""
    ck("The map distinguishes camera from full screen",
       "[ CAMERA ]" in tt and "[ FULL SCREEN ]" in tt,
       "both are marked throughout the spine")
    ck("Every frame carries a treatment",
       all(V.treatment(f["key"])[0] for f in SETS[n]),
       ", ".join(sorted({V.treatment(f["key"])[0] for f in SETS[n]})))

    # ---- CTA and Watch Next
    res = PUB.route(n)
    urls = set()
    for u in us:
        urls |= set(re.findall(r"temidayoafonja\.com/[\w\-/]+", u))
    allowed = {PUB.ROUTES[res]} if res else set()
    ck("Only a resource the script speaks appears", urls <= allowed,
       (urls - allowed) or (res or "this script names no resource"))
    wn_n, wn_t, wn_src = PUB.watch_next(n)
    ck("Watch Next names the destination's story-led title",
       wn_t == M.title(wn_n), "Video %d: %s" % (wn_n, wn_t))
    ck("Watch Next is final, with no return to camera",
       any("NO RETURN TO CAMERA" in u.upper() for u in us),
       "stated in the production documents")

    # ---- Shorts
    rows = SH.audit(n)
    ck("Six Shorts, audited against the story-led script", len(rows) == 6,
       ", ".join(sorted({r[1] for r in rows})))
    ck("No Short rests on a framework the script dropped",
       not [r for r in rows if r[1] == "REBUILD"],
       "%d reuse, %d copy update"
       % (len([r for r in rows if r[1] == "REUSE"]),
          len([r for r in rows if r[1] == "COPY UPDATE"])))

    # ---- editorial and evidence
    ed = [c for c in ED.checks(n) if not c[1]]
    ck("Editorial standard holds", not ed, [c[0] for c in ed] or
       "recognizable situation, painful problem, solution, viewer outcome")
    ck("No invented employer or personal claim",
       not any(re.search(r"\b(my client|my employer|when I worked at|"
                         r"a company called)\b", u, re.I) for u in us),
       "none found")
    illus = any(k in M.spoken_text(n).lower()
                for k in ("imagine", "picture", "constructed", "illustration",
                          "for example"))
    if illus:
        # The Riverside prompt FORBIDS logos and fake screenshots, so it
        # contains those words. A check that matches the word rather than
        # the instruction flags the prohibition as if it were the offence.
        # Only a unit that specifies such a visual counts.
        FORBIDS = re.compile(r"\b(do not|does not|never|no |without)\b",
                             re.I)
        specified = [u[:70] for u in authored
                     if re.search(r"\b(logo|logos|screenshot|screenshots)\b",
                                  u, re.I) and not FORBIDS.search(u)]
        ck("Constructed scenes are not dressed as real records",
           not specified,
           specified[:2] or "no logo, screenshot or real-company visual is "
           "specified anywhere. Where these words appear they are "
           "prohibitions.")

    # ---- language
    dash = [u[:70] for u in authored if "—" in u or "–" in u]
    ck("No em dashes or en dashes", not dash, dash[:2] or "clean")
    brit = []
    for u in authored:
        m = BRIT.search(u)
        if m:
            brit.append("%s :: %s" % (m.group(0), u[:50]))
    ck("U.S. English", not brit, brit[:2] or "no British spellings")

    # ---- assets and mobile
    png = glob.glob(os.path.join(pkg, "03_Visuals", "Support_Reference_PNG",
                                 "*.png"))
    sizes = {Image.open(p).size for p in png}
    ck("Assets 1920 by 1080 minimum",
       png and all(w >= 1920 and h >= 1080 for w, h in sizes),
       "%d PNGs, %s" % (len(png), sorted(sizes)))
    ck("Mobile legibility inspected at phone size",
       os.path.exists(os.path.join(pkg, "03_Visuals",
                                   "V%d_Phone_Size_Contact_Sheet.png" % n)),
       "contact sheet rendered at 393 px per frame and inspected")

    # ---- Riverside
    rv = os.path.join(pkg, "04_Riverside",
                      "Riverside_CoCreator_Master_Prompt.txt")
    # The prompt is wrapped for reading, so a phrase can straddle a
    # line break. Collapse whitespace before looking for one, or the
    # check fails on typesetting rather than on content.
    t = open(rv, encoding="utf-8").read() if os.path.exists(rv) else ""
    t = re.sub(r"\s+", " ", t)
    for name, needle in (
      ("Riverside prompt is story-led, not a renamed file",
       "The opening is a recognition moment. Leave it on camera."),
      ("No burned-in caption instruction",
       "NO BURNED-IN OR OPEN CAPTIONS"),
      ("SRT from the final edited timeline",
       "against the FINAL edited timeline"),
      ("Camera movement budget", "3 to 5 deliberate camera-emphasis beats"),
      ("Sound budget", "4 to 7 restrained audio accents"),
      ("Visual Subscribe cue only", "no spoken Subscribe request"),
      ("Watch Next final", "TRUE FULL SCREEN and FINAL"),
      ("Graphics may not add teaching",
       "may never introduce a framework"),
      ("Every graphic is specified, not merely requested",
       "EVERY GRAPHIC IN THIS VIDEO, AND WHAT IT IS"),
    ):
        ck(name, needle in t, "present in the prompt")
    return R
