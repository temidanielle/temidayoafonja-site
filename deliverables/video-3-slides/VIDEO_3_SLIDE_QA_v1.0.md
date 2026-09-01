# Video 3 slide deck: build record and QA

**Version 1.0**
**Built Wednesday, August 19, 2026 at 10:44 AM CT**

Build timezone: America/Chicago.

Deck: **Before You Quit Your Job, Check These 3 Things**
Thumbnail words: WAIT BEFORE YOU QUIT
Primary CTA: the Career Decision Evidence Check, temidayoafonja.com/career-decisions
Watch next: How to Change Jobs Without Starting Your Career Over

Built in the approved Capability Formation system, using Video 1 v2.4 and Video 2
v1.1 as visual, reveal and production precedent. Neither of those decks was
opened for writing and both are unchanged.

---

## 1. Two things are blocked, and one source was missing

### Blocked: the thumbnail. Nothing was produced.

Your instruction was explicit: if the approved gold-outfit portrait is
unavailable, stop and report rather than substitute another image. **It is
unavailable.** The only photographs supplied across this project are one
wine-dress session in three backgrounds, and that portrait is ruled out for this
video by name.

So no thumbnail was made. Not the 3840 x 2160 master, not the JPG, not the upload
version, not the 640, 360 or 200 pixel previews, and none of the three feed
simulations. Nothing was generated, altered or substituted for the portrait.

Send the gold-outfit photograph and the full thumbnail set can be produced in one
pass. Everything else about it is already decided: WAIT BEFORE YOU QUIT, a
prominent 3, a three-row checklist, neutral checkmarks, no icons, no alarmist
colour.

### Blocked for publication: the CTA route does not exist yet.

`temidayoafonja.com/career-decisions` is on slide 12 as instructed, and it is the
only invitation in the video. But the route is **not in the repository**. There is
no page, no redirect in `netlify.toml`, and no sitemap entry. As things stand it
would 404.

This is a publication blocker, not a deck problem. The slide is correct and does
not need changing. Somebody needs to build the destination before the video goes
live. The `/fieldkit` pattern is the precedent if it is going to be a redirect.

### Missing source: the launch cluster document

`Temidayo_Afonja_YouTube_Three_Video_Launch_Cluster_v1.1.docx` was named as source
of truth but was not attached to the request. The build therefore used the brief
itself, which specifies the title, thumbnail words, editorial job, viewer,
transformation, safety boundary, all three checks with their content, the decision
reading, the CTA, the watch-next, the full thirteen-slide architecture, the reveal
rules, the visual system and the run time.

No teaching material was invented to fill the gap. If the cluster document
contains anything the brief did not, send it and I will reconcile.

---

## 2. What was built

**13 main slides.** The three checks are three standalone section breaks at three
separate moments, and they appear together once, on the recap, after all three
are taught.

| # | Slide | On screen | Time |
|---|---|---|---|
| 1 | Title | Before You Quit Your Job, Check These 3 Things | 0:00-0:50 |
| 2 | Recognition | Once you leave, access changes, plus the safety boundary | 0:50-1:35 |
| 3 | **Section break 01** | Preserve the evidence | 1:35-1:43 |
| 4 | Check one | Yours to keep, and not yours to take | 1:43-3:15 |
| 5 | **Section break 02** | Name what the work built | 3:15-3:23 |
| 6 | Check two | Problem, constraint, judgment, outcome | 3:23-4:55 |
| 7 | **Section break 03** | Test the next move | 4:55-5:03 |
| 8 | Check three | Uses something proven / Builds something new | 5:03-6:30 |
| 9 | **Recap** | All three checks together | 6:30-6:45 |
| 10 | Decision reading | Leave / Reposition inside / Build a bridge | 6:45-7:45 |
| 11 | Before you resign | Three questions | 7:45-8:35 |
| 12 | CTA | Career Decision Evidence Check | 8:35-9:00 |
| 13 | Watch next | How to Change Jobs Without Starting Your Career Over | 9:00-9:25 |

Contiguous 0:00 to 9:25, inside the 9 to 9.5 minute target. The safety boundary
and the pauses were not compressed to hit a round number.

### Reveal builds

**27 frames**, sequential duplicate slides, no animations.

| Slide | Frames | Build |
|---|---|---|
| 4 Check one | 4 | Two permitted items at a time, then the boundary column |
| 6 Check two | 5 | One row at a time, then the closing question |
| 8 Check three | 4 | The contrast, then one question at a time |
| 10 Decision reading | 3 | Leave, then reposition inside, then build a bridge |
| 11 Before you resign | 3 | One question at a time |

Slides 3, 5, 7 and 9 carry no builds.

### Where the safety boundary lives

On slide 2, beneath a small rust rule, in navy rather than red: "If your health or
safety is at risk, or you are facing harassment or discrimination, this is not a
reason to wait." It is also in the speaker notes on slide 2 as a memorized line,
and again on slide 10, so a viewer arriving at the decision reading hears it a
second time. It is not softened anywhere, and nothing about the video is styled to
alarm.

---

## 3. QA results

Raw output: `out/qa-raw-v1.0.json`.

### Your required confirmations

