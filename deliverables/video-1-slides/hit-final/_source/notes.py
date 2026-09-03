# -*- coding: utf-8 -*-
"""Video 1 v5.0 speaker/editor notes. Notes parts only; no slide XML.
Timings are working estimates at 145 wpm for the 1,727-word script (~11:54)."""

NOTES=[
"""Timing: approximately 0:39 to 1:31.

Do NOT open on this slide. Begin full-screen on Temidayo and let the whole
opening land first: the viewer's situation, the question underneath it, "I know
that question, I have had to answer it more than once", the honest answer, and
the three-practice promise.

Recognition comes before anything is taught. Nothing may cut into that.

Bring the title up under the channel line, then hold for the promise boundary:
"I cannot tell you that everything transfers, because it does not."

That refusal is what makes the rest of the video believable. Do not soften it.

The on-screen deck title and the public YouTube title differ intentionally. Do
not change the title slide to match the public title.""",
"""Timing: approximately 1:31.

The chronology lives on the slide. Temidayo does not read it back.

This is the belonging and lived-proof section. She names the December 2008
accounting degree and the financial crisis exactly as spoken, the real
relearning in every move, going back to school, and preparing for a
professional certification she did not pass on the first attempt.

That non-pass is not a throwaway. It is what earns the "not everything
transfers" boundary, and it is why "I am not being modest, I have paid for that
lesson" works. Do not cut either.

Then the turn: she did not carry the tasks forward, she carried the kind of
work people kept trusting her with. And the question she asks herself changes.

Temidayo is evidence here, not the hero. If a cut makes her the subject rather
than the proof, it is the wrong cut.""",
"""Timing: approximately 3:09, holding to about 3:13.

Section card. Hold briefly, then back to presenter.

Note that the framework does not arrive until now, at over three minutes. That
is deliberate under v5.0: the viewer is identified before they are educated.""",
"""Timing: approximately 3:13.

Reveal the three questions as they are asked.

"The questions on screen are the ones I use, and I would like you to use them
on yourself." Keep her on camera for it.

The warning in this section is "a word is not evidence". The exercise — three
moments where people relied on your judgment, then the verb that repeats — is
the practical core. Give it room.

Close on the boundary: capability can travel while the context still has to be
learned. "That is not starting from zero. That is bringing something proven
into a real learning curve." """,
"""Timing: approximately 4:57, holding to about 5:02.

Section card. Hold briefly, then back to presenter.""",
"""Timing: approximately 5:02.

Show the internal description first, then the version that carries.

The point is explicitly NOT that a number is better: "That sentence is not
better because it has a number in it." Keep that qualifier — it is the whole
teaching point of the slide.

Three questions follow: what was different because I was there, what became
clearer or faster or safer or more possible, and what can I say without
stretching it.""",
"""Timing: approximately 6:09.

The bounded result slide. Reveal 47, then 75.

FACTUAL BOUNDARY, spoken aloud and not to be trimmed: ONE measure of how well
new hires felt integrated, not a claim about everything the redesign touched;
and team work that Temidayo LED, not solo work.

The v5.0 line to protect is "People trust the person who tells them the edges
of their own claim." That is the reason this slide exists.

Do not add the ~30% retention improvement or the >$2M avoided-turnover figure.
Neither is in this video and neither may appear in any graphic or caption.""",
"""Timing: approximately 6:52, holding to about 6:57.

Section card. Hold briefly, then back to presenter.""",
"""Timing: approximately 6:57.

Reveal the four lines: the situation, my role, what changed, what this shows.

The permitted-record boundary is spoken — in your own words, nothing
confidential, nothing employer-owned. Do not edit around it.

The "what this shows" line is the honesty test: the smallest claim the evidence
can hold. Temidayo models it on herself first, then extends it to the viewer:
"I do not want you to stretch yours either." """,
"""Timing: approximately 8:26.

The consolidation card, and then the most important stretch in the video.

Reveal the three practices in order. Then two mistakes: assuming everything
transfers, and assuming nothing does. Both halves matter.

Then the honest limits — this will not stop a restructure, will not decide a
hiring market, will not remove caregiving, money, health, timing or geography
from the decision. Do not cut them to save time; they are why the promise is
credible.

IDENTITY EXIT, at about 9:22: "I am not only trying to help you get through one
job change. I want you to get to the point where a new context does not make
you forget what you already know how to do."

That is the point of the video. If the edit runs long, cut something else.""",
"""Timing: approximately 9:50.

Reveal the three questions one at a time.

"Pause here if you want to write them down." Hold long enough for that to be
possible.

Close on the reframe: not proving you will never have to learn anything new,
but not starting over where you already have proof.""",
"""Timing: approximately 10:48.

Calm and brief. The only resource invitation in the video, and it is the FREE
Career Evidence Starter.

It lands AFTER the identity bridge, so it reads as the next step in what she
has just described rather than an advert. Keep that order.

Exact invitation, verbatim from the v5.0 script:

"If you want to try this on one real thing you have done, I made a free Career
Evidence Starter. It takes about 10 to 15 focused minutes, and you come out of
it with one accomplishment turned into a portable proof line — one sentence you
can actually use. I have linked it below."

The artwork on this slide is the REAL Career Evidence Starter artifact: cover in
front, Portable Proof Line page behind. No Field Kit imagery remains anywhere;
do not restore it. Direct public landing-page URL only — no PDF link.""",
"""Timing: approximately 11:10 to the end, about 11:54.

The card reads "Is Your Job Making You Less Marketable?", the locked Video 2
title, matching what Temidayo says.

Closing lines: "You do not have to erase your career to change jobs. But you do
have to know what you are carrying." Stay on her for both.

Do not summarize the video again.

The right side of the frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds. Do not leave
Subscribe as the only end-screen element.""",
]
FRAMES=[1,1,1,3,1,2,2,1,4,1,3,1,1]

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
    assert len(NOTES)==13 and len(r)==22, (len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
