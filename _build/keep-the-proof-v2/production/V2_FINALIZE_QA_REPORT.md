# Keep the Proof V2: finalize-before-launch QA report

V2 is the version that ships. v1.0.2 is archived and not shipped
(`archive/v1.0.2/ARCHIVED.md`). This report covers the voice pass, the v1.0.2
ports into V2, the four-file consistency, and the automated checks.

## 1. Automated checks (all four bundle files + website + Gumroad description)

Checks: em dashes (U+2014), the three banned words (actually / honestly / genuinely,
keeping the defined term "Actual ownership"), "Founder and Principal", and the
"it is not X, it is Y" antithesis pattern.

| Surface | Pages | em dash | actually | honestly | genuinely | Founder and Principal | "not X, it is Y" |
|---|---|---|---|---|---|---|---|
| 01 Start Here (PDF) | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 02 Guided Handbook (PDF) | 47 | 0 | 0 | 0 | 0 | 0 | 0 |
| 03 Your Professional Record (.docx) | — | 0 | 0 | 0 | 0 | 0 | 0 |
| 04 Printable & Fillable Tools (PDF) | 9 | 0 | 0 | 0 | 0 | 0 | 0 |
| keep-the-proof.html (live page) | — | 0 | 0 | 0 | 0 | 0 | 0 |
| Gumroad description (§2 of handoff) | — | 0 | 0 | 0 | 0 | 0 | 0 |

"Actual ownership" (the defined field term) is retained in the handbook and the
Professional Record, as required.

## 2. v1.0.2 improvements ported into V2

- **Match Your Proof to a Role** (three columns: what the role asks for / my Proof
  Line that shows it / the gap I will name), with instructions, the worked example,
  and the boundary note. Now in: the Guided Handbook (Part Eight, near "Retrieving
  the right evidence"), the Professional Record `.docx` (Section 5), and the
  Printable & Fillable Tools PDF (a dedicated form page). Confirmed present in all
  three.
- **Organization group-license line** on the copyright page: "Organizations
  providing Keep the Proof to employees or program participants can arrange a group
  license at temidayoafonja.com/work." Confirmed present.
- **"60 minutes is a guide, not a deadline"**: in Start Here and under "Your First
  60 Minutes" (about an hour of focused time, or several shorter sittings), with
  "Good place to pause" markers in both first-session paths (6 pause markers rendered
  in the handbook). Confirmed present.

## 3. Four-file consistency (site, Start Here, Gumroad)

All three list the same four files with the same page counts: Start Here; Guided
Handbook (47 pages); Your Professional Record (editable Word / Google Docs / Pages);
Printable & Fillable Tools (9 pages). Price held at $49. The Capture / Clarify /
Carry spine preserved.

## 4. Files changed

Sources (customer-facing text): `FINAL_MANUSCRIPT.md`, `scripts/build_handbook.py`,
`scripts/record_model.py`, `scripts/build_record_docx.py`,
`scripts/build_start_here.py`, `scripts/build_fillable_pdf.py`, `keep-the-proof.html`,
`GUMROAD_AND_LAUNCH_HANDOFF.md`. Rebuilt outputs: all four bundle files (+ the
internal `.md` mirror and the render HTML).
