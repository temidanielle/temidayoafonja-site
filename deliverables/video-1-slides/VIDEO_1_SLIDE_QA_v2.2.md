# Video 1 slide deck: refinement record and QA

**Version 2.2**
**Revised Tuesday, August 18, 2026 at 10:34 AM CT**

Build timezone: America/Chicago (CDT, UTC-05:00).

Deck: **How I Changed Jobs Without Starting My Career Over**
Revision type: targeted refinement of the approved version 2.1 deck. Three
slides changed. No redesign. Visual identity, palette, typography, slide
dimensions, layout language, pacing architecture, reveal-build approach, the
onboarding evidence example, the 47 to 75 result, the Field Kit artwork and the
Watch Next structure are all unchanged. Version 2.1 and every earlier version
remain untouched. No website, product, book, thumbnail, banner, profile or other
unrelated asset was modified.

---

## 1. Change log

Every slide changed, and the exact reason.

| Slide | Change | Reason |
|---|---|---|
| 2, career path | Timeline reduced from six mixed entries to four dominant stages: **ACCOUNTING & AUDIT → CYBERSECURITY → PEOPLE STRATEGY → CAPABILITY FORMATION**. Consulting, life sciences and technology moved to one muted line beneath the timeline reading "Along the way: consulting, life sciences, technology". Stage type set at 26 px, tracked, uppercase; context line at 22 px body weight, sentence case. | Refinement 1. The old row mixed functions, industries and settings as if they were equivalent steps, and left cybersecurity out of the visual entirely even though the explanatory copy names it. The four stages now show the substantive kinds of work, and the settings stay visible without competing. |
| 2, career path | Kicker, headline, explanatory paragraph, photograph and composition unchanged. | Refinement 1 requires the existing copy and photograph to be preserved. |
| 3, three things | Kicker "THE THREE MOVES" replaced with "THREE THINGS I LEARNED TO DO". Headline "Three things helped me carry my experience forward." replaced with "These helped me carry my experience forward." | Refinement 2. "Moves" could be read as three job changes rather than three things she learned to do. The new kicker and supporting line carry the same meaning in plain speech, with no framework, model, method or step language. |
| 3, three things | Cards 01, 02 and 03 unchanged in wording, position and styling. | Only the label was in scope. |
| 5, move two | Right-hand card label "Portable description" replaced with "What another employer can understand", set over two lines at the same size, weight, colour and position. | Refinement 5. The teaching point now lands without Capability Formation vocabulary. |
| 5, move two | Kicker, headline, subtitle, the internal description, the example wording and the reveal order unchanged. | Refinement 5 requires the evidence to stay exactly as written. |

Unchanged slides: 1, 4, 6, 7, 8, 9, 10. Verified pixel by pixel, see check 20.

---

## 2. Refinement-by-refinement confirmation

