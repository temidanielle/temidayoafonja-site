# Video 2 slide deck: build record and QA

**Version 1.0**
**Built Tuesday, August 18, 2026 at 2:31 PM CT**

Build timezone: America/Chicago (CDT, UTC-05:00).

Deck: **Is Your Job Making You Less Marketable?**
Thumbnail words: YOUR SKILLS ARE STALLING
Primary CTA: the Capability Formation Field Kit, temidayoafonja.com/fieldkit
Watch next: Before You Quit Your Job, Check These 3 Things

Content and timing come from the Video 2 un-script working sheet v1.0. The
visual system is the approved Video 1 v2.4 system, used as precedent and not
redesigned. Video 1 files were not opened for writing and are unchanged.

---

## 1. What was built

**13 main slides.** The three tests are three standalone section breaks at three
separate moments. They appear together once, on the recap, after all three have
been taught.

| # | Slide | On screen | Time |
|---|---|---|---|
| 1 | Title | Is Your Job Making You Less Marketable? | 0:00-0:45 |
| 2 | Recognition | Valuable here / Legible elsewhere | 0:45-1:55 |
| 3 | **Section break 01** | Remove the company nouns | 1:55-2:03 |
| 4 | Test one | Company-bound description, then what another employer can understand | 2:03-3:15 |
| 5 | **Section break 02** | Find outside-context evidence | 3:15-3:23 |
| 6 | Test two | Four sources of outside-context evidence | 3:23-4:35 |
| 7 | **Section break 03** | Read the last 90 days | 4:35-4:43 |
| 8 | Test three | New judgment / Same work faster | 4:43-5:55 |
| 9 | **Recap** | All three tests together | 5:55-6:25 |
| 10 | Interpretation | Is my judgment growing? / Can another context use it? | 6:25-7:10 |
| 11 | Action | What can I change before I leave? | 7:10-8:00 |
| 12 | Field Kit | Is your job still building you? temidayoafonja.com/fieldkit | 8:00-8:30 |
| 13 | Watch next | Before You Quit Your Job, Check These 3 Things | 8:30-9:00 |

Contiguous 0:00 to 9:00, no gaps or overlaps. The three section breaks take
eight seconds each, inside the test blocks rather than added to the runtime.

### Reveal builds

The recording deck is **23 frames**, built from sequential duplicate slides, no
PowerPoint animations. Reveals are kept only where they teach:

| Slide | Frames | Build |
|---|---|---|
| 4 Test one | 2 | Company-bound description, then the clearer description |
| 6 Test two | 4 | One evidence source at a time |
| 8 Test three | 4 | The contrast first, then one prompt at a time |
| 11 Action | 4 | One option at a time |

Slides 3, 5, 7 and 9 have **no builds**. Each section break is a single frame,
and the recap arrives with all three tests already present.

### Design notes

Cream ground for the teaching slides, deep navy for the title, the
interpretation and the end screen, the lighter blue for the single contrast
moment on Test three, muted gold for numerals and accents, rust only as the
small rule on the title and end slides. Type sizes, safe areas and whitespace
follow Video 1 v2.4.

Two things carried over deliberately: the section-break composition, one gold
numeral over one statement with a supporting line and air, and the two-panel
before-and-after used on Test one. The statements are sentence case, matching
Video 1, where capitals are reserved for kickers.

---

## 2. QA results

Raw output: `out/qa-raw-v1.0.json`.

### Required confirmations

| # | Confirmation | Result |
|---|---|---|
| 1 | 13 main slides | **Pass.** 13 slides, 13 PDF pages at 13.333 x 7.5 in. |
| 2 | Three standalone test-intro slides at separate moments | **Pass.** Slides 3, 5 and 7, with the teaching slides between them. |
| 3 | All three tests appear together only on the recap | **Pass.** A scan of all thirteen slides for all three test statements returns exactly one slide: 9. Each section break carries its own test and neither of the others, asserted both ways in the build. |
| 4 | Camera-safe areas preserved | **Pass.** 0 text elements in the 620 x 440 upper-left keep-clear zone, in the main deck and across all 23 recording frames. Camera box stays 480 x 270 at (72, 72), 25 percent of frame width. |
| 5 | Field Kit route is temidayoafonja.com/fieldkit | **Pass.** On slide 12 only. |
| 6 | Watch Next has end-screen space | **Pass.** 0 elements intrude on the reserved region x 1130 to 1860, y 190 to 890 on slide 13. Notes carry the twelve-second hold. |
| 7 | No clipped or crowded text | **Pass.** 0 clipped elements, 0 overlapping text boxes, 0 unintended wraps, in both decks. |
| 8 | No generated or invented evidence or assets | **Pass.** See the asset report below. |
| 9 | Video 1 files and unrelated files remain untouched | **Pass.** All Video 1 files byte-identical. Video 2 writes only inside `deliverables/video-2-slides/`. No website file was read into the build or edited. |

