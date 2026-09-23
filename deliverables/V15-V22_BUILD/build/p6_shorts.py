# -*- coding: utf-8 -*-
"""Three candidate Shorts per video. Every line is a whole sentence lifted verbatim
from that video's recording master. Nothing is invented and no two sentences are
joined into a claim the master does not make."""
import re, importlib
import p6_blocks as B

WPM = 165            # upper bound used for the length ceiling
PLANNING_WPM = 150   # rate used for the planning estimate
CEILING_SECONDS = 55
WORD_CEILING = 150   # hard "< 150 words" rule

def master_sentences(n):
    m = importlib.import_module(B.MODS[n])
    out = []
    for _, paras in m.SECTIONS:
        for p in paras:
            out.extend(B.sentences(p))
    return out

# A Short is (label, payoff_card, [stop...], [hold...], [ask...]) with every string a
# verbatim master sentence.
SHORTS = {
(15, 1): dict(
 label="SO WHAT DID YOU DO?",
 card="V15_FS_01_TWO_DAYS",
 stop=["The report used to take you two days. Now a tool produces most of it in about forty minutes. That sounds like progress, and mostly it is. Until somebody looks at the finished thing and asks, so what did you actually do?"],
 hold=["That question is getting harder to answer. Not because you did less. Because the part of the work that used to prove you were there is the part that got easy."],
 ask=["Take one piece of work from this week where a tool did most of the visible production."],
 opening="Cold open on camera, no card. The first four sentences run before anything appears on screen.",
 cut="Cut to V15_FS_01_TWO_DAYS on “Not because you did less.”",
),
(15, 2): dict(
 label="WHAT THE PAGES DO NOT SHOW",
 card="V15_FS_04_WHAT_YOU_CANNOT",
 stop=["Let me put one on the table.",
       "This is a made-up example. I wrote it for this video, and it is not anyone's real work. A quarterly business summary. Four pages, drafted from the underlying numbers in about forty minutes."],
 hold=["Now tell me what you cannot see. You cannot see whether anyone asked if that improvement is real. You cannot see whether anyone checked the thing that most often makes this kind of summary misleading. You cannot see who is on the hook if leadership walks out of the room with the wrong picture."],
 ask=["Write three or four sentences. What you were responsible for getting right. What you checked and why you distrusted that particular thing. What you concluded that the first draft did not."],
 opening="Open on the constructed summary with its label already on screen. The label stays up for the whole artifact hold.",
 cut="Cut to V15_FS_04_WHAT_YOU_CANNOT on “Now tell me what you cannot see.”",
),
(15, 3): dict(
 label="THE RECORD STOPPED REACHING YOU",
 card="V15_FS_06_WRITE_IT_DOWN",
 stop=["The document shows the output. It does not show that somebody decided what could be wrong with it, went and looked, and came back with a changed conclusion. If you handed me those four pages six months later, I would have no way to tell whether you did any of that."],
 hold=["That is the whole problem. Not that the tool did the work. That the record stopped reaching the part you did."],
 ask=["Take one piece of work from this week where a tool did most of the visible production."],
 opening="Open on camera, mid-thought, no greeting.",
 cut="Cut to V15_FS_06_WRITE_IT_DOWN under the ask.",
),
(16, 1): dict(
 label="RELIED ON. STILL SKIPPED.",
 card="V16_FS_01_CALLED_AND_SKIPPED",
 stop=["When something is urgent, they call you. When something breaks, they call you. When somebody new needs to understand how the work really runs, they get sent to you. Then the interesting assignment gets handed out. The promotion list comes around. The bigger scope gets discussed. And you are not in the conversation."],
 hold=["There is one distinction I want you to leave with, and it decides almost everything about what you do next. It is the difference between a manager who does not know, and a manager who knows and does not act."],
 ask=["Pick the one person who actually influences scope decisions about you."],
 opening="Build the pattern card line by line under the cold open, then hold it.",
 cut="Cut to camera on “And you are not in the conversation.”",
),
(16, 2): dict(
 label="INFORMATION OR NOT",
 card="V16_FS_02_THE_HINGE",
 stop=["If your manager does not know what you contributed, you have an information problem. Frustrating, but fixable. You can close that gap yourself."],
 hold=["If your manager knows exactly what you contributed and the outcome still does not move, more explanation is probably not the missing ingredient. You can write the clearest account of your work anyone has ever produced and it will change nothing, because information was never what was missing."],
 ask=["Take two or three pieces of consequential work from the last year and make sure the person who decides about scope actually knows what was yours in them."],
 opening="Open on camera. The card arrives only on the second situation.",
 cut="Cut to V16_FS_02_THE_HINGE on “If your manager knows exactly what you contributed”.",
),
(16, 3): dict(
 label="NOBODY IS PLOTTING",
 card="V16_FS_04_NOT_INFORMATION",
 stop=["One thing I want to be careful about. Finding out you are in the second situation is not the same as finding out the organization is against you."],
 hold=["Most of the time nobody is plotting. There is a budget, a headcount plan, a person who was promised something last year, and a manager who is managing constraints they did not choose. Do not turn a structural answer into a story about your worth."],
 ask=["Pick the one person who actually influences scope decisions about you."],
 opening="Camera throughout. This one should feel like a correction, not a reveal.",
 cut="Cut to V16_FS_04_NOT_INFORMATION on “There is a budget, a headcount plan”.",
),
(17, 1): dict(
 label="WHAT GOES IS THE PRECISION",
 card="V17_FS_01_WHAT_GOES",
 stop=["A layoff can take your title in one meeting. It can take your access in the same hour. And then a few weeks later, when you are still processing it, somebody tells you to update your resume. That is when you find out what you can actually still prove."],
 hold=["Let us be specific about what disappears, because it is not usually the memory. You will remember the project. You will remember that it mattered and that you were the one holding it together. What goes is the precision."],
 ask=["Write what was true before, what was yours, what changed, and how you knew."],
 opening="Cold open, camera, very quiet. No music under the first two sentences.",
 cut="Cut to V17_FS_01_WHAT_GOES on “What goes is the precision.”",
),
(17, 2): dict(
 label="KEEP THE PROOF, NOT THE PROPERTY",
 card="V17_FS_04_THE_LINE",
 stop=["And here is the line, because it does not move. Keeping proof does not mean taking company property."],
 hold=["Do not send confidential documents to yourself. Do not copy customer data. Do not take internal reports, screenshots, source code, financial files, or anything you are not allowed to keep. Keep the proof, not the property.",
       "That is not only an ethics point, although it is that. It is a practical one. Career evidence that would not survive being asked about is not evidence. It is a liability you are carrying into an interview."],
 ask=["Write what was true before, what was yours, what changed, and how you knew."],
 opening="Open on camera. The boundary card comes up on the first Do not and stays.",
 cut="Cut to V17_FS_04_THE_LINE on “Do not send confidential documents to yourself.”",
),
(17, 3): dict(
 label="IF YOU CANNOT VERIFY IT",
 card="V17_FS_05_CANNOT_VERIFY",
 stop=["You will not recover every number. There will be a result you are certain about and cannot support. A metric you watched every week for two years and can no longer produce."],
 hold=["If you cannot verify it, do not invent it. I know how that lands when you are already losing something. But a number you cannot stand behind is worth less than a description you can. Say what you owned, what you decided, what changed in terms you can defend, and be honest that the precise figure lived in a system you no longer have."],
 ask=["Mark anything you cannot verify."],
 opening="Camera, close, no card until the line itself.",
 cut="Cut to V17_FS_05_CANNOT_VERIFY on “If you cannot verify it, do not invent it.”",
),
(18, 1): dict(
 label="EXPERIENCED AND NEW",
 card="V18_FS_01_STILL_DO_THE_WORK",
 stop=["You made the industry change. And the surprising part is that you can still do the work. What keeps catching you are the things nobody thought to explain. A meeting where everybody understands a phrase you have never heard. A decision that goes a direction you would not have predicted. A relationship that matters for reasons no process document mentions."],
 hold=["By the end I want you to be able to sort what is still ahead of you into three kinds. Things you can read. Things you have to be near. And things somebody has to give you access to. Because those need completely different plans, and most people treat them all the same."],
 ask=["Take one destination role. Not an industry. One role."],
 opening="Cold open on camera. The three examples build on screen as she names them.",
 cut="Cut to V18_FS_01_STILL_DO_THE_WORK on “What keeps catching you are the things nobody thought to explain.”",
),
(18, 2): dict(
 label="IN PLACE, NOT IN TRANSIT",
 card="V18_FS_02_IN_PLACE",
 stop=["I have moved across industries more than once, and the thing that surprised me every time was not the work."],
 hold=["There is research behind that, and it is blunter than the career advice usually is. Experience holds its value in place and loses some of it in transit. When star analysts moved firms, their performance dropped, because a good part of what made them excellent belonged to the old firm's people, systems and support. That is not a reason to stay. It is a reason to know what you are carrying."],
 ask=["Take one destination role. Not an industry. One role."],
 opening="Open on camera. The evidence card carries its one-study label for the full hold.",
 cut="Cut to V18_FS_02_IN_PLACE on “Experience holds its value in place”.",
),
(18, 3): dict(
 label="A LICENSING REQUIREMENT",
 card="V18_FS_06_LICENSING",
 stop=["And then there is the third kind, which is the one career advice is worst about. Some of it is closed to you until somebody grants it. Supervised practice. A caseload. Sign-off authority. Being in the room where the real version of the decision happens."],
 hold=["And some of it is a hard requirement that does not care how good you are. If a role needs a license, a registration or a qualification you do not hold, adjacent experience does not erase it. A licensing requirement is not a mindset issue."],
 ask=["Take one destination role. Not an industry. One role."],
 opening="Open on camera, then build the third list one item at a time.",
 cut="Cut to V18_FS_06_LICENSING on “A licensing requirement is not a mindset issue.”",
),
(19, 1): dict(
 label="WHAT DO YOU RECOMMEND?",
 card="V19_FS_01_THE_QUESTION",
 stop=["You know the work. You know the numbers. You can explain exactly what happened and why. Then somebody turns to you and asks, so what do you recommend we do? And knowing the work is suddenly not enough."],
 hold=["The evidence is incomplete. There is no obviously correct answer. Whatever gets decided will affect real people. And you realize you have never actually had to make that call. That moment feels like one gap. It is usually one of three, and they need completely different responses. If you pick the wrong one you can spend a year working hard on something that was never the problem."],
 ask=["Take one recent moment when the work got harder than your answer."],
 opening="Cold open, camera. The question card lands on the question and comes straight off again.",
 cut="Cut to V19_FS_01_THE_QUESTION on “so what do you recommend we do?”",
),
(19, 2): dict(
 label="CLOSE TO IT, NEVER CARRIED IT",
 card="V19_FS_03_NEVER_CARRIED",
 stop=["You can understand a decision very well and still never have carried one. Being close to decisions is not the same as carrying them."],
 hold=["And the strange thing about this gap is that being good is what creates it. If you are the most reliable person in the supporting role, the organization has very little reason to move you out of it. So this one is often not about you at all. Someone else held the authority. The role kept you next to the decision without ever handing it over."],
 ask=["Then pick one next step that matches."],
 opening="Open on the card, then come off it to camera for the explanation.",
 cut="Cut to camera on “And the strange thing about this gap”.",
),
(19, 3): dict(
 label="THE CHEAPEST RESPONSE",
 card="V19_FS_04_THREE_RESPONSES",
 stop=["Same hesitation. Three completely different next moves. And the reason I am laboring this is that the default response to that moment is to assume the first one. You feel exposed, so you go and learn something. That is the cheapest response and it is often the wrong one."],
 hold=["If the real problem is that you have never owned a call, a course will make you better informed without making you more practiced. And if the real problem is that nobody can see what you have already done, a course will not touch it at all."],
 ask=["Take one recent moment when the work got harder than your answer."],
 opening="Camera throughout. No card until the ask.",
 cut="Cut to V19_FS_04_THREE_RESPONSES under the ask.",
),
(20, 1): dict(
 label="THEN IT WAS NOT",
 card="V20_FS_03_ONE_LUMP",
 stop=["You did what you were supposed to do. You got good at the work. Your scope grew. Maybe you became a manager, then a senior manager. And the next step was always there. Not promised, but there. A box above you that people moved into. Then it was not."],
 hold=["Maybe the layer got removed. Maybe it is still there and nobody has left it in four years. Either way, the thing you were working toward is not waiting for you the way it was. So what are you supposed to do with a career plan whose next move stopped existing?"],
 ask=["So here is the exercise, and it takes about ten minutes. Write down what you expected the next role to give you."],
 opening="Cold open, camera. Silence under Then it was not.",
 cut="Cut to V20_FS_03_ONE_LUMP on “So what are you supposed to do with a career plan”.",
),
(20, 2): dict(
 label="WHAT THE EVIDENCE SUPPORTS",
 card="V20_FS_01_THE_NUMBERS",
 stop=["Here is what the evidence I have actually supports. Middle managers made up twenty-nine percent of layoffs in 2024, against an average of twenty-two percent in the years before. Openings for those roles fell by more than forty percent after 2022. And manager engagement has fallen, including as the number of people reporting to each manager goes up."],
 hold=["That is a real, sustained contraction and it is worth taking seriously. It is also not middle management dying. Those roles still exist. People still get them. What the evidence supports is narrower and more useful: for a lot of experienced managers, the next rung has gotten harder to reach or has gone."],
 ask=["Write down what you expected the next role to give you."],
 opening="Open on the numbers card with the source line on screen. Three figures, no chart.",
 cut="Cut to camera on “It is also not middle management dying.”",
),
(20, 3): dict(
 label="IT IS NOT ONE THING",
 card="V20_FS_02_NOT_DYING",
 stop=["When you lose the next title, you do not actually lose a title. You lose everything you assumed the title was going to hand you, all at once, in one lump. And because it arrived as one lump, it feels like one loss. It is not one thing. Pull it apart."],
 hold=["Now, a few things I am not going to tell you. I am not going to tell you titles do not matter. They affect pay, how the market reads you, and which conversations you get invited to. Somebody telling an experienced professional that a title is just a label is usually somebody who already has one."],
 ask=["Write down what you expected the next role to give you."],
 opening="Camera. The list is not built on screen in the Short, because seven items will not read at this length.",
 cut="Cut to V20_FS_02_NOT_DYING on “Somebody telling an experienced professional”.",
),
(21, 1): dict(
 label="WHO GREW MORE?",
 card="V21_FS_01_TWO_PEOPLE",
 stop=["Let me put two people next to each other. Same level, same company, same year. The first one gets a bigger team. Twice as many people. Same kinds of decisions as before, same kind of work, more meetings, more one-to-ones, more coordination. The second one keeps the same title and the same team size."],
 hold=["But this year, a decision that used to go two levels up now stops with her. She makes the call. If it goes wrong, it is hers. Who grew more?",
       "The work says something different. One of them is carrying more volume. The other one is carrying more consequence."],
 ask=["Write down one decision you make now that you did not make a year ago."],
 opening="Two columns building side by side from the first sentence. This is the whole Short.",
 cut="Cut to camera on “Who grew more?” and leave the pause in.",
),
(21, 2): dict(
 label="TWELVE MONTHS FROM NOW",
 card="V21_FS_04_TWELVE_MONTHS",
 stop=["Are you making calls you used to escalate? That is the one people underestimate. The difference between recommending and deciding is enormous and it almost never shows up in a title."],
 hold=["There is one question I would ask about any role you are in or being offered. Twelve months from now, what will I be able to do, decide, or prove that I cannot do today? That is it. If you can answer it specifically, you have a real answer about growth."],
 ask=["Write down one decision you make now that you did not make a year ago."],
 opening="Open on camera. The question card comes up on the question and holds to the end.",
 cut="Cut to V21_FS_04_TWELVE_MONTHS on “Twelve months from now”.",
),
(21, 3): dict(
 label="A NICE WORD FOR THE SAME PAY",
 card="V21_FS_03_FOUR_LOOKS",
 stop=["Now the part I want to be firm about. Do not let growth become a nice word your company uses when it wants senior work at the same pay. It happens."],
 hold=["So keep compensation in the conversation. Keep title in the conversation too, if a title affects how the market reads your work, which in a lot of fields it does. You are allowed to say: I can see what this builds, and I would also like to talk about what it pays."],
 ask=["Write down one decision you make now that you did not make a year ago."],
 opening="Camera, firm, no card until the last line.",
 cut="Cut to V21_FS_03_FOUR_LOOKS on “You are allowed to say”.",
),
(22, 1): dict(
 label="READY, OR NOTHING TO BE READY FOR",
 card="V22_FS_01_THE_TWO_QUESTIONS",
 stop=["Most career advice still assumes there is a ladder waiting for you. Do good work. Get promoted. Manage people. Manage more people. Become a director."],
 hold=["That path still exists. For a lot of experienced professionals it has gotten shorter. And that changes more than how long you wait. It changes which question you should be asking about your own career. Because there are two very different questions and they feel identical from the inside. Am I not ready yet? Or is there nothing to be ready for?"],
 ask=["Stop planning from the org chart you remember and go and look at the one that exists."],
 opening="Cold open, camera. The ladder list builds as she says it, then clears.",
 cut="Cut to V22_FS_01_THE_TWO_QUESTIONS on “Am I not ready yet?”",
),
(22, 2): dict(
 label="THE PACKAGE CAME APART",
 card="V22_FS_03_THE_PACKAGE",
 stop=["The old arrangement connected a set of things together. More scope led to a bigger title, which brought more authority, more money, more status, and more access. They moved as a package. You could plan around the package."],
 hold=["Flattening breaks the connection, and it breaks it unevenly. Now you can get more scope with no title. More people with no more authority. A bigger title doing exactly the same work. Or an individual contributor role carrying harder decisions than the manager role next to it.",
       "A title no longer tells you what somebody decides. More people no longer tells you somebody grew."],
 ask=["Stop planning from the org chart you remember and go and look at the one that exists."],
 opening="Open on the package card assembled, then break it apart on screen as she says Flattening.",
 cut="Cut to V22_FS_04_BROKEN on “Flattening breaks the connection”.",
),
(22, 3): dict(
 label="READINESS OR STRUCTURE",
 card="V22_FS_08_READINESS_OR_STRUCTURE",
 stop=["Sometimes you are facing a readiness problem. There is something you have not done yet, or not done enough, and there is a seat you could reasonably move into once you have. And sometimes you are facing a structure problem. There is no seat. Better performance cannot create one."],
 hold=["You are allowed to stop blaming yourself for a bottleneck that may not be about your capability. But I want to be careful with that line, because it is the one people will screenshot. It does not mean every stalled career is structural. Sometimes there is a seat, it does open, and the honest answer is that somebody else was readier."],
 ask=["Stop planning from the org chart you remember and go and look at the one that exists."],
 opening="Camera. The two-sided card holds under the whole Short.",
 cut="Cut to camera on “But I want to be careful with that line”.",
),
}
def lines(k):
    s = SHORTS[k]
    return s["stop"] + s["hold"] + s["ask"]

