# -*- coding: utf-8 -*-
"""Six dedicated Shorts per video.

Each is a full vertical script, not an excerpt timestamp. A Short does not
have to copy the long-form opening, but it must strengthen the same
intellectual association and may not introduce a claim the locked master does
not support.

Default split is 4 Priority A and 2 Priority B. Nothing here is quota filler:
every Short carries one idea that stands on its own.

Pace assumption for the estimate is 165 spoken words per minute, which is the
short-form band. It is arithmetic, not a timed read.
"""
SPM = 165.0


def S(**kw):
    kw.setdefault("captions", "Designed captions permitted. Large, high "
                              "contrast, one or two lines at a time, never "
                              "over the speaker's mouth.")
    kw.setdefault("sound", "One restrained accent at the single strongest "
                           "visual change. Not one per line.")
    return kw


SHORTS = {}

SHORTS[14] = [
 S(priority="A", slug="v14_a1_same_words",
   title="Same words, different job",
   lines=[
     "Three job descriptions. A hospital. A bank. A technology company.",
     "All three asked for the same thing. Manage risk.",
     "At one, getting it wrong means a project slips.",
     "At another, it means financial-crimes and regulatory-compliance "
     "programs.",
     "At another, it is patient movement during an infectious-disease surge.",
     "Same words. Very different consequences.",
     "So before you decide your experience transfers, ask what the person "
     "actually has to decide, and what happens if they decide badly.",
   ],
   visual="Three industry labels, then MANAGE RISK under all three, then the "
          "three consequences one at a time. Full frame, large type.",
   cta="Ask those two questions about one role you are considering.",
   source="V14 hook and the two-question test."),

 S(priority="A", slug="v14_a2_what_travels",
   title="What actually travels",
   lines=[
     "Across 28 job descriptions in healthcare, financial services and "
     "technology, five things kept showing up.",
     "Owning a plan end to end.",
     "Influence without direct authority.",
     "The mechanics of risk and issue management.",
     "Executive communication and governance.",
     "Delivery-method discipline.",
     "Those are worth claiming, if you can support them with evidence from "
     "your own work.",
     "What does not travel as cleanly is the content underneath the words.",
   ],
   visual="The five, revealed one at a time. Then the closing caution as a "
          "single line.",
   cta="Name which of the five you can actually evidence.",
   source="V14 what travels."),

 S(priority="A", slug="v14_a3_two_questions",
   title="The two-question test",
   lines=[
     "Here is a test that works better than a transferable-skills list.",
     "Take one requirement in a role you want.",
     "Ask what you would actually have to decide.",
     "Then ask what happens if you decide badly.",
     "If your answers are comparable to work you have really done, that is "
     "overlap you can defend.",
     "If only the word matches, it is not.",
     "The word tells you almost nothing by itself.",
   ],
   visual="The two questions at full size, one at a time, then together.",
   cta="Run it on one requirement today.",
   source="V14 the test."),

 S(priority="A", slug="v14_a4_employers_disagree",
   title="Employers do not agree with each other",
   lines=[
     "One of the most useful things in the research was that employers "
     "disagreed.",
     "One healthcare posting wanted someone comfortable starting new projects "
     "with limited content knowledge.",
     "One wealth-management posting made years of financial-services "
     "experience a hard requirement, and project-management background only "
     "preferred.",
     "So transferability is not only a property of your experience.",
     "It is also something an employer decides how much to trust.",
     "You can make a strong case and still meet an employer who wants direct "
     "experience. That is the constraint, not a contradiction.",
   ],
   visual="Two postings side by side, described by type. Employers are not "
          "named on screen.",
   cta="Read the posting for how much it trusts adjacent experience.",
   source="V14 employer disagreement."),

 S(priority="B", slug="v14_b1_four_buckets",
   title="Four buckets, not one list",
   lines=[
     "Instead of a transferable-skills list, sort one destination role into "
     "four buckets.",
     "Travels. Capability you can already prove.",
     "Looks similar. Familiar language, different decision.",
     "Must be learned. Knowledge you can acquire through study.",
     "Must be experienced. Context that needs exposure, access or practice.",
     "It is a harder exercise than writing a transferable-skills list.",
     "It is also the one that tells you where you have a real starting point, "
     "and where you are making too big a claim.",
   ],
   visual="The four labels building in order, each with one line.",
   cta="Sort one role you are considering.",
   source="V14 application."),

 S(priority="B", slug="v14_b2_what_it_does_not_prove",
   title="What job descriptions cannot tell you",
   lines=[
     "I read 28 job descriptions for this, and I want to be careful about "
     "what that can show.",
     "It does not prove two roles are interchangeable.",
     "It does not prove someone with adjacent experience would be hired.",
     "It does not prove a hiring manager would waive a requirement.",
     "And 28 postings do not represent the whole labor market.",
     "What they show is what these employers chose to write down. That is "
     "useful. It is not the same as watching the work.",
   ],
   visual="Plain full-frame text. No graphics beyond the words.",
   cta="Treat a posting as a clue, not a verdict.",
   source="V14 what not to claim."),
]