### Standard checks

| # | Check | Result |
|---|---|---|
| 10 | Recording deck order | Pass. 23 slides in running order. |
| 11 | No reveal frame removes a permanent element | Pass. 0 removals across all 23 frames. Kickers, headlines, subtitles, backgrounds and card frames are present on every frame of their slide. |
| 12 | Last build of each slide equals the main slide | Pass, content-identical for all 13. |
| 13 | Section breaks and recap carry no builds | Pass. Slides 3, 5, 7 and 9 are one frame each. |
| 14 | Timings total about nine minutes | Pass. Contiguous 0:00 to 9:00. |
| 15 | Voice standard | Pass. 0 em dash and 0 en dash characters in visible copy or notes. No framework, model, method or step language. |
| 16 | Product boundary | Pass. Slide 12 claims only a private, evidence-led career position assessment using the last 90 days of actual work. No adjacent-role identification, no industry or employer mapping, no Career Portability Map, no AI Role Relevance Audit, no title or compensation guarantee, no price. No Maven and no Keep the Proof anywhere. |
| 17 | Not alarmist | Pass. No red warning marks, no countdowns, no scarcity language. Slide 2 states the tension calmly and slide 10 keeps the reading provisional in copy: "One familiar sign is not a diagnosis." The four patterns stay in the speaker notes, not on the slide. |
| 18 | Phone-thumbnail legibility | Pass. All 13 rendered at 320 x 180; the single idea on each slide still reads. Sheet at `out/phone-thumbnail-check-v1.0.png`. |

### Overflow-check note

Zero geometry warnings on either deck, so there is no edge-only versus visible
clipping distinction to draw. Backgrounds are drawn at exactly 1920 x 1080 with
no bleed. All audience-facing content is inside the canvas.

---

## 3. Asset report

**Used, all real:**

- `assets/fieldkit-cover.png`, the actual Field Kit cover, page 1 of
  `The_Capability_Formation_FieldKit.pdf` rendered at 220 dpi.
- `assets/fieldkit-page-06.png`, the actual Field Kit page 6.

**Not used, and nothing was created to fill the gap:** no resumes, LinkedIn
screenshots, performance ratings, employer dashboards, invented statistics,
stock-office scenes or icons. The QBR example on slide 4 is set as plain slide
type, not as a mocked-up document, and stays generic with no employer-specific
or confidential material.

### Missing asset, please supply

**The thoughtful gold-outfit portrait.** The working sheet asks for it where a
portrait is needed, and rules out the wine-dress portrait for this video. The
only photographs supplied to date are that wine-dress session in three
backgrounds, so the gold-outfit portrait is not available here.

No portrait was generated or substituted. Instead, Video 2 was composed so that
no slide requires one: slide 2 carries the recognition as type, which also suits
the working sheet's instruction to keep that beat mostly on camera. If you send
the gold-outfit photograph, slide 2 is the natural home for it and adding it is a
small change.

---

## 4. Before publishing

- Verify the live `temidayoafonja.com/fieldkit` redirect and the current Gumroad
  listing, as the working sheet requires.
- Chapter times in the YouTube description should be adjusted against the final
  export.
- Thumbnails were not produced in this pass, per your instruction.

---

## 5. Output paths

All paths relative to `deliverables/video-2-slides/`.

**Deliverables**

- `out/Video-2-Is-Your-Job-Making-You-Less-Marketable_v1.0.pptx`
- `out/Video-2-Reveal-Builds_v1.0.pptx`
- `out/Video-2-Is-Your-Job-Making-You-Less-Marketable_v1.0.pdf`
- `VIDEO_2_SLIDE_QA_v1.0.md` (this file)

**Supporting output**

- `out/png/slide-01 ... slide-13` at 1920 x 1080
- `out/reveals/frame-01 ... frame-23` at 1920 x 1080
- `out/Video-2-Reveal-Builds_v1.0.pdf`
- `out/contact-sheet-v1.0.png`
- `out/recording-deck-order-v1.0.png`
- `out/phone-thumbnail-check-v1.0.png`
- `out/guides/guide-01 ... guide-13`, camera and end-screen zones drawn
- `out/qa-raw-v1.0.json`

**Source**

- `build/slides.py`, one function per slide, each taking a reveal step
- `build/build.py`, build and QA pass
- `build/deck.py`, the shared primitives, copied unchanged from Video 1 so this
  folder is self-contained and Video 1 is never written to

Rebuild with `python3 build/build.py` from `deliverables/video-2-slides/`.
