# -*- coding: utf-8 -*-
"""Approved Video 3 spoken script, verbatim. Markers on their own lines."""
SCRIPT = """If you’re going to quit your job, don’t wait until after you leave to figure out what your work actually built in you.
Access changes. Systems close. People move on.
Before you resign, check three things: what you can preserve, what your work proved you can do, and what the next move needs to build.
I’ve worked inside systems where performance and talent decisions are documented, so I know how quickly that context can disappear.
And if your health or safety is at risk, this is not a reason to wait.
[SLIDE: Title]
I’m Temidayo Afonja. I help experienced professionals understand what they can carry from their work into whatever comes next, without assuming they have to start from zero.
[SLIDE: Once You Leave, Access Changes]
Before we go further, I want to make the safety boundary very clear.
If your health or safety is at risk, or you are dealing with harassment, discrimination or another urgent threat, nothing in this video is a reason to delay leaving.
Act on that first.
Everything else I’m about to say assumes you have enough time and safety to think before you go.
Because while you are still in the role, context is easier to reach.
You can check when something happened.
You can confirm what your responsibility actually was.
You can look at your own review or recognition history where you are permitted to access it.
You can remember who was involved and why a decision mattered.
Later, some of those details become much harder to reconstruct.
This is not about making you hesitate.
It is about making sure you do not leave the meaning of your own experience behind.
[SLIDE: 01 — Preserve the Evidence]
The first check is to preserve the evidence.
[SLIDE: What to Keep / What Not to Take]
And I want to be precise about what I mean by preserve.
This is not permission to take company material.
Keep only what you are entitled to retain.
The examples are on screen, but the rule is much simpler than the list:
If you do not have the right to keep it, do not take it.
Confidential information, customer or employee data, proprietary documents and employer-owned material stay with the employer.
What you are trying to preserve is a truthful record of your own contribution, in your own words, using information you are permitted to retain.
For each strong example, capture the starting condition, what you decided or influenced, what changed, and what permitted evidence supports that result.
That is enough.
You do not need a filing cabinet.
You need enough context that six months from now you can still explain why the work mattered and what you actually did.
[SLIDE: 02 — Name What Your Work Built]
The second check is to name what your work built in you.
[SLIDE: Problem / Constraint / Judgment / Outcome]
A résumé bullet can tell someone what happened.
It does not automatically tell them what you became able to do.
So go one level deeper.
The four prompts are on screen: problem, constraint, judgment and outcome.
What was difficult about the situation?
What did you have to notice, decide, interpret or influence?
And what changed because of it?
Imagine someone says:
“I reduced the amount of time an internal process took.”
That gives me an outcome.
But perhaps what they actually learned to do was identify where work kept getting stuck, bring together people who owned different parts of the process, redesign the handoff and make the change without creating another control problem.
That tells me much more.
The number belongs to one example.
The judgment may be useful again.
That is what I want you looking for.
What did your work prove you can now do that you could not have explained as clearly before?
And then ask:
Where else could that be useful?
[SLIDE: 03 — Test the Next Move]
The third check is to test the next move.
[SLIDE: Uses Something Proven / Builds Something New]
A strong next move usually does two things at once.
It uses something you have already proved.
And it asks you to build something new.
So ask yourself:
What will this next role allow me to carry?
What new judgment, exposure or responsibility will I have to develop?
And after a year there, what should I be able to do that I cannot do today?
This matters because there are two very different kinds of reset.
Sometimes you intentionally enter a new field or role knowing that you will have a real learning curve.
That can be a very good decision.
But you should know what you are choosing to relearn and why.
The other risk is moving to a new employer and discovering that you are essentially repeating the same work in a different setting.
The logo changed.
The work did not.
A new employer is not automatically a new direction.
[SLIDE: The Three Checks]
So before you resign:
Preserve the evidence.
Name what your work built in you.
Test the next move.
In that order.
Not because leaving is wrong.
Because once you know what you are carrying, you can make a much more accurate decision about where you are going.
[SLIDE: Decision Reading]
Once you do that, the evidence may point in a few different directions.
You may look at it and realize:
Yes. I am ready to leave, and I understand what I am taking forward.
Or you may see that the problem is not necessarily the whole organization.
A different role, project, manager or scope may give you the growth you are missing.
Or you may discover that you need a bridge before the move.
Maybe that is financial runway.
Maybe it is a credential.
Maybe you need one piece of evidence outside your current context.
Maybe you simply need a clearer way of explaining what your experience can do somewhere else.
None of those answers is automatically better.
And real constraints matter.
Pay, benefits, caregiving and timing can legitimately affect when you move.
The point is not to make the decision slow.
The point is to make the decision legible.
And again, if the safety boundary applies to you, none of this asks you to wait for perfect evidence.
A harmful situation does not need a bridge plan.
[SLIDE: Before You Resign]
So before you resign, put these three questions somewhere you can actually answer them:
What evidence do I need to preserve now?
What does my strongest evidence prove I can do?
And what must the next move use — and what must it build?
Do not keep the answers only in your head.
Write them down.
You are trying to leave with more than a memory that says, “I did a lot there.”
You want to be able to say:
This is what I handled.
This is what I became able to do.
And this is what I need next.
[SLIDE: Career Decision Evidence Check]
If you want a structured way to read the evidence behind a stay, move or leave decision, that is what the Career Decision Evidence Check is for.
It will help you slow the decision down just enough to separate what you know from what you are assuming.
You can find it at temidayoafonja.com/career-decisions.
I’ve also linked it below.
[SLIDE: Watch Next]
And if your next move changes your role, function, employer or industry, there is another question underneath this one:
What from your experience actually carries with you?
Watch How to Change Jobs Without Starting Your Career Over next.
Because leaving one job should not require you to erase everything your work has already built in you."""
LINES=[l.strip() for l in SCRIPT.split("\n") if l.strip()]
MARKERS=[l for l in LINES if l.startswith("[SLIDE:")]
SPOKEN=[l for l in LINES if not l.startswith("[SLIDE:")]
