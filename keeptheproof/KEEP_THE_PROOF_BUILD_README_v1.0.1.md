# Keep the Proof - Build README

Version 1.0.1
Author: Temidayo Afonja, Founder and Principal, The Density Group

This document explains how the two customer PDFs are generated so the build is
reproducible. It supersedes the v1.0.0 build README for the v1.0.1 outputs; the
v1.0.0 files are preserved unchanged.

---

## 1. Layout

```
keeptheproof/
├── Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf   # handbook (deliverable)
├── Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf               # ledger (deliverable)
├── KEEP_THE_PROOF_CUSTOMER_BUNDLE_v1.0.1.zip                            # customer ZIP (deliverable)
├── KEEP_THE_PROOF_MASTER_MANUSCRIPT_v1.0.1.md                           # full reading copy + page map
├── KEEP_THE_PROOF_CONTENT_AND_BOUNDARY_MAP_v1.0.1.md
├── KEEP_THE_PROOF_v1.0.1_QA_REPORT.md
├── KEEP_THE_PROOF_v1.0.1_CHANGELOG.md
├── KEEP_THE_PROOF_BUILD_README_v1.0.1.md                                # this file
├── customer/READ_ME_FIRST.txt                                          # ships in the ZIP
└── build/
    ├── ktp.py               # engine: fonts, palette, styles, flowables, KTPDoc, Field,
    │                        #   shared reusable forms (quick_capture_fields, full_entry_pages,
    │                        #   two_up_fields) and the Bookmark outline flowable
    ├── build_handbook.py    # handbook assembly, Parts One-Two + build
    ├── handbook_part2.py    # handbook assembly, Parts Three-Five (tools, examples, routines, close)
    ├── build_ledger.py      # standalone ledger assembly
    ├── fonts/               # embedded brand TrueType fonts (Cormorant Garamond, DM Sans)
    ├── buildtime.txt        # the Central-Time build stamp used for the shipped PDFs
    ├── requirements.txt     # pip dependencies and the system packages QA needs
    ├── gen_manuscript.py    # regenerates the master manuscript from the shipping handbook PDF
    ├── qa_content.py        # content + structure QA
    ├── qa_acroform.py       # AcroForm enumeration, fill / reopen / persistence QA
    ├── qa_accept.py         # RC2 form acceptance test (capacity + fill/save/reopen)
    ├── render3.py           # render selected pages through PyMuPDF, Poppler, Ghostscript
    └── qa_multiengine.py    # render every page through all engines; flag blanks / divergence
```

Every file listed above is committed to the repository and included in the
source archive; there is no separate `render/` output directory (QA renders are
written to a scratch path outside the tree).

## 2. Requirements

- Python 3.11
- `reportlab` (PDF generation) - tested with 5.0.1
- `pymupdf` (`fitz`) - used only for QA/inspection and to extract the master
  manuscript, not for the build itself. Tested with 1.28.2.
- The six TrueType fonts in `build/fonts/`.

## 3. Build commands

The build stamp is Central Time (America/Chicago), passed in explicitly so the
timestamp on the copyright / how-to-use page is deterministic.

```sh
cd build
BT="$(TZ='America/Chicago' date '+%A, %B %-d, %Y at %-I:%M %p')"

# Handbook (writes to the parent folder)
python3 build_handbook.py ../Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf "$BT"

# Ledger
python3 build_ledger.py   ../Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf "$BT"
```

`build_handbook.py` imports `handbook_part2.py` automatically; you do not run it
directly.

## 4. Design notes for v1.0.1 edits

- **Covers** are drawn by a `Cover` flowable whose `drawOn` is overridden to
  paint on the untranslated canvas at absolute page coordinates. The default
  `Flowable.drawOn` translated the canvas to the frame cursor and pushed the
  cover text off the page, which was the v1.0.0 blank-cover defect.
- **Reusable forms** are defined once in `ktp.py` so the handbook and the ledger
  never drift: `quick_capture_fields(S, prefix)` (five prompts, one per page)
  and `full_entry_pages(S, prefix)` (the twenty-field, two-page Full Entry, the
  same wording and order in both PDFs). `two_up_fields` lays two separate fields
  in one row for short metadata without merging prompts.
- **Multiline fields** set the AcroForm multiline flag; principal narrative
  fields are tall enough for a realistic 150-300 character answer without
  scrolling. Field names are auto-deduplicated, but the forms are authored with
  unique names.
- **Bookmarks** use the `Bookmark` flowable, which calls `bookmarkPage` and
  `addOutlineEntry` at its position. Levels never jump (a level-1 entry always
  follows a level-0 parent).
- **Page templates** (`cover`, `divider`, `content`) and the `_collapse_breaks`
  post-process are unchanged from v1.0.0.
- **Version stamp** is set by the `VERSION` constant in each build script and
  the `BT` argument; it renders on the copyright / how-to-use page and in the
  PDF metadata keywords, never on the cover.

## 5. Regenerating the supporting documents

Rebuild the PDFs first, then regenerate:

```sh
cd build
BT="$(cat buildtime.txt)"
python3 gen_manuscript.py ../Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf \
    ../KEEP_THE_PROOF_MASTER_MANUSCRIPT_v1.0.1.md "$BT"
python3 qa_content.py  ../Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf \
                       ../Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf
python3 qa_acroform.py ../Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf /tmp/hb_filled.pdf
python3 qa_acroform.py ../Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf /tmp/lg_filled.pdf
```

## 6. Determinism note

Re-running the build with the same `BT` value produces the same content. The
PDF's internal `ModDate` still reflects the moment of generation, so two builds
with identical content can differ at the byte level while being identical in
content. Compare at the content level, not by file hash.

## 7. Output metrics (v1.0.1, build RC2)

- Handbook: 41 pages, 16 bookmarks, 25 unique AcroForm fields (23 multiline).
- Ledger: 12 pages, 7 bookmarks, 117 unique AcroForm fields (51 multiline).

The Full Career Evidence Entry is three pages (all narrative fields full width
so a 200-300 character answer stays visible), and the optional-AI-prompt section
has its own page.

## 8. Multi-engine QA (RC2)

`requirements.txt` lists the pip packages (`reportlab`, `pymupdf`, `pillow`,
`numpy`) and the two system packages the render QA uses: `poppler-utils`
(`pdftoppm`) and `ghostscript` (`gs`). `qa_multiengine.py` renders every page
through PyMuPDF, Poppler (whole-document and isolated-page), and Ghostscript and
flags blank pages or renderer-dependent divergence; `qa_accept.py` runs the form
acceptance test. Run them after every rebuild.
