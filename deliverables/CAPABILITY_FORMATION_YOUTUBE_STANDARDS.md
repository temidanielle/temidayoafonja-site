# Capability Formation — YouTube Production Standards

Project-wide standards for the launch cluster and everything after it. This is the
single home for these values. No other document in `deliverables/` carries recording
or export settings, so nothing here duplicates an existing standard.

Applies to: Video 1, Video 2, Video 3, and future videos on this channel.

## Locked capture and export settings

| | Setting |
|---|---|
| Recording | 4K at 30 fps, if the capture is stable at that resolution |
| Final export | 1080p at 30 fps, highest quality |
| Slides | 1920 x 1080 |
| Audio | 48 kHz, speech normalised strongly enough that it does not come out quiet |

If 4K capture is not stable — dropped frames, overheating, storage pressure — record
1080p at 30 fps rather than an unstable 4K. A clean 1080p master beats a stuttering
4K one, and the export is 1080p either way.

## The single most important improvement

**More light on Temidayo.**

This outranks every other production change on this list. Camera resolution is
already sufficient; illumination is the limiting factor on how the footage reads.

Practical version: put the main light in front of her, not behind or beside. A
window works if she faces it. Avoid a bright window at her back, which makes the
camera expose for the window and leaves her face dark. Fill the shadow side so the
contrast across her face stays gentle.

## Thumbnail standards

Derived from the three launch thumbnails and the coherence audit.

| | Setting |
|---|---|
| Master | 3840 x 2160 PNG, exact 16:9 |
| Upload file | 1280 x 720 JPG, quality 95, progressive, 4:4:4 chroma |
| Upload size ceiling | 2 MB — the three launch files sit at 190 to 211 KB |
| Typeface | Montserrat ExtraBold, headline set flush left in short stacked lines |
| Headline cap height | 240 to 300 px on the 2160-high master |
| Palette | cream `#F5F0E8`, navy `#0F2346`, gold `#C9A84C`, lighter blue `#2C588C` as restrained accent |
| Gold coverage | accent only, never a field — keep under about 4% of the canvas |
| Portrait dominance | 44 to 47% of the canvas |
| Supporting graphic | one per thumbnail, unlabelled, no numbers, no implied statistic |
| Small copy | none |

Every thumbnail must be legible at 200 px wide. That is the recommendation-column
size and the one that decides whether it is read at all.

## Photographic integrity rule

Permitted on a source photograph: crop, mask, restrained exposure adjustment,
colour balance, background removal.

Never permitted: AI face reconstruction, beautification, feature alteration,
synthetic extension of the frame, generated poses, generated hands or gestures,
generated clothing, generated scenes, generated props, or any second person.

A thumbnail may not imply a gesture or setting that was never photographed. If the
image the concept needs does not exist, the concept changes or a real photograph
gets taken. It does not get generated.

Five rejected candidates that broke this rule are preserved as a record at
`deliverables/thumbnail-system-audit/NONCOMPLIANT-DO-NOT-USE/`.

## Expression standard

The face should support the emotional direction of the thumbnail, but it does not
need to mime the headline. Restrained credibility is more on-brand for this channel
than exaggerated creator-style reaction poses.

| | Emotional direction |
|---|---|
| Video 1 | confidence, reassurance — a warm smile is right |
| Video 2 | recognition, reflection — a broad celebratory smile would fight the message |
| Video 3 | caution, consequence — calm, no mimed gesture |

Where a real photograph does not match the needed tone, change the composition, the
crop, the supporting graphic, or use a different verified photograph. Never generate
an expression.

## Known constraint on the photo library

Four usable photographs of Temidayo exist. Three are the same broad-smile session in
the wine top; one is the caramel studio portrait. Videos 2 and 3 therefore share a
portrait.

The most valuable single addition to this project is **more photographs**: calm and
level, in varied wardrobe, plain backdrop, well lit, 2000 px or larger on the short
edge. That would unlock genuinely distinct thumbnails for every future video.

---

## EVERGREEN SEARCH TITLE + CONVERSATIONAL OPENING STANDARD

Recorded 31 August 2026. The governing approach to titles and spoken openings
for every future video on this channel.

**Approved reference set: Videos 4 to 8.** Their titles and first spoken lines
are the worked examples of this standard and are closed for revision.

### Title

1. Begin with an evergreen viewer problem expressed in ordinary language people
   may search on Google or YouTube.