| # | Confirmation | Result |
|---|---|---|
| 1 | No unrelated files changed | **Pass.** Only new files under `deliverables/video-3-slides/`. No website file was read into the build or edited. |
| 2 | Videos 1 and 2 remain byte-identical | **Pass.** No file in either folder was modified. |
| 3 | No fake evidence introduced | **Pass.** No employer documents, screenshots, dashboards, performance ratings or invented statistics anywhere in the deck. The internal-process example is described in words and carries no number. |
| 4 | Safety boundary intact | **Pass.** On slide 2 verbatim, in the notes on two slides, and unsoftened. |
| 5 | Career Decision Evidence Check is the primary CTA | **Pass.** On slide 12, the only invitation in the deck. The Field Kit does not appear anywhere in the visible copy or the notes. |
| 6 | All three checks separate before the recap | **Pass.** Slides 3, 5 and 7 each carry their own check and neither of the others, asserted both ways. A scan of all thirteen slides for all three check names returns exactly one slide: 9. |
| 7 | Thumbnail uses only the approved real portrait | **Not applicable, and reported.** No thumbnail was produced. See section 1. |
| 8 | No part of Temidayo's appearance generated or altered | **Pass by construction.** No photograph of any kind appears in this deck, and none was generated, edited or substituted. |

### Standard checks

| # | Check | Result |
|---|---|---|
| 9 | 13 main slides, 13 PDF pages | Pass, at 13.333 x 7.5 in. |
| 10 | Recording deck | Pass. 27 slides in running order. |
| 11 | No reveal frame removes a permanent element | Pass. 0 removals across all 27 frames. |
| 12 | Last build of each slide equals the main slide | Pass, content-identical for all 13. |
| 13 | Section breaks and recap carry no builds | Pass. |
| 14 | Camera safe areas preserved | Pass. 0 text elements in the 620 x 440 upper-left keep-clear zone, in the main deck and across all 27 recording frames. |
| 15 | End-screen reserve preserved | Pass. 0 elements intrude on x 1130 to 1860, y 190 to 890 on slide 13. |
| 16 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. |
| 17 | Text stays inside its container | Pass. Checked explicitly on slide 4, where the six permitted items were overflowing the white panel on the first build and were refitted. Lowest text now ends at y 934 inside a panel ending at 986. |
| 18 | The exact decision line is present | Pass. "The point is not to make the decision slow. The point is to make it legible." on slide 10. |
| 19 | The do-not-take boundary is on the slide | Pass. Confidential information, customer data, employee data and proprietary documents all named on slide 4. |
| 20 | Voice standard | Pass. 0 em dash and 0 en dash characters in visible copy or notes. |
| 21 | Timings | Pass. Contiguous 0:00 to 9:25. |

---

## 4. Script package

| File | What it is |
|---|---|
| `script/Video-3-Unscript-Working-Sheet_v1.0_Temidayo_Afonja.docx` | The filming working sheet, in the format of Videos 1 and 2: production snapshot, run of show, section-by-section un-script, presentation map, rehearsal checklist and upload package. |
| `script/Video-3-Teleprompter-Script-with-slide-markers_v1.0.docx` / `.txt` | Continuous spoken copy with ten slide markers. 1,171 words, about nine minutes at a natural pace, longer with the pauses the script calls for. |
| `script/Video-3-Reading-Script-no-markers_v1.0.docx` / `.txt` | The same words with every marker removed. |
| `script/Short-3A-Before-You-Resign-Preserve-the-Evidence_v1.0.docx` / `.txt` | 133 words, about 44 to 60 seconds. Opening, Check 1, and the confidentiality boundary. Points to Video 3. No sales pitch. |
| `script/Short-3B-A-Better-Next-Move-Does-Two-Things_v1.0.docx` / `.txt` | 129 words, about 43 to 58 seconds. The proven-and-new distinction. Points to Video 3. No sales pitch. |

The `.txt` files start on the first spoken line so they paste straight into
Descript. Both Shorts carry the safety boundary where it applies and neither
contains an additional call to action.

---

## 5. Output paths

All paths relative to `deliverables/video-3-slides/`.

**Deliverables**

- `out/Video-3-Before-You-Quit-Your-Job-Check-These-3-Things_v1.0.pptx`
- `out/Video-3-Reveal-Builds_v1.0.pptx`
- `out/Video-3-Before-You-Quit-Your-Job-Check-These-3-Things_v1.0.pdf`
- `VIDEO_3_SLIDE_QA_v1.0.md` (this file)

**Supporting output**

- `out/png/slide-01 ... slide-13` at 1920 x 1080
- `out/reveals/frame-01 ... frame-27`
- `out/Video-3-Reveal-Builds_v1.0.pdf`
- `out/contact-sheet-v1.0.png`
- `out/recording-deck-order-v1.0.png`
- `out/phone-thumbnail-check-v1.0.png`
- `out/guides/guide-01 ... guide-13`
- `out/qa-raw-v1.0.json`

**Source**

- `build/slides.py`, one function per slide, each taking a reveal step
- `build/build.py`, build and QA pass
- `build/deck.py`, the shared primitives, copied unchanged so this folder is
  self-contained and Videos 1 and 2 are never written to
- `script/make_scripts.py`, `script/make_worksheet.py`

Rebuild with `python3 build/build.py` and `python3 script/make_scripts.py`.

---

## 6. Before publishing


> **GATE SATISFIED — production journey verified before launch, 1 September 2026.**
> `https://temidayoafonja.com/career-decisions` is live and the full core
> production journey passed end to end. The blocking statement below is retained
> for release traceability and no longer describes current state.

1. Build the `/career-decisions` destination. It does not exist today.
2. Send the gold-outfit portrait so the thumbnail set can be produced.
3. Confirm the title against TubeBuddy if a replacement is coming; the deck uses
   the working title as instructed.
