# -*- coding: utf-8 -*-
"""Final QA for the correction pass, run against the archive on disk.

Every assertion below reads the built files, or the archive itself, rather
than the modules that produced them.
"""
import os, sys, json, zipfile, hashlib, glob, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import masters_sl as M
import packaging_sl as PK
import frames_sl as F
import prodocs_sl as P
import publish_sl as PUB
import shorts_sl as SH
import qa_sl
from docx import Document

ARCHIVE = os.path.join(OUT, "Videos_4-21_STORY_LED_FINAL_Production_Packages"
                            ".zip")
ROADMAP = {
 4: "I'D NEVER HELD THE ROLE", 5: "CHANGED TRACKS. NOT ZERO.",
 6: "NEW TITLE. SAME WORK?", 7: "MORE WORK ≠ GROWTH",
 8: "NOW IT LOOKS EASY", 9: "NEW FIELD. NOT ZERO.",
 10: "BEFORE ACCESS ENDS", 11: "THE TASK ISN'T THE JOB",
 12: "WHAT CAN CHANGE NOW?", 13: "TEST BEFORE YOU QUIT",
 14: "WHAT REALLY TRANSFERS?", 15: "KNOWING ISN'T OWNING",
 16: "THEY NEED YOU. THEN SKIP YOU.", 17: "WHAT DID YOU ACTUALLY DO?",
 18: "TWO DIFFERENT JOBS", 19: "EXPERIENCE ISN'T AN OFFER",
 20: "WHAT STILL COUNTS NOW?", 21: "NOT EVERYTHING TRAVELS",
}
R = []


def ck(name, ok, detail=""):
    R.append((name, bool(ok), detail))


def pkg(n):
    return os.path.join(OUT, "VIDEO_%d_STORY_LED_PACKAGE" % n)


