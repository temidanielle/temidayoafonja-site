# -*- coding: utf-8 -*-
"""Restored full-depth scripts for Videos 6, 7 and 8.

The compression pass that produced the September 11 V6, V7 and V8 masters cut
roughly half the approved teaching. This module puts it back.

The rule, in order of preference:

  CUR         the corrected September 11 master's own speech, unchanged. The
              stronger hooks, the current architecture and the current
              framework headings are kept.
  SEP09       previously approved speech, word for word.
  SEP09-SPLIT previously approved speech with a sentence removed because the
              corrected master already says it. Nothing is added.
  SEP09-ADJ   previously approved speech with a minimal adjustment, recorded
              in full. Only where the corrected master's wider scope or a
              changed destination title makes the old wording wrong.
  BRIDGE      genuinely new connecting language. Every instance is flagged,
              never placed silently.

Provenance travels with every paragraph so the change log is generated from
the script rather than asserted about it.
"""

CUR, SEP09, SPLIT, ADJ, BRIDGE = ("CUR", "SEP09", "SEP09-SPLIT",
                                  "SEP09-ADJ", "BRIDGE")


def P(text, src, note=""):
    return dict(text=text, src=src, note=note)


# =====================================================================  V6
V6 = [
 ("HOOK | Movement can look like growth before the work changes", [
  P("I have worked across eight industries and sectors, and one thing that "
    "taught me is that movement can look like career growth long before the "
    "work actually changes.", CUR),
  P("A role can come with more money, more visibility, a more senior title, "
    "and a different company name, and still leave you solving almost the "
    "same class of problem.", CUR),
  P("Another role can barely change the title and completely change what you "
    "are capable of doing a year later.", CUR),
  P("So when I judge a new role now, I want three things answered: will the "
    "Work change, will my Judgment expand, and will the Evidence travel?",
    CUR),
 ]),
 ("WHY THIS GETS HARDER LATER IN YOUR CAREER", [
  P("Earlier in a career, almost any new responsibility can teach you "
    "something. Later, the question becomes more selective: is this role "
    "expanding what you can carry, or is it simply using more of what you "
    "already know?", CUR),
  P("A role does not have to maximize growth to be a good decision. You may "
    "choose for pay, flexibility, stability, location, health, family, or a "
    "manager you trust. Those are real reasons.", CUR),
  P("The problem is calling every move development when the work underneath "
    "it has barely changed.", CUR),
 ]),
 ("1 | WORK: Will the problem actually change?", [
  P("Start with an ordinary Monday. What will actually be different? What "
    "problems will you own? Which customers, systems, regulations, operating "
    "models, or stakeholders will you have to understand that you do not "
    "understand today?", CUR),
  P("Do not let words like strategic, transformation, enterprise, or visible "
    "do the work for the hiring manager. Ask what this person will be "
    "expected to make happen and what will be difficult about it.", CUR),
  P("Ask the hiring manager three things: What are the most important "
    "problems this person will own in the first six months? What will I have "
    "to learn that I do not already know? What will I understand differently "
    "because I held this role?", ADJ,
    "September 9 read 'Ask the internal hiring manager three things'. The "
    "corrected Video 6 covers external moves as well as internal ones, so "
    "'internal' is dropped. Nothing else changed."),
  P("A move can be significant even if the title barely changes. A different "
    "problem environment can build range. The reverse is also true: a larger "
    "title can hide more volume of the same work.", CUR),
 ]),
 ("2 | JUDGMENT: Will your decision rights expand?", [
  P("Responsibility is not the same as judgment. You can own the deadline "
    "while somebody else still controls scope, resources, sequence, and the "
    "decision that determines whether the deadline is possible.", CUR),
  P("Dependable people often get more responsibility before they get more "
    "judgment.", SEP09),
  P("More tasks can mean volume, coordination, and absorption. More judgment "
    "means interpreting incomplete information, weighing tradeoffs, "
    "recommending a direction, influencing people with different incentives, "
    "or owning the consequence when the instructions stop being clear.",
    SEP09),
  P("Preparing a report is work. Deciding which pattern in the report "
    "matters, explaining the consequence, and recommending what happens next "
    "requires different judgment.", SEP09),
  P("Ask: where will I have to make a call when the instructions are "
    "incomplete? Which tradeoffs will belong to me? What recommendation will "
    "I be expected to make when two reasonable options conflict? What can I "
    "influence when the plan is not working?", CUR),
  P("If the answer is simply, 'You will have more to manage,' that is not "
    "enough information.", SEP09),
  P("You do not need complete control. Very few roles have it. But if "
    "accountability is growing and your judgment has nowhere to go, keep "
    "investigating.", CUR),
 ]),
 ("3 | EVIDENCE: Will you be able to prove the growth somewhere else?", [
  P("Imagine you take the role, do it for a year, and then have to explain "
    "what changed to somebody who has no history with you.", CUR),
  P("Could you name the problem, your role, the judgment you used, and a "
    "permitted result without relying on internal acronyms or your "
    "reputation inside that company?", CUR),
  P("I look for three kinds of return: a result I can support, judgment I "
    "can explain, and range I did not have before. If the role produces none "
    "of those, I want to know what I am getting instead.", CUR),
  P("Result: What changed, improved, stabilized, accelerated, or became "
    "possible?", SEP09),
  P("Judgment: What did you notice, weigh, recommend, or decide?", SEP09),
  P("Range: What new context, stakeholder group, system, or problem can you "
    "now handle?", SEP09),
  P("The strongest moves eventually let you say: 'I entered a new context. I "
    "was trusted to make this kind of judgment. Here is what changed.'", ADJ,
    "September 9 read 'The strongest internal moves'. 'internal' is dropped "
    "for the corrected video's wider scope. Nothing else changed."),
  P("Before you accept, ask how success is measured, which outcomes you "
    "would actually own, and what a strong first year would allow you to "
    "point to.", SEP09),
 ]),
 ("READ THE THREE ANSWERS", [
  P("Now put the three answers together.", SEP09),
  P("If all three are yes, different work, expanded judgment, and evidence "
    "that travels, the developmental case is strong. That does not mean the "
    "move is automatically right. It means you can see what the work is "
    "likely to build.", SEP09),
  P("If two are yes, identify the missing dimension. The role may be worth "
    "negotiating rather than rejecting. New work and strong evidence with "
    "vague decision authority, for example, gives you a very specific "
    "conversation to have.", SEP09),
  P("If zero or one is yes, the opportunity may be movement without much "
    "growth. It may still be the right choice for reasons that matter in "
    "your real life. Just be accurate about what the work is giving you.",
    SEP09),
  P("And do not assume the external option automatically wins. A new "
    "employer can give you a new logo and the same work. Compare the actual "
    "access to different work, stronger judgment, and clearer evidence.",
    SEP09),
 ]),
 ("THE 12-MONTH QUESTION", [
  P("Then ask one question: twelve months from now, what will I be able to "
    "do, decide, or prove that I cannot do today?", CUR),
  P("If the answer is specific, you can see the developmental value. If the "
    "answer is mostly, 'I will be busier, more visible, and managing more of "
    "the same,' you have learned something important.", CUR),
  P("You may still take the role. Just take it for the reason it actually "
    "serves.", CUR),
 ]),
 ("WHAT THIS TEST CANNOT SOLVE", [
  P("These three questions read the work. They do not replace the rest of "
    "the decision.", SEP09),
  P("Your company may not contain the work you need. A current manager may "
    "control access. An old reputation may follow you. Compensation bands or "
    "organizational politics may limit what is possible. Bias and age "
    "discrimination can shape who gets access to opportunities.", SEP09),
  P("And career decisions sit inside real lives. Compensation, caregiving, "
    "benefits, immigration status, health, safety, energy, stability, and "
    "timing can legitimately outweigh the developmental case.", SEP09),
  P("If the environment is harming your health or safety, or you are dealing "
    "with harassment, discrimination, or another urgent threat, protecting "
    "yourself and getting appropriate support comes first.", SEP09),
 ]),
 ("CLOSE | Make a cleaner yes, no, or negotiate decision", [
  P("Before your next move, write one sentence under Work, Judgment, and "
    "Evidence. If one area is weak, ask whether it can be redesigned before "
    "you accept.", CUR),
  P("What different work will I enter? What judgment will I be trusted to "
    "carry? What evidence could I explain a year from now?", SPLIT,
    "September 9 set these three questions as separate lines under 'Before "
    "your next internal conversation, write one sentence under each "
    "question'. That lead-in is dropped because the corrected master's own "
    "line above already says it. The three questions are unchanged."),
  P("Maybe the role needs a clearer decision right. Maybe you need access to "
    "a different stakeholder group. Maybe temporary scope needs a review "
    "point.", CUR),
  P("If you are actively deciding whether to stay, move internally, or "
    "leave, the free Career Decision Evidence Check gives you a structured "
    "way to read the evidence behind that choice. It is linked below.",
    SEP09),
  P("A different title can be useful. But a bigger title and a bigger career "
    "are not automatically the same thing.", CUR),
 ]),
 ("WATCH NEXT | Final visual", [
  P("And before you call any opportunity growth, there is one more "
    "distinction you need to make.", SEP09),
  P("More responsibility can mean you are growing. It can also mean the "
    "organization has learned that you will absorb more.", SEP09),
  P("That is what we are testing next in 'It Took Me Years to Stop "
    "Mistaking More Work for Career Growth.'", ADJ,
    "September 9 named the destination by its former title, 'Are You "
    "Growing, or Just Being Given More Work?'. Video 7's corrected master "
    "carries a different title, so the destination is named by the title it "
    "actually has. Nothing else changed."),
 ]),
]