SHORTS[15] = [
 S(priority="A", slug="v15_a1_the_question_changes",
   title="When the question changes",
   lines=[
     "You know the work. You know the numbers. You can explain exactly what "
     "happened.",
     "Then someone asks what you recommend.",
     "The evidence is incomplete. There is no obviously correct answer. And "
     "whatever gets decided affects real people.",
     "And you realize you have never actually had to make that call.",
     "That is not inexperience. It is a gap the work never asked you to fill.",
     "It may feel like one problem. It is usually three.",
   ],
   visual="The first question, then the second replacing it. Full frame.",
   cta="Name the moment where the work got harder.",
   source="V15 hook."),

 S(priority="A", slug="v15_a2_three_gaps",
   title="Learn, practice, prove",
   lines=[
     "Three career gaps feel identical from the inside and need completely "
     "different responses.",
     "A learning gap. There is something you genuinely do not know yet.",
     "A practice gap. You know how the decision should be made, but you have "
     "never been allowed to own it.",
     "An evidence gap. You already know how, and nobody can see enough proof.",
     "Learn. Practice. Prove.",
     "If you misread which one you have, you can spend a year fixing the "
     "wrong problem.",
   ],
   visual="Three labels revealed in order, each with one line.",
   cta="Say which of the three you are actually looking at.",
   source="V15 early payoff."),

 S(priority="A", slug="v15_a3_course_limit",
   title="What a course cannot do",
   lines=[
     "A course can teach you a method.",
     "A course cannot give you the history of having made a consequential "
     "decision with incomplete information, and then living with what "
     "happened next.",
     "So if what is missing is decision experience, more learning can make "
     "you better informed without making you more practiced.",
     "The response to that gap is access, not another reading list.",
     "A smaller decision you genuinely own. Supervised practice. A stretch "
     "where the judgment is yours.",
   ],
   visual="Can and cannot, side by side. The cannot side holds longer.",
   cta="Ask for one decision you are allowed to own.",
   source="V15 learn."),

 S(priority="A", slug="v15_a4_knowing_isnt_owning",
   title="Knowing is not owning",
   lines=[
     "Have you ever been the person who actually had to decide?",
     "Not the person in the meeting. Not the person who prepared the "
     "analysis. Not the person whose recommendation was useful.",
     "The person whose name was on the call, who had to answer for the "
     "consequence.",
     "You can understand a decision very well and still never have carried "
     "one.",
     "Knowing the work and owning the decision are not the same thing.",
   ],
   visual="The final line at maximum size, held in silence.",
   cta="Ask for the smallest decision you can genuinely own.",
   source="V15 practice."),

 S(priority="B", slug="v15_b1_evidence_gap",
   title="It might not be a development problem",
   lines=[
     "Some people have made the hard calls repeatedly, and the room does not "
     "know.",
     "The work was buried inside a team result, presented by someone else, or "
     "absorbed into a process that now looks routine.",
     "That is not a development gap. It is an evidence gap.",
     "And the fix is a record. What the situation was, what you decided, what "
     "you weighed, what happened, and what part was actually yours.",
     "If someone has to know your whole career before the example makes "
     "sense, the evidence is still doing too much work.",
   ],
   visual="Development gap struck through, replaced by evidence gap.",
   cta="Write one example where the judgment was yours.",
   source="V15 prove."),

 S(priority="B", slug="v15_b2_not_a_verdict",
   title="This is not a verdict on you",
   lines=[
     "One caution about naming a career gap.",
     "This is not a diagnostic and it does not assign you a type.",
     "You may have none of these gaps. You may have more than one.",
     "And some gaps are not yours to solve alone. You cannot award yourself "
     "authority your role does not hold, or manufacture access to "
     "consequential work.",
     "The point is not to label yourself. It is to stop spending time on a "
     "solution that does not match the problem.",
   ],
   visual="Plain full-frame text. No framework graphic here.",
   cta="Match the step to the gap you actually have.",
   source="V15 boundary."),
]

