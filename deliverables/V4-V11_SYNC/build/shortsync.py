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
   stop=["Imagine a task that takes someone hours. Now imagine AI produces "
         "a first draft in seconds. That sounds like progress. But those "
         "hours were not always wasted."],
   hold=["That was where someone learned what a bad answer looked like. "
         "Where they made mistakes. Where they started noticing patterns.",
         "So I think we are asking the wrong question about some of this "
         "work.",
         "Not just: What can AI do now?",
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
         "If people stop getting those smaller decisions, companies may "
         "discover the problem much later, when they need someone who can "
         "handle a messy situation and fewer people have practiced doing "
         "that.",
         "That does not mean the future is doomed.",
         "It means the learning path may need to be designed on purpose."],
   ask=["If the task used to teach something important, do not assume the "
        "learning will happen by itself after the task is gone."]),

 (5, 1): dict(
   stop=["Your company can need you so much that it becomes one of the "
         "reasons you stop growing."],
   hold=["I know that sounds backwards.",
         "Something breaks, they call you.",
         "Someone leaves, you absorb the work.",
         "A new person joins, you train them.",
         "Then a bigger opportunity opens.",
         "And they choose someone else.",
         "Dependence sounds like: “We cannot do this without you.”",
         "Development sounds like: “Here is something you have not "
         "done before. We want you to learn it.”",
         "The problem is when the only thing growing is how much the "
         "company depends on you."],
   ask=["Are they asking for more of your capacity, or expanding your "
        "capability?",
        "Once you can see that difference, you can stop confusing being "
        "needed with moving forward."]),
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
         "Then ask: What became permanent? What did I learn? What "
         "decisions became mine?",
         "What recognition or role change comes with this? What am I "
         "taking off my plate?"],
   ask=["Without a review point, temporary extra work can quietly become "
        "your normal job."]),

 (6, 1): dict(
   stop=["Supporting the development of strategy is not the same as "
         "setting the strategy."],
   hold=["When I read a job description, I look for four things: PROBLEM. "
         "AUTHORITY. PROOF. REAL GAP.",
         "look at the verbs. Does the person decide? Lead? Negotiate? "
         "Recommend? Influence? Support? Execute?",
         "That does not make the job unimportant.",
         "It tells you where the decision power may sit."],
   ask=["But do not only ask, “Is this senior?” Ask, “What "
        "is this person actually trusted to decide?”"]),
 (6, 2): dict(
   stop=["I want you to guess what this job actually is. Senior Divisional "
         "Strategy Consultant, Governance."],
   hold=["Sounds pretty senior, right?",
         "Sounds like someone setting strategy and making big decisions.",
         "But when I read the actual posting, the bottom of the pay range "
         "was $61,500, and one of the requirements was being able to "
         "accept direction and feedback.",
         "Nothing is wrong with either of those things.",
         "But they tell you something important: The title did not tell "
         "you the job."],
   ask=["And the first thing I would do is almost ignore the title.",
        "Ask: What problem does this company need this person to solve?"]),
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
   stop=["Two people can both be good at their jobs. Both dependable. Both "
         "experienced. Both working hard."],
   hold=["Then a bigger opportunity opens. One person’s name comes up. "
         "The other person’s does not.",
         "I have seen versions of that happen inside organizations, and "
         "the difference is not always who worked harder. Sometimes the "
         "person who gets the bigger role has something the other person "
         "does not have yet: evidence people can already see at the next "
         "level.",
         "And sometimes the difference has nothing to do with capability "
         "at all. Access matters. Sponsorship matters. Bias and politics "
         "can matter too."],
   ask=["Keep one question in mind: if a bigger role opened tomorrow, what "
        "evidence would someone in that room point to for you?",
        "Not what would you say about yourself. What could they already "
        "point to?"]),
 (7, 2): dict(
   stop=["If you want a bigger role, do not only ask for more "
         "responsibility."],
   hold=["Ask what kind of responsibility.",
         "What decisions will I get to make? What problem will I own from "
         "beginning to end? What level of stakeholder will I work with? "
         "What evidence would show that I am ready for the next level?"],
   ask=["That changes the question from: “Can I help more?” to: "
        "“What would let me practice the next level of work?”"]),
 (7, 3): dict(
   stop=["You may be doing hard work every day."],
   hold=["But if most of the work people see is rescue, cleanup, and "
         "execution, they may see you as very important to the role you "
         "already have.",
         "Your value is real.",
         "The problem may be that the evidence people see is evidence for "
         "your current role, not the next one.",
         "You can become more useful without becoming easier to picture at "
         "the next level."],
   ask=["Pick one kind of next-level work you want to be trusted with. Ask "
        "what decision, problem, stakeholder, or risk would let you "
        "practice it where someone can see the result."]),

 (8, 1): dict(
   stop=["Imagine tomorrow morning you try to log into your work account.",
         "You cannot."],
   hold=["Email gone. Dashboard gone. Project folders gone.",
         "Now imagine that six months later an interviewer asks: What "
         "exactly changed because of your work? You remember doing good "
         "work. You remember that the project mattered.",
         "But was the improvement 27% or 37%? Did you own the decision or "
         "the rollout? What was the baseline?",
         "That is why I think the worst time to reconstruct your career "
         "evidence is after you lose access to it."],
   ask=["Pick one project and write five things in your own words: "
        "baseline, scope, the decision that was yours, the result, and how "
        "the result was judged. Then ask what you are allowed to keep or "
        "say outside the company."]),
 (8, 2): dict(
   stop=["Keeping proof does not mean taking company property."],
   hold=["Do not send confidential documents to yourself.",
         "Do not copy customer data. Do not take private reports, "
         "screenshots, source code, internal financial information, or "
         "anything you are not allowed to keep. The goal is not to keep "
         "the company’s files. The goal is to keep a lawful record of "
         "your own work.",
         "You are keeping the shape of the evidence.",
         "You are not taking the company’s property."],
   ask=["Keep the proof.", "Not the property."]),
 (8, 3): dict(
   stop=["Most people think they will collect career evidence later."],
   hold=["But later is often when the details are hardest to remember. And "
         "sometimes later is after your access is already gone.",
         "Once a month, take ten minutes and write down: What changed? "
         "What was mine?",
         "What was hard? What proof do I have? What would I be allowed to "
         "say outside this company?"],
   ask=["That last question matters. You want a version of the story that "
        "is useful and also safe to carry with you."]),

 (9, 1): dict(
   stop=["I think some transferable-skills advice gives experienced "
         "professionals false confidence."],
   hold=["Not because your experience does not transfer.",
         "Some of it absolutely can.",
         "The problem is that we spend so much time asking, What can I "
         "take with me? that we avoid the harder question: What am I "
         "leaving behind?",
         "Your judgment may travel. Your relationships may not. Your "
         "problem-solving may travel. Your knowledge of that company’s "
         "systems may not."],
   ask=["So I would not make a transferable-skills list.",
        "I would make four columns: What travels? What does not? What can "
        "I prove? What must I relearn?"]),
 (9, 2): dict(
   stop=["I know from experience that changing context does not mean "
         "starting from zero. But I also know that not everything comes "
         "with you."],
   hold=["Then ask what belonged to the old place. Internal "
         "relationships. Company systems. The language everyone understood "
         "without explaining it.",
         "Informal power. Knowing exactly who to call. Knowing how that "
         "company really gets things done.",
         "Those things can make you excellent where you are. But they may "
         "not mean much in the next place."],
   ask=["If someone asks why your experience should count in a new field, "
        "you do not have to say: “Everything I have done "
        "transfers.”",
        "Try something more honest: “The part of my experience that "
        "is most useful here is X. I have used it to solve Y kind of "
        "problem. The part I would need to build in your environment is "
        "Z.”"]),
 (9, 3): dict(
   stop=["The longer you stay in one place, the easier it is to confuse "
         "knowing the place with having something you can carry "
         "anywhere."],
   hold=["You know who to call. You know which meeting matters. You know "
         "which rule can bend and which one cannot.",
         "That is real expertise.",
         "But some of that expertise belongs to the environment, not only "
         "to you. That is why a move can feel humbling even when you have "
         "a lot of experience.",
         "The capability may still be there. The shortcuts are not."],
   ask=["Take one job you are thinking about. Make four columns: TRAVELS. "
        "DOES NOT TRAVEL. PROOF. RELEARN."]),

 (10, 1): dict(
   stop=["And now you feel this pressure to prove they made the right "
         "decision."],
   hold=["That pressure can make you do exactly the wrong thing.",
         "You start talking too much about what worked at your last "
         "company. You start trying to fix things before you understand "
         "why they work this way. Or you go the other direction. You stay "
         "quiet because you are afraid of getting something wrong.",
         "I do not think either one is the job of your first 90 days.",
         "Your first job is not to prove that everything you already know "
         "works here."],
   ask=["It is to figure out three things: What from my experience "
        "actually works here? What do I need to learn about this new "
        "context? And what can I begin to prove here?",
        "I think about that as READ. TEST. PROVE."]),
 (10, 2): dict(
   stop=["You can be experienced and still be new to the context."],
   hold=["I’ve been the new person many times across different roles "
         "and industries, and I’ve also spent years thinking about "
         "how people actually build capability at work.",
         "One thing those moves taught me is that experience and context "
         "are not the same thing.",
         "You can know how to work and still have a lot to learn about how "
         "this place works.",
         "Then you walk into a new company and suddenly you do not know "
         "which meeting actually matters. You do not know who really makes "
         "the decision. You do not know which rule is a real rule and "
         "which one is simply how the last person did it."],
   ask=["That is why I would not spend the first 90 days trying to prove "
        "that everything you already know works here. I would spend them "
        "finding the boundary between what you brought with you and what "
        "this environment still has to teach you."]),
 (10, 3): dict(
   stop=["I would have a very simple conversation with your manager."],
   hold=["Not, “How am I doing?” That question is broad enough "
         "to get you an answer like, “You’re doing great.”",
         "Ask something more useful: “What have you seen me pick up "
         "quickly?” “Where do I still need more context?” "
         "“Is there anything I am treating like my old environment "
         "that works differently here?”"],
   ask=["And ask: “What would you want to trust me with by the end of "
        "my first 90 days that you would not have trusted me with on day "
        "one?” That question turns the first 90 days into "
        "development, not performance theater."]),

 (11, 1): dict(
   stop=["You accepted one job. Then you started doing another. Maybe the "
         "title is the same. Maybe the salary is the same. But three or "
         "six weeks in, you are thinking: This is not the job I thought I "
         "accepted."],
   hold=["Before you call it a bait-and-switch, slow down. Roles change. "
         "Priorities move. Managers inherit new problems. Companies "
         "reorganize.",
         "But there is a point where normal change becomes something you "
         "need to look at more closely."],
   ask=["I use four questions for that: EXPECTED. ACTUAL. COST. CHOICE."]),
 (11, 2): dict(
   stop=["Start with EXPECTED. What did you reasonably believe you were "
         "accepting? Not the perfect version you imagined."],
   hold=["Then write ACTUAL. What is the job asking from you now? Do not "
         "judge it from one bad week. Look for the recurring pattern.",
         "Sometimes the actual role is better than the one you expected. "
         "You may have more scope, more visibility, or a better manager "
         "than the job description suggested.",
         "And sometimes the actual role is narrower. You were hired for "
         "strategy and spend most of your time coordinating. You expected "
         "to lead a team and the team never arrived. You were told a "
         "decision was yours and discover that you can only recommend."],
   ask=["Write EXPECTED and ACTUAL side by side.",
        "The question is not, “Is this exactly what was "
        "written?” The better question is, “Is the job I am "
        "doing still close enough to the job I agreed to build my life "
        "and career around?”"]),
 (11, 3): dict(
   stop=["What does the difference actually cost you? Not every mismatch "
         "deserves the same response."],
   hold=["I would look at four costs. CAPABILITY. Is this role building "
         "judgment, scope, and experience you want to carry forward? "
         "EVIDENCE. Will you be able to prove meaningful work from this "
         "version of the job?",
         "COMPENSATION. Has the scope changed enough that the pay, level, "
         "or agreement needs to be revisited? LIFE. Did the practical cost "
         "change: travel, hours, location, caregiving, health, or "
         "something else that mattered when you accepted?",
         "There can also be a positive cost calculation. The job may be "
         "different but better.",
         "A mismatch can be manageable in one category and unacceptable in "
         "another. You need to know which one you are actually reacting "
         "to."],
   ask=["Name one real cost. Then choose one next action: clarify, "
        "negotiate, test for a defined period, or begin planning another "
        "option."]),
}



