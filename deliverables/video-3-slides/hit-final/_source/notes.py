# -*- coding: utf-8 -*-
"""Video 3 v5.0 speaker/editor notes. Notes parts only; no slide XML.
Timings are working estimates at 145 wpm for the 1,446-word script (~9:58)."""
NOTES=[
"""Timing: approximately 0:31 to 0:48.

Do NOT open on this slide. Begin full-screen on Temidayo. The first thing the
viewer must hear is that this is not a video trying to keep them in their job.

"I am not going to try to talk you out of it." Then the refusal to pretend she
knows their situation. Then the real cost: people leave carrying much less than
they earned.

Bring the title up briefly, then go straight to the safety boundary. Do not put
anything between them.""",
"""Timing: approximately 0:48.

THE SAFETY BOUNDARY COMES FIRST, IN FULL, AND IS NOT NEGOTIABLE:

"If your health or your safety is at risk, or you are dealing with harassment
or discrimination, nothing in this video is a reason to wait. Get yourself out
and get proper support. None of what follows is worth a single week of that."

Deliver it plainly and humanely, on camera, with captions. It is not a legal
disclaimer and must not be edited to look like one — no fine print, no red
alarm graphic, no cutaway.

Then the access explanation. The tone is practical, not ominous: afterwards it
is not impossible, just harder and slower and dependent on memory.

The belonging beat sits here — her own crossings, the relearning, and what she
has watched happen to capable people. NO personal job-loss story is established
and none is used. Do not let a visual imply one.""",
"""Timing: approximately 2:35, holding to about 2:38.

Section card. Hold briefly, then back to presenter.

The framework does not arrive until here, at over two and a half minutes. That
is deliberate.""",
"""Timing: approximately 2:38.

Reveal what is yours to keep, then the boundary column.

Say the boundary plainly. Confidential information, customer data, employee
data, proprietary documents, anything the employer owns — it stays with the
employer.

The rule to say out loud: if you do not have the right to keep it, do not take
it.

Then the four lines: where it started, what you decided or influenced, what
changed, what permitted evidence supports it.

Close on why this one is first: do it while you can still check.""",
"""Timing: approximately 3:52, holding to about 3:57.

Section card. Hold briefly, then back to presenter.""",
"""Timing: approximately 3:57.

Reveal the four prompts one at a time.

Temidayo stands in as the listener — "Say you tell me: I reduced the time an
internal process took. That gives me a result. Fine." Keep her on camera so it
reads as a conversation, not a case study.

The example stays generic. No employer, client, system, metric or result.

Close on the two questions she hands over: what did this chapter prove you can
do, and where else would that be needed?""",
"""Timing: approximately 5:15, holding to about 5:19.

Section card. Hold briefly, then back to presenter.""",
"""Timing: approximately 5:19.

Reveal the two halves, then the three questions.

Both kinds of reset need room. The deliberate one is endorsed — "That can be an
excellent decision. I have made it." The trap is the one where the logo changed
and the problems did not.

"A new employer is not automatically a new direction." Let it land.

Nothing here may read as discouragement from leaving.""",
"""Timing: approximately 6:33.

The consolidation card. Reveal the three checks in order.

"In that order. Not because leaving is wrong." That qualifier is load-bearing.
Do not cut it.

No fourth item, no acronym, no slogan.""",
"""Timing: approximately 6:52.

Reveal one direction at a time. Keep it provisional — she is not diagnosing the
viewer or telling them which one is right.

Real life stays in: pay, benefits, caregiving, timing, where you live. The line
"anyone who tells you otherwise is not being serious" protects the viewer from
tidier advice elsewhere. Keep it.

The safety boundary repeats here, briefly: a harmful situation does not need a
bridge plan. Do not cut it.""",
"""Timing: approximately 8:08.

Reveal the three questions one at a time. The instruction is concrete: write
them down, do not keep them in your head.

IDENTITY EXIT, at about 8:42: "I want you to become someone who closes a
chapter properly. Who walks out knowing what it built, what evidence stands
behind it, and what the next thing needs to use and needs to grow."

Then the widening line — do that once and you never arrive at a decision like
this empty-handed again. That is the point of the video. If the edit runs long,
cut something else.""",
"""Timing: approximately 9:11.

Calm and brief. The only invitation in the video, and it is the Career Decision
Evidence Check — not the Field Kit, not Keep the Proof, not the Starter.

It lands AFTER the identity bridge. Keep that order.

Note the phrasing: "that is exactly what I made the Career Decision Evidence
Check for." Offered, not announced.

CTA PRODUCTION GATE: SATISFIED. The page is live. One signed-out production
check is still required before upload or scheduling.""",
"""Timing: approximately 9:35 to the end, about 9:58.

The card reads "How to Change Jobs Without Starting Your Career Over", the
locked Video 1 title, matching what Temidayo says.

Closing line: "Leaving one job should not cost you everything the work built in
you." Stay on her for it.

Do not summarize the video again.

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
    r=reveal_notes(); assert len(NOTES)==13 and len(r)==27,(len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
