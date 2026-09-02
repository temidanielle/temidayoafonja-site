# Capability Formation — Series Status Tracker

Series-level record of publication gates, open decisions and outstanding
assets. Kept here so individual video packages do not have to be reopened to
carry a cross-cutting note.

Last updated: 1 September 2026.

---

## Publication gates

### `temidayoafonja.com/career-decisions` — GATE SATISFIED, 1 September 2026

**Production journey verified before launch.** The permanent page is live at
https://temidayoafonja.com/career-decisions and the full core journey passed end
to end. This supersedes the 31 August entry, which rested on a page-live
confirmation alone; the gate is now cleared on a verified journey, not just a
reachable URL.

What Temidayo verified:

| | |
|---|---|
| Page | Loads correctly |
| Gated reveal | Hidden Lightning Lesson and Register Free CTA appear only after successful submission |
| Unsubscribed addresses | Previously unsubscribed Kit addresses were **not** improperly reactivated |
| New subscriber | Submitted successfully; three evidence-check questions appeared; Lightning Lesson CTA appeared |
| Delivery email | "Your Career Decision Evidence Check" arrived immediately, and appears in Kit Email History |
| Kit record | Subscriber created with **Confirmed** status |
| Tags applied | `Career Decision Evidence Check — Requested`, `YouTube` |
| Ongoing Guidance tag | **Not** added, as intended |
| Consent fields | `delivery_consent = true`; `delivery_policy_version = 2026-08-18`; `guidance_consent = false`; guidance timestamp and policy fields empty |
| Attribution | YouTube UTM values captured correctly |

Recorded honestly: I could not verify any of this independently. Outbound
requests to temidayoafonja.com are refused by this environment's egress proxy,
and Kit is not reachable from here. The status above rests entirely on
Temidayo's production verification.

**Effect on the series.** The August 28 roadmap audit routes the Career Decision
Evidence Check to Videos 3, 5, 11, 17, 18 and 21 and stated "publish only when
the page is live and usable." That condition is **satisfied**, for those videos
and for any future video routed to the same destination. The URL is retained
unchanged: `https://temidayoafonja.com/career-decisions`.

Historical gate language is deliberately **not deleted** anywhere. It is marked
`GATE SATISFIED — production journey verified before launch` in place, so
release traceability survives. The documents carrying that marker are listed
under *Gate history* below.

The routine pre-publication signed-out link check stays in the publishing SOP
for every video that carries the URL.

#### Superseded — the 31 August 2026 entry, retained for traceability

> ### `temidayoafonja.com/career-decisions` — CLEARED, 31 August 2026
>
> **Temidayo confirmed the page is live at https://temidayoafonja.com/career-decisions.**
> This gate is closed for Video 3 and Video 5 on that confirmation.
>
> Recorded honestly: I could not verify it independently. Outbound requests to
> temidayoafonja.com are refused by this environment's egress proxy
> (`connect_rejected`, organization policy), and the route does not appear in the
> website source in this repository, so there was nothing here to corroborate it
> against either. The status above rests on Temidayo's confirmation, not on a
> check I ran.
>
> What the gate required, for the record: the August 28 roadmap audit routes the
> Career Decision Evidence Check to Videos 3, 5, 11, 17, 18 and 21, states
> "publish only when the page is live and usable," and marked Video 3 a **hard
> publication hold until the page is live**. That hold is now lifted.
>
> **Still required before Video 3 is uploaded or scheduled:** one signed-out
> production check of https://temidayoafonja.com/career-decisions — that it loads
> for a visitor who is not signed in and is not holding a preview link. This is
> Temidayo's check to run; it is recorded in Video 3's README, publishing package
> and editor brief. The same check is worth running before Video 5 publishes.

That entry rested on a page-live confirmation alone. The 1 September production
verification above replaces it on evidence, not on scope: the signed-out check it
names is now part of the routine publishing SOP rather than an open blocker.

### `temidayoafonja.com/keep-the-proof` — PASSED, 1 September 2026

**Temidayo independently checked the page signed out and confirmed it is live**,
displaying Keep the Proof, "A 60-Minute Career Evidence System", $49 pricing and
the Gumroad purchase route. This is no longer an open production blocker for
Video 4 or Video 7.

