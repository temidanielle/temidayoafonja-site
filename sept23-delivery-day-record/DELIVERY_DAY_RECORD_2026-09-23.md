# Delivery-day record — Wednesday, September 23, 2026

Stay or Leave? Live Career Growth Assessment · 60 minutes · 6:00 PM CT

This folder records three changes made to the **presenting copy** on delivery
day. It is not a new version of the September 23 package and it does not reopen
the freeze. The frozen CANDIDATE family in `sept23-v208-assets/` was not edited,
renamed or rebuilt, and the workbook PDF was read only.

## Freeze held

| Artifact | sha256 | State |
| --- | --- | --- |
| `sept23-v208-assets/PRESENTER_VERSION_..._v2.0.7_CANDIDATE.pptx` | `b9e1e5fbb302ec046116ec72b002aff37d84ff99eb5dc47a1707c761d3398f6b` | unchanged |
| `free-flagship-assets/60min-v2.0.1/Capability_Position_Read_Workbook_60MIN_v2.0.1_CANDIDATE.pdf` | `2bd2912846a679837e8e6bfb4aadff2bb07ee5959d35502ca1c5b5c728efa3ee` | unchanged, read only |

The workbook's Acrobat behaviour-test status therefore remains valid. Its 68 form
fields were never touched.

## What is in this folder

| File | What it is |
| --- | --- |
| `INPUT_GoogleSlides_export_2026-09-23.pptx` | The owner's presenting copy as exported from Google Slides on delivery day. This is the input the two scripts run against. `sha256 61e6fb943c349a6e23a0aaf36b20c91bd5560ad61dfb1c67e6e4b24dc32fdca5` |
| `PRESENTER_VERSION_..._v2.0.7_CANDIDATE_s12-numbered_s20-reordered.pptx` | **The delivered presenting copy**, all four changes applied. `sha256 30887393ccb7da96bb0018cb899b5bc75bde89344261958f6d413cd6fd7c15c9` |
| `PRESENTER_VERSION_..._v2.0.7_CANDIDATE_s12-clarifier_s20-reordered.pptx` | The same copy before the squares were numbered, kept as the step it was built from. `sha256 4e2131ecf95f6d717db18295995b2c810cbfaf6644abc2bfc1542817026c5247` |
| `PREVIEW_Presenting_Copy_2026-09-23_LibreOffice.pdf` | 26-page render of the above |
| `SOURCE_add_s12_clarifier.py` | Change 1 |
| `SOURCE_fix_s20.py` | Changes 2 and 3 |
| `SOURCE_add_s12_numbers.py` | Change 4 |
| `RUN_SHEET_Sept23_2026_60MIN_onepage.pdf`, `SOURCE_build_run_sheet.py` | One-page facilitator run sheet: timings, slide numbers and workbook pages, read from the delivered copy's own speaker notes |
| `RENDER_slide12_clarifier.png`, `RENDER_slide20_reordered.png` | The two changed slides as rendered |

## The three changes

### 1. Slide 12 — Fragile / Stagnant clarifier

Two lines added, one inside each bottom square of the matrix, beneath the
descriptor already there:

- STAGNANT square: `Neither axis is moving.`
- FRAGILE square: `What you built travels. It is just not being added to.`

**Why.** The word "Fragile" sounds worse than "Stagnant" to a room hearing them
for the first time, even though Stagnant is the double-low square. Slide 20
already states it as "Neither axis is accruing." The clarifier corrects the
mis-cue at the moment it happens.

**Why inside the squares rather than under the grid.** The only free space below
the grid is the 0.24in between the Optionality axis caption and the footer, which
will not hold two lines without moving the caption or the footer. The bottom
panels had 0.5in of unused space, so nothing moved.

**Why no `FRAGILE:` / `STAGNANT:` prefix.** Each line sits directly under the
label it belongs to, inside the same square, so the prefix is carried visually.

Styling is cloned from the descriptor above each line, inheriting DM Sans and
`5A6B84`, stepped down from 11pt to 9.5pt so it reads as secondary furniture and
not as a second descriptor.

### 2. Duplicate State Costs slide deleted