# =====================================================================  V7
V7 = [
 ("HOOK | More valuable to the company, not necessarily to your future", [
  P("You can become more valuable to your organization without becoming more "
    "valuable to your own future.", CUR),
  P("It took me years to learn that being trusted with more is not the same "
    "as being developed for more.", CUR),
  P("A colleague leaves. A project has no clear owner. Your manager asks, "
    "'Can you take this too?' You do, because you can. Six months later your "
    "scope is bigger, your calendar is fuller, and everybody describes it as "
    "growth.", CUR),
  P("Maybe it is. Or maybe the organization has simply learned that you can "
    "absorb more.", CUR),
  P("I use three tests now: Complexity, Authority, Return. CAR.", CUR),
 ]),
 ("WHY DEPENDABLE PEOPLE ARE VULNERABLE TO THIS", [
  P("Reliability attracts work quickly. Authority, support, recognition, and "
    "formal scope often arrive later, if they arrive at all.", CUR),
  P("The workload trap usually starts reasonably: a vacancy, a launch, a "
    "project in trouble. None of those requests is automatically a problem.",
    SEP09),
  P("That is why the workload trap can feel flattering at first. You are the "
    "person people trust. Then temporary coverage quietly becomes the "
    "permanent design of your job.", CUR),
  P("The question is not whether more work is bad. Some of the best growth "
    "opportunities begin outside the job description. The question is what "
    "the extra work is building in you and what it returns.", CUR),
 ]),
 ("C | COMPLEXITY: Did the problem get harder, or did the volume get bigger?",
  [
  P("If you managed three nearly identical projects last year and now manage "
    "eight, your capacity is being used more heavily. You may be faster, "
    "more organized, and more resilient. That is not automatically a new "
    "class of problem.", CUR),
  P("Complexity changes when the variables change: a new customer, a new "
    "regulation, a different operating model, conflicting priorities, "
    "incomplete instructions, stakeholders whose incentives do not line up.",
    CUR),
  P("A useful test is this: Could the answer that worked last time simply be "
    "copied? If yes, you may be doing more. If no, and you now have to "
    "diagnose, interpret, or make tradeoffs, the work may be becoming more "
    "complex.", SEP09),
  P("Ask: what variables are new? What ambiguity am I now expected to "
    "handle? What can I credibly do now that I could not credibly do before? "
    "If the only answer is 'more of the same,' call that capacity use. Do "
    "not automatically call it growth.", CUR),
 ]),
 ("A | AUTHORITY: Did your decision rights move with the responsibility?", [
  P("Responsibility is what you are expected to carry. Accountability is "
    "what you will answer for. Authority is what you can influence or "
    "decide. Those three do not always expand together.", CUR),
  P("You can own a deadline and still be unable to reduce scope. You can be "
    "accountable for a program and still be unable to secure the people it "
    "requires. You can attend more senior meetings and still be there mainly "
    "to report.", CUR),
  P("Exposure can be useful. Observation is part of learning. But sustained "
    "accountability without any growing decision rights, access, or support "
    "is not much of a development plan.", SEP09),
  P("Ask: which decisions now belong to me? What can I change when the plan "
    "is not working? Where am I expected to recommend a direction rather "
    "than only execute one? Your judgment should have somewhere to go.", CUR),
  P("You do not need complete control. Very few roles have that.", SEP09),
 ]),
 ("R | RETURN: What is the extra work giving back?", [
  P("Extra responsibility costs time, attention, and energy. Something "
    "should be coming back. That return does not have to be an immediate "
    "promotion.", CUR),
  P("A stretch assignment can be worth it because it builds capability you "
    "did not have, gives you evidence you could not previously claim, or "
    "creates recognition tied to the contribution.", CUR),
  P("I look in three places: capability, evidence, and recognition.", CUR),
  P("Capability: What can you handle now that you could not handle before?",
    SEP09),
  P("Evidence: What permitted result can you explain?", SEP09),
  P("Recognition: Has the expanded contribution been acknowledged through "
    "decision authority, formal scope, compensation, title, sponsorship, or "
    "a credible review point?", SEP09),
  P("Praise is welcome. Praise alone is not role design.", CUR,
    "Moved to sit after the three definitions, which is where the September "
    "9 master placed it. The line itself is unchanged."),
  P("Some worthwhile assignments will return more in one category than "
    "another. You may gain capability before the title catches up. You may "
    "accept a defined period of extra load because the evidence will be "
    "unusually valuable.", SEP09),
  P("But the return should be real, and the time boundary should be clear.",
    SEP09),
  P("Ask: How long is this expanded scope expected to last? What will "
    "success make possible? How will the role be reviewed? What evidence "
    "will I be able to point to six or twelve months from now?", SEP09),
 ]),
 ("READ THE CAR PATTERN", [
  P("Now read the three together.", SEP09),
  P("If Complexity, Authority, and Return are all expanding, the career case "
    "for growth is visible. The work may still be demanding, but you can see "
    "what it is building.", SEP09),
  P("If Complexity is increasing but Authority or Return has not caught up, "
    "you may be in a stretch assignment with a design problem. The next "
    "conversation is about decision rights, support, what comes off your "
    "plate, and when the arrangement gets reviewed.", SEP09),
  P("If volume increased but Complexity, Authority, and Return did not, the "
    "role has expanded mainly as workload.", SEP09),
  P("That may be acceptable for a short season, especially during a launch, "
    "vacancy, or transition. Just give the season a boundary. Temporary "
    "coverage without a review date has a way of becoming the new baseline.",
    SEP09),
  P("And this is not a moral judgment about every extra task. Growth can be "
    "tiring. Sometimes you make a deliberate trade because family, finances, "
    "visa, benefits, or timing require it.", SEP09),
  P("The purpose of the CAR test is accuracy. Know whether the cost you are "
    "carrying is building something you can use, or mostly consuming the "
    "space where development might have happened.", SEP09),
 ]),
 ("USE CAR BEFORE YOU SAY YES TO MORE", [
  P("CAR is not a score. You are looking for a pattern.", CUR),
  P("Before the next 'Can you take this too?', ask: what becomes more "
    "complex? What authority comes with it? When will we review what this "
    "additional scope returns?", CUR),
  P("That last question matters. Temporary stretch without a review point "
    "has a way of becoming permanent absorption.", CUR),
 ]),
 ("THE SCOPE CONVERSATION", [
  P("Before your scope expands again, look back at the responsibilities "
    "added during the last six to twelve months.", SEP09),
  P("For each one, write three things: What became more complex? What can I "
    "now influence or decide? What did the work return?", SPLIT,
    "September 9 set the three items as separate lines under 'For each one, "
    "write three things:'. They are joined into one spoken paragraph. No "
    "word changed."),
  P("Then take four questions into the conversation with your manager: "
    "Which of these responsibilities should remain with me? What should come "
    "off my plate as this becomes part of my role? Which decisions need to "
    "belong to me for these outcomes? How and when will the expanded scope "
    "be formally reviewed?", SPLIT,
    "September 9 set the four questions as separate lines under 'Then take "
    "four questions into the conversation with your manager:'. They are "
    "joined into one spoken paragraph. No word changed."),
  P("That is a stronger conversation than saying only, 'I have too much "
    "work.' It makes the design of the role visible: priorities, authority, "
    "support, and return.", SEP09),
 ]),
 ("CLOSE | Stop using workload as the growth metric", [
  P("Run CAR on one responsibility you have added in the last six months.",
    CUR),
  P("If Complexity, Authority, and Return all moved, you may be looking at "
    "real growth. If the only thing that moved was volume, name it "
    "accurately.", CUR),
  P("If you want a structured way to examine what your current work is "
    "actually building in you, the Capability Formation Field Kit helps you "
    "read the evidence in your role, see where your options may be expanding "
    "or narrowing, and identify where the role may need a boundary or "
    "redesign. It is linked below.", SEP09),
  P("More work can be part of growth. It is not proof of it.", CUR),
 ]),
 ("WATCH NEXT | Final visual", [
  P("There is another problem that often appears after you have done "
    "genuinely difficult growth work.", SEP09),
  P("Sometimes the work had no blueprint, no existing measure, and no "
    "obvious language for what you built. That can make a valuable chapter "
    "look vague on paper.", SEP09),
  P("In the next video, I will show you how to make that work visible: 'How "
    "to Show Your Impact at Work When You Built It From Scratch.'", SEP09),
 ]),
]