def _clock(secs):
    return "%d:%02d" % (secs // 60, secs % 60)


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
                        secs=int(round(w / float(WPM) * 60)),
                        clock=_clock(int(round(w / float(WPM) * 60)))))
    return out



# --------------------------------------------------------------- opening
# One opening and one payoff per candidate. The on-screen words are lifted
# from that Short's own spoken lines, the visual is an existing card family
# from this video reframed to 9:16, and the sound event names the exact
# spoken word it lands on. Nothing here is a second ask and nothing here
# reveals the answer before the Short earns it.
OPEN = {
 (4, 1): dict(text="But those hours were not always wasted.",
   visual="CAMERA", audio="wasted",
   mid=[("who gets the experience that used to come from doing it",
         "NEW_V4_FS_01_WHO_GETS_THE_EXPERIENCE")],
   payoff="NEW_V4_FS_04_THE_REAL_QUESTION"),
 (4, 2): dict(text="A task can be boring and still teach you something.",
   visual="NEW_V4_FS_02_INEFFICIENT_AND_DEVELOPMENTAL", audio="boring",
   mid=[("helps you notice patterns", "NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT")],
   payoff="NEW_V4_FS_07_WHAT_DID_IT_TEACH"),
 (4, 3): dict(text="built from hundreds of smaller decisions",
   visual="CAMERA", audio="title",
   mid=[("That does not mean the future is doomed.",
         "NEW_V4_FS_09_NOT_ONE_OUTCOME")],
   payoff="NEW_V4_FS_06_MOVED_OR_REMOVED"),

 (5, 1): dict(text="one of the reasons you stop growing",
   visual="CAMERA", audio="growing",
   mid=[("Something breaks, they call you.",
         "NEW_V5_FS_01_NEEDED_NOT_GROWN"),
        ("Dependence sounds like", "NEW_V5_FS_08_DEPENDENCE_VS_DEVELOPMENT")],
   payoff="NEW_V5_FS_08_DEPENDENCE_VS_DEVELOPMENT"),
 (5, 2): dict(text="Being useful can feel like career security.",
   visual="CAMERA", audio="security",
   mid=[("That does not mean they are plotting against you.",
         "NEW_V5_FS_02_NOT_ALIGNED")],
   payoff="NEW_V5_FS_04_THE_QUESTION"),
 (5, 3): dict(text="set a time to review it",
   visual="NEW_V5_FS_09_REVIEW_POINT", audio="90 days",
   mid=[], payoff="NEW_V5_FS_09_REVIEW_POINT"),

 (6, 1): dict(text="not the same as setting the strategy",
   visual="CAMERA", audio="strategy",
   mid=[("look at the verbs", "NEW_V6_FS_08_READ_THE_VERBS")],
   payoff="NEW_V6_FS_14_AUTHORITY_POSTURES"),
 (6, 2): dict(text="Senior Divisional Strategy Consultant, Governance.",
   visual="NEW_V6_FS_01_TITLE_ONLY", audio="Governance",
   mid=[("the bottom of the pay range was $61,500",
         "NEW_V6_FS_02_THE_CONTRADICTION")],
   payoff="NEW_V6_FS_02_THE_CONTRADICTION"),
 (6, 3): dict(text="The title does not tell you much.",
   visual="NEW_V6_FS_13_ACRONYM_WALL", audio="Compliance",
   mid=[("the highest published pay ceiling", "NEW_V6_FS_15_CEILING")],
   payoff="NEW_V6_FS_16_READ_THE_WORK"),

 (7, 1): dict(text="Both dependable. Both experienced. Both working hard.",
   visual="CAMERA", audio="hard",
   mid=[("the difference is not always who worked harder",
         "NEW_V7_FS_01_NOT_ALWAYS_WHO_WORKED_HARDER"),
        ("Access matters.", "NEW_V7_FS_05_NOT_MERIT")],
   payoff="NEW_V7_FS_02_TWO_QUESTIONS"),
 (7, 2): dict(text="Ask what kind of responsibility.",
   visual="CAMERA", audio="responsibility",
   mid=[("What decisions will I get to make?",
         "NEW_V7_FS_07_ASK_WHAT_KIND")],
   payoff="NEW_V7_FS_08_CHANGES_THE_CONVERSATION"),
 (7, 3): dict(text="evidence for your current role, not the next one",
   visual="CAMERA", audio="every day",
   mid=[("The problem may be that the evidence people see",
         "NEW_V7_FS_06_EVIDENCE_FOR_WHICH_ROLE")],
   payoff="NEW_V7_FS_13_CTA"),

 (8, 1): dict(text="You cannot.",
   visual="CAMERA", audio="You cannot.",
   mid=[("You remember doing good work.", "NEW_V8_FS_01_MEMORY_NOT_PROOF")],
   payoff="NEW_V8_FS_02_FIVE_KINDS"),
 (8, 2): dict(text="Keep the proof.",
   visual="CAMERA", audio="property",
   mid=[("The goal is not to keep", "NEW_V8_FS_04_NOT_THE_ARTIFACT")],
   payoff="NEW_V8_FS_03_KEEP_THE_PROOF"),
 (8, 3): dict(text="later is often when the details are hardest to remember",
   visual="NEW_V8_FS_06_THE_DETAILS_BLUR", audio="later",
   mid=[("Once a month, take ten minutes", "NEW_V8_FS_07_TEN_MINUTE_HABIT")],
   payoff="NEW_V8_FS_07_TEN_MINUTE_HABIT"),

 (9, 1): dict(text="What am I leaving behind?",
   visual="CAMERA", audio="false confidence",
   mid=[("Your judgment may travel.", "NEW_V9_FS_01_INCOMPLETE_QUESTION")],
   payoff="NEW_V9_FS_03_FOUR_QUESTIONS"),
 (9, 2): dict(text="not everything comes with you",
   visual="CAMERA", audio="zero",
   mid=[("Internal relationships.",
         "NEW_V9_FS_05_TIED_TO_THE_OLD_CONTEXT")],
   payoff="NEW_V9_FS_06_WHAT_CAN_ANOTHER_PERSON_SEE"),
 (9, 3): dict(text="The shortcuts are not.",
   visual="CAMERA", audio="anywhere",
   mid=[("That is real expertise.",
         "NEW_V9_FS_11_FLUENCY_AND_PORTABILITY")],
   payoff="NEW_V9_FS_09_FOUR_COLUMNS"),

 (10, 1): dict(text="pressure to prove they made the right decision",
   visual="CAMERA", audio="wrong thing",
   mid=[("It is to figure out three things",
         "NEW_V10_FS_01_READ_TEST_PROVE")],
   payoff="NEW_V10_FS_01_READ_TEST_PROVE"),
 (10, 2): dict(text="You can be experienced and still be new to the context.",
   visual="NEW_V10_FS_02_EXPERIENCED_BUT_NEW", audio="context",
   mid=[("which rule is a real rule", "NEW_V10_FS_04_FORMAL_VS_REAL")],
   payoff="NEW_V10_FS_02_EXPERIENCED_BUT_NEW"),
 (10, 3): dict(text="Not, “How am I doing?”",
   visual="NEW_V10_FS_06_MANAGER_CONVERSATION", audio="manager",
   mid=[("What would you want to trust me with",
         "NEW_V10_FS_07_THE_DAY_90_QUESTION")],
   payoff="NEW_V10_FS_07_THE_DAY_90_QUESTION"),

 (11, 1): dict(text="This is not the job I thought I accepted.",
   visual="CAMERA", audio="accepted",
   mid=[("Roles change. Priorities move.",
         "NEW_V11_FS_05_TEMPORARY_OR_NOT")],
   payoff="NEW_V11_FS_01_FOUR_QUESTIONS"),
 (11, 2): dict(text="Start with EXPECTED.",
   visual="NEW_V11_FS_02_WRITE_IT_DOWN", audio="EXPECTED",
   mid=[("And sometimes the actual role is narrower.",
         "NEW_V11_FS_03_EXPECTED_VS_ACTUAL")],
   payoff="NEW_V11_FS_04_THE_REAL_QUESTION"),
 (11, 3): dict(text="What does the difference actually cost you?",
   visual="CAMERA", audio="cost",
   mid=[("I would look at four costs.",
         "NEW_V11_FS_06_FOUR_COST_LENSES")],
   payoff="NEW_V11_FS_12_NAME_THE_DIFFERENCE"),
}