Recorded honestly: I could not verify it independently. Outbound requests to
temidayoafonja.com are refused by this environment's egress proxy. The status
above rests on Temidayo's signed-out check, not on one I ran.

The routine pre-publication signed-out link check stays in the publishing SOP
for every video that carries the URL.

### Other standing gates

| Gate | Applies to |
|---|---|
| ~~Confirm `temidayoafonja.com/keep-the-proof` is live~~ **PASSED, 1 Sep 2026** | Videos 4 and 7 |
| Chapter timestamps set from the real export, not the package estimates | All |
| End-screen elements set at upload (see each package's QA README) | All |

---

## Package status

| # | Package | Recording scripts | Thumbnail |
|---|---|---|---|
| 1 | slides, reveal deck and thumbnail **unchanged and authoritative** | **H.I.T. content APPROVED** — corrected package pending final verification | `DON'T START FROM ZERO` — approved production direction |
| 2 | slides, reveal deck and thumbnail **unchanged and authoritative** | **FINAL + LOCKED FOR RECORDING**, commit `d6883dd` | final, approved |
| 3 | slides, reveal deck and thumbnail **unchanged and authoritative** | **FINAL + LOCKED + CLEARED TO PUBLISH**, commit `c961b63` | Final A approved; Final B archived |
| 4 | slides, reveal deck and thumbnail **unchanged and authoritative** | **H.I.T. content + package APPROVED** — not yet final, see the note below | approved |
| 5 | slides, reveal deck and thumbnail **unchanged and authoritative** | **FINAL + LOCKED FOR RECORDING**, commit `51496ba` | approved |
| 6 | Slides 1–11 and thumbnail **unchanged**; Slide 12 Watch Next title corrected | **FINAL + LOCKED FOR RECORDING** | task closed — finalising in Canva |
| 7 | slides, reveal deck and thumbnail **unchanged and authoritative** | **REOPENED UNDER H.I.T.** — not yet revised, not locked | concept approved: `MAKE INVISIBLE WORK VISIBLE`, gesture version |
| 8 | slides, reveal deck and thumbnail **unchanged and authoritative** | **REOPENED UNDER H.I.T.** — not yet revised, not locked | leading direction: `YOUR EXPERIENCE STILL COUNTS` |

### Locked recording scripts

**The earlier Videos 4 to 8 lock is superseded.** Those five were locked at
commit `de4363c` and handed off as `Video_4-8_FINAL_Recording_Materials.zip`,
with canonical spoken-word counts V4 1,221 · V5 1,639 · V6 1,649 · V7 1,472 ·
V8 1,514. Temidayo has since reopened all of them under the H.I.T. standard.
**That instruction supersedes the `de4363c` lock.** Those packages remain in the
repository as historical reference material and are no longer the authoritative
recording scripts. Videos 5 to 8 are **not** to be described as locked for
recording merely because the older packages still exist.

Video 2 is locked separately at commit `d6883dd` under the H.I.T.
first-30-second standard: `deliverables/video-2-slides/hit-final/`. 105 spoken
paragraphs, 1,131 words, 13 slide markers mapping to the unchanged 13-slide
deck. Four standalone Shorts, and editor instruction held in two clearly
labelled EDITOR ONLY briefs, out of every recording document.

**Video 2's working chapter timestamps are deliberately estimates.** They are
not to be recalculated before recording. The editor replaces them with actual
timestamps from the finished edit before publication. Greater precision now
would be false precision, since the new opening and Temidayo's delivery will
change the timing.

Video 3 is locked at commit `c961b63`: `deliverables/video-3-slides/hit-final/`.
**FINAL + LOCKED + CLEARED TO PUBLISH** once recording, edit and upload QA are
complete — the Career Decision Evidence Check gate is satisfied.
108 spoken paragraphs, 1,205 words, 13 slide markers mapping to the unchanged
13-slide deck. Four standalone Shorts, and editor instruction held in two
clearly labelled EDITOR ONLY briefs, out of every recording document.

The approved archive is `Video_3_HIT_FINAL_Recording_and_Shorts_Package.zip`,
thirteen user-facing files, SHA-256
`2455a0d08105e3148215191e62ead6204c8e4cdf896525592a2983b8c14ea177`.

**Video 3's working chapter timestamps are estimates**, on the same terms as
Video 2's. The editor replaces them with actual timestamps from the finished
edit before publication.

Video 1's H.I.T. rebuild is built at `deliverables/video-1-slides/hit-final/`
and awaits approval. 111 spoken paragraphs, 1,356 words, 13 slide markers
mapping to the unchanged 13-slide deck; the 22-frame reveal deck is unchanged
too. Four standalone Shorts, and editor instruction held in two clearly
labelled EDITOR ONLY briefs, out of every recording document. It is a
**replacement** package: the currently published Video 1 and its published
description stay untouched until the replacement is recorded, edited, reviewed
and uploaded.

Video 4 is **FINAL + LOCKED FOR RECORDING** at
`deliverables/video-4-slides/hit-final/`; the packaged files are those of commit
`e2d405f`, and the canonical source-file verification passed on 1 September
2026. 124 spoken paragraphs, 1,322 words,
11 slide markers mapping to the unchanged 11-slide deck; the reveal deck
(26 frames) is unchanged. Four standalone Shorts, and editor instruction held in
two clearly labelled EDITOR ONLY briefs.

| Video 4 | |
|---|---|
| Title | How to Explain Your Career Change |
| Thumbnail | YOUR CAREER MAKES SENSE |
| Current authoritative script | Video 4 H.I.T. rebuild |
| Canonical spoken word count | 1,322 |
| Previous script | 1,221 words |
| Status of previous script | SUPERSEDED by the H.I.T. rebuild |
| CTA | Keep the Proof |
| Watch next | Should I Make an Internal Move? 3 Questions to Decide |

**This supersedes Video 4's earlier locked script.** Videos 4 to 8 were locked
at commit `de4363c` with Video 4 at 1,221 words. Temidayo instructed a full
H.I.T. rebuild on 1 September 2026; the new package replaces that script for
Video 4 only. Videos 5 to 8 were subsequently reopened under H.I.T. as well; their `de4363c` packages are historical reference material.

**Source verification — PASSED, 1 September 2026.** Video 4's script arrived
first as message text and was hand-transcribed into the package, so a literal
check against the canonical source was held open. Temidayo then supplied
`Video_4_Code_Prompt_HIT_Final.txt` (SHA-256
`9d66cce6a94117542e1f1e514a1fc18d86e1543371f9a0c47146e96a641bc3e1`), archived at
`deliverables/video-4-slides/hit-final/_source/`.

The text between the BEGIN/END APPROVED VIDEO 4 SCRIPT fences was extracted and
compared literally, with **no normalisation of any kind**. Both comparisons are
an **exact match**: the teleprompter script minus its slide markers, and the
clean reading script, each equal the canonical source across all 124 paragraphs
— every word, punctuation mark, apostrophe, quotation mark, em dash,
capitalisation and paragraph order. 8,057 characters on all three sides, and an
identical SHA-256 of the joined spoken text
(`bcbfab8720a5fb4a…`). The 11 slide-marker names and their positions match
exactly. The hand-transcription risk is closed.

No packaged file changed as a result of this verification. All 12 packaged files
still match their recorded checksums, none differs from the reviewed commit
`e2d405f`, the archive was not rebuilt, and its SHA-256 is retained:
`5ca42003ff3c100d5afb2d071e87d418abe6d7777b6f45d956d5830ab46104a0`.

### Gate history — `/career-decisions`

The gate is satisfied. These documents still carry the original blocking
language, each now marked `GATE SATISFIED — production journey verified before
launch, 1 September 2026` beside it. Nothing was deleted.

| Document | What it said |
|---|---|
| `thumbnail-system-audit/FINAL_EXPRESSION_AND_COHERENCE_AUDIT.md` | route "still does not exist"; blocks Video 3 |
| `video-3-slides/VIDEO_3_CHANGELOG_v1.1.md` | route "still does not exist"; marked a publication blocker |
| `video-3-slides/VIDEO_3_SLIDE_QA_v1.0.md` | "Build the /career-decisions destination. It does not exist today." |
| `video-3-slides/VIDEO_3_SLIDE_QA_v1.1.md` | route "Flagged, not verified"; "would 404 today" |
| `video-3-slides/VIDEO_3_UPLOAD_COPY_v1.1.md` | Publication blockers §1, the CTA route |
| `video-3-slides/VIDEO_3_PRODUCTION_HANDOFF_v1.1.md` | §1 "Build the /career-decisions destination", publication blocker |
| `video-3-slides/thumbnail/VIDEO_3_THUMBNAIL_STATUS_v1.2.md` | "This blocks publication" |
| `video-5-slides/Video_5_Final_QA_README.txt` | "PUBLICATION GATE — STILL OPEN", page "IS NOT LIVE" |
| `video-5-slides/Video_5_First_Pass_QA_README.txt` | "PUBLICATION GATE — REQUIRES ACTION", page "IS NOT LIVE" |

**Two places were left untouched on purpose.** The locked Video 3 H.I.T. package
(`video-3-slides/hit-final/`) carries the gate wording in `README_FINAL.txt` and
in the publishing package, and Temidayo approved that wording as part of a
locked archive with a published SHA-256. Editing it would break the checksums
and the lock for a status change. The wording there is now satisfied by this
entry; the package is unchanged and its archive hash stands. The same applies to
`video-5-slides/build/*.py`, which are slide build sources rather than status
documents.

### Video 5 — CTA gate

Video 5's primary CTA is the Career Decision Evidence Check. The former
statement "do not publish until the Career Decision Evidence Check page is live"
is **SATISFIED**. The URL is retained unchanged. Video 5 is reopened under H.I.T.; its `de4363c` script is historical reference
material, not the authoritative recording script. Nothing in it changed for this
status update.

### Standards recorded

`CAPABILITY_FORMATION_YOUTUBE_STANDARDS.md` carries the **Evergreen search
title and conversational opening standard**, with Videos 4 to 8 as the approved
reference set. Video 2's H.I.T. rebuild follows the same first-three-seconds
discipline.

**Slide wording — reviewed and intentionally retained.** Slides 5 and 6 use the
conceptual heading "Name what the work built." The spoken script addresses the
viewer directly with "Name what your work built." No slide change is required.
Temidayo reviewed and resolved this on 1 September 2026: the spoken wording
addresses the individual viewer, the slide heading names the broader conceptual
step, and slides do not change merely because spoken wording becomes more
conversational.

### Series position — authoritative state, 1 September 2026

Set by Temidayo. This section governs; where an older note elsewhere in this
file disagrees, this section is current.

#### Video 1 — How to Change Jobs Without Starting Your Career Over

**v3.1 CAREER EVIDENCE STARTER PATCH APPLIED. NOT YET LOCKED — one item
outstanding.** 1 September 2026.

The wording "roughly eighteen years" is **approved**. It is **not** an open
issue and is not a pending decision.

**The Capability Formation Field Kit CTA is SUPERSEDED for this video** by the
live Free Career Evidence Starter, `https://temidayoafonja.com/career-evidence-starter`.
Video 1 carries ONE primary CTA. The Field Kit product itself is unchanged and
remains the CTA for the videos that route to it.

The v3.1 patch changed exactly two things in the spoken script: the slide
marker `[SLIDE: Capability Formation Field Kit]` became
`[SLIDE: Career Evidence Starter]`, and the three-paragraph Field Kit CTA block
became the approved three-paragraph Starter block. Verified against the v3.0
canonical: those four paragraphs are the only ones that differ, at consecutive
positions. Canonical spoken count **1,329** across 111 paragraphs and 13
markers. All 35 QA checks pass. Every DOCX rendered and visually inspected.

Slide 12 and reveal frame 21 carry the authorised CTA text correction. Main
`slide12.xml` and reveal `slide21.xml` are the only changed parts; slides 1-11
and 13 and the other 21 reveal frames are byte-identical. 13 main slides, 22
reveal frames. The four Short recording scripts and the Shorts editor brief are
byte-identical to v3.0 and were deliberately not rewritten.

A separate description-only document now exists for Video 1, matching the
convention used for Videos 6 to 8.

Package ZIP SHA-256:
`b582e820c52d82af45b37e4d68928922d31758fd1a454ff3d2719713f940cb2b`
Sibling checksum: `Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256`
Description-only DOCX:
`9c4f251fe67f979a248d0df549009cf1e87fcc9c12e5af5a9ef9e2d7e5d70ce6`
The earlier v3.0 archive `c49fcc42…` is superseded.

**OUTSTANDING BEFORE LOCK — CTA artwork.** Slide 12 and reveal frame 21 still
carry the two Capability Formation Field Kit page images (cover and the "Part
Two: Optionality" interior page, whose footer reads *The Capability Formation
Field Kit*). They must be replaced with the real Career Evidence Starter
artifact — Starter cover in front, Portable Proof Line page visible behind,
warm cream background. The artifact was shown in the conversation but has not
been supplied as a file, and no substitute may be fabricated. Video 1 is **not
locked** until those two images are replaced byte-identically, with checksums.

Video 1 is **not** to be marked FINAL from a tracker update alone. Temidayo's
advisor will independently review the corrected deliverable before lock.

Thumbnail text: `DON'T START FROM ZERO`. No new thumbnail decision is to be
inferred beyond the approved existing production direction.

#### Video 2 — Is Your Job Making You Less Marketable?

**FINAL + LOCKED FOR RECORDING.** H.I.T. package approved.

#### Video 3 — 3 Things to Do Before Quitting Your Job

**FINAL + LOCKED + CLEARED TO PUBLISH** once recording, edit and upload QA are
complete. Career Decision Evidence Check gate: **SATISFIED**.

#### Video 4 — How to Explain Your Career Change

**FINAL + LOCKED FOR RECORDING.** Canonical source-file verification **PASSED**.

| | |
|---|---|
| Title | How to Explain Your Career Change |
| Thumbnail | YOUR CAREER MAKES SENSE |
| Canonical spoken count | 1,322 |
| CTA | Keep the Proof |
| Keep the Proof production gate | PASSED |
| Watch next | Video 5 — Should I Make an Internal Move? 3 Questions to Decide |
| Long-form H.I.T. rebuild | FINAL + LOCKED |
| Four standalone Shorts | FINAL + LOCKED |
| Long-form EDITOR ONLY brief | FINAL |
| Shorts EDITOR ONLY brief | FINAL |
| Publishing package | FINAL |
| Slides | UNCHANGED |
| Reveal deck | UNCHANGED |
| Thumbnail | UNCHANGED |
| Previous 1,221-word script | SUPERSEDED |
| Final package ZIP SHA-256 | `5ca42003ff3c100d5afb2d071e87d418abe6d7777b6f45d956d5830ab46104a0` |

The package was not rebuilt or altered for the lock; no packaged file changed.

#### Video 5 — Should I Make an Internal Move? 3 Questions to Decide

**FINAL + LOCKED FOR RECORDING.** Locked at commit `51496ba`:
`deliverables/video-5-slides/hit-final/`.

| | |
|---|---|
| Title | Should I Make an Internal Move? 3 Questions to Decide |
| Thumbnail | YOU MAY NOT NEED TO LEAVE |
| Canonical spoken count | 1,403 |
| Primary CTA | Career Decision Evidence Check |
| CTA URL | https://temidayoafonja.com/career-decisions |
| CTA production gate | SATISFIED |
| Watch next | Video 6 — Are You Growing—or Just Being Given More Work? |
| Long-form H.I.T. rebuild | FINAL + LOCKED |
| Four standalone Shorts | FINAL + LOCKED |
| Long-form EDITOR ONLY brief | FINAL |
| Shorts EDITOR ONLY brief | FINAL |
| Publishing package | FINAL |
| Canonical source verification | PASSED IN SAME BUILD PASS |
| Slides | UNCHANGED (12 main slides) |
| Reveal deck | UNCHANGED (25 frames) |
| Thumbnail | UNCHANGED |
| Final package ZIP SHA-256 | `3b9fcc52a0c79cae2b25da04f72e8f6eee34e270dad6f3b4bd731ac4ffa09854` |
| Sibling checksum | `Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256` |

141 spoken paragraphs. The source comparison against
`Video_5_Code_Prompt_HIT_Final.txt` ran inside the build pass and passed: exact
match on both scripts across all 141 paragraphs, 8,588 characters on all three
sides, identical SHA-256 of the joined spoken text, and all 12 slide-marker
names and positions matching. The canonical prompt is archived at
`video-5-slides/hit-final/_source/`.

**The previous `de4363c` Video 5 script and package are SUPERSEDED as recording
authority** by this H.I.T. rebuild. Retain them only as historical reference.

The package was not rebuilt or altered for the lock; no packaged file changed.

The old exception that delayed personal proof until roughly 1:35 is superseded;
the proof now sits in the opening.

#### Video 6 — Are You Growing—or Just Being Given More Work?

**FINAL + LOCKED FOR RECORDING.**

| | |
|---|---|
| Title | Are You Growing—or Just Being Given More Work? |
| Thumbnail | MORE WORK ≠ GROWTH |
| Canonical spoken count | 1,721 across 190 spoken paragraphs |
| CTA | Capability Formation Field Kit |
| Watch next | How to Show Your Impact at Work When You Built It From Scratch |
| Main slides | 12 — slides 1 to 11 UNCHANGED, slide 12 Watch Next title corrected only |
| Reveal frames | 23 — frames 1 to 22 UNCHANGED, frame 23 Watch Next title corrected only |
| Thumbnail asset | UNCHANGED |
| Four Shorts | FINAL + LOCKED |
| Description-only document | FINAL, SHA-256 `db08023929f08f7f6639b2d9fad26d0c787538865df13523f0cede5816e7fab2` |
| Package ZIP SHA-256 | `f3cf7b36167524d222852ba8b720ea65e10f1e9ade45065e4412cc3b1c999387` |
| Sibling checksum | `Video_6_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256` |
| Canonical source verification | **PASSED** |

**Canonical source verification — PASSED.** Against the uploaded
`Video_6_Code_Prompt_HIT_Final.txt` (SHA-256 `4ef0e003dc109534…`, archived at
`video-6-slides/hit-final/_source/`): exact match on both scripts across all 190
paragraphs, 10,521 characters on all three sides, identical SHA-256 of the
joined spoken text, and all 12 slide-marker names and positions matching, with
no normalisation applied.

**Slide 12 correction.** "How to Prove the Value of Work That Had No Blueprint"
became "How to Show Your Impact at Work When You Built It From Scratch", set as
four lines — HOW TO SHOW YOUR / IMPACT AT WORK / WHEN YOU BUILT / IT FROM
SCRATCH — inside the existing 29pt Montserrat Bold text box. Exactly one XML
part changed per deck, the only structural delta being one added run with
identical formatting plus one line break.

**Description copy boundary.** Both the publishing package and the separate
description-only document now place the editorial emoji instruction above an
explicit `COPY-READY YOUTUBE DESCRIPTION — BEGIN` marker. Their public copy is
**identical**, 36 paragraphs, all seven approved emoji markers intact, no
`[INSERT]` placeholder anywhere. The archive was rebuilt for the publishing-
package change and carries a new hash; the earlier `2c815849…` no longer
applies.

#### Video 7 — How to Show Your Impact at Work When You Built It From Scratch

**FINAL + LOCKED FOR RECORDING.** 1 September 2026.

Built from the canonical `Video_7_Code_Prompt_HIT_Final.txt`. Canonical source
verification passes on all seven comparisons: 186 spoken paragraphs, **1,632
words**, 12 markers with names and positions matching. All 45 QA checks pass.
Every DOCX was rendered and visually inspected.

**Six authorised slide corrections, text only.** Design, typography, palette,
layout and box positions unchanged throughout.

| Slide | From | To |
|---|---|---|
| 1 | YOU WERE NOT IMPROVING SOMETHING. / YOU WERE THE BEFORE. | BUILDING WHILE OPERATING / THE INFRASTRUCTURE WAS STILL MATURING. |
| 2 | FOUNDATIONAL WORK HAS NO PRIOR STATE. / The instrument that would have recorded it did not exist yet. | FOUNDATIONAL WORK CAN BE HARD TO SEE. / Sometimes the mechanism that would have recorded it was still maturing. |
| 4 | DOCUMENT THE ABSENCE YOU WALKED INTO. | RECONSTRUCT THE STARTING CONDITION |
| 5 | WHAT DID NOT EXIST? and eight absence claims | WHAT WAS STILL MATURING? and the seven approved categories |
| 10 | What did not exist. / What you created underneath the output. / What is different now—and how someone else could tell. | What was incomplete, inconsistent, or difficult before the work? / What did you help put in place, improve, or make more usable? / What changed afterward because of the work? |
| 12 | HOW TO EXPLAIN A NONLINEAR CAREER WITHOUT LOOKING UNFOCUSED | HOW TO EXPLAIN YOUR CAREER CHANGE |

Changed XML parts — main `slide1, slide2, slide4, slide5, slide10, slide12`;
reveal `slide1, slide2, slide4, slide8, slide9, slide10, slide11, slide20,
slide21, slide22, slide24`. Main slides 3, 6, 7, 8, 9 and 11 and the other
thirteen reveal frames are byte-identical. 12 main slides, 24 reveal frames.

No absolute-absence framing remains anywhere in either deck.

Final ZIP SHA-256:
`898434afee0ab6ee26dfbe36f8d3c169baec4d99b07126719547cef84b83a10d`
Sibling checksum: `Video_7_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256`
Description-only DOCX (outside the ZIP), unchanged across every correction
pass: `6d608afb31be46be9f84808ec3dce4861d586f470f7bd0037205bc2ee2803815`

Thumbnail direction is **already approved**: `MAKE INVISIBLE WORK VISIBLE`. The
gesture version, with Temidayo's open palm presenting the headline, is the
selected direction. The concept is not undecided.

Operational item still outstanding: ensure the approved Canva PNG is eventually
inserted **byte-identically** into the complete final Video 7 production package,
with a checksum.

#### Video 8 — How to Switch Industries Without Starting Over

**FINAL + LOCKED FOR RECORDING.** 1 September 2026.

The final public title is **How to Switch Industries Without Starting Over**.
The earlier working title "How to Move Into a New Industry Without Starting
Over" is superseded and is not used anywhere in the package.

Built from the canonical `Video_8_Code_Prompt_HIT_Final.txt`. Canonical source
verification passes on all seven comparisons: 174 spoken paragraphs, **1,563
words**, 12 markers with names and positions matching. All 43 QA checks pass.
Every DOCX was rendered and visually inspected. 12 main slides, 24 reveal
frames.

**Slide 5 correction stands as approved.** Text only; visual system,
typography family, colours, composition and hierarchy unchanged.

| From | To |
|---|---|
| It feels like a competence gap. It is an information gap. | IT CAN FEEL LIKE A COMPETENCE GAP. / SOME CONTEXT CAN BE RESEARCHED. / SOME MUST BE LEARNED THROUGH EXPOSURE. |

Changed XML parts — main `slide5` only; reveal `slide11` only. Reveal frame 10
is the title-only build of the same slide and never carried the line. Every
other slide and frame is byte-identical.

**Slide 12 is intentional and stays unchanged.** `CONTINUE THE SERIES / CAREER
PORTABILITY / CAREER PIVOTS · INTERNAL MOVES · GROWTH` is a deliberate series
and playlist end card, **not** a stale Watch Next error. It carries no video
title by design. The spoken script and the end-screen carry the route to Video
9. Do not "correct" this slide in any future pass.

Approved proof: roughly eighteen-year cross-context career, eight
industries/sectors, CISM preparation and first-attempt non-pass. No exam score,
date, further attempt or later passing result is stated anywhere.

Final ZIP SHA-256:
`672c8ccc4c0f2c02b2c2a01e5fd21554da2e6aaac84ec8e99a98cf791fdcdd74`
Sibling checksum: `Video_8_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256`
Description-only DOCX (outside the ZIP):
`c64b4d6313d67d6169136137be82acf177af257ba1712d573a09a4ad3dfb5c94`

Thumbnail direction: `YOUR EXPERIENCE STILL COUNTS`.

### Memorable-shorthand standard — recorded 2 September 2026

A standing rule now governs teaching devices across the series: at most one
device per video, recognition before the letters, 2 to 4 letters only when
they reflect a real method, no acronym in the title by default, repeated two
or three times, every part explained in plain language, shown once in a
restrained visual, and what/why/when/where taught before or alongside how.
Factual discipline and one primary CTA are preserved. The full rule and the
locked **3 Cs of Career Evidence** (Capture, Clarify, Carry) are recorded in
`CAPABILITY_FORMATION_YOUTUBE_STANDARDS.md`.

Per-video devices: Video 1 keeps its three practices and Video 4 keeps the
three-sentence career explanation — **the 3 Cs must not be added to either**.
Video 6's device is **the CAR test (Complexity, Authority, Return)** and Video
8's is **the 3 Cs of an industry change (Capability, Context, Credential)**.

### Final pre-recording patch pass — Videos 1, 4, 6, 8

Requested 2 September 2026. **Three of the four patches cannot start.** The
master instruction requires each patched script to be derived by applying the
exact replacements in that video's PATCH file to its SOURCE file, and forbids
hand-transcription. The bundle
`Final_PreRecording_Patches_Videos_1_4_6_8_for_Code.zip` did not arrive; only
the master file and the Video 1 SOURCE were received.

| Video | Patch | State |
|---|---|---|
| 1 | Career Evidence Starter CTA | Script, documents and Slide 12 text **already applied** in v3.1. Blocked only by the Starter artwork. |
| 4 | Replace Keep the Proof with the free Career Evidence Starter | **Not started — PATCH_Video_4_Career_Evidence_Starter.txt missing.** |
| 6 | Name and repeat the CAR test | **Not started — PATCH_Video_6_CAR_Test.txt missing.** |
| 8 | Name and repeat the 3 Cs of an industry change | **Not started — PATCH_Video_8_Three_Cs.txt missing.** |

Videos 4, 6 and 8 remain FINAL + LOCKED at their current verified packages.
Nothing in them was touched. Videos 2, 3, 5 and 7 were not touched.

### Series summary

| State | Videos |
|---|---|
| FINAL + LOCKED FOR RECORDING | 2, 3, 4, 5, 6, 7, 8 |
| v3.1 patch applied — awaiting CTA artwork and independent review before lock | 1 |

Videos 7 and 8 completed their H.I.T. rebuilds on 1 September 2026 and are
locked. Video 1 is the only remaining item in the series. Its v3.1 Career
Evidence Starter patch is applied and verified; it awaits the real Starter
artifact images for Slide 12 and reveal frame 21, and independent advisor
review, before lock.

Videos 5 to 8 are **not** to be reverted to their prior "locked" state merely
because older packages still exist in the repository. The H.I.T. packages named
in the sections above are the authoritative ones.

Outstanding operational item across the series: the approved Video 7 thumbnail
Canva PNG must eventually be inserted byte-identically, with a checksum.

---

## Open items — deferred to a separate thumbnail review

Both are held open at Temidayo's instruction and are not blocking any package.

1. **Video 1 thumbnail.** The approved production direction is
   `DON'T START FROM ZERO`. No new thumbnail decision is to be inferred beyond
   it. The Option A and Option B artwork files remain archived.
2. **Repeated portrait across Videos 4 and 5.** Both finals use
   `photo-portrait-wine.png` in the same layout. Flagged at the time as a
   series-coherence question; no change made.

---

## Series-wide evidence position

The **30% retention improvement** and the **$2M+ estimated turnover cost
avoidance** are excluded from produced scripts and decks.

`docs/claims-ledger.md` records both as "Needs source. No supporting document is
on file in this repository" and attributes them to an enterprise operating role.
The August 28 roadmap audit independently instructs: "Do not attach either
metric to a role or intervention until the relationship is documented."

Open question, for Temidayo rather than for any script: is there a document,
held outside this repository, tying either figure to a specific role and
intervention, with a stated population, baseline and measurement method? If one
exists, the claims ledger should be updated at the same time as any script that
would carry the figure.

---

## What this file is not

Not a substitute for any package's own QA README. Where a detail lives in a
package README, that README governs; this file records only what spans more
than one video.
