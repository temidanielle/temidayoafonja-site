# -*- coding: utf-8 -*-
"""Video 2 v3.0 direct-address speaker/editor notes. Notes parts only.

Every quoted anchor below is verbatim from the v3.0 direct-address script, so
the notes no longer carry the stale narration the decks were shipped with.
Timings are script-derived working estimates at 145 wpm (1,258 words, ~8:40)."""

NOTES=[
# 1 Title
"""Timing: approximately 0:38 to 0:57.

Do NOT open on this slide. Begin full-screen on Temidayo and let the whole
H.I.T. opening land first: the hook, the viewer bridge, her own cross-industry
proof, the valuable-here / legible-elsewhere line and the three-test promise.

Bring the title up under the channel line: "I'm Temidayo Afonja. I help
experienced professionals understand what their work has built, what can
travel, and what still has to be learned when the context changes. And that is
what I want to help you do here."

That second sentence is the turn from positioning to relationship. Stay on her
face for it.

Do not make the opening alarmist.""",
# 2 Valuable Here / Legible Elsewhere
"""Timing: approximately 0:57.

This is the central idea of the video. Let it sit.

Reveal the second question after the first has been asked, not before.

Temidayo is careful here and the edit must not undercut her: being relied on is
real value, and none of this implies the viewer should leave. The closing beat
of this section is "Praise tells you that you matter here. It cannot tell you
how easily what you do travels."

Non-alarmist. No warning graphics, no red, no urgency motifs.""",
# 3 01 — Remove the Company Nouns
"""Timing: approximately 2:02, holding to about 2:06.

Section card. Hold briefly, then return to presenter.""",
# 4 Test One
"""Timing: approximately 2:06.

Show the company-bound sentence first, then the clearer description.

What remains after the nouns come out should still tell another person what
problem the viewer solves and what judgment the work requires.

Note the direct-address framing: Temidayo says "Say you tell me: 'I own the QBR
process for this business unit.'" and then "Outside it, I mostly hear the name
of a process." She is standing in as the listener across the table. Keep her on
camera for those two lines so the exchange reads as a conversation.

Viewer action: one sentence from a résumé, a LinkedIn profile or the way they
introduce their work.

The example is generic. Keep it that way; no employer-specific or confidential
material.""",
# 5 02 — Find Outside-Context Evidence
"""Timing: approximately 3:14, holding to about 3:17.

Section card. Hold briefly, then return to presenter.""",
# 6 Test Two
"""Timing: approximately 3:17.

Reveal the evidence types one at a time as each is named.

The evidence can be small. It only has to show that the usefulness survived
some distance from where it was formed.

This is where the indispensable trap is named — and in v3.0 it is named at the
viewer: "This is where being indispensable can mislead you." Do not soften it
into a general observation, and do not turn it into a warning.

Close on the permission line: if the viewer cannot think of an example yet,
that is not a verdict on them. It is something to go and test.""",
# 7 03 — Read the Last 90 Days
"""Timing: approximately 4:38, holding to about 4:42.

Section card. Hold briefly, then return to presenter.""",
# 8 Test Three
"""Timing: approximately 4:42.

Reveal the three questions one at a time, then the new-judgment versus
same-work-faster contrast.

Speed and efficiency are not dismissed. Temidayo says so explicitly. The
distinction is proficiency versus expansion, and the edit should not tip it
into a criticism of anyone who has become faster at familiar work.""",
# 9 The Three Tests
"""Timing: approximately 5:43.

The consolidation card. Reveal the three in order.

Do not add a fourth item, an acronym or a slogan. The three tests are the only
memory device in this video.""",
# 10 Read the Pattern
"""Timing: approximately 5:58.

Hold the two questions side by side while Temidayo walks the four readings.

The governing line is hers and it is addressed to the viewer: "I am not asking
you to diagnose yourself from one quarter or one frustrating assignment. What
matters is the pattern."

No diagnostic tone. No scorecard treatment.""",
# 11 Before You Leave
"""Timing: approximately 6:50.

Progressive reveal, one option at a time.

This is the section that keeps the video non-alarmist, so give it room. A
concern in one test does not mean resign.

The documentation option keeps its boundary verbatim: in the viewer's own
words, at a permitted high level, without taking confidential or
employer-owned material. Do not trim that qualifier.

Close on "Before you change the employer, test whether you can change what the
work is building in you." """,
# 12 Capability Formation Field Kit
"""Timing: approximately 7:49.

Exact invitation, verbatim from the v3.0 script:

"If these three tests tell you that you need a fuller read of what your current
work is building and how portable it is, the Capability Formation Field Kit
gives you a private, evidence-led assessment using the last 90 days of your
actual work. It helps you see what is growing, what may be stalling, what looks
portable and what you still need to investigate before you decide what comes
next. You can find it at temidayoafonja.com/fieldkit."

Calm and brief. This is the only resource invitation in the video. Show the
real Field Kit artwork briefly. Do not add Keep the Proof or the Career
Evidence Starter.

Before publishing, verify the live /fieldkit redirect and the current listing.""",
# 13 Watch Next
"""Timing: approximately 8:21 to the end, about 8:40.

Exact bridge, verbatim from the v3.0 script:

"And if what you are seeing has you seriously considering an exit, do not move
straight from concern to resignation. There are three things I want you to
check first. That is the next video: 3 Things to Do Before Quitting Your Job.
Watch that one next."

DECK DEFECT — NOT FIXED. This card still reads "Before You Quit Your Job, Check
These 3 Things", which is the RETIRED Video 3 title. The locked title is "3
Things to Do Before Quitting Your Job", which is what Temidayo says. No slide
XML change was authorised in this pass. Until the card is corrected, do not
hold it on screen while she names the video: stay on Temidayo, or cut to the
end-screen route.

Do not summarize this video again.

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
