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

**SLIDE 13 WATCH NEXT — CORRECTED AND CLOSED, 3 September 2026.** Main slide 13
and reveal frame 23 now read `3 Things to Do Before Quitting Your Job`,
replacing the retired `Before You Quit Your Job, Check These 3 Things`. Text
only: same 40pt Montserrat Bold, same three-line block, same box, same colours,
no media change, end-screen clearance unchanged. Exactly one slide XML part
changed per deck. The editor brief, README and slide-13 speaker note now record
the correction rather than the defect. See the v4.0 section above for the full
verification and for the one derived asset that is deliberately one page
behind, the slide-preview PDF.

Updated Video 2 hashes after the correction: package ZIP
`123ff006a80ef0260e317190ae808668bd89083d8ecbb83f546c43b47615ee3f`,
description-only DOCX
`4b7e255d40759dbc148a096de62f9833b62764599b06227da65e786af8839b81`,
main deck `362d0e51fdbfbddfda6375b0a795b4ffb96a804e9aa1e53e15b95cb205c534af`,
reveal deck `cf7bad865313c5ea090f11ee104e2113c1e16e21119ff7d36cd5e542e41af617`.

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

### Videos 1-5 - v5.1.1 precision pass, verification against the formal prompt, 3 September 2026

`Videos_1-5_v5.1.1_Precision_Cleanup_Code_Prompt.txt` was received and checked
line by line against the deployed packages. Every correction it specifies was
already applied and committed. All fifteen were re-verified directly in the
deployed files: the superseded wording is absent and the corrected wording is
present in each of the five videos, their Shorts, editor briefs, publishing
packages, descriptions and speaker notes.

Preserved and re-confirmed as the prompt requires: the history / systems /
relationships / trust examples in Video 2; the safety boundary, the no-pressure
-to-stay stance, the confidentiality and evidence boundary and the Decision
Check CTA in Video 3; December 2008 and the financial crisis, the
cat-with-nine-lives boundaries, the certification non-pass, the three-sentence
method, the identity exit and the Starter CTA in Video 4; and the result /
judgment / range test plus "Closing that gap is not self-promotion. It is
maintenance." in Video 5.

#### One genuine miss found and fixed

The original U.S. English sweep was case-sensitive and matched only the four
listed words, so four British spellings survived. A case-insensitive sweep
across every script, Short, brief, publishing document, description, speaker
note and slide caught them:

| Where | Old | New | Reaches |
|---|---|---|---|
| Video 4 public description bullet | "orientation, not defence." | "orientation, not defense." | publishing package + description DOCX |
| Video 5 slide 6 speaker note | "THE ORGANISATIONAL LAYER" | "THE ORGANIZATIONAL LAYER" | deck notes only |
| Video 1 slide 6 speaker note | "with colour or emphasis" | "with color or emphasis" | deck notes only |
| Video 2 slide 4 speaker note | "is the centre of this slide" | "is the center of this slide" | deck notes only |

A full case-insensitive sweep now returns clean across every recording,
publishing, description, brief, speaker-note and slide surface. The only
remaining British spellings anywhere are inside each README's own change record,
which quotes the superseded wording deliberately, and the QA script's long-word
allowlist, which is not reader-facing.

#### Rebuild scope - only what actually changed

Package documents were compared by CONTENT, not bytes, because python-docx
re-stamps `docProps` timestamps on every save and would otherwise make all five
packages look changed.

- **Video 4 package rebuilt and redeployed.** "defence" reached the publishing
  package and the description-only DOCX, so both changed. New package ZIP
  `698ae6352efcd0b907c8c3639a7ff2c110bf6adcd74848357521bde9deacf36d`, new
  description DOCX
  `b9bd84500cd8fb35f83e1de5ff2f331123890020c61784abd2cc70323e715787`.
- **Videos 1, 2, 3 and 5 packages NOT rebuilt.** Their packaged documents are
  content-identical, so their deployed ZIPs, `SHA256SUMS.txt` files and sibling
  checksums are untouched and still verify: V1 `c20ba22f…`, V2 `31cca714…`,
  V3 `c06db1bb…`, V5 `4ce583dc…`.
- **Decks: Videos 1, 2 and 5 only**, one main-deck note part and two reveal note
  parts each - exactly the slides carrying the corrected word.
  `NON-NOTES PARTS CHANGED: []` on all six files. Videos 3 and 4 decks untouched.

| Deck | Main | Reveal |
|---|---|---|
| Video 1 | `c051f90c51474a17751ffb4c48843f51592de57a5de1285d0cf0c546cb478e38` | `112c38499b33e1727d8dbdd8154192f64f9203c25323aad5d6d5ffc248000c17` |
| Video 2 | `7e4c731c9a978244b9fa6158d3789f25c1d09daf5d54c393486296749b9a4503` | `de91230060b8aa7bda2105288d0452d119a6ead399ce9ff0b5739af5d07b6a8c` |
| Video 5 | `5f13f656a7b196e8f62bd8f74cf8eea33f743f4a5f2c8631e5d1d8bd9ac067b2` | `749d247141e02fef6585ec8ba9441911582fa1859b8a15400d7dd1f8778bd976` |

All five slide-preview PDFs remain byte-identical. No visible slide copy
contains any corrected phrase or any British spelling, so no slide XML change
was required and nothing needed reporting before proceeding.

#### Re-run in full

230 QA checks pass, 0 failures: canonical comparison, teleprompter/reading
equivalence, direct-address, factual, simple-language, U.S. English, the 13-file
ZIP allowlist, 12-entry `SHA256SUMS.txt` with `sha256sum -c` passing, and
sibling ZIP checksums on all five. Video 4's two changed documents were
re-rendered and hold at 3 pages with healthy trailing pages.

**VIDEOS 1-5 - FINAL + LOCKED. v5.1.1 PRECISION PASS COMPLETE.**

### Videos 1-7 slide-deck handoff - manifest, 3 September 2026

The 14 current authoritative decks were delivered individually under FINAL
names, plus a combined archive. Nothing was rebuilt, revised, regenerated or
redesigned: every delivered PPTX is a **byte-identical copy** of its repository
source, so each SHA-256 below is itself the proof of provenance.

    Videos_1-7_FINAL_Slides_and_Reveal_Builds.zip
    SHA-256 640a896e9cbf9dde3d905c7948e6b41cf1173db3cb49333335dba2fba0c3b033
    15 entries: the 14 PPTX plus SHA256SUMS.txt
    SHA256SUMS.txt inside covers the 14 decks, does not hash itself, and
    carries no archive checksum; that lives in the sibling .sha256.

The archive was built deterministically (fixed 2026-09-03 timestamps, fixed
order, fixed compression), so it is reproducible byte-for-byte from the
repository sources listed below.