SHORTS[16] = [
 S(priority="A", slug="v16_a1_called_then_skipped",
   title="They call you. Then they skip you.",
   lines=[
     "When something is urgent, they call you.",
     "When something breaks, they call you.",
     "When someone new needs to understand how the work really works, they "
     "send them to you.",
     "Then the interesting assignment gets handed out. The promotion list "
     "comes around. The bigger scope gets discussed.",
     "And you are not in the conversation.",
     "That is not the same problem as being invisible, and it does not have "
     "the same fix.",
   ],
   visual="Two stacked lists. What you are called for, and what you are "
          "included in. The second list stays short.",
   cta="Before you speak up more, work out which problem you actually have.",
   source="V16 hook."),

 S(priority="A", slug="v16_a2_the_hinge",
   title="Does not know, or knows and does not act",
   lines=[
     "There is one distinction worth more than any advice about visibility.",
     "A manager who does not know is a completely different situation from a "
     "manager who knows and does not act.",
     "The first is an information problem. Frustrating, but often fixable.",
     "The second is not. If they understand exactly what you contributed and "
     "nothing moves, more explanation is probably not the missing "
     "ingredient.",
     "And you cannot tell which one you are in until the information problem "
     "is gone.",
   ],
   visual="Two panels, clearly different problems rather than degrees of one.",
   cta="Fix the information problem first, so you can read what is left.",
   source="V16 the hinge."),

 S(priority="A", slug="v16_a3_where_work_disappears",
   title="Where good work disappears",
   lines=[
     "Good work disappears in predictable places.",
     "It disappears into a process that now runs smoothly.",
     "It disappears into a team result, where seven people delivered it and "
     "one person made the two calls that kept it from failing.",
     "And it disappears into prevention, where the evidence is that the "
     "problem did not happen.",
     "The better the system works, the easier it is for the work that made it "
     "work to become invisible.",
   ],
   visual="Three places, revealed in order. Prevention shown as an empty "
          "space.",
   cta="Write the version where nothing went wrong, and why.",
   source="V16 is the work seen."),

 S(priority="A", slug="v16_a4_three_pieces_four_lines",
   title="Three pieces, four lines each",
   lines=[
     "If your work is trusted and your name is not in the room, build this.",
     "Take three pieces of consequential work from the last year.",
     "For each, write four lines. What was true before. What you decided. "
     "What changed. And what evidence supports the account.",
     "Do not rely on everyone knows I am strong. Make the work inspectable.",
     "Then use those lines where scope actually gets allocated. One-to-ones. "
     "Planning conversations. The moment someone asks if you can take on "
     "more.",
   ],
   visual="Four lines building in order. The fourth held longest.",
   cta="Write one decision you made and what it changed.",
   source="V16 what to build."),

 S(priority="B", slug="v16_b1_trusted_vs_considered",
   title="Trusted to deliver is not the same as considered for scope",
   lines=[
     "This is where dependable people get stuck.",
     "The organization may trust you deeply and still keep imagining you in "
     "the same role.",
     "If you are the reason a difficult area runs smoothly, moving you "
     "creates a problem for the current system.",
     "That can make indispensability feel like recognition while functioning "
     "like a ceiling.",
     "Delivery and scope are different judgments. You can be near the top of "
     "one list and absent from the other.",
   ],
   visual="Two lists with the same name at different positions.",
   cta="Ask what scope you are being considered for, not just trusted with.",
   source="V16 trusted or considered."),

 S(priority="B", slug="v16_b2_what_it_does_not_fix",
   title="What a clearer record does not fix",
   lines=[
     "I want to be honest about the limit of this.",
     "A clearer record does not override bias.",
     "It does not create a role that does not exist.",
     "It does not move a budget you do not control, or change a manager who "
     "has already decided not to act.",
     "What it does is remove the obstacle you can remove, so whatever remains "
     "becomes easier to see.",
     "Spending years wondering whether the problem was your work or the "
     "environment is the expensive outcome.",
   ],
   visual="Plain full-frame text. No softening graphics.",
   cta="Remove the obstacle that is yours, then read what is left.",
   source="V16 what this does not fix."),
]

