# -*- coding: utf-8 -*-
"""Six dedicated 9:16 Shorts per video for Videos 8 to 13.

Four Priority A and two optional Priority B, as the brief specifies. These are
full word-for-word vertical takes, not timestamps and not candidate
descriptions.

The earlier Attachment B Shorts were read as drafts and evaluated against the
new locked masters. Strong standalone ideas were preserved. Every opening line,
example, framework wording, title reference and qualification was checked
against the new script, and anything the new master no longer supports was
rewritten. A Short does not have to begin with the same sentence as the
long-form video.

Duration is an estimate from the word count until the take is recorded.
"""

SPM = 165.0


def seconds(s):
    return sum(len(p.split()) for p in s["script"]) / SPM * 60.0


def words(s):
    return sum(len(p.split()) for p in s["script"])


S = {}

S[8] = [
 dict(n=1, pr="A", slug="V8_Short_01_Now_It_Looks_Easy",
      title="Now It Looks Easy", onscreen="NOW IT LOOKS EASY",
      source="HOOK | When your hardest work becomes invisible",
      hook="You built it from scratch. Now everybody uses it.",
      script=[
        "You built it from scratch. Now everybody uses it.",
        "And that is exactly why your contribution can become harder to see.",
        "In your next review or interview you say, I built the process. But "
        "the process already exists now. It looks obvious. Maybe even easy.",
        "What disappeared from the story is everything you had to work out "
        "before it could become normal.",
        "So put it back. Not by making the work sound dramatic.",
        "Show three things: what was missing before, what judgment you had to "
        "use, and what the evidence actually supports.",
        "You do not need to make your work sound harder than it was. You need "
        "to stop leaving out the part that made the finished thing possible."],
      ending="You need to stop leaving out the part that made the finished "
             "thing possible.",
      visual="Open on camera. Full-screen NOW IT LOOKS EASY on the first line, "
             "camera hidden. Back to her for the three things. One short "
             "callout on the closing line.",
      sound="One quiet accent as the full-screen line lands. Nothing else.",
      note="Carries the new opening verbatim. The earlier draft Short opened "
           "on the way we work, which the locked master no longer says."),

 dict(n=2, pr="A", slug="V8_Short_02_Existence_Use_Effect",
      title="Existence, Use, Effect", onscreen="THEY ARE NOT INTERCHANGEABLE",
      source="3 | Keep the proof",
      hook="For foundational work, separate three levels of evidence.",
      script=[
        "For foundational work, separate three levels of evidence.",
        "Existence. Use. Effect.",
        "They are not interchangeable.",
        "Existence means the process, framework, or function was created.",
        "Use means people actually used it.",
        "Effect means you have evidence that something important changed.",
        "A process can exist without being used. It can be used without "
        "producing the outcome you hoped for. And an outcome can have several "
        "causes.",
        "So do not jump from the first level to the third because the third "
        "sounds better.",
        "Choose the strongest level your evidence actually supports."],
      ending="Choose the strongest level your evidence actually supports.",
      visual="Hook on camera. Full-screen three-part reveal on existence, use "
             "and effect, camera hidden. Back to her for the closing line.",
      sound="One restrained click per level at most, or none.",
      note="The distinction the brief names as important. Adoption is not "
           "measured effect and this Short keeps that separation."),

 dict(n=3, pr="A", slug="V8_Short_03_Four_Sentences",
      title="The Four-Sentence Account", onscreen="FOUR SENTENCES",
      source="ASSEMBLE | Four sentences",
      hook="Here is how to explain something you built, in four sentences.",
      script=[
        "Here is how to explain something you built, in four sentences.",
        "Before this work, this was missing.",
        "My part was this.",
        "The judgment involved this.",
        "What changed was this, and this is how I know.",
        "That last clause is the one people skip, and it is the one that makes "
        "the rest believable.",
        "Then remove the employer name and the internal acronyms and ask "
        "whether a stranger can still tell what the starting problem was, what "
        "you contributed, and what your evidence supports.",
        "If they can, you have an account of your contribution."],
      ending="If they can, you have an account of your contribution.",
      visual="Full-screen four-line build, one line at a time, camera hidden. "
             "Back to her for the stranger test.",
      sound="One accent as the four lines complete.",
      note="Uses the master's exact four-sentence stem."),

 dict(n=4, pr="A", slug="V8_Short_04_Reconstruct_The_Before",
      title="It Was Chaos Is Not a Before", onscreen="RECONSTRUCT THE BEFORE",
      source="1 | Reconstruct the before",
      hook="If you want people to understand what you built, start before it "
           "existed.",
      script=[
        "If you want people to understand what you built, start before it "
        "existed.",
        "Ask what people could not do consistently. What decision had no "
        "shared rule.",
        "Imagine you built an intake process for a team. This is an "
        "illustration, not a real case.",
        "The weak version is: it was chaos.",
        "The more useful version is: there was no shared way to prioritize "
        "requests or decide when they needed escalation.",
        "That tells the listener what problem the process was supposed to "
        "solve.",
        "And be careful. Nothing existed before me is often too broad. Your "
        "contribution may have been connecting work that was already "
        "happening informally.",
        "Also, do not turn the before into a number you never measured."],
      ending="Do not turn the before into a number you never measured.",
      visual="Hook on camera. Full-screen weak-versus-useful comparison with "
             "the ILLUSTRATION label visible, camera hidden. Back to her for "
             "the two warnings.",
      sound="One soft click as the useful version arrives.",
      note="The intake process must stay labelled as an illustration in the "
           "Short exactly as it is in the long form."),

 dict(n=5, pr="B", slug="V8_Short_05_Show_The_Judgment",
      title="Show the Judgment", onscreen="WHAT DID YOU WORK OUT?",
      source="2 | Show the judgment",
      hook="Creating a form is a task. Deciding what the form is allowed to "
           "accept is judgment.",
      script=[
        "Creating a form is a task. Deciding what the form is allowed to "
        "accept is judgment.",
        "That second part disappears inside the finished thing, so name it.",
        "Ask four questions.",
        "What was not obvious at the start?",
        "What options existed?",
        "What did I recommend, decide, or bring into agreement?",
        "Which constraint made that choice difficult?",
        "And keep attribution accurate. If someone else held the decision, say "
        "you developed the options or made the recommendation. If the team "
        "designed it, name the part you led.",
        "The point is not to turn routine work into a rescue story."],
      ending="The point is not to turn routine work into a rescue story.",
      visual="Full-screen four-question build, camera hidden. Back to her for "
             "attribution and the closing line.",
      sound="One accent when the four questions complete.",
      note="Attribution accuracy is a hard boundary in the master and is kept "
           "in the Short."),

 dict(n=6, pr="B", slug="V8_Short_06_Where_The_Evidence_Ends",
      title="Where the Evidence Ends", onscreen="SAY WHERE IT ENDS",
      source="ASSEMBLE | Four sentences",
      hook="The sentence people are most afraid to say is usually the one "
           "that makes them credible.",
      script=[
        "The sentence people are most afraid to say is usually the one that "
        "makes them credible.",
        "Here is an example account, using an illustration rather than a real "
        "case.",
        "The process was adopted by the participating teams. Its effect on "
        "turnaround time had not yet been established.",
        "That last sentence does not weaken the story.",
        "It tells the listener exactly where the evidence ends.",
        "Compare it to claiming an improvement you never measured. One "
        "survives the next question. The other does not.",
        "And proof does not mean taking your employer's files. Keep your own "
        "account and information you are permitted to retain."],
      ending="Keep your own account and information you are permitted to "
             "retain.",
      visual="Hook on camera. Full-screen quotation with the ILLUSTRATION "
             "label, camera hidden. Back to her for the comparison and the "
             "permitted-material line.",
      sound="None, or one flat accent. Do not make this triumphant.",
      note="Keeps the permitted-material boundary and the illustration label."),
]

