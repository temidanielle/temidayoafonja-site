# Video 6 — Thumbnail Pass QA README

**Video 6 — Growth vs Workload**
Locked thumbnail text: **MORE WORK ≠ GROWTH**

This pass covers the thumbnail only. The approved Video 6 slides, reveal
sequence, decks, PDF, review sheets and three script files were not opened,
rebuilt or modified by this pass.

---

## 1. Carried-forward approvals recorded

These were approved by Temidayo Afonja in the slides-and-script pass and are
recorded here as locked:

- **The editable vector treatment of the ≠ symbol is approved.** No repository
  font contains U+2260, so the mark is constructed from vector geometry rather
  than substituted with another character or a non-brand font. The deck draws it
  as three editable PowerPoint shapes; this thumbnail draws it with the same
  proportions as raster geometry, since a thumbnail is a flat image by nature.
- **The 12 slide-marker placements are approved.** Markers 1–12 in the
  teleprompter script are locked and were not touched by this pass.
- The 12 main slides and the 23-frame reveal sequence are approved.
- The narrow script correction ("Then take **these** questions into the
  conversation with your manager:") is approved and in place in all three
  script files.

## 2. Photograph selection — full audit of the supplied assets

The brief required a real supplied photograph **not used for the final Video 4
or Video 5 thumbnail**. Every supplied image was inventoried and its use traced
through the build scripts that produced each final thumbnail.

| Supplied photograph | Native size | Used in a final thumbnail |
|---|---|---|
| `photo-headshot-cream.png` (= upload `IMG_4870`) | 800 × 800 | **Video 1** |
| `photo-headshot-green.png` (= upload `IMG_4869`) | 800 × 800 | not used |
| caramel studio portrait `a55ff6e1…B5.png` | 1254 × 1254 | **Video 2 and Video 3** |
| `photo-portrait-wine.png` (= upload `c4c7ac00…F7.png`) | 1122 × 1402 | **Video 4 and Video 5** |
| caramel selfie `7b293c91…F0.jpeg` | 1536 × 1536 | not used (Video 3 Variant D only, not selected) |
| LinkedIn profile screenshot `IMG_4785` | 1320 × 2868 | not used |

Two candidates were rejected and the reasons are recorded rather than assumed:

- **`photo-headshot-green.png` is not a distinct photograph.** It is the same
  exposure as `photo-headshot-cream.png` with a different backdrop colour.
  Measured: the eye region is byte-identical between the two files (max channel
  difference 0), the red garment is identical, and only the backdrop differs
  (100% of backdrop pixels differ, mean difference 182). Using it would place
  the identical pose and expression already carrying Video 1 into the system a
  second time. Its expression is also a broad open smile, which does not meet
  the brief's "calm, direct and thoughtful" requirement — and expression cannot
  be altered.
- **The LinkedIn screenshot is unusable as a source.** It is a phone screen
  capture containing interface chrome, and the photograph inside it is masked
  into a circle. Filling a rectangular portrait panel from it would require
  inventing background that does not exist in the file.

**Selected: `deliverables/video-6-slides/assets/photo-selfie-caramel.jpg`** — a
byte-identical copy of the supplied upload `7b293c91-78BFE8B3F16F408A8ACE6572F92B19F0.jpeg`
(sha256 `2d0869d55156fbb671965f2b78a582e084e7b7350cfade3049b3e86ea6cdb4d4`,
verified identical after copying). It is a real photograph, is not the Video 4 /
Video 5 portrait, has never appeared in a published thumbnail, and its
expression is calm, closed-mouth and thoughtful.

## 3. Photographic integrity

Only crop and Lanczos **downscale** were applied. No generation, reconstruction,
beautification, smoothing, reshaping or mirroring. No exposure or colour
adjustment of any kind was applied — the build contains no such operation.

Verified by re-deriving the crop independently and comparing it to the photo
panel inside each rendered master:

```
crop taken     : 1163 x 1536 at x=310  (native pixels)
panel rendered : 1090 x 1440   scale 0.9372  (downscale only, never upscaled)

master A photo panel vs pure crop+Lanczos: max diff 0, differing pixels 0  -> IDENTICAL
master B photo panel vs pure crop+Lanczos: max diff 0, differing pixels 0  -> IDENTICAL
```

The rendered photograph is bit-for-bit what a crop and a downscale produce from
the supplied file. Nothing else was done to it.

## 4. The two compositions

Both keep the established system: deep navy panel left, photograph right, hard
vertical seam, Montserrat ExtraBold uppercase, cream statement with the payoff
term in muted gold — the same structure as the Video 4 and Video 5 finals.

- **Composition A** — single-line equation. `MORE WORK` in cream above
  `≠ GROWTH` in gold, with a gold rule under GROWTH. Closest to the Video 4 and
  Video 5 typographic device.
- **Composition B** — the mark stands on its own line and `GROWTH` is reversed
  out of a solid gold block. Higher contrast; GROWTH is the largest element on
  the frame by a clear margin.

**GROWTH emphasis.** Required to be strongest or equally strong. Measured cap
heights at the 1280 × 720 upload size:

| element | Composition A | Composition B |
|---|---|---|
| MORE WORK | 64.0 px | 64.0 px |
| GROWTH | **77.0 px** | **84.5 px** |

GROWTH is the tallest text in both, and in both it is the only element carrying
gold as a fill or a ground.

## 5. Legibility at phone-feed size

Confirmed, not asserted: `Video_6_Thumbnail_Mobile_Check.png` shows each master
Lanczos-downscaled to 200, 180 and 160 px wide at 1:1, beside the same
downscale magnified 3× nearest-neighbour so no detail is added. Every word and
the ≠ mark survives at all three widths in both compositions.

Cap height in pixels as actually served:

| element | @1280 | @200 px | @160 px |
|---|---|---|---|
| MORE WORK (both) | 64.0 | 10.00 | 8.00 |
| GROWTH (A) | 77.0 | 12.03 | 9.62 |
| ≠ mark (A) | 66.0 | 10.31 | 8.25 |
| GROWTH (B) | 84.5 | 13.20 | 10.56 |
| ≠ mark (B) | 65.5 | 10.23 | 8.19 |

Clearance from the photo seam, so no text ever collides with the portrait:
Composition A leaves 44 px, Composition B leaves 66 px (at 1280 width).

## 6. Exclusions honoured

No icons, calendars, task lists, warning graphics, arrows, ladders, logos,
extra wording or generated scenery. The frame carries only the three locked
words, the drawn ≠ mark, one gold rule (A) or one gold block (B), and the
photograph. Measured: 99.4% of the navy panel is exactly one of the three brand
colours, the remainder being anti-aliasing between them — there is no fourth
colour, no gradient and no texture.

Palette: NAVY `#0F2346`, CREAM `#F5F1E8`, GOLD `#C9A84C`.

## 7. Files in this package

| File | Purpose |
|---|---|
| `Video_6_Thumbnail_A_UPLOAD_1280x720.jpg` | Composition A, upload file |
| `Video_6_Thumbnail_B_UPLOAD_1280x720.jpg` | Composition B, upload file |
| `Video_6_Thumbnail_A.png` / `_B.png` | 1280 × 720 lossless masters |
| `Video_6_Thumbnail_A_2560x1440.png` / `_B_2560x1440.png` | 2× render masters |
| `Video_6_Thumbnail_Comparison.png` | A vs B, full size plus 200/180/160 px previews |
| `Video_6_Thumbnail_Mobile_Check.png` | Phone-size legibility evidence with 3× inspection |
| `VIDEO_6_THUMBNAIL_QA_README.md` | This file |

All image files are exactly 16:9 — 1280 × 720 or 2560 × 1440. Upload JPGs are
roughly 205 KB, well inside YouTube's 2 MB limit.

## 8. Open items

- **Composition A or B has not been selected.** Both are supplied for your
  choice; neither is marked final.
- **The final upload title remains pending TubeBuddy validation.** No title is
  recorded as final in this package.
- Video 1 Option A vs Option B thumbnail selection is still outstanding from the
  earlier launch coherence audit.
- Videos 4 and 5 share the wine portrait in the same layout. Flagged previously;
  still your call.
