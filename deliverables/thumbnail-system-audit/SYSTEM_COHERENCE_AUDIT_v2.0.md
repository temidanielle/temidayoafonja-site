# Three-Video Thumbnail System — Coherence Audit v2.0

Run after the compliant rebuild of Videos 1 and 2. All three thumbnails now exist
and are built only from verified real photographs.

**Thumbnails assessed**

| | Words | File |
|---|---|---|
| Video 1 | DON'T START FROM ZERO | `VIDEO_1_THUMBNAIL_OPTION_A_3840x2160.png` (recommended) |
| Video 2 | YOUR SKILLS ARE STALLING | `VIDEO_2_THUMBNAIL_FINAL_3840x2160.png` |
| Video 3 | WAIT BEFORE YOU QUIT | `VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png` (approved, unchanged) |

## Measured, not asserted

Every figure below was measured off the rendered masters.

### Headline scale

| | Widest line | Point size | Cap height | Share of canvas height | vs Video 3 |
|---|---|---|---|---|---|
| Video 1 A | START | 430 | 301 px | 13.9% | +10.7% |
| Video 2 | STALLING | 345 | 242 px | 11.2% | −11.0% |
| Video 3 A | BEFORE | 388 | 272 px | 12.6% | benchmark |

All three sit within ±11% of the Video 3 benchmark. Video 3 falls in the middle
of the range, which is what a benchmark should do.

This was not true on the first build. Video 2 initially broke as
YOUR / SKILLS ARE / STALLING, and the long middle line forced the cap height down
to 206 px — 24% under the benchmark. Re-breaking it to four short lines recovered
the scale. The problem was caught by measurement before the audit, not after.

### Palette coverage

| | Cream | Navy | Gold | Lighter blue |
|---|---|---|---|---|
| Video 1 A | 24.8% | 47.4% | 2.0% | — |
| Video 2 | 6.8% | 44.2% | 3.5% | 1.7% |
| Video 3 A | 46.3% | 8.4% | 0.8% | — |

Exact same hex values throughout: cream `#F5F0E8`, navy `#0F2346`, gold `#C9A84C`,
lighter blue `#2C588C` used only inside Video 2's cue. The proportions differ by
design; the brief explicitly does not require identical background colours.

Gold stays a restrained accent everywhere — never above 3.5% of the canvas.

### Contrast

| Pairing | Ratio |
|---|---|
| Cream headline on navy (Videos 1 and 2) | 13.72:1 |
| Navy headline on cream (Video 3) | 13.72:1 |
| Gold on navy | 6.81:1 |
| Gold on cream | 3.03:1 |

The two dominant pairings are identical at 13.72:1. Gold on cream is the weakest
at 3.03:1 and appears only on the word ZERO in Video 1 Option B, at very large
size, where it clears comfortably.

### Portrait dominance

| | Portrait region | Share of canvas |
|---|---|---|
| Video 1 A | 1680 x 2160 | 43.8% |
| Video 2 | 1700 x 2160 | 44.3% |
| Video 3 A | 1800 x 2160 | 46.9% |

Within 3 percentage points across all three.

## Audit table

| Attribute | Video 1 | Video 2 | Video 3 | Consistent? | Action needed |
|---|---|---|---|---|---|
| Typeface | Montserrat ExtraBold | Montserrat ExtraBold | Montserrat ExtraBold | **YES** | None |
| Headline scale | cap 301 px | cap 242 px | cap 272 px | **YES** | None. Within ±11% |
| Headline contrast | 13.72:1 | 13.72:1 | 13.72:1 | **YES** | None |
| Palette hex values | identical set | identical set | identical set | **YES** | None |
| Palette proportion | navy-led | navy-led | cream-led | **MOSTLY** | None. Variation is intended |
| Gold restraint | 2.0% | 3.5% | 0.8% | **YES** | None |
| Portrait dominance | 43.8% | 44.3% | 46.9% | **YES** | None |
| Real photographs only | passes | passes | passes | **YES** | None |
| Face recognisable at 200 px | passes | passes | passes | **YES** | None |
| One dominant message | passes | passes | passes | **YES** | None |
| One supporting idea | accumulation rail | paused progression | three-check underscore | **YES** | None |
| Small copy present | none | none | none | **YES** | None |
| Layout | portrait right, navy left | portrait left, navy right | portrait right, cream left | **MOSTLY** | None. Deliberate variety |
| Geometry | 3840 x 2160, exact 16:9 | 3840 x 2160, exact 16:9 | 3840 x 2160, exact 16:9 | **YES** | None |
| Upload file under 2 MB | 190 KB | 211 KB | 196 KB | **YES** | None |

No material inconsistency was found. Nothing in the list of examples the brief
called material applies: same font family throughout, no significantly smaller
text, none looks like a corporate slide, portrait treatment is consistent, all
three are legible at 200 px, none carries supporting clutter, and all three sit
inside the Capability Formation palette.

## Channel recognition

Placed beside unrelated videos in a feed, would a viewer read these three as one
creator?

**Yes.** The grammar is carried by five things that hold across all three:

1. One typeface at one weight, at comparable size, always set flush left in short
   stacked lines.
2. One palette with identical hex values, and gold always as accent, never as a
   field.
3. One real portrait, dominant, occupying 44 to 47% of the canvas, always with a
   direct or near-direct gaze.
4. A single hard vertical seam between portrait and copy, marked by the same gold
   rule at the same weight.
5. One supporting graphic idea per thumbnail, always restrained, never labelled,
   never numeric.

What varies is which side the portrait sits on and whether the field is cream-led
or navy-led. That variety is what stops three videos in one feed reading as a
template. The dark-mode feed simulation shows the alternation working:
navy-left / portrait-left / cream-left down the column.

One genuine observation from dark mode: Video 3's cream field holds a hard edge
against the dark interface, while Videos 1 and 2 sit navy-against-near-black and
separate less sharply. This is visible but not material — both still read cleanly,
and the portrait provides the edge in each case.

## Verdict

**SYSTEM READY.**

All three are sufficiently cohesive. No changes recommended.

One decision remains yours, and it is a selection, not a correction: **Video 1
Option A or Option B.** Option A is recommended — the higher cap height, the
cleaner separation between headline and graphic, and the stronger reading at
200 px. Option B is built, exported and ready if you prefer the ledger treatment.
The contact sheet and dark-mode feed above use Option A.

Awaiting approval. No further changes made.
