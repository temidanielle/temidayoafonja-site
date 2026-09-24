# ARCHIVED: Keep the Proof v1.0.2 (do not ship)

**Status: archived and superseded. This version is not shipped.**

Keep the Proof **V2** is the version that ships. It is the ground-up rebuild in
`_build/keep-the-proof-v2/production/` (four-file bundle: Start Here, the 47-page
Guided Handbook, Your Professional Record `.docx`, and the 9-page Printable &
Fillable Tools). See `../../production/GUMROAD_AND_LAUNCH_HANDOFF.md` for the launch
and existing-customer-update steps.

v1.0.2 was an incremental update to the older "60-Minute Career Evidence System"
product. Its improvements have been **ported into V2**:

- The **Match Your Proof to a Role** page (three columns: what the role asks for /
  my Proof Line that shows it / the gap I will name), with the same instructions,
  the worked example, and the boundary note. In V2 it appears in the Guided Handbook
  (Part Eight), in the Professional Record `.docx`, and in the Printable & Fillable
  Tools PDF.
- The **organization group-license line** on the copyright page:
  "Organizations providing Keep the Proof to employees or program participants can
  arrange a group license at temidayoafonja.com/work."
- The **"60 minutes is a guide, not a deadline"** language, in Start Here and under
  "Your First 60 Minutes," with natural "Good place to pause" points marked in both
  first-session paths.

The V2 voice rules were then applied across every customer-facing file (no em dashes,
no "actually/honestly/genuinely" except the defined term "Actual ownership," no
"it is not X, it is Y" constructions, and "Founder, The Density Group" as the byline).

## The files in this folder

These are the built v1.0.2 deliverables, kept only for reference and reproducibility:

- `Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.2_FINAL.pdf`
- `Keep_the_Proof_Career_Evidence_Ledger_v1.0.2_FINAL.pdf`
- `KEEP_THE_PROOF_START_HERE_v1.0.2.pdf`
- `KEEP_THE_PROOF_v1.0.2_CHANGELOG.md`
- `KEEP_THE_PROOF_v1.0.2_GUMROAD_DRAFT.md`

Their reproducible ReportLab build source lives on the branch
`claude/keep-the-proof-v1_0_2` under `keeptheproof/build/`. That `keeptheproof/`
directory is deliberately kept off the website's `main` branch so the paid PDFs are
never web-served; this archive copy sits under `_build/`, which the site's
`netlify.toml` returns 404 for, so it is not web-served either.

**Do not upload these v1.0.2 files to Gumroad. Ship the V2 bundle instead.**
