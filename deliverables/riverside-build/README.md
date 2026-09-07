# Riverside edit assets

Build source for the Riverside visual asset sets. These are video visuals for a
talking-head edit, not presentation slides: large type, short copy, and nothing
important below the caption zone.

    python3 build.py 2        # writes deliverables/video-2-slides/riverside/

## Files

| file | what it is |
|---|---|
| `rdeck.py` | renderer: one element list, drawn as PPTX and as exact 1920x1080 PNGs via Chromium |
| `layouts.py` | the card layouts, each composed from measured text so nothing collides |
| `cards.py` | the Video 2, 3 and 4 card sets, with placement metadata |
| `cards_v1.py` | the Video 1 set, slide 01 deliberately absent |
| `audits.py` | per-video audit text: kept, merged, removed, and the real conflicts |
| `qa.py` | geometry QA measured against the rendered DOM |
| `build.py` | the build entry point |

## Why geometry is checked in the browser

PIL and Chromium do not always break a line in the same place. Predicting the
line count with PIL alone let two cards ship with overlapping text in an early
draft. `qa.py` reads the real bounding boxes out of the rendered page and fails
the build on any overlap, any text below the caption line, or anything inside
the safe margin. `layouts.TH` additionally measures against a narrower box than
the browser gets, so the predicted line count is never an under-count.

The existing presentation and reveal decks are never opened for writing.
