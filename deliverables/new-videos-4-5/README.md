# New Videos 4 and 5 — build source

Source for the September 7, 2026 packages. Both are complete and ready to
record. The finished packages live in `deliverables/new-video-4/` and
`deliverables/new-video-5/`; the combined archive is
`deliverables/Videos_4_5_FINAL.zip`.

    python3 build.py      # rebuilds both packages, the one pager and the ZIP

| file | what it is |
|---|---|
| `script_v4.py` | Video 4 script, 2,621 words, 18:04 at 145 wpm |
| `script_v5.py` | Video 5 script, 1,875 words, 12:55 at 145 wpm |
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
| CTA | end | 16:58 |
| total | 17:00 to 18:30 | 18:04 |

## The locked Claim

> "I get brought in when the evidence is incomplete and an important decision
> still has to be made."

Tested against all five evidence areas. Four support it directly. The 1,000+
managers Receipt is a reach and scale claim rather than a judgment-under-
uncertainty claim, so it supports the Claim less directly than the other two;
that is recorded in Video 4's QA report as a flag rather than fixed by
broadening the Claim or substituting evidence that is not on file.

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
