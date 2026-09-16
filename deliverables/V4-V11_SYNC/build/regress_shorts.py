# -*- coding: utf-8 -*-
"""Regression fixtures: the exact delivered Shorts the independent review
cited. Each must make the new audit fail, or the rule is decoration."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shortsync as S

DELIVERED = {
 (11, 3): dict(
   stop=[u"Then ask COST. What does the difference actually cost you?"],
   hold=[u"Not every mismatch deserves the same response.",
         u"I would look at four costs.",
         u"CAPABILITY. Is this role building judgment, scope, and "
         u"experience you want to carry forward?",
         u"EVIDENCE. Will you be able to prove meaningful work from this "
         u"version of the job?"],
   ask=[u"A mismatch can be manageable in one category and unacceptable "
        u"in another."]),
 (10, 1): dict(
   stop=[u"And now you feel this pressure to prove they made the right "
         u"decision."],
   hold=[u"That pressure can make you do exactly the wrong thing.",
         u"You start trying to fix things before you understand why they "
         u"work this way.",
         u"Or you go the other direction.",
         u"I do not think either one is the job of your first 90 days."],
   ask=[u"Your first job is not to prove that everything you already know "
        u"works here."]),
 (10, 2): dict(
   stop=[u"You can know how to work and still have a lot to learn about "
         u"how this place works."],
   hold=[u"One thing those moves taught me is that experience and context "
         u"are not the same thing.",
         u"It is to figure out three things: What from my experience "
         u"actually works here?",
         u"What do I need to learn about this new context?",
         u"And what can I begin to prove here?"],
   ask=[u"I think about that as READ. TEST. PROVE."]),
 (5, 1): dict(
   stop=[u"Your company can need you so much that it becomes one of the "
         u"reasons you stop growing."],
   hold=[u"I know that sounds backwards.",
         u"Something breaks, they call you.",
         u"Someone leaves, you absorb the work.",
         u"A new person joins, you train them.",
         u"Then a bigger opportunity opens.",
         u"And they choose someone else."],
   ask=[u"That is the problem I want to unpack, because being needed and "
        u"being developed are not the same thing."]),
 (4, 3): dict(
   stop=[u"Good judgment does not suddenly appear when someone gets a "
         u"senior title."],
   hold=[u"It has to be built over time.",
         u"Senior judgment is built from hundreds of smaller decisions "
         u"made over years.",
         u"That does not mean the future is doomed."],
   ask=[u"It means the learning path may need to be designed on "
        u"purpose."]),
 (6, 1): dict(
   stop=[u"Next, look at the verbs."],
   hold=[u"Does the person decide?", u"Lead?", u"Negotiate?",
         u"Recommend?",
         u"Supporting the development of strategy is not the same as "
         u"setting the strategy.",
         u"That does not make the job unimportant.",
         u"It tells you where the decision power may sit."],
   ask=[u"But do not only ask, “Is this senior?”",
        u"Ask, “What is this person actually trusted to "
        u"decide?”"]),
 (5, 3): dict(
   stop=[u"If you take on extra work because the company needs you, set a "
         u"time to review it."],
   hold=[u"You can say, “Let’s come back to this in 90 "
         u"days.”",
         u"Then ask: What became permanent?", u"What did I learn?",
         u"What decisions became mine?",
         u"What recognition or role change comes with this?"],
   ask=[u"Without a review point, temporary extra work can quietly become "
        u"your normal job."]),
 (8, 2): dict(
   stop=[u"Keeping proof does not mean taking company property."],
   hold=[u"Do not send confidential documents to yourself.",
         u"Do not copy customer data.",
         u"The goal is not to keep the company’s files.",
         u"The goal is to keep a lawful record of your own work.",
         u"You are keeping the shape of the evidence.",
         u"You are not taking the company’s property."],
   ask=[u"Keep the proof.", u"Not the property."]),
 (9, 2): dict(
   stop=[u"Then ask what belonged to the old place."],
   hold=[u"Internal relationships.", u"Company systems.",
         u"The language everyone understood without explaining it.",
         u"Informal power.", u"Knowing exactly who to call.",
         u"Those things can make you excellent where you are."],
   ask=[u"But they may not mean much in the next place."]),
 (9, 3): dict(
   stop=[u"The longer you stay in one place, the easier it is to confuse "
         u"knowing the place with having something you can carry "
         u"anywhere."],
   hold=[u"You know who to call.", u"You know which meeting matters.",
         u"That is real expertise.",
         u"But some of that expertise belongs to the environment, not "
         u"only to you."],
   ask=[u"The capability may still be there.", u"The shortcuts are not."]),
 (10, 3): dict(
   stop=[u"Not, “How am I doing?”"],
   hold=[u"That question is broad enough to get you an answer like, "
         u"“You’re doing great.”",
         u"Ask something more useful: “What have you seen me pick up "
         u"quickly?” “Where do I still need more context?” "
         u"“Is there anything I am treating like my old environment "
         u"that works differently here?”",
         u"And ask: “What would you want to trust me with by the end "
         u"of my first 90 days that you would not have trusted me with on "
         u"day one?”"],
   ask=[u"That question turns the first 90 days into development, not "
        u"performance theater."]),
 (7, 1): dict(
   stop=[u"Two people can both be good at their jobs."],
   hold=[u"Then a bigger opportunity opens.",
         u"One person’s name comes up.",
         u"The other person’s does not.",
         u"And sometimes the difference has nothing to do with capability "
         u"at all.",
         u"Access matters.", u"Sponsorship matters.",
         u"Bias and politics can matter too."],
   ask=[u"Keep one question in mind: if a bigger role opened tomorrow, "
        u"what evidence would someone in that room point to for you?"]),
 (11, 2): dict(
   stop=[u"Then write ACTUAL. What is the job asking from you now? Do not "
         u"judge it from one bad week. Look for the recurring pattern."],
   hold=[u"And sometimes the actual role is narrower. You were hired for "
         u"strategy and spend most of your time coordinating."],
   ask=[u"The question is not, “Is this exactly what was "
        u"written?”"]),
 (8, 1): dict(
   stop=[u"Imagine tomorrow morning you try to log into your work "
         u"account.", u"You cannot."],
   hold=[u"Email gone. Dashboard gone. Project folders gone.",
         u"You remember doing good work.",
         u"You remember that the project mattered.",
         u"But was the improvement 27% or 37%?",
         u"Did you own the decision or the rollout?",
         u"What was the baseline?"],
   ask=[u"That is why I think the worst time to reconstruct your career "
        u"evidence is after you lose access to it."]),
}

fired = 0
held = []
for (n, num), d in sorted(DELIVERED.items()):
    keep = S.SHORTS[(n, num)]
    S.SHORTS[(n, num)] = d
    bad = [b for b in S.audit(n) if b.startswith("V%d S%d " % (n, num))]
    S.SHORTS[(n, num)] = keep
    if bad:
        fired += 1
        print(u"FIRES  V%-2d S%d  %s" % (n, num, bad[0][len("V%d S%d " %
                                                            (n, num)):]))
        for b in bad[1:]:
            print(u"              %s" % b[len("V%d S%d " % (n, num)):])
    else:
        held.append((n, num))
        print(u"HELD   V%-2d S%d  <-- rule does not catch the cited defect"
              % (n, num))
print("")
print("delivered defects re-tested: %d   rules fired: %d   silent: %d"
      % (len(DELIVERED), fired, len(held)))
sys.exit(1 if held else 0)
