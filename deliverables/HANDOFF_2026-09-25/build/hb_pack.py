# -*- coding: utf-8 -*-
"""Bundle one: Capability Formation V1 to V3, plus the 2027 playlist kit."""
import os, sys, io, shutil, zipfile, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
FIXED = (2026, 9, 25, 0, 0, 0)
STAGE = os.path.join(HERE, "_stage1")
NAME = "CAPABILITY_FORMATION_V1-V3_AND_PLAYLIST_2027.zip"

SOURCES = [
 (DELIV + "V1-V3_COMPLETE_PACKAGES/V01-V03_COMPLETE_PRODUCTION_PACKAGES.zip",
  "01_CAPABILITY_FORMATION_V1-V3_COMPLETE_PRODUCTION_PACKAGES"),
 (DELIV + "PLAYLIST_2027/PLAYLIST_2027_ALL_THREE_VIDEOS.zip",
  "02_PLAYLIST_2027_NEW_JOB_WITHOUT_STARTING_OVER"),
]

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

README = """\
==============================================================================
CAPABILITY FORMATION  |  V1 TO V3  +  THE 2027 PLAYLIST
==============================================================================

Two separate bodies of work in one archive, kept in separate folders because
they are separate series with separate numbering.

------------------------------------------------------------------------------
01_CAPABILITY_FORMATION_V1-V3_COMPLETE_PRODUCTION_PACKAGES
------------------------------------------------------------------------------

  Videos 1, 2 and 3 of the Capability Formation YouTube series, built to the
  approved complete-package standard. Seven folders per video: recording,
  visuals, editor, Shorts, publishing, viewer application, evidence and QA.

  V1  How to Change Careers After 10+ Years Without Starting Over
  V2  Is Your Job Making You Harder to Hire?
  V3  What You Can Still Prove After You Leave

  STATUS: LOCKED, editorially and operationally. Recording masters, thought
  blocks, visuals, trigger maps, editor instructions, Sticky Realizations,
  viewer actions, Shorts and evidence records are all locked. Publishing
  copy marked DRAFT or REVIEW REQUIRED stays draft until separately
  approved for that video's publication.

  ONE OPEN ITEM: V1's private provenance still needs the employer names and
  source URLs for both job postings. Those fields read NOT SUPPLIED. They
  were never inferred or invented and must not be.

  Also included: V01-V03_COMPLETE_PRODUCTION_PACKAGE_MANIFEST.docx, which
  lists every required artifact for each of the three videos as present or
  missing.

------------------------------------------------------------------------------
02_PLAYLIST_2027_NEW_JOB_WITHOUT_STARTING_OVER
------------------------------------------------------------------------------

  A separate three-video playlist for January 2027, built from the
  September 24, 2026 playlist document and production brief.

  Video 1  How to Get a New Job in 2027 When You Have 10+ Years of
           Experience                                  Monday, January 4
  Video 2  How to Answer "You Don't Have Direct Experience" When You Have
           10+ Years                                Wednesday, January 6
  Video 3  How to Get Referred When Your Network Is Thin
                                                       Friday, January 8

  Each folder holds the script, the slides as PPTX and PNG, the one-page
  Riverside recording sheet, the editor notes, the thumbnail, the upload
  sheet and the Shorts cut sheet. Its own README.txt sits at the root of
  that folder and lists every file.

  STATUS: built, not published. Nothing has been uploaded or scheduled.

  TWO LINKS TO RESOLVE BEFORE JANUARY 4: every description and end card
  points at temidayoafonja.com/career-evidence-starter, which has no page
  and no redirect in the site repository. Videos 1 and 2 also link
  temidayoafonja.gumroad.com/l/keep-the-proof. Both are reproduced exactly
  as written and neither was changed.

------------------------------------------------------------------------------
NOT IN THIS ARCHIVE
------------------------------------------------------------------------------

  Videos 4 to 14 ship separately. They are larger than a single shareable
  archive, so they are split in two, and they come with a companion
  document explaining how they were built:

      V04-V14_PRODUCTION_APPROACH_FOR_EDITORIAL_ADVISOR.docx

==============================================================================
"""

def build():
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    for src, folder in SOURCES:
        dest = os.path.join(STAGE, folder)
        os.makedirs(dest)
        with zipfile.ZipFile(src) as z:
            z.extractall(dest)
    io.open(os.path.join(STAGE, "README.txt"), "w",
            encoding="utf-8").write(README)
    zp = os.path.join(OUT, NAME)
    names = sorted(os.path.relpath(os.path.join(r, f), STAGE)
                   for r, _d, fs in os.walk(STAGE) for f in fs)
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, open(os.path.join(STAGE, rel), "rb").read())
    io.open(zp + ".sha256", "w", encoding="utf-8").write(
        "%s  %s\n" % (sha256(zp), NAME))
    return zp, names

if __name__ == "__main__":
    zp, names = build()
    print("%s  %.2f MiB  %d files" % (os.path.basename(zp),
                                      os.path.getsize(zp) / 1048576.0,
                                      len(names)))
    print(sha256(zp))