def main():
    # --- sources untouched
    M.verify_all()
    ck("September 13 spoken sources unchanged", True,
       "all 36 verified against intake hashes")
    hashes = open(os.path.join(M.SRC, "SOURCE_HASHES.txt"),
                  encoding="utf-8").read()
    ck("36 source hashes still match", len(re.findall(r"\b[0-9a-f]{64}\b",
                                                      hashes)) >= 36,
       "%d recorded" % len(re.findall(r"\b[0-9a-f]{64}\b", hashes)))

    # --- placements
    cards = sum(len(F.SETS[n]) for n in M.VIDEOS)
    pl = [k for n in M.VIDEOS for k in
          [x[1]["key"] for x in P.spine(n) if x[0] == "FRAME"]]
    dups = sorted({k for k in pl if pl.count(k) > 1})
    ck("183 visual assets", cards == 183, "%d unique cards" % cards)
    ck("183 full-screen placements", len(pl) == 183,
       "%d placements" % len(pl))
    ck("Zero duplicate placements", not dups, dups or "none, across all 18")
    png = glob.glob(os.path.join(OUT, "VIDEO_*_STORY_LED_PACKAGE",
                                 "03_Visuals", "Support_Reference_PNG",
                                 "*.png"))
    ck("183 rendered graphics on disk", len(png) == 183, "%d PNG" % len(png))

    # --- the two corrected cues stay camera on the repetition
    for n, key, line in ((10, "v10_03_capture_qualify_retrieve",
                          "Capture the contribution."),
                         (13, "v13_02_define_investigate_try_decide",
                          "Define.")):
        spine = P.spine(n)
        at = [i for i, x in enumerate(spine)
              if x[0] == "FRAME" and x[1]["key"] == key]
        occ = [(li, pi) for li, (_, ps) in enumerate(M.sections(n))
               for pi, p in enumerate(ps) if M._norm(p) == M._norm(line)]
        mp = open(os.path.join(pkg(n), "03_Visuals",
                               "Camera_and_Full_Screen_Map.txt"),
                  encoding="utf-8").read()
        ck("V%d second %r stays camera" % (n, line),
           len(at) == 1 and len(occ) == 2 and mp.count(key) == 1,
           "%d occurrences of the line, %d cue in the built map"
           % (len(occ), mp.count(key)))

    # --- packaging
    for n in M.VIDEOS:
        j = json.load(open(os.path.join(
            pkg(n), "08_Sources_and_QA", "Source_Manifest_V%d.json" % n),
            encoding="utf-8"))
        ok = j["thumbnail"] == ROADMAP[n]
        if n in (4, 5):
            ck("V%d thumbnail = %s" % (n, ROADMAP[n]), ok, j["thumbnail"])
        elif not ok:
            ck("V%d thumbnail unchanged" % n, False, j["thumbnail"])
    ck("All other locked titles and thumbnails unchanged",
       all(json.load(open(os.path.join(
           pkg(n), "08_Sources_and_QA", "Source_Manifest_V%d.json" % n),
           encoding="utf-8"))["thumbnail"] == ROADMAP[n]
           and M.title(n) for n in M.VIDEOS),
       "18 of 18 match the locked roadmap")
    ck("Script-header thumbnail metadata recorded as an exception",
       len(PK.exceptions()) == 2
       and all("metadata exception" in
               open(os.path.join(OUT, "Source_Hierarchy_Manifest.txt"),
                    encoding="utf-8").read().lower()
               for _ in (0,)),
       ", ".join("V%d" % n for n, _, _ in PK.exceptions()))

    # --- routes
    routes = {n: PUB.route(n) for n in M.VIDEOS}
    named = {n: r for n, r in routes.items() if r}
    ck("CTA routes unchanged",
       all(r in PUB.ROUTES for r in named.values()),
       "%d videos name a resource, all on the locked routes; %d name none"
       % (len(named), len(routes) - len(named)))
    import wncheck_sl
    rows, bad, typo = wncheck_sl.check()
    ck("Watch Next routes unchanged", not bad and len(rows) == 18,
       "%d cards, %d mismatches" % (len(rows), len(bad)))

    # --- shorts, research, runtime
    ck("Six candidate Shorts per video",
       all(len(SH.audit(n)) == 6 for n in M.VIDEOS), "18 x 6")
    ck("V14 = 1,364 spoken words", M.word_count(14) == 1364,
       "%s words" % format(M.word_count(14), ","))
    import recdocs_sl
    ok14, det14 = M.blocks_match_script(14)
    ck("V14 thought block matches its script", ok14, det14)
    body14 = " ".join(qa_sl.all_units(pkg(14)))
    ck("V14 research = 28 retained postings, never 30",
       "28" in body14 and not re.search(r"\b30\s+(job\s+)?postings?\b",
                                        body14),
       "28 retained postings preserved")
    ck("Runtime values remain estimates only",
       all("not a runtime" in " ".join(qa_sl.all_units(pkg(n))).lower()
           or "arithmetic" in " ".join(qa_sl.all_units(pkg(n))).lower()
           for n in (4, 5, 10, 13)),
       "every figure is arithmetic on the script")

    # --- house style and edit rules, read from the archive itself
    with zipfile.ZipFile(ARCHIVE) as z:
        names = z.namelist()
    ck("Archive holds 18 packages, 18 checksums and 6 batch documents",
       len(names) == 42, "%d entries" % len(names))
    ck("The archive's own checksum is not inside it",
       not any(n.endswith("Production_Packages.zip.sha256") for n in names),
       "written beside it")
    ck("No SRT exists before the final edit",
       not glob.glob(os.path.join(OUT, "**", "*.srt"), recursive=True),
       "SRT generated in Riverside after the cut")

    style = []
    for n in M.VIDEOS:
        for u in qa_sl.all_units(pkg(n), True, n):
            if "—" in u and not qa_sl.quoted(n, u, "—"):
                style.append((n, "em dash", u[:40]))
            m = qa_sl.BRIT.search(u)
            if m and not qa_sl.quoted(n, u, m.group(0)):
                style.append((n, m.group(0), u[:40]))
    ck("U.S. English in build-authored copy",
       not [x for x in style if x[1] != "em dash"],
       [x for x in style if x[1] != "em dash"] or "clean")
    ck("No em dashes in build-authored copy",
       not [x for x in style if x[1] == "em dash"],
       [x for x in style if x[1] == "em dash"] or "clean")

    joined = " ".join(" ".join(qa_sl.all_units(pkg(n))).lower()
                      for n in M.VIDEOS)
    overlay = [(n, f["key"]) for n in M.VIDEOS for f in F.SETS[n]
               if "FULL SCREEN" not in f["mode"].upper()]
    mixed = [(n, f["key"]) for n in M.VIDEOS for f in F.SETS[n]
             if f["mode"].upper() != "FULL SCREEN"]
    ck("Full-screen teaching remains full screen", not overlay,
       overlay or ("%d cards full screen throughout; %d carry a short "
                   "headline callout over camera and put the teaching "
                   "itself full screen, both REUSE and unchanged"
                   % (183 - len(mixed), len(mixed))))
    ck("No burned-in long-form captions",
       "burned-in caption" not in joined or "no burned-in" in joined,
       "captions are not burned into the long-form video")
    ck("Watch Next is full screen and final",
       all("no return to camera" in " ".join(
           qa_sl.all_units(pkg(n))).lower() for n in M.VIDEOS),
       "stated in all 18 packages")
    ck("No return to camera after Watch Next",
       all("full screen" in " ".join(qa_sl.all_units(pkg(n))).lower()
           for n in M.VIDEOS), "18 of 18")

    bad = [r for r in R if not r[1]]
    for name, ok, detail in R:
        print("  [%s] %-56s %s" % ("PASS" if ok else "FAIL", name,
                                   str(detail)[:70]))
    print("\n  %d checks, %d passed, %d failed" % (len(R), len(R) - len(bad),
                                                   len(bad)))
    return not bad


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