SHORTS[17] = [
 S(priority="A", slug="v17_a1_what_did_you_actually_do",
   title="So what did you actually do?",
   lines=[
     "The report used to take you two days.",
     "Now a tool produces most of it in forty minutes.",
     "That sounds like progress. Until someone asks what you actually did.",
     "That question is getting harder to answer, because the visible part of "
     "the work is no longer the scarce part.",
     "Your judgment may be what makes you valuable. But the artifact leaves a "
     "record, and the judgment around it usually does not.",
   ],
   visual="Two days and forty minutes, then the question at full size.",
   cta="Start keeping a record of the part that leaves no trace.",
   source="V17 hook and reversal."),

 S(priority="A", slug="v17_a2_four_lines",
   title="Four lines that prove the contribution",
   lines=[
     "For one piece of AI-assisted work, keep four lines.",
     "One. What were you actually asked to get right, not just asked to "
     "produce.",
     "Two. What did you check, and why did you check that.",
     "Three. What did you conclude that the initial output did not establish.",
     "Four. What were you accountable for if the result was wrong.",
     "Those four make the contribution inspectable without pretending the "
     "tool did nothing.",
   ],
   visual="The four lines building in order. Line two held longest.",
   cta="Write the four lines for one piece of work this week.",
   source="V17 the four lines."),

 S(priority="A", slug="v17_a3_line_two",
   title="The line people forget fastest",
   lines=[
     "If you keep only one line, keep this one.",
     "What did you check, and why did you check that.",
     "A week later you may remember that you checked something. You may not "
     "remember why that was the thing you distrusted.",
     "That reason can come from history, pattern recognition, domain "
     "knowledge, a previous failure, or a consequence the output does not "
     "display.",
     "Write it while the work is still fresh.",
   ],
   visual="The question at maximum size, then the sources of the reason.",
   cta="Capture what you checked and why, today.",
   source="V17 why line two matters."),

 S(priority="A", slug="v17_a4_speed_pressure",
   title="Speed changes the pressure",
   lines=[
     "Here is a second thing happening as the work gets faster.",
     "The report that once took two days may now be expected the same "
     "afternoon.",
     "And the checking time becomes easier to squeeze, because it is harder "
     "to see.",
     "That does not mean the work should stay slow.",
     "It means the organization should be clear about what the checking is "
     "buying, and who still owns the consequence.",
   ],
   visual="A timeline compressing, with the checking segment shrinking.",
   cta="Make visible what the checking time is buying.",
   source="V17 speed changes the pressure."),

 S(priority="B", slug="v17_b1_output_vs_contribution",
   title="Output is not contribution",
   lines=[
     "When producing the output was slow, the output was a rough proxy for "
     "contribution.",
     "As production gets easier, that proxy gets weaker.",
     "So the record has to move.",
     "It used to be attached to the artifact. It now has to be attached to "
     "the decisions around the artifact.",
     "The document shows the output. Four short lines show the contribution.",
     "What you were asked to get right. What you checked and why. What you "
     "concluded. What you were accountable for.",
   ],
   visual="The record moving from the artifact to the decisions around it.",
   cta="Move your record to the decisions, not the deliverable.",
   source="V17 the reversal."),

 S(priority="B", slug="v17_b2_not_reassurance",
   title="This is not AI reassurance",
   lines=[
     "Two things I am not saying.",
     "I am not saying human judgment makes a job safe. Roles can still be "
     "redesigned or removed.",
     "And I am not claiming these tools cannot perform tasks that look like "
     "interpretation or judgment. Tools will change, and career advice should "
     "not depend on pretending they will not.",
     "The narrower point holds either way.",
     "If you are accountable for something being right, keep a record of the "
     "reasoning, the checks and the consequence.",
   ],
   visual="Plain full-frame text. No tool imagery of any kind.",
   cta="Keep the record whether or not the tools improve.",
   source="V17 boundary."),
]

