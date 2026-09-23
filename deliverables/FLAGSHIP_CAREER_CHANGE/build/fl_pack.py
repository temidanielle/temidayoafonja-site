# -*- coding: utf-8 -*-
"""Asset index, private provenance file, and the delivery ZIP."""
import os, sys, zipfile, hashlib, textwrap
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import fl_frames as F, fl_prov as P

VIS = os.path.join(OUT, "04_VISUAL_ASSETS")
ZIPNAME = "FLAGSHIP_CAREER_CHANGE_VISUAL_ASSETS.zip"
FIXED = (2026, 9, 23, 0, 0, 0)
SVGS = ("FLAG_01_THE_MOVE", "FLAG_02D_WHERE_ADVICE_STOPS",
        "FLAG_05C_HIGHER_TITLE", "FLAG_06C_ALL_GAPS",
        "FLAG_07D_COMPLETE", "FLAG_08_EXPERIENCED_AND_NEW")

SLIDE_TITLES = {
 "FLAG_01_THE_MOVE": "SLIDE 1  |  PUT THE MOVE ON THE TABLE",
 "FLAG_02_FIRST_READ": "SLIDE 2  |  AT FIRST, THIS LOOKS VERY TRANSFERABLE",
 "FLAG_03_RE_HOOK": "SLIDE 3  |  THE RE-HOOK",
 "FLAG_04_WHAT_TRAVELS": "SLIDE 4  |  WHAT ACTUALLY LOOKS PORTABLE?",
 "FLAG_05_THE_DIFFERENCE": "SLIDE 5  |  HERE IS WHERE THE ROLES SPLIT",
 "FLAG_06_THE_REAL_GAP": "SLIDE 6  |  THIS IS NOT A WORDING PROBLEM",
 "FLAG_07_THE_FULL_READ": "SLIDE 7  |  THE FULL CAREER MOVE READ",
 "FLAG_08_THE_POINT": "SLIDE 8  |  THE HUMAN PAYOFF",
}

def w(t, ind=6):
    return "\n".join(textwrap.fill(t, 74, initial_indent=" " * ind,
                                   subsequent_indent=" " * ind).splitlines())

def asset_index(path):
    L = []
    L.append("=" * 78)
    L.append("FLAGSHIP EVERGREEN  |  ASSET INDEX")
    L.append("=" * 78)
    L.append("")
    L.append(F.TITLE)
    L.append("THUMBNAIL: " + F.THUMB)
    L.append("")
    n = sum(1 for _ in F.states())
    L.append(w("%d rendered states across 8 core slides. All 1920 x 1080. "
               "Navy #112345, cream #F5F1E8, gold #C9A84C, yellow #F2C44C, "
               "with the rust accent and the derived tints the house system "
               "already uses." % n, 0))
    L.append("")
    L.append(w("Employer names appear nowhere in these assets. The two "
               "postings are Role A and Role B throughout. The private "
               "mapping back to source language is in "
               "FLAGSHIP_JD_PROVENANCE.md, which is not for publication.", 0))
    L.append("")
    L.append(w("The phone-size contact sheet is a proof sheet of these "
               "states, not a state. It is listed at the end and is not "
               "counted above.", 0))
    L.append("")
    L.append("!" * 78)
    L.append("SPOKEN MASTER SYNCHRONIZATION REQUIRED BEFORE RECORDING.")
    L.append("!" * 78)
    L.append("")
    L.append(w("The flagship recording master still uses the earlier "
               "hypothetical example: Senior Manager, Operations moving to "
               "Strategy Director. These approved assets use the real-artifact "
               "sequence: Senior Manager, Program Management moving to "
               "Director, Enterprise Transformation.", 0))
    L.append("")
    L.append(w("The visuals are the approved direction. The next spoken-master "
               "revision replaces the hypothetical role example with this "
               "sequence. Do not record against the current master and do not "
               "change these slides back to fit it.", 0))
    L.append("")
    L.append(w("Also outstanding: the private provenance file lists six "
               "fields still needed for both roles before publication. See "
               "FLAGSHIP_JD_PROVENANCE.md.", 0))
    L.append("")
    L.append("-" * 78)
    for fam, sts in F.SETS:
        L.append("")
        L.append(SLIDE_TITLES[fam])
        L.append("   " + fam)
        for i, (name, draw, note) in enumerate(sts, 1):
            L.append("      %d. %s.png" % (i, name))
            L.append(w(note, 9))
        if fam in [s[:len(fam)] for s in SVGS] or any(
                s in [x[0] for x in sts] for s in SVGS):
            for s in SVGS:
                if s in [x[0] for x in sts]:
                    L.append("      editable: %s.svg" % s)
    L.append("")
    L.append("-" * 78)
    L.append("")
    L.append("Phone_Size_Contact_Sheet.png")
    L.append(w("Proof sheet of all %d states at phone width." % n, 6))
    L.append("")
    L.append("FLAGSHIP_JD_PROVENANCE.md")
    L.append(w("PRIVATE. Do not publish. Maps every rephrased posting line "
               "on a slide back to the source language, with its "
               "classification and a note on what was shortened.", 6))
    L.append("")
    open(path, "w").write("\n".join(L) + "\n")
    return path

def provenance(path):
    L = []
    L.append("# FLAGSHIP JD PROVENANCE")
    L.append("")
    L.append("**PRIVATE. NOT FOR PUBLICATION.**")
    L.append("")
    L.append("Video: %s" % F.TITLE)
    L.append("Thumbnail: %s" % F.THUMB)
    L.append("Generated: September 23, 2026")
    L.append("")
    L.append("Every line of posting language that appears on a slide is "
             "mapped here to what the source read says, so a reviewer can "
             "confirm that no visual changed the meaning.")
    L.append("")
    L.append("## Roles")
    L.append("")
    L.append("| Public identifier | Role title | Employer | Source URL |")
    L.append("|---|---|---|---|")
    L.append("| ROLE A | Senior Manager, Program Management | NOT SUPPLIED | "
             "NOT SUPPLIED |")
    L.append("| ROLE B | Director, Enterprise Transformation | NOT SUPPLIED | "
             "NOT SUPPLIED |")
    L.append("")
    L.append("## What is missing")
    L.append("")
    L.append(P.UNAVAILABLE.strip())
    L.append("")
    L.append("## Required against preferred")
    L.append("")
    L.append(P.CLASSIFICATION.strip())
    L.append("")
    L.append("## Line by line")
    L.append("")
    L.append("| Public display text | Original source language | Slide | "
             "Classification | Notes |")
    L.append("|---|---|---|---|---|")
    for a, b, c, d, e in P.MAP:
        L.append("| %s | %s | %s | %s | %s |" %
                 (a.replace("|", "/"), b.replace("|", "/"), c, d,
                  e.replace("|", "/")))
    L.append("")
    open(path, "w").write("\n".join(L) + "\n")
    return path

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()

def main():
    asset_index(os.path.join(VIS, "Asset_Index.txt"))
    provenance(os.path.join(OUT, "FLAGSHIP_JD_PROVENANCE.md"))
    names = sorted(os.listdir(VIS))
    zp = os.path.join(OUT, ZIPNAME)
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for n in names:
            zi = zipfile.ZipInfo("04_VISUAL_ASSETS/" + n, date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(VIS, n), "rb") as f:
                z.writestr(zi, f.read())
    with open(zp + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zp), ZIPNAME))
    return zp, names

if __name__ == "__main__":
    zp, names = main()
    print("%d files in the archive" % len(names))
    print(zp)
    print(sha256(zp))
