# Video 1 slide deck: structural correction record and QA

**Version 2.4**
**Revised Tuesday, August 18, 2026 at 12:00 PM CT**

Build timezone: America/Chicago (CDT, UTC-05:00).

Deck: **How I Changed Jobs Without Starting My Career Over**
Revision type: targeted structural correction of the three ideas. Ten slides
become thirteen. No unrelated slide was redesigned. Version 2.3 and every
earlier version remain untouched, and no website, product or other asset was
modified.

---

## 1. What was wrong, and what changed

In version 2.3 the three ideas were reveal states of one three-card overview
slide. That meant idea one stayed on screen while idea two arrived, and both
stayed while idea three arrived. The viewer never got a clean moment with a
single idea, and the overview ran before any of them had been taught.

Version 2.4 makes them three standalone section-break slides at three separate
moments, and turns the old three-card composition into a recap that runs once,
after Move Three, when the viewer has learned all three.

| Position | Slide | Status |
|---|---|---|
| 1 | Title | Carried over unchanged |
| 2 | Career path | Carried over unchanged |
| 3 | **Section break 01, Look underneath the title** | **New** |
| 4 | Move one | Carried over unchanged |
| 5 | **Section break 02, Explain what the work changed** | **New** |
| 6 | Move two, translation | Carried over unchanged |
| 7 | Move two evidence, 47 to 75 | Carried over unchanged |
| 8 | **Section break 03, Keep evidence before you need it** | **New** |
| 9 | Move three, evidence record | Carried over unchanged |
| 10 | **Recap, all three together** | **Repurposed from the old slide 3** |
| 11 | Before your next move | Carried over unchanged |
| 12 | Field Kit invitation | Carried over unchanged |
| 13 | Watch next | Carried over unchanged |

The recap reuses the approved three-card composition. Its headline changes from
"These helped me carry my experience forward." to "What helped me carry my
experience forward.", and its cards no longer build; all three are present the
moment the slide appears.

### The section-break design

One dominant gold numeral, one dominant statement, one small supporting line,
and air. No cards, no icons, no diagrams, no rules, no framework language.

| Slide | Number | Statement | Supporting line |
|---|---|---|---|
| 3 | 01 | Look underneath the title | What has the work actually trained you to do? |
| 5 | 02 | Explain what the work changed | What changed because you were there? |
| 8 | 03 | Keep evidence before you need it | Capture the context, your role and what changed. |

Cream ground, gold numeral, navy statement, muted supporting line, all from the
approved system. The whole block sits below and left, clear of the presenter
camera area, so the upper right stays empty.

One typographic decision worth naming: the statements are set in sentence case,
not the capitals used in the brief. Every large headline in this deck is
sentence case and capitals are reserved for kickers, so capitals here would have
read as a different system. Say the word if you want them capitalised; it is a
one-line change.

---

## 2. Timing

Total unchanged at approximately nine minutes. The three breaks take eight
seconds each, taken from the teaching blocks around them rather than added to
the runtime.

| Slide | Span | Length |
|---|---|---|
| 1 Title | 0:00-0:35 | 0:35 |
| 2 Career path | 0:35-1:35 | 1:00 |
| 3 Section break 01 | 1:35-1:43 | 0:08 |
| 4 Move one | 1:43-3:05 | 1:22 |
| 5 Section break 02 | 3:05-3:13 | 0:08 |
| 6 Move two | 3:13-4:05 | 0:52 |
| 7 Evidence, 47 to 75 | 4:05-4:50 | 0:45 |
| 8 Section break 03 | 4:50-4:58 | 0:08 |
| 9 Move three | 4:58-6:25 | 1:27 |
| 10 Recap | 6:25-6:40 | 0:15 |
| 11 Before your next move | 6:40-7:45 | 1:05 |
| 12 Field Kit | 7:45-8:20 | 0:35 |
| 13 Watch next | 8:20-9:00 | 0:40 |

Contiguous 0:00 to 9:00, no gaps or overlaps.

---

## 3. Reveal builds

The recording deck is **22 frames**. Reveals are kept only where they teach:

| Slide | Frames | Build |
|---|---|---|
| 4 Move one | 3 | One question at a time |
| 6 Move two | 2 | Internal description, then what another employer can understand |
| 7 Evidence | 2 | 47, then 75 |
| 9 Move three | 4 | One evidence row at a time |
| 11 Before your next move | 3 | One question at a time |

Slides 3, 5, 8 and 10 have **no builds**, verified in the build. Each section
break is a single frame that appears once and leaves.

---

## 4. QA results

Raw output: `out/v2.4/qa-raw-v2.4.json` and `out/v2.4/qa-raw-main-v2.4.json`.