| # | Refinement | Result |
|---|---|---|
| 1 | Career path uses the four-stage hierarchy | Pass. Accounting & audit, cybersecurity, people strategy, Capability Formation are the four dominant labels. Consulting, life sciences and technology appear once, smaller, in body weight, beneath the timeline, and cannot read as stages. Explanatory paragraph, photograph and composition preserved. No dates, employer names, titles or extra stages invented. |
| 2 | "THE THREE MOVES" replaced | Pass. Kicker now reads "THREE THINGS I LEARNED TO DO" with the supporting line "These helped me carry my experience forward." The phrase "the three moves" no longer appears anywhere in the deck. No proprietary framework name introduced. |
| 3 | 01, 02 and 03 reveal separately | Pass. One scene, three sequential states: frame 3 shows card 01 only, frame 4 adds 02, frame 5 adds 03. Kicker, headline and background are identical across all three, so it reads as one slide progressively revealing. Pacing note preserved: "Introduce the three ideas briefly. Do not explain all three on this slide." |
| 4 | Move One questions reveal separately | Pass. Frames 6, 7 and 8 show question 01, then 01 and 02, then all three. Kicker, headline, subtitle and the three questions are unchanged, and no explanatory copy was added. |
| 5 | Move Two label corrected | Pass. "Internal description" kept, "Portable description" replaced with "What another employer can understand". The example is unchanged and the internal description still appears before the translated one, frames 9 then 10. |
| 6 | 47 to 75 language accurate and unchanged | Pass. Slide 6 is byte-identical to version 2.1. Kicker "ONE RESULT", headline "One measure of new-hire integration", subtitle "A team result from a redesign I led", 47 before the redesign then 75 after. No percentage, no invented increase, no renamed metric. The spoken line remains "One measure of how well new hires felt integrated moved from 47 to 75." |
| 7 | Move Three rows reveal separately | Pass. Frames 13 to 16 add Situation, then My role, then What changed, then What this shows. Row wording, the subtitle about a permitted, high-level account, and the instruction to leave confidential and employer-owned material out are unchanged. |
| 8 | Before Your Next Move questions reveal separately | Pass. Frames 17, 18 and 19. Heading, supporting line and all three questions unchanged. Spacing unchanged: the three rows occupy y 476 to 942 on a 1080 canvas, so the final frame holds comfortably. The note still instructs a pause after each question and five to seven seconds after the third. |
| 9 | Field Kit CTA | Copy and artwork unchanged. URL verified rather than guessed, and left unchanged pending your decision. See section 3. |
| 10 | Watch Next intact | Pass. Slide 10 is byte-identical to version 2.1. Right-side end-screen region x 1130 to 1860, y 190 to 890 remains empty, no second CTA, no summary of Video 1, suitable to hold for at least 12 seconds. |
| - | Title slide ruling | Honoured. The deck title remains "How I Changed Jobs / Without Starting / My Career Over". It was not changed to match the search-facing YouTube title. |
| - | Opening ruling | Honoured. Slide 1 notes still read "Begin full-screen on Temidayo rather than on the slide" and "Move to the title slide after introducing the three questions." |
| - | Camera and slide rhythm | Honoured. No slides added, no stock footage, no B-roll prompts. Slide count is unchanged at 10. |
| - | Design restraint | Honoured. No icons, stock imagery, gradients, screenshots, fabricated documents, extra branding text or step language added. The only new mark is one line of muted text on slide 2. |

---

## 3. Field Kit URL verification

**The slide was not changed. This is a reported discrepancy awaiting your decision.**

Slide 9 still displays `temidayoafonja.com/book`, exactly as approved in 2.1.

What the repository actually contains:

1. **`netlify.toml`** defines an explicit, permanent, Field-Kit-only route:
   `/fieldkit` → `https://temidayoafonja.gumroad.com/l/czmqp`, status 301, forced.
2. **`book.html`** is the page served at `/book`. Its title is "Books & Tools" and
   it carries three products in this order: The Capability Audit field guide with
   an Amazon button, then the Capability Formation Field Kit at $150 with a
   "Get the Field Kit" button to the same Gumroad product, then Density, described
   as forthcoming. There is no `/book` redirect rule; Netlify serves `book.html`
   for the extensionless path.
3. **`docs/data-inventory.md`** and **`docs/legal-review-required.md`** both describe
   Field Kit purchase as happening through "the `/fieldkit` redirect".

The discrepancy: `/book` does work and the Field Kit is genuinely on it, so the
current slide is not broken. But `/book` is a three-product page on which the
field guide appears first, so a viewer who types the URL from the video does not
land on the Field Kit itself. `/fieldkit` is the route the repository defines for
exactly that purpose.

Options, for you to choose:

- **Keep `temidayoafonja.com/book`.** Correct if you want viewers to see the full
  set of published assets and choose. No change needed; 2.2 already ships this way.
- **Change to `temidayoafonja.com/fieldkit`.** Correct if the video's single paid
  route should land directly on the Field Kit. This is a one-line change and a
  rebuild, and it would produce a version 2.3.

No route was invented, and nothing was changed without your approval.

---

## 4. QA results

Raw output: `out/v2.2/qa-raw-v2.2.json` and `out/v2.2/qa-raw-main-v2.2.json`.

