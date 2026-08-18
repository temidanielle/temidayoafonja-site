# Video 1 slide deck: revision record and QA

**Version 2.1**
**Revised Tuesday, August 18, 2026 at 7:57 AM CT**

Build timezone: America/Chicago (CDT, UTC-05:00). All times in this record are
Central Time.

Deck: **How I Changed Jobs Without Starting My Career Over**
Revision type: controlled correction pass on the approved version 2 deck. Two
copy corrections and one added recording deck. No redesign, repositioning,
restyling or reinterpretation. All 10 slides, layouts, typography, images,
timings, CTA order and speaker notes are otherwise unchanged. Version 2 and
version 1 files were not modified.

---

## 1. Corrections made in 2.1

### 1.1 Factual correction, slide 2 visible copy

Removed "workforce strategy" from the cybersecurity clause.

- Before: "I carried that way of seeing into cybersecurity workforce strategy and
  later into people strategy."
- After: "I carried that way of seeing into cybersecurity and later into people
  strategy."

The paragraph now reads, in full:

> Accounting and audit trained me to look for evidence, controls, risk and what a
> system was failing to reveal. I carried that way of seeing into cybersecurity and
> later into people strategy.

The career timeline and every other visible element on slide 2 are untouched. The
paragraph occupies the same block at the same position and still sets on three
lines; only the third line is shorter.

### 1.2 Ownership correction, slide 6 speaker notes

- Before: "after the redesign my team and I led"
- After: "after the onboarding redesign I led with my team"

The spoken passage now reads, in full:

> One measure of how well new hires felt integrated moved from 47 to 75 after the
> onboarding redesign I led with my team. The number becomes useful because I can
> explain what it measured, what changed and what I was responsible for.

Visible slide 6 wording is unchanged: kicker "ONE RESULT", headline "One measure
of new-hire integration", subtitle "A team result from a redesign I led", the
47 to 75 figure and the "Before the redesign" and "After the redesign" labels.

### 1.3 Recording deck added

The main deck carries no embedded animations, by design. The staged reveals its
notes call for are delivered as a separate recording deck built from sequential
duplicate slides, so they survive export, screen recording and import into any
other presentation tool. No PowerPoint animation objects are used anywhere.

**No other copy or design change was made.**

---

## 2. Recording deck

`Video-1-Reveal-Builds_v2.1.pptx`, **21 slides**, running in presentation order.
Slides with no reveal appear once; slides with reveals appear as consecutive
duplicates, each adding one element.

| Frame | Slide | State |
|---|---|---|
| 1 | 1 | Title |
| 2 | 2 | Career path |
| 3, 4, 5 | 3 | Card 01, then 01 and 02, then all three |
| 6, 7, 8 | 4 | Question 01, then 01 and 02, then all three |
| 9, 10 | 5 | Internal description alone, then arrow and portable description |
| 11, 12 | 6 | 47 and "Before the redesign", then arrow, 75 and "After the redesign" |
| 13, 14, 15, 16 | 7 | Situation, then My role, then What changed, then What this shows |
| 17, 18, 19 | 8 | Question 01, then 01 and 02, then all three |
| 20 | 9 | Field Kit invitation |
| 21 | 10 | Next-video bridge |

Verified sequences, all confirmed against the rendered frames and the PowerPoint
file itself:

- Slide 3 advances one card at a time. Pass.
- Slide 4 advances one question at a time. Pass.
- Slide 5 shows the internal description before the portable description. Pass.
- Slide 6 shows 47 before 75. Pass.
- Slide 7 advances one evidence row at a time. Pass.
- Slide 8 advances one question at a time. Pass.

Nothing is removed as the builds advance: across all 21 frames, **0 frames drop
any text present in the previous frame of the same slide**. Backgrounds, the gold
frame, the logomark, kickers, headlines, subtitles and the evidence-card frame
are drawn on every frame of their slide. The final build of each slide is
content-identical to the corresponding main-deck slide, verified by comparing the
full element description of both canvases. Renders of those pairs differ only by
rasteriser antialiasing, at most 1,338 pixels of 2,073,600 with a maximum channel
delta of 7, on slide 9's rotated product image.

Safe areas hold across the whole recording deck: **0 of 21 frames** place any text
in the 620 x 440 upper-left camera keep-clear zone, and **0 frames** intrude on the
reserved end-screen region on the slide 10 frame. 0 clipped elements.

Frame-by-frame proof sheet: `out/v2.1/recording-deck-order-v2.1.png`.

---

## 3. Unchanged from version 2

Confirmed still true after the correction pass.

| Item | Status |
|---|---|
| Slide count | 10 |
| Slide order and CTA position | Unchanged. Moves on 4, 5, 6 and 7, exercise on 8, Field Kit invitation on 9, bridge on 10 |
| Layouts, typography, palette, images | Unchanged |
| Speaker-note timings | Unchanged, contiguous 0:00 to 9:00 |
| Runtime estimate | Approximately 9 minutes 0 seconds |
| Presenter camera safe area | 480 x 270 at (72, 72), 620 x 440 keep-clear zone |
| End-screen reserve on slide 10 | x 1130 to 1860, y 190 to 890 |
| Photographs and product images | One authentic portrait on slide 2; actual Field Kit cover and actual page 6 on slide 9 |

