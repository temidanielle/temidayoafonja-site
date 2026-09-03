# Capability Formation — Series Status Tracker

Series-level record of publication gates, open decisions and outstanding
assets. Kept here so individual video packages do not have to be reopened to
carry a cross-cutting note.

Last updated: 3 September 2026.

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
| 2 | slides and reveal deck **unchanged**; see the open Slide 13 Watch Next defect | **FINAL + LOCKED UNDER DIRECT ADDRESS**, v3.0 | final, approved |
| 3 | slides, reveal deck and thumbnail **unchanged and authoritative** | **FINAL + LOCKED UNDER DIRECT ADDRESS**, v3.0 | Final A approved; Final B archived |
| 4 | slides, reveal deck and thumbnail **unchanged and authoritative** | **FINAL + LOCKED UNDER DIRECT ADDRESS**, v3.0 | approved |
| 5 | slides, reveal deck and thumbnail **unchanged and authoritative** | **FINAL + LOCKED UNDER DIRECT ADDRESS**, v3.1 | approved |
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

Video 2 is now locked under the **direct-address register** at
`deliverables/video-2-slides/hit-final/` as v3.0: 108 spoken paragraphs, 1,258
words, 13 slide markers mapping to the unchanged 13-slide deck. Four standalone
Shorts, and editor instruction held in two clearly labelled EDITOR ONLY briefs,
out of every recording document. The earlier `d6883dd` H.I.T. lock (105
paragraphs, 1,131 words, no package ZIP) is **superseded** and retained only as
historical reference.

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

**FINAL + LOCKED FOR RE-RECORDING.** v3.1 Career Evidence Starter patch
applied 1 September 2026; CTA artwork corrected 2 September 2026.

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
`17e881ea97774f0d4a9e080f2077b093b6367f6f3ce14e22fe119ceb17a793e6`
(supersedes `b582e820…`; the editor brief and README were rebuilt to record
the artwork correction)
Sibling checksum: `Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256`
Description-only DOCX:
`9c4f251fe67f979a248d0df549009cf1e87fcc9c12e5af5a9ef9e2d7e5d70ce6`
The earlier v3.0 archive `c49fcc42…` is superseded.

**CTA artwork — CORRECTED 2 September 2026.** Slide 12 and reveal frame 21
now carry the real Career Evidence Starter artifact, rendered from the
approved PDF: the Starter cover (page 1) in front and the Portable Proof Line
page (page 5) visible behind, on the warm cream ground. Both renders are
1870x2420, the same pixel dimensions as the Field Kit images they replace, so
every shape position, size and z-order is untouched. Only the two media parts
changed — `ppt/media/image2.png` and `ppt/media/image3.png` in each deck — and
NO slide XML or rels changed in that pass. No Field Kit imagery remains
anywhere in either deck.

**Speaker/editor notes — CORRECTED 2 September 2026.** Both decks carried
stale Field Kit CTA language in the notes. Three corrections were applied
across six notesSlide parts: the cue now reads "Career Evidence Starter
invitation", the exact invitation is the canonical v3.1 spoken CTA verbatim,
and "the only purchase invitation" reads "the only resource invitation". Only
notes XML changed — no slide XML, media, rels or presentation.xml — so the
approved Slide 12 visual is bit-for-bit unchanged. No Field Kit, fieldkit or
keep-the-proof string remains anywhere in either deck.

Deck SHA-256 after the notes correction:
main `fbed816d195b32941c73190b7e1e318699844fbc849fcee106fa9589117a4ce0`,
reveal `169cae1ffcb00b6f9d5fb98f06bf4f1395c7ec8d80a0fd5aa3d47683c117cad3`.
The decks sit outside the 13-file ZIP, so the package hash is unchanged.

Video 1's independent review is **complete**. Temidayo accepted the notes
correction and confirmed the locked status on 2 September 2026.

Authoritative Video 1 hashes:
package ZIP `17e881ea97774f0d4a9e080f2077b093b6367f6f3ce14e22fe119ceb17a793e6`,
description-only DOCX `9c4f251fe67f979a248d0df549009cf1e87fcc9c12e5af5a9ef9e2d7e5d70ce6`,
main deck `fbed816d195b32941c73190b7e1e318699844fbc849fcee106fa9589117a4ce0`,
reveal deck `169cae1ffcb00b6f9d5fb98f06bf4f1395c7ec8d80a0fd5aa3d47683c117cad3`.

