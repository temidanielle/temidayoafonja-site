# Session Workbook — "Should I Stay or Should I Move?"

Source and build for the **live Capability Position Read** session workbook,
rebuilt in the Capability Formation Field Kit's visual system.

Content is frozen and taken **verbatim** from the v5.3 fillable workbook PDF.
Presentation is rebuilt from scratch to match
`../fieldkit/The_Capability_Formation_FieldKit.pdf`, the canonical house style.
None of the v5.3 PDF's visual decisions are carried over — no navy emphasis
bands, no near-invisible fields, and four navy section openers are added.

## Files

| File | What it is |
|---|---|
| `build_workbook.py` | Generator: draws all 24 pages + 104 AcroForm fields, then attaches the tolerant calculation JS. |
| `verify_workbook.py` | Acceptance-criteria checker (glyphs, dashes, field parity, pass-one purity, statements, computed totals, overlaps, page fill). |
| `fonts/` | Cormorant Garamond + DM Sans, subset to Latin and instanced to static weights (OFL). |
| `Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf` | The rendered, fillable output. |
| `HANDBACK.md` | Page-by-page inspection log and the flagged spec/Field-Kit disagreements. |

## The visual system (matched to the Field Kit)

- **Palette** (exact): navy `#0F2347`, rust `#C1440E`, gold `#C9A84C`, gold-deep
  `#B89532` (gold on light grounds), sand `#F5F0E8`, white. Body text is navy —
  the strict palette lists no other text colour. The one functional exception,
  mandated by the spec for form widgets only, is the **pale-blue field fill
  (`#E9F0F8`) with a tan (`#CDAE70`) 0.75pt border**, so a participant can see
  what is typeable.
- **Type**: Cormorant Garamond (titles, section words, numerals, emphasis
  italics) and DM Sans (body, labels, tables, form text). Interactive field
  *values* use Helvetica (an AcroForm requirement — the same base-14 choice the
  Field Kit build makes for typed text).
- **Chrome**: 96pt navy header bar with a rust icon square, white Cormorant
  title, gold subtitle, and a 2x2 brand mark top-right; gold hairline footer
  with the identity line and page number. Section openers are full-navy pages.
- **No arrow or box glyphs.** Neither brand font contains U+2192 or U+25A1, so
  axis directions read "low at left to high at right" and every checkbox is a
  vector rectangle plus an AcroForm widget.

## Interactivity

- 104 AcroForm fields (84 text, 20 checkbox), names identical to the v5.3 set.
- Ten read-only totals compute automatically: the four axis sums
  (`dens_initial`, `opt_initial`, `dens_corr`, `opt_corr`), the two first-
  placement mirrors (`*_copy`), and the four What-Moved mirrors (`*_r`).
- The calculation JS strips non-numeric characters before summing, so a field
  containing `3?` counts as 3.
- `NeedAppearances` is set and the AcroForm `/CO` calculation-order array is
  populated, so totals fire in Acrobat and most desktop readers. Calculation
  degrades to plain typeable fields in some browser viewers; the totals then
  need a desktop reader to recompute.

## Rebuild & verify

```bash
pip install reportlab pymupdf pdfminer.six fonttools
python3 build_workbook.py            # -> Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf
python3 verify_workbook.py Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf \
        --source /path/to/Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3_FILLABLE.pdf
```

`build_workbook.py` uses ReportLab to draw the pages and create the fields, then
pymupdf to attach the calculation actions (which also builds `/CO`) and set
`NeedAppearances`. The fonts under `fonts/` are the only assets it reads.
