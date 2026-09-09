# -*- coding: utf-8 -*-
"""Publishing copy for Videos 4 to 7, corrected against the September 9 lock.

Descriptions and pinned comments are carried forward from the existing
packages and changed only where the locked script makes the existing copy
inaccurate. Each entry records what changed and why, and that becomes the
publishing section of the change log.

Video 4 and Video 5 pinned comments come from the PINNED COMMENT BRIDGE table
inside their own Recording Masters, which is the authoritative wording.
"""

PLAYLIST_NAME = "Make Your Next Move Without Starting Over"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLJt1Qn1s6-3U"
STARTER = "https://temidayoafonja.com/career-evidence-starter"
KEEP_THE_PROOF = "https://temidayoafonja.com/keep-the-proof"
DECISIONS = "https://temidayoafonja.com/career-decisions"
FIELDKIT = "https://temidayoafonja.com/fieldkit"

META = {
4: dict(number=4,
    title="How to Explain a Career That Looks All Over the Place",
    thumbnail="STOP LISTING JOBS",
    opening_id="“You’re halfway through answering: Walk me through "
               "your background.”",
    framework="Chapters, Spine, Next Direction",
    framework_note="Same ingredients. The order and the amount of detail "
                   "depend on the question.",
    cta_name="Career Evidence Starter", cta_url=STARTER,
    secondary=("Keep the Proof", KEEP_THE_PROOF),
    participation="Share the 20-second version in the comments.",
    watch_next="Why Nobody Can Tell What You’re Actually Good At",
    watch_next_slot="Video 5", watch_next_placeholder="[ADD VIDEO 5 LINK]",
    search="how to explain a career that looks all over the place"),
5: dict(number=5,
    title="Why Nobody Can Tell What You’re Actually Good At",
    thumbnail="THEY CAN’T READ YOU",
    opening_id="“You’re being introduced to someone who could open "
               "a door for you.”",
    framework="The One-Line Test: Claim, Spine, Receipts",
    framework_note=None,
    cta_name="Career Evidence Starter", cta_url=STARTER,
    secondary=None,
    participation="Write the one-line Claim in the comments.",
    watch_next="How to Change Jobs Without Starting Your Career Over",
    watch_next_slot="Video 1", watch_next_placeholder="[ADD VIDEO 1 LINK]",
    search="why nobody can tell what you are good at"),
6: dict(number=6,
    title="Before You Take an Internal Role, Ask These 3 Questions",
    thumbnail="NEW TITLE, SAME WORK?",
    opening_id="“You are offered an internal role.”",
    framework="Work, Judgment, Evidence",
    framework_note=None,
    cta_name="Career Decision Evidence Check", cta_url=DECISIONS,
    secondary=None,
    participation=None,
    watch_next="Are You Growing, or Just Being Given More Work?",
    watch_next_slot="Video 7", watch_next_placeholder="[ADD VIDEO 7 LINK]",
    search="before you take an internal role ask these 3 questions"),
7: dict(number=7,
    title="Are You Growing, or Just Being Given More Work?",
    thumbnail="MORE WORK ≠ GROWTH",
    opening_id="“Sometimes the reward for being dependable is not "
               "growth. It is more work.”",
    framework="CAR: Complexity, Authority, Return",
    framework_note=None,
    cta_name="Capability Formation Field Kit", cta_url=FIELDKIT,
    secondary=None,
    participation=None,
    watch_next="How to Show Your Impact at Work When You Built It From "
               "Scratch",
    watch_next_slot="Video 8", watch_next_placeholder="[ADD VIDEO 8 LINK]",
    search="are you growing or just being given more work"),
}

CONNECT = """\U0001F517 CONNECT AND EXPLORE
Website:
https://temidayoafonja.com

LinkedIn:
https://www.linkedin.com/in/temidayo-afonja

Substack:
https://temidayoafonja.substack.com"""

