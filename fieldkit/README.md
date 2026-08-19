# The Capability Formation Field Kit — source & build

This folder holds the source of truth for the **Capability Formation Field Kit**
PDF (the $150 calibration companion sold via `/fieldkit`).

## Files

| File | What it is |
|---|---|
| `The_Capability_Formation_FieldKit.pdf` | Canonical, published PDF (23 pages). |
| `fieldkit-source-v3.pdf` | Pre-edit input the generator reads. |
| `build_fieldkit.py` | Generator: parses the source PDF and re-emits it via ReportLab. |
| `verify.py` | Verification suite (page count, glyph parity, form-field parity, overlap + margin checks). |

## Background

The original Field Kit PDF was produced by a one-off ReportLab script that was
never committed. `build_fieldkit.py` reconstructs that generator: it parses
every page's content stream (text runs, vector paths, colours) and replays them
onto a fresh ReportLab canvas at identical coordinates, fonts, and colours, and
recreates the 65 interactive AcroForm worksheet fields. All fonts are base-14
(standard ReportLab metrics) and there are no raster images, so text position is
reproduced exactly.

## The boundary-rule correction

The only intentional content change reconciles the boundary-rule threshold with
the canonical wording in the Capability Formation Diagnostic. On page 8, the
first sentence of the boundary rule changed from:

> The boundary rule: within a point or two of the line on either axis, treat
> yourself as standing on the boundary and read both neighboring states.

to:

> The boundary rule: if either score falls between 17 and 21, even a high one,
> treat yourself as standing on the boundary and read both neighboring states.

The second sentence ("Boundary positions move fastest, in both directions.") is
unchanged, as is the Section 2 opener ("Nineteen or higher is high on each
axis.") and the twelve statements (instrument frozen at v1.0).

## Rebuild & verify

```bash
pip install reportlab pymupdf pdfminer.six
python3 build_fieldkit.py fieldkit-source-v3.pdf The_Capability_Formation_FieldKit.pdf
python3 verify.py   # expects original.pdf + new.pdf; see notes below
```

Notes:
- `build_fieldkit.py <input> <output>` — defaults to `original.pdf` → `new.pdf`.
- `verify.py` compares `original.pdf` (pre-edit) against `new.pdf` (rebuilt).
- Reconstruction re-serialises fill colours, so solid fills render within 1/255
  of the source in one channel (imperceptible, below print tolerance). Text
  glyphs are pixel-exact; only page 8's two boundary lines differ.