| # | Delivered as | Repository source | SHA-256 | Slides / frames |
|---|---|---|---|---|
| 1 | `Video_1_Main_Slides_FINAL.pptx` | `video-1-slides/out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.4.pptx` | `c051f90c51474a17751ffb4c48843f51592de57a5de1285d0cf0c546cb478e38` | 13 |
| 1 | `Video_1_Reveal_Builds_FINAL.pptx` | `video-1-slides/out/Video-1-Reveal-Builds_v2.4.pptx` | `112c38499b33e1727d8dbdd8154192f64f9203c25323aad5d6d5ffc248000c17` | 22 |
| 2 | `Video_2_Main_Slides_FINAL.pptx` | `video-2-slides/out/Video-2-Is-Your-Job-Making-You-Less-Marketable_v1.1.pptx` | `7e4c731c9a978244b9fa6158d3789f25c1d09daf5d54c393486296749b9a4503` | 13 |
| 2 | `Video_2_Reveal_Builds_FINAL.pptx` | `video-2-slides/out/Video-2-Reveal-Builds_v1.1.pptx` | `de91230060b8aa7bda2105288d0452d119a6ead399ce9ff0b5739af5d07b6a8c` | 23 |
| 3 | `Video_3_Main_Slides_FINAL.pptx` | `video-3-slides/out/Video-3-3-Things-to-Do-Before-Quitting-Your-Job_v1.1.pptx` | `552a1db2780adf0756a6c9ad372432d57e84a4eedcc91b8d88c2d5331a45851e` | 13 |
| 3 | `Video_3_Reveal_Builds_FINAL.pptx` | `video-3-slides/out/Video-3-Reveal-Builds_v1.1.pptx` | `8981839522e08409b50b4c17de04df99bc887652e4671b19aa73f915baa6ad44` | 27 |
| 4 | `Video_4_Main_Slides_FINAL.pptx` | `video-4-slides/out/Video_4_Main_Slides.pptx` | `e3d5325b3f297bdc9daa372b7afbbf7dd3ce29fbcfd631b0a20fe4cf4e5aaf04` | 11 |
| 4 | `Video_4_Reveal_Builds_FINAL.pptx` | `video-4-slides/out/Video_4_Reveal_Builds.pptx` | `777626c7f6a8769c0b81258fc9111d7c1754b8bdb3a4d741a18b2079559f66ee` | 26 |
| 5 | `Video_5_Main_Slides_FINAL.pptx` | `video-5-slides/out/Video_5_Main_Slides.pptx` | `5f13f656a7b196e8f62bd8f74cf8eea33f743f4a5f2c8631e5d1d8bd9ac067b2` | 12 |
| 5 | `Video_5_Reveal_Builds_FINAL.pptx` | `video-5-slides/out/Video_5_Reveal_Builds.pptx` | `749d247141e02fef6585ec8ba9441911582fa1859b8a15400d7dd1f8778bd976` | 25 |
| 6 | `Video_6_Main_Slides_FINAL.pptx` | `video-6-slides/out/Video_6_Main_Slides.pptx` | `fcf3051c579d111d36a5357bcf810dd4dfefe4eb92070ce9721587e82dfe91dd` | 12 |
| 6 | `Video_6_Reveal_Builds_FINAL.pptx` | `video-6-slides/out/Video_6_Reveal_Builds.pptx` | `cb8127089944e9885d0411592383153ace98b78ea53dc8e380e587804c1a8f3a` | 23 |
| 7 | `Video_7_Main_Slides_FINAL.pptx` | `video-7-slides/out/Video_7_Main_Slides.pptx` | `2bc375e0a6751ffbe63c477e7ee6018fd88764aef3c4083fd7620dfd6f523e21` | 12 |
| 7 | `Video_7_Reveal_Builds_FINAL.pptx` | `video-7-slides/out/Video_7_Reveal_Builds.pptx` | `b0cee4e9595295a1e1026e8d7eb9dcc86e47f6e38206db805afce0840e89ff05` | 24 |

#### Visible slide content - verified unchanged on all 14 decks

For each deck the most recent commit that changed ANY visible part was found by
unpacking every historical version and diffing OOXML parts, then HEAD was
compared against that commit. In every case the only difference is
`ppt/notesSlides/*`. No `ppt/slides/`, `ppt/media/`, `ppt/theme/`,
`ppt/slideLayouts/`, `ppt/slideMasters/` or `ppt/presentation.xml` part differs.

| Video | Last visible change | Since then |
|---|---|---|
| 1 | `f97e9de` - replace the CTA artwork with the real Career Evidence Starter | notes parts only |
| 2 | `828e819` - correct the stale Watch Next title on slide 13 | notes parts only |
| 3 | `7598f27` - Video 3 v1.1: approved title, script package, upload copy | notes parts only |
| 4 | `f8a4ac7` - Videos 4, 6, 8: final pre-recording patch pass | notes parts only |
| 5 | `cf211bc` - Video 5 mobile-legibility pass on six supporting lines | notes parts only |
| 6 | `0d4aab1` - Video 6: H.I.T. package built; Slide 12 Watch Next corrected | byte-identical |
| 7 | `6d1536c` - Videos 7 and 8: final corrections, both FINAL + LOCKED | byte-identical |

Videos 6 and 7 are byte-identical to their locked state - they were not part
of the v5.0, v5.1 or v5.1.1 passes at all. The research-roadmap commit
`5c0e1ef` appears in no deck's history.

As with the package handoff, the staging directory was not committed: every
PPTX in it duplicated a tracked file, and the archive is reproducible from this
manifest. Video 8 was excluded from this handoff.

### Videos 1-7 production handoff - manifest, 3 September 2026

Seven individual package downloads were delivered to Temidayo, plus each
video's main deck, reveal deck, description DOCX, sibling checksum and
approved thumbnail where one exists.

The delivered ZIPs were **byte-identical copies of the authoritative
repository packages, renamed only** - nothing was rebuilt, so each ZIP's
SHA-256 below is itself the proof of provenance. The staging directory used to
assemble the download set was NOT committed: every file in it duplicated an
already-tracked file, so committing it would have added roughly 14 MB of
duplicate binaries to git history for a one-time delivery. This manifest is the
durable record, and the set is reproducible from it in seconds.

#### Video 1

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_1_FINAL_Recording_and_Shorts_Package.zip` | `video-1-slides/hit-final/Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip` | `c20ba22f395a0051d4af8244256edc966693c927fd390909dede3412361557d0` |
| `Video_1_MAIN_DECK.pptx` | `video-1-slides/out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.4.pptx` | `c051f90c51474a17751ffb4c48843f51592de57a5de1285d0cf0c546cb478e38` |
| `Video_1_REVEAL_BUILDS.pptx` | `video-1-slides/out/Video-1-Reveal-Builds_v2.4.pptx` | `112c38499b33e1727d8dbdd8154192f64f9203c25323aad5d6d5ffc248000c17` |
| `Video_1_YouTube_Description_HIT.docx` | `video-1-slides/hit-final/Video_1_YouTube_Description_HIT.docx` | `152defc2aa200744bd88f327b98187ff76d9a686e6b4ea4b2675c34cd6eb8b44` |
| thumbnail | — | **THUMBNAIL ASSET OUTSTANDING** |

#### Video 2

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_2_FINAL_Recording_and_Shorts_Package.zip` | `video-2-slides/hit-final/Video_2_HIT_FINAL_Recording_and_Shorts_Package.zip` | `31cca714a477ea4f3c2d48abb72a93f008362b7358e323e05e7b2e02f45557fb` |
| `Video_2_MAIN_DECK.pptx` | `video-2-slides/out/Video-2-Is-Your-Job-Making-You-Less-Marketable_v1.1.pptx` | `7e4c731c9a978244b9fa6158d3789f25c1d09daf5d54c393486296749b9a4503` |
| `Video_2_REVEAL_BUILDS.pptx` | `video-2-slides/out/Video-2-Reveal-Builds_v1.1.pptx` | `de91230060b8aa7bda2105288d0452d119a6ead399ce9ff0b5739af5d07b6a8c` |
| `Video_2_YouTube_Description_HIT.docx` | `video-2-slides/hit-final/Video_2_YouTube_Description_HIT.docx` | `99381854008c0e0aed6044f7df95e1f0cb5190a383b81e23f26df55f2085364b` |
| thumbnail | — | **THUMBNAIL ASSET OUTSTANDING** |