DESCRIPTION = {
4: """You are halfway through answering "Walk me through your background," and you notice that you are explaining why you left each job without ever saying what all that work built in you. So you add more context. Now the answer feels less like an introduction and more like a defense.

You do not need to pretend every move was planned. You need to show what stayed consistent through the moves that actually happened.

This video gives you three versions of the same story, built from the same ingredients:

✨ Chapters: where you have been, compressed.
✨ Spine: what kept being true underneath those different chapters.
✨ Next Direction: why where you are going follows from what came before.

The ingredients stay the same. The order and the amount of detail depend on the question. A quick introduction leads with the Spine. A longer answer uses the Chapters to make the Spine visible. Your Spine does not change depending on who is asking.

You get a twenty-second version, a ninety-second version, and an answer to "Why so many changes?" You also get the limits an answer cannot fix, and the one thing to do before you need any of it.

Coherence is not the same thing as inevitability. A useful career story does not pretend every step was part of a master plan.

\U0001F9ED FREE 10-MINUTE CAREER EVIDENCE STARTER
Turn one real accomplishment into a proof line you can actually use. It is in the pinned comment:
%(starter)s

\U0001F50E KEEP THE PROOF
The deeper system, if you want to build the evidence properly:
%(keep)s

▶️ WATCH NEXT
Why Nobody Can Tell What You're Actually Good At
[ADD VIDEO 5 LINK]

▶️ START HERE
%(pl_name)s
%(pl_url)s

%(connect)s

#CareerAdvice #InterviewTips #CareerChange""",

5: """You are being introduced to someone who could open a door for you. But the introduction is built around a job title you moved on from ten years ago. To you, that title is one chapter. To them, it is still the headline.

People can respect your experience and still have no idea what to do with you.

So in this video we build one sentence that tells people what kind of problem you are the answer to. I also show you a version of my own sentence that I rejected, even though it sounded stronger, because sounding impressive and being able to prove it are not the same thing.

It is called the One-Line Test:

✨ Claim: one sentence naming the kind of problem you are the answer to.
✨ Spine: what makes that claim true across chapters that look different.
✨ Receipts: evidence that stands on its own, without the chronology.

Claim gets you read. Spine makes you make sense. Receipts make you believable.

I run all three on my own career so you can see whether it holds up, including the sharper sentence I chose not to use and why.

And a better sentence has limits. It cannot erase a weak market, bias or age discrimination, a missing credential, or domain knowledge you do not have yet. Some experience simply will not travel into the next context. The point is to stop creating an additional problem by making people work too hard to understand the experience you do have.

\U0001F9ED FREE 10-MINUTE CAREER EVIDENCE STARTER
Turn one real accomplishment into a proof line, which is exactly the raw material a Claim is built from. It is in the pinned comment:
%(starter)s

▶️ WATCH NEXT
How to Change Jobs Without Starting Your Career Over
[ADD VIDEO 1 LINK]

▶️ START HERE
%(pl_name)s
%(pl_url)s

%(connect)s

#CareerStrategy #CareerClarity #CareerAdvice""",

6: """You are offered an internal role. Same company. Better title. Maybe more visibility. Maybe more money. It feels like progress because something is changing.

But before saying yes, there is one question worth answering: a year from now, what will you be able to do, decide, or prove that you cannot do today?

An internal move can change your title without changing your career. In this video I give you three questions for reading what an internal opportunity will actually build:

✨ Will the work change?
✨ Will my judgment expand?
✨ Will the evidence travel?

This is not an argument that internal is better than external. A new employer can give you a new logo and the same work. Compare the actual access to different work, stronger judgment, and clearer evidence.

A move can still be right for compensation, flexibility, stability, manager fit, family needs, benefits, timing, or another reason that matters in your life. And an internal move cannot erase bias, age discrimination, blocked access, compensation bands, missing credentials, or the fact that your organization may not contain the work you need.

You may not need to leave. But the work does need to change.

\U0001F9ED FREE CAREER DECISION EVIDENCE CHECK
If you are deciding whether to stay, move internally, or leave, use this free evidence check to read the choice more clearly:
%(decisions)s

▶️ WATCH NEXT
Are You Growing, or Just Being Given More Work?
[ADD VIDEO 7 LINK]

▶️ START HERE
%(pl_name)s
%(pl_url)s

%(connect)s

#InternalMobility #CareerGrowth #CareerDecision""",

7: """Sometimes the reward for being dependable is not growth. It is more work.

A colleague leaves. A project has no clear owner. Your manager asks if you can take this too. You do, because you can. Six months later your scope is bigger, your calendar is fuller, and everybody describes it as growth. Maybe it is. Or maybe the organization has simply learned that you will absorb more.

Before you accept the label, run the CAR test:

✨ Complexity: did the problem become harder, or did the volume simply increase?
✨ Authority: did your ability to influence or decide expand with the responsibility?
✨ Return: what did the additional work return in capability, evidence, or recognition?

More work can be part of growth. It is not proof of it.

Praise is welcome. Praise alone is not role design.

This is not a moral judgment about every extra task. Temporary coverage can be a responsible choice during a launch, vacancy, or transition, and growth can be tiring. The issue is whether the extra work has a boundary, a review point, and a real return. Some worthwhile assignments return more in one category than another, and you may gain capability before the title catches up. And finances, family, health, safety, immigration, benefits, stability, and timing can legitimately shape what you choose.

\U0001F9ED CAPABILITY FORMATION FIELD KIT
A private, evidence-led assessment of what your current work is building, where your options may be expanding or narrowing, and where the role may need a boundary or redesign:
%(fieldkit)s

▶️ WATCH NEXT
How to Show Your Impact at Work When You Built It From Scratch
[ADD VIDEO 8 LINK]

▶️ START HERE
%(pl_name)s
%(pl_url)s

%(connect)s

#CareerGrowth #CareerDevelopment #Workload""",
}

