# -*- coding: utf-8 -*-
"""YouTube descriptions and metadata for V15 to V22.

One resource per video, maximum, and four of the eight carry none. The CTA map is
locked: V15 Career Evidence Starter, V16 none, V17 Keep the Proof, V18 Field Kit,
V19 none, V20 none, V21 Field Kit, V22 none. A resource appears here only when the
recording master itself earns it out loud. The faith anchor is never a second call
to action and is never spoken on camera.
"""

# ---- resources. Absent key means the video ships with no resource link at all.
RESOURCE = {
15: ("\U0001F4D8 Career evidence starter", "Career Evidence Starter",
     "A simple place to work one accomplishment into evidence a reader can check, "
     "including work a tool helped you produce.",
     "https://temidayoafonja.com/career-evidence-starter"),
17: ("\U0001F5C3 Keep the Proof", "Keep the Proof",
     "A full system for building a record of your own work properly, rather than under "
     "pressure in a week when the window is closing.",
     "https://temidayoafonja.com/keep-the-proof"),
18: ("\U0001F9ED Capability Formation Field Kit", "Capability Formation Field Kit",
     "A structured way to test what your experience actually means for one specific "
     "direction, instead of one industry in general.",
     "https://temidayoafonja.com/fieldkit"),
21: ("\U0001F9ED Capability Formation Field Kit", "Capability Formation Field Kit",
     "A structured way to test what your current work is building against a direction "
     "you are considering.",
     "https://temidayoafonja.com/fieldkit"),
}

# URLs carried from the locked pack. career-decisions is recorded but NOT used, because
# no video in V15 to V22 earns it out loud.
URLS_CARRIED = {
    "career-evidence-starter": "https://temidayoafonja.com/career-evidence-starter",
    "keep-the-proof": "https://temidayoafonja.com/keep-the-proof",
    "fieldkit": "https://temidayoafonja.com/fieldkit",
    "career-decisions": "https://temidayoafonja.com/career-decisions",
}
URLS_UNUSED = ["career-decisions"]

