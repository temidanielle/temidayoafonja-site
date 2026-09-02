# -*- coding: utf-8 -*-
"""Video 5 v3.0 speaker/editor notes. Notes parts only: no slide XML, no media."""

TIMING=["0:38","1:58","2:14","2:38","4:32","4:39","6:40","7:00","8:00","9:00",
        "11:17","11:45"]

NOTES=[
# 1 Core Distinction
"""Timing: approximately 0:38.

Bring this up only after the H.I.T. opening has fully landed: the hook, SAME
COMPANY / DIFFERENT WORK, the maternity-return proof and the three questions.

State one holds the main statement. Reveal the INTERNAL MOVE ≠ AUTOMATIC GROWTH line
after the first statement has been made.

The not-equal sign is drawn rather than typeset: no brand font contains that
glyph.

Hold through the organizational turn that follows — an internal move is also a
decision the organization is making about what it will trust this person to do
next. That passage is carried by Temidayo on camera, not by a new slide.""",
# 2 The Three Questions
"""Timing: approximately 1:58.

Reveal one question at a time as each is named. These are the three tests the
whole video runs on, so let each land before the next arrives.

Do not put the answers here. The questions alone.

Do not add an acronym or a second framework. The three questions are the only
memory device in this video.""",
# 3 Question 1
"""Timing: approximately 2:14, holding to about 2:38.

Section break. Hold briefly, then return to presenter.

The point being carried: do not begin with the title. Ask what will actually be
different on an ordinary Monday.""",
# 4 Access Test
"""Timing: approximately 2:38.

Reveal one line at a time as each is named.

These are the four things to look for before calling a move real access. If
none of them can be named, the first answer may be no.

Stay on this slide through the recognition passage: familiarity can hide a weak
move, and sometimes the organizational problem is not capability but
recognition. Do not build a new graphic for it and do not imply discrimination
or deliberate resistance.""",
# 5 Question 2
"""Timing: approximately 4:32, holding to about 4:39.

Section break.

This is where more responsibility can be misleading. More volume is not more
judgment.""",
# 6 More Tasks / More Judgment
"""Timing: approximately 4:39.

Show MORE TASKS first, on its own, while the point about volume is made.

Then contrast with MORE JUDGMENT and let it carry the weight. Neither example
makes the operational task unimportant. The distinction is what the work is
forming.

Hold long enough to cover the authority point and the organizational line: a
stretch opportunity is developmental when the person is trusted with more
judgment, not simply handed more volume.""",
# 7 Question 3
"""Timing: approximately 6:40, holding to about 7:00.

Section break.

Internal credibility can be powerful inside one company and surprisingly
difficult to explain outside it. Portable evidence does not mean taking
confidential material.""",
# 8 Result / Judgment / Range
"""Timing: approximately 7:00.

Reveal Result, Judgment and Range sequentially.

A move becomes more portable when it creates all three.""",
# 9 Decision Read
"""Timing: approximately 8:00.

Reveal rows one at a time. Do not gamify the read.

Two yeses is not a rejection. Identify the missing dimension and investigate
whether it can be designed into the move.

Zero or one yes may still be the right choice for pay, flexibility, stability,
benefits or a better manager. Just not a formation case.""",
# 10 Conversation Prompts
"""Timing: approximately 9:00.

Progressive reveal, one prompt at a time.

These are for the internal hiring conversation. Listen for concrete work, not
encouraging adjectives.

Stay with this slide through the organizational read and the limits section:
what the answers say about the opportunity's design, why an internal move can
fail even when the person is capable, the same three questions applied to an
external offer, and the health, safety, harassment, discrimination, caregiving,
location, immigration, energy and timing boundaries. Presenter carries all of
it; no new slide.""",
# 11 CTA
"""Timing: approximately 11:17.

Simple CTA card. No competing offer on screen. Do not add Keep the Proof, the
Capability Formation Field Kit or the Career Evidence Starter.

CTA PRODUCTION GATE: SATISFIED. temidayoafonja.com/career-decisions is live and
the core production journey has been verified. Video 5 is not blocked on it.
Retain one normal signed-out link check in the final upload SOP.""",
# 12 Watch Next
"""Timing: approximately 11:45 to the end, about 12:09.

All content is held left of x=1130 so the right side stays clear for YouTube
end-screen elements.

Watch next is Video 6, Are You Growing—or Just Being Given More Work? Use direct
end-screen routing once Video 6 is public; before that, the Career Portability
playlist. Do not leave Subscribe as the only end-screen element.

Closing lines: you may not need to leave, but the next move should increase what
you can carry.""",
]

# reveal frames per main slide, inspected from the actual reveal deck (25 total)
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
