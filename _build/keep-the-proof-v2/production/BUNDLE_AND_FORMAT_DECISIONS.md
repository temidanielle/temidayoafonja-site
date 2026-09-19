# Keep the Proof V2 — Customer bundle and format decisions

Internal build record. Not shipped to customers.

## Final customer bundle (what the buyer receives)

| # | File | Customer label | Format | Purpose |
|---|------|----------------|--------|---------|
| 1 | `01_START_HERE.pdf` | READ THIS FIRST | PDF (2 pp) | Orientation + map of the bundle, the one rule, how to begin |
| 2 | `02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf` | LEARN & BUILD | PDF (47 pp) | The full teaching guide |
| 3 | `03_YOUR_PROFESSIONAL_RECORD.docx` | KEEP USING | Word (.docx) — **primary** | Editable, copyable, searchable long-term working document |
| 3b | `03_YOUR_PROFESSIONAL_RECORD.md` | KEEP USING (portable copy) | Markdown / plain text | Maximally durable, universally openable mirror of the same record |
| 4 | `04_PRINTABLE_FILLABLE_TOOLS.pdf` | PREFER PRINT OR A FORM? | Fillable PDF (8 pp) | Same fields as the Professional Record, as printable + fillable form pages |

## Professional Record format decision (item 6)

**Requirement:** primary format must be copyable, searchable, editable, platform-neutral, and durable — with no forced dependency on Notion, Excel, Google, or any proprietary app or subscription.

**Decision:** ship the Professional Record as **`.docx` (primary) plus a `.md` plain-text mirror.**

**Why `.docx` is the primary working document:**
- It is the single most universally *editable* rich-text working format. It opens and edits natively in Microsoft Word, Google Docs, Apple Pages, LibreOffice/OpenOffice, and most mobile office apps — the customer is not pushed into any one vendor's ecosystem.
- The underlying format (Office Open XML) is a published ISO/IEC standard (29500), not a closed proprietary blob, so it is durable and readable far into the future.
- It is fully copyable and searchable, supports the structured prompts, fillable lines, checklists, and the index table the record needs, and the customer can duplicate entry blocks for years of use.
- A PDF was rejected as the primary working document because a PDF is not comfortably editable for daily capture; the fillable PDF instead serves the "prefer print / prefer a form" customer as component 4.

**Why a `.md` / plain-text mirror ships alongside it:**
- Plain text / Markdown is the most durable and portable format that exists — it opens in any text editor on any device, forever, with zero software dependency, and pastes cleanly into any note app, wiki, or document.
- It guarantees the customer never loses access to the *structure and prompts* of their record even if they have no word processor at all.
- Both formats carry the **identical field set** (they are generated from one shared field model), so nothing differs but the medium.

**Platform-neutrality:** neither file names or requires any specific app, spreadsheet, or service. The guide and record repeatedly tell the customer to keep their copy "somewhere you control and your employer does not own," without recommending a product.

## Same-fields guarantee (items 6–7)

`03_YOUR_PROFESSIONAL_RECORD.docx`, `03_YOUR_PROFESSIONAL_RECORD.md`, and `04_PRINTABLE_FILLABLE_TOOLS.pdf` are all generated from one shared field model (`record_model.py`), so the Professional Record and the Printable & Fillable Tools hold exactly the same underlying fields, prompts, and order. Customers are told, in both Start Here and the Professional Record, that they do **not** need to complete both — they choose whichever they will keep up.

## Career Evidence Ledger (item 6)

The V1 **Career Evidence Ledger** is retired from the active bundle. Its useful fields and prompts were absorbed into the Professional Record (Capture Log, Full Entries, Corroboration, Translation & Proof Line workspace, running index, optional monthly/quarterly checklists). The V1 files are **archived, not deleted**, at `_build/keep-the-proof-v2/archive/v1_bundle/`:
- `Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf`
- `Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf`
- `KEEP_THE_PROOF_START_HERE_v1.0.1.pdf`

No active V2 artifact is a Career Evidence Ledger, and no active V2 primary artifact is the old Ledger.