S[9] = [
 dict(n=1, pr="A", slug="V9_Short_01_Direct_Industry_Experience",
      title="Direct Industry Experience Required",
      onscreen="NEW FIELD. NOT ZERO.",
      source="HOOK | New field does not mean zero",
      hook="You can be very experienced and still read one sentence in a job "
           "description that makes you feel like a beginner again.",
      script=[
        "You can be very experienced and still read one sentence in a job "
        "description that makes you feel like a beginner again.",
        "Direct industry experience required.",
        "You know you have done difficult work. You know you are not starting "
        "your career over.",
        "But a new industry may not count your experience exactly the way your "
        "current one does.",
        "So do not make either mistake.",
        "Do not say, I can already do all of this.",
        "And do not say, none of my experience counts here.",
        "Separate three things instead. Capability. Context. Credentials.",
        "What can you already prove? What changes in this setting? And what do "
        "you genuinely need before the door is open?"],
      ending="What do you genuinely need before the door is open?",
      visual="Open on camera. Full-screen quotation of the job-description "
             "line, camera hidden. Full-screen three-word framework on the "
             "separation. Back to her for the three questions.",
      sound="One soft impact on the quotation.",
      note="Uses the new title's framing. The earlier draft referenced the "
           "superseded title Before You Change Industries, Know What Still "
           "Counts, which is removed."),

 dict(n=2, pr="A", slug="V9_Short_02_Same_Verb_Different_Work",
      title="The Same Verb Is Not the Same Work",
      onscreen="SAME VERB. DIFFERENT WORK.",
      source="1 | Capability: What underlying work can you prove?",
      hook="Do not declare your experience equivalent just because two roles "
           "use the same verb.",
      script=[
        "Do not declare your experience equivalent just because two roles use "
        "the same verb.",
        "Take approve. This is a constructed comparison, not a real employer's "
        "rules.",
        "In one role, approve can mean checking a routine item.",
        "In another, it can mean accepting a consequential risk.",
        "Same word. Very different work.",
        "So compare the scale of the decision, the consequences of being "
        "wrong, and the support around it.",
        "Then write the capability sentence this way. This role needs someone "
        "to handle this problem. My evidence is this example.",
        "If you cannot finish both halves, you have a question to investigate, "
        "not yet a transfer claim."],
      ending="You have a question to investigate, not yet a transfer claim.",
      visual="Full-screen approve comparison with the ILLUSTRATION label, "
             "camera hidden. Back to her for the capability sentence.",
      sound="One accent as the second meaning arrives.",
      note="The constructed comparison stays labelled. No employer "
           "requirements are fabricated."),

 dict(n=3, pr="A", slug="V9_Short_03_Confirmed_Preferred_Unclear",
      title="Is It a Gate or a Preference?", onscreen="WHAT IS ACTUALLY A GATE?",
      source="3 | Credentials: What is actually a gate?",
      hook="Before you buy another qualification, find out whether it is "
           "actually a gate.",
      script=[
        "Before you buy another qualification, find out whether it is actually "
        "a gate.",
        "A credential can be an employer screen, a professional requirement, "
        "or evidence of preparation. Which one is it here?",
        "Check the original posting, the employer's explanation, and the "
        "appropriate authoritative source when a regulated qualification is "
        "involved.",
        "Then write down three things.",
        "Confirmed requirement. Preferred qualification. Still unclear.",
        "Do not assume a course substitutes for a license. Do not assume a "
        "certificate overrides an explicit experience requirement.",
        "But also do not collect three new qualifications because one "
        "unfamiliar acronym appeared in a job description.",
        "And if a genuine gate is closed, that is useful information. You do "
        "not argue a closed requirement open with better wording."],
      ending="You do not argue a closed requirement open with better wording.",
      visual="Hook on camera. Full-screen three-label build, camera hidden. "
             "Back to her for the two warnings and the closing line.",
      sound="One flat accent as the three labels complete.",
      note="No credential mandate, regulatory rule or eligibility claim is "
           "invented."),

 dict(n=4, pr="A", slug="V9_Short_04_Ask_About_The_Work",
      title="Ask a Better Question", onscreen="ASK ABOUT THE WORK",
      source="2 | Context: What changes when the setting changes?",
      hook="Stop asking people whether you could switch industries.",
      script=[
        "Stop asking people whether you could switch industries.",
        "That question invites an opinion about you.",
        "Ask about the work instead.",
        "Where do otherwise experienced people tend to need the most support "
        "when they first enter this role?",
        "Then ask for an example of a decision that would be unfamiliar.",
        "You are trying to discover the work behind the hiring language.",
        "Because context is not just vocabulary you can learn over a weekend. "
        "It can change which answer is responsible.",
        "You may know how to bring a difficult decision together and still not "
        "know how this organization decides something is ready, or who has "
        "authority to approve a change.",
        "Naming that gap does not cancel your capability."],
      ending="Naming that gap does not cancel your capability.",
      visual="Camera for the reframe. Full-screen callout on the better "
             "question, camera hidden. Back to her for the context "
             "explanation.",
      sound="One quiet accent on the better question.",
      note="Keeps the script's point that a relationship helps you learn "
           "context but does not prove you already know it."),

 dict(n=5, pr="B", slug="V9_Short_05_A_Defensible_Introduction",
      title="A Defensible Introduction", onscreen="THREE PARTS",
      source="PUT IT TOGETHER | A defensible introduction",
      hook="Here is what a careful introduction into a new industry sounds "
           "like.",
      script=[
        "Here is what a careful introduction into a new industry sounds like.",
        "I have evidence of coordinating complex delivery decisions across "
        "teams.",
        "I would need to learn this organization's approval routes and "
        "operating risks.",
        "Before proceeding, I want to confirm which direct experience and "
        "qualifications are essential for this role.",
        "That is not a script to memorize. It shows the shape of the decision.",
        "Relevant evidence. Named learning. Verified requirements.",
        "It does not pretend everything transfers, and it does not pretend "
        "nothing does.",
        "A good explanation cannot erase bias, a weak market, a closed hiring "
        "rule, or a real experience gap. Its job is narrower."],
      ending="Its job is narrower.",
      visual="Full-screen three-part shape on the summary line, camera hidden. "
             "Back to her for the limits.",
      sound="One accent as the three parts complete.",
      note="The limits sentence is kept verbatim from the master."),

 dict(n=6, pr="B", slug="V9_Short_06_What_Are_You_Giving_Up",
      title="What Are You Giving Up?", onscreen="INVESTIGATE THE TRADEOFF",
      source="PUT IT TOGETHER | A defensible introduction",
      hook="A new industry may value some of your experience without "
           "preserving all of your current scope, pay, authority, or status.",
      script=[
        "A new industry may value some of your experience without preserving "
        "all of your current scope, pay, authority, or status.",
        "That is not a universal rule. It is something to investigate before "
        "you commit.",
        "So ask four questions.",
        "What are you gaining?",
        "What are you giving up?",
        "For how long?",
        "And what evidence supports the opportunity rather than just the hope?",
        "That last one matters most, because hope is easy to collect and "
        "evidence is not.",
        "Being new to an industry is not the same as being new to every "
        "problem inside it."],
      ending="Being new to an industry is not the same as being new to every "
             "problem inside it.",
      visual="Hook on camera. Full-screen four-question build, camera hidden. "
             "Back to her for the closing line, which is the long-form closing "
             "line.",
      sound="One accent when the questions complete.",
      note="No promise of preserved pay, title, authority or seniority."),
]