def words(k):
    return sum(len(x.split()) for x in lines(k))

def seconds(k, rate=WPM):
    return words(k) / rate * 60.0

# ---- one-ask rule: count INSTRUCTIONS, not verbs.
IMPERATIVE = r"^(pick|take|answer|write|underline|read|name|choose|mark|list|start|stop|put|do)\b"
def actions(k):
    """A new sentence with an imperative verb starts a new instruction. A bare 'and'
    inside one sentence keeps two steps of one task together. 'Then ...' starts another."""
    count = 0
    for line in SHORTS[k]["ask"]:
        for s in B.sentences(line):
            t = s.strip().lower()
            if re.match(IMPERATIVE, t):
                count += 1
            if re.search(r"\bthen\b\s+[a-z]*\s*(ask|write|do|read|pick|take|mark)\b", t):
                count += 1
            if re.search(r",\s*and\s+(ask|write|do|read|pick|take|mark|underline)\b", t):
                count += 1
    return count

# ---- dangling antecedent check: an opening pronoun with nothing in the Short to bind to.
OPENERS = r"^(that|this|those|these|it|they|he|she|there)\b"
def antecedent_problems(k):
    body = lines(k)
    bad = []
    for i, line in enumerate(body):
        first = B.sentences(line)[0].strip().lower()
        if i == 0 and re.match(OPENERS, first):
            bad.append(first[:70])
    return bad

