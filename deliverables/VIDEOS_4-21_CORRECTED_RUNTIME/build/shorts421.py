# -*- coding: utf-8 -*-
"""Six Shorts per video for the corrected-runtime batch.

Each is a full vertical script, not an excerpt. Nothing introduces a claim the
corrected master does not support. Default split is 4 Priority A and 2
Priority B.

Timing is arithmetic at 165 spoken words per minute, the short-form band. Not
a timed read.
"""
import sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                   "VIDEOS_14-21_FINAL_PRODUCTION/build")

SPM = 165.0


def S(**kw):
    kw.setdefault("captions", "Designed captions permitted on Shorts. Large, "
                              "high contrast, one or two lines at a time, "
                              "never over the speaker's mouth.")
    kw.setdefault("sound", "One restrained accent at the single strongest "
                           "visual change. Not one per line.")
    kw.setdefault("status", "NEW")
    kw.setdefault("why", "Written against the corrected September 11 master.")
    return kw


SHORTS = {}

SHORTS[4] = [
 S(priority="A", slug="v4_a1_never_held_the_role",
   title="I'd never held the role",
   lines=[
     "Three times in five years, I stepped into a role that did not have a "
     "predecessor.",
     "Each time the title was new to me. The work underneath it was not "
     "completely new.",
     "What changed was how I judged whether I was ready.",
     "I stopped waiting for an exact title match.",
     "I stopped proving myself with a task list.",
     "And I stopped treating every learning gap like evidence that I was not "
     "ready.",
   ],
   visual="The three stops, building one at a time.",
   cta="Ask what problem the role needs solved, what you can prove, and what "
       "you need to learn.",
   source="V4 hook."),
 S(priority="A", slug="v4_a2_remove_the_title",
   title="Compare the roles without their titles",
   lines=[
     "Titles are useful, but they are incomplete.",
     "Remove the title and ask what this person is actually being hired to "
     "make clearer, less risky, more reliable, or more possible.",
     "If the new role still asks you to diagnose ambiguity, align people who "
     "do not report to you, or make a recommendation under uncertainty, you "
     "may have more relevant evidence than the title suggests.",
     "That does not make every role interchangeable.",
     "It means never having held the title is not the same as never having "
     "done the work.",
   ],
   visual="Two role descriptions with the titles removed.",
   cta="Do the comparison on one role you are considering.",
   source="V4 stop one."),
 S(priority="A", slug="v4_a3_evidence_of_judgment",
   title="Stop proving readiness with a task list",
   lines=[
     "A task list works when the new job is almost identical to the old one.",
     "It is weaker when the role is new, redesigned, or in a different "
     "context.",
     "For unfamiliar work, look for evidence of judgment.",
     "When the instructions were incomplete, what did people trust you to "
     "notice? What tradeoff did you weigh? What did you recommend when there "
     "was more than one reasonable answer?",
     "That is different from saying I am strategic.",
     "A real example has a decision, a constraint, what you did, and what "
     "happened.",
   ],
   visual="A task list struck through, replaced by the four-part example.",
   cta="Write one example with a decision, a constraint, and a result.",
   source="V4 stop two."),
 S(priority="A", slug="v4_a4_three_line_readiness_case",
   title="The 3-line readiness case",
   lines=[
     "Take one role you have never held and write three lines.",
     "Problem. What does this role actually need someone to solve?",
     "Proof. What have I already done that shows I can handle the underlying "
     "judgment?",
     "Gap. What do I genuinely need to learn, earn, or experience here?",
     "If the proof is thin, you know what evidence you still need.",
     "If the gap is a hard gate, you know what must change before the move "
     "makes sense.",
   ],
   visual="The three labels building in order.",
   cta="Write the three lines for one role this week.",
   source="V4 the 3-line readiness case."),
 S(priority="B", slug="v4_b1_name_the_gap",
   title="Do not hide the gap",
   lines=[
     "A real move should contain things you do not know yet.",
     "Domain knowledge can matter. Regulation, systems, relationships, "
     "credentials, and internal history can matter too.",
     "Do not hide those gaps. Name them.",
     "A credible readiness case is not, I can already do every part of this.",
     "It is, here is what I can carry, here is the proof, and here is what I "
     "still need to learn.",
   ],
   visual="The weak claim struck through, replaced by the credible one.",
   cta="Name the gap instead of hiding it.",
   source="V4 stop three."),
 S(priority="B", slug="v4_b2_what_it_does_not_guarantee",
   title="What a readiness case cannot do",
   lines=[
     "I want to be straight about the limit of this.",
     "A strong readiness case does not guarantee that an employer will "
     "choose you.",
     "Credentials, markets, relationships, compensation, employer "
     "preferences, and bias still matter.",
     "What it does is separate two very different problems.",
     "I have never held this title. And I do not yet have the evidence this "
     "work requires.",
   ],
   visual="Plain full-frame text. No reassurance imagery.",
   cta="Work out which of those two problems you actually have.",
   source="V4 close."),
]