#### Video 3

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_3_FINAL_Recording_and_Shorts_Package.zip` | `video-3-slides/hit-final/Video_3_HIT_FINAL_Recording_and_Shorts_Package.zip` | `c06db1bbfddbed4d511b8a7b8fecc5954086e9a121ba3d2309ecc62daa1f0750` |
| `Video_3_MAIN_DECK.pptx` | `video-3-slides/out/Video-3-3-Things-to-Do-Before-Quitting-Your-Job_v1.1.pptx` | `552a1db2780adf0756a6c9ad372432d57e84a4eedcc91b8d88c2d5331a45851e` |
| `Video_3_REVEAL_BUILDS.pptx` | `video-3-slides/out/Video-3-Reveal-Builds_v1.1.pptx` | `8981839522e08409b50b4c17de04df99bc887652e4671b19aa73f915baa6ad44` |
| `Video_3_YouTube_Description_HIT.docx` | `video-3-slides/hit-final/Video_3_YouTube_Description_HIT.docx` | `9398612c460edb87585af814ec17c8a2cfa278ba2c0d1ca0dc73c40c632208dd` |
| thumbnail | `video-3-slides/thumbnail/VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png` | `5f6ae9fdc8df82c31f180a4f856877a6e4b246848429d1a8db9b36b6f4a23dd2` |

#### Video 4

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_4_FINAL_Recording_and_Shorts_Package.zip` | `video-4-slides/hit-final/Video_4_HIT_FINAL_Recording_and_Shorts_Package.zip` | `698ae6352efcd0b907c8c3639a7ff2c110bf6adcd74848357521bde9deacf36d` |
| `Video_4_MAIN_DECK.pptx` | `video-4-slides/out/Video_4_Main_Slides.pptx` | `e3d5325b3f297bdc9daa372b7afbbf7dd3ce29fbcfd631b0a20fe4cf4e5aaf04` |
| `Video_4_REVEAL_BUILDS.pptx` | `video-4-slides/out/Video_4_Reveal_Builds.pptx` | `777626c7f6a8769c0b81258fc9111d7c1754b8bdb3a4d741a18b2079559f66ee` |
| `Video_4_YouTube_Description_HIT.docx` | `video-4-slides/hit-final/Video_4_YouTube_Description_HIT.docx` | `b9bd84500cd8fb35f83e1de5ff2f331123890020c61784abd2cc70323e715787` |
| thumbnail | `video-4-slides/thumbnail/Video_4_Thumbnail_A.png` | `9c6b31ea741965741aacc86f2a3ea15287a199676fc71505bc4e438984a3618f` |

#### Video 5

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_5_FINAL_Recording_and_Shorts_Package.zip` | `video-5-slides/hit-final/Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip` | `4ce583dc8d68520b2d9f9679166ed1ad7470c56b52207520b40e501a757847ff` |
| `Video_5_MAIN_DECK.pptx` | `video-5-slides/out/Video_5_Main_Slides.pptx` | `5f13f656a7b196e8f62bd8f74cf8eea33f743f4a5f2c8631e5d1d8bd9ac067b2` |
| `Video_5_REVEAL_BUILDS.pptx` | `video-5-slides/out/Video_5_Reveal_Builds.pptx` | `749d247141e02fef6585ec8ba9441911582fa1859b8a15400d7dd1f8778bd976` |
| `Video_5_YouTube_Description_HIT.docx` | `video-5-slides/hit-final/Video_5_YouTube_Description_HIT.docx` | `841aa5063e2aadfb80ed54b1c0437afe0ddc66f6f120e993bc0deda9fc8eb501` |
| thumbnail | `video-5-slides/thumbnail/Video_5_Thumbnail_A_Final.png` | `0ff8d7c495d6be648a2913b248ba23ac0dcd8083753ba4e9d2691ea9565af9c1` |

#### Video 6

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_6_FINAL_Recording_and_Shorts_Package.zip` | `video-6-slides/hit-final/Video_6_HIT_FINAL_Recording_and_Shorts_Package.zip` | `4e11cac762dbac072a64c7818a3014aa124499133525910c26dda109a76cbdaf` |
| `Video_6_MAIN_DECK.pptx` | `video-6-slides/out/Video_6_Main_Slides.pptx` | `fcf3051c579d111d36a5357bcf810dd4dfefe4eb92070ce9721587e82dfe91dd` |
| `Video_6_REVEAL_BUILDS.pptx` | `video-6-slides/out/Video_6_Reveal_Builds.pptx` | `cb8127089944e9885d0411592383153ace98b78ea53dc8e380e587804c1a8f3a` |
| `Video_6_YouTube_Description_HIT.docx` | `video-6-slides/hit-final/Video_6_YouTube_Description_HIT.docx` | `52d040580ce0eea6395f0467081b64112fa36638b31b57636851f30339c4a722` |
| thumbnail | — | **THUMBNAIL ASSET OUTSTANDING** |

#### Video 7

| Delivered as | Repository source | SHA-256 |
|---|---|---|
| `Video_7_FINAL_Recording_and_Shorts_Package.zip` | `video-7-slides/hit-final/Video_7_HIT_FINAL_Recording_and_Shorts_Package.zip` | `898434afee0ab6ee26dfbe36f8d3c169baec4d99b07126719547cef84b83a10d` |
| `Video_7_MAIN_DECK.pptx` | `video-7-slides/out/Video_7_Main_Slides.pptx` | `2bc375e0a6751ffbe63c477e7ee6018fd88764aef3c4083fd7620dfd6f523e21` |
| `Video_7_REVEAL_BUILDS.pptx` | `video-7-slides/out/Video_7_Reveal_Builds.pptx` | `b0cee4e9595295a1e1026e8d7eb9dcc86e47f6e38206db805afce0840e89ff05` |
| `Video_7_YouTube_Description_HIT.docx` | `video-7-slides/hit-final/Video_7_YouTube_Description_HIT.docx` | `6d608afb31be46be9f84808ec3dce4861d586f470f7bd0037205bc2ee2803815` |
| thumbnail | — | **THUMBNAIL ASSET OUTSTANDING** |

Thumbnail positions: Videos 3, 4 and 5 have an approved final in the
repository and it was sent. Video 1's A/B selection is still open, Video 2's
artwork still carries the superseded `YOUR SKILLS ARE STALLING` copy, Video 6's
files are explicitly superseded by a pending Canva export, and Video 7 has no
thumbnail asset on file. No substitute was sent for any of the four.

All seven packages verified at delivery: exactly 13 files, 12-entry
`SHA256SUMS.txt`, `sha256sum -c` passing, sibling checksum matching, and no
source, Python, QA, render, temporary or superseded files.

Visible slide content: verified NO change for all seven by unpacking every
version of all fourteen decks across their full git history and diffing OOXML
parts. Across the v5.0, v5.1 and v5.1.1 work only `ppt/notesSlides/*` parts
ever changed; the roadmap commit `5c0e1ef` appears in no deck's history.