SHORTS[18] = [
 S(priority="A", slug="v18_a1_congratulated",
   title="They congratulate you before they describe the job",
   lines=[
     "Someone offers you a management role.",
     "And before they explain what the job actually is, they congratulate "
     "you.",
     "That tells you something.",
     "Management is often offered as a reward. But it is not a reward. It is "
     "a different job.",
     "Different days. Different skills. Different hard parts.",
     "Not a higher version of the work you are doing now, and not a lower "
     "one either.",
     "Two jobs. Ask which one you are actually being offered.",
   ],
   visual="The compliment, then the job description that was never given.",
   cta="Before you answer, ask what the job actually consumes.",
   source="V18 hook and reframe."),

 S(priority="A", slug="v18_a2_five_things",
   title="Five things that do not move together",
   lines=[
     "Five things get bundled together when a bigger role is offered.",
     "Scope. Responsibility. Compensation. Authority. People management.",
     "They do not reliably move together.",
     "A role can increase your responsibility without increasing your "
     "authority.",
     "It can increase your scope without changing compensation.",
     "It can add people management while taking you away from the work you "
     "most enjoy.",
     "Separate the bundle before you decide.",
   ],
   visual="Five items shown moving independently, never as one bar.",
   cta="Ask which of the five this offer actually changes.",
   source="V18 five things."),

 S(priority="A", slug="v18_a3_ask_for_names",
   title="Ask for names",
   lines=[
     "If you want to stay an individual contributor, ask what senior "
     "individual work looks like here, and whether it exists in practice.",
     "Then ask for names.",
     "Ask what those people are trusted to decide. Ask how their scope and "
     "compensation compare with management at the same level.",
     "Some organizations genuinely cap individual contributors.",
     "If the only route upward runs through people management, that is not "
     "encouragement or discouragement. It is information you need before you "
     "choose.",
   ],
   visual="ASK FOR NAMES at maximum size, then the follow-up questions.",
   cta="Ask for names before you decide.",
   source="V18 question two."),

 S(priority="A", slug="v18_a4_responsibility_without_authority",
   title="Responsibility without authority",
   lines=[
     "Before you accept a bigger role, write two lists.",
     "What you can decide without asking. Budget. Hiring. Prioritization. "
     "Saying no. Changing scope.",
     "Then what you will be answerable for.",
     "If the second list is much longer than the first, name that before you "
     "accept.",
     "Responsibility without enough authority is not a small detail of the "
     "job. It is the job.",
     "It is also sometimes negotiable at the point of offer, and almost never "
     "negotiable six months later.",
   ],
   visual="Two lists at visibly different lengths.",
   cta="Compare the two lists before you answer.",
   source="V18 question three."),

 S(priority="B", slug="v18_b1_can_you_come_back",
   title="Can you come back?",
   lines=[
     "One question people forget to ask before moving into management.",
     "Is it reversible here?",
     "Do people move into management and later back into senior individual "
     "work without penalty?",
     "Look for real examples. Not the policy. People.",
     "A reversible decision deserves less fear than one that is culturally "
     "one-way.",
     "And if you cannot find anyone who has done it, that is your answer "
     "about how the door works in practice.",
   ],
   visual="In principle, and in practice. Two columns.",
   cta="Look for two people who have actually come back.",
   source="V18 question four."),

 S(priority="B", slug="v18_b2_neither_is_brave",
   title="Neither answer is the brave one",
   lines=[
     "Staying an individual contributor is not automatically the more "
     "authentic choice.",
     "Becoming a manager is not automatically the more ambitious one.",
     "Managing people well is difficult, valuable work.",
     "Deep senior individual work is difficult, valuable work.",
     "Pick the path whose hard parts you would rather have, inside the "
     "organization you actually work in.",
     "Do not choose the title. Choose the work.",
   ],
   visual="Two paths side by side, never stacked as a ladder.",
   cta="Choose the hard parts you would rather have.",
   source="V18 boundary and close."),
]

