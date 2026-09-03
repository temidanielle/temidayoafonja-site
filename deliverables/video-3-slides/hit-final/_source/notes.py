# -*- coding: utf-8 -*-
"""Video 3 v3.0 direct-address speaker/editor notes. Notes parts only.

Timings are script-derived working estimates at 145 wpm (1,251 words, ~8:37).
Every quoted anchor is verbatim from the v3.0 direct-address script."""

NOTES=[
# 1 Title
"""Timing: approximately 0:37 to 0:55.

Do NOT open on this slide. Begin full-screen on Temidayo and let the opening
land first: the hook, the three-check promise, her own perspective on
documented performance and talent systems, and the safety line.

Bring the title up under the channel line: "I'm Temidayo Afonja. I help
experienced professionals understand what they can carry from their work into
whatever comes next, without assuming they have to start from zero. And that is
what I want to help you do before you hand in your notice."

That second sentence is the turn from positioning to relationship. Stay on her
face for it.""",
# 2 Once You Leave, Access Changes
"""Timing: approximately 0:55.

Speak from ideas, calmly. The point is timing, not fear.

STATE THE SAFETY BOUNDARY OUT LOUD, IN FULL, AND DO NOT SOFTEN IT:

"If your health or safety is at risk, or you are dealing with harassment,
discrimination or another urgent threat, nothing in this video is a reason to
delay leaving. Act on that first."

Deliver it humanely and directly. It is not a legal disclaimer and must not be
edited to look like one — no fine print, no red alarm graphic, no cutaway.

Then return to the viewer who has time to think, and say plainly that the rest
of the video is for them.

The closing beat of this section is addressed straight at the viewer: "I am not
trying to make you hesitate. I am trying to make sure you do not leave the
meaning of your own experience behind." """,
# 3 01 — Preserve the Evidence
"""Timing: approximately 2:01, holding to about 2:04.

Section card. Hold briefly, then return to presenter.""",
# 4 What to Keep / What Not to Take
"""Timing: approximately 2:04.

Reveal the left column two items at a time, then bring up the boundary column.

Say the boundary plainly. Confidential information, customer data, employee
data, proprietary documents and anything the employer owns stay with the
employer. Preserving your record does not mean taking their material.

The test to say out loud: if you do not have the right to keep it, do not take
it.

Then give the shape of the record itself, spoken, not on the slide: the
starting condition, what you decided or influenced, what changed, and what
permitted evidence supports that result.

Nothing here needs a screenshot of an employer system. Close on the reassurance
that a filing cabinet is not the goal — enough context to explain the work six
months later is.""",
# 5 02 — Name What Your Work Built
"""Timing: approximately 3:07, holding to about 3:12.

Section card. Hold briefly, then return to presenter.""",
# 6 Problem / Constraint / Judgment / Outcome
"""Timing: approximately 3:12.

Reveal the four prompts one at a time as each is named.

Note the direct-address framing in v3.0: Temidayo says "Say you tell me: 'I
reduced the amount of time an internal process took.' That gives me an
outcome." She is standing in as the listener across the table, and the example
is then turned back on the viewer — "what you may have actually learned to do
was…". Keep her on camera through that exchange so it reads as a conversation,
not a case study.

The example stays generic. No employer, client, system, metric or result.

Close on the two questions she hands the viewer: what did your work prove you
can now do, and where else could that be useful?""",
# 7 03 — Test the Next Move
"""Timing: approximately 4:23, holding to about 4:27.

Section card. Hold briefly, then return to presenter.""",
# 8 Uses Something Proven / Builds Something New
"""Timing: approximately 4:27.

Reveal the two halves, then the three questions.

The two kinds of reset both need room. A deliberate learning curve can be a
very good decision; the risk is repeating the same work behind a new logo.

"A new employer is not automatically a new direction for you." Let that land.

Nothing here should read as discouragement from leaving.""",
# 9 The Three Checks
"""Timing: approximately 5:32.

The consolidation card. Reveal the three in order.

"In that order. Not because leaving is wrong." That qualifier is load-bearing —
this video is not three reasons to stay. Do not cut it.

Do not add a fourth item, an acronym or a slogan. The three checks are the only
memory device in this video.""",
# 10 Decision Reading
"""Timing: approximately 5:51.

Reveal one direction at a time. Keep it provisional. Temidayo is not diagnosing
the viewer and not telling them which direction is correct.

Real constraints stay in: pay, benefits, caregiving and timing legitimately
affect when someone moves.

Say the line as written, in its v3.0 form: "I am not trying to make your
decision slow. I am trying to make it legible to you."

The safety boundary is repeated here, briefly and plainly: a harmful situation
does not need a bridge plan. Do not cut it.""",
# 11 Before You Resign
"""Timing: approximately 7:07.

Reveal the three questions one at a time.

The instruction is concrete and directed at the viewer: do not keep the answers
only in your head, write them down.

Close on the three sentences she wants them to be able to say — what I handled,
what I became able to do, what I need next. Stay on Temidayo for those.""",
# 12 Career Decision Evidence Check
"""Timing: approximately 7:50.

Calm and brief. This is the only invitation in the video, and it is the Career
Decision Evidence Check — not the Field Kit, not Keep the Proof, not the Career
Evidence Starter.

Note the v3.0 phrasing: "that is what I made the Career Decision Evidence Check
for." It is offered, not announced. Keep it that way.

CTA PRODUCTION GATE: SATISFIED. The page is live. One signed-out production
check is still required before Video 3 is uploaded or scheduled: confirm it
loads for a visitor who is not signed in and is not holding a preview link.""",
# 13 Watch Next
"""Timing: approximately 8:14 to the end, about 8:37.

If the move changes role, function, employer or industry, this is the video
that answers what carries across. The card reads "How to Change Jobs Without
Starting Your Career Over", which is the locked Video 1 title and matches what
Temidayo says.

Closing line: "Because leaving one job should not require you to erase
everything your work has already built in you."

Do not summarize this video again.

The right side of the frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds.""",
]

FRAMES=[1,1,1,4,1,5,1,4,1,3,3,1,1]

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
    assert len(NOTES)==13 and len(r)==27, (len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
