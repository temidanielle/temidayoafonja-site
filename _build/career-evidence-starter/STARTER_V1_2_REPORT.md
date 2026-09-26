# Career Evidence Starter v1.2 — Report

## Branch and commit
- Branch: `claude/career-evidence-starter-v1-2`
- Created from `claude/keep-the-proof-v2-finalize` (that branch is not yet merged into `main`, so per the timing rules the new branch was cut from it, not from `main`).
- v1.2 content commit (source, PDF, previews, archived v1.1): `8eae3bdef4056eead9c56000d65f737bb05b9a7c`
- This report is committed on top of that; the pushed branch HEAD is recorded at push time.

## Main and the live site were not changed
- `origin/main` is unchanged at `48a743895487ffd082f79723223852c9cad96110`. All commits are on the new branch only. The branch was not merged and no pull request was opened for auto-merge.
- The live Starter that the site and Kit currently deliver is `resources/keep-the-proof-career-evidence-starter-v1-1-dac91eea9ebf.pdf`. It was **not** touched. No download link, delivery config, or website copy was changed. `_build/` is 404'd by `netlify.toml`, so the new v1.2 file is not web-served.
- Keep the Proof is free on LinkedIn through Sunday, Oct. 18, 2026; nothing that serves the live Starter changes until Temi approves deployment on or after Oct. 19.

## Email address used
- Used the one clear public contact email published on the site: **temidayo@thedensitygroup.com** (it appears as a `mailto:` contact across privacy.html, terms.html, for-professionals.html, speaking.html, and others). The placeholder was not left in; no address was invented.

## What changed (this revision only)
- New page 2, "Before You Rebuild Anything," inserted after the cover and before "Why I Made This." Condensed from Handbook pages 7 and 8, with the six Words That Hold in a cream panel with a gold left edge, set in the serif to match the Handbook. No fill-in line was added, and no personal story was added.
- New "Send me your Proof Line" ask on the final page, placed after "Adapt the evidence to the conversation…" and before "One Proof Line is useful…".
- The Starter goes from 6 to 7 pages; footers renumbered 1 through 7.
- Output file renamed to v1.2. Everything else (the seven prompts, Quick Capture, Before You Write checks and the "not legal advice" line, the Project Horizon before-and-after, the Can It Travel checklist, the "Why I Made This" quote, the Keep the Proof handoff, and the temidayoafonja.com/keep-the-proof link) is unchanged.

## Checks
1. **Forbidden-term scan of v1.2 text** (em dash, en dash, "résumé", "CV", "actually", "honestly", "genuinely", "stand on", "60-minute system", "Career Evidence Ledger"): **zero hits.**
2. **Six Words That Hold vs Handbook page 8:** all six lines match character for character, confirmed present in both v1.2 page 2 and Handbook page 8.
3. **Structure:** PDF is **7 pages**. Footers read 1 through 7 (the cover carries its own footline; pages 2 through 7 show 2 through 7). Nothing overflows or is clipped; the final italic line clears the running foot. Fillable fields still work: **15 text fields and 8 checkboxes** (unchanged from v1.1; the new page adds no fields; the form is not flattened).
4. **Previews rendered** for page 2 (Before You Rebuild Anything) and page 7 (the closing ask), at readable resolution.

## Files changed (one line)
`starter-source.html` (new page 2 + Words That Hold panel CSS + closing-ask block + footer renumber), `build.js` / `qa.js` / `fieldtest.js` / `README.md` (v1.2 filename), added `Keep_the_Proof_Career_Evidence_Starter_v1.2.pdf` + `starter_v1_2_page2_*.png` + `starter_v1_2_page7_*.png`, and moved the v1.1 PDF to `archive/v1.1/`.

## Deployment steps (for Temi, on or after Oct. 19 — written out, not run)
Do these only after the free LinkedIn window closes on Oct. 18 and you approve the update.
1. Publish the file: copy `_build/career-evidence-starter/Keep_the_Proof_Career_Evidence_Starter_v1.2.pdf` into `resources/` under a cache-busting name, for example `resources/keep-the-proof-career-evidence-starter-v1-2-<hash>.pdf` (mirror the v1.1 naming). Do not delete the v1.1 file until the swap is verified.
2. Point delivery at v1.2:
   - In Kit (the email that delivers the Starter), replace the attached or linked Starter file with the v1.2 PDF.
   - Update any site reference or docs that name the v1.1 file (for example `docs/career-evidence-starter-emails.md` and `docs/career-evidence-starter-qa.md`) to the new v1.2 filename.
3. Merge/deploy the branch so the new resource is live (the website session's normal merge path), or cherry-pick the v1.2 file if only the download needs to change.
4. Verify with a test download: in a private browser window, request the Starter through the live form, open the delivered PDF, and confirm it is 7 pages, opens on the cover, shows "Before You Rebuild Anything" as page 2, and shows "Send me your Proof Line" on the final page.
5. Once verified, retire the old v1.1 resource file.