SHORTS[19] = [
 S(priority="A", slug="v19_a1_experience_is_not_an_offer",
   title="Experience is not an offer",
   lines=[
     "Someone has told you that you should consult. Probably more than once.",
     "It usually happens right after you solve something difficult, which is "
     "why it feels flattering and why almost nobody examines it.",
     "But twenty years of experience can still leave you with nothing a "
     "client knows how to buy.",
     "Your experience tells you what you know. It does not automatically tell "
     "you what somebody will buy.",
     "Those are different questions.",
   ],
   visual="The compliment, then the two questions separating.",
   cta="Write what somebody would actually receive from you.",
   source="V19 hook and reversal."),

 S(priority="A", slug="v19_a2_who_signs_it",
   title="Who already pays for this?",
   lines=[
     "Before anything else, ask who already spends money on this problem.",
     "Not who suffers from it. Almost everybody has problems.",
     "Who actually pays somebody to solve it now?",
     "Sometimes the answer is that it is handled internally and there is no "
     "obvious external budget.",
     "That does not make consulting impossible. It means part of your work "
     "will be creating demand, and you should know that before you resign.",
     "And if a budget exists, find out who signs it. That may not be the "
     "person with the problem.",
   ],
   visual="Who has the problem, and who releases the money. Two people.",
   cta="Name one organization that already pays for this.",
   source="V19 the buyer question."),

 S(priority="A", slug="v19_a3_deliverable",
   title="I advise on risk is not an offer",
   lines=[
     "Here is where a lot of good experience stalls.",
     "I advise on risk is expertise. It is not yet an offer.",
     "An offer is a bounded review. A decision workshop. A diagnostic. A "
     "written recommendation. A defined implementation sprint.",
     "Something a buyer can assess, with a beginning and an end.",
     "Then state what is not included. Scope is part of the offer, not a "
     "legal footnote you discover after the work expands.",
   ],
   visual="The unbuyable sentence struck through, then the alternatives.",
   cta="Write one sentence: what somebody receives, and by when.",
   source="V19 turn expertise into a deliverable."),

 S(priority="A", slug="v19_a4_test_before_you_leave",
   title="Test it before you leave anything",
   lines=[
     "Do not start with a website launch.",
     "Start with conversations, within whatever your current employment "
     "agreement permits.",
     "Ask people who understand the problem how it is solved today, what "
     "creates budget, and what they would expect from an external provider.",
     "Then write one page. The problem, the buyer, the deliverable, the "
     "scope, and the conditions that would need to be true.",
     "You are not testing whether you are talented. You are testing whether "
     "what you described is recognized as worth buying.",
   ],
   visual="The one page building field by field.",
   cta="Have three conversations before you change anything.",
   source="V19 test before you leave."),

 S(priority="B", slug="v19_b1_repeatability",
   title="Can you do it a second time?",
   lines=[
     "The first engagement often contains invention. The second should "
     "contain more structure.",
     "What questions do you always ask? What input do you need? What does the "
     "output look like?",
     "What did you learn about scope, timing, or risk?",
     "That is the beginning of repeatable delivery.",
     "Without it, consulting can become a series of custom favors built from "
     "scratch every time.",
   ],
   visual="The first engagement, then what survives into the second.",
   cta="Write down what you would keep for the next one.",
   source="V19 repeatability."),

 S(priority="B", slug="v19_b2_costs",
   title="The costs the compliment leaves out",
   lines=[
     "There is work around the work.",
     "Finding the next client. Managing uneven demand. Handling commercial "
     "conversations. Defining scope. Waiting to be paid.",
     "None of that means consulting is a bad move.",
     "It means you should trade knowingly.",
     "And check your employment agreement before side work or outreach.",
     "Notice periods, non-compete clauses and conflict-of-interest rules vary "
     "by employer and by where you are. This is not legal or tax advice.",
   ],
   visual="Plain full-frame text. No lifestyle imagery.",
   cta="Read your agreement before you approach anyone.",
   source="V19 the costs."),
]

