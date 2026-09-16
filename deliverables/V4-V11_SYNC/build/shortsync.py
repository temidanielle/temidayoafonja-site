# -*- coding: utf-8 -*-
"""Three candidate Shorts per video, synchronized to the reconciled master.

Every line is a whole sentence lifted verbatim from its own reconciled
master. No narration is invented, no sentences are joined into a claim the
script does not make, and no Short is a trailer: each carries one complete
idea and one ask.

Each candidate keeps the angle of the candidate it replaces, so the bank is
still three per video and still the same three purposes.

V4's Shorts deliberately avoid the unresolved numerical opening. That
comparison is a live evidence question, so no Short is built on it.
"""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recon as R

WPM = 165

ANGLE = {
 (4, 1): "AI Took the Task. Who Gets the Experience?",
 (4, 2): "What Did This Task Used to Teach?",
 (4, 3): "Senior Judgment Has to Come From Somewhere",
 (5, 1): "Being Needed Is Not the Same as Growing",
 (5, 2): "Useful Can Become a Career Trap",
 (5, 3): "Set a Review Point for Extra Scope",
 (6, 1): "Read the Verb Before You Trust the Title",
 (6, 2): "The $61,500 Strategy Title",
 (6, 3): "The Title That Tells You Almost Nothing",
 (7, 1): "The Bigger Role Is Not Always About Working Harder",
 (7, 2): "Ask for the Work That Proves the Next Level",
 (7, 3): "You Can Be Valuable and Still Hard to Picture Higher",
 (8, 1): "Your Memory Stays. Your Dashboard Does Not.",
 (8, 2): "Keep the Proof, Not the Property",
 (8, 3): "The Worst Time to Rebuild Your Career Story",
 (9, 1): "Transferable Skills Advice Is Incomplete",
 (9, 2): "Not Everything Travels",
 (9, 3): "The Longer You Stay, the Easier This Is to Miss",
 (10, 1): "Don't Spend Your First 90 Days Proving Yourself",
 (10, 2): "Experienced but New to the Context",
 (10, 3): "Ask Your Manager This by Day 90",
 (11, 1): "This Isn't the Job",
 (11, 2): "Expected vs Actual",
 (11, 3): "What Is the Cost of Role Drift?",
}