S[10] = [
 dict(n=1, pr="A", slug="V10_Short_01_Access_Not_Experience",
      title="Your Access Disappears First", onscreen="BEFORE ACCESS ENDS",
      source="HOOK | The proof can disappear before the experience does",
      hook="Imagine the job ends tomorrow. Your access is gone.",
      script=[
        "Imagine the job ends tomorrow. Your access is gone.",
        "Then someone asks what you actually accomplished there.",
        "You remember the projects. You remember the pressure.",
        "But the dashboard is inside a system you cannot open anymore. The "
        "decision trail lived in meetings you no longer attend.",
        "Your experience did not disappear. Your access to the evidence did.",
        "That is why you should know what you can still prove before you "
        "urgently need to explain it.",
        "This is not a video about predicting a layoff, and it is not a reason "
        "to take company files.",
        "It is a habit. Capture the contribution. Qualify the claim. Make it "
        "retrievable."],
      ending="Capture the contribution. Qualify the claim. Make it "
             "retrievable.",
      visual="Open on camera. Full-screen on your experience did not "
             "disappear, camera hidden. Full-screen three-part habit at the "
             "end.",
      sound="One soft impact on the access line.",
      note="The not-a-prediction and not-a-reason-to-take-files boundaries "
           "stay in the Short."),

 dict(n=2, pr="A", slug="V10_Short_02_Preparation_Is_Not_Extraction",
      title="Preparation Is Not Extraction",
      onscreen="PREPARATION IS NOT EXTRACTION",
      source="THE BOUNDARY | Preparation is not extraction",
      hook="Before you build any record of your work, one boundary.",
      script=[
        "Before you build any record of your work, one boundary.",
        "Access to a document does not mean you are entitled to keep it.",
        "Removing a company name does not automatically make restricted "
        "material yours to retain.",
        "No forwarding internal emails. No downloading dashboards. No copying "
        "customer information. No collecting employee records.",
        "This exercise is about your own high-level account and information "
        "you are permitted to retain.",
        "If you are unsure what you can keep or disclose, leave it out and get "
        "appropriate guidance.",
        "A personal device is not a permission slip. The first question is "
        "whether the information belongs there at all.",
        "Keep an account of your contribution, not a copy of your employer's "
        "files."],
      ending="Keep an account of your contribution, not a copy of your "
             "employer's files.",
      visual="Full-screen boundary card, camera hidden. Never animate any of "
             "the prohibited actions. Back to her for the guidance line.",
      sound="None. This should not feel dramatic.",
      note="Closes on the long-form final spoken line. No legal, severance or "
           "access-rights advice is added."),

 dict(n=3, pr="A", slug="V10_Short_03_Calendar_Versus_Contribution",
      title="A Calendar Entry Is Not a Contribution",
      onscreen="NOT THE CALENDAR",
      source="1 | Capture the contribution, not the calendar",
      hook="Attended weekly implementation meetings is a calendar entry.",
      script=[
        "Attended weekly implementation meetings is a calendar entry.",
        "It tells me where you spent time, not what you contributed.",
        "Here is an illustration. Suppose what you actually did was notice "
        "that two teams were using different definitions of completion, "
        "explain why that mattered, and help them agree on a common readiness "
        "check.",
        "Now the useful record begins.",
        "I identified conflicting completion criteria and helped the teams "
        "agree what needed to be true before handoff.",
        "Notice what that does not claim. It does not automatically claim that "
        "delays fell.",
        "The result comes next, if you have it.",
        "You are not trying to reconstruct the whole company. You are "
        "preserving the part that lets someone assess your contribution "
        "accurately."],
      ending="You are preserving the part that lets someone assess your "
             "contribution accurately.",
      visual="Full-screen calendar-versus-contribution comparison with the "
             "ILLUSTRATION label, camera hidden.",
      sound="One soft click as the contribution arrives.",
      note="Hypothetical stays labelled. No improvement figure is added."),

 dict(n=4, pr="A", slug="V10_Short_04_Confirmed_Qualified_Not_Verified",
      title="Confirmed, Qualified, Not Yet Verified",
      onscreen="QUALIFY THE CLAIM",
      source="2 | Qualify the claim",
      hook="Put one of three labels beside every result you record.",
      script=[
        "Put one of three labels beside every result you record.",
        "Confirmed. Qualified. Not yet verified.",
        "Confirmed means you have a permitted basis for the statement you are "
        "making.",
        "Qualified means the result needs its scope attached.",
        "Not yet verified means you should not present it as established.",
        "These are simple labels for your own record. Their job is to stop "
        "uncertainty disappearing when you shorten the story later.",
        "And preserve attribution. We delivered the integration and I owned "
        "the risk analysis that informed the sequence can both be true. "
        "Turning that into I delivered everything changes the claim.",
        "This is not timid language. It is language that survives the next "
        "question."],
      ending="It is language that survives the next question.",
      visual="Full-screen three-label build, camera hidden. Back to her for "
             "attribution. One short callout on the closing line.",
      sound="One flat accent per label at most, or one on the closing line.",
      note="Keeps the time-window and attribution qualifications."),

 dict(n=5, pr="B", slug="V10_Short_05_Name_It_By_The_Problem",
      title="Name It by the Problem", onscreen="MAKE IT RETRIEVABLE",
      source="3 | Make it retrievable",
      hook="A good record is useless if you cannot find it when the question "
           "changes.",
      script=[
        "A good record is useless if you cannot find it when the question "
        "changes.",
        "So name each entry by the problem or the contribution, not by the "
        "project code.",
        "Conflicting handoff criteria is more useful than Project Alpha, "
        "especially to somebody outside the company.",
        "Add the period, a few plain-language tags, and the qualification you "
        "need to preserve.",
        "Decision under uncertainty. Cross-team coordination. New operating "
        "context.",
        "Then write one short explanation in ordinary language. Not a polished "
        "resume bullet for every possible future job.",
        "Source material you can adapt without losing the truth."],
      ending="Source material you can adapt without losing the truth.",
      visual="Full-screen naming comparison, camera hidden. Back to her for "
             "the tags.",
      sound="One accent as the better name arrives.",
      note="Uses the master's own tag examples."),

 dict(n=6, pr="B", slug="V10_Short_06_Two_Reasons_Evidence_Is_Thin",
      title="Two Reasons the Evidence Is Thin",
      onscreen="TWO DIFFERENT PROBLEMS",
      source="WHEN THE EVIDENCE IS THIN",
      hook="There are two very different reasons an example may be missing.",
      script=[
        "There are two very different reasons an example may be missing.",
        "You may have done the work and failed to capture it clearly.",
        "Or you may never have had the opportunity to own the decision, access "
        "the result, or build that part of your range.",
        "Do not solve both problems by writing a stronger sentence.",
        "The first needs reconstruction.",
        "The second needs an honest account of the experience you do and do "
        "not have.",
        "If a result was never shared with you, say what you can support about "
        "your contribution. Do not fill the gap with what probably happened.",
        "And if a layoff has already happened, do not hear this as you missed "
        "your chance."],
      ending="Do not hear this as you missed your chance.",
      visual="Full-screen two-problem comparison, camera hidden. Back to her "
             "for the closing reassurance.",
      sound="One flat accent. Nothing triumphant.",
      note="Keeps the already-laid-off passage, which matters for tone."),
]