| # | Check | Result |
|---|---|---|
| 1 | Version 2.1 remains unchanged | Pass. All version 2.1 files, and version 2 and version 1 before them, are byte-identical. Version 2.2 writes only `*_v2.2` files and `out/v2.2/`. |
| 2 | Career path uses the corrected four-stage hierarchy | Pass, asserted in the build. |
| 3 | "THE THREE MOVES" has been replaced | Pass, asserted in the build. |
| 4 | 01, 02 and 03 reveal separately | Pass. Verified in the recording deck and in the rendered frames. |
| 5 | Move One questions reveal separately | Pass. |
| 6 | Move Two label corrected | Pass, asserted in the build. |
| 7 | 47 to 75 language unchanged | Pass. Slide 6 render is pixel-identical to 2.1. |
| 8 | Move Three evidence rows reveal separately | Pass. |
| 9 | Before Your Next Move questions reveal separately | Pass. |
| 10 | Field Kit URL verified, not guessed | Pass. See section 3. |
| 11 | Watch Next intact | Pass. Slide 10 render is pixel-identical to 2.1. |
| 12 | No unrelated assets or website files changed | Pass. The working tree contains only new files under `deliverables/video-1-slides/`. No site page, style, product, image or configuration file was touched. |
| 13 | Main deck is exactly 10 slides | Pass. 10 slides, 10 PDF pages at 13.333 x 7.5 in. |
| 14 | Recording deck order | Pass. 21 slides, running order identical in structure to 2.1. |
| 15 | No reveal frame removes a permanent element | Pass. 0 removals across all 21 frames. Kickers, headlines, subtitles, backgrounds, card frames and the logomark are present on every frame of their slide. |
| 16 | Last build of each slide equals the main slide | Pass, content-identical for all 10. |
| 17 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. The tightest new line is "CAPABILITY FORMATION", which uses 378 px of its 420 px box, a 10 percent margin, and ends 121 px from the slide edge. |
| 18 | Camera safe areas preserved | Pass. 0 hits in the main deck and 0 across all 21 recording frames. |
| 19 | End-screen area preserved | Pass in both decks. |
| 20 | No unintended change anywhere | Pass. Rendered 2.2 slides compared pixel by pixel with 2.1: seven of ten are pixel-identical, and the three changed slides differ only inside the intended regions. Slide 2 differs only within x 120 to 1813, y 847 to 988, the timeline band. Slide 3 differs only within x 712 to 1496, y 136 to 243, the kicker and headline. Slide 5 differs only within x 1084 to 1466, y 568 to 616, the right-hand card label. Nothing else on any slide moved by a pixel. |
| 21 | Voice standard holds | Pass. 0 em dash and 0 en dash characters. No framework, model, method, formula, system or step language. No new teaching concepts. |
| 22 | Timings unchanged | Pass. Contiguous 0:00 to 9:00, identical to 2.1. Approximately nine minutes. |

### Overflow-check note

Zero geometry warnings on either deck, so there is again no edge-only versus
visible-clipping distinction to draw. Full-slide backgrounds are drawn at exactly
1920 x 1080 with no bleed. All audience-facing content is inside the canvas.

---

## 5. Output paths

All paths relative to `deliverables/video-1-slides/`.

**Version 2.2 deliverables**

- `out/Video-1-Reveal-Builds_v2.2.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.2.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.2.pdf`
- `VIDEO_1_SLIDE_QA_v2.2.md` (this file)

**Supporting version 2.2 output**

- `out/v2.2/png/slide-01 ... slide-10` at 1920 x 1080
- `out/v2.2/reveals/frame-01 ... frame-21` at 1920 x 1080
- `out/v2.2/Video-1-Reveal-Builds_v2.2.pdf`
- `out/v2.2/contact-sheet-v2.2.png`
- `out/v2.2/recording-deck-order-v2.2.png`
- `out/v2.2/guides/guide-01 ... guide-10`
- `out/v2.2/qa-raw-v2.2.json`, `out/v2.2/qa-raw-main-v2.2.json`

**Source**

- `build/slides_v2_2.py` copied from `slides_v2_1.py` with the three refinements
- `build/build_v2_2.py` build and QA pass
- `build/deck.py` shared primitives, unchanged since version 1

Rebuild with `python3 build/build_v2_2.py` from `deliverables/video-1-slides/`.

**Archive, untouched**

- Version 2.1: `out/..._v2.1.pptx`, `out/..._v2.1.pdf`, `out/Video-1-Reveal-Builds_v2.1.pptx`, `out/v2.1/`, `VIDEO_1_SLIDE_QA_v2.1.md`
- Version 2: `out/..._v2.pptx`, `out/..._v2.pdf`, `out/v2/`, `VIDEO_1_SLIDE_QA_v2.md`
- Version 1: `out/....pptx`, `out/....pdf`, `out/png/`, `out/reveals/`, `out/guides/`