BODY = {
15: [
 "The report used to take two days. Now a tool produces most of it in forty minutes. "
 "The writing is clean, the charts are right, and somebody still looks at the finished "
 "thing and asks what you actually did.",
 "This video is about a narrow problem, not a big one. The output used to carry the "
 "evidence of the thinking underneath it. It carries less of that now. The four-page "
 "summary on screen is a constructed example. I wrote it for this video and it is not "
 "anyone's real work.",
 "This is not an argument that AI is taking your value. The payroll evidence currently "
 "runs the other way: in the occupations most exposed to these tools, early-career "
 "employment has softened while experienced workers have held steadier. Faster is not "
 "worse and using a tool is not a confession.",
 "What a record of your reasoning does not do is make a role safe. Roles get redesigned "
 "and removed for reasons that have nothing to do with how good anyone is. The narrow "
 "point is the durable one: if you are accountable for something being right, keep the "
 "reasoning, the checks and the consequence, not just the output.",
],
16: [
 "When it is urgent they call you. When it breaks they call you. Then the interesting "
 "assignment gets handed out, the promotion list comes around, and you are not in the "
 "conversation.",
 "There is one distinction this video is built on, and it decides almost everything "
 "about what you do next: a manager who does not know what you contributed is a "
 "completely different situation from a manager who knows and does not act. The first "
 "is an information problem you can close yourself. The second is not.",
 "I cannot tell you which one you are in. Neither can anyone who has not been in the "
 "room. What I can tell you is that no explanation fixes a missing role, a budget you "
 "do not control, or a decision already made somewhere else.",
 "Finding out you are in the second situation is not the same as finding out the "
 "organization is against you. Most of the time nobody is plotting. There is a "
 "headcount plan, a promise made last year, and a manager managing constraints they "
 "did not choose.",
],
17: [
 "A layoff can take your title in one meeting and your access in the same hour. A few "
 "weeks later somebody tells you to update your resume, and that is when you find out "
 "what you can still prove.",
 "This one is about a narrow window: either you can see it coming, or it has just "
 "happened and the login already stopped working. What goes first is not the memory. "
 "It is the precision, and the context around it.",
 "Keeping proof does not mean taking company property. No confidential documents, no "
 "customer data, no internal reports, screenshots, source code or financial files. "
 "Career evidence that would not survive being asked about is not evidence. It is a "
 "liability you are carrying into an interview.",
 "You will not recover every number, and if you cannot verify it, do not invent it. A "
 "number you cannot stand behind is worth less than a description you can. None of this "
 "gets you the next job, and it does not make the loss smaller. It stops you losing two "
 "things at once.",
],
18: [
 "You made the industry change and you can still do the work. What keeps catching you "
 "are the things nobody thought to explain: a phrase everybody in the room knows, a "
 "decision that goes a direction you would not have predicted, a relationship that "
 "matters for reasons no process document mentions.",
 "This video sorts what is still ahead of you into three kinds that need completely "
 "different plans. Things you can read. Things you have to be near. And things somebody "
 "has to give you access to. Most preparation goes into the first kind, because it is "
 "the one with names on it.",
 "The research behind this is blunter than career advice usually is. In one study of "
 "star equity analysts who changed firms, performance dropped after the move, because "
 "part of what made them excellent belonged to the old firm's people, systems and "
 "support. That is one study of one profession, not a law. It is a reason to know what "
 "you are carrying, not a reason to stay.",
 "A licensing requirement is not a mindset issue. If a role needs a license, a "
 "registration or a qualification you do not hold, adjacent experience does not erase "
 "it. Some barriers are just barriers, and the useful response is to find out exactly "
 "what the requirement is from the body that sets it.",
],
19: [
 "You know the work. You know the numbers. Then somebody asks what you recommend, the "
 "evidence is incomplete, whatever gets decided affects real people, and you realize "
 "you have never actually had to make that call.",
 "That moment feels like one gap. It is usually one of three, and they need completely "
 "different responses: something you were never taught, something you have never been "
 "handed, or something you have already done that nobody can see. Pick the wrong one "
 "and you can spend a year working hard on the wrong problem. The person described in "
 "this video is a constructed example.",
 "The default response is to assume the first one, because you feel exposed and going "
 "to learn something is the cheapest move available. If the real problem is that you "
 "have never owned a call, a course will make you better informed without making you "
 "more practiced.",
 "Some of this is not yours to solve alone. You cannot award yourself authority your "
 "role does not hold, and you cannot manufacture access to consequential work by "
 "wanting it. You can ask for it, negotiate for it, look for it somewhere that offers "
 "it, or decide the environment is the problem.",
],
20: [
 "You got good at the work, your scope grew, and the next step was always there. Not "
 "promised, but there. Then it was not, either because the layer was removed or because "
 "nobody has left it in four years.",
 "Here is what the evidence actually supports. Middle managers were 29% of 2024 layoffs "
 "against a 22% average in the years before, and openings for those roles fell by more "
 "than 40% after 2022 (Korn Ferry, citing Live Data Technologies and Revelio Labs). "
 "Manager engagement has fallen, including as spans of control widen (Gallup). That is a "
 "real contraction. It is not middle management dying. Those roles still exist and "
 "people still get them.",
 "When you lose the next title you do not lose a title. You lose everything you assumed "
 "the title was going to hand you, all at once, in one lump: money, authority, harder "
 "problems, scope, status, access, and future options. They do not all disappear "
 "together, and they are not the same list for two people sitting next to each other.",
 "This does not decide whether you should leave. Compensation, caregiving, health, "
 "immigration status, where you live and what the market is doing are all real, and none "
 "of them shows up in a career framework. A blocked path is information. It is not an "
 "instruction. Your organization is one organization, not a trend.",
],
21: [
 "For a long time career growth was easy to draw. You start here, you move up, bigger "
 "title, bigger team, bigger scope. So what happens when there are fewer boxes above you?",
 "This video puts two people at the same level next to each other. One gets twice as "
 "many people and the same kinds of decisions. The other keeps the same title, and a "
 "decision that used to go two levels up now stops with her. The org chart says the "
 "first one grew. A year later, only one of them has something specific to say about "
 "what changed.",
 "This is not an argument that promotion stopped mattering. Promotion usually comes with "
 "money and it changes how the market reads you. Anyone telling an experienced "
 "professional that titles are meaningless is asking them to absorb a real cost and feel "
 "good about it.",
 "So keep compensation in the conversation, and title too. Do not let growth become a "
 "nice word your company uses when it wants senior work at the same pay. It can "
 "genuinely be a development opportunity and still be underpaid. Both things can be true.",
],
22: [
 "Most career advice still assumes there is a ladder waiting for you. That path still "
 "exists. For a lot of experienced professionals it has gotten shorter, and that changes "
 "which question you should be asking: am I not ready yet, or is there nothing to be "
 "ready for?",
 "I am not going to tell you middle management is dead. The evidence does not support "
 "that. What it supports is a contraction: middle managers were 29% of 2024 layoffs "
 "against 22% in the years before, openings fell more than 40% after 2022 (Korn Ferry, "
 "citing Live Data Technologies and Revelio Labs), and the managers who remain carry "
 "wider spans with engagement falling as those spans grow (Gallup).",
 "The old arrangement moved scope, title, authority, money, status and access together "
 "as a package. Flattening breaks that connection unevenly, so a title no longer tells "
 "you what somebody decides and more people no longer tells you somebody grew. The org "
 "chart shown in this video is a constructed example, not a real employer's chart.",
 "You are allowed to stop blaming yourself for a bottleneck that may not be about your "
 "capability. That line has a limit. Sometimes there is a seat, it does open, and the "
 "honest answer is that somebody else was readier. This is your organization, not the "
 "economy, and nobody can tell you confidently how it looks in 2030.",
],
}