SHORTS[5] = [
 S(priority="A", slug="v5_a1_changed_tracks_not_zero",
   title="Changed tracks. Not zero.",
   lines=[
     "When you change career tracks, other people can start reading you like "
     "a beginner.",
     "The more expensive mistake is when you start doing it to yourself.",
     "Not every move is a promotion. Not every part of your experience "
     "transfers.",
     "But you do not have to throw away the judgment you already built just "
     "because the context changed.",
     "Separate four things: what you can carry, what you have to translate, "
     "what you genuinely need to relearn, and what you can prove.",
   ],
   visual="The four labels building in order.",
   cta="Sort one move you are considering into those four.",
   source="V5 hook."),
 S(priority="A", slug="v5_a2_carry",
   title="What actually carries",
   lines=[
     "Years of experience do not travel by themselves.",
     "But some judgment can. Pattern recognition can. Influence without "
     "formal authority can. Building structure in ambiguity can.",
     "Here is the test.",
     "If the employer name, the old title, and the industry language "
     "disappeared, which parts of your experience would still help you solve "
     "the destination problem?",
     "That is what you carry.",
     "Everything else either needs translating, relearning, or proving.",
   ],
   visual="Employer name, title and industry language removed one at a time.",
   cta="Name the parts that survive the removal.",
   source="V5 carry."),
 S(priority="A", slug="v5_a3_translate",
   title="Translate, do not repeat the label",
   lines=[
     "The same accomplishment can sound valuable in one room and irrelevant "
     "in another, because the listener does not know the old context.",
     "Do not repeat the old label and hope they understand it.",
     "Translate the underlying work.",
     "What did you have to notice? What decision did you support? What "
     "tradeoff did you manage? What changed because of your contribution?",
     "Translation is not changing the story. It is removing the "
     "context-specific language so the useful judgment becomes visible.",
   ],
   visual="An internal program name replaced by the underlying work.",
   cta="Translate one accomplishment out of its old context.",
   source="V5 translate."),
 S(priority="A", slug="v5_a4_prove_the_level",
   title="Fifteen years is not a level",
   lines=[
     "Do not rely on I have fifteen years of experience, or I was a "
     "director.",
     "Those statements tell me duration and title, not what level of "
     "judgment you can carry into a new context.",
     "Use evidence instead.",
     "What difficult problem did you own? What did you decide when the "
     "answer was not obvious? What scope or consequence did you carry?",
     "The goal is not to prove that every part of your seniority transfers. "
     "It is to show which parts deserve to be read at the level they were "
     "actually exercised.",
   ],
   visual="Duration and title struck through, replaced by the questions.",
   cta="Write one example that supports the level you are claiming.",
   source="V5 prove the level."),
 S(priority="B", slug="v5_b1_relearn",
   title="Relearn without calling yourself a beginner",
   lines=[
     "Every real context change creates things you have to learn from inside "
     "the new environment.",
     "Systems. Regulation. Domain language. Relationships. Sometimes "
     "credentials, or practice under a different consequence.",
     "Those gaps matter. Your experience does not make them optional.",
     "But needing to learn them does not erase everything you already know "
     "how to do.",
     "Name the gap accurately, then decide whether it is a reasonable "
     "learning curve or a reason not to move yet.",
   ],
   visual="The gap named rather than hidden.",
   cta="Name the gap accurately before you decide.",
   source="V5 relearn."),
 S(priority="B", slug="v5_b2_both_directions",
   title="Confidence misleads in both directions",
   lines=[
     "This is where confidence can become misleading, and it goes both "
     "ways.",
     "You do not need to apologize for every gap.",
     "But you also do not get to rename a real domain or credential "
     "requirement as a transferable skill because that makes the move easier "
     "to explain.",
     "A career-track change can lower your leverage in some areas. "
     "Employers may still prefer direct experience.",
     "A new track does not automatically make all of your old judgment "
     "irrelevant either.",
   ],
   visual="Two overcorrections side by side.",
   cta="Check which direction you are overcorrecting in.",
   source="V5 relearn and close."),
]

SHORTS[6] = [
 S(priority="A", slug="v6_a1_movement_is_not_growth",
   title="Movement can look like growth",
   lines=[
     "I have worked across eight industries and sectors, and one thing that "
     "taught me is that movement can look like career growth long before the "
     "work actually changes.",
     "A role can come with more money, more visibility, a more senior title, "
     "and still leave you solving almost the same class of problem.",
     "Another role can barely change the title and completely change what "
     "you are capable of doing a year later.",
     "So I want three things answered before I move.",
     "Will the work change. Will my judgment expand. Will the evidence "
     "travel.",
   ],
   visual="The three questions building in order.",
   cta="Answer those three before your next move.",
   source="V6 hook."),
 S(priority="A", slug="v6_a2_ordinary_monday",
   title="Start with an ordinary Monday",
   lines=[
     "When somebody describes a new role as strategic or transformational, "
     "do not let the words do the work for the hiring manager.",
     "Start with an ordinary Monday.",
     "What will actually be different? What problems will you own?",
     "Which customers, systems, regulations, operating models, or "
     "stakeholders will you have to understand that you do not understand "
     "today?",
     "A move can be significant even if the title barely changes. And a "
     "larger title can hide more volume of the same work.",
   ],
   visual="ORDINARY MONDAY at full size, then the questions.",
   cta="Ask what an ordinary Monday actually contains.",
   source="V6 work."),
 S(priority="A", slug="v6_a3_responsibility_is_not_judgment",
   title="Responsibility is not judgment",
   lines=[
     "Responsibility is not the same as judgment.",
     "You can own the deadline while somebody else still controls scope, "
     "resources, sequence, and the decision that determines whether the "
     "deadline is even possible.",
     "So ask where you will have to make a call when the instructions are "
     "incomplete.",
     "Which tradeoffs will belong to you. What you can influence when the "
     "plan is not working.",
     "You do not need complete control. But if accountability is growing and "
     "your judgment has nowhere to go, keep investigating.",
   ],
   visual="Responsibility and judgment shown as separate, unequal things.",
   cta="Ask which decisions would actually belong to you.",
   source="V6 judgment."),
 S(priority="A", slug="v6_a4_twelve_month_question",
   title="The 12-month question",
   lines=[
     "Here is the one question I would ask before taking any new role.",
     "Twelve months from now, what will I be able to do, decide, or prove "
     "that I cannot do today?",
     "If the answer is specific, you can see the developmental value.",
     "If the answer is mostly, I will be busier, more visible, and managing "
     "more of the same, you have learned something important.",
     "You may still take the role. Just take it for the reason it actually "
     "serves.",
   ],
   visual="The question at maximum size, held long.",
   cta="Answer it before you accept.",
   source="V6 the 12-month question."),
 S(priority="B", slug="v6_b1_harder_later",
   title="This gets harder later in a career",
   lines=[
     "Earlier in a career, almost any new responsibility can teach you "
     "something.",
     "Later, the question becomes more selective.",
     "Is this role expanding what you can carry, or is it simply using more "
     "of what you already know?",
     "A role does not have to maximize growth to be a good decision. You may "
     "choose for pay, flexibility, stability, location, health, or family.",
     "The problem is calling every move development when the work underneath "
     "it has barely changed.",
   ],
   visual="Early career and later career, two different questions.",
   cta="Take the role for the reason it actually serves.",
   source="V6 why this gets harder."),
 S(priority="B", slug="v6_b2_negotiate_before_you_accept",
   title="You can redesign the role before you accept",
   lines=[
     "Before your next move, write one sentence under Work, one under "
     "Judgment, and one under Evidence.",
     "If one area is weak, ask whether it can be redesigned before you "
     "accept.",
     "Maybe the role needs a clearer decision right.",
     "Maybe you need access to a different stakeholder group.",
     "Maybe temporary scope needs a review point.",
     "A different title can be useful. But a bigger title and a bigger "
     "career are not automatically the same thing.",
   ],
   visual="The three headings with one sentence each.",
   cta="Ask what could be redesigned before you say yes.",
   source="V6 close."),
]

