# -*- coding: utf-8 -*-
"""Video 1 v4.0 speaker/editor notes. Notes parts only.
Timings are script-derived working estimates at 145 wpm (1,409 words, ~9:43)."""

NOTES=[
"""Timing: approximately 0:33 to 1:09.

Do NOT open on this slide. Begin full-screen on Temidayo and let the whole
opening land: the hook, the correction, her roughly eighteen years across very
different functions and industries, and the three-practice promise.

Bring the title up under the channel line, then the promise boundary: "And I
want to be clear with you about the promise. Not everything transfers."

The on-screen deck title and the public YouTube title differ intentionally.
Do not change the title slide to match the public title.""",
"""Timing: approximately 1:09.

The chronology lives on the slide. Temidayo deliberately does not walk through
every title: "The slide shows the broad chapters of my career, so I am not
going to walk you through every title."

The December 2008 accounting degree and the financial crisis stay exactly as
spoken. No employer named, no further detail.

The turn is "I did not carry every task forward. I carried forms of judgment."
Let it sit, then the viewer hand-off: "That is the question I want to help you
answer, and three practices got me there." """,
"""Timing: approximately 2:15, holding to about 2:19.

Section card. Hold briefly, then return to presenter.""",
"""Timing: approximately 2:19.

Reveal the three questions as they are asked.

Note the v4.0 framing: "The questions on screen are the ones I use, and I want
you to use them too." Keep her on camera for it.

Her own nouns — accounting, cybersecurity, people strategy — are named once and
then set against the recurring forms of judgment. Do not turn that into a claim
that they are one profession.

Close on the portability boundary: capability can travel while context still
has to be learned. "That is not starting from zero. That is carrying something
proven into a real learning curve." Do not cut it.""",
"""Timing: approximately 4:03, holding to about 4:07.

Section card. Hold briefly, then return to presenter.""",
"""Timing: approximately 4:07.

Show the internal description first, then the clearer version.

"Let me show you the more useful version" is the coaching turn. Stay on
Temidayo.

The point is explicitly NOT that a number is better: "That sentence is not
better simply because it includes a number." Keep that qualifier.""",
"""Timing: approximately 5:06.

The bounded result slide. Reveal 47, then 75.

FACTUAL BOUNDARY, spoken out loud and not to be trimmed: it was ONE measure of
how well new hires felt integrated, not a claim about everything the redesign
affected, and it was team-based work that Temidayo LED, not something she did
alone.

Do not add the ~30% retention improvement or the >$2M avoided-turnover figure.
Neither is in this video and neither may appear in a graphic, caption or
thumbnail.

Close on: portable evidence connects the situation, the contribution and what
changed.""",
"""Timing: approximately 5:45, holding to about 5:50.

Section card. Hold briefly, then return to presenter.""",
"""Timing: approximately 5:50.

Reveal the four lines: the situation, my role, what changed, what this shows.

The permitted-record boundary is spoken: nothing confidential, nothing
employer-owned. Do not edit around it.

The narrowest-capability rule is the teaching point of this slide. Temidayo
models it on herself and then extends it to the viewer: "I should not turn that
into a claim that I can transform every employee experience problem, and I do
not want you to overreach either." """,
"""Timing: approximately 7:09.

The consolidation card. Reveal the three practices in order.

"They helped me avoid two mistakes: assuming that everything transfers, and
assuming that nothing does." Both halves matter; do not cut either.

Do not add a fourth practice, an acronym or the Career Evidence 3 Cs. The three
practices are the only memory device in this video.""",
"""Timing: approximately 7:51.

Reveal the three questions one at a time.

"Pause here if you want to write them down." Hold the frame long enough for
that to be possible.

Close on the reframe: you are not trying to prove you will never need to learn
anything new, you are trying to avoid starting over where you already have
evidence.""",
"""Timing: approximately 8:43.

Calm and brief. This is the only resource invitation in the video, and it is
the FREE Career Evidence Starter.

Exact invitation, verbatim from the v4.0 script:

"If you want to try this on one real accomplishment of yours, I made a free
Career Evidence Starter. It takes about 10 to 15 focused minutes and helps you
turn one piece of work into a portable Proof Line. I've linked it below."

The supporting artwork on this slide is the REAL Career Evidence Starter
artifact: the cover in front, the Portable Proof Line page behind. No Field Kit
imagery remains anywhere in either deck; do not restore it. Use the direct
public landing-page URL only — no PDF link.""",
"""Timing: approximately 9:01 to the end, about 9:43.

The card reads "Is Your Job Making You Less Marketable?", which is the locked
Video 2 title and matches what Temidayo says.

Closing lines: "You do not have to erase your career to change jobs. But you do
need to know what you are carrying." Stay on her for both.

Do not summarize this video again.

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
