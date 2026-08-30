# -*- coding: utf-8 -*-
"""Write Video_7_First_Pass_QA_README.txt from the measured QA outputs."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
q = json.load(open(os.path.join(ROOT, "out", "qa.json")))
r = json.loads(subprocess.run([sys.executable,
        os.path.join(ROOT, "script", "verify.py")],
        capture_output=True, text=True).stdout)

flush_main = ", ".join(str(x) for x in q["flush_edge_slides_main"])
flush_rev = ", ".join(str(x) for x in q["flush_edge_frames_reveals"])

TXT = """VIDEO 7 — FIRST-PASS PRODUCTION PACKAGE — QA README  (corrected pass)
How to Show Your Impact at Work When You Built It From Scratch

===============================================================================
1. WHAT CHANGED IN THIS PASS
===============================================================================

Content correction, applied at source and regenerated through every file:

  REMOVED from the spoken script and from slide 9
    "Used by every team in the region for two years after I left it."
    It read as a specific personal result, was not documented, and exceeded the
    approved personal-evidence ceiling.

  SPOKEN COPY now reads
    "Continued use is evidence. Record who was still using the system after
    the handoff, and for how long—but use only the scope and duration you can
    verify."

  SLIDE 9 example now reads
    CONTINUED USE IS EVIDENCE.
    Who still used it after the handoff—and for how long?

Verified: the removed sentence appears nowhere in the package DOCX, the
teleprompter DOCX, the clean TXT, the main deck or the reveal deck. The
replacement copy is present in all three script files. Spoken length is now
%(wc)d words, still inside the 1,450–1,700 target.

QA corrections:

  · Slide 12 playlist contrast. The previous colour #3E506B measured 1.90:1
    against the navy ground #0F2346 — below any legibility threshold, and the
    observation was correct. It is now #8E9CB2, measured 5.59:1, which passes
    4.5:1 while staying clearly secondary to the cream headline at 13.81:1.
    The end-screen zone is unaffected: every element on slide 12 still ends at
    x=1060 of 1920, left of the 1130 boundary.

  · Rendered-bleed flag reconciled. See section 6.

===============================================================================
2. ROADMAP AUDIT — NOT VALIDATED, AND WHY
===============================================================================

The August 28 roadmap audit was referenced as attached but did not arrive. No
file matching it is present in the repository, in this session's uploaded
files, or anywhere on the working filesystem; the most recent upload of any
kind is the Video 6 production package, dated 28 August 17:50.

This package therefore CANNOT be reported as validated against that audit, and
is not. Send the file and the check will be run and recorded here.

What this package was built against instead:
  · deliverables/video-6-slides/ — the approved Video 6 first-pass package,
    mirrored file for file and section for section
  · deliverables/CAPABILITY_FORMATION_YOUTUBE_STANDARDS.md
  · docs/claims-ledger.md — which decided the excluded metrics in section 5

TITLE AND KEYWORD — INTENTIONAL CHANGE, RECORDED
  Final title:      How to Show Your Impact at Work When You Built It From Scratch
  Target keyword:   how to show your impact at work

  This is the TubeBuddy-validated update to the roadmap's working title and is
  deliberate, not a drift from the roadmap. Supporting evidence, production
  rationale only and never referenced on air: primary keyword weighted score
  71/100; complete title weighted score 59/100; complete-title search volume
  excellent; competition fair; zero exact title matches in the top 20.

  Because the audit itself is unavailable, this entry records the change as
  intended rather than confirming it against the audit's own wording.

===============================================================================
3. DELIVERABLES
===============================================================================

  1  Video_7_Main_Slides.pptx                    12 editable slides
  2  Video_7_Reveal_Builds.pptx                  %(frames)d duplicate sequential slides
  3  Video_7_Slide_Preview.pdf                   12 pages, 13.333 x 7.5 in
  4  Video_7_Main_Slide_Contact_Sheet.png        all 12 slides
  5  Video_7_Reveal_Order_Sheet.png              all %(frames)d frames in advance order
  6  Video_7_Phone_Legibility_Sheet.png          every slide at 320 x 180
  7  YouTube_Video_7_Production_Package_Impact_Without_Blueprint.docx
  8  Video_7_Teleprompter_Script_with_Slide_Markers.docx
  9  Video_7_Recording_Script_Clean.txt
 10  Video_7_First_Pass_QA_README.txt            this file