SHORTS[20] = [
 S(priority="A", slug="v20_a1_not_the_whole_return",
   title="The gap is not the whole return",
   lines=[
     "You may already know someone will ask about the break, so you prepare "
     "an honest, brief answer.",
     "Good. Have that sentence.",
     "But the conversation eventually moves to a harder question. What can "
     "you do now, and what can you prove?",
     "That is where I would put most of the preparation.",
     "The explanation matters. It is not the whole return.",
   ],
   visual="The prepared sentence, then the question that actually decides it.",
   cta="Prepare the answer to what can you prove, not just the explanation.",
   source="V20 hook and reframe."),

 S(priority="A", slug="v20_a2_unproven_is_not_absent",
   title="Unproven is not the same as absent",
   lines=[
     "This is the distinction I want you to remember most.",
     "Unproven is not the same as absent.",
     "You may still know how to do something and simply have no recent "
     "evidence that another person can inspect.",
     "If it is unproven, the response is not automatically to relearn it from "
     "the beginning.",
     "The response may be to create a current instance. A bounded project. A "
     "permitted work sample. A short contract. Volunteer work. Refreshed "
     "training.",
     "If it is genuinely absent, that is a different problem.",
   ],
   visual="The two words side by side, then their different responses.",
   cta="Sort one capability into unproven or absent.",
   source="V20 the distinction."),

 S(priority="A", slug="v20_a3_three_buckets",
   title="Three buckets instead of behind on everything",
   lines=[
     "Instead of treating your whole career as current or obsolete, sort it "
     "into three buckets.",
     "Still current. Needs updating. Needs rebuilding.",
     "Still current is capability that survives time away. How you structure "
     "a problem. How you read a room. The standard you recognize when work is "
     "good.",
     "Needs updating separates decay from change in the field.",
     "Needs rebuilding is the part that does not travel automatically.",
     "That is a very different problem from I have been out for years, so I "
     "am behind on everything.",
   ],
   visual="Three columns filling one at a time.",
   cta="Sort one skill into one of the three buckets.",
   source="V20 three buckets."),

 S(priority="A", slug="v20_a4_put_a_date_on_it",
   title="Put a date on it",
   lines=[
     "Build two short lists before you apply anywhere.",
     "First, what is current now, with evidence for each item.",
     "Second, what you are rebuilding now, with a date attached.",
     "A date matters. I plan to refresh this and I started this in September "
     "and will complete it in November are different signals.",
     "The second one is also the part entirely within your control.",
   ],
   visual="The two lists, with the date emphasized on the second.",
   cta="Choose one thing you are rebuilding and put a date on it.",
   source="V20 application."),

 S(priority="B", slug="v20_b1_bias_is_real",
   title="A good explanation cannot remove bias",
   lines=[
     "I am not going to tell you that the right sentence fixes this.",
     "Bias against career breaks exists, and a better explanation does not "
     "make every employer fair.",
     "What a stronger return record does is keep you from arguing for the "
     "wrong thing.",
     "It lets you say what is still current, what you are updating, what you "
     "can prove, and what you are rebuilding now.",
     "And some routes back may involve a different title, scope or "
     "compensation. That is a tradeoff to evaluate, not a measurement of your "
     "worth.",
   ],
   visual="Plain full-frame text. No reassurance imagery.",
   cta="Argue for what you can prove, not against the gap.",
   source="V20 market reality."),

 S(priority="B", slug="v20_b2_decay_vs_change",
   title="Decay and change are different problems",
   lines=[
     "When you come back, separate two things that feel identical.",
     "Decay is something you once used and have not practiced recently. A "
     "system. A process. A pace.",
     "Change is when the field itself moved while you were away. New tools. "
     "New expectations. New operating assumptions.",
     "Those are different problems.",
     "But both can often be addressed with targeted updating rather than "
     "starting again from zero.",
   ],
   visual="Two labels, then their shared response.",
   cta="Name one thing that decayed and one thing that changed.",
   source="V20 needs updating."),
]

