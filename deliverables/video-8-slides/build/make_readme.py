# -*- coding: utf-8 -*-
"""Write Video_8_First_Pass_QA_README.txt from the measured QA outputs."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
q = json.load(open(os.path.join(ROOT, "out", "qa.json")))
r = json.loads(subprocess.run([sys.executable,
        os.path.join(ROOT, "script", "verify.py")],
        capture_output=True, text=True).stdout)

import zipfile as _z
_pkg = os.path.join(ROOT, "YouTube_Video_8_Production_Package_New_Industry.docx")
ROWS = _z.ZipFile(_pkg).read("word/document.xml").decode("utf8").count("<w:cantSplit")

fm = ", ".join(str(x) for x in q["flush_edge_slides_main"])
fr = ", ".join(str(x) for x in q["flush_edge_frames_reveals"])

TXT = """VIDEO 8 - FIRST-PASS PRODUCTION PACKAGE - QA README
How to Move Into a New Industry Without Starting Over

Latest pass: targeted corrections. Preserved without substantive change - the
title, target keyword, thumbnail copy, opening distinction, personal evidence,
the three teaching moves, the Field Kit as sole CTA, the fieldkit URL, the
exclusion of the 30%% and $2M+ claims, and the visual system.

===============================================================================
1. WHAT THE CORRECTION PASS CHANGED
===============================================================================

1.1  VIEWER DEFINITION BROADENED

  Was   "Experienced professional, particularly a senior corporate woman with
        substantial career history and real financial, family and reputational
        stakes."
  Now   "Experienced professionals - especially mid-career and senior
        professionals, managers, directors and experienced specialists -
        considering a move into a new industry without wanting to erase their
        prior experience."

  The public-facing viewer is no longer gendered; the roadmap does not require
  it for this video. Verified: "senior corporate woman" appears nowhere in the
  package.

1.2  FOUR GENERALISATIONS SOFTENED

  Applied at source and regenerated through the package DOCX, teleprompter
  DOCX, clean TXT, description, pinned comment and speaker notes. No
  replacement statistic, research claim or universal conclusion was introduced.

    was  "...closes faster than most people expect when someone is deliberate
         about closing it."
    now  "...it can close when you are deliberate about learning it."

    was  "...nothing to evaluate, and experienced people stop hearing them
         entirely."
    now  "...very little to evaluate, and experienced interviewers have heard
         them many times."

    was  "A clear first-ninety-days learning plan counts for more than most
         people expect."
    now  "A clear first-ninety-days learning plan can also reduce the
         credibility gap."

    was  "Most people find the first column is longer than they feared and the
         third is shorter than they assumed."
    now  "You may find the first column is longer than you feared and the third
         is shorter than you assumed."

  The fourth also appeared in the pinned comment and in slide 10's speaker
  note; both were softened to match. Verified: all four new forms present, all
  four superseded forms absent.

1.3  WATCH-NEXT MADE PUBLICATION-SAFE

  No unpublished video is named in the recorded script or on the final slide.

    spoken   "When you are ready for the next step, continue with the Career
             Portability playlist."
    slide 12 CONTINUE THE SERIES
             CAREER PORTABILITY
             CAREER PIVOTS  -  INTERNAL MOVES  -  GROWTH

  INTENDED ROUTING, set at upload:
    - If the next video in the sequence is public when Video 8 publishes, the
      YouTube end-screen video element may route directly to it.
    - Otherwise, route to the public Career Portability playlist.
    - Verify before publication that the selected playlist contains at least
      one other public video and opens successfully in a signed-out browser.
    - Do not use a playlist containing only Video 8 as the fallback.

  The next title is held in the roadmap audit and in these QA notes only. It is
  in no spoken or on-slide wording, so neither route needs a re-record or a
  re-render. Verified: the script contains no reference to a layoff video, and
  slide 12 names only the playlist.

