# -*- coding: utf-8 -*-
"""Bundle two: videos 4 to 14.

The whole set is 38 MiB, past the share limit, so it goes out as two parts.
Each part is self-contained and carries the advisor document and the presence
manifest, so either one can be opened on its own.
"""
import os, sys, io, shutil, zipfile, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
FIXED = (2026, 9, 25, 0, 0, 0)
STAGE = os.path.join(HERE, "_stage2")
SRC = DELIV + "V4-V14_COMPLETE_PACKAGES/V04-V14_COMPLETE_PRODUCTION_PACKAGES.zip"
DOC = "V04-V14_PRODUCTION_APPROACH_FOR_EDITORIAL_ADVISOR.docx"
GROUPS = [("PART_1_OF_2_VIDEOS_04-09", range(4, 10)),
          ("PART_2_OF_2_VIDEOS_10-14", range(10, 15))]

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

HEAD = """\
==============================================================================
CAPABILITY FORMATION  |  VIDEOS 4 TO 14  |  COMPLETE PRODUCTION PACKAGES
%s
==============================================================================

The full set is larger than a single shareable archive, so it ships as two
parts. This is %s. The two parts together hold all eleven videos and
nothing is duplicated between them except the two documents below, which are
in both so either part can be read on its own.

  V04-V14_PRODUCTION_APPROACH_FOR_EDITORIAL_ADVISOR.docx
      How these eleven packages were built, what was reused rather than
      made, and the seven questions that are open and need an editorial
      decision. This is the document to hand to the advisor.

  V04-V14_COMPLETE_PRODUCTION_PACKAGE_MANIFEST.docx
      Every required artifact for every one of the eleven videos, listed as
      present or missing. 31 artifacts per video, 341 slots, none missing.

------------------------------------------------------------------------------
IN THIS PART
------------------------------------------------------------------------------

%s
------------------------------------------------------------------------------
STATUS
------------------------------------------------------------------------------

  V4 to V11   REOPENED for the limited editorial refresh described in the
              September 24 audit. The packages here are the base source.
              They are not superseded until revised masters are approved.

  V12 to V14  LOCKED. Not part of the refresh and not to be modified.

  Each video folder holds seven sub-folders: 01 recording, 02 visuals,
  03 editor, 04 Shorts, 05 publishing, 06 viewer application, and
  07 evidence and QA.

  Every recording master and thought-block copy in here is byte for byte
  identical to the locked V1 to V14 archive. Verified by checksum, all 22
  of them.

==============================================================================
"""

def titles():
    sys.path.insert(0, DELIV + "V4-V14_COMPLETE_PACKAGES/build")
    import ap_meta as M
    return {n: M.TITLES[n][0] for n in range(4, 15)}

def build():
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    with zipfile.ZipFile(SRC) as z:
        z.extractall(STAGE)
    shutil.copy2(os.path.join(OUT, DOC), os.path.join(STAGE, DOC))
    T = titles()
    out = []
    for tag, grp in GROUPS:
        listing = "\n".join(
            "  V%-4d %s\n        VIDEO_%02d_COMPLETE_PRODUCTION_PACKAGE/"
            % (n, T[n], n) for n in grp)
        readme = HEAD % (tag.replace("_", " ").title(),
                         tag.replace("_", " ").lower(), listing + "\n")
        rp = os.path.join(STAGE, "README.txt")
        io.open(rp, "w", encoding="utf-8").write(readme)
        keep = tuple("VIDEO_%02d_COMPLETE_PRODUCTION_PACKAGE/" % n for n in grp)
        names = sorted(os.path.relpath(os.path.join(r, f), STAGE)
                       for r, _d, fs in os.walk(STAGE) for f in fs)
        sel = [x for x in names
               if x.replace(os.sep, "/").startswith(keep)
               or x in ("README.txt", DOC,
                        "V04-V14_COMPLETE_PRODUCTION_PACKAGE_MANIFEST.docx")]
        zp = os.path.join(OUT, "CAPABILITY_FORMATION_VIDEOS_04-14_%s.zip" % tag)
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED,
                             compresslevel=6) as z:
            for rel in sel:
                zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                z.writestr(zi, open(os.path.join(STAGE, rel), "rb").read())
        io.open(zp + ".sha256", "w", encoding="utf-8").write(
            "%s  %s\n" % (sha256(zp), os.path.basename(zp)))
        out.append((zp, len(sel)))
    return out

if __name__ == "__main__":
    for zp, n in build():
        print("%-58s %6.2f MiB  %3d files"
              % (os.path.basename(zp), os.path.getsize(zp) / 1048576.0, n))
        print("   %s" % sha256(zp))
