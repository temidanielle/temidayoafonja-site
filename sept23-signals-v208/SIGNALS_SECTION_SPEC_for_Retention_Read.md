# Signals Worth Watching — build spec for the Retention Read editions

**Status: not built, because the deck does not exist yet.**

A search of this repository on branch `claude/capability-position-read-preview-gmdtws`
and of every asset folder found no Retention Read deck, in either the standard or
the educator edition, and no file, route, page or source script that mentions one.
There is also no Transition Read deck. Nothing was created to stand in for them,
because inventing a deck family would be a far larger decision than adding a
section to one.

So this file is the spec. When the Retention Read is built, these three slides go
in it, and the person building it does not have to come back and ask what was
agreed.

## Where the section goes

Immediately after the state-costs slide and before the move categories. The order
is: read your position, see what each state costs, learn what to watch, then
choose a move. Same placement as the public deck.

## What differs from the public deck

Slides 1 and 3 are **identical** to the public "Stay or Leave?" deck. Only slide 2
changes, and only in two places.

| | Public deck | Retention Read, both editions |
| --- | --- | --- |
| Slide 2 title | Signals around your role | **Questions worth raising with your manager** |
| Slide 2 footer | One signal is something to examine. Several together are worth testing a move. | **Bring one of these to your next development conversation.** |
| Slide 2 items | the five below | the same five, unchanged |

The reason for the change is the audience, not the content. The Retention Read is
employer sponsored. A participant reading these signals in a sponsored session is
not being invited to plan an exit, they are being given language for a
conversation they are already entitled to have. The five items stay exactly as
they are because they are observations, not accusations, and they survive being
said out loud to a manager.

## The three slides, verbatim

### Slide 1

- Eyebrow: `SIGNALS`
- Title: **Signals Worth Watching**
- Subtitle: *Questions to investigate, not predictions.*
- Body, in a pale panel with the gold accent bar: "Your reading describes the last
  ninety days. These signals tell you what to watch between now and your next read."

### Slide 2

- Eyebrow: `SIGNALS`
- Title: **Questions worth raising with your manager**
- No subtitle
- Five numbered items, navy chips:
  1. Your mandate is being absorbed, narrowed, duplicated, or redefined again.
  2. Decisions about your work are being made in rooms you are no longer in.
  3. Your role exists because of one sponsor, and that sponsor's position is changing.
  4. Few people outside your manager would notice if your function disappeared.
  5. The routine parts of your work are getting easier to automate or reproduce.
- Footer line, in rust: **Bring one of these to your next development conversation.**

### Slide 3

- Eyebrow: `SIGNALS`
- Title: **Signals when things feel fine**
- Subtitle: *Compounding is the state most likely to feel fine. A strong position
  still needs renewal.*
- Five numbered items, navy chips:
  1. You cannot name what you are learning right now.
  2. You are being praised for the same things as last year.
  3. Your last unfamiliar problem was more than 90 days ago.
  4. Your evidence has not been updated in a quarter.
  5. People outside your organization have not seen your recent work.
- Footer line, in rust: **Choose two signals to watch before your rescore date.**

## Speaker notes

Take them from the public deck build, `SOURCE_build_deck_v208.py`, constants
`NOTE_A`, `NOTE_B` and `NOTE_C`, with one change on slide 2 for the sponsored
setting: the note must say that these are questions to raise, not evidence to
present, and that a participant should not be encouraged to take a list of five
grievances into a review. One question, brought as a question.

Everything else in the notes carries over unchanged, including the two sentences
that matter most:

- These are questions to investigate, not predictions. Nothing here forecasts a
  layoff, diagnoses an employer or claims anything about the job market.
- Noticing a signal is a reason to gather evidence, never a reason to panic and
  never a reason to leave.

Those two hold with more force in a sponsored room, not less.

## The Transition Read deck

**This section does not go in it.** Those participants are already leaving. A
watch list for a position they are exiting is noise, and the slide about things
feeling fine is worse than noise. If a Transition Read is built, leave the
section out and leave this paragraph in the build notes so nobody adds it later
for symmetry.

## Next-Move Note

If the Retention Read carries a Next-Move Note artifact, it takes the same line
the public workbook now carries on page 8:

> Two signals I will watch before my rescore date: ______ and ______