1.4  WORD-COUNT METHOD DOCUMENTED AND APPLIED CONSISTENTLY

  Python str.split() on whitespace, over the spoken paragraphs of section 4
  only. Timed block headers and the target line are excluded. The same method
  produces the count in the package DOCX, in this README and in the build
  output. Recorded in section 1 of the package.

  Word count after the corrections: %(wc)d, down from 1,607. Spoken paragraphs
  remain 38, as required.

1.5  PAGINATION REPAIRED STRUCTURALLY - AND A LIMITATION TO STATE PLAINLY

  Package DOCX:
    - w:cantSplit on every table row - all %(rows)d of them - so no row can
      break across a page. That covers the "Title relationship to the roadmap"
      row, every slide-content row, and the slide 11 Field Kit URL row, which
      can no longer strand "kit" on a following page.
    - w:keepNext on every section heading and sub-heading, so no heading is
      left alone at the foot of a page.
    - w:keepLines on table cell paragraphs and on description lines.
    - w:autoHyphenation off, so Word will not break a URL or a filename with a
      hyphen.
    - The section 6 filename column widened from 2.6in to 3.1in so full
      filenames fit without wrapping, rather than shrinking the type.
    - Font sizes and margins unchanged.

  Teleprompter DOCX:
    - w:keepNext and w:keepLines on all 12 slide markers and all 9 timed
      headers, so a marker cannot be separated from the paragraph it
      introduces and the closing block cannot strand alone.
    - Paragraph spacing eased from 14pt/1.55 to 12pt/1.50. Type size unchanged
      at 13.5pt; the text was not compressed to remove a page.
    - w:autoHyphenation off.

  THE LIMITATION: I could not render either DOCX to pages and inspect them.
  LibreOffice in this environment cannot load any .docx - the Writer filter
  registry (writer.xcd) is absent. Verified as environmental rather than caused
  by these files: the same command fails on the unmodified, independently
  reviewed Video 6 production package with "source file could not be loaded".

  So the pagination work is verified STRUCTURALLY, by reading the generated XML
  - every attribute is confirmed present - but NOT visually. Page counts,
  orphans, widows and awkward breaks should be checked once in Word or Google
  Docs. These are the standard mechanisms Word uses for exactly these problems,
  so the fixes should hold, but I have not seen the pages and am not reporting
  that I have.

===============================================================================
2. ONE CONFLICT TO RESOLVE BEFORE RECORDING
===============================================================================

CAREER SPAN: the brief and the roadmap say "18 years." The claims ledger
says that wording was retired.

  Brief          "approximately 18 years of professional experience" is
                 permitted personal evidence.
  Roadmap audit  "Over roughly 18 years, I have worked across eight industries
                 and sectors and progressed from Consultant to Head of
                 Function."
  Claims ledger  Section 6, Career span. "The wording changed to 'nearly two
                 decades' on every page. Verified by search: 'eighteen years'
                 appears nowhere in the repository, in any casing." Resolved by
                 operator decision, August 2026. Date range 2008 to 2026.

  The ledger also records WHY: the published claim read "eighteen years" while
  the visible career timeline began at 2011, which reads as fifteen. Both
  remedies were taken - the wording was changed everywhere, and a 2008-2011
  timeline entry was added.

  WHAT THIS PACKAGE DID, and it is a judgement call, not a silent fix:
  the script says "over nearly two decades." That is the same fact in the
  approved public wording, and it satisfies the brief's intent - establishing
  why Temidayo understands cross-industry transition - without reintroducing
  retired wording into public-facing material.

  YOUR DECISION: if you want "18 years" spoken instead, say so and the line
  will be changed. If the ledger wording stands, no action is needed. Nothing
  else in the script depends on this.

No other conflict was found between the brief, the roadmap audit, the claims
ledger and the Video 7 precedent. Everything else lines up - see section 4.

===============================================================================
3. WHAT WAS BUILT
===============================================================================