_SUB = dict(starter=STARTER, keep=KEEP_THE_PROOF, decisions=DECISIONS,
            fieldkit=FIELDKIT, pl_name=PLAYLIST_NAME, pl_url=PLAYLIST_URL,
            connect=CONNECT)
DESCRIPTION = {k: v % _SUB for k, v in DESCRIPTION.items()}

DESC_CHANGE = {
4: "REWRITTEN OPENING AND FRAMEWORK PARAGRAPHS. The previous description "
   "opened on \"they are not asking for your life story\" and stated the rule "
   "\"stop explaining your career in order.\" Neither survives in the locked "
   "script, and the second now contradicts it, because the ninety-second "
   "answer uses compressed Chapters on purpose. The description now opens on "
   "the script's own opening beat and states the ingredients-plus-order rule. "
   "Resource routes, Watch Next and hashtags unchanged.",
5: "OPENING PARAGRAPH REPLACED, LIMITS PARAGRAPH EXTENDED. The previous "
   "description opened on the sorting problem in the abstract. The locked "
   "script opens on the outdated-title introduction, so the description now "
   "does too, and the rejected-sharper-Claim promise is named because the "
   "script promises it in the first minute. The limits paragraph now matches "
   "the script's own list. Framework, resource route, Watch Next and hashtags "
   "unchanged.",
6: "OPENING PARAGRAPH REPLACED. The previous description opened on \"an "
   "internal move can look safe because the logo does not change,\" which the "
   "locked script no longer says. It now opens on the offer and the one-year "
   "question, which is the script's actual opening. The three questions, the "
   "boundaries paragraph, the resource route, Watch Next and hashtags are "
   "unchanged.",
7: "TWO SENTENCES ADDED, NOTHING REMOVED. The opening, the CAR bullets, the "
   "resource route, Watch Next and hashtags were already accurate against the "
   "locked script. Added the \"Praise alone is not role design\" payoff, which "
   "the script now makes a major beat, and the script's nuance that some "
   "assignments return more in one category than another. Title and thumbnail "
   "unchanged; the thumbnail field keeps the exact locked symbol form.",
}

# Videos 4 and 5: the wording below is the PINNED COMMENT BRIDGE from each
# Recording Master's own table, which is the authoritative copy. The producer
# instruction that sat inside the master's cell ("Keep the Proof can be linked
# in the description") is a note to the publisher, not viewer copy, so it is
# carried in PINNED_NOTE instead of in the comment itself.
PINNED = {
4: """If your career story still sounds like a list of jobs, start with one piece of proof.

The free 10-Minute Career Evidence Starter helps you turn one accomplishment into a portable proof line you can use in an interview, review, internal move, or pivot:
%s

Then share your 20-second version here:

I [work pattern].
I've done that in [2-3 contexts].
Today I [current direction].""" % STARTER,

5: """Trying to write your Claim? Start with one piece of proof.

The free 10-Minute Career Evidence Starter helps you turn one accomplishment into a portable proof line you can use in an interview, performance review, internal move, or pivot:
%s

Then come back and share your one-line Claim here:

What kind of problem are you the answer to?""" % STARTER,

6: """Before your next internal conversation, write one sentence under each question:

1. What different work will I enter?
2. What judgment will I be trusted to carry?
3. What evidence could I explain a year from now?

Three clear yeses and the developmental case is strong. Two yeses tells you which dimension to investigate or negotiate. Zero or one does not automatically make the move wrong, but it may be movement without much growth, and it is worth being accurate about that.

Free Career Decision Evidence Check:
%s""" % DECISIONS,

7: """When your scope grows, run CAR:

C: Did the problem become more complex, or did the volume simply increase?
A: Did authority expand with the responsibility?
R: What did the extra work return in capability, evidence, or recognition?

If Complexity, Authority, and Return are all expanding, the career case for growth is visible. If the volume grew but those three did not, the role may have expanded mainly as workload. That can be acceptable for a short season. Just give the season a boundary and a review date.

Praise is welcome. Praise alone is not role design.

Capability Formation Field Kit:
%s""" % FIELDKIT,
}