SHORTS[21] = [
 S(priority="A", slug="v21_a1_the_room_is_different",
   title="You can still do the work",
   lines=[
     "You made the industry change.",
     "And the surprising part is that you can still do the work.",
     "What keeps catching you are the things nobody thought to explain.",
     "A meeting where everybody understands a phrase you have never heard.",
     "A decision that goes a direction you would not have predicted.",
     "A relationship that matters for reasons no process document mentions.",
     "That is the part of an industry change people underestimate.",
   ],
   visual="What came with you, and the empty column beside it.",
   cta="Make the inventory for one destination, not the whole industry.",
   source="V21 hook."),

 S(priority="A", slug="v21_a2_licensing_is_not_a_mindset",
   title="A licensing requirement is not a mindset issue",
   lines=[
     "If a role requires a license, a registration, or a qualification you do "
     "not hold, adjacent experience does not erase that requirement.",
     "A licensing requirement is not a mindset issue.",
     "It is not a confidence problem and it is not something you can approach "
     "your way around.",
     "Confirm what is binding, what is preferred, and what you need to do, "
     "from the body or the employer that actually sets the requirement.",
     "Then plan around it, because that timeline shapes everything else.",
   ],
   visual="The line at maximum size, held in silence.",
   cta="Check the binding requirements before anything else.",
   source="V21 regulation and credentials."),

 S(priority="A", slug="v21_a3_five_layers",
   title="Five layers to relearn",
   lines=[
     "When you change industries, sort the relearning into five layers.",
     "Domain knowledge. What the work is actually about here.",
     "Regulation and credentials.",
     "Systems and tooling.",
     "Relationships and internal history.",
     "And how decisions actually get made.",
     "The order matters less than one question. Which layer will block useful "
     "contribution first in this specific role?",
     "That is a better sequence than starting with whatever course looks "
     "easiest to buy.",
   ],
   visual="Five layers building downward, then the ordering question.",
   cta="Reorder your list by what blocks you first.",
   source="V21 the five-layer inventory."),

 S(priority="A", slug="v21_a4_easiest_layer_trap",
   title="Do not prepare for the easiest layer",
   lines=[
     "Systems and tooling are often the most visible gaps, because they have "
     "names.",
     "New platforms. New internal systems. Different workflows.",
     "Some of it can be learned relatively directly through documentation, "
     "training, or guided use.",
     "So do not spend all your preparation time on the easiest-to-name layer "
     "while the harder context remains untouched.",
     "Relationships, internal history, and how decisions get made are the "
     "layers that take longer and get skipped.",
   ],
   visual="The named layer beside the unnamed ones.",
   cta="Give the harder layers real preparation time.",
   source="V21 systems and tooling."),

 S(priority="B", slug="v21_b1_has_anyone_tried_this",
   title="Has anyone tried this before?",
   lines=[
     "There is knowledge in a new organization you cannot read your way into.",
     "Why a team is cautious. Why the obvious solution has already been "
     "tried. Who has to be told before a decision even when they do not "
     "formally approve it.",
     "This is the kind of knowledge least likely to be learned from "
     "documentation.",
     "So a useful early question is simple.",
     "Has anyone tried this before, and what happened?",
   ],
   visual="The question alone, full frame.",
   cta="Ask it before you propose anything.",
   source="V21 relationships and internal history."),

 S(priority="B", slug="v21_b2_read_or_practice",
   title="Some of it you read. Some of it you practice.",
   lines=[
     "Some parts of a new industry can be read. Requirements, documentation, "
     "domain facts, formal processes.",
     "Set aside real time for those, because it is the fastest return "
     "available.",
     "Some parts need exposure, feedback, and practice in the actual "
     "environment.",
     "Relationships, exception logic, and local decision-making are usually "
     "in that group.",
     "Do not treat the second group as proof that you made the wrong move "
     "simply because it takes time to learn.",
   ],
   visual="Two columns sorting the five layers by how they are learned.",
   cta="Start the readable items this week.",
   source="V21 read it or practice it."),
]
