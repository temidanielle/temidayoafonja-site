# Capability Formation — Series Status Tracker

Series-level record of publication gates, open decisions and outstanding
assets. Kept here so individual video packages do not have to be reopened to
carry a cross-cutting note.

Last updated: 1 September 2026.

---

## Publication gates

### `temidayoafonja.com/career-decisions` — CLEARED, 31 August 2026

**Temidayo confirmed the page is live at https://temidayoafonja.com/career-decisions.**
This gate is closed for Video 3 and Video 5 on that confirmation.

Recorded honestly: I could not verify it independently. Outbound requests to
temidayoafonja.com are refused by this environment's egress proxy
(`connect_rejected`, organization policy), and the route does not appear in the
website source in this repository, so there was nothing here to corroborate it
against either. The status above rests on Temidayo's confirmation, not on a
check I ran.

What the gate required, for the record: the August 28 roadmap audit routes the
Career Decision Evidence Check to Videos 3, 5, 11, 17, 18 and 21, states
"publish only when the page is live and usable," and marked Video 3 a **hard
publication hold until the page is live**. That hold is now lifted.

**Still required before Video 3 is uploaded or scheduled:** one signed-out
production check of https://temidayoafonja.com/career-decisions — that it loads
for a visitor who is not signed in and is not holding a preview link. This is
Temidayo's check to run; it is recorded in Video 3's README, publishing package
and editor brief. The same check is worth running before Video 5 publishes.

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
| 1 | slides, reveal deck and thumbnail **unchanged and authoritative** | **H.I.T. rebuild built — awaiting Temidayo's approval** | **Option A vs B not selected** — open |
| 2 | slides, reveal deck and thumbnail **unchanged and authoritative** | **H.I.T. rebuild approved and LOCKED**, commit `d6883dd` | final, approved |
| 3 | slides, reveal deck and thumbnail **unchanged and authoritative** | **H.I.T. rebuild approved and LOCKED**, commit `c961b63` | Final A approved; Final B archived |
| 4 | slides, reveal deck and thumbnail **unchanged and authoritative** | **H.I.T. rebuild built — awaiting Temidayo's approval** | approved |
| 5 | approved and locked | **approved and locked** | approved |
| 6 | approved and locked | **approved and locked** | task closed — finalising in Canva |
| 7 | approved and closed | **approved and locked** | **outstanding** — approved Canva export carrying `MAKE INVISIBLE WORK VISIBLE` |
| 8 | approved | **approved and locked** | **outstanding** — Canva export carrying `YOUR EXPERIENCE STILL COUNTS` |

### Locked recording scripts

Videos 4 to 8 are locked at commit `de4363c`, handed off as
`Video_4-8_FINAL_Recording_Materials.zip`. Canonical spoken-word counts:
V4 1,221 · V5 1,639 · V6 1,649 · V7 1,472 · V8 1,514.

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

Video 4's H.I.T. rebuild is built at `deliverables/video-4-slides/hit-final/`.
Content and package structure are **approved**; the package is **not yet locked**
— see the source-verification note below. 124 spoken paragraphs, 1,322 words,
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
Video 4 only. Videos 5 to 8 remain locked at `de4363c` and are untouched.

**Source verification — open.** Video 4's script arrived as message text rather
than as a file, so it was hand-transcribed into the package. Temidayo asked for
a literal comparison against `Video_4_Code_Prompt_HIT_Final.txt`. **That file is
not present** in this session's uploads or in the repository, so the check she
specified has not been run and Video 4 is **not marked final**.

A secondary literal check was run against the one machine-recorded copy of the
approved script that does exist — the session transcript's stored copy of
Temidayo's own brief, extracted programmatically between the BEGIN/END APPROVED
VIDEO 4 SCRIPT fences, with no normalisation. Against that source, the
teleprompter script minus its slide markers and the clean reading script are
both an **exact match**: 124 paragraphs, every word, apostrophe, quotation mark,
em dash, capitalisation and paragraph order identical; 8,057 characters on both
sides; identical SHA-256 of the joined spoken text. The 11 marker names and
their positions also match exactly. This is corroboration, not a substitute for
the canonical file Temidayo named.

**Fact boundary carried into every Video 4 document.** The recurring "cat with
nine lives" description is established — one of Temidayo's senior-manager
friends at EY used to joke that she was a "cat with nine lives". The original
conversation that first prompted it is **not** established, is not invented
anywhere in the package, and no cat imagery, animation, sound or reenactment is
permitted.

Video 1's public title and on-screen deck title differ **intentionally** —
"How to Change Jobs Without Starting Your Career Over" versus "How I Changed
Jobs Without Starting My Career Over". The title slide is not to be changed to
match the public metadata title.

**Open for Temidayo, raised at build time.** The approved Video 1 script says
"Over roughly eighteen years". `docs/claims-ledger.md` §6 records a resolved
August 2026 operator decision to use "nearly two decades" on every page, and
verifies that "eighteen years" appears nowhere in the repository. The script
was built exactly as approved and the wording was not altered. The figure is
not inaccurate — the ledger's own date range is 2008 to 2026 — but it is a
consistency conflict with a resolved decision, and it is Temidayo's to settle.

### Packaging convention — approved, applies to future packages

Recording-package archives are built from an **explicit allowlist**, never from
a directory walk. Build scripts, QA utilities and source text are kept beside
the package, never inside it.

`SHA256SUMS.txt` ships inside the archive and covers every other user-facing
file in it. It does not hash itself. The archive's own SHA-256 lives in a
sibling file, `<archive-name>.zip.sha256`, so the copy of `SHA256SUMS.txt`
inside the archive is byte-identical to the one outside it.

Approved by Temidayo on 1 September 2026 and to be used for every package from
here on.

Video 2's package predates this and carries the older convention, where the
on-disk `SHA256SUMS.txt` has a trailing archive-hash line the archived copy
does not. Video 2 is locked and is not being reopened for it.

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

### Next

No Video 3 revision is required unless Temidayo explicitly reopens it.

Nothing is queued for build. What remains open across the series is the
Video 7 and Video 8 Canva thumbnail exports, the Video 1 thumbnail selection,
and Temidayo's signed-out check of the Career Decision Evidence Check page
before Video 3 or Video 5 is scheduled.

---

## Open items — deferred to a separate thumbnail review

Both are held open at Temidayo's instruction and are not blocking any package.

1. **Video 1 thumbnail selection.** Option A and Option B are both built and
   archived; neither is marked final. Outstanding since the three-video launch
   coherence audit.
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