PINNED_CHANGE = {
4: "REPLACED with the PINNED COMMENT BRIDGE from the Video 4 Recording "
   "Master's own table, which is the authoritative wording. The previous "
   "pinned comment also carried Temidayo's filled-in example; the master's "
   "version does not, so it was dropped rather than kept alongside an "
   "authoritative text.",
5: "REPLACED with the PINNED COMMENT BRIDGE from the Video 5 Recording "
   "Master's own table.",
6: "COPY UPDATE. The three questions are unchanged and still spoken verbatim. "
   "The reading line said \"a strong growth case\"; the locked script says the "
   "developmental case is strong, and the zero-or-one reading now carries the "
   "script's own MAY BE qualification.",
7: "COPY UPDATE. The CAR questions are unchanged. \"A real growth case\" "
   "became \"the career case for growth is visible,\" matching the locked "
   "script, and the praise payoff was added because the script now makes it a "
   "major beat.",
}

PINNED_NOTE = {
4: "The Recording Master's pinned bridge ends with a note to the publisher: "
   "Keep the Proof can be linked in the description. That is a production "
   "instruction, not viewer copy, so it is not pasted into the comment. Keep "
   "the Proof is already in the description.",
5: None, 6: None, 7: None,
}

TAGS = {
4: ["Temidayo Afonja", "Capability Formation",
    "how to explain your career", "career change interview answer",
    "tell me about yourself", "walk me through your background",
    "why so many job changes", "explaining a varied career",
    "career story interview", "mid career professional",
    "interview answer structure", "how to talk about your career",
    "experienced professional interview", "career narrative",
    "job interview preparation", "career pivot interview"],
5: ["Temidayo Afonja", "Capability Formation",
    "career positioning", "how to describe what you do",
    "personal positioning statement", "senior career advice",
    "experienced professional career", "career clarity",
    "how to stand out in your career", "generalist career",
    "career brand statement", "what am i good at",
    "mid career professional", "hard to categorize career",
    "career direction", "professional identity", "career strategy"],
6: ["Temidayo Afonja", "Capability Formation",
    "before you take an internal role", "internal role",
    "should I make an internal move", "internal move",
    "internal mobility", "internal job transfer", "lateral move",
    "career growth", "career decision", "stay or leave job",
    "career change", "career transition", "career evidence",
    "experienced professionals", "mid career",
    "internal career move", "career development"],
7: ["Temidayo Afonja", "Capability Formation",
    "are you growing at work", "more work vs growth",
    "career growth", "career development", "workload", "scope creep",
    "stretch assignment", "career stagnation",
    "responsibility vs authority", "career evidence",
    "experienced professionals", "mid career", "job growth",
    "professional development", "workload management"],
}

TAGS_CHANGE = {
4: "Unchanged.", 5: "Unchanged.",
6: "Unchanged. The retired primary title is deliberately retained as a search "
   "tag so the topic still surfaces for people searching that way.",
7: "Unchanged.",
}

HASHTAGS = {
4: ["#CareerAdvice", "#InterviewTips", "#CareerChange"],
5: ["#CareerStrategy", "#CareerClarity", "#CareerAdvice"],
6: ["#InternalMobility", "#CareerGrowth", "#CareerDecision"],
7: ["#CareerGrowth", "#CareerDevelopment", "#Workload"],
}

LINK_CHECK = """LINKED DESTINATIONS

Confirm each destination is reachable by a viewer before publication. These
addresses are carried forward from the approved packages and were not invented
here, but nothing in this package can test whether they resolve:

  %s
  %s
  %s
  %s
  %s

No YouTube video URL is supplied for any Watch Next card. The placeholder in
each description is deliberate. Paste the real URL once the destination video
is published. Do not construct a YouTube URL from a guessed identifier.""" % (
    STARTER, KEEP_THE_PROOF, DECISIONS, FIELDKIT, PLAYLIST_URL)