S[11] = [
 dict(n=1, pr="A", slug="V11_Short_01_Can_We_Reduce_The_Team",
      title="Does This Mean We Can Reduce the Team?",
      onscreen="THE TASK ISN'T THE JOB",
      source="HOOK | If AI can produce the output, what still belongs to you?",
      hook="The report is ready. AI helped produce it.",
      script=[
        "The report is ready. AI helped produce it.",
        "Then your manager asks: does this mean we can reduce the team?",
        "That is the moment the job changes.",
        "Because if part of your value has been producing the report, a tool "
        "that can produce it faster can feel like it is coming directly for "
        "your role.",
        "But the next question is not, can the tool make the report.",
        "It is, what still has to be interpreted, verified, and decided before "
        "anybody should act?",
        "A report is an output. Reducing a team is a decision.",
        "There is work between them, and there is accountability after them.",
        "A faster output is not the same thing as a finished decision."],
      ending="A faster output is not the same thing as a finished decision.",
      visual="Open on camera. Full-screen on the manager's question, camera "
             "hidden. Back to her. One short callout on the output-versus-"
             "decision line.",
      sound="One soft impact on the question.",
      note="Closes on the long-form final spoken line. The thumbnail wording "
           "is the current THE TASK ISN'T THE JOB, not the superseded WHAT "
           "STILL NEEDS YOU?"),

 dict(n=2, pr="A", slug="V11_Short_02_The_Mix_Changed",
      title="The Number Improved. The Work Did Not.",
      onscreen="SYNTHETIC DATA",
      source="DEMONSTRATION | Faster output, unfinished decision",
      hook="Here is a small synthetic service report. These are invented "
           "teaching numbers, not customer data.",
      script=[
        "Here is a small synthetic service report. These are invented teaching "
        "numbers, not customer data.",
        "In the first period, sixty out of a hundred cases met the target. In "
        "the second, eighty out of a hundred did.",
        "Sixty percent to eighty percent. The headline looks better.",
        "Now separate routine cases from complex cases.",
        "Routine cases met the target ninety percent of the time in both "
        "periods. Complex cases met it forty percent of the time in both "
        "periods.",
        "What changed was the mix. The second period had far more routine "
        "cases and fewer complex ones.",
        "So the overall number improved even though the within-category rates "
        "did not.",
        "The AI-assisted summary prepared for this example identifies that "
        "distinction. This is not a story about AI missing things."],
      ending="This is not a story about AI missing things.",
      visual="Full-screen data frames with the SYNTHETIC DATA and PREPARED "
             "AI-ASSISTED EXAMPLE label visible throughout, camera hidden. Do "
             "not show a product interface.",
      sound="One restrained accent on the mix reveal only.",
      note="Every figure recomputed from the supplied CSV. A rise of twenty "
           "percentage points, not twenty percent relative growth. Do not "
           "stage an AI failure and do not claim a live benchmark."),

 dict(n=3, pr="A", slug="V11_Short_03_Produce_Interpret_Decide",
      title="Produce, Interpret, Decide", onscreen="PRODUCE INTERPRET DECIDE",
      source="HOOK and 1 to 3",
      hook="If a tool can produce your output, map what is left.",
      script=[
        "If a tool can produce your output, map what is left.",
        "Produce. Interpret. Decide. And verify across all three.",
        "Produce is the draft, the classification, the comparison, the report. "
        "Those are useful contributions. Do not minimize them to protect an "
        "old job description.",
        "Interpret asks what the output actually establishes, and what it does "
        "not.",
        "Decide asks who owns the consequence.",
        "Verification is not a little ceremony at the end. It runs through the "
        "work.",
        "Can you trace the numbers to the source? Are missing values "
        "identified? Are we looking at the right period and population?",
        "And use approved tools and permitted data. Do not paste restricted "
        "company information into an unapproved system."],
      ending="Do not paste restricted company information into an unapproved "
             "system.",
      visual="Full-screen framework build, camera hidden. Back to her for the "
             "verification questions.",
      sound="One accent as the framework completes.",
      note="Keeps the approved-tools boundary."),

 dict(n=4, pr="A", slug="V11_Short_04_Who_Owns_The_Consequence",
      title="Who Owns the Consequence?", onscreen="THAT IS A DECISION PROCESS",
      source="3 | Decide: Who owns the consequence?",
      hook="When someone asks whether a tool means you can cut the team, the "
           "answer is not another prettier report.",
      script=[
        "When someone asks whether a tool means you can cut the team, the "
        "answer is not another prettier report.",
        "It is a decision process.",
        "Who is authorized to make the change?",
        "Which risks must be accepted or reduced?",
        "What alternatives are available?",
        "What would trigger a review or reversal?",
        "Who will monitor what happens after the decision?",
        "Those are organizational responsibilities. A tool producing a "
        "recommendation does not automatically assign them to anyone.",
        "And do not take responsibility for decisions you cannot influence. If "
        "your role is being redesigned, authority, access, and support need to "
        "be part of that conversation too."],
      ending="Authority, access, and support need to be part of that "
             "conversation too.",
      visual="Full-screen five-question build, camera hidden. Back to her for "
             "the closing caution.",
      sound="One accent when the questions complete. Not one per question.",
      note="Does not claim job security. The master is explicit that none of "
           "this guarantees a role remains."),

 dict(n=5, pr="B", slug="V11_Short_05_Map_One_Output",
      title="Map One Recurring Output", onscreen="ONE OUTPUT. THREE COLUMNS.",
      source="MAP YOUR ROLE | Do not look for an AI-proof job",
      hook="Take one recurring output from your job. Not your whole "
           "profession.",
      script=[
        "Take one recurring output from your job. Not your whole profession.",
        "Make three columns. Produce. Interpret. Decide.",
        "Then put a verification question under each.",
        "What can an approved tool help produce?",
        "What must be established before anyone relies on it?",
        "What decision does it inform, and who owns that decision?",
        "Now put your own contribution on the map honestly. Separate what you "
        "already do from what you could learn and what belongs to another "
        "qualified role.",
        "You may find valuable work you have been doing without naming it. You "
        "may also find that a large part of the role really is easier to "
        "automate.",
        "Both of those are useful to know."],
      ending="Both of those are useful to know.",
      visual="Full-screen three-column map, camera hidden. Back to her for the "
             "honest-map line.",
      sound="One soft click per column at most.",
      note="Keeps the possibility that the role is automatable. Do not turn "
           "this into reassurance."),

 dict(n=6, pr="B", slug="V11_Short_06_No_AI_Proof_Job",
      title="Do Not Look for an AI-Proof Job",
      onscreen="NOT A HUMAN STAMP",
      source="MAP YOUR ROLE | Do not look for an AI-proof job",
      hook="None of this guarantees that a job will remain.",
      script=[
        "None of this guarantees that a job will remain.",
        "Employers can reduce roles, change scope, or choose a different "
        "operating model.",
        "So the goal is not to become the person who adds a human stamp to "
        "anything AI produces.",
        "It is to be clear about the judgment, evidence, authority, and "
        "consequences the work still requires.",
        "And if you currently only assemble the report, do not claim "
        "interpretive authority because a video gave you new language.",
        "Ask what experience, supervision, and access would let you build it.",
        "You do not have to deny that the technology is useful to explain "
        "where your contribution still matters."],
      ending="You do not have to deny that the technology is useful to explain "
             "where your contribution still matters.",
      visual="Camera-led. One short callout on the human-stamp line. One "
             "full-screen callout on the closing sentence.",
      sound="One quiet accent at most.",
      note="Deliberately unreassuring, matching the master. No job-security "
           "promise."),
]

