# Video 3 slide deck: refinement record and QA

**Version 1.1**
**Wednesday, August 19, 2026, America/Chicago**

Deck: **3 Things to Do Before Quitting Your Job** (approved title)
Thumbnail words: WAIT BEFORE YOU QUIT
Primary CTA: the Career Decision Evidence Check, temidayoafonja.com/career-decisions
Watch next: How to Change Jobs Without Starting Your Career Over

A refinement and completion of v1.0, not a redesign. v1.0 is preserved unchanged,
Videos 1 and 2 were not touched, and no website file was read into the build or
edited. Before-and-after detail is in `VIDEO_3_CHANGELOG_v1.1.md`.

---

## 1. Required confirmations

| # | Confirmation | Result |
|---|---|---|
| 1 | Title updated to 3 Things to Do Before Quitting Your Job | **Pass.** On slide 1, in the deck metadata, in both v1.1 filenames, in the working sheet, and in the upload copy. No variant of the old title survives anywhere in the v1.1 package. |
| 2 | v1.0 preserved | **Pass.** Every v1.0 file is untouched, including its own filenames. |
| 3 | 13-slide architecture preserved | **Pass.** Same thirteen slides, same order, no teaching slides added, no section slides combined. |
| 4 | All three checks separate before the recap | **Pass.** Slides 3, 5 and 7 each carry their own check and neither of the others, asserted both ways. A scan of all thirteen slides for all three check names returns exactly one slide: 9. |
| 5 | Only slide 6's supporting line materially changed besides title copy | **Pass.** Pixel comparison against v1.0: eleven of thirteen slides are pixel-identical. Slide 1 differs only in the title text block, x 134 to 942, y 530 to 833. Slide 6 differs only inside x 887 to 1534, y 286 to 315, which is the one line of supporting copy. Nothing else on any slide moved by a pixel. |
| 6 | Safety boundary intact | **Pass.** On slide 2 verbatim, in navy beneath a small rust rule, never red, and in the speaker notes on slides 2 and 10. Not softened. |
| 7 | CTA remains the Career Decision Evidence Check | **Pass.** Slide 12, the only invitation in the deck. The Field Kit appears nowhere in the visible copy or the notes. |

> **GATE SATISFIED — production journey verified before launch, 1 September 2026.**
> `https://temidayoafonja.com/career-decisions` is live and the full core
> production journey passed end to end. The blocking statement below is retained
> for release traceability and no longer describes current state.

| 8 | /career-decisions route status explicitly verified or flagged | **Flagged, not verified.** Re-checked against the repository at build time: no page, no redirect among the thirteen rules in `netlify.toml`, no sitemap entry. It would 404 today. The route stays on slide 12 as instructed, no replacement was invented, and it is not claimed live anywhere in this package. |
| 9 | 27-frame reveal structure preserved | **Pass.** 27 frames, same build counts on slides 4, 6, 8, 10 and 11, no builds on 3, 5, 7 or 9, no animations. Six frames differ from v1.0: the title frame and the five builds of slide 6. |
| 10 | No fabricated evidence | **Pass.** No screenshots, employer documents, fake reviews, dashboards, icons or invented statistics anywhere. The internal-process example is described in words and carries no number. |
| 11 | No unrelated files changed | **Pass.** Only files under `deliverables/video-3-slides/`. |
| 12 | Videos 1 and 2 untouched | **Pass.** No file in either folder was modified. |
| 13 | Thumbnail uses only the approved real portrait | **Stopped at verification.** The gold-outfit portrait has not been supplied. Nothing was rendered and nothing was substituted. Full verification in `VIDEO_3_THUMBNAIL_STATUS_v1.1.md`. |
| 14 | No Temidayo appearance generated or altered | **Pass.** No photograph appears in this deck at all, and no image of Temidayo was generated, recreated, retouched or modified anywhere in this task. No source photograph was changed. |

---

## 2. Architecture

| # | Slide | Builds |
|---|---|---|
| 1 | Title, 3 Things to Do Before Quitting Your Job | none |
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

Timings contiguous 0:00 to 9:25.

---

## 3. Standard checks

