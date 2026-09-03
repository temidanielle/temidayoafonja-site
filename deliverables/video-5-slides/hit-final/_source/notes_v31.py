# -*- coding: utf-8 -*-
"""Video 5 v3.1 speaker/editor notes. Notes parts only: no slide XML, no media.

Timings are script-derived working estimates at 145 wpm for the 1,980-word
direct-address script (about 13:39 total)."""

NOTES=[
# 1 Core Distinction
"""Timing: approximately 0:46.

Bring this up only after the H.I.T. opening has fully landed: the hook, SAME
COMPANY / DIFFERENT WORK, "Let me show you what this looked like for me" and
the maternity-return proof, then the three questions.

State one holds the main statement. Reveal the INTERNAL MOVE ≠ AUTOMATIC GROWTH
line after the first statement has been made.

The not-equal sign is drawn rather than typeset: no brand font contains that
glyph.

Direct address: this section carries the one channel-positioning sentence about
experienced professionals, and then returns immediately to "you." Hold on
Temidayo through "And I want to help you do the same here" — do not cover it
with a graphic.

Hold through the organizational turn that follows: an internal move is also a
decision about what the viewer's organization is willing to trust them to do
next. Temidayo carries that on camera; no new slide.""",
# 2 The Three Questions
"""Timing: approximately 2:19.

Reveal one question at a time as each is named. These are the three tests the
whole video runs on, so let each land before the next arrives.

Do not put the answers here. The questions alone.

Do not add an acronym or a second framework. The three questions are the only
memory device in this video.""",
# 3 Question 1
"""Timing: approximately 2:37, holding to about 3:04.

Section break. Hold briefly, then return to presenter.

The point being carried: do not start with the title. Temidayo asks the viewer
to picture an ordinary Monday in the new role and say what would actually be
different. Those are direct questions to one person — keep them attached to her
face.""",
# 4 Access Test
"""Timing: approximately 3:04.

Reveal one line at a time as each is named.

These are the four places to look for change before calling a move real access.

Stay on this slide through the recognition passage at about 3:49: familiarity
can make a weak move look stronger than it is, and the problem may not be the
viewer's capability but whether people can see them beyond the work they are
already known for. Do not build a new graphic for it, and do not imply
discrimination or deliberate resistance.

Also carried here: the limit. A move that does not change the work may still be
right for pay, flexibility, a better manager or stability. Temidayo names those
as legitimate. Do not cut the qualifier.""",
# 5 Question 2
"""Timing: approximately 5:24, holding to about 5:33.

Section break.

This is where Temidayo asks the viewer to be careful with the phrase "more
responsibility." More volume is not more judgment.""",
# 6 More Tasks / More Judgment
"""Timing: approximately 5:33.

Show MORE TASKS first, on its own, while the point about volume is made.

Then contrast with MORE JUDGMENT and let it carry the weight. Temidayo is
explicit that she is not saying the operational task does not matter — she is
asking what the work is forming in the viewer. Keep that distinction intact.

Hold long enough to cover the authority point and the organizational line: a
stretch opportunity becomes developmental when the viewer is trusted with more
judgment, not simply handed more volume.

"So here is what I would ask you" is a relational beat. Stay on Temidayo.""",
# 7 Question 3
"""Timing: approximately 7:43, holding to about 8:07.

Section break.

The viewer's credibility inside the company may not automatically make sense
outside it. Portable evidence does not mean taking confidential material.""",
# 8 Result / Judgment / Range
"""Timing: approximately 8:07.

Reveal Result, Judgment and Range sequentially.

A move becomes more portable when it creates all three. "I want you to be able
to say…" is spoken to one person — do not cut away from her for it.""",
# 9 Decision Read
"""Timing: approximately 9:11.

Reveal rows one at a time. Do not gamify the read.

Two yeses is not a rejection. Temidayo gives the viewer the concrete questions
to ask about the missing dimension.

Zero or one yes may still be exactly the right choice for pay, flexibility,
stability, benefits or a better manager. Keep "you do not have to call every
useful move growth" — it is the closing line of this section.""",
# 10 Conversation Prompts
"""Timing: approximately 10:26.

Progressive reveal, one prompt at a time.

These are for the viewer's internal hiring conversation. Listen for concrete
work, not encouraging adjectives.

Stay with this slide through the organizational read and the limits section:
what the answers say about how the opportunity is designed, that a capable
person can still land in a poorly designed role, the same three questions
applied to an external offer, and — from about 11:59 — the health, safety,
harassment, discrimination, caregiving, location, immigration, energy and
timing boundaries. Temidayo carries all of it; no new slide.

"I want you to compare which option gives you meaningful access…" is a
relational beat. Do not trim it for pace.""",
# 11 CTA
"""Timing: approximately 12:45.

Simple CTA card. No competing offer on screen. Do not add Keep the Proof, the
Capability Formation Field Kit or the Career Evidence Starter.

Note the v3.1 phrasing: "I made the Career Decision Evidence Check to help you
organize the evidence behind that choice." It is offered, not announced. Keep
it that way.

CTA PRODUCTION GATE: SATISFIED. temidayoafonja.com/career-decisions is live and
the core production journey has been verified. Video 5 is not blocked on it.
Retain one normal signed-out link check in the final upload SOP.""",
# 12 Watch Next
"""Timing: approximately 13:14 to the end, about 13:39.

All content is held left of x=1130 so the right side stays clear for YouTube
end-screen elements.

Watch next is Video 6, Are You Growing—or Just Being Given More Work? Use direct
end-screen routing once Video 6 is public; before that, the Career Portability
playlist. Do not leave Subscribe as the only end-screen element.

Closing lines are spoken to one person: "You may not need to leave. But your
next move should increase what you can carry." Stay on Temidayo for both.""",
]

FRAMES=[2,3,1,4,1,2,1,3,3,3,1,1]

def reveal_notes():
    out=[]
    for s,(n,note) in enumerate(zip(FRAMES,NOTES),1):
        for k in range(1,n+1):
            head=("Reveal frame %d of %d — main slide %d."%(k,n,s)
                  if n>1 else "Single-state frame — main slide %d."%s)
            out.append(head+"\n\n"+note)
    return out

if __name__=="__main__":
    r=reveal_notes()
    assert len(NOTES)==12 and len(r)==25, (len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
