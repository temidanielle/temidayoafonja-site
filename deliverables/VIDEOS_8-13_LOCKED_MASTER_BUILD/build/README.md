# Videos 8 to 13 production build

First Code production build for Videos 8 to 13, from the six supplied final
Recording Masters. Isolated batch: it writes only inside
`VIDEOS_8-13_LOCKED_MASTER_BUILD/` and never touches the V4 to V7 work or
Videos 1 to 3.

    python3 build813.py       # builds all six packages, the ZIPs and the manifest
    python3 masters813.py     # verifies the six masters and prints their structure
    python3 shorts813.py      # prints every Short with its duration estimate

## Source hierarchy as applied

The six final masters are the primary source of truth. Each file's SHA-256 was
recorded before anything was generated, and an unchanged copy sits in each
video's `01_Recording_Master/`. The build reads them and never writes to them,
so the reading copies, run of show, trigger maps and word counts are all
generated from the locked text.

The spoken section is taken between `RECORDING SCRIPT STARTS HERE` and
`END OF SPOKEN SCRIPT`. Section headings, production labels and the closing
instruction are excluded from the spoken word count.

The earlier components archive was used as **secondary reference only**, for
asset concepts and Shorts drafts, each remapped to the locked script. The
`Recording_Master_v1.0_REVIEW` files were not used as spoken sources, and
`Code_Build_Prompt_V8-V13.txt` was not executed as a second instruction set.

## Modules

| File | What it holds |
|---|---|
| `masters813.py` | Parses the six locked masters: sections, speech, word counts, hashes |
| `lay813.py` | Batch-local layouts built on the shared primitives |
| `frames813.py` | 54 assets, nine per video, each with the full specification |
| `shorts813.py` | 36 Shorts, six per video, four Priority A and two B |
| `publish813.py` | Titles, thumbnails, descriptions, pinned comments, tags, Canva briefs |
| `exercise813.py` | Viewer exercises |
| `riverside813.py` | The standing Co-Creator rules that go into every prompt |
| `build813.py` | Every document, the renders, the QA pass, the ZIPs and the manifest |
| `summary813.py` | Delivery summary and the scoped roadmap/tracker patch |

## Why the shared layouts were not edited

`layouts.py` in `riverside-build` is shared with the V4 to V7 packages. Adding
a parameter to it would risk changing their renders, so this batch has its own
`lay813.py` built on the same primitives. Verified: all 39 V4 to V7 assets
still re-render byte-identically after this build.

## Assets are new builds

No prior rendered V8 to V13 artwork exists, so every PNG here is a new build
from a reusable concept, not a byte-identical reuse. The earlier asset
specifications were proposed build specifications rather than finished
graphics, and the packages say so.

## Mobile readability is inspected, not asserted

Every frame is measured against the rendered DOM for overlap, caption-zone and
safe-edge violations, and the build aborts on any failure. Each video's
`03_Visuals/` then carries a 390-point-wide contact sheet that was actually
read at that size.

Three frames were reduced during the build for that reason rather than shrunk:
V9's context list dropped one item and its footer, and V13's hypothesis frame
dropped its footer. In each case the removed line is still spoken, and the
build note on the asset records the decision.