---

## 4. QA results

Full version 2 suite re-run against the version 2.1 files, plus the new recording
deck checks. Raw output: `out/v2.1/qa-raw-v2.1.json` and
`out/v2.1/qa-raw-main-v2.1.json`.

| # | Check | Result |
|---|---|---|
| 1 | Slide 2 correction applied | Pass. New sentence present, "workforce strategy" absent. |
| 2 | Slide 6 notes correction applied | Pass. New wording present, "my team and I led" absent. |
| 3 | Slide 6 visible wording unchanged | Pass. Byte-identical to version 2. |
| 4 | Main deck is exactly 10 slides | Pass. 10. |
| 5 | PDF has 10 matching pages | Pass. 10 pages at 13.333 x 7.5 in. |
| 6 | Recording deck slide count and order | Pass. 21 slides in the sequence tabled above. |
| 7 | Recording deck advances correctly on slides 3, 4, 5, 6, 7, 8 | Pass, all six. |
| 8 | No reveal frame removes permanent elements | Pass. 0 removals across all frames. |
| 9 | Last build of each slide equals the main slide | Pass. Content-identical for all 10. |
| 10 | Both PowerPoint files rendered and inspected | Pass. 10 main frames and 21 recording frames rendered at 1920 x 1080 and inspected, plus a structural read of both .pptx files (slide count, shape inventory, text, notes). |
| 11 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 in the main deck, 0 in the recording deck. |
| 12 | Camera safe areas preserved | Pass. 0 hits in the main deck, 0 in the recording deck. |
| 13 | End-screen area preserved on the final slide | Pass in both decks. |
| 14 | Field Kit URL only on the invitation slide | Pass. Slide 9 only. |
| 15 | Speaker-note timings total about nine minutes | Pass. 0:00 to 9:00, contiguous. |
| 16 | No em dashes | Pass. 0 em dash and 0 en dash characters in visible copy or notes. |
| 17 | "Resume" without an accent | Pass by absence. The word does not appear. |
| 18 | No Career Portability Map or AI Role Relevance Audit promise | Pass. Neither appears. |
| 19 | No Maven or Keep the Proof invitation | Pass. Neither appears. |
| 20 | Version 2 and version 1 files untouched | Pass. Both remain byte-identical; 2.1 writes only `*_v2.1` files and `out/v2.1/`. |
| 21 | No unintended change anywhere in the deck | Pass. Rendered version 2.1 slides compared pixel by pixel against version 2: nine of ten slides are pixel-identical, and the only difference on slide 2 is confined to the bounding box x 308 to 945, y 723 to 750, which is the third line of the corrected paragraph. Nothing else on any slide moved by a single pixel. |

### Overflow-check note

The geometry pass measures every rendered paragraph against the slide canvas.
**Zero warnings were raised on either deck**, so there is again no edge-only versus
visible-clipping distinction to draw. Full-slide background shapes are drawn at
exactly 1920 x 1080 with no bleed and produce no edge warnings. All
audience-facing content sits inside the canvas.

### Product boundary

Unchanged and re-verified. Slide 9 claims only a private, evidence-led career
position assessment using the last 90 days of actual work. No adjacent-role
identification, no industry or employer mapping, no Career Portability Map, no AI
Role Relevance Audit, no title or compensation guarantee, no price.

---

## 5. Output paths

All paths relative to `deliverables/video-1-slides/`.

**Version 2.1 deliverables**

- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.1.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.1.pdf`
- `out/Video-1-Reveal-Builds_v2.1.pptx`
- `VIDEO_1_SLIDE_QA_v2.1.md` (this file)

**Supporting version 2.1 output**

- `out/v2.1/png/slide-01 ... slide-10` at 1920 x 1080
- `out/v2.1/reveals/frame-01 ... frame-21` at 1920 x 1080
- `out/v2.1/Video-1-Reveal-Builds_v2.1.pdf`
- `out/v2.1/contact-sheet-v2.1.png`
- `out/v2.1/recording-deck-order-v2.1.png`
- `out/v2.1/guides/guide-01 ... guide-10`
- `out/v2.1/qa-raw-v2.1.json`, `out/v2.1/qa-raw-main-v2.1.json`

**Source**

- `build/slides_v2_1.py` slide content, copied from `slides_v2.py` with the two corrections
- `build/build_v2_1.py` build and QA pass
- `build/deck.py` shared primitives, unchanged since version 1

Rebuild with `python3 build/build_v2_1.py` from `deliverables/video-1-slides/`.

**Earlier versions, untouched**

- Version 2: `out/...\_v2.pptx`, `out/...\_v2.pdf`, `out/v2/`, `VIDEO_1_SLIDE_QA_v2.md`
- Version 1: `out/...\.pptx`, `out/...\.pdf`, `out/png/`, `out/reveals/`, `out/guides/`
