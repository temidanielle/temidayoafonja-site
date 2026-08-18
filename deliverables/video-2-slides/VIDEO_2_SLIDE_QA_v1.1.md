# Video 2 slide deck: copy refinement record and QA

**Version 1.1**
**Revised Tuesday, August 18, 2026 at 3:32 PM CT**

Build timezone: America/Chicago (CDT, UTC-05:00).

Deck: **Is Your Job Making You Less Marketable?**
Revision type: one copy refinement on slide 2. Nothing else was changed. No
slide was redesigned, no reveal build, timing, layout, CTA, end screen, visual
system or asset was altered. Version 1.0 and the Video 1 decks remain untouched.

---

## 1. The change

Slide 2 only. Two text blocks.

**Headline**

- Before: "Success answers one of them at a time."
- After: "Being valuable here answers only one question."

**Supporting line**

- Before: "Current success can answer one question while leaving the other unresolved."
- After: "The second question is whether another context can recognize and use what you have built."

Both blocks keep the same typography, size, weight, colour, position, box width
and line count as version 1.0. The headline is still 54 px bold navy on two
lines in the headline zone. The supporting line is still 32 px body weight in
the muted navy on two lines beneath the rule.

**Preserved exactly, and verified pixel by pixel:** the kicker
"TWO DIFFERENT QUESTIONS", the two phrases "Valuable here" and
"Legible elsewhere", the gold vertical divider between them, the horizontal
hairline, and all whitespace and composition.

### Speaker note

One sentence was added to slide 2's notes, because the slide now points at "the
second question" and the presenter should name it aloud:

> Name the second question out loud, since the slide now points at it: whether
> another context can recognize and use what you have built.

The rest of slide 2's notes, including the recognition beats and the exact
landing line "Praise can tell you that you matter here. It cannot tell you how
easily your value travels.", is unchanged. No other slide's notes were touched.

---

## 2. QA results

Raw output: `out/v1.1/qa-raw-v1.1.json`.

### The change itself

| # | Check | Result |
|---|---|---|
| 1 | New headline present | Pass. |
| 2 | New supporting line present | Pass. |
| 3 | Old copy gone | Pass. Neither "Success answers one of them at a time." nor "leaving the other unresolved" appears anywhere in the deck. |
| 4 | Slide 2 frame preserved | Pass. Kicker and both phrases still present and unmoved. |
| 5 | Only slide 2 changed | Pass. Twelve of the thirteen rendered slides are pixel-identical to version 1.0. |
| 6 | Within slide 2, only the two intended blocks changed | Pass. Region by region against version 1.0: kicker 0 pixels changed, the two phrases and the gold divider 0, the hairline 0, everything below the supporting line 0. Only the headline band and the supporting-line band differ. |
| 7 | Only the matching recording frame changed | Pass. One of 23 frames differs, frame 02, which is slide 2. The other 22 are pixel-identical. |

### Everything else still holds

| # | Check | Result |
|---|---|---|
| 8 | 13 main slides, 13 PDF pages | Pass, at 13.333 x 7.5 in. |
| 9 | Recording deck | Pass. 23 slides, same running order. |
| 10 | Three standalone test intros at separate moments | Pass. Slides 3, 5 and 7. |
| 11 | All three tests appear together only on the recap | Pass. Slide 9 only. |
| 12 | Section breaks and recap carry no builds | Pass. |
| 13 | No reveal frame removes a permanent element | Pass. 0 removals across all 23 frames. |
| 14 | Last build of each slide equals the main slide | Pass, content-identical for all 13. |
| 15 | Camera safe areas preserved | Pass. 0 hits in the main deck and across all 23 recording frames. |
| 16 | End-screen reserve preserved | Pass on slide 13. |
| 17 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. |
| 18 | Field Kit route | Pass. `temidayoafonja.com/fieldkit`, slide 12 only. |
| 19 | Timings unchanged | Pass. Contiguous 0:00 to 9:00, identical to version 1.0. |
| 20 | Voice standard | Pass. 0 em dash and 0 en dash characters. |
| 21 | Version 1.0 and Video 1 untouched | Pass. All prior files byte-identical. Version 1.1 writes only `*_v1.1` files and `out/v1.1/`. |

### Overflow-check note

Zero geometry warnings on either deck. The new headline uses two deliberate
lines and the new supporting line uses two, both as intended, with no wrapping
beyond that. Backgrounds are drawn at exactly 1920 x 1080 with no bleed.

---

## 3. Output paths

All paths relative to `deliverables/video-2-slides/`.

**Version 1.1 deliverables**

- `out/Video-2-Is-Your-Job-Making-You-Less-Marketable_v1.1.pptx`
- `out/Video-2-Reveal-Builds_v1.1.pptx`
- `out/Video-2-Is-Your-Job-Making-You-Less-Marketable_v1.1.pdf`
- `VIDEO_2_SLIDE_QA_v1.1.md` (this file)

**Supporting version 1.1 output**

- `out/v1.1/png/slide-01 ... slide-13` at 1920 x 1080
- `out/v1.1/reveals/frame-01 ... frame-23`
- `out/v1.1/Video-2-Reveal-Builds_v1.1.pdf`
- `out/v1.1/contact-sheet-v1.1.png`
- `out/v1.1/recording-deck-order-v1.1.png`
- `out/v1.1/phone-thumbnail-check-v1.1.png`
- `out/v1.1/guides/`, `out/v1.1/qa-raw-v1.1.json`

**Source**

- `build/slides_v1_1.py`, copied from `slides.py` with the two lines changed
- `build/build_v1_1.py`, build and QA pass
- `build/deck.py`, shared primitives, unchanged

Rebuild with `python3 build/build_v1_1.py` from `deliverables/video-2-slides/`.

**Archive, untouched**

Version 1.0: `out/Video-2-...-_v1.0.pptx`, `out/Video-2-...-_v1.0.pdf`,
`out/Video-2-Reveal-Builds_v1.0.pptx`, `out/png/`, `out/reveals/`,
`out/guides/`, the version 1.0 sheets and `VIDEO_2_SLIDE_QA_v1.0.md`.