# ------------------------------------------------------- regression rules
# Each rule below was written from a named defect in the independent review
# of the delivered archive. They are regression fixtures: if a future edit
# reintroduces the defect, the rule fires.

# A Short that names a count must carry every member of that list.
LISTS = [
 (11, 3, "four costs", ["CAPABILITY", "EVIDENCE", "COMPENSATION", "LIFE"]),
 (11, 1, "four questions", ["EXPECTED", "ACTUAL", "COST", "CHOICE"]),
 (9, 1, "four columns", ["What travels?", "What does not?",
                         "What can I prove?", "What must I relearn?"]),
 (9, 3, "four columns", ["TRAVELS", "DOES NOT TRAVEL", "PROOF", "RELEARN"]),
 (10, 1, "three things", ["actually works here", "learn about this new "
                          "context", "begin to prove here"]),
 (8, 1, "five things", ["baseline", "scope", "the decision that was yours",
                        "the result", "how the result was judged"]),
 (6, 1, "four things", ["PROBLEM", "AUTHORITY", "PROOF", "REAL GAP"]),
 (6, 1, "look at the verbs", ["decide", "Lead", "Negotiate", "Recommend",
                              "Influence", "Support", "Execute"]),
 (5, 3, "set a time to review it",
  ["What became permanent?", "What did I learn?",
   "What decisions became mine?",
   "What recognition or role change comes with this?",
   "What am I taking off my plate?"]),
 (8, 2, "taking company property",
  ["confidential documents", "customer data", "private reports",
   "screenshots", "source code", "internal financial information"]),
 (8, 3, "take ten minutes and write down",
  ["What changed?", "What was mine?", "What was hard?",
   "What proof do I have?",
   "What would I be allowed to say outside this company?"]),
 (9, 2, "what belonged to the old place",
  ["Internal relationships", "Company systems",
   "The language everyone understood", "Informal power",
   "Knowing exactly who to call",
   "Knowing how that company really gets things done"]),
 (9, 3, "knowing the place",
  ["You know who to call", "You know which meeting matters",
   "which rule can bend and which one cannot"]),
 (7, 2, "what kind of responsibility",
  ["What decisions will I get to make?",
   "What problem will I own from beginning to end?",
   "What level of stakeholder will I work with?",
   "What evidence would show that I am ready for the next level?"]),
 (11, 2, "the actual role is narrower",
  ["Sometimes the actual role is better", "more scope",
   "more visibility", "a better manager"]),
]

