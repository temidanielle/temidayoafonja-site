# -*- coding: utf-8 -*-
"""Video 2 v5.0 speaker/editor notes. Notes parts only; no slide XML.
Timings are working estimates at 145 wpm for the 1,632-word script (~11:15)."""

NOTES=[
"""Timing: approximately 0:34 to 1:21.

Do NOT open on this slide. Begin full-screen on Temidayo and let the opening
land: the compliment that is meant, the private question, "I have had to answer
that question about myself more than once", and the promise that this is not a
scare video.

Recognition comes before anything is taught.

Bring the title up under the channel line, then hold for the tone-setting
block: being valuable where you are is real value, it is not a trap and not a
warning sign. Being paid well, being trusted, being the person everyone calls —
none of that is the problem.

NON-ALARMIST IS A HARD RULE for this whole video. No red, no warning graphics,
no countdown, no urgency motifs, anywhere.""",
"""Timing: approximately 1:21.

The central distinction. Reveal the second question after the first has landed.

This section explains the mechanism, and it must stay generous: the viewer's
knowledge is real skill, some of it just belongs to the room they are standing
in. The company knows why they matter because they watched it happen. Another
company is not being unfair — it simply cannot read the evidence.

Closing beat: "praise tells you that you matter here. It cannot tell you how
easily what you do travels." Let it sit before the tests begin.""",
"""Timing: approximately 2:50, holding to about 2:53.

Section card. Hold briefly, then back to presenter.

Note that the framework does not arrive until nearly three minutes. That is
deliberate: the viewer is identified before they are taught.""",
"""Timing: approximately 2:53.

Show the company-bound sentence first, then the version that travels.

Temidayo stands in as the listener — "Outside it, I hear the name of a process.
I do not know what you are actually good at." Keep her on camera so it reads as
a conversation.

FACTUAL BOUNDARY: the QBR sentence is a generic example, not a real client. No
employer, metric or result anywhere in this video.

Close on the reassurance: if the sentence collapses, the value is real and the
description was simply built for an audience that already knew them.""",
"""Timing: approximately 4:16, holding to about 4:22.

Section card. Hold briefly, then back to presenter.""",
"""Timing: approximately 4:22.

Reveal the evidence types one at a time.

This test is explicitly not about visibility or popularity. No job offer, no
audience, no public profile required. Say that plainly.

The indispensable trap is named at the viewer and stays even-handed: depending
on you raises how much they need you; it does not automatically make you
easier for anyone else to understand. Two different kinds of value.

Close on the permission line: if nothing comes to mind yet, that is not a
verdict — it is something untested.""",
"""Timing: approximately 5:56, holding to about 6:00.

Section card. Hold briefly, then back to presenter.""",
"""Timing: approximately 6:00.

Reveal the three questions, then the new-judgment versus same-work-faster
contrast.

Speed is not dismissed. The line to protect is "You can get much better at work
you already know how to do. That is real, and it is not the same thing as your
range getting bigger." Both are allowed to be fine.""",
"""Timing: approximately 7:07.

The consolidation card. Reveal the three tests in order.

Do not add a fourth item, an acronym or a slogan. The three tests are the only
memory device in this video.""",
"""Timing: approximately 7:21.

Hold the two questions side by side while Temidayo walks the four readings.

Two lines carry the tone here: "That is a translation problem, not a value
problem", and "Not panic. Attention." Neither may be cut.

One quarter is not a pattern. No diagnostic treatment, no scorecard.""",
"""Timing: approximately 8:19.

The section that keeps the video honest, and the longest single stretch. Give
it room.

Progressive reveal of the four options. The documentation option keeps its
boundary verbatim: in your own words, at a level you are permitted to share,
nothing confidential or employer-owned.

Then the honest limits, spoken plainly: this will not stop a restructure, or
control a hiring market or a reorg. What it changes is WHEN you find out.

IDENTITY EXIT, at about 10:01: "Not a plan for leaving. The habit of checking —
so you are the person who already knows what you carry, before anybody else
makes the timing decision for you."

That is the point of the video. If the edit runs long, cut something else.""",
"""Timing: approximately 10:16.

Calm and brief. The only resource invitation in the video, and it is the
Capability Formation Field Kit.

It lands AFTER the identity bridge, so it reads as the next step rather than an
advert. Keep that order. Do not add Keep the Proof or the Career Evidence
Starter.

Show the real Field Kit artwork briefly. Before publishing, verify the live
/fieldkit redirect and the current listing.""",
"""Timing: approximately 10:49 to the end, about 11:15.

This card was corrected: it reads "3 Things to Do Before Quitting Your Job",
the locked Video 3 title, matching what Temidayo says. You can hold it on
screen while she names the video.

Closing lines: "Being valuable here is worth having. Being understood elsewhere
is worth building." Stay on her for both.

Do not summarize the video again.

The right side of the frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds.""",
]
FRAMES=[1,1,1,2,1,4,1,4,1,1,4,1,1]

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
    assert len(NOTES)==13 and len(r)==23, (len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