Thumbnail text: `DON'T START FROM ZERO`. No new thumbnail decision is to be
inferred beyond the approved existing production direction.

#### Video 2 — Is Your Job Making You Less Marketable?

**FINAL + LOCKED UNDER THE DIRECT-ADDRESS REGISTER — v3.0 DIRECT ADDRESS.**
`deliverables/video-2-slides/hit-final/`.

| | |
|---|---|
| Prior authoritative source | `Video2TeleprompterScriptwithslidemarkers_HIT_v2.0.txt` |
| Prior package | v2.0, unpacked folder, **no ZIP existed** |
| New package | v3.0 direct address, 13-file ZIP created for the first time |
| Title | Is Your Job Making You Less Marketable? |
| Thumbnail | YOUR SKILLS ARE STALLING |
| Primary CTA | Capability Formation Field Kit — https://temidayoafonja.com/fieldkit |
| Watch next | 3 Things to Do Before Quitting Your Job (Video 3) |
| Spoken word count | 1,131 → **1,258** |
| Change report | 62 paragraphs unchanged, 46 rewritten, 0 inserted, 0 removed |
| Direct-address QA | PASSED — 89% of viewer-facing paragraphs in second person |
| Slides | UNCHANGED, 13 main slides |
| Reveal deck | UNCHANGED, 23 frames |
| Notes parts changed | main 13, reveal 23 — no other part changed |
| ZIP SHA-256 | `f8ebaa45f657d5fbd60440a54bde58127c343b15fd0b8956c84d6cf7701e18a9` |
| Description-only DOCX | `50a84e39dfc168972125d75b528ba25cb34adf92c2321ea4797966c11d6af57f` |
| Main deck | `cc6ca0e8914b3f9d2248e6758793171a944c011c292aff2a6e09dd89aa1156d5` |
| Reveal deck | `35131b87a0802f970b674d8214f2be7a2de505e7770b1482f4be3d0e25f023e0` |
| Preview PDF | `7917d0fafcc77d557d394e59427c37e5d6813cd2c28a210e35a0bc8415a190b0` |

The thumbnail value in the revision prompt (`VALUABLE HERE. STUCK HERE?`)
differs from the locked repository value. The prompt itself directs that the
repository value wins, so `YOUR SKILLS ARE STALLING` is unchanged.

Video 2 previously had no package ZIP and no description-only document. Both
were created in this pass, bringing it onto the convention used by Videos 1
and 3 to 8.

**OPEN DECK ITEM — REQUIRES SEPARATE AUTHORISATION.** Slide 13 and reveal frame
23 still read `Before You Quit Your Job, Check These 3 Things`, the RETIRED
Video 3 title. The locked Video 3 title is `3 Things to Do Before Quitting Your
Job`, which is what the script says. This defect pre-dates the direct-address
pass and was not created by it. No slide XML change was authorised in this
pass, so the card was left alone; the editor brief, the README and the slide-13
speaker note all record it and instruct the editor to stay on Temidayo rather
than hold the stale card on screen.

#### Video 3 — 3 Things to Do Before Quitting Your Job

**FINAL + LOCKED UNDER THE DIRECT-ADDRESS REGISTER — v3.0 DIRECT ADDRESS.**
Career Decision Evidence Check gate: **SATISFIED**.
`deliverables/video-3-slides/hit-final/`.

