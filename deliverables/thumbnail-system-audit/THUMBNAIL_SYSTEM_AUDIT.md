# Three-Video Thumbnail System Audit

Date: 2026-08-20. Nothing was redesigned, created or altered to produce this audit.

## Headline

**The audit cannot be completed as a three-way comparison, and the reason is
material.** Video 3 Final A is approved and valid. Videos 1 and 2 have no
approved thumbnail, and the candidates supplied for them contain synthetic
imagery of Temidayo, which breaks the "real photographs only" rule.

---

## Step 1 — File inventory

### Video 3 — exists, approved

| | |
|---|---|
| Filename | `VIDEO_3_THUMBNAIL_FINAL_A_UPLOAD_1280x720.jpg` |
| Path | `deliverables/video-3-slides/thumbnail/` |
| Version | v1.2 |
| Dimensions | 1280 x 720 |
| File size | 200,945 bytes (196.2 KB) |
| Marked | **SELECTED / APPROVED**, recorded in `VIDEO_3_THUMBNAIL_STATUS_v1.2.md` |
| Source portrait | `a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png`, 1254 x 1254 |

Archived alternate: `VIDEO_3_THUMBNAIL_FINAL_B_UPLOAD_1280x720.jpg`, same folder,
same version, 1280 x 720, 204,663 bytes, marked ALTERNATE.

### Video 1 — no final exists

No thumbnail file. No `thumbnail/` directory. Nothing marked FINAL, RECOMMENDED
or SELECTED. Searched the working tree and all branches of git history. The words
`DON'T START FROM ZERO` appear nowhere in the repository.

### Video 2 — no final exists

Same. The words `YOUR SKILLS ARE STALLING` appear once, as deck metadata on line 9
of `deliverables/video-2-slides/VIDEO_2_SLIDE_QA_v1.0.md`. Recorded, never designed.

> Files named `phone-thumbnail-check-*.png` exist for both videos. Despite the
> name these are slide legibility checks at phone size, not YouTube thumbnails.

### Candidates supplied in this message

Not in the repository. Conversation attachments only. No version number, no
approval marker, no documentation identifying any of them as approved.

| Ref | Words | Dimensions | File size | 16:9? |
|---|---|---|---|---|
| c1 | WHAT STILL TRAVELS? | 1672 x 941 | 3,013,462 B | No — 1.7768 |
| c2 | DON'T START FROM ZERO | 1672 x 941 | 3,711,486 B | No — 1.7768 |
| c3 | YOUR EXPERIENCE COUNTS | 1672 x 941 | 3,154,622 B | No — 1.7768 |
| c4 | YOUR SKILLS ARE STALLING | 1672 x 941 | 3,146,999 B | No — 1.7768 |
| sheet | contact sheet, panels 1A/1B/1C/2/3 | 1536 x 1024 | 2,242,910 B | n/a |

**Competing candidates, not chosen silently.** Video 1 has three competing sets of
words across five files: `DON'T START FROM ZERO` (c2, sheet 1A), `YOUR EXPERIENCE
COUNTS` (c3, sheet 1B), `WHAT STILL TRAVELS?` (c1, sheet 1C). Only the first
matches your locked wording. Video 2 has two competing treatments: c4 (wine outfit,
briefcase blocks) and sheet panel 2 (caramel outfit, desk pose). **No project
documentation identifies any of them as approved, because none is documented at
all.** The contact sheet's own manifest describes a `thumbs_v1.0/` folder that does
not exist in this repository.

---

## The blocking finding

Four independent pieces of evidence, all magnified in
`THUMBNAIL_SYSTEM_AUDIT_EVIDENCE.png`:

**A. A different person is presented as her career history.** The middle polaroid
in "YOUR EXPERIENCE COUNTS" shows a woman in a black business suit with different
facial structure and different hair. It is not Temidayo.

**B. A pose and setting that never existed.** Contact-sheet panel 2 shows her in
the caramel top, seated at a desk, index finger to her temple, with a full office
behind her. The real caramel photograph is a plain studio headshot against a
seamless backdrop with her hands out of frame. No such photograph was ever supplied.

**C. Pseudo-text.** The sticky notes on the papers in that same panel carry
letter-shaped marks that spell nothing in any language. This is a signature of
generative image synthesis.

**D. Garments that do not exist.** Panel 1A shows insets of a purple suit and a
green shirt. Every real photograph available shows the same wine top; "green" in
`photo-headshot-green.png` refers to the **backdrop**, not a shirt. Your expected
visual story for Video 1 asks for "real earlier purple-outfit photograph" and
"real earlier green-shirt photograph" — those photographs do not exist, and
something generated them to fill the gap.

**The supplied contact sheet asserts the opposite.** Its footer reads: "No part of
Temidayo's appearance was generated or altered. All thumbnails use original
photographs only." Items A to D contradict that claim directly. I am flagging the
false assurance as its own finding, because it is the part most likely to cause
harm if trusted.

---

## Steps 2 to 5 — why they are not delivered as specified

Step 2 asks for a contact sheet of the three **selected launch thumbnails**.
Two of the three do not exist in any compliant form. Building that sheet would
require me to either invent Video 1 and 2 thumbnails, or present synthetic
imagery as approved launch artwork. I did neither.

Steps 3 and 4 grade the three against shared rules. Grading imagery that fails
the threshold test — real photographs only — would give it a legitimacy it has
not earned. The one row that can be filled honestly:

| Attribute | Video 1 | Video 2 | Video 3 | Consistent? | Action |
|---|---|---|---|---|---|
| Compliant thumbnail exists | No | No | **Yes** | **NO** | Videos 1 and 2 need original work |
| Real photographs only | Fails (A, D) | Fails (B, C) | **Passes** | **NO** | Do not adopt the candidates |
| Correct locked words | Three competing sets | Matches | **Matches** | **NO** | Confirm Video 1 wording |
| Correct source portrait | Wine, per brief | **Wine, brief says caramel** | Caramel | **NO** | Resolve for Video 2 |
| Upload-ready geometry | 1672 x 941, not 16:9 | 1672 x 941, not 16:9 | **1280 x 720** | **NO** | Rebuild at 16:9 |

---

## Step 5 — verdict

### D. NOT A SYSTEM YET — VIDEOS 1 AND 2 NEED ORIGINAL, COMPLIANT THUMBNAILS

None of A, B or C fits. This is not a cohesion problem to be micro-aligned; two of
the three thumbnails do not exist in a form that can be published under your own
rules.

**Video 3 needs no change and is cleared to upload.**

### What I need from you before building Videos 1 and 2

1. **Photographs.** Real ones. There is no purple-outfit or green-shirt photo. If
   earlier-career photographs exist, they need to land as files. If they do not
   exist, Video 1's "past leading into present" story needs a different device
   built from real material — the green-backdrop and cream-backdrop headshots can
   carry a then/now reading through backdrop and treatment rather than wardrobe.
2. **Video 2's portrait.** Your brief says caramel; candidate c4 uses wine. Confirm
   which, noting the caramel portrait is the one Video 3 already uses — worth
   deciding whether the two videos should share a portrait.
3. **Video 1's title and words.** The title here reads "How **to Change** Jobs
   Without Starting **Your** Career Over"; the deck, scripts and all v2.4 exports
   use "How **I Changed** Jobs Without Starting **My** Career Over".

---

## Confirmations

- No existing thumbnail was overwritten.
- No source photograph was modified.
- No part of Temidayo's appearance was generated or altered by me.
- No website, video, slide, script or product file was changed.
- Video 3 Final A, Final B and all their derivatives are untouched.