SHORTS = {
 (4, 1): dict(
   stop=["So I think we are asking the wrong question about some of this "
         "work."],
   hold=["Not just: What can AI do now?",
         "But: If AI takes the task, who gets the experience that used to "
         "come from doing it?",
         "Because we still need experienced people later.",
         "And somehow, they have to become experienced."],
   ask=["So do not only ask, “Who does the task now?”",
        "Ask: “Who gets the experience?”"]),
 (4, 2): dict(
   stop=["A task can be boring and still teach you something."],
   hold=["Doing the same kind of work again and again helps you notice "
         "patterns.",
         "Making mistakes helps you learn what to watch for.",
         "If you manage people, do not only ask, “What can we "
         "automate?”",
         "Also ask, “What did this task used to teach?”"],
   ask=["Then decide where that learning will happen now."]),
 (4, 3): dict(
   stop=["Good judgment does not suddenly appear when someone gets a "
         "senior title."],
   hold=["It has to be built over time.",
         "Senior judgment is built from hundreds of smaller decisions made "
         "over years.",
         "That does not mean the future is doomed."],
   ask=["It means the learning path may need to be designed on purpose."]),

 (5, 1): dict(
   stop=["Your company can need you so much that it becomes one of the "
         "reasons you stop growing."],
   hold=["I know that sounds backwards.",
         "Something breaks, they call you.",
         "Someone leaves, you absorb the work.",
         "A new person joins, you train them.",
         "Then a bigger opportunity opens.",
         "And they choose someone else."],
   ask=["That is the problem I want to unpack, because being needed and "
        "being developed are not the same thing."]),
 (5, 2): dict(
   stop=["Being useful can feel like career security."],
   hold=["Sometimes it is.",
         "But being very useful can also make it hard for a team to "
         "imagine moving you.",
         "That does not mean they are plotting against you.",
         "It means what helps the company today may not be the same thing "
         "that helps your future."],
   ask=["Ask: What is this company building in me beyond my ability to "
        "keep this role running?"]),
 (5, 3): dict(
   stop=["If you take on extra work because the company needs you, set a "
         "time to review it."],
   hold=["You can say, “Let’s come back to this in 90 days.”",
         "Then ask: What became permanent?", "What did I learn?",
         "What decisions became mine?",
         "What recognition or role change comes with this?"],
   ask=["Without a review point, temporary extra work can quietly become "
        "your normal job."]),

 (6, 1): dict(
   stop=["Next, look at the verbs."],
   hold=["Does the person decide?", "Lead?", "Negotiate?", "Recommend?",
         "Supporting the development of strategy is not the same as "
         "setting the strategy.",
         "That does not make the job unimportant.",
         "It tells you where the decision power may sit."],
   ask=["But do not only ask, “Is this senior?”",
        "Ask, “What is this person actually trusted to decide?”"]),
 (6, 2): dict(
   stop=["Senior Divisional Strategy Consultant, Governance."],
   hold=["Sounds pretty senior, right?",
         "Sounds like someone setting strategy and making big decisions.",
         "But when I read the actual posting, the bottom of the pay range "
         "was $61,500, and one of the requirements was being able to "
         "accept direction and feedback.",
         "Nothing is wrong with either of those things.",
         "But they tell you something important: The title did not tell "
         "you the job."],
   ask=["And the first thing I would do is almost ignore the title."]),
 (6, 3): dict(
   stop=["Sometimes a title sounds smaller or stranger than the work "
         "really is."],
   hold=["One posting was called Member of Technical Staff, Governance "
         "Risk Compliance.",
         "The title does not tell you much.",
         "But the work included leading federal authorization work, "
         "advising leaders, working across teams, and serving as a "
         "subject-matter expert.",
         "In my sample, one of the least clear titles sat on the highest "
         "published pay ceiling."],
   ask=["So if a title confuses you, do not automatically skip the job.",
        "Read the work."]),

 (7, 1): dict(
   stop=["Two people can both be good at their jobs."],
   hold=["Then a bigger opportunity opens.",
         "One person’s name comes up.",
         "The other person’s does not.",
         "And sometimes the difference has nothing to do with capability "
         "at all.",
         "Access matters.", "Sponsorship matters.",
         "Bias and politics can matter too."],
   ask=["Keep one question in mind: if a bigger role opened tomorrow, what "
        "evidence would someone in that room point to for you?"]),
 (7, 2): dict(
   stop=["If you want a bigger role, do not only ask for more "
         "responsibility."],
   hold=["Ask what kind of responsibility.",
         "What decisions will I get to make?",
         "What problem will I own from beginning to end?",
         "What level of stakeholder will I work with?",
         "What evidence would show that I am ready for the next level?"],
   ask=["That changes the question from: “Can I help more?”",
        "to: “What would let me practice the next level of "
        "work?”"]),
 (7, 3): dict(
   stop=["You may be doing hard work every day."],
   hold=["But if most of the work people see is rescue, cleanup, and "
         "execution, they may see you as very important to the role you "
         "already have.",
         "Your value is real.",
         "The problem may be that the evidence people see is evidence for "
         "your current role, not the next one."],
   ask=["You can become more useful without becoming easier to picture at "
        "the next level."]),

 (8, 1): dict(
   stop=["Imagine tomorrow morning you try to log into your work account.",
         "You cannot."],
   hold=["Email gone.", "Dashboard gone.", "Project folders gone.",
         "You remember doing good work.",
         "You remember that the project mattered.",
         "But was the improvement 27% or 37%?",
         "Did you own the decision or the rollout?",
         "What was the baseline?"],
   ask=["That is why I think the worst time to reconstruct your career "
        "evidence is after you lose access to it."]),
 (8, 2): dict(
   stop=["Keeping proof does not mean taking company property."],
   hold=["Do not send confidential documents to yourself.",
         "Do not copy customer data.",
         "The goal is not to keep the company’s files.",
         "The goal is to keep a lawful record of your own work.",
         "You are keeping the shape of the evidence.",
         "You are not taking the company’s property."],
   ask=["Keep the proof.", "Not the property."]),
 (8, 3): dict(
   stop=["Most people think they will collect career evidence later."],
   hold=["But later is often when the details are hardest to remember.",
         "And sometimes later is after your access is already gone.",
         "Once a month, take ten minutes and write down: What changed?",
         "What was mine?", "What was hard?", "What proof do I have?"],
   ask=["What would I be allowed to say outside this company?"]),

 (9, 1): dict(
   stop=["I think some transferable-skills advice gives experienced "
         "professionals false confidence."],
   hold=["Not because your experience does not transfer.",
         "Some of it absolutely can.",
         "The problem is that we spend so much time asking, What can I "
         "take with me?",
         "that we avoid the harder question: What am I leaving behind?"],
   ask=["So I would not make a transferable-skills list.",
        "I would make four columns: What travels?", "What does not?",
        "What can I prove?", "What must I relearn?"]),
 (9, 2): dict(
   stop=["Then ask what belonged to the old place."],
   hold=["Internal relationships.", "Company systems.",
         "The language everyone understood without explaining it.",
         "Informal power.", "Knowing exactly who to call.",
         "Those things can make you excellent where you are."],
   ask=["But they may not mean much in the next place."]),
 (9, 3): dict(
   stop=["The longer you stay in one place, the easier it is to confuse "
         "knowing the place with having something you can carry "
         "anywhere."],
   hold=["You know who to call.", "You know which meeting matters.",
         "That is real expertise.",
         "But some of that expertise belongs to the environment, not only "
         "to you."],
   ask=["The capability may still be there.", "The shortcuts are not."]),

 (10, 1): dict(
   stop=["And now you feel this pressure to prove they made the right "
         "decision."],
   hold=["That pressure can make you do exactly the wrong thing.",
         "You start trying to fix things before you understand why they "
         "work this way.",
         "Or you go the other direction.",
         "I do not think either one is the job of your first 90 days."],
   ask=["Your first job is not to prove that everything you already know "
        "works here."]),
 (10, 2): dict(
   stop=["You can know how to work and still have a lot to learn about "
         "how this place works."],
   hold=["One thing those moves taught me is that experience and context "
         "are not the same thing.",
         "It is to figure out three things: What from my experience "
         "actually works here?",
         "What do I need to learn about this new context?",
         "And what can I begin to prove here?"],
   ask=["I think about that as READ. TEST. PROVE."]),
 (10, 3): dict(
   stop=["Not, “How am I doing?”"],
   hold=["That question is broad enough to get you an answer like, "
         "“You’re doing great.”",
         "Ask something more useful: “What have you seen me pick up "
         "quickly?” “Where do I still need more context?” "
         "“Is there anything I am treating like my old environment "
         "that works differently here?”",
         "And ask: “What would you want to trust me with by the end "
         "of my first 90 days that you would not have trusted me with on "
         "day one?”"],
   ask=["That question turns the first 90 days into development, not "
        "performance theater."]),

 (11, 1): dict(
   stop=["You accepted one job. Then you started doing another. Maybe the "
         "title is the same. Maybe the salary is the same. But three or "
         "six weeks in, you are thinking: This is not the job I thought I "
         "accepted."],
   hold=["Before you call it a bait-and-switch, slow down. Roles change. "
         "Priorities move. Managers inherit new problems. Companies "
         "reorganize."],
   ask=["But there is a point where normal change becomes something you "
        "need to look at more closely. I use four questions for that: "
        "EXPECTED. ACTUAL. COST. CHOICE."]),
 (11, 2): dict(
   stop=["Then write ACTUAL. What is the job asking from you now? Do not "
         "judge it from one bad week. Look for the recurring pattern."],
   hold=["Sometimes the actual role is better than the one you expected. "
         "You may have more scope, more visibility, or a better manager "
         "than the job description suggested.",
         "And sometimes the actual role is narrower. You were hired for "
         "strategy and spend most of your time coordinating. You expected "
         "to lead a team and the team never arrived. You were told a "
         "decision was yours and discover that you can only recommend."],
   ask=["The question is not, “Is this exactly what was "
        "written?” The better question is, “Is the job I am "
        "doing still close enough to the job I agreed to build my life "
        "and career around?”"]),
 (11, 3): dict(
   stop=["Then ask COST. What does the difference actually cost you?"],
   hold=["Not every mismatch deserves the same response.",
         "I would look at four costs.",
         "CAPABILITY. Is this role building judgment, scope, and "
         "experience you want to carry forward?",
         "EVIDENCE. Will you be able to prove meaningful work from this "
         "version of the job?"],
   ask=["A mismatch can be manageable in one category and unacceptable in "
        "another."]),
}