Video 8 was deliberately excluded, HELD FOR RESEARCH-ALIGNMENT STRENGTHENING
around the "direct industry experience" pain before it joins a final handoff.

### Forward roadmap - FILED as the current source of truth, 3 September 2026

The missing roadmap was supplied and is now in the repository.

    deliverables/roadmap/
      Capability_Formation_YouTube_Roadmap_1-30_v5.1_Research_Aligned_FINAL.docx
      SHA-256 58c8383965a854c8d7cd5baef7632694478eeaa9d4e3f3848441a923dacfe7b7
      + sibling .sha256
      + README.md  (source-of-truth marker, supersession record, preserved rules)

The filed copy is byte-identical to the file Temidayo supplied. **This is the
CURRENT FORWARD SOURCE OF TRUTH for the Videos 1-30 roadmap.** The earlier gap
note recorded here is closed.

**Superseded:** `YouTube_Audience_and_20_Video_Roadmap_Audit_Aug28_2026.docx`
(SHA-256 `df1754b8698d6ed7a149794893bf9fae21983ff70040da00b24339b611ff0a05`,
copies in `deliverables/video-7-slides/reference/` and
`deliverables/video-8-slides/reference/`) and all earlier September roadmap
versions. The old copies were deliberately NOT deleted - they are the record of
how the roadmap arrived here - and each folder now carries a
`ROADMAP_SUPERSEDED.txt` pointing at the current file. Do not plan or draft from
them, and do not reconcile the new roadmap against them.

#### Filing it changed nothing editorially

The roadmap is an **alignment layer, not a rebuild trigger**. Videos 1-7 are
unchanged by this pass: no script, Short, CTA, thumbnail copy, slide content or
structure was touched, and no video package or deck was rebuilt. Verified by
hash - every Videos 1-8 package ZIP and every deck is byte-identical to the
state committed in 13a3e83.

One positive check worth recording. The roadmap's Videos 1-5 titles and
thumbnail copy were compared field by field against the locked package configs
and match exactly. CTA routes also match: the roadmap's per-video grid uses
shorthand ("Decision Check", "Field Kit") while its own CTA-routing table names
the products in full - Career Evidence Starter, Field Kit, Career Decision
Evidence Check - which is what the packages carry. No conflict to report.

#### Preserved from the roadmap - both audience states

| Moment | Viewer state |
|---|---|
| **ACUTE** | "My context already changed. Help me move." |
| **PREPAREDNESS** | "My context has not changed yet. Help me be ready if it does." |

Serve both. The channel must not collapse into only one.

#### Preserved - the permanent research audit

On every professional-facing video: **What travels? What does not? What can I
prove? What must I relearn?**

#### Preserved - employer legibility as a differentiation seam

Move beyond "How do I describe my transferable skills?" toward:
**"What would make the other side trust that this experience is useful here?"**
Show both sides where relevant - what the professional must prove AND what the
hiring leader, manager or talent system must be able to trust - and always
translate the organizational layer back to what it means for the viewer. Use
ordinary viewer language ("direct experience") before proprietary terminology
when that is the actual pain.

#### Preserved - mandatory strengthening notes for Videos 8, 13, 14, 19, 30

- **Video 8** - must name the "direct experience" pain while preserving
  Capability / Context / Credential.
- **Video 13** - must test search packaging around "How to Get Hired Without
  Direct Industry Experience", WITHOUT auto-replacing the current title. The
  underlying hiring-manager trust argument stays.
- **Video 14 - RESEARCH REQUIRED BEFORE SCRIPTING FACTUAL CONCLUSIONS.** Do not
  script findings until 30 real, current, senior-level job descriptions have
  been collected and documented. The title makes an empirical claim and the
  claim must be earned before it is spoken. No findings from memory, inference
  or plausibility. This marker stays until the research exists.
- **Video 19** - must add employer trust, recency and directness: "My experience
  is real, but is it recent enough or direct enough for this employer?"
- **Video 30** - must distinguish restarting financially, by title, by scope, by
  context, and in actual capability.

#### Preserved - future topic queue, QUEUED NOT SCHEDULED

1. Will I Have to Take a Pay Cut to Change Careers?
2. How to Pivot After a Layoff Without Starting Over
3. Do I Need to Take a Lower Title to Change Industries?
4. How to Prove You Can Do a Job You Haven't Done Before

**Do not insert any of these into the locked 1-30 sequence unless Temidayo
explicitly approves it.**

#### Standing rules the roadmap carries forward

No CTA stacking - route by viewer stage and the job of the video, not by which
product needs promoting. The research does not justify more dramatic packaging;
the gain is the spoken opening naming the lived pain underneath the thumbnail.
First-shelf thumbnail copy stands. Brand stays exact deep navy `#112345` with
the approved cream/gold values and real Temidayo photography. Permanent
boundary: we cannot promise that employers will accept adjacent experience,
eliminate ageism, overcome a weak market, or make every skill transfer. Before
drafting, inspect the roadmap, the latest factual boundaries, current artifacts
and proof, and any newer explicit decision - and never silently resolve a
conflict.

### Videos 1-5 - v5.1.1 PRECISION PASS, 3 September 2026

A narrow correction pass following Temidayo's independent human read of all five
long-form scripts and all twenty Short recording scripts. **This is not a
rewrite and not a v5.2.** Its purpose was to remove a small number of
generalized, unsupported or detached lines that the automated QA did not catch,
and to standardize public-facing spelling to U.S. English.

Nothing changed in: titles, thumbnails, core stories, memory structures, H.I.T.
architecture, belonging sequence, identity exits, CTAs, Watch Next, slide order,
slide design, factual evidence, or overall script structure.

#### The corrections, old to new

**Video 1** - long form needed no substantive change. Short 2 only:

- "When people change job, function or industry, they tend to make one of two
  mistakes." -> "When you change jobs, functions or industries, two mistakes are
  easy to make."

**Video 2** - two universal claims narrowed, in the long form and in Short 1:

- "The better you get at one place, the more of your value gets wrapped inside
  that place." -> "As you get better at one place, some of your value can become
  wrapped in that context." (history / systems / relationships / trust examples
  kept)
- "Your company knows exactly why you matter. They watched you earn it." -> "The
  people around you may know exactly why you matter, because they have seen the
  work."
- Short 1 opening: "There is a question good employees ask themselves quietly."
  -> "You can be very good at your job and still quietly wonder: would anyone
  outside this company understand what I do?"

**Video 3** - three absolutes softened:

- "They take a couple of evenings, and you cannot do them afterwards." -> "They
  are much easier to do while you still have access. Parts of this become harder
  once you leave."
- "your own memory of the detail starts to blur almost immediately" -> "the
  detail can start to blur faster than you expect"
- Short 3: "...is mostly what you did in the two weeks before you handed in your
  notice." -> "...is often what you take the time to capture before your access
  changes." **The invented two-week rule is gone.**

**Video 4** - three speculative or universal lines corrected, plus Shorts 2 and 3:

- "Here is the mistake almost all of us make, and I made it for years." -> "Here
  is a mistake I made for years, and one I still hear often."