WATCH_NEXT = {
15: ("How to Turn One Accomplishment Into Proof in 10 Minutes", None),
16: ("Before a Layoff, Know What You Can Still Prove", None),
17: ("Which Parts of Your Experience Actually Transfer to Another Industry?", None),
18: ("The Career Gaps You Don't See Until the Work Gets Harder", None),
19: ("What Happens When the Next Step in Your Career Disappears?", None),
20: ("How Do You Grow When There Are Fewer Roles Above You?", None),
21: ("The Career Ladder Doesn't Work the Same Way Anymore", None),
22: ("Which Parts of Your Experience Actually Transfer to Another Industry?", None),
}

PLAYLIST = "Capability Formation: career pivots and internal moves"

SCRIPTURE_STATUS = ("NLT WORDING REQUIRES VERIFICATION. No authorized New Living Translation "
                    "text exists anywhere in this workspace, so the eight verses below could "
                    "not be checked against one in this pass. They are recorded as intended "
                    "references, not as verified NLT wording. Confirm each against an NLT "
                    "edition before publishing. The faith anchor is never spoken on camera "
                    "and is never a second call to action.")

FAITH = {
15: ("“People may be pure in their own eyes, but the Lord examines their motives.”",
     "Proverbs 16:2 (NLT)",
     "A finished document was never the whole account of what you did, and it is less of "
     "one now. There is a reader who already sees the part that does not make it onto "
     "the page. Writing the rest down is for the people who cannot."),
16: ("“Pay careful attention to your own work, for then you will get the satisfaction "
     "of a job well done, and you won’t need to compare yourself to anyone else.”",
     "Galatians 6:4 (NLT)",
     "Being relied on and being considered are not the same thing, and finding out which "
     "one you have is worth more than another year of trying harder at the wrong thing. "
     "My prayer is for a clear read and for peace with whatever it turns out to be."),
17: ("“The Lord detests lying lips, but he delights in those who tell the truth.”",
     "Proverbs 12:22 (NLT)",
     "There is a temptation, when something has just been taken from you, to round a "
     "number up to what it felt like. The strongest truthful version you can actually "
     "support will hold in rooms the other one will not. My prayer is for steadiness "
     "while you rebuild the account of your own work."),
18: ("“Intelligent people are always ready to learn. Their ears are open for "
     "knowledge.”",
     "Proverbs 18:15 (NLT)",
     "Being experienced and being new are not in conflict, and saying both out loud is "
     "more accurate than picking one. My prayer is for the patience to be near something "
     "long enough to understand it, and for grace in the ten seconds where you have to "
     "ask."),
19: ("“Enthusiasm without knowledge is no good; haste makes mistakes.”",
     "Proverbs 19:2 (NLT)",
     "The instinct to go and learn something is a good instinct pointed, often, at the "
     "wrong gap. My prayer is for the honesty to look at which one you actually have "
     "before you spend a year on the other."),
20: ("“We can make our plans, but the Lord determines our steps.”",
     "Proverbs 16:9 (NLT)",
     "Losing the next rung is losing a plan, and plans can be rebuilt once you know what "
     "they were actually for. That is a smaller loss than it feels like on the day, and I "
     "am not going to pretend the day is easy."),
21: ("“If you are faithful in little things, you will be faithful in large ones.”",
     "Luke 16:10 (NLT)",
     "Carrying more consequence is real growth even in a year when nothing on the org "
     "chart moved. My prayer is that you can name it clearly enough to ask for what it is "
     "worth, and not have it named for you."),
22: ("“The prudent understand where they are going, but fools deceive themselves.”",
     "Proverbs 14:8 (NLT)",
     "Looking honestly at the structure you are standing in is not pessimism. A structure "
     "you can see is easier to live with than one you are quietly taking personally, and "
     "it is easier to argue with. My prayer is for clear eyes and an unhurried decision."),
}