def lines(n, num):
    d = SHORTS[(n, num)]
    return d["stop"] + d["hold"] + d["ask"]


def rows(n):
    out = []
    for num in (1, 2, 3):
        d = SHORTS[(n, num)]
        body = " ".join(lines(n, num))
        w = len(body.split())
        out.append(dict(num=num, title=ANGLE[(n, num)], stop=d["stop"],
                        hold=d["hold"], ask=d["ask"], body=body, words=w,
                        secs=int(round(w / float(WPM) * 60))))
    return out


def verify(n):
    body = R.S._norm(R.spoken_text(n)).lower()
    bad = []
    for num in (1, 2, 3):
        for l in lines(n, num):
            if R.S._norm(l).lower() not in body:
                bad.append((num, l[:70]))
    return bad


if __name__ == "__main__":
    tot = 0
    for n in R.VIDEOS:
        bad = verify(n)
        tot += len(bad)
        print("V%-3d %s" % (n, "all three verbatim from the reconciled "
                            "master" if not bad else "NOT VERBATIM: %s"
                            % bad))
        for r in rows(n):
            print("     %d  %-52s %3d words  about 0:%02d"
                  % (r["num"], r["title"][:52], r["words"], r["secs"]))
    print("\nlines not verbatim: %d" % tot)
