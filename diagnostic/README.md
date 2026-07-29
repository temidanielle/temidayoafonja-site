# The Capability Formation Diagnostic — PDF & build

Source of record for the fillable **Capability Formation Diagnostic** PDF
(the 3-page, 12-statement instrument linked from `/diagnostic`).

## Files

| File | What it is |
|---|---|
| `The_Capability_Formation_Diagnostic.pdf` | Canonical interactive PDF — clickable 1–5 circles, auto-fill + live `/30` totals (JS). |
| `The_Capability_Formation_Diagnostic_no-js.pdf` | Same, minus the JavaScript auto-total (clickable circles + typeable boxes only). |
| `diagnostic-source-original.pdf` | The original WeasyPrint PDF the edits were applied to. |
| `rebuild_all.py` | Boundary rewording + `/audit`→`/diagnostic` URL change (redact + reinsert, no cmap-stripping subset). |
| `add_radios.py` | Adds the 12 radio-button groups (60 buttons) over the drawn circles. |
| `add_calc.py` | Adds AcroForm calculation scripts: circle → box → live total. |
| `fonts/` | ASCII subsets (with cmap) of Inter / Inter-Semi-Bold / Inter-Italic used for reinserted display text. |

## What changed vs. the original

1. **Boundary sentence reworded** (page 2) to match the site's boundary note:
   *"Any score between 17 and 21 sits close enough to the line to go either way,
   even a high one."* (was *"If either score falls between 17 and 21, even a
   high one, it is a boundary score."*). The checkbox pledge is unchanged.
2. **`temidayoafonja.com/audit` → `temidayoafonja.com/diagnostic`** in all four
   spots (two footers, the Save-Your-Score link, plus the visible text), and the
   four clickable link targets. `/book` and `/fieldkit` are untouched.
3. **Clickable 1–5 rating circles** — 12 native radio groups (one per statement).
   Selecting draws a navy ring; single-select per row; works in any viewer.
4. **Auto-fill / live totals** (interactive PDF only) — clicking a circle fills
   that statement's answer box and recomputes the `/30` total. Degrades
   gracefully: viewers without PDF JavaScript still get the native circles and
   typeable boxes; only the auto-sum is skipped.

## A note on fonts (important for form fillability)

The original embeds subset TrueType fonts. An aggressive `subset_fonts()` pass
strips their `cmap`, which breaks typed input in the score boxes. `rebuild_all.py`
therefore starts from the original and never calls `subset_fonts` — the form
font (`LNXIQZ+Inter`) keeps its full 2,849-glyph cmap so the boxes stay typeable.
Only the small reinserted display strings use the pre-subset fonts in `fonts/`.

## Rebuild order

```bash
pip install pymupdf pypdf fonttools
# (fonts/ already contains the pre-subset display fonts)
python3 rebuild_all.py    # original -> diag_edited.pdf   (boundary + URLs)
python3 add_radios.py     # diag_edited.pdf -> The_Capability_Formation_Diagnostic.pdf (circles)
python3 add_calc.py       # + calculation scripts -> *_interactive.pdf
```

Note: the scripts expect their inputs in the working directory (they were written
as a linear pipeline); paths at the top of each script may need adjusting if run
from a fresh checkout. The committed PDFs are the finished artifacts.