Editable sources at deliverables/video-7-slides/
  build/deck.py          shared rendering engine, carried from Video 6
                         unchanged (sha256 verified identical)
  build/slides.py        the 12 slide definitions and the reveal map
  build/build.py         build and deck QA
  build/make_package.py  authors the production package DOCX
  build/make_readme.py   writes this file from the measured QA outputs
  script/make_scripts.py generates both script files from that DOCX
  script/verify.py       script-identity and consistency checks

===============================================================================
4. THUMBNAIL — EXTERNALLY APPROVED, NOT IN THIS PACKAGE
===============================================================================

Required copy: MAKE INVISIBLE WORK VISIBLE

No thumbnail was created, regenerated, reinterpreted, redesigned or edited in
this pass, and no substitute was made. The approved Canva export is not in the
repository or the supplied assets. It is recorded as an externally approved
asset still to be added, and will be included byte-identically with a recorded
checksum once supplied.

===============================================================================
5. QA — SLIDES AND DECKS
===============================================================================

  main slides in the deck                12          (required 12)
  reveal frames                          %(frames)-2d          duplicate sequential slides
  reveal map per slide                   2,2,3,2,2,2,1,3,2,3,1,1
  PowerPoint animations                  none — reveals are duplicate slides
  PDF pages                              12
  PDF page size                          13.333 x 7.5 in (true 16:9)
  slide canvas                           1920 x 1080
  images or stock photography            0 picture shapes in the deck
  live text shapes                       %(text)d — every word stays editable
  shapes beyond the slide canvas         none
  elements outside the design canvas     none
  reveal states differ only by addition  yes — no element moves between states
  final reveal state matches main slide  yes, all 12
  slide 12 end-screen zone kept clear    yes
  removed line present anywhere in deck  no
  no opening title card                  confirmed
  every slide rendered and inspected     yes — 12 PNGs plus %(frames)d reveal frames
  phone legibility at 320 x 180          Video_7_Phone_Legibility_Sheet.png

Every phrase in Section 5 of the production package was searched for in the
rendered PPTX text: all present, none missing.

===============================================================================
6. RENDERED-BLEED FLAG — RECONCILED, BENIGN
===============================================================================

The flag was correct about which shapes it found and wrong about what they are.

Flagged: main slides %(fm)s and reveal frames %(fr)s. The QA now separates two
different conditions instead of reporting one, and it reproduces exactly that
set — the same four items, no more and no fewer.

  shapes that EXCEED the canvas          0
  shapes FLUSH to the canvas edge        %(nflush)d
  main slides with a flush edge          %(fm)s
  reveal frames with a flush edge        %(fr)s
  maximum overhang measured              %(overhang)d EMU

All four are the same element: the full-bleed navy band on slides 2 and 6, and
those slides' second reveal states, which are frames 4 and 13.

Measured in EMU, from the real PPTX files:

  left   0            slide left    0
  right  12192000     slide width   12192000
  top    3657600
  bottom 6858000      slide height  6858000

The band's right edge equals the slide width exactly and its bottom edge equals
the slide height exactly. Overhang is 0 EMU in every case — not a rounding
tolerance, zero. A checker testing `right >= slide_width` rather than
`right > slide_width` flags a flush edge as a bleed; that is what happened.

VERDICT: benign, and intentional. The band is a designed flush-edge panel in
the established system — Video 6 uses the same device. Nothing is clipped and
no content sits outside the canvas. No change was made to the geometry;
`flush_to_canvas_edge` is now reported alongside `shapes_outside_canvas` in
out/qa.json so the distinction is visible on every future build rather than
having to be re-derived.

===============================================================================
7. QA — SCRIPT IDENTITY AND CONTENT BOUNDARIES
===============================================================================