SHORTS[7] = [
 S(priority="A", slug="v7_a1_valuable_to_them",
   title="More valuable to them, not to your future",
   lines=[
     "You can become more valuable to your organization without becoming "
     "more valuable to your own future.",
     "It took me years to learn that being trusted with more is not the same "
     "as being developed for more.",
     "A colleague leaves. A project has no clear owner. Your manager asks, "
     "can you take this too.",
     "Six months later your scope is bigger, your calendar is fuller, and "
     "everybody describes it as growth.",
     "Maybe it is. Or maybe the organization has simply learned that you can "
     "absorb more.",
   ],
   visual="Scope and calendar filling while the work stays the same.",
   cta="Run complexity, authority and return on that extra responsibility.",
   source="V7 hook."),
 S(priority="A", slug="v7_a2_complexity",
   title="Did the problem get harder, or did the volume get bigger?",
   lines=[
     "If you managed three nearly identical projects last year and now "
     "manage eight, your capacity is being used more heavily.",
     "You may be faster, more organized, and more resilient. That is not "
     "automatically a new class of problem.",
     "Complexity changes when the variables change.",
     "A new customer. A new regulation. A different operating model. "
     "Conflicting priorities. Stakeholders whose incentives do not line up.",
     "If the only answer is more of the same, call that capacity use. Do not "
     "automatically call it growth.",
   ],
   visual="Volume increasing beside complexity staying flat.",
   cta="Name what variables are actually new.",
   source="V7 complexity."),
 S(priority="A", slug="v7_a3_authority",
   title="Three things that do not expand together",
   lines=[
     "Responsibility is what you are expected to carry.",
     "Accountability is what you will answer for.",
     "Authority is what you can influence or decide.",
     "Those three do not always expand together.",
     "You can own a deadline and still be unable to reduce scope. You can be "
     "accountable for a program and still be unable to secure the people "
     "it requires.",
     "Your judgment should have somewhere to go.",
   ],
   visual="Three bars moving independently.",
   cta="Ask which decisions now belong to you.",
   source="V7 authority."),
 S(priority="A", slug="v7_a4_review_point",
   title="Ask for the review point",
   lines=[
     "Before the next can you take this too, ask three things.",
     "What becomes more complex?",
     "What authority comes with it?",
     "And when will we review what this additional scope returns?",
     "That last question matters most.",
     "Temporary stretch without a review point has a way of becoming "
     "permanent absorption.",
     "CAR is not a score. You are looking for a pattern. If complexity, "
     "authority and return all moved, you may be looking at real growth.",
     "If the only thing that moved was volume, name it accurately.",
   ],
   visual="The three questions, the third held longest.",
   cta="Ask for the review point before you say yes.",
   source="V7 use CAR before you say yes."),
 S(priority="B", slug="v7_b1_dependable_people",
   title="Why dependable people are vulnerable",
   lines=[
     "Reliability attracts work quickly.",
     "Authority, support, recognition, and formal scope often arrive later, "
     "if they arrive at all.",
     "That is why the workload trap can feel flattering at first. You are "
     "the person people trust.",
     "Then temporary coverage quietly becomes the permanent design of your "
     "job.",
     "The question is not whether more work is bad. It is what the extra "
     "work is building in you, and what it returns.",
   ],
   visual="Work arriving fast, everything else arriving slowly.",
   cta="Ask what the extra work is building and returning.",
   source="V7 why dependable people are vulnerable."),
 S(priority="B", slug="v7_b2_praise_is_not_role_design",
   title="Praise alone is not role design",
   lines=[
     "Extra responsibility costs time, attention, and energy. Something "
     "should be coming back.",
     "That return does not have to be an immediate promotion.",
     "A stretch assignment can be worth it because it builds capability you "
     "did not have, gives you evidence you could not previously claim, or "
     "creates recognition tied to the contribution.",
     "I look in three places. Capability. Evidence. Recognition.",
     "Praise is welcome. Praise alone is not role design.",
   ],
   visual="The three returns, then the closing line at full size.",
   cta="Check what the extra work is actually returning.",
   source="V7 return."),
]