# A referring expression may only appear after the thing it refers to.
ANTECEDENTS = [
 (10, 1, "either one", "You stay quiet because you are afraid of getting "
                       "something wrong."),
 (10, 1, "the other direction", "You start trying to fix things"),
 (10, 1, "It is to figure out", "Your first job is not to prove"),
 (10, 2, "those moves", "I’ve been the new person many times"),
 (10, 2, "I would spend them", "the first 90 days"),
 (4, 3, "those smaller decisions", "hundreds of smaller decisions"),
 (4, 3, "the future is doomed", "companies may discover the problem much "
                                "later"),
 (6, 1, "look at the verbs", "I look for four things"),
 (11, 2, "Then write ACTUAL", "Start with EXPECTED"),
 (11, 3, "which one you are actually reacting to", "COMPENSATION"),
 (7, 3, "practice it where someone can see", "Pick one kind of next-level "
                                             "work"),
 (8, 1, "was the improvement 27% or 37%", "an interviewer asks"),
 (9, 2, "Then ask what belonged to the old place",
        "not everything comes with you"),
 (10, 3, "Not, “How am I doing?”",
         "a very simple conversation with your manager"),
 (7, 1, "the difference has nothing to do with capability",
        "the difference is not always who worked harder"),
 (6, 2, "Sounds pretty senior, right?",
        "Senior Divisional Strategy Consultant, Governance"),
 (11, 3, "A mismatch can be manageable in one category",
         "I would look at four costs"),
 (5, 1, "Once you can see that difference",
        "Dependence sounds like"),
]

