# New Videos 4 and 5 — build source

Source for the September 7, 2026 packages. Both are complete and ready to
record. The finished packages live in `deliverables/new-video-4/` and
`deliverables/new-video-5/`; the combined archive is
`deliverables/Videos_4_5_FINAL.zip`.

    python3 build.py      # rebuilds both packages, the one pager and the ZIP

| file | what it is |
|---|---|
| `script_v4.py` | Video 4 script, 2,682 words, 18:29 at 145 wpm |
| `script_v5.py` | Video 5 script, 1,917 words, 13:13 at 145 wpm |
| `frames.py` | 8 teaching frames plus CTA and Watch Next per video |
| `meta.py` | packaging, the renumbering table, the full-screen rule, the sound plan |
| `extras.py` | descriptions, Shorts maps, thumbnail briefs |
| `docs.py` | Word formatting helpers |
| `build.py` | assembles all fifteen deliverables per video |

Frame geometry is verified against the rendered DOM by
`deliverables/riverside-build/qa.py`, not against a predicted line count.

## Sources of truth used

- `Video_4 — Outlier Research & Concept.docx`, September 7, 2026, 6,601 words,
  read in full before the scripts were finalized
- the September 7 production brief
- the v5.1 roadmap, as amended by the September 7 revision
- `docs/claims-ledger.md` and `about.html` for every factual claim

## Video 4 timing

| beat | brief | actual |
|---|---|---|
| participation ask | minute 2 to 3 | 2:27 |
| framework named | before the final quarter | 6:33 |
| Claim teaching begins | minute 7 to 8 | 7:08 |
| CTA | end | 17:32 |
| total | 17:00 to 18:30 | 18:29 |

## The locked Claim

> "I get brought in when the evidence is incomplete and an important decision
> still has to be made."

Tested against all five evidence areas. All three Receipts now support it
directly, after the September 7 evidence pass replaced the third one. See
"Evidence pass" below.

## Evidence pass, September 7

A targeted factual pass after the first build. Five corrections, no creative
rewrite:

1. **Video 4's third Receipt was replaced.** It read "more than a thousand
   managers have come through programs I built or led", which proves scale, not
   the Claim. The same era supports a much stronger framing, already documented
   on `case-studies.html` and `about.html`: brought in to a regulated global
   life sciences organization to build a capability function that did not exist,
   where leadership expectations were written down but nothing connected them to
   the decisions managers actually faced. The 1,000+ figure is now the outcome
   of that work rather than the substance of the claim.
2. **All three Receipts now carry context.** Each one states what was unclear,
   what had to be worked out, what Temidayo contributed and what happened, with
   its scope qualifier intact.
3. **"A recruiter has about forty seconds" was removed.** Nothing in the
   research supports it. The research's only scan-time language is the author's
   own rhetorical framing in the white-space statement, is unlabeled, and says
   six seconds rather than forty. Replaced with non-numeric language.
4. **"Different decades" was corrected to "different years".** The three
   Receipts run 2021-2022 and 2022-2026, so different decades was not
   supportable.
5. **Video 5's BLS inference was scoped.** Median tenure is a snapshot of how
   long people have been somewhere, not a count of employers across a whole
   career, so it cannot support "the long single-employer career is not the
   common case". The figures are unchanged; the conclusion now goes only as far
   as the 22 percent figure does.
6. **Video 5's 20-second script now carries the same Spine** as the 90-second
   version, in slightly different words so it does not sound scripted.

## Judgment calls recorded, not resolved silently

Each is written up in the relevant QA report:

1. The cold open departs from the research's recommended Hook A, which states
   flatly that "interesting background" is not a compliment. The brief rules
   that too absolute. The brief is newer, so the script allows that the phrase
   is sometimes genuine and then turns.
2. The research's third-ranked thumbnail, `"INTERESTING BACKGROUND"`, is
   recorded but cannot be used against this script without restoring the
   absolute framing the brief rejected.
3. The research refers to Temidayo as he and him throughout. Every artifact in
   this repository, and the live site, use she and her. The packages follow the
   repository.
4. No misread story was invented. The research asks for one move told in full
   where Temidayo was clearly misread. No such scene is documented anywhere
   here, so none was written.

## What is outstanding

Thumbnail artwork for both videos. Made in Canva, not in this repository. Both
briefs are written; neither video should publish without the approved export.