12 main slides and %(frames)d reveal frames in the approved Capability Formation
visual system, a 12-page 16:9 PDF preview, three review sheets, the production
package DOCX, and the two script files generated from it.

Sources read before any change was made:
  - No AGENTS.md or CLAUDE.md exists in this repository; none was found at any
    depth, so there were no repository instructions to follow beyond the files
    below.
  - deliverables/video-7-slides/ - the approved and closed Video 7 package,
    used as the structural, visual and technical precedent, including its final
    QA README.
  - reference/YouTube_Audience_and_20_Video_Roadmap_Audit_Aug28_2026.docx
    sha256 df1754b8698d6ed7a149794893bf9fae21983ff70040da00b24339b611ff0a05
    Stored here byte-identically, copied from the Video 7 package.
  - deliverables/CAPABILITY_FORMATION_YOUTUBE_STANDARDS.md
  - docs/claims-ledger.md - checked before every personal claim. See sections
    1 and 4.

deck.py is carried forward from Video 7 unchanged - sha256 verified identical,
cc24c1f24eceb80b... So the navy, cream, gold, geometry, fonts and production
conventions are inherited rather than approximated.

===============================================================================
4. COMPARISON AGAINST THE AUGUST 28 ROADMAP AUDIT
===============================================================================

Sequence row 8 in the audit:

  Recommended title   How to Change Industries Without Starting at Entry Level
  Thumbnail           YOUR EXPERIENCE STILL COUNTS
  Viewer question     What can I carry into a field where I am new?
  CTA                 Field Kit
  Why here            "Fulfills the public promise directly and replaces
                      generic interview content."

Production architecture row 8:

  Early lived proof   "18 years; eight industries/sectors; three Big Four;
                      CISM attempt and IAPP chapter show relearning."
  Three moves         "Separate capability/context/credential; match
                      destination problems; build bridge evidence and a
                      learning plan."

  Package               Audit                          Result
  Thumbnail copy        YOUR EXPERIENCE STILL COUNTS   exact match
  Viewer question       identical                      exact match
  CTA                   Field Kit                      exact match
  Move one              separate capability/context/
                        credential                     verbatim, slides 3-6
  Move two              match destination problems     verbatim, slides 7-8
  Move three            bridge evidence + learning
                        plan                           verbatim, slide 9
  Career span           "18 years"                     SEE SECTION 2
  Title                 working title                  intentional SEO
                                                       refinement, recorded

  TITLE - INTENTIONAL REFINEMENT, RECORDED
    Final title    How to Move Into a New Industry Without Starting Over
    Keyword        how to move into a new industry

    TubeBuddy, 30 August 2026, production rationale only and never referenced
    on air: 73/100 weighted for the target keyword, Very Good; 71/100 for
    "how to switch industries without starting over"; 69/100 for "transferable
    skills for a career change"; the roadmap's working wording scored 58/100.

    The change is consistent with the audit's own title rule - "a recognizable
    search question or consequence." Viewer question, thumbnail copy, CTA and
    the three moves are unchanged from the roadmap.

  CTA ROUTING - CONFIRMED
    The audit's CTA routing table assigns the Capability Formation Field Kit to
    Videos 1, 2, 6, 8, 10, 12, 13, 14, 19, 20, 22 and 23, with the boundary
    "Primary method product. Do not stack Keep the Proof beside it," and the
    URL https://temidayoafonja.com/fieldkit. Video 8 is in that list. QA
    confirms no competing offer anywhere in the script or the decks.

  IAPP CHAPTER - AVAILABLE, NOT USED
    The audit lists the IAPP chapter alongside CISM as evidence of relearning.
    The brief's personal-evidence ceiling does not include it, so it was left
    out. Available if you want it in a later pass.

===============================================================================
5. PERSONAL EVIDENCE - USED AND EXCLUDED
===============================================================================