# The ask may not defer the payoff to a video the viewer is not watching.
TRAILER = ["i want to unpack", "i am going to show you", "in the next 10 "
           "minutes", "by the end of this video", "by the end, i will",
           "by the end, put", "later i will", "stay with me",
           "we will come back", "in a few minutes", "as we go",
           "i will give you", "that is the problem i want"]

# The ask is one ask.
PROMO = ["watch “", "subscribe", "link in", "comment below",
         "next video", "full video", "part two"]


def audit(n):
    """Editorial regressions, reported as failures with their rule id."""
    bad = []
    for num in (1, 2, 3):
        d = SHORTS[(n, num)]
        body = R.S._norm(" ".join(lines(n, num)))
        low = body.lower()
        askl = R.S._norm(" ".join(d["ask"])).lower()
        tag = "V%d S%d" % (n, num)
        for v, m, trigger, items in LISTS:
            if (v, m) != (n, num):
                continue
            if R.S._norm(trigger).lower() not in low:
                bad.append("%s LIST: says nothing about '%s'" % (tag,
                                                                 trigger))
                continue
            for it in items:
                if R.S._norm(it).lower() not in low:
                    bad.append("%s LIST: names %s but omits '%s'"
                               % (tag, trigger, it))
        for v, m, ref, ante in ANTECEDENTS:
            if (v, m) != (n, num):
                continue
            r = R.S._norm(ref).lower()
            a = R.S._norm(ante).lower()
            if r not in low:
                bad.append("%s ANTECEDENT: fixture phrase '%s' is gone; "
                           "re-point the rule" % (tag, ref))
            elif a not in low:
                bad.append("%s ANTECEDENT: '%s' has no antecedent ('%s')"
                           % (tag, ref, ante))
            elif low.index(a) > low.index(r):
                bad.append("%s ANTECEDENT: '%s' arrives before '%s'"
                           % (tag, ref, ante))
        for t in TRAILER:
            if t in askl:
                bad.append("%s TRAILER: the ask defers the payoff ('%s')"
                           % (tag, t))
        for t in PROMO:
            if t in askl:
                bad.append("%s PROMO: a second ask is stacked ('%s')"
                           % (tag, t))
        if len(d["ask"]) > 2:
            bad.append("%s ASK: %d ask blocks; one natural action only"
                       % (tag, len(d["ask"])))
        o = OPEN[(n, num)]
        if R.S._norm(o["text"]).lower() not in low:
            bad.append("%s OPENING: on-screen text is not the Short's own "
                       "wording" % tag)
        if R.S._norm(o["audio"]).lower() not in low:
            bad.append("%s OPENING: the sound event lands on a word the "
                       "Short never says" % tag)
        for trig, fam in o["mid"]:
            if R.S._norm(trig).lower() not in low:
                bad.append("%s CUTAWAY: '%s' is not spoken in this Short"
                           % (tag, trig[:40]))
        secs = rows(n)[num - 1]["secs"]
        if secs > 59:
            bad.append("%s LENGTH: %d seconds at %d wpm exceeds the Short "
                       "ceiling" % (tag, secs, WPM))
    return bad


def families(n):
    """Every card family this video's Shorts reuse."""
    out = []
    for num in (1, 2, 3):
        o = OPEN[(n, num)]
        for k in [o["visual"]] + [f for _, f in o["mid"]] + [o["payoff"]]:
            if k != "CAMERA" and k not in out:
                out.append(k)
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
            print("     %d  %-52s %3d words  about %s"
                  % (r["num"], r["title"][:52], r["words"], r["clock"]))
    print("\nlines not verbatim: %d" % tot)