- "...the person listening is quietly doing arithmetic about why you left each
  place." -> "...you leave the other person to work out what connects them."
  (Short 2: "When you give somebody only the chronology, you leave them to work
  out what connects the moves.")
- "Anybody experienced enough to be interviewing you has had their own unplanned
  turns." -> "You are not the only person whose path had turns they did not
  choose."

**Video 5** - five overclaims removed, plus Shorts 1, 2 and 4:

- "Job descriptions are written to be approved, not to be accurate." **Deleted.**
  -> "A job description can tell you the broad role. It may not tell you what an
  ordinary Monday will actually ask of you."
- "The story your organisation tells about you is usually a year or two behind
  what you can actually do now." -> "The story people inside an organization tell
  about you can lag behind what you are actually ready to do now." ("Closing that
  gap is not self-promotion. It is maintenance." is kept.)
- "...and most good managers are relieved to be asked them." -> "They are
  reasonable questions to ask a manager, because they show you are taking the
  role seriously."
- "...your judgment will not grow. You will get faster, and more tired." -> "...your
  judgment may not expand very much. You may simply get faster at work you
  already know."
- Short 4: "Be careful with internal moves in particular, because this is where
  they are weakest. A lot of internal work is legible only inside the building."
  -> "Internal moves can be especially easy to describe only in internal
  language. If the outcome only makes sense to people inside the company,
  translate it before you assume the evidence will travel." The result / judgment
  / range test is unchanged.

#### U.S. English standardization

`organisation` to `organization`, `organisational` to `organizational`,
`programme` to `program`, `apologising` to `apologizing`. Two further instances
of the same rule were applied and are recorded here: `travelled` to `traveled`
and `recognises` to `recognizes`. Proper nouns were not altered, and the old
wording quoted inside each README's change record was deliberately left as
written.

#### Verification

**No slide XML change was required.** All ten decks were scanned for every
corrected phrase and for every British spelling before any edit: none appears in
visible slide copy anywhere, so nothing needed reporting or changing. Speaker
notes were regenerated and reapplied - notes-only, with `NON-NOTES PARTS
CHANGED: []` on all ten files. All five slide-preview PDFs remain
byte-identical.

| Video | Words | Runtime | Method arrives | Identity bridge | Slides / reveals |
|---|---|---|---|---|---|
| 1 | 1,722 | 11:52 | 4:14 | 10:28 | 13 / 22 |
| 2 | 1,415 | 9:45 | 2:54 | 8:32 | 13 / 23 |
| 3 | 1,378 | 9:30 | 2:41 | 8:20 | 13 / 27 |
| 4 | 1,364 | 9:24 | 2:46 | 7:51 | 11 / 26 |
| 5 | 1,395 | 9:37 | 2:32 | 8:22 | 12 / 25 |

**230 QA checks pass, 0 failures**, re-run in full: canonical comparison,
long-form/reading equivalence (teleprompter minus markers equals the reading
script, all markers present, no markers in the reading copy), direct-address
measurement, factual QA, simple-language and jargon sweeps, the 13-file
allowlist, 12-entry `SHA256SUMS.txt` with `sha256sum -c` passing, and sibling
ZIP checksums. All 50 documents were re-rendered and inspected; the only thin
trailing page is the Video 1 teleprompter's two-line sign-off page, which is
intentional because recording copy is never compressed.

One regression was caught and fixed during the pass: Video 4's direct-address
measure fell to 59% (threshold 60%) after the interviewer line was softened, so
that line was reworded to address the viewer directly without reintroducing the
overclaim. Video 4 now measures 61%.

#### Videos 1-5 v5.1.1 hashes

| Video | Package ZIP | Description DOCX | Main deck | Reveal deck | Preview PDF |
|---|---|---|---|---|---|
| 1 | `c20ba22f395a0051d4af8244256edc966693c927fd390909dede3412361557d0` | `152defc2aa200744bd88f327b98187ff76d9a686e6b4ea4b2675c34cd6eb8b44` | `b0cc7687ff2357a14fabf2d3c6c82732e93cfc6fdb268d307d91bb22eed9c636` | `f7047626d8d1ec5262e30ed7fce09427eec76d5dc7340ae627b4e9e01500cdf5` | `af4e763c0cdf56f758571b0a655c76aaf92fffabbbac082d49920a21e2c2bf3c` |
| 2 | `31cca714a477ea4f3c2d48abb72a93f008362b7358e323e05e7b2e02f45557fb` | `99381854008c0e0aed6044f7df95e1f0cb5190a383b81e23f26df55f2085364b` | `6b27e196d0ed881ec7f7444a125dfefd950e24cb98d8f4d7974865c2aa5732d9` | `f84fac0af6022d7db5b07452ef0bda494fdcf5e0a11d30482f44fe842dbf8e2d` | `7917d0fafcc77d557d394e59427c37e5d6813cd2c28a210e35a0bc8415a190b0` |
| 3 | `c06db1bbfddbed4d511b8a7b8fecc5954086e9a121ba3d2309ecc62daa1f0750` | `9398612c460edb87585af814ec17c8a2cfa278ba2c0d1ca0dc73c40c632208dd` | `552a1db2780adf0756a6c9ad372432d57e84a4eedcc91b8d88c2d5331a45851e` | `8981839522e08409b50b4c17de04df99bc887652e4671b19aa73f915baa6ad44` | `76f3bd78be4151e9adb5fcdec6b399e2f255feacec6e703deb74175b4e274ec4` |
| 4 | `855d7c9a8973ab71841c639de422c00666ea6e0c1c3828ec4eb6054c523a395e` | `38e5bec84eba543ef777e6b4d73f05edc1f2715cd31eab9fe096656579f43b48` | `e3d5325b3f297bdc9daa372b7afbbf7dd3ce29fbcfd631b0a20fe4cf4e5aaf04` | `777626c7f6a8769c0b81258fc9111d7c1754b8bdb3a4d741a18b2079559f66ee` | `da482aff3ce4d4253c9f0d5417fddb53688207d24d0d9f6a72ca5b6a77f1b832` |
| 5 | `4ce583dc8d68520b2d9f9679166ed1ad7470c56b52207520b40e501a757847ff` | `841aa5063e2aadfb80ed54b1c0437afe0ddc66f6f120e993bc0deda9fc8eb501` | `284d8c57307f4149a0c4508100a282f4b363951de6d0590ae7d3264beac99da1` | `d1d9041aa859c69827b4927909630a0bfd6a9c0e47ed787bb1829eef6e887afd` | `b8443372b168308bc188863be45f903349f63246ab2c7af0a82913dfdfc5bdb1` |

Package filenames and in-document headers now carry `v5.1.1`. The superseded
v5.1 package hashes are recorded in the section below; v5.0 and v4.0 hashes
remain in each README change record.

**VIDEOS 1-5 - FINAL + LOCKED. v5.1.1 PRECISION PASS COMPLETE.**

### Videos 1–5 — v5.1 belonging-first rebuild with the established job-offer / Uber transition story, 3 September 2026

Built under `Videos_1-5_Belonging_Identity_Full_Rebuild_Code_Prompt_v5.1_FINAL.txt`,
which supersedes the v5.0 prompt. **All five spoken scripts were written from
scratch again.** No v5.0 prose was carried forward on the grounds that it had
passed QA; earlier scripts were used only as sources for established facts,
teaching logic, boundaries, CTA, Watch Next and slide mapping.

The substantive change is that **the job-offer / Uber transition story is now
established and approved**, and it becomes the primary belonging beat of
Video 1.

#### The established story, and its boundaries

Temidayo had accepted a job offer; an acquisition rescinded the role before she
ever got to start it. Within a few months she was driving Uber, thinking about
income and uncertainty rather than career strategy. The question underneath it
was one she could not yet name: did everything I had done before this still
count? The role had disappeared. Her experience had not. Later, a recruiter
found her on LinkedIn and asked whether she would consider returning to
Deloitte.

**CAUSALITY BOUNDARY — ABSOLUTE. Driving Uber did not lead to Deloitte.** They
were two parts of the same career-transition chapter. Video 1's script says so
immediately after the recruiter line, and the editor brief, README and deck
notes all carry the instruction that the protective line must stay adjacent to
the recruiter line in the final cut.

Not invented anywhere: a passenger referral, networking-while-driving
causality, the employer of the rescinded offer, the acquiring company, an exact
month, income, a duration beyond "within a few months", or any recruiter
dialogue. The video does not rush to Deloitte as a triumphant ending; it is a
recognition story about income uncertainty and loss of context.

**Video 1 owns the full story.** Video 3 carries a single truthful bridge
sentence — a role she had accepted was rescinded by an acquisition before she
started — used only to make the point that access can change without anybody
choosing it, with the very next line establishing that the viewer's situation
differs because they may be the one choosing. Videos 2, 4 and 5 do not
reference it at all.

| Video | Words | Runtime | Method arrives | Identity bridge | Slides / reveals |
|---|---|---|---|---|---|
| 1 | 1,722 | 11:52 | 4:14 | 10:28 | 13 / 22 |
| 2 | 1,411 | 9:43 | 2:52 | 8:30 | 13 / 23 |
| 3 | 1,377 | 9:29 | 2:41 | 8:19 | 13 / 27 |
| 4 | 1,366 | 9:25 | 2:46 | 7:52 | 11 / 26 |
| 5 | 1,392 | 9:36 | 2:32 | 8:22 | 12 / 25 |

**230 QA checks across the five videos pass, 0 failures.** All twenty Shorts
were rewritten. Every editor brief carries the fourteen required sections
including the identity promise and the identity exit. All five packages are
exactly 13 files with 12-entry `SHA256SUMS.txt`, `sha256sum -c` passing, and a
matching sibling `.zip.sha256`.

**Slides were authorised to change under v5.1 and did not need to.** Every
marker in all five videos was mapped against its deck slide by slide and every
slide still serves the new script — including Video 1 slide 2, which now
carries the job-offer and Uber chapter before it carries the career sequence.
No slide text was changed anywhere. Only notes changed — 62 main and 123 reveal
notes parts across the ten decks — with **no slide XML, media, rels or theme
part touched in any file**, verified by part-level SHA-256 diff.

All five slide-preview PDFs are byte-identical to their previous state.

#### Source status — the Uber gap is CLOSED

The v5.0 record noted that the Uber-driving transition story had no source in
the repository and was therefore not used. **That gap is resolved as of v5.1**
and must not be reported as open again. Two related findings still stand:
"executive 1:1s" is not established and is not used, and no *additional*
personal job-loss story beyond the rescinded offer is established.

#### Videos 1–5 v5.1 hashes

| Video | Package ZIP | Description DOCX | Main deck | Reveal deck | Preview PDF |
|---|---|---|---|---|---|
| 1 | `201be8c1cd02a432b9f926e9f921b2e2509e66bacb8d5832c01fdbe94aec206f` | `3b149f9e6efaabc1e25f851628b3a22543c5b4cf8ab0264bce19c507440d70b4` | `4032d1fdfadcc388af81365af947cf03bfff7c089cc1445706741897120acfad` | `d0d3376b8764aa9eeaca7b3c4c990cad805d1719e0c10fe9e39f1fd72c08e6fc` | `af4e763c0cdf56f758571b0a655c76aaf92fffabbbac082d49920a21e2c2bf3c` |
| 2 | `1c37da1d6f4a918fe18e62587d58969bf4d6e1c3e34c64215fc171d43be222dd` | `48ff07344473c63e24d1e04a036f6a0757f6850198a9d1f04a0776e61caf6923` | `109073c5e7caa0986170d5f19969eeac8b1096fa4451ac06aa67c6d08f9246de` | `ad7e42ef93717c4e0dc0d1449a2a2d6bdce4e8e8a23ed90802e97dea28ef4d12` | `7917d0fafcc77d557d394e59427c37e5d6813cd2c28a210e35a0bc8415a190b0` |
| 3 | `649fba6f8edcf543596f47d5aef9fcd1e9eacbef25059167d8e3db40d45726bb` | `7e0e1d902f0df0e1f0ea782b3e71646dd0c28eec2f34b3ebdd1c43a36e1ce791` | `a5004695b427fde4b2ef77713703b128fba70b73ed68ad712324d148462024ae` | `dc9e40a5137cf2262115977a639063946e87070646b8351f20a4f4574dd566ae` | `76f3bd78be4151e9adb5fcdec6b399e2f255feacec6e703deb74175b4e274ec4` |
| 4 | `81eac17a3e6dcdc36c5bc20489231951c4a74a7002e7d1ba8703ce2f883f9c5b` | `bd516af6538a2bf022124e2702315bae7afbb0926f747ddea499f3d4904a533b` | `46300ad9b721c76b0df5d2caf147cd3d6579452e6cd9fe687a8a01b6674c834b` | `06c5203bded75431042cf147114c13f9a971e3cf0707a117a75b7e7c4c242e31` | `da482aff3ce4d4253c9f0d5417fddb53688207d24d0d9f6a72ca5b6a77f1b832` |
| 5 | `868824de8ee1ea0b43b96310812a27f44f6ea38c562aecb900084e88bdaabf00` | `60f55f1ad687857d963cccadb9f12353035a773dded8bcef5d73ab3f97ce9235` | `c3f7ca7853a7d56d0f10724e78ceffc515bd4f37de4838972983f2e367e831eb` | `8d083e24eb2d6643b947976162e2535f9d77c6c6f7403915decdacb94423193d` | `b8443372b168308bc188863be45f903349f63246ab2c7af0a82913dfdfc5bdb1` |

Prior v5.0 and v4.0 package hashes are preserved in each README change record.
The v5.0 packages listed in the section below are superseded, not deleted from
the record.

**VIDEOS 1–5 — FINAL + LOCKED UNDER BELONGING-FIRST + IDENTITY-TRANSFORMATION +
H.I.T. + DIRECT-ADDRESS REGISTER (v5.1).**

Two Video 2 publishing assets remain open, neither a recording blocker: the
approved Canva thumbnail export for `VALUABLE HERE. STUCK HERE?`, and a clean
slide-preview PDF re-export from an environment that resolves the brand fonts
correctly. Re-rendering the Video 2 preview here returns the brand font in the
wrong weight, so it was deliberately not regenerated.

One further note for the record: the Video 1 teleprompter's final page carries
only the two sign-off lines. Recording copy is never compressed, so this is
intentional and is not a pagination defect.

### Videos 1–5 — v5.0 belonging-first rebuild, 3 September 2026

A genuine editorial reopening under
`Videos_1-5_Belonging_Identity_Full_Rebuild_Code_Prompt_v5.0.txt`. **All five
spoken scripts were written from scratch.** The v4.0 scripts were not carried
forward; they were used only as sources for established facts, teaching logic,
boundaries, CTA, Watch Next and slide mapping.

Every script now moves in the belonging order: the viewer's situation and the
question underneath it, then a line that shows Temidayo has stood there,
then her lived evidence as recognition rather than autobiography, then the
interpretation — and only then the method. Each video ends on who the viewer is
becoming, with the identity bridge placed **before** the CTA so the resource
reads as a next step rather than an advert.

| Video | Words | Runtime | Method arrives | Identity bridge | Slides / reveals |
|---|---|---|---|---|---|
| 1 | 1,727 | 11:54 | 3:09 | 9:22 | 13 / 22 |
| 2 | 1,632 | 11:15 | 2:50 | 10:01 | 13 / 23 |
| 3 | 1,446 | 9:58 | 2:35 | 8:42 | 13 / 27 |
| 4 | 1,548 | 10:40 | 2:28 | 9:31 | 11 / 26 |
| 5 | 1,804 | 12:26 | 1:49 | 11:06 | 12 / 25 |

**230 QA checks across the five videos pass, 0 failures.** All twenty Shorts
were rewritten. Every editor brief carries the fourteen required sections
including the identity promise and the identity exit.

**Slides were authorised to change under v5.0 and did not need to.** Every
marker in all five videos was mapped against its deck and every slide still
serves the new script, so no slide text was changed anywhere. Only notes
changed — 62 main and 123 reveal notes parts across the ten decks — with no
slide XML, media, rels or theme part touched in any file.

#### Three source findings, recorded so they are not re-litigated

The v5.0 brief allowed several stories only if an exact source were
established. The repository was searched and:

1. **The Uber-driving transition story has no source anywhere** in
   `deliverables/` or `docs/`. It was not used.
2. **No specific personal job-loss or layoff story is established** for
   Temidayo. "Layoff" appears only as a generic category and as a future video
   title. Video 3's belonging beat was therefore built from what *is*
   established: her own crossings between function and industry, the real
   relearning that came with them, and what she has observed happen to capable
   people who left a chapter with only exhaustion.
3. **"Executive 1:1s" is not established** and was not used.

If a source for the first two is supplied later, Video 3's opening in
particular could be rebuilt around it.

#### Videos 1–5 v5.0 hashes

| Video | Package ZIP | Description DOCX | Main deck | Reveal deck | Preview PDF |
|---|---|---|---|---|---|
| 1 | `df0bcad5d34ecfe703a9a9501d1cd5970cd8426180db68dc7d5da7ce48bca731` | `118e81fc6192f5a87a83d5da2808c6d4ee03aa668456f3a389c0ef8a3929c77e` | `6f5099f45fcd52c7133397935308f6c23c5ee4cd12f2573ed94a66a87da52dec` | `64ee9a7f2a773cf8f64d22c30249eb44c53311bc54d6c06153ba8cbbddb112f7` | `af4e763c0cdf56f758571b0a655c76aaf92fffabbbac082d49920a21e2c2bf3c` |
| 2 | `87d336b72fb44e32aaeabcec36c224b6b38f14f33304f4309902419481c3f9b8` | `d9d41cf2eff06c8c94b0437c248ffd861661a246af245e90036df9794593cf3d` | `dcef2ae32d28e88db3044f05505f67ae8b83a5ba448ae2ae39623663ddbdce2e` | `6b03213abf25bd603fd6961a4aef0bcd3b1b0c89c33f2e986de5dc4fe445b578` | `7917d0fafcc77d557d394e59427c37e5d6813cd2c28a210e35a0bc8415a190b0` |
| 3 | `2cd564565df7232a6dbf05918f11127dfcea46f299eba1402d68423292ce7b05` | `7e30e2719ff36898d51e8a9dd283639f5bb6c49828b3162d223b6ebf394a6196` | `a21b8b91a6b88003e39e4cfd213b2a1ec727dc768e0206cddf255cadd897dad3` | `d87749b90e9cdd4e590ebda7d53f37841f7ee7b1e553738722fe35dc3d38efa8` | `76f3bd78be4151e9adb5fcdec6b399e2f255feacec6e703deb74175b4e274ec4` |
| 4 | `1f59e2ba88c5c37b9363005030e037ce6d777bd0108d23c29a6f84fb2e2570d2` | `ffebddc71472acb09d57aa1aa165387d0bb931388b08abd649b7b5078279a4f6` | `5eb8c3c4baa400dab32747cd90a24204ae1637b62439dd34ae971b3657573858` | `7130690f9c0e0179c613501f4452188c120eb00957f73150fff361806894cae4` | `da482aff3ce4d4253c9f0d5417fddb53688207d24d0d9f6a72ca5b6a77f1b832` |
| 5 | `28b5facd8cb85b385785be99dec783f29203428ec2205f69ba74ecd4babaaca0` | `a94106338d41817487e80c03fcf223d3d2bb509373950ad60bcd76be6a15a345` | `719b4f510adb820d3c5479270006b481f65d3aea21753854bc8c7f53c933bca7` | `449a44bc35b3f1edc18013d44b5f202af2bf7c08657957d8ca08d92fafa4fe24` | `b8443372b168308bc188863be45f903349f63246ab2c7af0a82913dfdfc5bdb1` |

Prior v4.0 package hashes are preserved in each README change record: Video 1
`fe9d1d6a…`, Video 2 `123ff006…`, Video 3 `3cc786b4…`, Video 4 `245fd3be…`,
Video 5 `da93ca06…`.

**VIDEOS 1–5 — FINAL + LOCKED UNDER BELONGING-FIRST + IDENTITY-TRANSFORMATION +
H.I.T. + DIRECT-ADDRESS REGISTER.**

Two Video 2 publishing assets remain open, neither a recording blocker: the
approved Canva thumbnail export for `VALUABLE HERE. STUCK HERE?`, and a clean
slide-preview PDF re-export from an environment that resolves the brand fonts
correctly.

### Videos 1–5 — v4.0 unified rebuild, 3 September 2026

Rebuilt and reconciled under the compiled v4.0 register: **H.I.T. + direct
address + differentiation + multi-layer hook system + one memorable teaching
structure + factual discipline + one primary CTA**, from
`Videos_1-5_Unified_Final_Rebuild_Code_Prompt_v4.0.txt`.

The pass began with an audit rather than a rewrite. Videos 2, 3, 4 and 5
already passed the direct-address, factual and memory standards, so **their
spoken scripts were carried forward with zero paragraph changes**. Only Video 1
needed a voice revision: it measured 54% second person across viewer-facing
paragraphs and now measures 77%.

| Video | Prior version | Prior spoken | v4.0 spoken | Changed / unchanged paragraphs | Viewer-facing 2nd person | Slides / reveals |
|---|---|---|---|---|---|---|
| 1 | v3.1 | 1,329 | **1,409** | 41 / 70 | 54% → **77%** | 13 / 22 |
| 2 | v3.0 direct address | 1,258 | **1,258** | 0 / 108 | **89%** | 13 / 23 |
| 3 | v3.0 direct address | 1,251 | **1,251** | 0 / 108 | **88%** | 13 / 27 |
| 4 | v3.0 direct address | 1,355 | **1,355** | 0 / 123 | **74%** | 11 / 26 |
| 5 | v3.1 | 1,980 | **1,980** | 0 / 191 | **85%** | 12 / 25 |

**203 QA checks across the five videos pass, 0 failures** (200 at the v4.0 rebuild, plus three added for the Video 2 slide-13 correction). No slide XML, media,
rels or theme part changed in any of the ten decks; only notes parts changed.

What v4.0 newly added to every package: a **first-30-second H.I.T. audit table**
in the long-form editor brief (time, exact spoken line, verbal hook job,
on-screen hook, visual cue, trust beat, viewer payoff), an explicit
**multi-layer hook block** naming all five hook layers, the **restrained emoji
description system** and the **YouTube tag field** in both the publishing
package and the description-only document. Videos 2 and 3 had neither the emoji
system nor a tag field before this pass; Video 4 had only 🧭.

**Video 1's authoritative decks were resolved by hash**, not by filename: the
tracker's recorded deck hashes match `..._v2.4.pptx` and
`Video-1-Reveal-Builds_v2.4.pptx`, so those are authoritative and the earlier
v2, v2.1, v2.2 and v2.3 decks are archive.

#### Video 2 thumbnail — SUPERSEDED, decided 3 September 2026

The authoritative Video 2 thumbnail copy is **`VALUABLE HERE. STUCK HERE?`**.

It **supersedes `YOUR SKILLS ARE STALLING`**, which must not reappear in any
future package, tracker entry or publishing document.

The thumbnail artwork in `deliverables/video-2-slides/thumbnail/` still carries
the old words and is therefore **SUPERSEDED — REPLACE WITH APPROVED CANVA
EXPORT BEFORE PUBLISHING**. No thumbnail was generated or redesigned; the
missing export is not a blocker for the recording package.

#### Videos 1–5 v4.0 hashes

| Video | Package ZIP | Description-only DOCX | Main deck | Reveal deck | Preview PDF |
|---|---|---|---|---|---|
| 1 | `fe9d1d6a59705ff0fd212bc1cac038e9a32e1cf8fb49741477abf0edda3e3c41` | `228e5314198e75acb0a29d046cf074ee50c93a6b840972bd01c2d7075ca1780b` | `bf3dee5f6ae946e1f25219bf13ca4d91250d52c18726e6f855c7bb4f97b490a1` | `27e575044b35348aa112aaeebf09ab50b65b22ba430cb5bd3905f3e998dcf955` | `af4e763c0cdf56f758571b0a655c76aaf92fffabbbac082d49920a21e2c2bf3c` |
| 2 | `123ff006a80ef0260e317190ae808668bd89083d8ecbb83f546c43b47615ee3f` | `4b7e255d40759dbc148a096de62f9833b62764599b06227da65e786af8839b81` | `362d0e51fdbfbddfda6375b0a795b4ffb96a804e9aa1e53e15b95cb205c534af` | `cf7bad865313c5ea090f11ee104e2113c1e16e21119ff7d36cd5e542e41af617` | `7917d0fafcc77d557d394e59427c37e5d6813cd2c28a210e35a0bc8415a190b0` |
| 3 | `3cc786b4ca291d78962dae2f2ae54de3d94c790532791e4d19db65767527d41e` | `bf3d98030c8da161d98e574de511f336b7dd8c1845cddc799f304225be477cd5` | `296d1fc8365fe72c4b68f51d5b7c9d190ac9f29db78beeccde8eb6e22e15ccb8` | `0f76384a14f6f4e1a8e82bc055dfeb2dcc09ce0b35c9c209f0f952f087f0195a` | `76f3bd78be4151e9adb5fcdec6b399e2f255feacec6e703deb74175b4e274ec4` |
| 4 | `245fd3be2e15090fb6f7bf86d0b5eea9332ab7d8f2171d8a9d48bef99463674d` | `4a2f10109a5d5748522b3cfcb049c726475ab76000c3bbd01f200119893252ab` | `cd9b7b80fa2860b313ce19c501b601b2e69f9e6ed538adeeec56957673ff271f` | `04cdf28e49d46d754f7db482697cd36d054f047bda7e64d6caadce955eb5bb1e` | `da482aff3ce4d4253c9f0d5417fddb53688207d24d0d9f6a72ca5b6a77f1b832` |
| 5 | `da93ca06af102bf12f4ae23b445dbcb4bebcd579ba42bfe86e31c5f82e4ad65a` | `d43d8a8a6666c612466aa7706f88a19c79af8fec7b784ed77e27ca86521e4f57` | `a2d30edcc49e6f9b42be74b457aa16e5a049338feff7fe70e388c5c8743d5447` | `a1a85d9d9d3d486e54a6e6832d9ca372e557386969f07d21305b9cb3513e30c7` | `b8443372b168308bc188863be45f903349f63246ab2c7af0a82913dfdfc5bdb1` |

Prior package hashes are preserved in the change record: Video 1
`17e881ea…`, Video 2 `f8ebaa45…`, Video 3 `62af1ca5…`, Video 4 `600bbf40…`,
Video 5 `0067d553…`.

**VIDEOS 1–5 — FINAL + LOCKED UNDER H.I.T. + DIRECT-ADDRESS + DIFFERENTIATION +
MULTI-LAYER HOOK REGISTER.**

#### Video 2 slide 13 — CORRECTED AND CLOSED, 3 September 2026

The stale Watch Next card is fixed. Main slide 13 and reveal frame 23 read

  3 Things to Do Before Quitting Your Job

replacing the retired `Before You Quit Your Job, Check These 3 Things`.

The correction was measured before it was applied and was text only. The three
existing runs were rewritten in place at the same 40pt Montserrat Bold, in the
same three-line block, in the same text box at the same position and size, with
the same colours, no media change and no change to the end-screen clearance on
the right. The widest line moved from 4.655 in to 4.525 in inside a 6.667 in
box, so it fits with more room than before.

Exactly one slide XML part changed in each deck — `ppt/slides/slide13.xml` in
the main deck and `ppt/slides/slide23.xml` in the reveal deck. No other slide,
reveal, media, rels or theme part changed. The spoken Watch Next line was
already correct and is unchanged. The slide-13 speaker note, the editor brief
and the README were updated to record the correction instead of the defect,
which is why the Video 2 package was rebuilt; Videos 1, 3, 4 and 5 were not
reopened and their deck hashes are unchanged.

**One derived asset is deliberately one page behind.** The Video 2
slide-preview PDF was NOT regenerated. Re-rendering it in the current build
environment returns Montserrat in the wrong weight — the published PDF is Bold,
the re-render came back light — and replacing it would change typography that
must be preserved. Page 13 of that PDF therefore still shows the retired title.
The two PowerPoint decks are the authoritative artifacts and both carry the
corrected card. The PDF needs one clean re-export from an environment that
resolves the brand fonts correctly before it is used for review. This is a
review-asset gap, not a recording blocker, and it is recorded in the Video 2
editor brief and README.

**Videos 1–5 status: FINAL + LOCKED UNDER H.I.T. + DIRECT-ADDRESS +
DIFFERENTIATION + MULTI-LAYER HOOK REGISTER.** The only outstanding Video 2
items are publishing assets, not recording blockers: the approved Canva
thumbnail export for `VALUABLE HERE. STUCK HERE?`, and the clean slide-preview
PDF re-export.

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
| FINAL + LOCKED - v5.1.1 PRECISION PASS COMPLETE | 1, 2, 3, 4, 5 |
| FINAL + LOCKED FOR RECORDING | 6, 7, 8 |

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