SHORTS[8] = [
 S(priority="A", slug="v8_a1_now_it_looks_easy",
   title="If you build it well enough, nobody sees how hard it was",
   lines=[
     "One of the strangest things about building something from scratch is "
     "that if you do it well enough, eventually nobody can see how hard it "
     "was.",
     "The process exists. People use it. The decisions have become routine.",
     "And the uncertainty you had to solve at the beginning has disappeared "
     "from view.",
     "Once foundational work starts operating, I built it is not enough.",
     "A person who was not there still cannot see what was missing, what you "
     "had to work out, or what the evidence actually supports.",
   ],
   visual="A working system, with the starting conditions fading out.",
   cta="Reconstruct the before, your part, the judgment, and the proof.",
   source="V8 hook."),
 S(priority="A", slug="v8_a2_the_before",
   title="Reconstruct what was true before",
   lines=[
     "The finished thing hides the conditions you started with.",
     "You say I built the process. The listener sees a process.",
     "What they do not see is the uncertainty before it existed. The "
     "conflicting expectations. The missing rule. The decisions that had no "
     "obvious owner.",
     "So put the missing information back.",
     "A weak before is, it was chaos.",
     "A stronger before is, there was no shared way to prioritize requests "
     "or decide which issues needed escalation.",
   ],
   visual="The weak before struck through, replaced by the specific one.",
   cta="Write the specific version of what was true before.",
   source="V8 before."),
 S(priority="A", slug="v8_a3_existence_use_effect",
   title="Existence, use, effect",
   lines=[
     "For foundational work, separate three levels of evidence.",
     "Existence means the process, framework, or function was created.",
     "Use means people actually adopted it.",
     "Effect means you have evidence that something important changed "
     "because of the work.",
     "Those are not interchangeable. A process can exist without being used. "
     "It can be used without producing the outcome you hoped for.",
     "Do not jump from existence to effect because effect sounds more "
     "impressive. Precision makes the story more credible.",
   ],
   visual="Three levels, built upward, with the jump blocked.",
   cta="Mark which level your evidence actually supports.",
   source="V8 proof."),
 S(priority="A", slug="v8_a4_four_sentences",
   title="The four-sentence impact account",
   lines=[
     "Choose one thing people now take for granted because it works.",
     "Then write four sentences.",
     "Before. What was true before the work existed.",
     "My part. What did I personally own, recommend, or lead.",
     "Judgment. What did I have to work out that was not obvious.",
     "Proof. What is the strongest result I can support without overstating "
     "causation.",
     "Then remove the employer name and the internal acronyms. Can a "
     "stranger still understand the contribution?",
   ],
   visual="The four labels building in order.",
   cta="Write the four sentences for one thing you built.",
   source="V8 the four-sentence impact account."),
 S(priority="B", slug="v8_b1_accurate_attribution",
   title="You do not need sole credit",
   lines=[
     "Be careful with nothing existed before me.",
     "People may already have been doing useful work informally. Your "
     "contribution may have been connecting it, making it repeatable, or "
     "clarifying ownership.",
     "And name your part accurately.",
     "If somebody else held the final decision, say you developed the "
     "options or made the recommendation. If the team designed the process, "
     "name the part you led.",
     "You do not need sole credit to make your contribution legible. You "
     "need accurate attribution.",
   ],
   visual="Sole credit struck through, replaced by accurate attribution.",
   cta="Name your part accurately rather than broadly.",
   source="V8 my part."),
 S(priority="B", slug="v8_b2_evidence_boundary",
   title="Proof does not mean taking files",
   lines=[
     "One boundary worth saying plainly.",
     "Proof does not mean taking your employer's files.",
     "Keep only information you are permitted to retain.",
     "Removing a name does not create permission to keep restricted "
     "material.",
     "Your own written account can preserve the structure of the evidence "
     "without preserving confidential material.",
     "That is the version that travels with you safely.",
     "Write what the situation was, what you decided, and what changed. Not "
     "the dashboard, not the deck, not the customer list.",
   ],
   visual="Plain full-frame text. No document imagery.",
   cta="Keep the account, not the file.",
   source="V8 evidence boundary."),
]

SHORTS[9] = [
 S(priority="A", slug="v9_a1_new_field_not_zero",
   title="New field does not mean zero",
   lines=[
     "You can be very experienced and still read one sentence in a job "
     "description that makes you feel like a beginner again.",
     "Direct industry experience required.",
     "You know you have done difficult work. You know you are not starting "
     "your career over.",
     "But a new industry may not count your experience exactly the way your "
     "current one does.",
     "So do not make either mistake. Do not say I can already do all of "
     "this. And do not say none of my experience counts here.",
     "Separate three things instead. Capability. Context. Credentials.",
   ],
   visual="The posting sentence, then the three-part separation.",
   cta="Sort one destination role into those three.",
   source="V9 hook."),
 S(priority="A", slug="v9_a2_same_verb_different_decision",
   title="The same verb can hide a different decision",
   lines=[
     "Do not declare equivalence just because two roles use the same verb.",
     "Approve can mean checking a routine item in one role and accepting a "
     "consequential risk in another.",
     "So compare the scale of the decision, the consequences of being wrong, "
     "and the support around it.",
     "Then write the capability sentence.",
     "This role needs someone to handle this problem. My evidence is this "
     "example.",
     "If you cannot finish both halves, you have a question to investigate, "
     "not yet a transfer claim.",
   ],
   visual="One verb, two different decisions underneath it.",
   cta="Write both halves of the capability sentence.",
   source="V9 capability."),
 S(priority="A", slug="v9_a3_better_question",
   title="Ask a better question than can I switch",
   lines=[
     "Instead of asking somebody in the field, do you think I could switch "
     "industries, ask this.",
     "Where do otherwise experienced people tend to need the most support "
     "when they first enter this role?",
     "Then ask for an example of a decision that would be unfamiliar.",
     "You are trying to discover the work behind the hiring language.",
     "And remember, a relationship can help you learn the context. It is not "
     "proof that you already know it.",
   ],
   visual="The weak question struck through, replaced by the better one.",
   cta="Ask about the work, not about your potential.",
   source="V9 context."),
 S(priority="A", slug="v9_a4_credentials",
   title="Is it a gate, or did you assume it?",
   lines=[
     "Separate a preference from a requirement, and a requirement from "
     "something you have simply assumed.",
     "A credential can be an employer screen, a professional requirement, or "
     "evidence of preparation. Which one is it here?",
     "Do not assume a course substitutes for a license.",
     "But also do not collect three new qualifications because one "
     "unfamiliar acronym appeared in a job description.",
     "Write down three things. Confirmed requirement. Preferred "
     "qualification. Still unclear.",
     "You do not argue a closed requirement open with better wording.",
   ],
   visual="The three labels, then the closing line at full size.",
   cta="Verify one requirement before you assume it.",
   source="V9 credentials."),
 S(priority="B", slug="v9_b1_defensible_introduction",
   title="A defensible introduction",
   lines=[
     "A careful version of the introduction might sound like this.",
     "I have evidence of coordinating complex delivery decisions across "
     "teams.",
     "I would need to learn this organization's approval routes and "
     "operating risks.",
     "Before proceeding, I want to confirm which direct experience and "
     "qualifications are essential for this role.",
     "That is not a script to memorize. It shows the shape of the decision.",
     "Relevant evidence. Named learning. Verified requirements.",
   ],
   visual="The three parts of the introduction, labeled.",
   cta="Build yours from evidence, learning, and verification.",
   source="V9 put it together."),
 S(priority="B", slug="v9_b2_the_tradeoff",
   title="What are you giving up, and for how long?",
   lines=[
     "A new industry may value some of your experience without preserving "
     "all of your current scope, pay, authority, or status.",
     "That is not a universal rule. It is something to investigate before "
     "you commit.",
     "What are you gaining? What are you giving up? For how long?",
     "And what evidence supports the opportunity rather than just the hope?",
     "A good explanation cannot erase bias, a weak market, a closed hiring "
     "rule, or a real experience gap.",
     "Its job is narrower. It stops you describing all your experience as "
     "either fully portable or worthless.",
   ],
   visual="Gaining and giving up, side by side.",
   cta="Investigate the tradeoff before you commit.",
   source="V9 put it together."),
]