### Required confirmations

| # | Confirmation | Result |
|---|---|---|
| 1 | 01, 02 and 03 are separate slides in separate positions | **Pass.** Slides 3, 5 and 8, with Move One, Move Two and the result slide between them. |
| 2 | No section-break slide contains another section's idea | **Pass.** Asserted in the build. Slide 3 carries "Look underneath the title" and neither of the others. Slide 5 carries "Explain what the work changed" and neither of the others. Slide 8 carries "Keep evidence before you need it" and neither of the others. |
| 3 | All three appear together only on the recap | **Pass.** A scan of all thirteen slides for all three statements returns exactly one slide: 10. |
| 4 | Recap appears after Move Three | **Pass.** Move three is slide 9, the recap is slide 10. |
| 5 | Move One, Move Two, 47 to 75, Move Three, viewer questions, Field Kit and Watch Next remain intact | **Pass.** Verified two ways: text assertions on each slide, and a pixel comparison of every carried-over slide against its version 2.3 render. Seven of the nine are pixel-identical. Two differ only by rasteriser antialiasing: the 47 to 75 slide by 604 pixels of 2,073,600 in the numeral area, and the Field Kit slide by 124 pixels in the rotated product image. No content difference on either. |
| 6 | Version 2.3 and earlier remain untouched | **Pass.** All prior files byte-identical. Version 2.4 writes only `*_v2.4` files and `out/v2.4/`. |
| 7 | No unrelated files changed | **Pass.** The working tree contains only new files under `deliverables/video-1-slides/`. No website file was read into the build or edited. |

### Standard checks

| # | Check | Result |
|---|---|---|
| 8 | Main deck slide count | Pass. 13 slides, 13 PDF pages at 13.333 x 7.5 in. |
| 9 | Recording deck | Pass. 22 slides in running order. |
| 10 | No reveal frame removes a permanent element | Pass. 0 removals across all 22 frames. |
| 11 | Last build of each slide equals the main slide | Pass, content-identical for all 13. |
| 12 | Section-break slides carry no builds | Pass. Slides 3, 5, 8 and 10 are one frame each. |
| 13 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. |
| 14 | Camera safe areas preserved | Pass. 0 text elements in the 620 x 440 upper-left keep-clear zone, in the main deck and across all 22 recording frames. |
| 15 | End-screen reserve preserved | Pass. 0 elements intrude on x 1130 to 1860, y 190 to 890 on slide 13. |
| 16 | Recap headline updated | Pass. "What helped me carry my experience forward." |
| 17 | Field Kit URL | Pass. `temidayoafonja.com/fieldkit`, on slide 12 only. |
| 18 | Voice standard | Pass. 0 em dash and 0 en dash characters. No framework, model, method or step language. No new teaching concepts. |
| 19 | Timings total about nine minutes | Pass. Contiguous 0:00 to 9:00. |
| 20 | Recap differs from the old slide 3 only in its headline | Pass. Pixel comparison shows a single difference region, x 660 to 1306, y 191 to 243, which is the first headline line. The cards and everything else are unmoved. |

### Overflow-check note

Zero geometry warnings on either deck. Backgrounds are drawn at exactly
1920 x 1080 with no bleed. All audience-facing content is inside the canvas.

---

## 5. Output paths

All paths relative to `deliverables/video-1-slides/`.

**Version 2.4 deliverables**

- `out/Video-1-Reveal-Builds_v2.4.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.4.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.4.pdf`
- `VIDEO_1_SLIDE_QA_v2.4.md` (this file)

**Supporting version 2.4 output**

- `out/v2.4/png/slide-01 ... slide-13` at 1920 x 1080
- `out/v2.4/reveals/frame-01 ... frame-22` at 1920 x 1080
- `out/v2.4/Video-1-Reveal-Builds_v2.4.pdf`
- `out/v2.4/contact-sheet-v2.4.png`
- `out/v2.4/recording-deck-order-v2.4.png`
- `out/v2.4/guides/`, `out/v2.4/qa-raw-v2.4.json`, `out/v2.4/qa-raw-main-v2.4.json`

**Source**

- `build/slides_v2_4.py`, copied from `slides_v2_3.py` with the three section
  breaks added, the overview slide repurposed as the recap, the running order
  rebuilt and the timings redistributed
- `build/build_v2_4.py`, build and QA pass
- `build/deck.py`, shared primitives, unchanged since version 1

Rebuild with `python3 build/build_v2_4.py` from `deliverables/video-1-slides/`.

**Archive, untouched**

Versions 2.3, 2.2, 2.1, 2 and 1, with their QA records, decks, PDFs and frames.