# =====================================================================  V8
# The corrected master's four-part architecture is the structure. The
# September 9 master is the depth source. Approved material is placed under
# the heading whose job it actually does, not under the heading it happened
# to sit beneath before, and every move is recorded.
V8 = [
 ("HOOK | Success can hide how hard the work was", [
  P("One of the strangest things about building something from scratch is "
    "that if you do it well enough, eventually nobody can see how hard it "
    "was.", CUR),
  P("The process exists. People use it. The decisions have become routine. "
    "And now the uncertainty you had to solve at the beginning has "
    "disappeared from view.", CUR),
  P("I have been the first person in a role more than once. In one of those "
    "roles, inside a regulated life sciences organization, I was brought in "
    "to build a capability function that did not exist in that form before.",
    CUR),
  P("Once foundational work starts operating, 'I built it' is not enough. A "
    "person who was not there still cannot see what was missing, what you "
    "had to work out, or what the evidence actually supports.", CUR),
  P("So I use four things: the Before, My Part, the Judgment, and the "
    "Proof.", CUR),
 ]),
 ("THE PROBLEM | Finished work hides unfinished conditions", [
  P("Foundational work is easy to lose because the finished thing hides the "
    "conditions you started with.", CUR),
  P("You say, 'I built the process.' The listener sees a process. You say, "
    "'I created the framework.' They see a framework. What they do not see "
    "is the uncertainty before it existed: conflicting expectations, the "
    "missing rule, the tradeoffs, the decisions that had no obvious owner.",
    CUR),
  P("Listen to this sentence: 'I built a leadership framework.' It names an "
    "output. It does not tell you why that output was needed or what had to "
    "be worked out before it could exist.", SEP09),
  P("Leadership expectations were already there. The missing connection was "
    "between those expectations, the decisions managers needed to make, and "
    "the operating situations where they would use them.", SPLIT,
    "September 9 opened this paragraph with 'In a regulated life-sciences "
    "organization, I was brought in to build a capability function that did "
    "not exist.' That sentence is dropped because the corrected master's "
    "hook already says it. The rest is unchanged."),
  P("I led work on an enterprise leadership capability framework and a "
    "manager enablement approach.", SEP09),
  P("That is the public, high-level account. I am not claiming I created "
    "every part alone or that every manager became more capable because the "
    "framework existed.", SEP09),
  P("But now you can hear the problem behind the output. The contribution "
    "was not simply that a framework appeared. It was working out how broad "
    "expectations could become usable in real management decisions.", SEP09),
  P("The solution is not to make the story more dramatic. It is to put the "
    "missing information back.", CUR),
 ]),
 ("1 | BEFORE: Reconstruct what was true before your solution", [
  P("Ask: what could people not do consistently? What decision had no shared "
    "rule? What had to be renegotiated every time because there was no "
    "agreed way through?", CUR),
  P("Be careful with 'nothing existed before me.' People may already have "
    "been doing useful work informally. Your contribution may have been "
    "connecting it, making it repeatable, clarifying ownership, or giving it "
    "a place to sit.", CUR),
  P("Imagine you built an intake process for a team. Requests used to arrive "
    "through several channels. Different people made priority decisions, and "
    "nobody had agreed which requests needed escalation.", SEP09),
  P("A weak Before is 'It was chaos.' A stronger Before is 'There was no "
    "shared way to prioritize requests or decide which issues needed "
    "escalation.'", CUR),
  P("That tells the listener what problem the process was supposed to "
    "solve.", SEP09),
  P("And do not turn the before into a number you never measured. If you do "
    "not know the old turnaround time, do not invent one because a "
    "percentage sounds more persuasive.", SEP09),
  P("Your first sentence is: 'Before this work, people could not "
    "consistently...' Finish it with the actual problem.", SPLIT,
    "September 9 set the sentence stem and its instruction as three "
    "separate lines. They are joined into one spoken paragraph. No word "
    "changed."),
 ]),
 ("2 | MY PART: Make attribution accurate", [
  P("Now name your part. If somebody else held the final decision, say you "
    "developed the options or made the recommendation. If the team designed "
    "the process, name the part you led.", CUR),
  P("You do not need sole credit to make your contribution legible. You need "
    "accurate attribution.", CUR),
  P("A stronger version of the example is: 'I helped the team agree a common "
    "triage approach, including which requests needed escalation and who "
    "could change priorities.' That tells me far more about your "
    "contribution than 'I created a form.'", SEP09,
    "September 9 placed this under 'Show the judgment'. It is moved to MY "
    "PART, where it does its actual job: it is a worked example of naming "
    "your part accurately rather than naming the artifact. No word changed."),
 ]),
 ("3 | JUDGMENT: Show what was not obvious", [
  P("Next, show what you had to work out. Not every action. The decisions "
    "that made the solution usable.", SPLIT,
    "September 9 set 'Next, show what you had to work out.' and 'Not every "
    "action. The decisions that made the solution usable.' as two lines. "
    "They are joined into one spoken paragraph. No word changed."),
  P("If you created an intake form, the form may be the least interesting "
    "part. The judgment could have been deciding what the team would accept, "
    "what required an exception, who could change priority, or how two "
    "competing needs would be resolved.", CUR),
  P("That work disappears inside the finished form.", SEP09),
  P("Ask: what was not obvious at the start? What options existed? What did "
    "I recommend, decide, or bring into agreement? Which constraint made "
    "that choice difficult?", CUR),
  P("The point is not to turn routine work into a rescue story. It is to "
    "show the judgment that would otherwise disappear behind the output.",
    SEP09),
 ]),
 ("4 | PROOF: Keep only what the evidence supports", [
  P("For foundational work, I separate three levels of evidence: Existence, "
    "Use, Effect.", CUR),
  P("Existence means the process, framework, or function was created. Use "
    "means people actually adopted it. Effect means you have evidence that "
    "something important changed because of the work.", CUR),
  P("Those are not interchangeable. A process can exist without being used. "
    "It can be used without producing the outcome you hoped for. And an "
    "outcome can have several causes.", CUR),
  P("In our illustration, an approved intake process is evidence that "
    "something was built. Teams using the same prioritization route is "
    "evidence of adoption. A measured reduction in rework would be a "
    "different claim, and you would need evidence for it.", SEP09),
  P("Do not jump from existence to effect because effect sounds more "
    "impressive. Precision makes the story more credible.", CUR),
  P("The same is true for prevention work. 'We did not have an incident' is "
    "not, by itself, proof that your action prevented one. You can still "
    "describe the weakness you addressed, the decision you made, and the "
    "control or process that was put in place.", SEP09),
  P("Choose the strongest level your evidence actually supports.", SEP09),
 ]),
 ("EVIDENCE BOUNDARY | Do not take what you are not allowed to keep", [
  P("Proof does not mean taking your employer's files. Keep only "
    "information you are permitted to retain. Removing a name does not "
    "create permission to keep restricted material.", CUR),
  P("Your own written account can preserve the structure of the evidence "
    "without preserving confidential material.", CUR),
 ]),
 ("THE FOUR-SENTENCE IMPACT ACCOUNT", [
  P("Put it together in four sentences.", CUR),
  P("Before: what was true before the work existed? My Part: what did I "
    "personally own, recommend, or lead? Judgment: what did I have to work "
    "out that was not obvious? Proof: what is the strongest result I can "
    "support without overstating causation?", SPLIT,
    "The corrected master sets the four prompts as four separate lines. "
    "They are joined into one spoken paragraph so the account reads as one "
    "instruction. No word changed."),
  P("For our illustration: 'The team did not have a shared way to prioritize "
    "incoming requests. I helped develop an agreed triage and escalation "
    "process. My contribution focused on the criteria for exceptions and "
    "ownership of priority decisions. The process was adopted by the "
    "participating teams; its effect on turnaround time had not yet been "
    "established.'", SEP09),
  P("That last sentence does not weaken the story. It tells the listener "
    "exactly where the evidence ends.", SEP09),
  P("Then remove the employer name and internal acronyms. Can a stranger "
    "still understand the contribution? If yes, the work is becoming "
    "portable enough to explain.", CUR),
  P("Then look at the judgment sentence. Does it show something you could "
    "use again in another context? Or did it depend heavily on "
    "relationships, authority, regulation, or domain knowledge you would "
    "have to rebuild? Either answer is useful.", SPLIT,
    "September 9 set 'Then look at the judgment sentence.', the two "
    "questions and 'Either answer is useful.' as four lines. They are "
    "joined into one spoken paragraph. No word changed."),
  P("This is an account of contribution, not a promise that every part of "
    "the experience travels.", SEP09),
 ]),
 ("ACTION AND RESOURCE", [
  P("Keep the Proof is linked below if you want the deeper evidence system "
    "and reusable ledger. But the four-sentence account from this video "
    "stands on its own.", SEP09),
  P("You do not need to make your work sound harder than it was. You need to "
    "stop leaving out the part that made the finished thing possible.",
    SPLIT,
    "September 9 set these as two lines. They are joined into one spoken "
    "paragraph. No word changed."),
 ]),
 ("CLOSE | Do not let successful work disappear", [
  P("Choose one thing people now take for granted because it works. Write "
    "the four sentences.", CUR),
  P("A system looking easy now does not mean it was easy to build.", CUR),
  P("Your job is not to make the story bigger. Your job is to make the "
    "invisible judgment visible.", CUR),
 ]),
 ("WATCH NEXT | Final visual", [
  P("Once you can explain the work, the next question is where else it could "
    "count and what a different industry would still require you to learn.",
    SEP09),
  P("Watch 'How to Change Industries Without Starting Over' next.", SEP09),
 ]),
]