def verbatim_problems(k):
    """Each Short line is a RUN of consecutive whole sentences from the master.

    Membership alone is not enough: sentences pulled from different places and pushed
    together can assert something the master never says. So each line must appear as an
    unbroken consecutive run in the master sentence stream, in the same order. The first
    draft of this check compared whole lines against the set of single master sentences
    and flagged all nine Shorts, which was a checker-scope error, not a Shorts defect.
    stitch_regression() below proves the corrected check still rejects a stitch.
    """
    ms = master_sentences(k[0])
    bad = []
    for line in lines(k):
        run = B.sentences(line)
        if any(x not in ms for x in run):
            bad.append(line); continue
        hit = False
        for i in range(len(ms) - len(run) + 1):
            if ms[i:i + len(run)] == run:
                hit = True; break
        if not hit:
            bad.append(line)
    return bad

def stitch_regression():
    """Two real master sentences that are not adjacent must still be rejected."""
    ms = master_sentences(15)
    probe = ms[0] + " " + ms[-1]
    run = B.sentences(probe)
    for i in range(len(ms) - len(run) + 1):
        if ms[i:i + len(run)] == run:
            return False
    return True

def audit():
    rows = []
    for k in sorted(SHORTS):
        rows.append(dict(key=k, label=SHORTS[k]["label"], words=words(k),
                         sec_165=seconds(k, WPM), sec_150=seconds(k, PLANNING_WPM),
                         actions=actions(k), verbatim=verbatim_problems(k),
                         antecedent=antecedent_problems(k)))
    return rows

if __name__ == "__main__":
    fails = 0
    for r in audit():
        p = []
        if r["words"] >= WORD_CEILING: p.append("WORDS>=%d" % WORD_CEILING)
        if r["sec_165"] > CEILING_SECONDS: p.append("OVER 55s AT 165WPM")
        if r["actions"] != 1: p.append("ACTIONS=%d" % r["actions"])
        if r["verbatim"]: p.append("NOT VERBATIM: %s" % r["verbatim"][0][:60])
        if r["antecedent"]: p.append("DANGLING: %s" % r["antecedent"][0])
        fails += len(p)
        print("V%d S%d  %-32s %3dw  %4.1fs@165  %4.1fs@150  acts=%d  %s"
              % (r["key"][0], r["key"][1], r["label"], r["words"], r["sec_165"],
                 r["sec_150"], r["actions"], " ".join(p) or "OK"))
    print("\nstitch check still rejects a non-adjacent pair:", stitch_regression())
    print("problems:", fails)
