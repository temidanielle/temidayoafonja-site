# -*- coding: utf-8 -*-
"""Video 5 v5.0 speaker/editor notes. Notes parts only; no slide XML.
Timings are working estimates at 145 wpm for the 1,804-word script (~12:26)."""
NOTES=[
"""Timing: approximately 0:38.

Do NOT open on this slide. Begin full-screen on Temidayo and let the opening
land: doing well and browsing job adverts anyway, the assumption underneath it,
the reframe, and the offer.

Then this slide carries the proof.

FACTUAL BOUNDARY, exact: about six months after Temidayo came back from
maternity leave in one chapter of her career, her scope expanded beyond the
original box of the role. The meaningful part was being trusted with DIFFERENT
work, not more of the same. No employer, assignment, result, promotion, metric
or conversation. NO maternity or baby imagery — the proof is her saying what
happened.

"More landed on me. That part is easy to describe. But that is not the part
that mattered." Stay on her face for it.

State one holds the main statement; reveal INTERNAL MOVE ≠ AUTOMATIC GROWTH
after it. The not-equal sign is drawn, not typeset — no brand font has the
glyph.""",
"""Timing: approximately 1:18.

The channel line and the three questions.

Reveal one question at a time. These are the only memory device in the video —
no acronym, no second framework, and CAR belongs to Video 6.

Close on the reframe: the point is not whether you moved, it is whether the
move increased what you can carry afterwards.""",
"""Timing: approximately 1:49, holding to about 2:24.

Section break, then straight into the first question.

The instruction is vivid and specific: picture an ordinary Monday four months
in, not the announcement and not the first week. Keep that framing — it is what
stops the viewer answering about the title.""",
"""Timing: approximately 2:24.

Reveal the four access variables one at a time.

Not all four are required. Familiarity is named as an advantage before it is
named as a risk — keep that order, it is what makes the section fair.

At about 3:20 comes the organisational beat, and it is the most delicate thing
in the video: the people who value you most may be the ones least able to
imagine you doing something else, because every time you were excellent in one
shape you made that shape more convincing. "That is not them being unfair."
Do not let an edit turn this into a grievance.

Then the questions to ask, then the limit: a move that does not change the work
can still be right. "I just do not want you calling it development when it is
relief. Both are allowed." Do not cut that.""",
"""Timing: approximately 4:33, holding to about 4:41.

Section break. Hold briefly, then back to presenter.""",
"""Timing: approximately 4:41.

Show MORE TASKS alone first, then bring up MORE JUDGMENT.

The authority point matters as much as the contrast: accountability without
influence is "exposure without ownership, and a well-known way for capable
people to end up looking worse than they are."

Then the three questions to ask the hiring manager, and the closing test — if
the clearest answer is "you will have more to manage", keep asking.""",
"""Timing: approximately 6:45, holding to about 7:09.

Section break.

Credibility inside a company does not automatically make sense outside it. The
people around the viewer watched it happen; someone else did not.""",
"""Timing: approximately 7:09.

Reveal Result, Judgment and Range in order.

The target sentence is the one to protect: "I moved into a new context, I was
trusted to make this kind of call, and here is what was different because of
it." That is what a portable answer sounds like.

Close on the translation test — if you cannot say what the role could prove,
you do not yet know what it will build.""",
"""Timing: approximately 8:08.

Reveal the rows one at a time. Do NOT gamify this — no scorecard treatment, no
tally graphics.

Two yeses is not a rejection; it is something specific to negotiate before
accepting.

Zero or one is not a verdict either. Better pay, better hours, a better
manager, stability while life is complicated — all real reasons. "Just name the
trade honestly. You do not have to call every useful move growth." """,
"""Timing: approximately 9:08.

Progressive reveal, one prompt at a time. Then Temidayo carries a long stretch
on camera — no new slide for any of it.

What the answers say about the organisation. Being capable and still landing in
a badly designed role. The same three questions applied to an external offer.
When an internal move will not fix the problem.

THE SAFETY BOUNDARY sits here and is not optional: if health or safety is at
risk, or the viewer is dealing with harassment or discrimination, they do not
need a mobility strategy — they need to protect themselves and get proper
support. Deliver it plainly, on camera, with captions. Not fine print.

Then the life factors: pay, caregiving, location, immigration status, energy,
timing.

IDENTITY EXIT, at about 11:06: "I want you to be able to read any opportunity —
inside or outside — for what it will actually build in you… Once you can do
that, you stop needing anyone to tell you whether an opportunity is good. You
can see it yourself."

That last sentence is the point of the video. If the edit runs long, cut
something else.""",
"""Timing: approximately 11:33.

Calm and brief. The only invitation in the video, and it is the Career Decision
Evidence Check — not the Field Kit, not Keep the Proof, not the Starter.

It lands AFTER the identity bridge. Keep that order.

The one-sentence exercise comes first, then the offer: "I made the Career
Decision Evidence Check to help you organise the evidence behind that choice."
Offered, not announced.

CTA PRODUCTION GATE: SATISFIED. Retain one signed-out link check in the final
upload SOP.""",
"""Timing: approximately 12:01 to the end, about 12:26.

All content is held left of x=1130 so the right side stays clear for the
YouTube end-screen element.

Watch next is Video 6, Are You Growing—or Just Being Given More Work? Use
direct end-screen routing once Video 6 is public; before that, the Career
Portability playlist. Do not leave Subscribe as the only end-screen element.

Closing lines: "You may not need to leave. But the next move should increase
what you can carry." Stay on her for both.

Hold the final frame for at least 12 seconds.""",
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
    r=reveal_notes(); assert len(NOTES)==12 and len(r)==25,(len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