SHORTS[10] = [
 S(priority="A", slug="v10_a1_before_access_ends",
   title="The proof disappears before the experience does",
   lines=[
     "Imagine the job ends tomorrow. Your access is gone.",
     "Then someone asks what you actually accomplished there.",
     "You remember the projects. You remember the pressure. You remember "
     "that something changed because of work you helped do.",
     "But the dashboard is inside a system you cannot open anymore. The "
     "decision trail lived in meetings you no longer attend.",
     "Your experience did not disappear. Your access to the evidence did.",
     "That is why you should know what you can still prove before you "
     "urgently need to explain it.",
   ],
   visual="Experience staying, access falling away.",
   cta="Start one entry while you still have access.",
   source="V10 hook."),
 S(priority="A", slug="v10_a2_preparation_not_extraction",
   title="Preparation is not extraction",
   lines=[
     "One boundary before anything else.",
     "Access to a document does not mean you are entitled to keep it.",
     "Removing a company name does not automatically make restricted "
     "material yours to retain.",
     "No forwarding internal emails, downloading dashboards, copying "
     "customer information, or collecting employee records.",
     "This is about your own high-level account and information you are "
     "permitted to retain.",
     "If you are unsure what you can keep, leave it out and get appropriate "
     "guidance.",
   ],
   visual="Plain full-frame text. No document imagery.",
   cta="Keep the account, not the file.",
   source="V10 the boundary."),
 S(priority="A", slug="v10_a3_calendar_vs_contribution",
   title="A calendar entry is not a contribution",
   lines=[
     "Suppose your note says, attended weekly implementation meetings.",
     "That is a calendar entry. It tells me where you spent time, not what "
     "you contributed.",
     "Now suppose what you actually did was notice that two teams were using "
     "different definitions of completion, explain why that mattered, and "
     "help them agree on a common readiness check.",
     "Now the useful record begins.",
     "I identified conflicting completion criteria and helped the teams "
     "agree what needed to be true before handoff.",
     "Notice what that does not claim. It does not automatically claim that "
     "delays fell.",
   ],
   visual="The calendar entry struck through, replaced by the contribution.",
   cta="Rewrite one calendar entry as a contribution.",
   source="V10 capture the contribution."),
 S(priority="A", slug="v10_a4_qualify_the_claim",
   title="Confirmed, qualified, not yet verified",
   lines=[
     "Put one of three labels beside every result you record.",
     "Confirmed means you have a permitted basis for the statement you are "
     "making.",
     "Qualified means the result needs its scope attached.",
     "Not yet verified means you should not present it as established.",
     "Their job is to stop uncertainty from disappearing when you shorten "
     "the story later.",
     "That is not timid language. It is language that survives the next "
     "question.",
   ],
   visual="Three labels, then the closing line at full size.",
   cta="Label one result you have been rounding up.",
   source="V10 qualify the claim."),
 S(priority="B", slug="v10_b1_name_it_by_the_problem",
   title="Name it by the problem, not the project",
   lines=[
     "A good record is useless if you cannot find it when the question "
     "changes.",
     "Give each entry a name based on the problem or contribution.",
     "Conflicting handoff criteria is more useful than Project Alpha, "
     "especially to somebody outside the company.",
     "Add the period, a few plain-language tags, and the qualification you "
     "need to preserve.",
     "Decision under uncertainty. Cross-team coordination. New operating "
     "context.",
     "Then write one short explanation in ordinary language.",
   ],
   visual="The internal project name replaced by the problem name.",
   cta="Rename one entry by its problem.",
   source="V10 make it retrievable."),
 S(priority="B", slug="v10_b2_two_reasons",
   title="Two reasons the evidence is thin",
   lines=[
     "There are two very different reasons an example may be missing.",
     "You may have done the work and failed to capture it clearly.",
     "Or you may never have had the opportunity to own the decision, access "
     "the result, or build that part of your range.",
     "Do not solve both problems by writing a stronger sentence.",
     "The first needs reconstruction. The second needs an honest account of "
     "the experience you do and do not have.",
     "If a result was never shared with you, say what you can support. Do "
     "not fill the gap with what probably happened.",
   ],
   visual="Two causes, two different fixes.",
   cta="Work out which of the two you are actually looking at.",
   source="V10 when the evidence is thin."),
]