S[12] = [
 dict(n=1, pr="A", slug="V12_Short_01_Constraint_Versus_Conclusion",
      title="A Constraint Is Not a Conclusion",
      onscreen="WHAT CAN CHANGE NOW?",
      source="HOOK | I cannot leave yet is not the same as nothing can change",
      hook="Just leave is easy advice when nobody has asked what your paycheck "
           "has to cover.",
      script=[
        "Just leave is easy advice when nobody has asked what your paycheck "
        "has to cover.",
        "Maybe you need the income. Maybe benefits matter. Maybe caregiving, "
        "immigration status, or the timing of your life makes a quick exit "
        "unrealistic.",
        "So start with a more accurate sentence.",
        "I cannot leave yet. That is a constraint.",
        "Nothing can change. That is a conclusion.",
        "They are not the same thing.",
        "You do not need a second full-time job called escaping the first one.",
        "You need to protect what must hold, put boundaries where you can, and "
        "prepare one possible next step."],
      ending="Protect what must hold, put boundaries where you can, and "
             "prepare one possible next step.",
      visual="Open on camera. Full-screen constraint-versus-conclusion "
             "comparison, camera hidden. Full-screen three-part framework at "
             "the end.",
      sound="One soft accent as the conclusion column arrives.",
      note="Uses the current thumbnail direction WHAT CAN CHANGE NOW?, not the "
           "superseded STUCK FOR NOW?"),

 dict(n=2, pr="A", slug="V12_Short_02_Protect_What_Must_Hold",
      title="Name the Constraint Precisely", onscreen="WHAT MUST HOLD?",
      source="1 | Protect what must hold",
      hook="I cannot leave is a conclusion. What is underneath it?",
      script=[
        "I cannot leave is a conclusion. What is underneath it?",
        "A dependable income right now? An arrangement you cannot interrupt? A "
        "family responsibility? Or not knowing what another role would "
        "actually offer?",
        "You do not have to justify the answer to strangers. This is a private "
        "planning exercise.",
        "Then separate what you know from what you have assumed.",
        "You may know you cannot manage a gap in income. You may not yet know "
        "whether a particular employer offers the flexibility you need.",
        "Those are different constraints.",
        "So write one sentence. For now, any change needs to protect, and then "
        "finish it with the constraint you actually have.",
        "That narrows the search. It also stops you spending scarce energy on "
        "options that would never work."],
      ending="It stops you spending scarce energy on options that would never "
             "work.",
      visual="Full-screen sentence stem, camera hidden. Back to her for the "
             "know-versus-assumed distinction.",
      sound="One soft accent on the stem.",
      note="Private exercise. Nothing asks the viewer to disclose the answer."),

 dict(n=3, pr="A", slug="V12_Short_03_Make_The_Tradeoff_Visible",
      title="Make the Tradeoff Visible", onscreen="BE SPECIFIC",
      source="2 | Bound what you can",
      hook="This job is impossible captures the feeling. It does not give "
           "anyone something to address.",
      script=[
        "This job is impossible captures the feeling. It does not give anyone "
        "something to address.",
        "Try this instead.",
        "These two commitments require the same time, and I need a priority "
        "decision.",
        "Or: I can carry A and B at the agreed level. With C added, what should "
        "change in priority, scope, support, or timing?",
        "That makes the tradeoff visible.",
        "It is not a guarantee of a reasonable response, and it is not advice "
        "to refuse work in a way that could put you at risk.",
        "Use the conversation only where it is safe and appropriate.",
        "And if the environment has repeatedly shown you there is no room to "
        "negotiate, stop building a plan that depends on one conversation "
        "changing everything. That is information too."],
      ending="That is information too.",
      visual="Full-screen feeling-versus-specific-ask comparison, camera "
             "hidden. Back to her for the safety caveat, which must not be "
             "cut.",
      sound="One soft click as the specific ask arrives.",
      note="The safety caveat is not optional. Negotiation is not presented as "
           "always safe or effective."),

 dict(n=4, pr="A", slug="V12_Short_04_The_Four_Lines",
      title="The Four-Line Private Plan", onscreen="FOUR LINES",
      source="THE PLAN | Four lines",
      hook="If leaving is not an option yet, put four lines on a page.",
      script=[
        "If leaving is not an option yet, put four lines on a page.",
        "What must hold for now?",
        "What part of the current situation can I influence safely?",
        "What one question would make the next option clearer?",
        "When will I review this again?",
        "That last line matters, because for now needs a way to be revisited. "
        "It does not need to be a resignation deadline. Use a date or a "
        "condition that is real for your situation.",
        "And if your capacity is extremely limited, choose only the first line "
        "and the review point.",
        "Protecting yourself and postponing a nonessential career project can "
        "be a deliberate choice."],
      ending="Protecting yourself and postponing a nonessential career project "
             "can be a deliberate choice.",
      visual="Full-screen four-line build, camera hidden. Back to her for the "
             "limited-capacity permission.",
      sound="One accent when the four lines complete.",
      note="The limited-capacity permission is kept. Rest is a legitimate "
           "response."),

 dict(n=5, pr="B", slug="V12_Short_05_A_Question_Not_An_Activity",
      title="Choose a Question, Not an Activity",
      onscreen="A QUESTION, NOT AN ACTIVITY",
      source="3 | Prepare one possible next step",
      hook="Choose a question before you choose an activity.",
      script=[
        "Choose a question before you choose an activity.",
        "I should be on LinkedIn more is an activity without a test.",
        "What would I need to prove to be considered for that role is a "
        "question.",
        "Preparation does not have to mean adding another course or another "
        "project.",
        "Sometimes the useful move is recovering one permitted example of work "
        "you already did.",
        "Sometimes it is clarifying one requirement in a role you are "
        "considering.",
        "And if there is room inside the current job, development might come "
        "from exchanging a repetitive responsibility for one that involves a "
        "new decision. Exchange, not automatically add. Ask what comes off the "
        "plate.",
        "A small step should answer a useful question or preserve an option."],
      ending="A small step should answer a useful question or preserve an "
             "option.",
      visual="Full-screen question-versus-activity comparison, camera hidden. "
             "Back to her for exchange, not add.",
      sound="One accent as the question arrives.",
      note="No side-hustle or constant-networking framing."),

 dict(n=6, pr="B", slug="V12_Short_06_What_This_Cannot_Do",
      title="What a Plan Cannot Do", onscreen="TWO UNHELPFUL EXTREMES",
      source="WHAT THIS DOES AND DOES NOT DO",
      hook="A plan like this can make a decision clearer. Here is what it "
           "cannot do.",
      script=[
        "A plan like this can make a decision clearer. Here is what it cannot "
        "do.",
        "It cannot create vacancies, eliminate bias, supply a missing "
        "credential, or make a difficult employer reasonable.",
        "And it does not mean every part of your experience will be useful "
        "somewhere else.",
        "The point is to avoid two unhelpful extremes.",
        "Pretending you have no constraints.",
        "Or treating the constraints as proof that no useful decision remains.",
        "Sometimes the next action is preparation. Sometimes it is support. "
        "Sometimes it is a boundary. Sometimes it is rest before anything else "
        "is realistic.",
        "You can respect your constraints without pretending the current "
        "situation is the whole story."],
      ending="You can respect your constraints without pretending the current "
             "situation is the whole story.",
      visual="Camera-led. One full-screen card on the two extremes, camera "
             "hidden. Back to her for the closing line.",
      sound="One flat accent at most.",
      note="Closes on the long-form final spoken line. Rest is kept as a "
           "legitimate response."),
]

