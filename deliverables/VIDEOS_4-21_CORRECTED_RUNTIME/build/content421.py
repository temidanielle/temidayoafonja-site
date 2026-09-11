# -*- coding: utf-8 -*-
"""Publishing copy, viewer exercises and the problem/solution/outcome check
for all eighteen videos, written against the corrected September 11 masters.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M

ROUTES = {
 "Career Evidence Starter": "temidayoafonja.com/career-evidence-starter",
 "Field Kit": "temidayoafonja.com/fieldkit",
 "Capability Formation Field Kit": "temidayoafonja.com/fieldkit",
 "Career Decision Evidence Check": "temidayoafonja.com/career-decisions",
 "Keep the Proof": "temidayoafonja.com/keep-the-proof",
}
PLAYLIST = "Capability Formation: career pivots and internal moves"

# PAINFUL PROBLEM -> SOLUTION / TOOL -> VIEWER OUTCOME, per section 26.
PSO = {
 4: ("You are looking at a role you have never held, and you cannot tell "
     "whether never having held the title means you cannot do the work.",
     "Three stops, and a 3-line readiness case: problem, proof, gap.",
     "You can separate 'I have never held this title' from 'I do not yet "
     "have the evidence this work requires', and say which one you have."),
 5: ("You are changing career tracks and other people are reading you like a "
     "beginner, and you are starting to do it to yourself.",
     "Carry, Translate, Relearn, Prove, written as a 4-line move case.",
     "You can state what travels, translate it into the destination's terms, "
     "name the real gap, and support the level you are claiming."),
 6: ("A new role has more money, more visibility and a bigger title, and you "
     "cannot tell whether it will actually develop you.",
     "Work, Judgment, Evidence, plus the 12-month question.",
     "You can make a cleaner yes, no or negotiate decision, and take the "
     "role for the reason it actually serves."),
 7: ("Your scope keeps growing, everyone calls it growth, and you are not "
     "sure whether you are being developed or simply absorbed.",
     "CAR: Complexity, Authority, Return, used before you accept more.",
     "You can tell capacity use from growth, and ask for the review point "
     "before temporary scope becomes permanent."),
 8: ("You built something from scratch, it now runs well, and nobody can see "
     "how hard it was.",
     "Before, My Part, Judgment, Proof, with evidence levels Existence, Use "
     "and Effect.",
     "You can give a four-sentence account a stranger understands, without "
     "overstating causation."),
 9: ("A job description says direct industry experience required, and you "
     "cannot tell whether your experience counts for something or nothing.",
     "Capability, Context, Credentials, read against one destination role.",
     "You can say what you can support with evidence now, what must be "
     "learned, and which requirements are actually gates."),
 10: ("Your access could end before you ever have to explain what you "
      "accomplished, and the evidence lives in systems you will lose.",
      "Capture the contribution, qualify the claim, make it retrievable, "
      "inside a clear compliance boundary.",
      "You have a permitted record that survives the next question, and you "
      "know which claims are confirmed, qualified or unverified."),
 11: ("A tool produced the output and your manager asks whether the team can "
      "be reduced.",
      "Produce, Interpret, Decide, with a verification question under each.",
      "You can show what the role still has to verify, interpret and decide, "
      "without claiming the tool did nothing or that any job is safe."),
 12: ("You cannot leave yet, and it is starting to feel as though nothing "
      "can change.",
      "Protect what must hold, bound what you can, prepare one possible next "
      "step, written as four lines with a review point.",
      "You have a plan that fits the constraint you actually have, and a "
      "date or condition for revisiting it."),
 13: ("You have collected career activity for months and still cannot answer "
      "whether you want the work you are preparing for.",
      "A 30-day test: Define, Investigate, Try, Decide.",
      "You can continue, modify or stop on evidence rather than on sunk "
      "effort, and say why."),
 14: ("You are reading a role in another industry and cannot tell which "
      "parts of your experience actually transfer.",
      "Two questions applied to every familiar requirement, then a "
      "four-bucket audit.",
      "You can sort one destination role into travels, looks similar, must "
      "be learned and must be experienced, with evidence for the first."),
 15: ("Someone asks what you recommend, the evidence is incomplete, and you "
      "realize the work never required you to make that call.",
      "Three gaps and three responses: Learn, Practice, Prove.",
      "You can name the one gap you actually have and take the one step that "
      "matches it."),
 16: ("Your work is relied on and your name is not in the room where scope "
      "is decided.",
      "Four separations, the does-not-know versus knows-and-does-not-act "
      "hinge, and a three-item contribution record.",
      "You can remove the obstacle that was yours, then read what is left "
      "and decide whether to wait or test elsewhere."),
 17: ("A tool produces most of the visible work and the answer to what you "
      "actually did has become hard to give.",
      "A four-line contribution record, with line two carrying the "
      "judgment.",
      "You have evidence of the contribution that survives the output "
      "becoming cheap, without claiming judgment makes a job safe."),
 18: ("You have been offered a management role and congratulated instead of "
      "told what the job is.",
      "Five variables that do not move together, and four questions to ask "
      "before answering.",
      "You can decide on what the role actually contains, and know what you "
      "still do not know."),
 19: ("People keep telling you to consult, and nobody has said what a buyer "
      "would actually purchase.",
      "Expertise, offer, buyer, repeatability, tested with a one-page "
      "proposal before anything is risked.",
      "You have one defined service, a named buyer, and the conditions that "
      "would have to be true before consulting is a real option."),
 20: ("You are returning after a break and the gap is the first thing "
      "everyone asks about.",
      "Six categories, and the distinction between unproven and absent.",
      "You have a two-part record: what is current with its evidence, and "
      "what you are rebuilding now with a date."),
 21: ("You changed industries, you can still do the work, and something else "
      "keeps catching you out.",
      "A five-layer relearning inventory, ordered by what blocks "
      "contribution first.",
      "You know which layer to start with, and which parts you cannot read "
      "your way into."),
}

# Description bodies. Paragraphs separated by blank lines.
DESC = {
 4: ("Three times in five years I stepped into a role that had no "
     "predecessor. Each time the title was new. The work underneath it was "
     "not completely new.\n\n"
     "This video is about what I stopped doing: waiting for an exact title "
     "match, proving readiness with a task list, and treating every learning "
     "gap as evidence that I was not ready.\n\n"
     "You will leave with a three-line readiness case for one role you have "
     "never held. Problem, proof, gap.\n\n"
     "A note on the limit. A strong readiness case does not guarantee that "
     "an employer will choose you. Credentials, markets, relationships, "
     "compensation, employer preferences and bias still matter."),
 5: ("Changing career tracks can make other people read you like a "
     "beginner. The more expensive mistake is when you start doing it to "
     "yourself.\n\n"
     "This video separates four things: what you can carry, what you have to "
     "translate, what you genuinely need to relearn, and what you can "
     "prove.\n\n"
     "You will leave with a four-line move case for one move you are "
     "considering.\n\n"
     "It is honest in both directions. You do not need to apologize for "
     "every gap, and you do not get to rename a real domain or credential "
     "requirement as a transferable skill because that makes the move easier "
     "to explain."),
 6: ("I have worked across eight industries and sectors, and one thing that "
     "taught me is that movement can look like career growth long before the "
     "work actually changes.\n\n"
     "This video asks three things of any new role: will the work change, "
     "will your judgment expand, and will the evidence travel.\n\n"
     "Then one question. Twelve months from now, what will you be able to "
     "do, decide or prove that you cannot do today?\n\n"
     "A role does not have to maximize growth to be a good decision. The "
     "problem is calling every move development when the work underneath it "
     "has barely changed."),
 7: ("You can become more valuable to your organization without becoming "
     "more valuable to your own future. It took me years to learn that being "
     "trusted with more is not the same as being developed for more.\n\n"
     "This video uses three tests before you accept more work. Complexity: "
     "did the problem get harder, or did the volume get bigger? Authority: "
     "did your decision rights move with the responsibility? Return: what is "
     "the extra work giving back?\n\n"
     "You will leave able to run CAR on one responsibility you added in the "
     "last six months, and to ask for the review point before temporary "
     "scope becomes permanent.\n\n"
     "More work can be part of growth. It is not proof of it."),
 8: ("If you build something well enough, eventually nobody can see how hard "
     "it was. The process exists, people use it, and the uncertainty you "
     "solved at the beginning has disappeared from view.\n\n"
     "This video uses four things to put the missing information back: the "
     "Before, My Part, the Judgment, and the Proof.\n\n"
     "It also separates three levels of evidence that are not "
     "interchangeable. Existence, Use and Effect. A process can exist "
     "without being used, and be used without producing the outcome you "
     "hoped for.\n\n"
     "Proof does not mean taking your employer's files. Keep only "
     "information you are permitted to retain."),
 9: ("Direct industry experience required. One sentence in a job description "
     "can make an experienced professional feel like a beginner again.\n\n"
     "This video separates three things so you can read a destination role "
     "accurately: Capability, what you can already prove. Context, what "
     "changes when the setting changes. Credentials, what is actually a "
     "gate.\n\n"
     "It is careful in both directions. Do not say you can already do all of "
     "it, and do not say none of your experience counts.\n\n"
     "A good explanation cannot erase bias, a weak market, a closed hiring "
     "rule or a real experience gap. Its job is narrower."),
 10: ("Imagine the job ends tomorrow and your access is gone. Your "
      "experience did not disappear. Your access to the evidence did.\n\n"
      "This video is a preparation habit, not a prediction and not a reason "
      "to take company files. Capture the contribution, qualify the claim, "
      "make it retrievable.\n\n"
      "One boundary is stated clearly. Access to a document does not mean "
      "you are entitled to keep it, and removing a company name does not "
      "make restricted material yours to retain.\n\n"
      "You will leave with one permitted entry and a way of labelling what "
      "is confirmed, qualified, or not yet verified."),
 11: ("The report is ready, AI helped produce it, and your manager asks "
      "whether that means the team can be reduced.\n\n"
      "This video works through a small synthetic example where the headline "
      "rate improves while the within-category rates do not, because the "
      "case mix changed. The numbers are invented teaching figures, not "
      "customer data.\n\n"
      "Then it maps one recurring output across three columns: Produce, "
      "Interpret, Decide, with a verification question under each.\n\n"
      "It does not claim that machines never interpret, and it does not "
      "promise that any job will remain. Employers can reduce roles, change "
      "scope, or choose a different operating model."),
 12: ("Just leave is easy advice when nobody has asked what your paycheck "
      "has to cover.\n\n"
      "I cannot leave yet is a constraint. Nothing can change is a "
      "conclusion. They are not the same thing.\n\n"
      "This video helps you protect what must hold, bound what you can "
      "influence safely, and prepare one possible next step. You will leave "
      "with four private lines and a review point.\n\n"
      "If health, safety, harassment, discrimination or another urgent issue "
      "is involved, appropriate support comes before any career exercise. "
      "This video cannot interpret an employment agreement, benefits, "
      "immigration rules or a health decision."),
 13: ("You have saved the jobs, rewritten the headline, maybe started a "
      "course, and you still do not know whether you want the work you are "
      "preparing for.\n\n"
      "This video gives you a thirty-day test for one destination. Define, "
      "Investigate, Try, Decide.\n\n"
      "The test only works if not this option is allowed to be a good "
      "result. At the end you continue, modify, or stop, on evidence rather "
      "than on the effort you spent.\n\n"
      "It cannot validate every part of your career, overcome employer bias, "
      "guarantee access, or remove a real qualification gap."),
 15: ('Three career gaps feel identical from the inside and need '
      'completely different responses.\n'
      '\n'
      'A learning gap, where there is something you genuinely do not '
      'know yet. A practice and authority gap, where you understand the '
      'decision but have never been allowed to own it. And an evidence '
      'gap, where you already know how and nobody can see enough '
      'proof.\n'
      '\n'
      'Learn. Practice. Prove. If you misread which one you have, you '
      'can spend a year fixing the wrong problem.\n'
      '\n'
      'This is a reflection tool, not a diagnostic. It does not assign '
      'you a type, and some of these gaps are shaped by the '
      'organization rather than by you.'),
 16: ('There is a particular kind of stuck that is not the same as '
      'being invisible. Your work is relied on. Your name is not in the '
      'room where scope gets decided.\n'
      '\n'
      'The usual advice is to speak up more. That can help, but it '
      'treats several different problems as though they are one.\n'
      '\n'
      'This video separates four: is the work seen, is it attributed to '
      'you, are you trusted for delivery or considered for larger '
      'scope, and is the obstacle one you can actually remove.\n'
      '\n'
      'It is honest about the limit. A clearer record does not override '
      'bias, create a role that does not exist, or move a budget you do '
      'not control. What it does is remove the obstacle that is yours, '
      'so whatever remains becomes easier to see.'),
 17: ('The report used to take two days. Now a tool produces most of it '
      'in forty minutes. The work is not worse, but the answer to what '
      'did you actually do has become harder to give.\n'
      '\n'
      'The problem is usually not that your value dropped. It is that '
      'the artifact used to be the evidence, and the artifact has '
      'stopped being scarce.\n'
      '\n'
      'This video gives four lines to keep for one piece of AI-assisted '
      'work: what you were asked to get right, what you checked and '
      'why, what you concluded that the output did not say, and what '
      'you were accountable for.\n'
      '\n'
      'It does not claim that human judgment makes a job safe, and it '
      'does not claim that these tools cannot perform work that looks '
      'like judgment. The narrower point holds either way.'),
 18: ('Management is often offered as a reward. It is not a reward. It '
      'is a different job.\n'
      '\n'
      'This video separates five things that get bundled together and '
      'do not reliably move together: scope, responsibility, '
      'compensation, authority, and people management.\n'
      '\n'
      'Then four questions to ask before you answer. What does the job '
      'consume? Does the other path really exist here? What authority '
      'comes with it? And can you come back?\n'
      '\n'
      'It stays two-sided. Some organizations genuinely cap individual '
      'contributors, and that is information you need rather than '
      'encouragement or discouragement.'),
 19: ('Someone has told you that you should consult. It usually arrives '
      'right after you solve something difficult, which is why almost '
      'nobody examines it.\n'
      '\n'
      'Your experience tells you what you know. It does not '
      'automatically tell you what somebody will buy.\n'
      '\n'
      'This video separates four things people call consulting: '
      'expertise, an offer, a buyer, and repeatability. Then it works '
      'through the buyer question, turning expertise into a '
      'deliverable, and how to test the offer before you change '
      'anything.\n'
      '\n'
      'No income promises, no client promises, and no business-setup '
      'advice. Check your own employment agreement before side work or '
      'outreach. This video is not legal or tax advice.'),
 20: ('Returning after a career break is not mainly about finding the '
      'perfect sentence to explain the gap. The explanation matters. It '
      'is not the whole return.\n'
      '\n'
      'This video sorts what you carry into three buckets: still '
      'current, needs updating, and needs rebuilding. And it holds on '
      'to one distinction that saves people a great deal of wasted '
      'effort. Unproven is not the same as absent.\n'
      '\n'
      'It is honest about the market. Bias against career breaks '
      'exists, and a better explanation does not make every employer '
      'fair. Some routes back may involve a different title, scope or '
      'compensation, which is a tradeoff to evaluate rather than a '
      'measurement of your worth.'),
 21: ('You made the industry change, and you can still do the work. '
      'What keeps catching you are the things nobody thought to '
      'explain.\n'
      '\n'
      'This video sorts the relearning into five layers: what the work '
      'is actually about here, regulation and credentials, systems and '
      'tooling, relationships and internal history, and how decisions '
      'actually get made.\n'
      '\n'
      'It says the part a lot of career content avoids. A licensing '
      'requirement is not a mindset issue. If a role requires a '
      'qualification you do not hold, adjacent experience does not '
      'erase that.\n'
      '\n'
      'You will leave with an inventory for one destination role, '
      'ordered by one question: what stops me contributing usefully '
      'first?'),
}
DESC[14] = ("Most transferable-skills advice stops at the words. This video "
            "compares what the words actually sit on top of.\n\n"
            "Working from a structured reading of 28 senior program and "
            "project delivery job descriptions across healthcare, financial "
            "services and technology, all collected on September 10, 2026, "
            "it separates the delivery work that genuinely recurs across "
            "industries from the requirements that only look portable until "
            "you examine the decision underneath.\n\n"
            "The test is two questions. What would this person actually have "
            "to decide? And what happens if they decide badly?\n\n"
            "You will leave with a four-bucket audit for one destination "
            "role: what travels, what only looks similar, what must be "
            "learned, and what must be experienced.\n\n"
            "A note on the evidence. 28 job descriptions are a convenience "
            "sample. They show what these employers chose to write down on "
            "one date. They do not represent the labor market, they do not "
            "prove two roles are interchangeable, and they cannot tell you "
            "who would be hired.")

PINNED = {
 4: ("One role you have never held. Three lines.\n"
     "Problem: what does this role actually need someone to solve?\n"
     "Proof: what have I already done that shows the underlying judgment?\n"
     "Gap: what do I genuinely need to learn, earn or experience?\n\n"
     "If the proof is thin, you know what evidence you still need. If the "
     "gap is a hard gate, you know what must change before the move makes "
     "sense."),
 5: ("Four lines for one move you are considering.\n"
     "Carry: the capability that still helps.\n"
     "Translate: how it shows up in the new context.\n"
     "Relearn: the genuine gap.\n"
     "Prove: one example that supports the level you are claiming.\n\n"
     "More honest than either I am starting over or everything transfers."),
 6: ("Write one sentence under each before your next move.\n"
     "Work: will the problem actually change?\n"
     "Judgment: will my decision rights expand?\n"
     "Evidence: will I be able to prove the growth somewhere else?\n\n"
     "Then the 12-month question. Twelve months from now, what will I be "
     "able to do, decide or prove that I cannot do today?"),
 7: ("Run CAR on one responsibility you added in the last six months.\n"
     "Complexity: did the problem get harder, or did the volume get bigger?\n"
     "Authority: did your decision rights move with it?\n"
     "Return: capability, evidence, or recognition?\n\n"
     "And before the next 'can you take this too', ask when you will review "
     "what the extra scope returns."),
 8: ("Choose one thing people now take for granted because it works, and "
     "write four sentences.\n"
     "Before. My Part. Judgment. Proof.\n\n"
     "Then check which level of evidence you actually have. Existence means "
     "it was created. Use means people adopted it. Effect means something "
     "changed because of it. Do not jump from existence to effect."),
 9: ("One destination role. Not five industries at once.\n"
     "Capability: what can I already prove?\n"
     "Context: what changes in this setting?\n"
     "Credentials: what is actually a gate?\n\n"
     "Then make one move that reduces uncertainty. Verify a requirement, ask "
     "about a difficult decision in the role, or find your strongest "
     "example."),
 10: ("Start with one entry.\n"
      "Capture the contribution, not the calendar.\n"
      "Qualify the claim: confirmed, qualified, or not yet verified.\n"
      "Make it retrievable by naming it after the problem.\n\n"
      "And keep the boundary. This is your own high-level account and "
      "information you are permitted to retain. Not company files."),
 11: ("Take one recurring output from your job and build three columns.\n"
      "Produce. Interpret. Decide.\n"
      "Then put a verification question under each.\n\n"
      "The figures in the example are invented teaching numbers, not "
      "customer data and not a result from my career."),
 12: ("Four lines, written privately.\n"
      "What must hold for now?\n"
      "What can I influence safely?\n"
      "What one question would make the next option clearer?\n"
      "When will I review this again?\n\n"
      "If your capacity is very limited, choose only the first line and the "
      "review point. That is a deliberate choice, not a failure."),
 13: ("Choose one destination and write the hypothesis before you add "
      "another course.\n"
      "Define. Investigate. Try. Decide.\n\n"
      "And let not this option be a good result. If the month ends without "
      "enough evidence, call it inconclusive rather than turning uncertainty "
      "into a yes."),
 15: ('Name one gap and the step that matches it.\n'
      'LEARN, PRACTICE or PROVE. One word, one sentence.\n'
      '\n'
      'This is a reflection tool, not a diagnostic. It does not assign '
      'you a type, and some of these gaps are shaped by the '
      'organization rather than by you.'),
 16: ('Write one decision you made and what it changed.\n'
      '\n'
      'Then the harder read: does your manager not know, or do they '
      'know and not act? Those are different situations, and you cannot '
      'tell which one you are in until the information problem is gone.'),
 17: ('Take one piece of work from this week where a tool did most of '
      'the visible production, and write what you checked and why.\n'
      '\n'
      'That is the line people forget fastest, and it is the one that '
      'carries the contribution.'),
 18: ('Before you answer the offer, ask four questions.\n'
      'What does the job consume? Does the other path really exist '
      'here? What authority comes with it? Can you come back?\n'
      '\n'
      'And ask for names. If nobody can name a person on the senior '
      'individual track, that path may exist on a slide and nowhere '
      'else.'),
 19: ('One sentence: what would somebody receive from you, and by '
      'when?\n'
      '\n'
      'If that is hard to write, the offer is still a description of '
      'you rather than something a person can buy. Check your '
      'employment agreement before any outreach. This video is not '
      'legal or tax advice.'),
 20: ('Two short lists.\n'
      'What is current now, with evidence for each item.\n'
      'What you are rebuilding now, with a date attached.\n'
      '\n'
      'The date is the part entirely within your control.'),
 21: ('Build the five-layer inventory for one destination role, then '
      'reorder it by one question: what stops me contributing usefully '
      'first?\n'
      '\n'
      'And check the binding requirements from the body or employer '
      'that actually sets them. A licensing requirement is not a '
      'mindset issue.'),
}
PINNED[14] = ("The two questions from this video, for one role you are "
              "considering:\nWhat would I actually have to decide? What "
              "happens if I decide badly?\nThen sort what you find into "
              "TRAVELS, LOOKS SIMILAR, MUST BE LEARNED, MUST BE "
              "EXPERIENCED.\n\nOn the evidence: 28 retained job "
              "descriptions, 10 healthcare, 10 financial services, 8 "
              "technology, all collected September 10, 2026. That is a "
              "convenience sample of what these employers wrote down. It "
              "does not represent the labor market and it cannot tell you "
              "who gets hired.")

TAGS = {
 4: ["new role", "first in the role", "career readiness", "job title",
     "experienced professionals", "career change", "internal move",
     "readiness case", "career evidence", "mid career", "career strategy",
     "no predecessor"],
 5: ["career change", "changing career tracks", "transferable skills",
     "career pivot", "starting over", "career evidence", "seniority",
     "experienced professionals", "consulting to corporate", "mid career",
     "career strategy", "career translation"],
 6: ["is this role growth", "career growth", "new role decision",
     "internal move", "career decision", "job offer", "experienced "
     "professionals", "career development", "promotion", "mid career",
     "career strategy", "eight industries"],
 7: ["more work is not growth", "workload", "career growth", "scope creep",
     "authority at work", "career development", "experienced professionals",
     "promotion", "stretch assignment", "mid career", "career strategy",
     "being dependable"],
 8: ["show your impact", "built from scratch", "career evidence",
     "contribution record", "first in the role", "experienced professionals",
     "performance review", "attribution", "foundational work", "mid career",
     "career strategy", "proving impact"],
 9: ["change industries", "industry change", "career pivot",
     "transferable skills", "direct industry experience", "career change",
     "experienced professionals", "credentials", "domain knowledge",
     "mid career", "career strategy", "new field"],
 10: ["layoff preparation", "career evidence", "before a layoff",
      "contribution record", "job loss", "experienced professionals",
      "career records", "proving impact", "redundancy", "mid career",
      "career strategy", "keep the proof"],
 11: ["AI at work", "will AI take my job", "AI and careers",
      "future of work", "knowledge work", "experienced professionals",
      "AI automation", "professional value", "decision making", "mid career",
      "career strategy", "task versus job"],
 12: ["cannot quit my job", "stuck at work", "career constraints",
      "job search", "career planning", "experienced professionals",
      "work boundaries", "career decision", "financial constraints",
      "mid career", "career strategy", "what can change now"],
 13: ["test a career change", "30 day plan", "career experiment",
      "career decision", "career pivot", "experienced professionals",
      "job research", "career planning", "before you quit", "mid career",
      "career strategy", "career test"],
 15: ['career gaps',
      'decision making at work',
      'career development',
      'experienced professionals',
      'career growth',
      'skills gap',
      'career reflection',
      'workplace judgment',
      'career evidence',
      'mid career',
      'professional development',
      'career strategy'],
 16: ['overlooked at work',
      'workplace recognition',
      'career visibility',
      'promotion',
      'contribution record',
      'career evidence',
      'experienced professionals',
      'workplace advice',
      'scope and promotion',
      'mid career',
      'career strategy',
      'being undervalued'],
 17: ['AI at work',
      'proving your value',
      'contribution record',
      'AI and careers',
      'career evidence',
      'knowledge work',
      'experienced professionals',
      'workplace AI',
      'professional value',
      'career strategy',
      'mid career',
      'future of work'],
 18: ['individual contributor',
      'should I become a manager',
      'management career',
      'career decision',
      'IC vs manager',
      'career path',
      'promotion decision',
      'experienced professionals',
      'senior individual contributor',
      'career strategy',
      'mid career',
      'people management'],
 19: ['consulting',
      'should I consult',
      'independent consulting',
      'career change',
      'consulting business',
      'career decision',
      'experienced professionals',
      'leaving employment',
      'consulting offer',
      'career strategy',
      'mid career',
      'professional services'],
 20: ['career break',
      'returning to work',
      'career gap',
      'return to work',
      'maternity leave return',
      'career restart',
      'returnship',
      'experienced professionals',
      'career reentry',
      'career strategy',
      'mid career',
      'employment gap'],
 21: ['changing industries',
      'industry change',
      'career pivot',
      'transferable skills',
      'new industry',
      'career transition',
      'relearning',
      'experienced professionals',
      'domain knowledge',
      'career strategy',
      'mid career',
      'starting over'],
}
TAGS[14] = ["transferable skills", "career change", "changing industries",
            "job description analysis", "career pivot", "program manager",
            "project manager", "senior individual contributor",
            "career research", "experienced professionals",
            "industry transfer", "career strategy"]

HASH = {
 4: ["#CareerChange", "#NewRole", "#CapabilityFormation"],
 5: ["#CareerChange", "#TransferableSkills", "#CapabilityFormation"],
 6: ["#CareerGrowth", "#CareerDecisions", "#CapabilityFormation"],
 7: ["#CareerGrowth", "#WorkloadVsGrowth", "#CapabilityFormation"],
 8: ["#CareerEvidence", "#ShowYourImpact", "#CapabilityFormation"],
 9: ["#ChangingIndustries", "#CareerChange", "#CapabilityFormation"],
 10: ["#CareerEvidence", "#LayoffPreparation", "#CapabilityFormation"],
 11: ["#AIAtWork", "#FutureOfWork", "#CapabilityFormation"],
 12: ["#CareerAdvice", "#StuckAtWork", "#CapabilityFormation"],
 13: ["#CareerChange", "#CareerPlanning", "#CapabilityFormation"],
 14: ["#CareerChange", "#TransferableSkills", "#CapabilityFormation"],
 15: ['#CareerGrowth', '#CareerDevelopment', '#CapabilityFormation'],
 16: ['#CareerAdvice', '#WorkplaceRecognition', '#CapabilityFormation'],
 17: ['#AIAtWork', '#CareerAdvice', '#CapabilityFormation'],
 18: ['#CareerDecisions',
      '#IndividualContributor',
      '#CapabilityFormation'],
 19: ['#Consulting', '#CareerDecisions', '#CapabilityFormation'],
 20: ['#CareerBreak', '#ReturnToWork', '#CapabilityFormation'],
 21: ['#CareerChange', '#ChangingIndustries', '#CapabilityFormation'],
}

EX = {
 4: ("The 3-line readiness case",
     ["Choose ONE role you have never held and are actually considering.",
      "Line one, Problem. Write what this role needs someone to solve, with "
      "the title removed.",
      "Line two, Proof. Write what you have already done that shows the "
      "underlying judgment. A decision, a constraint, what you did, what "
      "happened.",
      "Line three, Gap. Write what you genuinely need to learn, earn or "
      "experience in this context.",
      "Read the three back. If the proof is thin, name the evidence you "
      "still need. If the gap is a hard gate, name what must change first."],
     ["A readiness case does not guarantee that an employer will choose "
      "you.",
      "Credentials, markets, relationships, compensation, employer "
      "preferences and bias still matter."]),
 5: ("The 4-line move case",
     ["Choose ONE move you are considering.",
      "Carry. Remove the employer name, the old title and the industry "
      "language, then write which parts of your experience would still help "
      "solve the destination problem.",
      "Translate. Write the same capability in the destination's terms. What "
      "you had to notice, what decision you supported, what changed.",
      "Relearn. Name the genuine gap accurately. Systems, regulation, domain "
      "language, relationships, credentials.",
      "Prove. Write one example that supports the level you are claiming, "
      "not the duration or the title."],
     ["A career-track change can lower your leverage in some areas.",
      "Do not rename a real domain or credential requirement as a "
      "transferable skill."]),
 6: ("Work, Judgment, Evidence, and the 12-month question",
     ["Take the role you are considering, or the one you are in.",
      "Work. Describe an ordinary Monday in the new role. What problems "
      "would you own that you do not own today?",
      "Judgment. Write where you would have to make a call when the "
      "instructions are incomplete, and which tradeoffs would belong to "
      "you.",
      "Evidence. Write what you could name a year later to somebody with no "
      "history with you, without internal acronyms.",
      "Then answer the 12-month question in one sentence.",
      "If one area is weak, write what would have to be redesigned before "
      "you accept."],
     ["A role does not have to maximize growth to be a good decision.",
      "This exercise does not tell you whether to take the role. It tells "
      "you what you would be taking it for."]),
 7: ("Run CAR on one responsibility",
     ["Choose ONE responsibility you added in the last six months.",
      "Complexity. Write what variables are new. If the only answer is more "
      "of the same, write capacity use.",
      "Authority. Write which decisions now belong to you and what you can "
      "change when the plan is not working.",
      "Return. Write what came back in capability, evidence, or "
      "recognition.",
      "Then write the sentence you will use before the next request, "
      "including when the additional scope will be reviewed."],
     ["CAR is not a score. You are looking for a pattern.",
      "Some of the best growth opportunities begin outside the job "
      "description. The question is what the extra work is building."]),
 8: ("The four-sentence impact account",
     ["Choose ONE thing people now take for granted because it works.",
      "Before. What could people not do consistently? What decision had no "
      "shared rule?",
      "My Part. What did you personally own, recommend or lead? Name "
      "attribution accurately.",
      "Judgment. What was not obvious at the start? What options existed and "
      "what made the choice difficult?",
      "Proof. Mark your evidence as Existence, Use or Effect, and keep only "
      "what it supports.",
      "Remove the employer name and internal acronyms. Can a stranger still "
      "understand the contribution?"],
     ["Keep only information you are permitted to retain.",
      "Do not jump from existence to effect because effect sounds more "
      "impressive."]),
 9: ("Read one destination role",
     ["Choose ONE destination role. Not an industry.",
      "Capability. Write the problem the role needs handled, then one "
      "example from your history with the judgment and the result.",
      "Context. List the unfamiliar elements: customer, operating model, "
      "approval routes, stakeholders, tools, relationships, consequences of "
      "error.",
      "Credentials. Write three headings: confirmed requirement, preferred "
      "qualification, still unclear.",
      "Then make one move that reduces uncertainty, and write what it "
      "answered."],
     ["A closed requirement is not argued open with better wording.",
      "A relationship can help you learn the context. It is not proof that "
      "you already know it."]),
 10: ("One evidence entry",
      ["Choose ONE piece of work you are permitted to describe.",
       "Capture. What was the problem, what was your role, what judgment did "
       "you contribute, what result are you allowed to describe?",
       "Qualify. Label the result confirmed, qualified, or not yet "
       "verified.",
       "Preserve attribution and the time window.",
       "Retrieve. Name the entry after the problem, add the period and a few "
       "plain-language tags, and write one short explanation.",
       "Check the boundary before you keep anything: is this information you "
       "are permitted to retain?"],
      ["This is your own account, not your employer's files.",
       "If you are unsure what you can keep or disclose, leave it out and "
       "get appropriate guidance."]),
 11: ("Map one recurring output",
      ["Choose ONE recurring output from your job. Not your whole "
       "profession.",
       "Produce. What can an approved tool help make?",
       "Interpret. What does the output actually establish, and what does it "
       "not?",
       "Decide. What decision does it inform, and who owns that decision?",
       "Put a verification question under each column.",
       "Then mark honestly what you already do, what you could learn, and "
       "what belongs to another qualified role."],
      ["None of this guarantees that a job will remain.",
       "Use approved tools and permitted data. Do not paste restricted "
       "company information into an unapproved system."]),
 12: ("Four private lines",
      ["Write these privately. Nobody else needs to read them.",
       "What must hold for now? Finish the sentence: for now, any change "
       "needs to protect...",
       "What part of the current situation can I influence safely? Describe "
       "one recurring cost concretely.",
       "What one question would make the next option clearer?",
       "When will I review this again? Use a date or a real condition.",
       "If capacity is very limited, keep only the first line and the review "
       "point."],
      ["If health, safety, harassment or discrimination is involved, "
       "appropriate support comes first.",
       "This exercise cannot interpret an employment agreement, benefits, "
       "immigration rules or a health decision."]),
 13: ("The 30-day test",
      ["Choose ONE destination specific enough to investigate.",
       "Write the hypothesis: this option may fit because it uses this "
       "evidence, builds this missing experience, and meets these "
       "constraints.",
       "Write what would change your mind.",
       "Days 1 to 7. Map what the role needs, what you can evidence, what "
       "context is new, and what needs verifying. Keep the two questions "
       "that matter most.",
       "Days 8 to 14. Ask people who know the work about the work, not about "
       "your potential.",
       "Days 15 to 21. Try one bounded piece using permitted material, with "
       "a time limit set before you start.",
       "Days 22 to 30. Read the record and choose continue, modify or stop. "
       "Write why."],
      ["Do not confuse effort with evidence.",
       "If the month ends without enough evidence, call the result "
       "inconclusive."]),
 14: ('Audit one destination role',
      ['Choose ONE role you are actually considering. Not an industry.',
       'List every requirement in the posting that looks familiar.',
       'For each one, answer two questions. What would I actually have '
       'to decide? What happens if I decide badly?',
       'Sort each answer into one of four buckets: TRAVELS, LOOKS '
       'SIMILAR, MUST BE LEARNED, MUST BE EXPERIENCED.',
       'Look at the TRAVELS column and write the evidence you already '
       'have for each item.',
       'Look at the MUST BE LEARNED column and pick the one item you '
       'would start this month.',
       'Look at the MUST BE EXPERIENCED column and write honestly what '
       'access or practice it would require.'],
      ['A posting is a recruiting document, not a description of the '
       'work.',
       'Similar wording does not make two roles interchangeable.',
       'This exercise cannot tell you whether you would be hired.']),
 15: ('Name one gap and the step that matches',
      ['Write down one recent moment when the work got harder. A '
       'question you could not answer well, a decision you were not '
       'ready to own, or a capability you could not demonstrate.',
       'Ask: do I need to learn this?',
       'Ask: have I ever genuinely practiced this, as the person who '
       'had to decide?',
       'Ask: can I prove that I already have?',
       'Choose the ONE answer that fits and write the matching next '
       'step. Learn, practice, or prove.',
       'Write one sentence describing what you will do in the next two '
       'weeks.'],
      ['This is a reflection tool, not a diagnostic. It assigns no '
       'score, level or type.',
       'You may have none of these gaps, or more than one.',
       'Some gaps require access or authority you cannot award '
       'yourself.']),
 16: ('Build a contribution record',
      ['Choose three pieces of consequential work from the last year.',
       'For each, write four lines. What was true before. What you '
       'decided. What changed. What evidence supports the account.',
       'Read each one back and ask whether a person outside your team '
       'could understand it without you explaining.',
       'Pick the conversations where scope actually gets allocated and '
       'decide where each line belongs.',
       'Then answer the harder question in writing: does the '
       'decision-maker not know, or do they know and not act?'],
      ['A clearer record does not override bias, create a role, or move '
       'a budget you do not control.',
       'It removes the obstacle that is yours, so what remains is '
       'easier to see.']),
 17: ('Four lines for one piece of AI-assisted work',
      ['Choose one piece of work from this week where a tool did most '
       'of the visible production.',
       'Line one: what were you actually asked to get right, not what '
       'were you asked to produce.',
       'Line two: what did you check, and why did you check that. Write '
       'the reason, not just the check.',
       'Line three: what did you conclude that the initial output did '
       'not establish.',
       'Line four: what were you accountable for if the result was '
       'wrong.',
       'Put the record where your work already gets discussed, not in a '
       'file you will not open again.'],
      ['This does not make a job safe. Roles are redesigned and removed '
       "for reasons unrelated to any individual's contribution.",
       'It is also not a claim about what these tools can or cannot '
       'do.']),
 18: ('A decision record for the offer',
      ['Write what work you want more of, using last month as evidence '
       'rather than a general sense of yourself.',
       'Ask two managers at the level you are considering what their '
       'last ordinary week actually contained.',
       'Ask what senior individual work looks like here, and ask for '
       'names.',
       'List what you could decide without asking, then list what you '
       'would be answerable for. Compare the lengths.',
       'Find out whether anyone has moved into management here and back '
       'out without penalty.',
       'Write the one thing you still do not know, and who could answer '
       'it this week.'],
      ['Some organizations genuinely cap individual contributors.',
       'Neither path is the braver choice.']),
 19: ('One service, written as a proposal',
      ["Name the problem in the buyer's words, not yours.",
       'Name the buyer specifically enough that you could list three '
       'real organizations.',
       'Write the deliverable as something a person receives, with a '
       'beginning and an end.',
       'Write the scope, including what is not included.',
       'Write the conditions that would have to be true before this is '
       'viable.',
       'Read your employment agreement before any outreach, and get '
       'qualified advice on anything unclear.'],
      ['This is not legal or tax advice.',
       'Nothing here promises revenue, clients or a timeline.']),
 20: ('The two-part return record',
      ['Sort what you carry into three buckets: still current, needs '
       'updating, needs rebuilding.',
       'Inside those, mark what stayed current, what decayed, what '
       'changed in the field, what changed in your circumstances, what '
       'is unproven rather than absent, and what genuinely has to be '
       'rebuilt.',
       'For every item in still current, write the evidence a person '
       'could actually inspect.',
       'For every unproven item, write one way you could create a '
       'current instance.',
       'Choose ONE thing you are rebuilding and put a start date and a '
       'target date on it.',
       'Write the short, honest sentence about the break. Once. Then '
       'stop working on it.'],
      ['Bias against career breaks exists and framing does not remove '
       'it.',
       'A different title, scope or compensation on return is a '
       'tradeoff to evaluate, not a measurement of your worth.']),
 21: ('A five-layer relearning inventory',
      ['Choose ONE destination role. Not an entire industry.',
       "Make five headings, in the script's own words: what the work is "
       'actually about here, regulation and credentials, systems and '
       'tooling, relationships and internal history, and how decisions '
       'actually get made.',
       'Under each, write what you actually need to understand here, '
       'and how you could realistically learn it.',
       'Mark each item as something you can read, or something that '
       'needs exposure and practice.',
       'Confirm the binding requirements from the body or employer that '
       'actually sets them.',
       'Reorder the whole list by one question: what stops me '
       'contributing usefully first?',
       'Start the top item this week. The item, not the plan for it.'],
      ['A licensing requirement is not a mindset issue.',
       'Some layers only develop through practice in the environment, '
       'and that is normal rather than evidence of a wrong move.']),
}