SHORTS[11] = [
 S(priority="A", slug="v11_a1_can_we_reduce_the_team",
   title="Does this mean we can reduce the team?",
   lines=[
     "The report is ready. AI helped produce it.",
     "Then your manager asks, does this mean we can reduce the team?",
     "That is the moment the job changes.",
     "Because if part of your value has been producing the report, a tool "
     "that can produce it faster can feel like it is coming for your role.",
     "But the next question is not, can the tool make the report.",
     "It is, what still has to be interpreted, verified, and decided before "
     "anybody should act?",
   ],
   visual="The question at full size, then the reframe.",
   cta="Map one recurring output into produce, interpret, and decide.",
   source="V11 hook."),
 S(priority="A", slug="v11_a2_the_mix_changed",
   title="The headline improved. The work did not.",
   lines=[
     "These are invented teaching numbers, not customer data.",
     "In the first period, sixty out of a hundred cases met the target. In "
     "the second, eighty out of a hundred did.",
     "The headline looks better.",
     "But separate routine cases from complex ones.",
     "Routine cases met the target ninety percent of the time in both "
     "periods. Complex cases met it forty percent of the time in both "
     "periods.",
     "What changed was the mix. The overall number improved even though the "
     "within-category rates did not.",
   ],
   visual="SYNTHETIC DATA label throughout. The split revealed under the "
          "headline rate.",
   cta="Ask what the aggregate number is hiding.",
   source="V11 demonstration."),
 S(priority="A", slug="v11_a3_produce_interpret_decide",
   title="The task is not the whole job",
   lines=[
     "Take one recurring output from your job. Not your whole profession.",
     "Make three columns. Produce. Interpret. Decide.",
     "Produce is what an approved tool can help make.",
     "Interpret is what the output actually establishes, and what it does "
     "not.",
     "Decide is who owns the consequence, what risks must be accepted, and "
     "what would trigger a reversal.",
     "Then put a verification question under each one.",
   ],
   visual="Three columns building, with a verification question under each.",
   cta="Build the three-column map for one output.",
   source="V11 map your role."),
 S(priority="A", slug="v11_a4_output_is_not_a_decision",
   title="A report is an output. Reducing a team is a decision.",
   lines=[
     "A report is an output. Reducing a team is a decision.",
     "There is work between them, and there is accountability after them.",
     "So a useful sentence is this.",
     "The tool can help produce this output. To use it responsibly, this "
     "role still needs to verify these assumptions, interpret this "
     "consequence, and make or support this decision.",
     "That does not compete with the model's ability to summarize.",
     "It connects the analysis to the work that must happen next.",
   ],
   visual="Output and decision separated, with the work between them.",
   cta="Write that sentence for one output you produce.",
   source="V11 decide."),
 S(priority="B", slug="v11_b1_the_boundary",
   title="The boundary is not machines never interpret",
   lines=[
     "I do not want to build this on a fake premise that AI can only write "
     "and people do all the thinking.",
     "AI can be genuinely useful here. It may help formulate questions, "
     "examine additional data, or compare scenarios.",
     "So the boundary is not, machines never interpret.",
     "The boundary is, is this interpretation supported, relevant, and "
     "sufficient for this decision in this organization?",
     "Your contribution may be knowing which assumptions need checking, or "
     "recognizing that the metric is not measuring what leadership thinks it "
     "measures.",
   ],
   visual="The weak boundary struck through, replaced by the real question.",
   cta="Ask whether the interpretation is sufficient for this decision.",
   source="V11 interpret."),
 S(priority="B", slug="v11_b2_no_ai_proof_job",
   title="Do not look for an AI-proof job",
   lines=[
     "Put your own contribution on the map honestly.",
     "Separate what you already do from what you could learn and what "
     "belongs to another qualified role.",
     "You may find valuable work you have been doing without naming it.",
     "You may find that a large part of the role really is easier to "
     "automate.",
     "None of those findings guarantees that a job will remain. Employers "
     "can reduce roles, change scope, or choose a different operating model.",
     "The goal is not to become the person who adds a human stamp to "
     "anything AI produces.",
   ],
   visual="Plain full-frame text. No reassurance imagery.",
   cta="Be clear about the judgment and consequences the work still "
       "requires.",
   source="V11 map your role."),
]