USED, all inside the brief's ceiling and checked against the claims ledger:
  - career span, spoken as "nearly two decades" (see section 1)
  - work across eight industries and sectors
  - Deloitte, EY and PwC, named in speech only; no logo appears on screen
  - progression from Consultant to Head of Function
  - preparation for the CISM exam and an unsuccessful first attempt

EXCLUDED DELIBERATELY:
  - the 30%% retention improvement. The claims ledger records it as "Needs
    source. No supporting document is on file in this repository," attributed
    to an enterprise operating role. The roadmap adds: "Do not attach either
    metric to a role or intervention until the relationship is documented."
    Nothing connects it to an industry-change story.
  - the $2M+ estimated turnover cost avoidance, on the same basis.
  - any promotion attributed to a specific industry. The roadmap boundary is
    "do not claim promotion in every industry"; no promotion is tied to any
    named industry anywhere in the script.
  - any claim that a move was seamless, that a prior skill transferred
    automatically, or that any employer caused a later outcome.
  - any CISM score, date, reason or consequence. The script says only that she
    prepared and did not pass the first time.
  - the IAPP chapter, which the ceiling in the brief does not cover.

Verified by search across the finished script:
  "18 years" and "eighteen years" absent           %(span)s
  "seamless" absent                                %(seam)s
  "transfer automatically" absent                  %(auto)s
  promotion-in-every-industry claim absent         %(promo)s
  30%% and $2M+ absent                              %(m1)s / %(m2)s
  CISM stated only within the ceiling              %(cism)s

===============================================================================
6. QA - SLIDES AND DECKS
===============================================================================

  main slides in the deck                12          (required 12)
  reveal frames                          %(frames)-2d          duplicate sequential slides
  reveal map per slide                   2,2,3,2,2,1,2,2,3,3,1,1
  PowerPoint animations                  none - reveals are duplicate slides
  PDF pages                              12
  PDF page size                          13.333 x 7.5 in (true 16:9)
  slide canvas                           1920 x 1080
  images or stock photography            0 picture shapes in the deck
  rasterised text                        none - every word is live text
  live text shapes                       %(text)d
  employer logos                         none
  shapes beyond the slide canvas         none
  elements outside the design canvas     none
  reveal states differ only by addition  yes - no element moves between states
  final reveal state matches main slide  yes, all 12
  slide 12 end-screen zone kept clear    yes
  no opening title card                  confirmed
  every slide rendered and inspected     yes - 12 PNGs plus %(frames)d reveal frames
  phone legibility at 320 x 180          Video_8_Phone_Legibility_Sheet.png

Every phrase in Section 5 of the production package was searched for in the
rendered PPTX text: all present, none missing.

FLUSH EDGES, REPORTED SEPARATELY FROM TRUE OVERHANG

  shapes that EXCEED the canvas          0
  shapes FLUSH to the canvas edge        %(nflush)d
  main slides with a flush edge          %(fm)s
  reveal frames with a flush edge        %(fr)s
  maximum overhang measured              %(overhang)d EMU

The flush elements are the full-bleed navy bands on slides 2 and 8 and those
slides' second reveal states. Right edge equals the slide width exactly; bottom
edge equals the slide height exactly; overhang is zero, not a tolerance. This
is the same designed device used in Videos 6 and 7 and is not an overflow. The
distinction is reported on every build in out/qa.json.

===============================================================================
7. QA - SCRIPT IDENTITY AND CONTENT BOUNDARIES
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

  locked opening distinction present     %(open)s
  translation sentence present           %(trans)s
  three columns named in the script      %(cols)s
  title consistent across files          yes
  target keyword present in package      yes
  keyword phrase opens the description   yes
  tags - exact target keyword first      yes
  CTA name and URL consistent            yes - Capability Formation Field Kit,
                                         temidayoafonja.com/fieldkit
  thumbnail copy recorded in package     yes - YOUR EXPERIENCE STILL COUNTS
  competing offers in script or slides   none
  TubeBuddy or scores mentioned on air   no - production rationale only
  confidentiality boundary spoken        %(conf)s
  fabrication explicitly ruled out       %(fab)s
  promise of a tradeoff-free move        none
  promise that evidence produces
    promotion or recognition             none