S[13] = [
 dict(n=1, pr="A", slug="V13_Short_01_Stop_Collecting_Activity",
      title="Stop Collecting Career Activity",
      onscreen="TEST BEFORE YOU QUIT",
      source="HOOK | Stop collecting career activity",
      hook="You have saved the jobs. Rewritten the headline. Maybe started a "
           "course.",
      script=[
        "You have saved the jobs. Rewritten the headline. Maybe started a "
        "course.",
        "And you still do not know whether you actually want the work you are "
        "preparing for.",
        "That is the problem with career activity. It can make you feel "
        "productive without answering the decision.",
        "So before you make a high-cost commitment, choose one destination and "
        "test it for thirty days.",
        "Not to prove you can change careers in a month.",
        "To answer four questions. What is the work really asking for? What do "
        "I already have evidence for? What would I still need to learn? And "
        "does this option fit the life I actually have?",
        "Define. Investigate. Try. Decide.",
        "And the test only works if not this option is allowed to be a good "
        "result."],
      ending="The test only works if not this option is allowed to be a good "
             "result.",
      visual="Open on camera. Full-screen on the activity-versus-decision "
             "line, camera hidden. Full-screen four-phase framework at the "
             "end.",
      sound="One soft impact on the activity line.",
      note="A plan, not a completed experiment. No participant, offer or "
           "outcome is invented."),

 dict(n=2, pr="A", slug="V13_Short_02_One_Destination_One_Hypothesis",
      title="One Destination, One Hypothesis",
      onscreen="SPECIFIC ENOUGH TO TEST",
      source="SETUP | One destination, one hypothesis",
      hook="Choose a destination specific enough to test.",
      script=[
        "Choose a destination specific enough to test.",
        "Something strategic is too vague.",
        "An internal operations-improvement role that uses my cross-team "
        "problem solving and keeps predictable hours gives you something you "
        "can investigate. That is an illustration, not a real participant "
        "story.",
        "Then write one hypothesis.",
        "This option may fit because it uses this evidence, builds this "
        "missing experience, and meets these constraints.",
        "And write what would change your mind. A requirement you cannot meet. "
        "Work that is different from what you imagined. A schedule that does "
        "not fit.",
        "A useful test has permission to produce an inconvenient answer.",
        "Thirty days gives the investigation a boundary. It does not create "
        "time you do not have."],
      ending="Thirty days gives the investigation a boundary. It does not "
             "create time you do not have.",
      visual="Full-screen vague-versus-testable comparison with the "
             "ILLUSTRATION label, camera hidden. Back to her for the "
             "hypothesis.",
      sound="One soft click as the testable version arrives.",
      note="The schedule is adaptable. Do not borrow from essential rest or "
           "care to finish on an arbitrary day."),

 dict(n=3, pr="A", slug="V13_Short_03_Ask_About_The_Work",
      title="Ask About the Work, Not Your Potential",
      onscreen="ASK ABOUT THE WORK",
      source="DAYS 8-14 | Investigate with people who know the work",
      hook="Do not ask for blanket reassurance about your potential.",
      script=[
        "Do not ask for blanket reassurance about your potential.",
        "Ask about the work.",
        "What is a difficult ordinary week in this role?",
        "Where do people with an adjacent background tend to need support?",
        "Which decisions distinguish someone who is ready from someone who "
        "still needs supervision?",
        "Two thoughtful conversations may reveal a lot. But two is not a magic "
        "number, and nobody owes you access.",
        "If no one responds, do not record silence as proof that your whole "
        "career has been rejected. Mark the question unresolved and keep "
        "investigating through credible public information.",
        "And remember a pleasant conversation is not an offer, and not proof "
        "that you meet every requirement."],
      ending="A pleasant conversation is not an offer.",
      visual="Full-screen three-question build, camera hidden. Back to her for "
             "the no-response guidance.",
      sound="One accent when the questions complete.",
      note="Nobody owes access, and silence is not rejection. Both kept."),

 dict(n=4, pr="A", slug="V13_Short_04_Continue_Modify_Stop",
      title="Continue, Modify, or Stop", onscreen="DECIDE FROM THE EVIDENCE",
      source="DAYS 22-30 | Decide from the evidence",
      hook="At the end of the month, stop collecting activities and read the "
           "record.",
      script=[
        "At the end of the month, stop collecting activities and read the "
        "record.",
        "Does this option use experience you can support? What new context or "
        "capability would it build? Which requirements are confirmed? Does the "
        "route respect your constraints?",
        "Then choose one of three decisions.",
        "Continue does not mean resign tomorrow. It could mean a targeted "
        "conversation, an application, or a specific learning commitment now "
        "supported by evidence.",
        "Modify might mean an adjacent role, a different employer, a "
        "supervised entry point, or a longer preparation period.",
        "Stop means the investigation gave you a reason not to keep investing "
        "here right now. That is useful information.",
        "And if the month ends without enough evidence, call the result "
        "inconclusive.",
        "Do not turn uncertainty into a yes because you spent thirty days on "
        "it."],
      ending="Do not turn uncertainty into a yes because you spent thirty days "
             "on it.",
      visual="Full-screen three-decision build, camera hidden. The "
             "inconclusive line gets its own reveal.",
      sound="One flat accent per decision at most, or one on the closing "
            "line.",
      note="Inconclusive must stay available. No forced positive outcome."),

 dict(n=5, pr="B", slug="V13_Short_05_A_Work_Sample_Not_Experience",
      title="A Work Sample Is Not Experience",
      onscreen="A WORK SAMPLE, NOT EXPERIENCE",
      source="DAYS 15-21 | Try one bounded piece",
      hook="In the third week, test one important part of the destination.",
      script=[
        "In the third week, test one important part of the destination.",
        "Use public, synthetic, or otherwise permitted material.",
        "Do not recreate a confidential employer process, and do not turn the "
        "exercise into unpaid operational work for a prospective employer.",
        "For an operations-improvement illustration, use a fictional intake "
        "process and write a one-page recommendation. What is the problem? "
        "What alternatives are available? What tradeoff would you make? What "
        "would you need to verify before implementation?",
        "Set a time limit before you begin. The sample should answer a "
        "question, not become a consulting engagement.",
        "And label it honestly. A simulation can show a way of thinking. It "
        "cannot prove results with real customers, real stakes, or a team you "
        "have never led.",
        "It is a work sample, not professional experience."],
      ending="It is a work sample, not professional experience.",
      visual="Full-screen card carrying the A WORK SAMPLE, NOT PROFESSIONAL "
             "EXPERIENCE label, camera hidden. Keep the label readable.",
      sound="One quiet accent at most.",
      note="Both boundaries kept: no confidential process, no unpaid "
           "operational work."),

 dict(n=6, pr="B", slug="V13_Short_06_Do_Not_Confuse_Effort_With_Evidence",
      title="Do Not Confuse Effort With Evidence",
      onscreen="EFFORT IS NOT EVIDENCE",
      source="THE EVIDENCE STANDARD | What the month can prove",
      hook="Reading descriptions, having conversations, and making a sample "
           "are activities.",
      script=[
        "Reading descriptions, having conversations, and making a sample are "
        "activities.",
        "What those activities teach you is the evidence that informs the "
        "decision.",
        "Do not confuse effort with evidence.",
        "This plan can help you understand a destination and choose a better "
        "next action.",
        "It cannot validate every part of your career, overcome employer bias, "
        "guarantee access, or remove a real qualification gap. And it does not "
        "prove that all your prior experience transfers.",
        "So write one closing sentence for your private record.",
        "I will continue, modify, or stop this option because of this "
        "evidence. The next question I need answered is this.",
        "The best outcome of a test is a clearer decision, not necessarily the "
        "decision you hoped for."],
      ending="The best outcome of a test is a clearer decision, not "
             "necessarily the decision you hoped for.",
      visual="Camera-led. One full-screen card on effort versus evidence. One "
             "on the closing sentence stem.",
      sound="One flat accent at most.",
      note="Closes on the long-form final spoken line. No transition "
           "guarantee."),
]

SHORTS = S