| | |
|---|---|
| Prior authoritative source | `Video3TeleprompterScriptwithslidemarkers_HIT_v2.0.txt` |
| Prior package | v2.0, ZIP `2455a0d08105e3148215191e62ead6204c8e4cdf896525592a2983b8c14ea177` |
| New package | v3.0 direct address |
| Title | 3 Things to Do Before Quitting Your Job |
| Thumbnail | WAIT BEFORE YOU QUIT |
| Primary CTA | Career Decision Evidence Check — https://temidayoafonja.com/career-decisions |
| Watch next | How to Change Jobs Without Starting Your Career Over (Video 1) |
| Spoken word count | 1,205 → **1,251** |
| Change report | 65 paragraphs unchanged, 44 rewritten, 0 inserted, 0 removed |
| Direct-address QA | PASSED — 88% of viewer-facing paragraphs in second person |
| Slides | UNCHANGED, 13 main slides |
| Reveal deck | UNCHANGED, 27 frames |
| Notes parts changed | main 13, reveal 27 — no other part changed |
| ZIP SHA-256 | `62af1ca5d1c2096a61309d7d0529e761c07af2237521c2e18ad51c821e890874` |
| Description-only DOCX | `e0d002cff63a6adaeb24b7b67ed57eaddddbb75f9f58d82053dac04ae7e1fda2` |
| Main deck | `d0c27f682fecac3a3d53ba61c06aef01c39e122dec9de281ff52e4cf827a7544` |
| Reveal deck | `9680a4b50dce3ad9cf78fae70ca474b17f9d49623e05325a5471d95886ada5ae` |
| Preview PDF | `76f3bd78be4151e9adb5fcdec6b399e2f255feacec6e703deb74175b4e274ec4` |

The safety boundary is unchanged in meaning and prominence: it is spoken in the
opening, in full on slide 2, again in the decision reading and again in the
pinned comment. The permitted-evidence boundary — if you do not have the right
to keep it, do not take it — is unchanged. The video remains a cleaner-decision
video, not a case for staying. Slide 13 was inspected and carries the correct
Video 1 title.

Video 3 also gained a description-only document in this pass.

#### Video 4 — How to Explain Your Career Change

**FINAL + LOCKED UNDER THE DIRECT-ADDRESS REGISTER — v3.0 DIRECT ADDRESS.**
`deliverables/video-4-slides/hit-final/`.

| | |
|---|---|
| Prior authoritative source | `Video4TeleprompterScriptwithslidemarkers_HIT_v2.1.txt` |
| Prior package | v2.1, ZIP `6d9e8339a83a463ad231db8d180f6bb27025b07f41fd4bfc914778ea5f602684` |
| New package | v3.0 direct address |
| Title | How to Explain Your Career Change |
| Thumbnail | YOUR CAREER MAKES SENSE |
| Primary CTA | Free Career Evidence Starter — https://temidayoafonja.com/career-evidence-starter |
| Watch next | Should I Make an Internal Move? 3 Questions to Decide (Video 5) |
| Spoken word count | 1,261 → **1,355** |
| Change report | 78 paragraphs unchanged, 44 rewritten, 1 coaching line inserted, 0 removed |
| Direct-address QA | PASSED — 74% of viewer-facing paragraphs in second person |
| Slides | UNCHANGED, 11 main slides |
| Reveal deck | UNCHANGED, 26 frames |
| Notes parts changed | main 11, reveal 26 — no other part changed |
| ZIP SHA-256 | `600bbf407b7d4c7da2d2339d16c9670896c310894588f836db4a8b627cd6a65f` |
| Description-only DOCX | `f96350b54d5f593c4ca088366e8ad710ba07e5f8b1c8ad330178a2174e46429d` |
| Main deck | `b4732a966af9dd587d14cd12544fbbe31fa22ffc26b54ac492bc7c023f73b33a` |
| Reveal deck | `ad74573ee7f47fcd79cc090eb7ec69e0b580eda91b1920b3f278b8464e4aac5a` |
| Preview PDF | `da482aff3ce4d4253c9f0d5417fddb53688207d24d0d9f6a72ca5b6a77f1b832` |

Video 4's second-person share is the lowest of the three because roughly a
third of the script is Temidayo's own first-person career evidence, which is
correct for this video and must not be converted.

**The Video 4 record that previously appeared here was stale.** It recorded
Keep the Proof as the CTA and ZIP `5ca42003…`. That was superseded by the
2 September master pre-recording patch pass, which moved Video 4 to the Free
Career Evidence Starter at v2.1. This entry replaces it. Keep the Proof is NOT
restored, only the direct public landing-page URL is used, the cat-with-nine-
lives fact stays bounded with no employer named and no cat imagery, the
December 2008 financial-crisis context is unchanged, and the
not-everything-transfers boundary is intact.