2. The public title should use recognizable search language. Capability
   Formation may provide the distinctive answer, but unfamiliar internal
   framework language should not normally be the search front door.
3. Put the central searchable problem or consequence near the beginning of the
   title.
4. Keep the title accurate, concise and evergreen. Do not chase a TubeBuddy or
   SEO score at the expense of human clarity.
5. Treat TubeBuddy, YouTube results and keyword tools as directional evidence —
   not editorial authority, and not proof of demand.

### Spoken opening

6. Open with a natural first sentence that can be comfortably said in one
   breath, normally within the first three seconds.
7. The opening must sound like something Temidayo would say in a real
   conversation. Avoid proposition-first corporate language, overly structured
   framing, generic "If you have ever…" openings and conspicuous framework
   announcements.
8. The spoken hook should align with the title without merely repeating it.
9. Preferred opening forms:
   - a genuine viewer question;
   - a specific lived moment;
   - an unresolved contradiction;
   - a concise statement that creates immediate recognition.
10. Move quickly from the first line into tension, recognition or a direct
    answer. Give the viewer a clear reason to continue within approximately
    15 to 20 seconds.
11. Introduce lived or documented proof early where it fits naturally.
    Approximately 30 to 45 seconds is preferred, but do not force evidence into
    that window if doing so makes the opening less natural. **Video 5 is the
    approved example of personal proof arriving later, at approximately 1:35.**

### Search, packaging and integrity

12. Use the script naturally to reinforce the title's subject and related search
    language. Do not mechanically repeat an exact keyword.
13. Use the description, corrected captions and meaningful chapter names to
    strengthen search understanding.
14. Let the thumbnail create complementary curiosity. It should not simply
    repeat the full title.
15. Preserve editorial integrity: no invented evidence, unsupported metrics,
    exaggerated outcomes, or claims created merely to strengthen a hook.

### The approved reference set

| Video | Approved title | First spoken line | Spoken words |
|---|---|---|---|
| 4 | How to Explain Your Career Change | "A senior colleague once called me a cat with nine lives." | **1,322** |
| 5 | Should I Make an Internal Move? 3 Questions to Decide | "You may not need to leave your company." | 1,639 |
| 6 | Are You Growing—or Just Being Given More Work? | "Is this actually growth, or am I just being given more work?" | 1,649 |
| 7 | How to Show Your Impact at Work When You Built It From Scratch | "How do you prove something when there was nothing there before you?" | 1,472 |
| 8 | How to Move Into a New Industry Without Starting Over | "Do I really have to start over just because I'm changing industries?" | 1,514 |

Word counts are canonical: spoken paragraphs only, excluding document headers,
length statements, timed block headers, slide markers and production
directions. The counting function is `script/canon.py` in each video's
directory.

**Video 4 was rebuilt under the H.I.T. standard on 1 September 2026.** The
current authoritative Video 4 script is the H.I.T. rebuild at
`deliverables/video-4-slides/hit-final/`, canonical spoken count **1,322**. The
earlier 1,221-word script is **SUPERSEDED** and is no longer current. Its
counting method differs from the other rows in this table: the H.I.T. packages
count spoken paragraphs directly from the package's own `_source/script_text.py`
rather than through `script/canon.py`, which does not exist in the H.I.T.
package layout. The definition of a canonical count is unchanged.

Video 4 record:

| Field | Value |
|---|---|
| Title | How to Explain Your Career Change |
| Thumbnail | YOUR CAREER MAKES SENSE |
| Current authoritative script | Video 4 H.I.T. rebuild |
| Canonical spoken word count | 1,322 |
| Previous script | 1,221 words |
| Status of previous script | SUPERSEDED by the H.I.T. rebuild |
| CTA | Keep the Proof |
| Watch next | Should I Make an Internal Move? 3 Questions to Decide |

Video 4 is **FINAL AND LOCKED FOR RECORDING** as of 1 September 2026.

Its script was verified literally against the canonical source file
`Video_4_Code_Prompt_HIT_Final.txt` — exact match against both the teleprompter
spoken sequence and the clean reading script across all 124 paragraphs and 8,057
characters, with every word, punctuation mark, apostrophe, quotation mark, em
dash, capitalisation and paragraph order matching, all 11 slide-marker names and
positions matching, and no normalisation applied. The full evidence is retained
in `video-4-slides/hit-final/QA_REPORT.json` and in the series tracker.

The standards for Videos 5 to 8 are unchanged.
