# Video 1 — "How I Changed Jobs Without Starting My Career Over"

A standalone 12-slide, 16:9 presentation deck built for screen recording, from the
*Video 1 Un-script Working Sheet*. Nothing on the website, book page, products,
global styles or existing source files was touched — everything lives in this folder.

---

## Deliverables

| File | What it is |
|---|---|
| `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over.pptx` | **Editable PowerPoint**, 13.333 × 7.5 in (true 1920 × 1080 at 144 px/in). Native text boxes and shapes — every word, colour and position is editable. Speaker notes on each slide carry the timecode, delivery mode and camera cue from the un-script. |
| `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over.pdf` | 12-page PDF, same true slide size, live text. |
| `out/png/slide-01 … slide-12` | Individual **1920 × 1080** PNG frames, named by slide job. |
| `out/reveals/slide-NN-build-N.png` | **Progressive-reveal frames** — every intermediate state of the six build slides (18 frames). Cut between these in the edit instead of animating. |
| `out/Video-1-Reveal-Builds.pptx` / `.pdf` | The same reveal states as an editable deck, if you would rather advance them live. |
| `out/contact-sheet.png` | One-page contact sheet of all 12 slides. |
| `out/phone-thumbnail-check.png` | Every slide rendered at 320 × 180 — the phone-thumbnail legibility check. |
| `out/guides/guide-NN.png` | Each slide with the camera safe area (and, on slide 12, the YouTube end-screen zone) drawn on top. Reference only — do not record these. |

---

## The twelve slides

| # | Slide | Script section | Time |
|---|---|---|---|
| 1 | Title — *How I Changed Jobs Without Starting My Career Over* | 01 Opening promise | 0:00–0:35 |
| 2 | Career path — accounting → consulting → life sciences → technology → people strategy → Capability Formation | 02 Personal context | 0:35–1:25 |
| 3 | The three moves | Bridge into 03 | 1:25 |
| 4 | Move 1 — separate the title from the capability (four questions) | 03 | 1:25–3:10 |
| 5 | Field Kit page 6, statement 9 — *"If my role disappeared tomorrow…"* | 03 artifact | — |
| 6 | Move 2 — translate the work into outcomes (internal description → portable outcome) | 04 | 3:10–5:05 |
| 7 | Onboarding evidence — integrating score **47 → 75** | 04 proof | — |
| 8 | Field Kit page 6, statement 8 — *"I can describe what I do in terms of outcomes…"* | 04 artifact | — |
| 9 | Field Kit invitation — real cover + real page 6 + **temidayoafonja.com/book** | 05 CTA | 5:05–5:35 |
| 10 | Move 3 — 90-day evidence card: Problem / Action / Outcome / Capability | 06 | 5:35–7:25 |
| 11 | Three questions before your next move | 07 Viewer exercise | 7:25–8:25 |
| 12 | End screen — *Is Your Job Making You Less Marketable?* | 07 Final bridge | 8:25–9:00 |

Slides with progressive reveals: **3** (3 steps), **4** (4), **6** (2), **7** (2), **10** (4), **11** (3).

---

## Recording layout

- **Presenter picture-in-picture:** 480 × 270 px at x = 72, y = 72 — 25% of frame width,
  in the upper-left corner, on every instructional slide.
- **Keep-clear zone:** the upper-left 620 × 440 px carries no essential content on any
  slide, so the camera box never covers a word that matters. Verify against `out/guides/`.
- Instructional slides use one consistent rhythm: kicker and headline to the *right* of
  the safe area, body content *below* it.
- **Slide 12** additionally keeps the region x 1130–1860, y 190–890 empty for YouTube's
  linked-video end-screen element. Hold it for at least 12 seconds.
- Camera cues per slide are in the PowerPoint speaker notes.

## Design system

| Role | Colour |
|---|---|
| Medium blue (primary) | `#244B78` |
| Warm cream (ground) | `#F5F1E8` |
| Muted gold (accent) | `#C9A84C` |
| Deep navy (type and bands) | `#0F2346` |
| Rust (small accent only) | `#C1440E` |

Type: **Montserrat** for display and labels, **DM Sans** for supporting copy,
**Cormorant Garamond** for the Field Kit statement slides — the same three families the
website already uses, loaded from `/fonts`.

**Phone-thumbnail check:** all 12 slides were rendered at 320 × 180 (`out/phone-thumbnail-check.png`).
The single idea on every slide — headline, statement, or the 47 → 75 number — stays readable at that size.
On the three list slides (4, 10, 11) the individual rows are secondary by design; that is what the
progressive-reveal frames are for, so each line arrives large and alone on screen while you talk.

---

## Assets — all real, none generated

| Used on | Asset | Source |
|---|---|---|
| Slide 2 | `assets/photo-headshot-green.png` | Your supplied green-background portrait |
| Slide 2 | `assets/photo-headshot-cream.png` | Your supplied cream-background portrait |
| Slide 2 | `assets/photo-portrait-wine.png` | Your supplied present-day wine-dress portrait |
| Slide 9 | `assets/fieldkit-cover.png` | **Actual** Field Kit cover — page 1 of `The_Capability_Formation_FieldKit.pdf`, rendered at 220 dpi |
| Slide 9 | `assets/fieldkit-page-06.png` | **Actual** Field Kit page 6 (Part Two: Optionality) |
| Reference | `assets/fieldkit-page-05.png`, `-07.png` | Actual neighbouring pages, extracted but not used |

No substitute portraits, invented documents or fake product pages were created.
Statements 8 and 9 on slides 5 and 8 are rebuilt as large slide type, quoted verbatim from
page 6 of the Field Kit, as the un-script instructs — the full PDF page is never shrunk onto screen.
Maven is not shown anywhere in this deck.

### Missing asset — please supply

**Earlier-era photographs.** The un-script's slide-2 camera cue calls for "the earlier purple
and green photos as the past." Three photographs were supplied — green-background,
cream-background and the in-room wine portrait — and all three appear to be from the same
recent session; no purple-backdrop or earlier-career photograph was provided. Slide 2
therefore uses the three real photographs supplied, ordered green → cream → present-day,
and no placeholder box was inserted because all three frames are filled with real images.
If you send the earlier purple photograph, it drops into the first frame
(x 700, y 96, 344 × 316) and the deck rebuilds in one command.

Nothing else referenced by the script is missing.

---

## Rebuilding

```bash
cd deliverables/video-1-slides
python3 build/build.py
```

`build/deck.py` describes each slide once as absolutely-positioned elements on a
1920 × 1080 canvas; two backends render that same description — python-pptx for the
editable PowerPoint, and HTML rasterised by Chromium for the exact-pixel PNGs and the PDF.
Slide content lives in `build/slides.py`, one function per slide, each taking a reveal step.
Requires `python-pptx`, `pillow`, `playwright` and the Chromium build in `/opt/pw-browsers`.
