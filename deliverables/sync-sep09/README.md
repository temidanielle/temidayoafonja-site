# Videos 4 to 7: September 9 script synchronization

A targeted production update, not a strategy rebuild and not a numbering change.

    python3 build.py           # rebuilds all four packages, the ZIPs and the manifest
    python3 masters.py         # verifies the four locked masters and prints their structure
    python3 shorts.py          # prints every Short with its reuse/change status

## Source

The four locked Recording Masters in
`YouTube_Roadmap_and_V4V7_Lock_Sep09_2026.zip`. Each file's SHA-256 is
recomputed and matched against the handoff's own `Source_Lock_Manifest.json`
before anything is generated, and the build aborts if one does not match.

`masters.py` reads those files and never writes to them. The reading copy, the
run of show, the trigger map and the word counts are all generated from the
locked text, so there is no transcription step in which a line could drift.

The word counts reproduce the roadmap's figures exactly (1580, 1801, 1151,
1209), using the roadmap's own method and its own 130 to 145 wpm band.

## Modules

| File | What it holds |
|---|---|
| `masters.py` | Parses the four locked masters: sections, speech, delivery directions, visual maps |
| `frames.py` | 39 assets across four videos, each with a status and a reason |
| `shorts.py` | Imports the existing 24 Shorts and applies targeted patches only |
| `publish.py` | Descriptions and pinned comments, corrected only where the lock made them inaccurate |
| `standing.py` | The standing Riverside instructions that apply from Video 4 onward |
| `build.py` | Every document, the renders, the QA pass, the ZIPs and the manifest |

`docs.py` is borrowed from `new-videos-4-5/build`; the render engine and the
geometry QA are `deliverables/riverside-build`.

## Reuse is proved, not asserted

Every rendered asset is hashed against the pre-synchronization package. An asset
marked REUSE or REORDER whose bytes moved is a QA failure. **28 of 39 carried
over byte-identical.**

Three assets failed that check on the first run. The cause was mine: I had
retyped their draw calls from the previous package instead of copying them, so
type sizes and separator spacing drifted by a few points. They were restored
exactly, which made the reuse claim true rather than relabelling it.

## Checks that were corrected rather than relaxed

Two QA checks failed for reasons that were the checker's fault, and both were
rewritten to test the real thing.

**Sentence triggers.** Six triggers I wrote spanned two script paragraphs, so
they did not exist as single spoken sentences. That is the check working: each
was shortened to a sentence the script actually contains.

**Retired instructions.** The first version read hard-wrapped lines in
isolation, so a paragraph that named a retired rule in order to record that it
was retired failed on the wrapped fragment. It now reads paragraph units. A
separate check was added for the thing that actually matters: that no prompt
still *requires* a retired opening. The V5 sentence "People can respect your
experience..." is retired as an opening only; it is still spoken in the locked
script, so banning the string would have been wrong.

## The QA reports are split

Each `QA_Report.txt` separates 28 **package checks completed now** from 10
**final-export checks still pending**. Executed animation, recorded audio, audio
balance, final pacing, actual runtime, caption placement, chapter timestamps,
thumbnail artwork and live link reachability are PENDING and are not claimed as
verified. No earlier QA pass is reused as evidence.