COPYRIGHT = ("Scripture quotations are taken from the Holy Bible, New Living Translation, "
             "copyright ©1996, 2004, 2015 by Tyndale House Foundation. Used by permission of "
             "Tyndale House Publishers, Carol Stream, Illinois 60188. All rights reserved.")

TAGS = {
15: ["ai at work", "proving your value", "career evidence", "knowledge work and ai",
     "performance review preparation", "mid career professionals", "judgment and ai",
     "what did you actually do", "capability formation"],
16: ["overlooked at work", "passed over for promotion", "career visibility",
     "relied on but not promoted", "manager relationship", "mid career professionals",
     "internal mobility", "capability formation"],
17: ["layoff preparation", "career evidence", "what to do before a layoff",
     "keeping a record of your work", "resume after layoff", "job loss",
     "mid career professionals", "capability formation"],
18: ["industry change", "career change to another industry", "transferable skills",
     "what does not transfer", "licensing requirements", "new industry learning curve",
     "mid career professionals", "capability formation"],
19: ["career gaps", "decision making at work", "owning a decision",
     "senior individual contributor", "career development plan", "being close to decisions",
     "mid career professionals", "capability formation"],
20: ["promotion blocked", "flattening", "middle management", "no next role",
     "career plan", "span of control", "mid career professionals", "capability formation"],
21: ["career growth without promotion", "fewer roles above me", "flat organization",
     "decision rights", "compensation conversation", "what growth means",
     "mid career professionals", "capability formation"],
22: ["career ladder", "flattening", "middle management contraction",
     "readiness or structure", "org chart", "promotion stalled",
     "mid career professionals", "capability formation"],
}

PINNED = {
15: "The four-page summary in this video is a constructed example. I wrote it so the "
    "argument could be shown end to end without using anyone's real work. The point is "
    "not that the tool did the job badly. It is that the artifact no longer shows who "
    "checked it.",
16: "I cannot tell you which of the two situations you are in, and neither can anyone "
    "who has not been in the room. The one thing you can do is remove the explanation "
    "you control, then see whether anything moves.",
17: "Keep the proof, not the property. Nothing in this video asks you to take "
    "confidential documents, customer data, internal reports or anything you are not "
    "allowed to keep. Evidence that would not survive being asked about is not evidence.",
18: "The study referenced here is one study of one profession: equity research analysts "
    "who changed firms. It is a reason to know what you are carrying, not a law about "
    "everyone who ever changed industries.",
19: "The person described in this video is a constructed example. She is not a client "
    "and not a composite of anyone in particular. The three gaps are not a diagnostic "
    "and they do not assign you a type.",
20: "The figures cited are from Korn Ferry, citing Live Data Technologies and Revelio "
    "Labs, and from Gallup. They describe a pattern in that data. They are not a "
    "forecast, and your organization is one organization, not a trend.",
21: "Nothing here says promotion stopped mattering. It usually comes with money and it "
    "changes how the market reads you. The argument is that the things promotion used to "
    "deliver are still worth going after separately when that route narrows.",
22: "The org chart in this video is constructed. It is not a real employer's chart and "
    "no organization is being described. Draw your own, count the roles that actually "
    "exist above you, and look at how often they open.",
}
