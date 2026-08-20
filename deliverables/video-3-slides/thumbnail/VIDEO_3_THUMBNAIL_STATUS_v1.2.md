# Video 3 Thumbnail — Status v1.2

**Status: complete and cleared.** The approved portrait landed in the workspace,
was verified against all four required criteria, and both finals were built from
it.

This supersedes `archive/VIDEO_3_THUMBNAIL_STATUS_v1.1.md`, which recorded the
stop for a missing asset.

## Verification performed before rendering

| Step | Result |
|---|---|
| File present in workspace | Yes |
| File opened and read | Yes |
| Real file name | `a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png` |
| Real pixel dimensions | 1254 x 1254 |
| Gold or caramel sleeveless top | Confirmed |
| Large fabric rosette on the shoulder | Confirmed |
| Braided bun | Confirmed |
| Thoughtful, calm expression | Confirmed |

Two other images arrived in the same batch and were **not** used:

- `7b293c91-78BFE8B3F16F408A8ACE6572F92B19F0.jpeg`, 1536 x 1536 — same outfit but
  a selfie against an office chair and lamp, with the subject low in frame.
- `5bb1bcec-IMG_4785.png`, 1320 x 2868 — a phone screenshot of the LinkedIn
  profile photo screen, showing the same portrait inside a circular crop with app
  chrome around it.

Neither is a studio source. The full-resolution studio portrait was used instead.

## Confirmations

- Real source file name: `a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png`
- Real source dimensions: 1254 x 1254
- Upscaling required: yes for the 4K master, 1.905x. No upscaling occurs in the
  1280 x 720 file that YouTube actually serves, which is a downsample from the
  source. See the manifest for the full arithmetic.
- No part of Temidayo was generated, reconstructed, retouched or altered.
- No substitute photograph was used. The wine-outfit portrait was not used.
- No files outside `deliverables/video-3-slides/thumbnail/` were changed.

## Selection — approved

**Final A is the selected upload version for Video 3.** Approved by Temidayo on
2026-08-20. No further redesign. Title words, portrait and colour system are
locked as built.

Upload this file:

    01-UPLOAD-THESE/FINAL-A-RECOMMENDED-1280x720.jpg
    (repo name: VIDEO_3_THUMBNAIL_FINAL_A_UPLOAD_1280x720.jpg)

| Check | Result |
|---|---|
| File size | 200,945 bytes, 196.2 KB — 9.6 percent of the 2 MB ceiling |
| Under 2 MB | Yes |
| Dimensions | 1280 x 720 |
| Aspect ratio | Exactly 16:9 |
| Format | JPEG, quality 95, progressive, 4:4:4 chroma |

**Final B stays archived as the alternate**, kept intact for future A/B testing:
`VIDEO_3_THUMBNAIL_FINAL_B_UPLOAD_1280x720.jpg`, 204,663 bytes, also 1280 x 720
and also under the limit. Its master, previews and placement simulations remain
in place so it can be swapped in without a rebuild.

The manifest and rationale ship with the package and are not to be separated from
it: `VIDEO_3_THUMBNAIL_MANIFEST_v1.2.md` carries the source-file provenance and
the resampling arithmetic, `VIDEO_3_THUMBNAIL_RATIONALE_v1.2.md` carries the
visual hypothesis behind the two layouts.

## Still open, and not solved here

1. **`/career-decisions` does not exist.** The route has no page, no redirect
   among the netlify.toml rules, and no sitemap entry. The Video 3 CTA points at
   `temidayoafonja.com/career-decisions`. This blocks publication and is a
   website change, which is outside what I was asked to touch.
2. **Chapter timestamps are not final.** As instructed, the deck speaker notes
   and YouTube chapters have not been retimed. They should be set from the real
   export once it exists, against the accepted runtime of roughly 9:50.
