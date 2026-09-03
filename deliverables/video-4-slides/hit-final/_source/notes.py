# -*- coding: utf-8 -*-
"""Video 4 v3.0 direct-address speaker/editor notes. Notes parts only.

Timings are script-derived working estimates at 145 wpm (1,355 words, ~9:20).
Every quoted anchor is verbatim from the v3.0 direct-address script."""

NOTES=[
# 1 Career Path
"""Timing: approximately 0:32 to 1:21.

Do NOT open on this slide. Begin full-screen on Temidayo and let the whole
opening land first: the cat-with-nine-lives line, the disconnected-list
problem, "The career wasn't the problem. The explanation was.", and the turn to
the viewer — "So if your career looks disconnected on paper, let me show you how
I learned to explain mine."

FACTUAL BOUNDARY: the joke is the entire approved fact. Do not name the
employer publicly, do not invent the original conversation, do not script the
colleague's words beyond "a cat with nine lives", and use NO CAT IMAGERY
anywhere — not in the edit, not in the thumbnail.

Bring the chapters up as the chronology. Temidayo deliberately does not read
them back: "The slide gives you the chronology, so I am not going to read every
chapter back to you." Let the visual do that work.

She then names the limits out loud — the work did not stay identical, some
knowledge belonged to the context she was leaving, every move required real
learning. Do not trim those.""",
# 2 Chronology / Portability
"""Timing: approximately 1:21.

The central distinction of the video. Reveal the second half after the first
has been stated.

Note the direct-address framing in v3.0: "when someone asks you, 'Walk me
through your background,' you probably give them a list." The list that follows
is the viewer's list, not a case study. Keep it restrained — no résumé-scroll
animation, no timeline gag.

Close on the instruction: give them enough chronology to orient them, then
explain what the work repeatedly required you to become able to do.

"There are three parts, and I want to walk you through each one" is the
coaching turn. Stay on Temidayo.""",
# 3 1 — Name the Chapters Briefly
"""Timing: approximately 2:09.

Reveal the three cues as she names them.

The coached framing is deliberate: "Your first sentence only has one job:
orientation, not defense." Do not cut it.

Her own example chapters are spoken once, briefly. The 2008 financial-crisis
context stays exactly as spoken and gains nothing: she graduated into that
market, so the first turn was not part of a designed plan. No employer, no
metric, no further detail.

Close on the honesty line: a coherent career story does not require pretending
every move was strategic.""",
# 4 2 — Find the Repeated Work
"""Timing: approximately 3:11, holding to about 3:40.

Reveal NOTICE • TRANSLATE • BUILD • DECIDE as the questions are asked.

"In the second sentence, I want you to look underneath the titles" is the
coaching bridge into this section. Keep it.

The four questions are handed to the viewer one at a time. Let each land; do not
stack them into a single graphic.""",
# 5 Look Beneath the Nouns
"""Timing: approximately 3:40.

Show the three nouns first, then the verb question.

Temidayo's own recurring verbs — examine, translate, connect, build — are her
evidence, not a template. The script is explicit that accounting, cybersecurity
and people strategy are NOT the same profession, and that she would not force a
connection the evidence does not support. In v3.0 that is turned to the viewer:
"so do not force yours either." Do not cut either half.

Close on the rule: a portable capability is not a word you like, it is
something your work repeatedly required you to demonstrate.""",
# 6 3 — Explain the Direction
"""Timing: approximately 4:52, holding to about 5:11.

Reveal PAST CHAPTERS → REPEATED CAPABILITY → NEXT VALUE.

The goal is not to prove the next move was inevitable. It is to make the
connection understandable. That distinction is the whole section.""",
# 7 Three-Sentence Structure
"""Timing: approximately 5:11.

Reveal the three stems one at a time.

"The third sentence explains why the next direction makes sense" is spoken as
part of the coaching; it is not a caption.

Her worked example is hers — "Here is mine:". Then note what it does NOT say:
not every chapter was the same, not every move was planned, not everything
transferred automatically. Those three denials are load-bearing and must not be
trimmed for pace.

Close on the hand-off: "Now try the same three sentences on your own career."
Stay on Temidayo for it.

This is the only memory device in the video. Do not add CAR, the Career
Evidence 3 Cs, or any second framework.""",
# 8 Do Not Invent a Perfect Plan
"""Timing: approximately 6:17.

The honesty test, and the reason the video is credible. Give it room.

"There is an honesty test here, and here is what I would not do." That framing
is Temidayo taking the risk first, then handing the viewer the standard. Keep
it.

Markets, caregiving, health, compensation, restructuring and unpredicted
opportunity are all named as legitimate. Interruption, redirection and
relearning are all allowed in a truthful explanation.

Close on: you are not trying to make your career look linear, you are trying to
make your formation legible.""",
# 9 Explanation Test
"""Timing: approximately 7:08.

Reveal the three test questions one at a time, then the evidence challenges.

The three "if you say…" lines are the sharpest moment in the video and they are
addressed straight at the viewer. Do not soften them and do not bury them under
a graphic.

Then the written exercise: three or four chapters, the problem, the judgment,
one piece of PERMITTED evidence, then circle the repeating verbs. The permitted
qualifier is not optional.

Close on the reassurance: if it still sounds disconnected, the problem may not
be your path — you may just need better evidence behind the connection.""",
# 10 Career Evidence Starter
"""Timing: approximately 8:31.

Calm and brief. This is the only invitation in the video, and it is the FREE
Career Evidence Starter — not Keep the Proof, not the Capability Formation
Field Kit.

Exact invitation, verbatim from the v3.0 script:

"If you want to try this on one real accomplishment of yours, I made a free
Career Evidence Starter. Set aside about 10 to 15 focused minutes and you will
leave with one portable Proof Line. I've linked it below."

Show the real Starter artwork. Use the direct public landing-page URL only —
temidayoafonja.com/career-evidence-starter. Do not expose a PDF link.""",
# 11 Watch Next
"""Timing: approximately 8:48 to the end, about 9:20.

The card reads "Should I Make an Internal Move? 3 Questions to Decide" with the
playlist line. That is the locked Video 5 title and it matches what Temidayo
says.

Closing lines: "Your career does not have to look linear to make sense. But you
do have to make the continuity visible." Stay on her for both.

Do not summarize this video again.

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
    r=reveal_notes()
    assert len(NOTES)==11 and len(r)==26, (len(NOTES),len(r))
    print("main notes:",len(NOTES)," reveal notes:",len(r))
