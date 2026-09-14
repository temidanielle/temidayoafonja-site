# QA report

Package: Substack visuals for **What Your Current Role Should Be Doing for Your Future**
Checked against `... PRODUCTION_FINAL_v5.2.docx` and the build request.
Automated gate: `source/verify-visuals.mjs`, currently passing.

## Verified

1. **Copy is exact.** Every string on every sheet is compared against
   `source/copy.json` by the gate, and the three card questions plus the cover
   title are compared against the essay text. All match verbatim except the
   Practice question, which is an approved rewrite. See item 7 below.
2. **Placement anchors are present and unaltered** in v5.2. All four were found
   verbatim: "That is what the 3 Ps help you see.", "Practice: What are you
   becoming better able to handle?", "That is exactly where the Starter
   begins.", "Get the free 10-Minute Career Evidence Starter:".
3. **No text is clipped.** The gate checks that every text element sits inside
   its sheet at full size. Nothing overflows.
4. **Legible when scaled down.** Smallest type by sheet: cover 18px, 3 Ps 23px,
   Starter caption 20px. In a 600px wide mobile column those become 6.8px,
   8.6px and 7.5px. The 3 Ps questions, the element that carries the meaning,
   render at 45px, which is 16.9px in that column. A 600px proof was reviewed.
5. **Palette matches the system.** Navy `#0F2347`, cream `#F5F0E8`, gold
   `#B8952E` on cream, white card panels. These are the values the real Career
   Evidence Starter is drawn in, sampled from the artifact renders themselves.
6. **Three assets, two in body.** The cover is marked cover only in the
   manifest and is not placed in the body.
7. **No older graphic reused.** The repository was searched for an existing
   cover, 3 Ps or CURRENT DELIVERY / NEXT PRACTICE graphic. None exists, so all
   three assets are new. No previous graphic was carried over.
8. **No generic career imagery.** No arrows, ladders, puzzle pieces,
   briefcases, dashboards, icons, stock photography, generated people or images
   of Temidayo.
9. **Real artifact only.** Sheet 3 composes the two repository renders
   `career-evidence-starter-cover.png` (sha256 71fec1ffc179) and
   `career-evidence-starter-inside.png` (sha256 a9e010658f3f), both placed by
   reference and unmodified. Each is scaled down, never up: 900 x 1165 natural,
   shown at 560 x 724 and 520 x 673. No page was recoloured, retyped or
   invented, and no timing or performance claim was added. The phrase
   "The 10-Minute Career Evidence Starter" is visible only because it is printed
   on the approved artifact.
10. **No em dash or en dash characters** in the rendered text, `copy.json`, this
    report or the manifest. The gate fails the build on either character.
11. **Export sizes are modest:** 1600 x 900 at 68KB, 1600 x 1000 at 83KB,
    1600 x 1000 at 154KB.
12. **The article document was not modified.**

## Could not verify, or decided rather than guessed

0. **The Practice question is an approved rewrite, at your direction.** The card
   now reads "What can you handle now that was harder before?" This is the
   essay's own 90-day question, "What can I handle now that was genuinely harder
   for me before?", put into second person to match the other two cards. The
   essay heading it replaces, "What are you becoming better able to handle?", did
   not read naturally on the card. Proof and Portability are unchanged and still
   verbatim. The rewrite is recorded in `source/copy.json` under
   `approvedRewrite`, and the gate reports it rather than failing on it, so the
   verbatim check stays in force for every other line.

1. **Two copy lines differ between the build request and v5.2, and I used the
   build request.** Flagging rather than silently reconciling:
   - The 3 Ps title. v5.2 implementation notes call it "The 3 Ps of a Role That
     Builds Your Future" in title case. The build request gives
     "THE 3 Ps OF A ROLE THAT BUILDS YOUR FUTURE" in capitals. The asset uses
     the capitals from the build request. Say the word and it becomes title case.
   - The supporting line under the cards. v5.2 reads "A role does not need to
     maximize all three every quarter. But over time, you should be able to see
     evidence of each one." The build request supplies the shorter
     "A role does not need to maximize all three every quarter. Over time, look
     for evidence of each." The asset uses the build request version.
2. **Cover supporting line and footer are not in v5.2 at all.**
   "BETTER DECISIONS · CLEAR PROOF · MORE OPTIONS" and
   "CAPABILITY FORMATION · TEMIDAYO AFONJA" come only from the build request.
   That is expected for cover furniture, but it means they cannot be checked
   against the essay.
3. **Navy is `#0F2347`, not the `#112345` named in the build request.** The real
   Career Evidence Starter that appears inside asset 3 is drawn in `#0F2347`,
   as is the Density Group brand spec. Surrounding a `#0F2347` artifact with a
   `#112345` field would read as a near miss. One word and the batch re-renders
   on `#112345`.
4. **Gold is `#B8952E`, the brand value for gold on a light field.** The
   `#C8A35D` named in earlier briefs is the on dark value and measures about
   2.5 to 1 against cream, which is too weak for small tracked capitals.
5. **Substack rendering was not tested in Substack.** Legibility was judged from
   a 600px wide downscale, not from a live post. Worth one look in a draft
   before publishing.
6. **The live Career Evidence Starter URL was not checked.** v5.2 asks for that
   verification immediately before publishing. That is a publishing step and
   requires the live site.
