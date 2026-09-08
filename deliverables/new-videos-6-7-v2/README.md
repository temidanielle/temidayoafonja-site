# Videos 6 and 7 revised production packages, v2.0

Built September 8, 2026 from the two **v2.0 Revised Recording Masters**, with
the two v1.0 Final Production Packages used only where they did not conflict
with a revised master. Where they conflicted, the master won.

    python3 build.py      # rebuilds both packages, the manifest and the ZIP

Finished packages:

    deliverables/VIDEO_6_Before_You_Take_An_Internal_Role_FINAL/
    deliverables/VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL/
    deliverables/Video_6_and_7_FINAL_REVISED_Production_Packages.zip
    deliverables/V6_V7_FINAL_MANIFEST.md

## Source rule as applied

The Recording Master is the spoken source of truth. Its spoken copy is
reproduced verbatim in `Approved_Recording_Master_Reference.docx`, verified line
by line by the QA pass: 61 of 61 for Video 6 and 63 of 63 for Video 7, zero
altered. The master files copied into each folder are byte-identical to the
files supplied; they already carried the correct number and title, so no header
edit was needed.

Publishing copy comes from the v1.0 Production Packages, rewritten for Video 6
around the new title and thumbnail and tightened for Video 7 against the v2.0
spoken copy.

## Modules

| File | What it holds |
|---|---|
| `frames.py` | 9 Video 6 assets, 10 Video 7 assets, from each master's visual map |
| `shorts.py` | 6 dedicated 9:16 Shorts per video, Priority A x3 and B x3 |
| `publish.py` | Titles, thumbnails, descriptions, pinned comments, tags, hashtags |
| `build.py` | Every document, the renders, the QA pass, the ZIP and the manifest |

`docs.py` is borrowed from `new-videos-4-5/build`; the render engine and the
geometry QA are `deliverables/riverside-build`.

## Flagged, not silently changed

1. **The Video 6 replacement thumbnail artwork does not exist.** Flagged rather
   than independently redesigned, per the brief. Video 6 cannot publish until it
   is supplied. Recording and editing are not blocked.
2. **Video 6, second question.** The master's visual map writes `WILL YOUR
   JUDGMENT EXPAND?`; its own spoken line and the brief say *my*. The asset uses
   **MY**.
3. **Video 6, decision read.** The master's table reads "Movement, not much
   growth"; the brief and the spoken line use the softer "may be movement
   without much growth". The asset uses the softer wording.
4. **Video 7, `BUSIER IS NOT BETTER`.** Three competing lines on the opening
   frame fell below phone-readable size. The brief calls it an alternate only,
   so it was dropped from the frame and recorded as an alternate thumbnail line.

No spoken copy was changed in any of the four cases.

## Checks that had to be made honest, not loosened

Two QA checks failed on their first run for reasons that were the checker's
fault rather than the package's, and both were rewritten to test the real thing.

**The superseded Video 6 thumbnail line.** A blunt "this string must not appear"
check fails, because `YOU MAY NOT NEED TO LEAVE` is still the approved *closing
spoken line* in the v2.0 master. It is superseded as a thumbnail and nothing
else. The check now tests what matters: the words appear on no asset, and every
line pairing them with the word thumbnail also marks them old or superseded.

**Real limits preserved.** Requiring the word "bias" in both scripts fails Video
7, which argues about role design rather than access and never raises the
subject. The required limits are now taken from what each script actually names,
and the report says plainly that Video 7's bias boundary lives in the run of show
rather than in the spoken copy.

Two other first-run failures were genuine package defects and were fixed: a
British `colour` in two treatment notes, and the Video 7 Watch Next title
breaking into five ragged lines.
