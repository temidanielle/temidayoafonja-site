# -*- coding: utf-8 -*-
"""Video 4 v5.0 speaker/editor notes. Notes parts only; no slide XML.
Timings are working estimates at 145 wpm for the 1,548-word script (~10:40)."""
NOTES=[
"""Timing: approximately 0:48 to 1:35.

Do NOT open on this slide. Begin full-screen on Temidayo and let the opening
land: the viewer's CV making sense only to them, the exact moment halfway into
the second job when it stops landing, the cat-with-nine-lives joke, "the career
was not the problem, the explanation was", and the offer.

FACTUAL BOUNDARY: the joke is the entire approved fact. A senior-manager friend
at EY used to joke it. Do not invent the original conversation, do not script
the friend's words, and use NO CAT IMAGERY anywhere — edit, graphic or
thumbnail.

The chronology lives on the slide. Temidayo does not read it: "The slide has the
chapters, so I am not going to read them to you."

What she does instead is confess the old habit — listing the jobs and handing
the listener a pile of parts. That admission earns the method. Keep it.""",
"""Timing: approximately 1:35.

The central distinction. Reveal the second half after the first has landed.

The straight-line versus non-straight-line explanation is the mechanism of the
whole video: for a nonlinear path, a chronology actively works against you,
because every jump is one more thing the listener has to explain to themselves.

Restrained treatment. No résumé-scroll animation, no timeline gag.

Close on the instruction, then the coaching turn: "There are three parts to it.
I want to walk you through each one." """,
"""Timing: approximately 2:28.

Reveal the cues as she names them.

"Your first sentence has one job: orientation. Not defence." Do not cut it.

The December 2008 context stays exactly as spoken — accounting degree,
financial crisis, took the door that was open, not a designed plan. Nothing is
added.

Close on the honesty line: a career story does not become coherent by
pretending every move was strategic.""",
"""Timing: approximately 3:26, holding to about 3:56.

Reveal NOTICE • TRANSLATE • BUILD • DECIDE as the questions arrive.

"In your second sentence, I want you to look under the labels." That is the
coaching bridge into the section.

Four questions, one at a time. Do not stack them into a single graphic.""",
"""Timing: approximately 3:56.

Show the three nouns first, then the verb question.

Her own verbs — examine, translate, connect, build — are her evidence, not a
template for the viewer.

The script is explicit that accounting, cybersecurity and people strategy are
NOT the same profession, and that she would not force a connection the evidence
does not support. In v5.0 that is turned to the viewer as well: "and I do not
want you to either. A forced story is worse than a messy one, because the
person listening can feel it." Do not cut either half.

Close on the rule: a portable capability is not a word you like the sound of.""",
"""Timing: approximately 5:28, holding to about 5:49.

Reveal PAST CHAPTERS → REPEATED CAPABILITY → NEXT VALUE.

You are not proving the next move was inevitable. You are making the connection
possible to hear. That distinction is the section.""",
"""Timing: approximately 5:49.

Reveal the three stems one at a time.

"The third sentence is doing the real work. It is where the past stops being a
list and starts pointing somewhere." That is spoken coaching, not a caption.

Her worked example is hers. Then the three denials: not the same chapters, not
planned, not everything transferred. All three are load-bearing and must not be
trimmed for pace.

Close on the hand-off: "Now try the same three sentences on your own career.
Out loud, not in your head." The out-loud instruction is deliberate — it is how
the viewer finds the sentence they cannot finish.

This is the only memory device in the video. Do not add CAR or the 3 Cs.""",
"""Timing: approximately 7:05.

The honesty test, and the reason the video is credible. Give it room.

"And here is what I would not do." She takes the risk first, then hands the
viewer the standard.

Markets, caregiving, health, money, restructures and unpredicted opportunity
are all named as legitimate. Interruption, redirection and relearning all
belong in a truthful explanation.

"If one of your chapters does not fit a tidy progression, leave it untidy." Let
that land — it is the permission the viewer came for.""",
"""Timing: approximately 8:03.

Reveal the three test questions, then the evidence challenges.

The three "if you say…" lines are the sharpest moment in the video, and the
follow-up "who disagreed first" is the one that makes it real. Do not soften
them or bury them under a graphic.

Then the written exercise, with the PERMITTED evidence qualifier intact.

Then the honest limits: this will not make a hiring manager say yes, fix a
market, make a change easy, or remove the relearning. What it removes is the
part where the viewer's own experience works against them in the room.

IDENTITY EXIT, at about 9:31: "I want you to stop apologising for a career that
actually makes sense — and to be able to say what it built, plainly, without
inventing a plan you never had."

That is the point of the video. If the edit runs long, cut something else.""",
"""Timing: approximately 9:50.

Calm and brief. The only invitation in the video, and it is the FREE Career
Evidence Starter — not Keep the Proof, not the Field Kit.

It lands AFTER the identity bridge. Keep that order.

Show the real Starter artwork. Direct public landing-page URL only — no PDF
link.""",
"""Timing: approximately 10:11 to the end, about 10:40.

The card reads "Should I Make an Internal Move? 3 Questions to Decide" with the
playlist line — the locked Video 5 title, matching what Temidayo says.

Closing lines: "Your career does not have to look linear to make sense. But
somebody has to be able to hear it." Stay on her for both.

Do not summarize the video again.

The right side of the frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds. Do not leave
Subscribe as the only end-screen element.""",
]
FRAMES=[4,2,1,5,2,3,3,1,3,1,1]
def reveal_notes():
    out=[]
    for s,(n,note) in enumerate(zip(FRAMES,NOTES),1):
        for k in range(1,n+1):
            head=("Reveal frame %d of %d — main slide %d."%(k,n,s)
                  if n>1 else "Single-state frame — main slide %d."%s)
            out.append(head+"\n\n"+note)
    return out
if __name__=="__main__":
    r=reveal_notes(); assert len(NOTES)==11 and len(r)==26,(len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