===============================================================================
8. THUMBNAIL - NOT BUILT HERE
===============================================================================

Required copy: YOUR EXPERIENCE STILL COUNTS

No thumbnail was created, redesigned or substituted, and no placeholder was
produced. Temidayo will create the final thumbnail in Canva. Supply the export
and it will be included byte-identically with a recorded checksum.

Standards that apply: 1280 x 720 upload at exact 16:9; cream #F5F0E8, navy
#0F2346, gold #C9A84C; legible at 200 px wide. See
CAPABILITY_FORMATION_YOUTUBE_STANDARDS.md.

===============================================================================
9. WATCH-NEXT ROUTING
===============================================================================

Confirmed from the roadmap audit rather than from the brief alone: sequence
row 9 is "What to Do Before a Layoff Happens". That title is held here and in
the audit only. It is not produced - no video-9 package exists in this
repository - and it appears in no spoken or on-slide wording.

The routing rules are in section 1.3 above and in section 8 of the package
DOCX. Slide 12 and the spoken line both point at the Career Portability
playlist, so the end-screen element can be set either way at upload with no
re-render and no re-record.

===============================================================================
10. PUBLICATION GATES
===============================================================================

  - Resolve the career-span wording in section 1.
  - Supply the approved Canva thumbnail carrying YOUR EXPERIENCE STILL COUNTS.
  - Chapter timestamps in the package are planning estimates. Reset them from
    the finished export before publishing.
  - Confirm temidayoafonja.com/fieldkit is live before publishing.
  - Set the end-screen video element per the routing rules in section 1.3, and
    verify the chosen playlist opens signed out and holds at least one other
    public video.
  - Open both DOCX files once in Word or Google Docs and confirm pagination.
    The fixes are verified in the XML but were not rendered here; see 1.5.

===============================================================================
11. WHAT WAS NOT TOUCHED
===============================================================================

No Videos 1-7 deliverable, no website file, no product file and no shared
standards file was modified. Verified with git: the only changes in this pass
are new files under deliverables/video-8-slides/.
""" % dict(frames=q["reveal_slides"], text=q["text_shapes"],
           fm=fm, fr=fr, nflush=len(q["flush_to_canvas_edge"]),
           overhang=q["flush_edge_max_overhang_emu"],
           pp=r["package_paragraphs"], tp=r["teleprompter_paragraphs"],
           cp=r["clean_paragraphs"], wc=r["word_count"],
           ceq=str(r["clean_equals_package"]).lower(),
           teq=str(r["teleprompter_equals_package"]).lower(),
           cteq=str(r["clean_equals_teleprompter"]).lower(),
           span=str(r["career_span_uses_ledger_wording"]).lower(),
           seam=str(r["no_seamless_claim"]).lower(),
           auto=str(r["no_automatic_transfer_claim"]).lower(),
           promo=str(r["no_promotion_in_every_industry_claim"]).lower(),
           m1=str(r["no_retention_metric_in_script"]).lower(),
           m2=str(r["no_turnover_metric_in_script"]).lower(),
           cism=str(r["cism_stated_within_ceiling"]).lower(),
           open=str(r["opening_distinction_present"]).lower(),
           trans=str(r["translation_sentence_present"]).lower(),
           cols=str(r["three_columns_named"]).lower(),
           rows=ROWS,
           conf=str(r["confidentiality_boundary_spoken"]).lower(),
           fab=str(r["no_fabrication_permitted"]).lower())

out = os.path.join(ROOT, "Video_8_First_Pass_QA_README.txt")
open(out, "w").write(TXT)
print("wrote", os.path.basename(out), "-", len(TXT.splitlines()), "lines")