SHORTS[12] = [
 S(priority="A", slug="v12_a1_constraint_not_conclusion",
   title="I cannot leave yet is not nothing can change",
   lines=[
     "Just leave is easy advice when nobody has asked what your paycheck has "
     "to cover.",
     "Maybe you need the income. Maybe benefits matter. Maybe caregiving, "
     "immigration status, or the timing of your life makes a quick exit "
     "unrealistic.",
     "So start with a more accurate sentence.",
     "I cannot leave yet. That is a constraint.",
     "Nothing can change. That is a conclusion.",
     "They are not the same thing.",
   ],
   visual="The two sentences side by side, labeled.",
   cta="Name your constraint precisely enough to plan around it.",
   source="V12 hook."),
 S(priority="A", slug="v12_a2_name_the_constraint",
   title="Name the constraint precisely",
   lines=[
     "I cannot leave is a conclusion. What is underneath it?",
     "A dependable income right now? An arrangement you cannot interrupt? A "
     "family responsibility? Not knowing what another role would actually "
     "offer?",
     "Then separate what you know from what you have assumed.",
     "You may know you cannot manage a gap in income. You may not yet know "
     "whether a particular employer offers the flexibility you need.",
     "Those are different constraints.",
     "Write one sentence. For now, any change needs to protect, and finish "
     "it with the constraint you actually have.",
   ],
   visual="The sentence stem, waiting to be finished.",
   cta="Finish that sentence privately today.",
   source="V12 protect what must hold."),
 S(priority="A", slug="v12_a3_make_the_tradeoff_visible",
   title="Make the tradeoff visible",
   lines=[
     "Not everything that needs changing requires a resignation. But not "
     "everything can be negotiated either.",
     "Describe the cost concretely.",
     "This job is impossible may capture the feeling.",
     "These two commitments require the same time, and I need a priority "
     "decision, gives someone something specific to address.",
     "A possible sentence is, I can carry A and B at the agreed level. With "
     "C added, what should change in priority, scope, support, or timing?",
     "Use that only where it is safe and appropriate.",
   ],
   visual="The feeling struck through, replaced by the specific request.",
   cta="Describe one recurring cost concretely.",
   source="V12 bound what you can."),
 S(priority="A", slug="v12_a4_question_before_activity",
   title="Choose a question before you choose an activity",
   lines=[
     "Preparation does not have to mean another course or another project.",
     "Sometimes the useful move is recovering one permitted example of work "
     "you already did.",
     "Sometimes it is clarifying one requirement in a role you are "
     "considering.",
     "Choose a question before you choose an activity.",
     "What would I need to prove to be considered for that role, is a "
     "question.",
     "I should be on LinkedIn more, is an activity without a test.",
   ],
   visual="A question and an activity, side by side.",
   cta="Write the question your next small step would answer.",
   source="V12 prepare one possible next step."),
 S(priority="B", slug="v12_b1_exchange_not_add",
   title="Exchange, not automatically add",
   lines=[
     "If there is room inside the current job, development might come from "
     "exchanging a repetitive responsibility for one that involves a new "
     "decision.",
     "Exchange, not automatically add.",
     "Ask what comes off the plate.",
     "And if there is no room, do not manufacture a stretch assignment on "
     "top of an already unsustainable workload just to feel proactive.",
     "A small step should answer a useful question or preserve an option. "
     "Otherwise it is just more activity.",
   ],
   visual="Something coming off the plate as something goes on.",
   cta="Ask what comes off before anything goes on.",
   source="V12 prepare one possible next step."),
 S(priority="B", slug="v12_b2_four_lines",
   title="Four lines, and permission to do less",
   lines=[
     "Put four lines on a page.",
     "What must hold for now? What part of the current situation can I "
     "influence safely? What one question would make the next option "
     "clearer? And when will I review this again?",
     "That last line matters because for now needs a way to be revisited.",
     "If your capacity is extremely limited, choose only the first line and "
     "the review point.",
     "Protecting yourself and postponing a nonessential career project can "
     "be a deliberate choice.",
     "You do not owe anyone constant visible progress to prove you care "
     "about your future.",
   ],
   visual="Four lines, with the reduced version shown beside them.",
   cta="Write the lines your capacity actually allows.",
   source="V12 the plan."),
]

SHORTS[13] = [
 S(priority="A", slug="v13_a1_stop_collecting_activity",
   title="Stop collecting career activity",
   lines=[
     "You have saved the jobs. Rewritten the headline. Maybe started a "
     "course.",
     "And you still do not know whether you actually want the work you are "
     "preparing for.",
     "That is the problem with career activity. It can make you feel "
     "productive without answering the decision.",
     "So before you make a high-cost commitment, choose one destination and "
     "test it for thirty days.",
     "Define. Investigate. Try. Decide.",
     "And the test only works if not this option is allowed to be a good "
     "result.",
   ],
   visual="The four phases building, then the permission line.",
   cta="Choose one destination and write the hypothesis.",
   source="V13 hook."),
 S(priority="A", slug="v13_a2_testable_destination",
   title="Choose a destination specific enough to test",
   lines=[
     "Something strategic is too vague to test.",
     "An internal operations-improvement role that uses my cross-team "
     "problem solving and keeps predictable hours gives you something you "
     "can investigate.",
     "Then write one hypothesis.",
     "This option may fit because it uses this evidence, builds this missing "
     "experience, and meets these constraints.",
     "Then write what would change your mind.",
     "A useful test has permission to produce an inconvenient answer.",
   ],
   visual="The vague version struck through, replaced by the testable one.",
   cta="Write the hypothesis and what would change your mind.",
   source="V13 setup."),
 S(priority="A", slug="v13_a3_ask_about_the_work",
   title="Do not ask for reassurance. Ask about the work.",
   lines=[
     "In the investigation week, do not ask for blanket reassurance about "
     "your potential.",
     "Ask about the work.",
     "What is a difficult ordinary week in this role?",
     "Where do people with an adjacent background tend to need support?",
     "Which decisions distinguish someone who is ready from someone who "
     "still needs supervision?",
     "A pleasant conversation is not an offer, and it is not proof that you "
     "meet every requirement.",
   ],
   visual="The three questions building in order.",
   cta="Ask those three, not whether you could do it.",
   source="V13 days 8 to 14."),
 S(priority="A", slug="v13_a4_effort_is_not_evidence",
   title="Do not confuse effort with evidence",
   lines=[
     "At the end of the month, stop collecting activities and read the "
     "record.",
     "Do not confuse effort with evidence.",
     "Reading descriptions, having conversations, and making a sample are "
     "activities.",
     "What those activities teach you is the evidence that informs the "
     "decision.",
     "Then choose one of three. Continue. Modify. Stop pursuing this version "
     "of the option.",
     "And if the month ends without enough evidence, call the result "
     "inconclusive.",
   ],
   visual="Activities on one side, evidence on the other.",
   cta="Write why you will continue, modify, or stop.",
   source="V13 the evidence standard."),
 S(priority="B", slug="v13_b1_bounded_sample",
   title="Try one bounded piece",
   lines=[
     "In the third week, test one important part of the destination where a "
     "safe and relevant sample is possible.",
     "Use public, synthetic, or otherwise permitted material.",
     "Do not recreate a confidential employer process. Do not turn the "
     "exercise into unpaid operational work for a prospective employer.",
     "Set a time limit before you begin. The sample should answer a "
     "question, not become a consulting engagement.",
     "A simulation can show a way of thinking. It cannot prove results with "
     "real customers or a team you have never led.",
     "Label it as a work sample, not professional experience.",
   ],
   visual="The boundary stated plainly, no imagery.",
   cta="Set the time limit before you start.",
   source="V13 days 15 to 21."),
 S(priority="B", slug="v13_b2_stop_is_a_good_result",
   title="Stop is a real result",
   lines=[
     "Continue does not mean resign tomorrow. It could mean a targeted "
     "conversation, an application, or a specific learning commitment now "
     "supported by evidence.",
     "Modify might mean an adjacent role, a different employer, a supervised "
     "entry point, or a longer preparation period.",
     "Stop means the investigation gave you a reason not to keep investing "
     "here right now.",
     "That is useful information.",
     "Do not turn uncertainty into a yes because you spent thirty days on "
     "it.",
   ],
   visual="Three outcomes, none styled as failure.",
   cta="Let the evidence choose, not the sunk time.",
   source="V13 days 22 to 30."),
]

