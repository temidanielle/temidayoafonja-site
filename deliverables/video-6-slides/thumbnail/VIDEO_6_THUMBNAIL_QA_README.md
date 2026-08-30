# Video 6 — Thumbnail Pass QA README (revision 2)

**Video 6 — Growth vs Workload**
Locked thumbnail text: **MORE WORK ≠ GROWTH**

Thumbnail only. The approved Video 6 slides, reveal sequence, decks, PDF,
review sheets and three script files were not opened or modified by this pass.

---

## 1. What changed in revision 2

Revision 1 was built to a written description of the system. Revision 2 is
built to the approved files themselves.

| | Revision 1 | Revision 2 |
|---|---|---|
| Gold divider at the seam | **missing** | restored, `[1470, 0, 1482, 1440]` — the Video 4A / 5A rectangle |
| Faint hairline | missing | restored, x 150–1370 at y 268, white at alpha 22 (Video 5A) |
| Cream | `#F5F1E8` — one value off | `#F5F0E8`, sampled from the approved masters |
| Text column | x 150, width 1234 | x 190, width 1150 (Video 4A / 5A) |
| Headline centre | canvas centre | y 696 = H/2 − 24 (Video 5A) |
| Underline | full width of the payoff word | 0.74 of it (Video 5A's restrained rule) |
| Composition B | solid gold block, GROWTH in navy | **removed.** Replaced with a three-line setting using only established elements |

Every layout constant now comes from the approved build scripts rather than
from a description of them: portrait box `(1470, 0, 2560, 1440)`, divider width
12, column x 190, column width 1150, line gap `s × 0.34`, payoff gap
`s × 0.46`, rule gap `s3 × 0.20`, rule height `s3 × 0.052`, underline
`0.74 × payoff width`.

## 2. Palette — sampled, not retyped

Colours were read back out of the approved upload files:

```
V2   #0F2346  #F5F0E8  #C9A84C
V3   #F5F0E8  #0F2346  #C9A84C
V4A  #0F2346  #C9A84C  #F5F0E8
V5A  #0F2346  #F5F0E8  #C9A84C
V6   #0F2346  #C9A84C  #F5F0E8
```

Video 6 is an exact match with all four approved masters on NAVY, CREAM and
GOLD. The navy `#0F2346` you confirmed is unchanged. The only palette edit in
this revision was cream, which was one point off in the green channel.

## 3. Series geometry

| | approved (V4A / V5A) | Video 6 | |
|---|---|---|---|
| portrait box left edge | 1470 | 1470 | match |
| gold divider width | 12 | 12 | match |
| text column x | 190 | 190 | match |
| text column width | 1150 | 1150 | match |
| headline centre y | 696 | 696 | match |
| hairline y | 268 | 268 | match |
| underline fraction | 0.74 | 0.74 | match |

## 4. The two options

Both use only established elements: navy ground, cream statement, gold payoff,
thin gold divider, faint hairline, short gold underline. No blocks, gradients,
icons, effects or new graphic devices.

- **Option A — two lines.** `MORE WORK` in cream, `≠ GROWTH` in gold beneath it,
  short gold rule under GROWTH. The Video 4A structure.
- **Option B — three lines.** `MORE WORK` cream, the ≠ mark alone on line two in
  gold, `GROWTH` in gold on line three with the short rule. The Video 5A
  structure, line for line.

MORE WORK stays cream and ≠ GROWTH stays gold in both. Cap heights at the
1280 × 720 upload size: MORE WORK 59.5 px in both; GROWTH 71.5 px (A) and
84.5 px (B) — the payoff is the largest text in each.

## 5. Photograph — preserved exactly

Crop and Lanczos downscale only. No background replacement, retouching,
expression change, mirroring or any other alteration; the build contains no
colour or exposure operation at all.

```
crop 1163 x 1536 at (240, 0) -> 1090 x 1440, scale 0.9372 (downscale only)
master A photo area vs pure crop+Lanczos: max diff 0, differing pixels 0 -> IDENTICAL
master B photo area vs pure crop+Lanczos: max diff 0, differing pixels 0 -> IDENTICAL
```

The horizontal offset moved from 310 to 240 to take the wall lamp out of frame
and reduce the office chair to a small wedge behind her shoulder.

## 6. Limitation — portrait scale and eye line cannot be matched by cropping

Stated plainly rather than worked around.

| | inter-pupil distance | eye line |
|---|---|---|
| Video 4A | ~64 px | y ~219 |
| Video 5A | ~69 px | y ~211 |
| **Video 6** | **119 px** | **y 253** |

Two hard constraints make this unreachable:

1. **Scale.** The panel is 1090 × 1440, so its crop must be 0.757 as wide as it
   is tall. The tallest crop the 1536 × 1536 source allows is the full frame,
   giving 1163 × 1536 — which is what is used. Every smaller crop makes her
   larger, never smaller. Matching Video 5A's portrait scale would need a crop
   about 2106 px wide, which is 570 px wider than the photograph exists. The
   selfie was taken at arm's length; the Video 4 / 5 portrait is an
   environmental shot. Cropping cannot add field of view.
2. **Eye line.** With the full-height crop the eye line falls at y 253.
   Raising it to ~215 would mean cropping about 116 px off the top — but there
   are only **9 px** of headroom above her hair at this scale, so that crop
   would cut the top of her head off. It would also enlarge the portrait
   further, worsening the first problem.

Both would require inventing pixels, so neither was done. If closer alignment
matters more than using an unused photograph, the options are a different
supplied photograph (all of which are already in use — see revision 1's audit)
or a new one shot at a wider framing.

## 7. Contact sheet and mobile checks

- `Video_6_Thumbnail_Series_Contact_Sheet.png` — the actual approved upload
  files for Videos 2, 3, 4 and 5 beside both revised Video 6 options, all at the
  same displayed size on the same neutral cream ground.
- `Video_6_Thumbnail_Mobile_Check.png` — 200, 180 and 160 px at 1:1, with the
  approved Video 4 and Video 5 uploads on the same rows as the reference.

Both words and the ≠ mark hold at all three widths in both options.

Worth noting from the contact sheet: Videos 2 and 3 place the photograph on the
left, Videos 4 and 5 on the right. Video 6 follows Videos 4 and 5.

## 8. Carried-forward approvals recorded

- **The editable vector treatment of the ≠ symbol is approved.** No repository
  font contains U+2260, so it is built from vector geometry rather than
  substituted with another character or a non-brand font.
- **The 12 slide-marker placements are approved.**
- The 12 main slides and the 23-frame reveal sequence are approved.
- The narrow script correction is approved and in place in all three files.

## 9. Files

| File | Purpose |
|---|---|
| `Video_6_Thumbnail_A_UPLOAD_1280x720.jpg` | Option A, upload file |
| `Video_6_Thumbnail_B_UPLOAD_1280x720.jpg` | Option B, upload file |
| `Video_6_Thumbnail_A.png` / `_B.png` | 1280 × 720 lossless masters |
| `Video_6_Thumbnail_A_2560x1440.png` / `_B_2560x1440.png` | 2× render masters |
| `Video_6_Thumbnail_Series_Contact_Sheet.png` | Videos 2–6 as one series |
| `Video_6_Thumbnail_Mobile_Check.png` | 200 / 180 / 160 px against V4 and V5 |
| `VIDEO_6_THUMBNAIL_QA_README.md` | This file |

All thumbnails are exactly 16:9. Upload JPGs are ~205 KB, inside YouTube's 2 MB
limit.

## 10. Status — CLOSED

**This thumbnail task is closed. Neither Composition A nor Composition B was
selected.** Temidayo is finalising the Video 6 thumbnail in Canva, which is
producing a closer visual match to the established channel thumbnails. The
files here are superseded and are retained only as a record of the work and its
verification. Do not treat them as the Video 6 upload asset.

The rest of this document stands as the record of what was built and measured.

- **The final upload title remains pending TubeBuddy validation.**
- Video 1 Option A vs Option B is still outstanding from the launch audit.
- Videos 4 and 5 share the wine portrait in the same layout.
