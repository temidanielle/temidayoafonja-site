# Keep the Proof — Build README

Version 1.0.0 · Revised Monday, August 17, 2026 at 1:45 PM CT (America/Chicago)
Author: Temidayo Afonja, Founder and Principal, The Density Group

This document explains how the two customer PDFs are generated so the build is reproducible.

---

## 1. Layout

```
keeptheproof/
├── Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.0_FINAL.pdf   # handbook (deliverable)
├── Keep_the_Proof_Career_Evidence_Ledger_v1.0.0_FINAL.pdf               # ledger (deliverable)
├── Keep_the_Proof_Customer_Bundle_v1.0.0.zip                            # customer ZIP (deliverable)
├── KEEP_THE_PROOF_MASTER_MANUSCRIPT_v1.0.0.md                           # full reading copy + page map
├── KEEP_THE_PROOF_CONTENT_AND_BOUNDARY_MAP_v1.0.0.md
├── KEEP_THE_PROOF_ORIGINALITY_RECONCILIATION_v1.0.0.md
├── KEEP_THE_PROOF_QA_REPORT_v1.0.0.md
├── KEEP_THE_PROOF_CHANGELOG_v1.0.0.md
├── KEEP_THE_PROOF_BUILD_README_v1.0.0.md                                # this file
└── build/
    ├── ktp.py               # engine: fonts, palette, styles, flowables, KTPDoc, Field, tables, callouts
    ├── build_handbook.py    # handbook assembly, sections 1–13 (Parts One–Two) + build
    ├── handbook_part2.py    # handbook assembly, Parts Three–Five (tools, examples, routines, close)
    ├── build_ledger.py      # standalone ledger assembly
    ├── fonts/               # embedded brand TrueType fonts (Cormorant Garamond, DM Sans)
    └── render/              # QA render output (not shipped)
```

## 2. Requirements

- Python 3.11
- `reportlab` (PDF generation)
- `pymupdf` (`fitz`) — used only for QA/inspection and to extract the master manuscript, not for the build itself
- The six TrueType fonts in `build/fonts/`

## 3. Build commands

The build stamp is Central Time (America/Chicago), passed in explicitly so the timestamp on the copyright / how-to-use page is deterministic and correct.

```sh
cd build
BT="$(TZ='America/Chicago' date '+%A, %B %-d, %Y at %-I:%M %p')"

# Handbook (writes to the parent folder)
python3 build_handbook.py ../Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.0_FINAL.pdf "$BT"

# Ledger
python3 build_ledger.py   ../Keep_the_Proof_Career_Evidence_Ledger_v1.0.0_FINAL.pdf "$BT"
```

`build_handbook.py` imports `handbook_part2.py` automatically; you do not run it directly.

## 4. Design notes for future edits

- **Fonts** are registered in `ktp.py::register_fonts()` from `build/fonts/`. Keep the files in place or the build will fall back to core fonts.
- **Palette and styles** live in `ktp.py` (`styles()` and the module-level color constants). Headings carry `keepWithNext` so a section heading never strands at a page bottom when sections flow.
- **Fillable fields** use the `Field` flowable in `ktp.py`. AcroForm text fields ignore the page-layout transform, so `Field.drawOn` maps its position through `canvas._currentMatrix` to place the widget at the true absolute page coordinate. This is what lets fields sit correctly both when placed directly and when nested inside two-column tables. Field names are auto-deduplicated so a repeated form never collides.
- **Page templates**: `KTPDoc` defines `cover`, `divider`, and `content` templates. Section dividers switch templates with `NextPageTemplate` + `PageBreak`. A post-process (`_collapse_breaks`) drops any `PageBreak` immediately followed by a `NextPageTemplate` so a divider is never preceded by a blank page.
- **Page budget**: to keep the handbook in the 30–38 range, selected inter-section page breaks are emitted as soft `GAP` spacers instead of hard breaks; callouts are wrapped in `KeepTogether` so they never split across a page.
- **Version stamp**: set by the `BT` argument. It renders on the copyright page (handbook) and the how-to-use page (ledger), never on the cover.

## 5. Regenerating the supporting documents

The master manuscript is extracted directly from the shipping handbook PDF (so its words always match the product). The QA numbers in the QA report are produced by inspecting the two final PDFs with `pymupdf`. Rebuild the PDFs first, then regenerate these if the content changes.

## 6. Determinism note

Re-running the build with the same `BT` value produces the same content. The PDF's internal `ModDate` still reflects the moment of generation, so two builds with identical content can differ at the byte level while being identical in content. Compare at the content level, not by file hash.
