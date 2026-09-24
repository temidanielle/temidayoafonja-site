# Signals Worth Watching — change log

Built 24 September 2026. Three new slides, one new workbook line, one re-cut
timeline, one spec for a deck that does not exist yet.

## What was updated, and what it is called now

| Deck or file | Version | State |
| --- | --- | --- |
| `PRESENTER_VERSION_Stay_or_Leave_..._60MIN_v2.0.8_CANDIDATE_signals.pptx` | **v2.0.8** | built, 43 slides, `sha256 372402b8906b076ed872aaf34928c0188a0be31dd461c00aa088b8d8a7aad5e6` |
| `Capability_Position_Read_Workbook_60MIN_v2.0.2_CANDIDATE.pdf` | **v2.0.2** | built, 8 pages, 70 fields, `sha256 f73c2830390e6681b385ceca53e2d4e7bde31eea01db15883084c821f27044f3` |
| Retention Read, standard and educator | not versioned | **not built: the deck does not exist.** Spec written instead |
| Transition Read | not versioned | **deliberately excluded**, and the exclusion is recorded in the spec |
| September 9 Lightning Lesson v3.5.1 FINAL | unchanged | not in scope, not opened, not modified |

Source scripts ship beside the artifacts: `SOURCE_build_deck_v208.py` and
`Capability_Position_Read_Workbook_60MIN_v2.0.2_SOURCE.py`. Both assert their own
correctness and fail rather than save.

## Base deck

The base is the file uploaded as
`USE_FINAL_PRESENTER_VERSION_..._v2.0.7_CANDIDATE_s12-clarifier_s20-reordered.pptx`,
kept here as `INPUT_USE_FINAL_v2.0.7_working_copy.pptx`,
`sha256 d1e60b388ecd3c30d01bba55180a6fc01221251c208e963a0ee262d4535c7ab5`. It is the
owner's own working copy, 40 slides, with a welcome slide and section dividers the
repository copy does not have. Its numbering is the numbering the brief cites:
slide 33 is the Position Exposure Signals appendix, slide 24 is State Costs.

It does **not** contain two changes made on 23 September: the numerals on the four
states and the seven-categories tease on the boundary slide. Those live in
`sept23-delivery-day-record/`. They were not merged in, because merging them would
have meant changing slides this brief did not name.

## 1. The three new slides

Inserted after State Costs and before Seven Categories of Move, as slides 25, 26
and 27, carrying footer numbers 22, 23 and 24.

Each is cloned from Seven Categories of Move, so the eyebrow, title, subtitle,
numbered navy chips, body text, rust footer line and page number all inherit the
deck's own styling rather than being drawn with guessed values. The section opener
borrows its pale panel and gold accent from the Next-Move Note slide, which is
where that treatment already lives.

Content comes from the existing appendix slide 33, Position Exposure Signals, and
from the State Costs line "a strong current position still requires renewal",
promoted into the recorded core and expanded. No new framework term is introduced.

**Boundary.** Every signal is phrased as something to examine. There are no
forecasts, no statistics, and no claim about the job market or about any employer.
The speaker notes say twice, in different words, that noticing a signal is a reason
to gather evidence and never a reason to panic or to leave.

## 2. The Next-Move Note

Both the slide and workbook page 8 gain one line under WHAT HAPPENS NEXT:

> Two signals I will watch before my rescore date: ______ and ______

On the slide, the three prompt blocks tighten by a tenth of an inch each so the
line fits inside the WHAT HAPPENS NEXT block rather than floating between
sections, and the closing navy band moves down by the same tenth.

In the workbook the block grows from 64pt to 86pt and the line carries two real
form fields, `signal_1` and `signal_2`.

## 3. Timing, and what was trimmed

**The brief asked for about two minutes per new slide. Six minutes do not exist in
this session.** The trims the brief authorises yield two minutes, and one more
comes from the close buffer:

| Block | Was | Now | Change |
| --- | --- | --- | --- |
| Calibration, three ways a self-score goes wrong | 16:00-19:00 | 16:00-18:00 | minus 1:00 |
| Re-total before you place again | 31:00-32:30 | 30:00-31:00 | minus 0:30 |
| When the evidence remains uncertain | 32:30-34:00 | 31:00-32:00 | minus 0:30 |
| Close buffer | 2:00 long | 1:00 long | minus 1:00 |

That is three minutes, so **the section runs at sixty seconds a slide, not two
minutes.** Reaching six would mean taking three minutes from the protected
twelve-minute evidence block or from Q&A, and this build does neither.

Each new slide's speaker note still carries about two minutes of material, as
asked. Each note states which part is the sixty-second live read and which part is
there for the replay and for questions.

**The twelve-minute evidence block is shifted, never shortened.** It moves from
19:00-31:00 to 18:00-30:00 and keeps all twelve minutes. Its internal cues move
with it: the midpoint cue from 25:00 to 24:00, the two-minute warning from 29:00 to
28:00, the thirty-second warning from 30:30 to 29:30.

Q&A still starts at 50:00 and the session still ends at 60:00.

The re-cut timeline, from the first block that moved:

| Slide | Block | New window |
| --- | --- | --- |
| 18 | Calibration | 16:00-18:00 |
| 19 | Score all twelve again, PROTECTED | 18:00-30:00 |
| 20 | Re-total | 30:00-31:00 |
| 21 | Evidence still uncertain | 31:00-32:00 |
| 22 | Your corrected position | 32:00-33:00 |
| 24 | What each state costs | 33:00-36:00 |
| **25** | **Signals Worth Watching** | **36:00-37:00** |
| **26** | **Signals around your role** | **37:00-38:00** |
| **27** | **Signals when things feel fine** | **38:00-39:00** |
| 28 | Seven categories of move | 39:00-42:00 |
| 29 | The Next-Move Note | 42:00-46:00 |
| 30 | Choose how to continue | 46:00-47:00 |
| 31 | Keep working privately | 47:00-48:00 |
| 32 | Before you go, close and buffer | 48:00-50:00 |
| 35 | Questions and Applications | 50:00-60:00 |

The workbook's pacing cues were re-cut to match, which is a cross-reference fix
rather than an editorial one: a workbook that puts a participant on page 7 at
minute 31 while the deck is there at minute 30 is simply wrong.

| Workbook page | Was | Now |
| --- | --- | --- |
| 2 and 3 | minutes 5-9, 9-14 | unchanged, nothing before minute 16 moved |
| 4 | minutes 14-19 | minutes 14-18 |
| 5 and 6 | minutes 19-31 | minutes 18-30 |
| 7 | minutes 31-35 | minutes 30-33 |
| 8 | minutes 41-45 | minutes 42-46 |

## 4. Footer numbers

Page numbers on this deck are static text, so inserting three slides required
renumbering. The new slides take 22, 23 and 24, and the five later numbered slides
move up by three: Seven Categories 22 to 25, Next-Move Note 23 to 26, continuation
24 to 27, keep working privately 25 to 28, Questions and Applications 26 to 29.

## Verification

The deck build asserts and passed:

- 40 slides in, 43 out, with the three new slides at positions 25, 26 and 27,
  State Costs immediately before and Seven Categories immediately after.
- Every pre-existing slide maps one to one onto its counterpart, and the only ones
  whose face or note changed are the thirteen this log accounts for: 15, 18, 19,
  20, 21, 22, 24, 25, 26, 27, 28, 29 and 32.
- The protected block still reads TWELVE MINUTES, PROTECTED AND NON-NEGOTIABLE.
- Q&A still reads 50:00-60:00.
- All ten signals appear on the faces, once each, and the workbook line is on the
  Next-Move Note slide.
- No em dash appears anywhere in the new slides, their notes, or the Next-Move
  Note edit.

The workbook build was verified against the shipped v2.0.1 twice:

- **Fidelity first.** v2.0.1 was rebuilt from its own source and compared to the
  distributed PDF: zero text-position differences across all eight pages, and all
  68 fields identical in name, type and rectangle. The original TTFs did not
  survive in the repository, so static instances were cut from the upstream
  variable fonts; this test is what proves those instances are the right ones.
- **Then the change.** v2.0.2 against v2.0.1: pages 1 to 3 identical, pages 4 to 7
  differing only in the pacing cue, page 8 gaining exactly one new text block.
  Fields 68 to 70, the two new ones being `signal_1` and `signal_2`, nothing lost,
  and the only pre-existing field to move is `rescore_date`, 22pt down, because it
  sits below the grown block.

## Open items

**1. The workbook needs a fresh Acrobat behaviour test.** v2.0.1's test status does
not transfer to v2.0.2. The field-behaviour pass ran and reattached the same
counts it always did, 32 alignments, 14 keystroke rules, 12 keystroke-with-question-mark
rules and 4 calculations, but that is the builder reporting on itself, not a test.
`free-flagship-assets/60min-v2.0.1/` is untouched and still holds the tested file,
`sha256 2bd2912846a679837e8e6bfb4aadff2bb07ee5959d35502ca1c5b5c728efa3ee`.

**2. Em dashes already in the deck.** The check asked for none anywhere. This build
introduced none. It also did not remove the 43 that were already there, across 24
slides, 5 of them on visible faces: slides 10, 18, 19, 35 and 36 of the base deck.
Removing them is an editorial pass on slides this brief did not name, because each
one needs a judgment about what replaces it. Say the word and it is a separate,
small job.

**3. Three timing faults in the base deck, which predate this work.**

- The welcome slide, "Why I Built This Lesson", claims 1:00-3:00, which overlaps
  the reframe, the boundary slide and the first definition. It was inserted without
  re-timing anything around it.
- The appendix slide "What moved when you tested your first read" is now visible
  and sits between Your Corrected Position and What Each State Costs, inside the
  timed core, carrying no timing at all. Every number in the table above assumes it
  takes zero time.
- The two section dividers, Definitions and Matrix, carry speaker notes copied from
  the closing slide and claim 47:00-50:00.

None of these were touched. Fixing them means deciding what the welcome slide is
worth and whether the appendix slide belongs in the core, and those are decisions,
not corrections.

**4. The SOP and QA report still describe the old timeline.**
`sept23-v208-assets/` holds SOP v2.0.10 with a reconciliation table built on
19:00-31:00 and a 35:00 state-costs block. Neither was updated, because the frozen
package was not opened. They will need a pass before v2.0.8 is delivered.
