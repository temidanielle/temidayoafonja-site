# Video 3 slide deck: refinement record and QA

**Version 1.1**
**Wednesday, August 19, 2026, America/Chicago**

Deck: **Before You Quit Your Job, Check These 3 Things** (working title)
Primary CTA: the Career Decision Evidence Check, temidayoafonja.com/career-decisions
Watch next: How to Change Jobs Without Starting Your Career Over

A refinement of v1.0, not a redesign. Two content changes and four supporting
documents. Version 1.0 is preserved unchanged, Videos 1 and 2 were not touched,
and no website file was read into the build or edited.

Full before-and-after detail is in `VIDEO_3_CHANGELOG_v1.1.md`.

---

## 1. What changed

| Where | Change |
|---|---|
| Slide 6, visible supporting line | "A resume bullet is not automatically portable evidence." becomes "A resume bullet does not automatically show what you can do." |
| Slide 4, speaker notes | Adds the approved heuristic: "The test to say out loud: if you are not entitled to keep it, do not take it." |
| Script and working sheet, Check 1 | The legal-team heuristic is replaced with "If you are not entitled to keep it, do not take it." The line "Preserving your record does not mean taking their material." is kept. |

One correction to the brief's assumption, worth stating plainly: the legal-team
heuristic was never in the presenter notes. The v1.0 deck notes carried no
heuristic at all. It lived in the spoken script and the working sheet, so it was
replaced there, and the approved wording was added to the deck notes where it had
been missing. That is why the script package was reissued at v1.1.

---

## 2. Architecture, preserved

13 main slides, unchanged order, unchanged content except the one line above.

| # | Slide | Builds |
|---|---|---|
| 1 | Title | none |
| 2 | Once you leave, access changes, with the safety boundary | none |
| 3 | Standalone 01, preserve the evidence | none |
| 4 | Check 1, yours to keep and not yours to take | 4 |
| 5 | Standalone 02, name what the work built | none |
| 6 | Check 2, problem, constraint, judgment, outcome | 5 |
| 7 | Standalone 03, test the next move | none |
| 8 | Check 3, uses something proven and builds something new | 4 |
| 9 | Recap, all three checks | none |
| 10 | Decision reading, leave, reposition inside, build a bridge | 3 |
| 11 | Before you resign, three questions | 3 |
| 12 | Career Decision Evidence Check | none |
| 13 | Watch next | none |

27 recording frames, sequential duplicate slides, no animations. Timings
contiguous 0:00 to 9:25.

---

## 3. QA results

Raw output: `out/v1.1/qa-raw-v1.1.json`.

### The change itself

| # | Check | Result |
|---|---|---|
| 1 | New slide 6 supporting line present | Pass. |
| 2 | Old slide 6 line gone | Pass. "portable evidence" appears nowhere in the deck. |
| 3 | Slide 4 notes carry the entitlement test | Pass. |
| 4 | "Preserving your record does not mean taking their material." kept | Pass. |
| 5 | Legal-team heuristic gone everywhere | Pass. Zero occurrences in visible copy, notes, script or working sheet. |
| 6 | Only slide 6 changed visually | Pass. Twelve of thirteen slides pixel-identical to v1.0. Slide 6 differs only inside x 887 to 1534, y 286 to 315, one line of type. |
| 7 | Only slide 6 frames changed in the recording deck | Pass. Five of 27 frames differ, all five being builds of slide 6. The other 22 are pixel-identical. |
| 8 | Reveal architecture preserved | Pass. Still 27 frames, same build counts on slides 4, 6, 8, 10 and 11. |

### Everything the brief asked to preserve