# ---------------------------------------------------------------- V14 to V21
# Audited against the corrected masters rather than carried forward
# automatically. V14's master is byte-identical, so its Shorts are genuine
# REUSE. V15 to V21 were written against the shortened September 10 masters;
# the restored masters preserve and expand the same teaching, so each Short
# was re-read against its corrected master and every claim confirmed to be
# supported there. Where the corrected master changes wording the Short uses,
# the Short is reclassified.
from shorts1421 import SHORTS as _SEP10

_AUDIT = {
 14: ("REUSE", "The V14 master is byte-identical to the one this Short was "
               "written against, SHA-256 4a36cc83. Carried unchanged."),
 15: ("REUSE", "Re-read against the restored master. Every claim is "
               "supported there, and the restored version expands the same "
               "teaching rather than changing it."),
 16: ("REUSE", "Re-read against the restored master. Every claim is "
               "supported, including the hinge, the four separations and the "
               "limits section."),
 17: ("REUSE", "Re-read against the restored master. The four lines, line "
               "two, the speed section and both boundaries are all present "
               "in the corrected text."),
 18: ("REUSE", "Re-read against the restored master. The five variables, the "
               "four questions, ask for names and the two-sidedness are all "
               "present."),
 19: ("COPY UPDATE", "Re-read against the restored master. The teaching is "
                     "unchanged, but the corrected title is now 'Should You "
                     "Become a Consultant? The Part Everyone Leaves Out', so "
                     "the packaging around these Shorts changes."),
 20: ("COPY UPDATE", "Re-read against the restored master. The opening "
                     "personal account is reworded in the corrected master, "
                     "so any Short echoing it is reclassified even where the "
                     "teaching is unchanged."),
 21: ("REUSE", "Re-read against the restored master. The five layers, the "
               "licensing line and the read-or-practice split are all "
               "present in the corrected text."),
}

# Per-Short findings from reading each carried Short against its corrected
# master. Four were genuinely built on superseded structure or wording and are
# corrected below rather than carried forward. The rest were confirmed line by
# line: a low lexical overlap with the master is rephrasing, not an unsupported
# claim, and each was checked individually.
_OVERRIDE = {
 ("v17_a2_four_lines"): (
   "COPY UPDATE",
   "The corrected master's third line reads 'what did I conclude that the "
   "output did not say'. The Short said 'the initial output did not "
   "establish'. Aligned to the master's wording.",
   {2: "One. What was I asked to get right. Not what was I asked to "
       "produce.",
    4: "Three. What did I conclude that the output did not say."}),
 ("v17_a3_line_two"): (
   "COPY UPDATE",
   "The Short attributed the reason to history, pattern recognition and "
   "domain knowledge. The corrected master does not say that; it says the "
   "knowledge came from doing the work before it got faster. Replaced.",
   {1: "What did I check, and why did I check that.",
    3: "The part that requires you is knowing which two things in the result "
       "were worth checking, and why those two. That knowledge came from "
       "doing the work before it got faster.",
    4: "Write it the same day or you will lose it."}),
 ("v20_a3_three_buckets"): (
   "REBUILD",
   "Built on the superseded three-bucket structure. The corrected master "
   "uses six categories, so the Short is rebuilt against them.",
   None),
 ("v20_b2_decay_vs_change"): (
   "COPY UPDATE",
   "The closing line referred to the superseded 'needs updating' bucket. "
   "Replaced with what the corrected master actually says about the two "
   "categories.",
   {4: "Both are worth naming separately, because what decayed is about you "
       "and what changed is about the field."}),
}

for _n, (_st, _why) in _AUDIT.items():
    SHORTS[_n] = []
    for _s in _SEP10[_n]:
        _t = dict(_s)
        _t["status"] = _st
        _t["why"] = _why
        if _t["slug"] in _OVERRIDE:
            _ost, _owhy, _lines = _OVERRIDE[_t["slug"]]
            _t["status"], _t["why"] = _ost, _owhy
            if _lines:
                _new = list(_t["lines"])
                for _i, _txt in _lines.items():
                    _new[_i] = _txt
                _t["lines"] = _new
        SHORTS[_n].append(_t)

# The rebuilt V20 Short, written against the corrected six categories.
for _i, _s in enumerate(SHORTS[20]):
    if _s["slug"] == "v20_a3_three_buckets":
        SHORTS[20][_i] = S(
          priority="A", slug="v20_a3_six_categories",
          title="Six categories instead of behind on everything",
          lines=[
            "Before the applications, sort what you have into six "
            "categories.",
            "What stayed current. Some things do not decay. How you read a "
            "room, how you structure a problem, what good work looks like.",
            "What decayed. The particular system you have not touched. The "
            "pace of a workday you have not kept for a while.",
            "What changed in the field while you were away. That is "
            "different from decay. The thing itself moved.",
            "What changed in your circumstances. That decides which routes "
            "are actually open to you.",
            "What is unproven rather than absent. And what genuinely has to "
            "be rebuilt.",
          ],
          visual="Six categories filling one at a time.",
          cta="Sort one capability into one of the six.",
          source="V20 the six categories.",
          status="REBUILD",
          why="Built on the superseded three-bucket structure. The corrected "
              "master uses six categories, so the Short is rebuilt against "
              "them.")
