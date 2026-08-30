VIDEO 7 — FIRST-PASS PRODUCTION PACKAGE — QA README
How to Show Your Impact at Work When You Built It From Scratch

===============================================================================
1. WHAT WAS BUILT
===============================================================================

12 main slides and 24 reveal frames in the approved Capability Formation
visual system, a 12-page 16:9 PDF preview, three review sheets, the production
package DOCX, and the two script files generated from it.

Sources of truth used:
  · deliverables/video-6-slides/  — the approved Video 6 first-pass package,
    mirrored file for file and section for section.
  · deliverables/CAPABILITY_FORMATION_YOUTUBE_STANDARDS.md — locked recording
    and channel standards.
  · docs/claims-ledger.md — the repository's record of which public figures are
    sourced. This decided the metrics question in section 5 below.

Note on the roadmap audit: no file named as a roadmap audit exists in the
repository. The two sources above are the closest standing records and were
used in its place. If a separate roadmap audit document exists outside the
repository, this package has not been checked against it.

deck.py is carried forward from Video 6 unchanged — sha256 verified identical.
The palette, geometry, fonts and production conventions were not approximated;
they come from that file.

===============================================================================
2. DELIVERABLES
===============================================================================

  1  Video_7_Main_Slides.pptx                    12 editable slides
  2  Video_7_Reveal_Builds.pptx                  24 duplicate sequential slides
  3  Video_7_Slide_Preview.pdf                   12 pages, 13.333 x 7.5 in
  4  Video_7_Main_Slide_Contact_Sheet.png        all 12 slides
  5  Video_7_Reveal_Order_Sheet.png              all 24 frames in advance order
  6  Video_7_Phone_Legibility_Sheet.png          every slide at 320 x 180
  7  YouTube_Video_7_Production_Package_Impact_Without_Blueprint.docx
  8  Video_7_Teleprompter_Script_with_Slide_Markers.docx
  9  Video_7_Recording_Script_Clean.txt
 10  Video_7_First_Pass_QA_README.txt            this file

Editable sources are saved in the repository at deliverables/video-7-slides/
  build/deck.py        the shared rendering engine, unchanged from Video 6
  build/slides.py      the 12 slide definitions and the reveal map
  build/build.py       build and QA
  build/make_package.py  authors the production package DOCX
  script/make_scripts.py generates both script files from that DOCX
  script/verify.py     the script-identity and consistency checks

===============================================================================
3. THUMBNAIL — EXTERNALLY APPROVED, NOT IN THIS PACKAGE
===============================================================================

Locked copy: MAKE INVISIBLE WORK VISIBLE

The Video 7 thumbnail was created and approved in Canva outside this workflow.
No thumbnail was created, regenerated, reinterpreted, redesigned or edited
here, and no substitute was made.

STATUS: the approved Canva export was not present in the repository or in the
supplied assets when this package was built. It is recorded as an externally
approved asset still to be added. Supply the export and it will be included
byte-identically as an additional clearly named file, with a checksum recorded.

===============================================================================
4. QA — SLIDES AND DECKS
===============================================================================

  main slides in the deck                12          (required 12)
  reveal frames                          24          duplicate sequential slides
  reveal map per slide                   2,2,3,2,2,2,1,3,2,3,1,1
  PowerPoint animations                  none — reveals are duplicate slides
  PDF pages                              12
  PDF page size                          13.333 x 7.5 in (true 16:9)
  slide canvas                           1920 x 1080
  images or stock photography            0 picture shapes in the deck
  live text shapes                       55 — every word stays editable
  shapes outside the slide canvas        none
  elements outside the design canvas     none
  reveal states differ only by addition  yes — no element moves between states
  final reveal state matches main slide  yes, all 12
  slide 12 end-screen zone kept clear    yes
  no opening title card                  confirmed
  every slide rendered and inspected     yes — 12 PNGs plus 24 reveal frames
  phone legibility at 320 x 180          Video_7_Phone_Legibility_Sheet.png

Section 5 of the production package lists the copy for all 12 slides. Every
phrase in that section was searched for in the rendered PPTX text: all present,
none missing.

===============================================================================
5. QA — SCRIPT IDENTITY AND CONTENT BOUNDARIES
===============================================================================

The production package DOCX is the single source of truth. Both script files
are generated from it, so the three cannot drift apart.

  package spoken paragraphs              45
  teleprompter spoken paragraphs         45
  clean TXT paragraphs                   45
  clean TXT == package                   true
  teleprompter == package                true
  clean TXT == teleprompter              true
  spoken word count                      1502   (target 1,450-1,700)
  slide markers                          1-12, in order, none missing
  clean TXT contains timestamps          no
  clean TXT contains slide markers       no
  clean TXT contains directions          no

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

  30% retention improvement in script    ABSENT
  $2M+ turnover cost avoidance in script ABSENT

===============================================================================
6. OPEN EVIDENCE QUESTION
===============================================================================

The two figures were excluded, and the reason is on file rather than assumed.

docs/claims-ledger.md records both as "Needs source. No supporting document is
on file in this repository," and attributes them to an enterprise operating
role held before founding The Density Group — not to the first-in-role builder
story that opens this video. The ledger also notes that the estimation model
behind the turnover figure is not recorded. No evidence in this repository
connects either figure to this specific story, and no supportable attribution
exists, so both are excluded entirely.

QUESTION STILL OPEN, for Temidayo, not for the script:
  Is there a document — held outside this repository — that ties the 30%
  retention improvement or the $2M+ estimated turnover cost avoidance to the
  same first-in-role work described in the 0:35 block, with a stated
  population, baseline and measurement method?

  If yes, the 0:35 block could carry one figure, and the claims ledger should
  be updated at the same time. If no, the block stands as written. Nothing in
  the spoken script depends on the answer, and no unresolved fact request was
  placed inside the script.

Personal evidence in the video is held to the approved ceiling: the
first-in-role/builder line only. No company, role, date, conflict, result or
causal claim was invented around it.

===============================================================================
7. PUBLICATION GATES
===============================================================================

  · Chapter timestamps in the package are planning estimates. Reset them from
    the finished export before publishing.
  · The approved Canva thumbnail export must be supplied and added.
  · Watch-next routing: point the end screen at "How to Explain a Nonlinear
    Career Without Looking Unfocused" if it has published by the time Video 7
    goes live; otherwise use the Career Portability playlist. Slide 12 names
    the playlist either way, so no re-render is needed to switch.
  · Confirm temidayoafonja.com/keep-the-proof is live before publishing.

===============================================================================
8. WHAT WAS NOT TOUCHED
===============================================================================

No Video 1-6 deliverable was modified. Verified with git: the only changes in
this pass are new files under deliverables/video-7-slides/.