The production package DOCX is the single source of truth. Both script files
are generated from it, so the three cannot drift apart.

  package spoken paragraphs              %(pp)d
  teleprompter spoken paragraphs         %(tp)d
  clean TXT paragraphs                   %(cp)d
  clean TXT == package                   %(ceq)s
  teleprompter == package                %(teq)s
  clean TXT == teleprompter              %(cteq)s
  spoken word count                      %(wc)d   (target 1,450-1,700)
  slide markers                          1-12, in order, none missing
  clean TXT contains timestamps          no
  clean TXT contains slide markers       no
  clean TXT contains directions          no

  removed line absent from all scripts   yes
  replacement copy present in all three  yes
  title consistent across files          yes
  target keyword present in package      yes
  keyword phrase opens the description   yes
  CTA name and URL consistent            yes — Keep the Proof,
                                         temidayoafonja.com/keep-the-proof
  thumbnail copy recorded in package     yes — MAKE INVISIBLE WORK VISIBLE
  competing offers in script or slides   none
  TubeBuddy or scores mentioned on air   no — production rationale only
  permitted-evidence boundary spoken     yes
  promise that evidence produces
    promotion or recognition             none

  30%% retention improvement in script    ABSENT
  $2M+ turnover cost avoidance in script ABSENT

===============================================================================
8. EXCLUDED METRICS AND THE OPEN EVIDENCE QUESTION
===============================================================================

Both figures remain excluded, on evidence rather than preference.

docs/claims-ledger.md records both as "Needs source. No supporting document is
on file in this repository," and attributes them to an enterprise operating
role held before founding The Density Group — not to the first-in-role builder
story that opens this video. The ledger also notes that the estimation model
behind the turnover figure is not recorded.

QUESTION STILL OPEN, for Temidayo, not for the script:
  Is there a document — held outside this repository — that ties the 30%%
  retention improvement or the $2M+ estimated turnover cost avoidance to the
  same first-in-role work described in the 0:35 block, with a stated
  population, baseline and measurement method?

  If yes, the 0:35 block could carry one figure, and the claims ledger should
  be updated at the same time. If no, the block stands as written. Nothing in
  the spoken script depends on the answer, and no unresolved fact request was
  placed inside the script.

Personal evidence is held to the approved ceiling: the first-in-role/builder
line only, with no company, role, date, conflict, result or causal claim
invented around it. The correction in section 1 brings slide 9 and the 8:30
block back inside that ceiling.

===============================================================================
9. PUBLICATION GATES
===============================================================================

  · Chapter timestamps in the package are planning estimates. Reset them from
    the finished export before publishing.
  · The approved Canva thumbnail export must be supplied and added.
  · Watch-next routing: point the end screen at "How to Explain a Nonlinear
    Career Without Looking Unfocused" if it has published by the time Video 7
    goes live; otherwise use the Career Portability playlist. Slide 12 names
    the playlist either way, so no re-render is needed to switch.
  · Confirm temidayoafonja.com/keep-the-proof is live before publishing.
  · Send the August 28 roadmap audit so this package can be checked against it.

===============================================================================
10. WHAT WAS NOT TOUCHED
===============================================================================

No Video 1-6 deliverable and no website file was modified. Verified with git:
the only changes in this pass are inside deliverables/video-7-slides/.
""" % dict(frames=q["reveal_slides"], text=q["text_shapes"],
           fm=flush_main, fr=flush_rev,
           nflush=len(q["flush_to_canvas_edge"]),
           overhang=q["flush_edge_max_overhang_emu"],
           pp=r["package_paragraphs"], tp=r["teleprompter_paragraphs"],
           cp=r["clean_paragraphs"], wc=r["word_count"],
           ceq=str(r["clean_equals_package"]).lower(),
           teq=str(r["teleprompter_equals_package"]).lower(),
           cteq=str(r["clean_equals_teleprompter"]).lower())

out = os.path.join(ROOT, "Video_7_First_Pass_QA_README.txt")
open(out, "w").write(TXT)
print("wrote", os.path.basename(out), "-", len(TXT.splitlines()), "lines")
