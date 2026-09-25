# v2.0.10 change log

Built 25 September 2026. Six decisions applied, all checks re-run.

| Artifact | Version | sha256 |
| --- | --- | --- |
| `PRESENTER_VERSION_..._60MIN_v2.0.10_CANDIDATE.pptx` | **v2.0.10** | `7c1660c63f76c49ce43f747fba01fef7c5be07c549bf92fd7827ac9f5d6ddaed` |
| `Capability_Position_Read_Workbook_60MIN_v2.0.3_CANDIDATE.pdf` | v2.0.3, **unchanged** | `c2bb7f1626a2500305a4b55573dfc92c9b97c41d71f28288eff2c09ea395f8ce` |
| `Capability_Formation_Free_Flagship_SOP_..._v2.0.12_CANDIDATE.docx` | **v2.0.12** | `552053759c886351eb78fb39307e81cd8a89f3bb2c896d0cc17dc1b91e8f02fb` |
| `Free_Flagship_60MIN_v2.0.13_Change_Log_and_QA_Report.docx` | **v2.0.13** | `dc2fa71396fe93a558ee54c653c3ceadff63558a13d30efa2fbbad593a834029` |

The workbook did not change, so it stays at v2.0.3.

## 1. Timing

Seventy-five seconds each for the two definition slides is accepted. **No other
timing changed, so this build changes no time at all.** The build asserts that
the opening block, both seventy-five second windows and the protected twelve
minutes all still read as v2.0.9 left them.

## 2. Three constructions replaced, verbatim

| Slide | Now reads |
| --- | --- |
| Signals around your role | "A participant who sees several at once **is in a position worth testing sooner than ninety days.**" |
| Keep working privately | "**The Field Kit is a private system they can own, revisit, and rerun as conditions change.**" |
| Keep working privately | "**Leave it unmentioned here, on slide 23, and in Q&A. It does not return under that name.**" |

## 3. Banned words

Removed from **nine note instances and one appendix face**. The face now reads
**What translation means**. Four sentences were rewritten where the removal left
them reading badly.

**Your brief said twelve note instances. There were nine.** The other three sat
in the Definitions and Matrix divider notes, which v2.0.9 had already replaced
with "Divider. Advance immediately." They went out with those notes.

| Was | Now |
| --- | --- |
| the work that **actually** occurred inside the evidence window | the work that occurred inside the evidence window |
| someone **genuinely** excellent at the work | someone excellent at the work |
| depends on **genuinely** releasing the people who have enough | depends on releasing the people who have enough |
| confirm it has **actually** stopped | confirm it has stopped |
| the Field Kit if it **genuinely** fits the question (×3) | the Field Kit if it fits the question |
| if a delivery **genuinely** runs ahead | if a delivery runs ahead |
| What translation **actually** means | What translation means |

### The one exception, kept and recorded

> "Looking back six months, the work I do now would have been **genuinely** hard
> for me then."

Kept unchanged. It is statement 6 of the locked twelve-statement instrument and
the workbook carries it verbatim. The QA report records it as a deliberate
exception under the heading **ONE DELIBERATE EXCEPTION**, with the instruction
that any future banned-word sweep must skip it.

The build asserts that exactly one instance of *actually*, *genuinely* or
*honestly* survives in the whole deck and that it is that statement. If the
survivor were anywhere else, the build would fail rather than save.

## 4. Appositives

Untouched, as approved: *Direction, not a plan.* · *Questions to investigate, not
predictions.* · *Phrases, not essays.* · *Privately, and provisionally.*

## 5. Q&A

**Questions & Applications is now visible and is slide 29.** Its face carries
LIVE ONLY, RECORDING OFF and 10 MINUTES. The bare "Q & A" divider is hidden.

This is the one change here with operational weight: the recording-off
instruction is now on the face of the slide the room sees at 50:00, instead of on
a divider that said nothing.

A second, older "Q & A" slide carrying a spoken-boundary quote remains hidden
where it was. You did not mention it and I did not move it.

SOP v2.0.12 follows: the Q&A row's Slides column reads **29**, its facilitator
action now begins "Advance to slide 29, which says LIVE ONLY and RECORDING OFF on
its face", and the prose line that said "advance to the Q&A slide" now names
slide 29.

## 6. Poll slides

The appendix version is kept, with its appendix eyebrow and its anonymity line.
The other is deleted. **The deck goes from 43 slides to 42.**

## Checks, all re-run

| Check | Result |
| --- | --- |
| Banned words in the deck | **1**, and it is the locked statement |
| Em dashes, deck / SOP / report | **0 / 0 / 0** |
| British spellings in the deck | **0** |
| Retired category names, deck or workbook | **0** |
| Overlaps in the opening five minutes | **0** |
| Poll slides | **1**, hidden, the appendix one |
| Visible bare Q & A slides | **0** |
| QA report | **266 of 266 PASS** |

Footer numbers renumbered again, because unhiding Questions & Applications added
a numbered slide. **Twenty-nine numbered core slides.** The close slide still has
no printed number, which is pre-existing and was left alone.

Page counts: deck renders 32 visible pages, SOP 9, QA report 47.

## Still open

1. **Workbook v2.0.3 needs a fresh Acrobat behaviour test.** v2.0.1 in
   `free-flagship-assets/60min-v2.0.1/` is untouched and still holds the tested
   status.
2. **Retention Read still not built**, because the deck does not exist. The spec
   in this folder stands.
3. **The close slide has no printed number.** Pre-existing; say the word and I
   will give it one.