| # | Check | Result |
|---|---|---|
| 9 | 13 main slides, 13 PDF pages | Pass, at 13.333 x 7.5 in. |
| 10 | Order unchanged, no teaching slides added | Pass. |
| 11 | Standalone section slides not combined | Pass. Slides 3, 5 and 7 each carry their own check and neither of the others. |
| 12 | Slide 9 is the only place all three checks appear together | Pass. A scan of all thirteen slides returns exactly one: 9. |
| 13 | Slide 2 safety boundary intact, not red, rust rule kept | Pass. Verbatim on the slide, in navy beneath a small rust rule, and in the notes on slides 2 and 10. |
| 14 | Slide 4 two-column structure and examples intact | Pass. No screenshots, employer documents, fake reviews, dashboards or icons. |
| 15 | Slide 8 unchanged | Pass. Pixel-identical to v1.0. |
| 16 | Slide 9 three-card recap unchanged | Pass. Pixel-identical. |
| 17 | Slide 10 exact line present | Pass. "The point is not to make the decision slow. The point is to make it legible." The three directions are equal in weight, with no visual ranking and no diagnosis. |
| 18 | Slide 11 three questions, one at a time | Pass. Three builds, pause preserved in the notes. |
| 19 | Slide 12 CTA unchanged, Field Kit not substituted | Pass. The Field Kit appears nowhere in the deck or the notes. |
| 20 | Slide 13 end-screen reserve | Pass. 0 elements intrude on x 1130 to 1860, y 190 to 890. |
| 21 | Camera safe areas | Pass. 0 text elements in the 620 x 440 upper-left keep-clear zone, in the main deck and across all 27 recording frames. |
| 22 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. The new supporting line sets on one line, as the old one did, so no geometry moved. |
| 23 | Design system untouched | Pass. No gradients, icons, stock photography, fake documents or new illustration styles. No photograph of any kind appears in this deck. |
| 24 | Voice standard | Pass. 0 em dash and 0 en dash characters. |
| 25 | No keyword stuffing on slides | Pass. None of the TubeBuddy phrases appear in any slide copy. They are confined to the upload document. |

---

## 4. Publication blockers, both re-checked and both still open

### The CTA route does not exist

`temidayoafonja.com/career-decisions` was re-checked against the repository at
build time for v1.1. There is still no page, no redirect among the thirteen rules
in `netlify.toml`, and no sitemap entry. It would 404 today.

The route stays on slide 12 as instructed. No replacement was invented and the
URL is not claimed to be live anywhere in this package. The request to build it
is in `VIDEO_3_PRODUCTION_HANDOFF_v1.1.md`.

### The thumbnail cannot be produced

The gold-outfit portrait has still not been supplied. The photographs available
remain the same three from one wine-dress session, which this video's brief rules
out by name. No thumbnail was produced, nothing was substituted, and no part of
any photograph was generated or altered.

---

## 5. Output paths

All paths relative to `deliverables/video-3-slides/`.

**Version 1.1 deliverables**

- `out/Video-3-Before-You-Quit-Your-Job-Check-These-3-Things_v1.1.pptx`
- `out/Video-3-Reveal-Builds_v1.1.pptx`
- `out/Video-3-Before-You-Quit-Your-Job-Check-These-3-Things_v1.1.pdf`
- `VIDEO_3_SLIDE_QA_v1.1.md` (this file)
- `VIDEO_3_CHANGELOG_v1.1.md`
- `VIDEO_3_UPLOAD_COPY_v1.1.md`
- `VIDEO_3_PRODUCTION_HANDOFF_v1.1.md`

**Regenerated supporting output**

- `out/v1.1/png/slide-01 ... slide-13` at 1920 x 1080
- `out/v1.1/reveals/frame-01 ... frame-27`
- `out/v1.1/Video-3-Reveal-Builds_v1.1.pdf`
- `out/v1.1/contact-sheet-v1.1.png`
- `out/v1.1/recording-deck-order-v1.1.png`
- `out/v1.1/phone-thumbnail-check-v1.1.png`
- `out/v1.1/guides/guide-01 ... guide-13`
- `out/v1.1/qa-raw-v1.1.json`

**Script package, reissued at v1.1**

- `script/Video-3-Unscript-Working-Sheet_v1.1_Temidayo_Afonja.docx`
- `script/Video-3-Teleprompter-Script-with-slide-markers_v1.1.docx` / `.txt`
- `script/Video-3-Reading-Script-no-markers_v1.1.docx` / `.txt`
- `script/Short-3A-Before-You-Resign-Preserve-the-Evidence_v1.1.docx` / `.txt`
- `script/Short-3B-A-Better-Next-Move-Does-Two-Things_v1.1.docx` / `.txt`

**Source**

- `build/slides_v1_1.py`, copied from `slides.py` with the two changes
- `build/build_v1_1.py`, build and QA pass
- `script/make_scripts_v1_1.py`, `script/make_worksheet_v1_1.py`

Rebuild with `python3 build/build_v1_1.py`.

**Archive, untouched**

All v1.0 files: both decks, the PDF, `VIDEO_3_SLIDE_QA_v1.0.md`, the v1.0 PNGs,
frames, sheets and guides, and the v1.0 script package.