SCRIPTS = {6: V6, 7: V7, 8: V8}
PREV_WORDS = {6: 1151, 7: 1209, 8: 1198}


def provenance_report(n, wrap=70):
    """Every restored line, what it is, and where it came from."""
    import textwrap
    from collections import Counter
    L = []
    cnt = Counter(p["src"] for _, ps in SCRIPTS[n] for p in ps)
    w = sum(len(p["text"].split()) for _, ps in SCRIPTS[n] for p in ps)
    L += ["Restored spoken script: %d words in %d sections."
          % (w, len(SCRIPTS[n])),
          "Previously approved master: %d words." % PREV_WORDS[n], "",
          "Line provenance:"]
    for k in (CUR, SEP09, SPLIT, ADJ, BRIDGE):
        L += ["    %-14s %d" % (k, cnt.get(k, 0))]
    L += ["",
          "    CUR          the corrected September 11 master's own speech",
          "    SEP09        previously approved speech, word for word",
          "    SEP09-SPLIT  approved speech with a sentence the corrected",
          "                 master already says removed, or approved lines",
          "                 joined into one spoken paragraph. Nothing added",
          "    SEP09-ADJ    approved speech with a minimal recorded change",
          "    BRIDGE       newly authored connecting language", "",
          "%d lines of newly authored speech." % cnt.get(BRIDGE, 0), ""]
    for sec, paras in SCRIPTS[n]:
        L += ["-" * wrap, sec, ""]
        for p in paras:
            L += ["  [%s]" % p["src"]]
            L += ["      " + x for x in textwrap.wrap(p["text"], wrap - 6)]
            if p["note"]:
                L += ["      why: " + x
                      for x in textwrap.wrap(p["note"], wrap - 11)[:1]]
                L += ["           " + x
                      for x in textwrap.wrap(p["note"], wrap - 11)[1:]]
            L += [""]
    return L