| # | Check | Result |
|---|---|---|
| 15 | 13 slides, 13 PDF pages | Pass, at 13.333 x 7.5 in. |
| 16 | No reveal frame removes a permanent element | Pass. 0 removals across all 27 frames. |
| 17 | Last build of each slide equals the main slide | Pass, content-identical for all 13. |
| 18 | Camera safe areas | Pass. 0 text elements in the 620 x 440 upper-left keep-clear zone, in the main deck and across all 27 recording frames. |
| 19 | End-screen reserve on slide 13 | Pass. 0 elements intrude on x 1130 to 1860, y 190 to 890. |
| 20 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. The new title sets on three lines as the old one did, and the new slide 6 line sets on one line as the old one did, so no geometry moved. |
| 21 | Text inside its container | Pass, including the slide 4 panels. |
| 22 | Slide 10 exact line | Pass. "The point is not to make the decision slow. The point is to make it legible." The three directions are equal in weight with no visual ranking. |
| 23 | Design system untouched | Pass. Warm cream teaching slides, deep navy title and end slides, muted gold, restrained rust, same typography and spacing. No gradients, icons, stock photography or new illustration styles. |
| 24 | Voice standard | Pass. 0 em dash and 0 en dash characters in slide copy, speaker notes or spoken script. The thirteen production slide markers carry the em dash exactly as specified in the brief; they are annotations, not spoken words, and they do not appear in the reading script. |
| 25 | No keyword stuffing on slides | Pass. No search phrase appears in any slide copy. The primary phrase appears once, in the description's opening sentence, where it reads as a sentence. |

---

## 4. Script package

| File | Notes |
|---|---|
| `script/Video-3-Unscript-Working-Sheet_v1.1_Temidayo_Afonja.docx` | Opens with the viewer transformation, then the production snapshot and run of show. MEMORIZE EXACTLY and SPEAK FROM IDEAS labelled throughout. Carries the approved opening verbatim. |
| `script/Video-3-Teleprompter-Script-with-slide-markers_v1.1.docx` / `.txt` | 1,180 spoken words, about nine minutes at a natural pace, longer with the pauses the script calls for. Thirteen slide markers, exactly as specified. |
| `script/Video-3-Reading-Script-no-markers_v1.1.docx` / `.txt` | Identical spoken copy, all markers removed. |
| `script/Short-3A-...-Preserve-the-Evidence_v1.1` | 132 words, about 44 to 59 seconds. Carries the confidentiality boundary and the safety boundary. |
| `script/Short-3B-...-Two-Things_v1.1` | 131 words, about 43 to 59 seconds. |

Both Shorts point to the video by its approved title and carry no second call to
action. The `.txt` files start on the first spoken line for pasting into Descript.

---

## 5. Output paths

All paths relative to `deliverables/video-3-slides/`.

**v1.1 deliverables**

- `out/Video-3-3-Things-to-Do-Before-Quitting-Your-Job_v1.1.pptx`
- `out/Video-3-Reveal-Builds_v1.1.pptx`
- `out/Video-3-3-Things-to-Do-Before-Quitting-Your-Job_v1.1.pdf`
- `VIDEO_3_SLIDE_QA_v1.1.md`, `VIDEO_3_CHANGELOG_v1.1.md`,
  `VIDEO_3_UPLOAD_COPY_v1.1.md`, `VIDEO_3_PRODUCTION_HANDOFF_v1.1.md`,
  `VIDEO_3_THUMBNAIL_STATUS_v1.1.md`

**Regenerated supporting output**

`out/v1.1/png/` 13 slides, `out/v1.1/reveals/` 27 frames,
`out/v1.1/Video-3-Reveal-Builds_v1.1.pdf`, `out/v1.1/contact-sheet-v1.1.png`,
`out/v1.1/recording-deck-order-v1.1.png`,
`out/v1.1/phone-thumbnail-check-v1.1.png`, `out/v1.1/guides/`,
`out/v1.1/qa-raw-v1.1.json`

**Source**

`build/slides_v1_1.py`, `build/build_v1_1.py`, `script/make_scripts_v1_1.py`,
`script/make_worksheet_v1_1.py`. Rebuild with `python3 build/build_v1_1.py`.

**Archive, untouched**

All v1.0 files under their original names, and the v1.0 script package.