#### Video 5 — Should I Make an Internal Move? 3 Questions to Decide

**FINAL + LOCKED FOR RECORDING — v3.1 DIRECT-ADDRESS REBUILD.**
`deliverables/video-5-slides/hit-final/`.

| | |
|---|---|
| Canonical instruction | `Video_5_Code_Prompt_Differentiated_Direct_Address_v3.1.txt` |
| Title | Should I Make an Internal Move? 3 Questions to Decide |
| Thumbnail | YOU MAY NOT NEED TO LEAVE |
| Format | Searchable decision + organizational mechanics |
| Voice register | Direct address — one experienced professional across the table, never lecturer to a crowd |
| Canonical spoken count | 1,980 across 191 spoken paragraphs (203 blocks) |
| Estimated runtime | ~13:39 at 145 wpm |
| Memorable device | The three questions (no acronym, no second framework) |
| Primary CTA | Career Decision Evidence Check |
| CTA URL | https://temidayoafonja.com/career-decisions |
| CTA production gate | SATISFIED |
| Watch next | Video 6 — Are You Growing—or Just Being Given More Work? |
| Long-form v3.1 rebuild | FINAL + LOCKED |
| Four standalone Shorts | FINAL + LOCKED, all four rewritten in direct address |
| Long-form EDITOR ONLY brief | FINAL — 12 sections, including the new Direct-address register |
| Shorts EDITOR ONLY brief | FINAL — carries "Direct address is part of the creative" |
| Publishing package | FINAL |
| Description-only DOCX | FINAL, outside the ZIP |
| Canonical source verification | PASSED IN SAME BUILD PASS |
| QA | 64 / 64 PASSED (52 core + 12 direct-address) |
| Slides | UNCHANGED (12 main slides) — no slide XML, geometry, typography, palette or media change |
| Reveal deck | UNCHANGED (25 frames) |
| Speaker notes | UPDATED to v3.1 — 12 main notes parts, 25 reveal notes parts |
| Slide preview PDF | UNCHANGED (verified pixel-identical to a fresh render of the current deck) |
| Thumbnail | UNCHANGED |
| Final package ZIP SHA-256 | `0067d5530c26d2625eec0bcce131ab61cfadba6f438f5febff30d557c04d2b23` |
| Sibling checksum | `Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256` |
| Description-only DOCX SHA-256 | `12cde0558c6109ac3a3d75c8b77f1e34947ccbabf8d128281640831987c3252a` |
| Main deck SHA-256 | `8f6fec230dcd46adf0e57403da48140a23481474132738d37c64956c78669de8` |
| Reveal deck SHA-256 | `ee43aefa88ed77234ffa1392185e10c0e57432d3d7d223c19a5074e6373a89fb` |
| Slide preview PDF SHA-256 | `b8443372b168308bc188863be45f903349f63246ab2c7af0a82913dfdfc5bdb1` |

The literal comparison against the uploaded canonical TXT ran inside the build
pass and passed on every axis: all 203 blocks, 191 spoken paragraphs, 12 slide
markers by name and by position, and both DOCX and TXT forms of the
teleprompter and reading scripts. Teleprompter minus markers equals the reading
script exactly. All four Shorts match the canonical spoken copy verbatim.

**Direct-address result.** No occurrence of "some people", "professionals
often", "people may" or "a person should" anywhere in the long-form, the
Shorts or the public copy. 92 of 124 substantive spoken paragraphs (74%)
address the viewer directly, 56% across all 191 paragraphs — direct enough to
carry the relationship, not so mechanical that every sentence repeats "you".
35 paragraphs carry first-person lived voice. The first-person bridges are
present and counted: "Let me show you" ×1, "I want to help you" ×3, "I want you
to" ×9. "Experienced professionals" appears exactly once, in the
channel-positioning sentence, and the script returns immediately to "you". All
five organizational-mechanics lines are addressed to the viewer. No keynote
markers.