The presenting copy carried `What each state costs` twice, at positions 20 and
21, identical in face and in speaker note. The duplicate exists only in the
Google Slides copy; the frozen artifact has the slide once. Position 21 was
removed and the deck is back to 33 slides.

The page numbers on this deck are hardcoded text written for a 33-slide deck, so
removing the duplicate **realigned** them rather than breaking them: Move
Categories already carried the number 21 while sitting in position 22.

### 3. Slide 20 reordered to climb

| Order | State | Cost line (unchanged) |
| --- | --- | --- |
| 1 | STAGNANT | Neither axis is accruing. |
| 2 | DEPTH TRAP | Value is deep but context-bound. |
| 3 | FRAGILE | What travels today is no longer being renewed. |
| 4 | COMPOUNDING | A strong current position still requires renewal. |

Previously the rows read the matrix left to right: Depth Trap, Compounding,
Stagnant, Fragile. The new order is the owner's own reading of the axes, lowest
to highest: nothing accruing in either direction, then something real being built
that does not travel, then something that travels with nothing being added under
it, then both axes high.

**Chip colour changed with it.** The chips used to alternate navy, light, navy,
light, which was positional striping with no meaning. Reordered under that
stripe, Stagnant would have taken the boldest treatment, the opposite of what the
sequence says. The first three rows now take the light panel and COMPOUNDING
alone takes the navy panel with the gold label, which is the same relationship
slide 12 holds, where Compounding is the one inverted square.

**Checked before reordering.** Workbook page 3 carries the placement tick list and
page 7 carries the 2x2 grid, but neither carries a state-costs sequence, so
nothing in participants' hands contradicts the new order.

**Speaker note left alone.** It reads "one pass, four states, no favourites" and
prohibits deepening the heaviest square for the room. Ordering the four is not
favouring one, so the note still holds.

### 4. Slide 12 — the four squares numbered

The square labels now read `1  STAGNANT`, `2  DEPTH TRAP`, `3  FRAGILE`,
`4  COMPOUNDING`, in the same order slide 20 runs in, so the two slides agree and
the climb is visible to the room rather than living only in the presenter's head.

Each numeral is its own run in front of the existing label run, so every label
keeps its exact font, size, weight and colour and nothing on the slide moves. No
new shapes.

The numeral takes the panel's secondary accent so it reads as an order marker and
not as part of the state's name: gold `C9A84C` on the three light panels, where
the label is navy, and `B8C5D9` on the navy panel, where the label is gold and
that tone is already in use for the panel's own text.

**Open conflict, deliberately left standing.** Slide 12's speaker note says the
matrix is "not a ranking, and not a square to aim for." Visible numerals assert
an order. The owner's own ranking text is already pasted into that note in the
presenting copy, so the conflict predates this change and was accepted knowingly.
The note was not edited. At promotion, either the note or the numerals should
move, not both stay as they are.

## Narrowness, as asserted by the scripts

Both scripts fail rather than save if any of this is untrue, and both passed:

- Change 1: exactly one face changed (slide 12); no speaker note changed on any
  slide; every pre-existing shape on slide 12 holds its exact position, size and
  text; slide 12 gained nothing but the two strings.
- Changes 2 and 3: exactly one slide changed content (20) once the deletion shift
  is accounted for; no speaker note changed anywhere; every shape on slide 20
  holds its exact geometry; the slide 12 clarifier survived.

## Open item for the CANDIDATE to FINAL promotion

The presenting copy and the frozen artifact now differ in four ways, all
recorded above. At promotion, decide each one deliberately:

1. **Slide 12 clarifier** — carry into the FINAL deck, or keep it as a spoken
   line only. If carried, note that the workbook's page 7 grid does not have it,
   so the two artifacts would say slightly different things about the same
   squares.
2. **Slide 20 reorder and chip colour** — carry into the FINAL deck or revert.
3. **The duplicate** — a defect of the Google Slides copy only. Nothing to carry.
4. **Slide 12's numerals** — carry into the FINAL deck or revert, and settle the
   "not a ranking" wording in the speaker note either way. Note that workbook
   page 7 carries the same grid unnumbered, so if the numerals are carried, the
   workbook and the deck would differ on the same four squares.

Still deferred and **not** to be addressed as part of promotion: the review of
Optionality statements 7, 10 and 12, and the "Fragile" label connotation.