**The v3.0 package (ZIP `f54447a6…`, 1,762 spoken words) is SUPERSEDED as
recording authority**, and `Video_5_Code_Prompt_Differentiated_v3.0.txt` is
superseded as the canonical instruction, by this v3.1 direct-address rebuild.
The v3.0 prompt is retained in `_source/` as
`Video_5_Code_Prompt_Differentiated_v3.0_SUPERSEDED.txt`. The v2.0 H.I.T.
package and the earlier `de4363c` script remain superseded as before.

Only speaker notes changed in the two decks. Part-level diffs confirm that the
12 `ppt/notesSlides/notesSlideN.xml` parts of the main deck and the 25 of the
reveal deck are the only parts that changed in either file — no slide XML, no
media, no rels, no theme.

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

Completed 2 September 2026 from
`Final_PreRecording_Patches_Videos_1_4_6_8_for_Code.zip`. The bundle's own
`SHA256SUMS.txt` verified, and all four SOURCE files were confirmed
byte-identical to the canonical prompts the locked packages were built from.
Every authorised FROM string was found verbatim and consecutively in its
SOURCE before anything was changed. Videos 2, 3, 5 and 7 were not touched.

| Video | Patch | Script diff vs SOURCE | Slides / reveals |
|---|---|---|---|
| 1 | Career Evidence Starter CTA (v3.1) | one merged block: marker + 3 CTA paragraphs | main `slide12`, reveal `slide21` |
| 4 | Keep the Proof → Career Evidence Starter (v2.1) | one merged block: marker + 7 CTA paragraphs → marker + 3 | main `slide10`, reveal `slide25` |
| 6 | The CAR test (v2.1) | three blocks, exactly as authorised | **none** |
| 8 | The 3 Cs of an industry change (v2.1) | three blocks, exactly as authorised | **none** |

Canonical verification passes for all four: each patched script differs from
its SOURCE only in the authorised diff blocks, and all four delivered script
files match the derivation literally. 71 QA checks across Videos 4, 6 and 8
pass. Every DOCX was rendered and visually inspected.

Two documents needed a pagination fix and were retuned to
`compress(1.14, 0.56)`, holding three pages across line-factor 1.06 to 1.20:
the Video 4 publishing package spilled a near-empty fourth page under the
patch, and the Video 6 description document already carried one before it.

Video 4 gained a separate description-only document, so Videos 1 and 4 to 8
now all follow that convention.

### Direct-address voice register — series standard, 3 September 2026

Video 5 v3.1 set the register and Videos 2, 3 and 4 were revised into it in a
single pass. Temidayo speaks to one experienced professional sitting across
from her, never to an abstract audience. Each revision is auditable as a voice
revision rather than a rewrite: no paragraph was deleted, no factual claim was
added, no CTA or Watch Next route moved, and no second framework appeared.

| Video | Prior | New | Unchanged / rewritten paragraphs | Viewer-facing second person |
|---|---|---|---|---|
| 2 | v2.0, 1,131 words | v3.0, 1,258 words | 62 / 46 | 89% |
| 3 | v2.0, 1,205 words | v3.0, 1,251 words | 65 / 44 | 88% |
| 4 | v2.1, 1,261 words | v3.0, 1,355 words | 78 / 44 (+1 inserted) | 74% |
| 5 | v3.0, 1,762 words | v3.1, 1,980 words | rebuilt from canonical v3.1 | 74% |

117 QA checks across Videos 2 to 4 pass. No slide XML, media, rels or theme
part changed in any of the six decks; only notes parts changed.

### Series summary

| State | Videos |
|---|---|
| FINAL + LOCKED UNDER DIRECT-ADDRESS REGISTER | 2, 3, 4, 5 |
| FINAL + LOCKED FOR RECORDING | 6, 7, 8 |
| FINAL + LOCKED FOR RE-RECORDING | 1 |

Videos 7 and 8 completed their H.I.T. rebuilds on 1 September 2026 and are
**Videos 1 to 8 are CLOSED AND READY FOR RECORDING**, confirmed by Temidayo
on 2 September 2026. Video 1's v3.1 CTA patch, its Starter artwork replacement
and its deck notes correction are all applied and verified. No editorial or
visual change is authorised for any of the eight videos before recording
unless Temidayo explicitly reopens something.

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
