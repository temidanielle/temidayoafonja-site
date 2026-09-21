# -*- coding: utf-8 -*-
"""Three candidate Shorts per video. Every line is a whole sentence lifted verbatim
from that video's recording master. Nothing is invented and no two sentences are
joined into a claim the master does not make."""
import re, importlib
import p2_blocks as B

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
(12, 1): dict(
 label="THE SENTENCE DOES NOT",
 card="V12_FS_01_THE_LINE",
 stop=["Here is one line from a resume. Not a real resume. I wrote it for this video, and it is the kind of line I read all the time.",
       "“Led a cross-functional transformation that improved on-time delivery by 18 percent.”",
       "That sounds strong. There is a verb. There is scope. There is a number."],
 hold=["And I still cannot tell what you did. I cannot see what was broken before you got there, what you were allowed to decide, what was hard about it, or where the 18 percent came from.",
       "You did the work. I believe you. The sentence does not."],
 ask=["Pick one accomplishment you remember clearly. Not your best one. Just one you can still see."],
 opening="Cold open on the card. No greeting, no channel bumper. The line is on screen before the first word.",
 cut="Cut to camera on “And I still cannot tell what you did.”",
),
(12, 2): dict(
 label="WHAT WAS MINE TO DECIDE",
 card="V12_FS_03_MINE_TO_DECIDE",
 stop=["We are used to being asked what we were responsible for, so we answer with a title or a list of duties. Try the harder version. What was mine to decide?"],
 hold=["If your honest answer is, I did not own much, I mostly executed, do not throw the example away. Execution is full of decisions. What did you sequence? What did you escalate? What tradeoff did you put in front of somebody else?",
       "In the senior postings I read for this series, one of the most common asks was moving people who do not report to you. This is not about pretending you had power you did not have. It is about naming the decisions that were genuinely yours."],
 ask=["Answer four questions. What was true before. What was mine to decide. What was not obvious. What changed and how I know."],
 opening="Open on camera, mid-thought. The card arrives on the question, not before it.",
 cut="Cut to V12_FS_03_MINE_TO_DECIDE on “What was mine to decide?”",
),
(12, 3): dict(
 label="IF NOBODY COULD HAVE DISAGREED",
 card="V12_FS_04_NOT_OBVIOUS",
 stop=["Picture yourself halfway through fixing a system, where the cleanest move is also the one most likely to make your numbers look worse before they get better. That is where judgment shows."],
 hold=["Judgment is this. There were two reasonable options. I picked one. Here is why. It has to be a call that could have gone the other way. If nobody could have disagreed with you, it was a task."],
 ask=["Pick one accomplishment you remember clearly. Not your best one. Just one you can still see."],
 opening="Open on camera. The card holds only under the definition.",
 cut="Cut to V12_FS_04_NOT_OBVIOUS on “Judgment is this.”",
),
(13, 1): dict(
 label="SAME WORDS. DIFFERENT WORK.",
 card="V13_FS_02_THREE_RISKS",
 stop=["Three job postings. All three of them say manage risk.",
       "Same two words. Three different jobs.",
       "And on a resume, all three of them read: managed risk."],
 hold=["Go back to those three risk clauses. The mechanics are identical. Identify, assess, mitigate, escalate. That travels.",
       "What does not travel is knowing what wrong looks like before it happens.",
       "You can carry the method. You cannot carry the instinct for what counts as a risk in a room you have never been in."],
 ask=["Take one posting you are actually considering and underline every place its language matches your experience. Not a category. One posting."],
 opening="Cold open on the three-column card with all three risk clauses already visible.",
 cut="Cut to camera on “What does not travel is knowing what wrong looks like before it happens.”",
),
(13, 2): dict(
 label="TWENTY-EIGHT POSTINGS",
 card="V13_FS_01_THE_SAMPLE",
 stop=["About fifty-five postings surfaced in the search. I read forty of them all the way through. Twenty-eight went into the set. Ten healthcare, ten financial services, eight technology. Everything I threw out is logged with a reason, eighteen entries, so you can check the work instead of trusting me."],
 hold=["In this set, direct same-industry experience was a hard requirement in six of the twenty-eight. Preferred in about nine. Not mentioned at all in eleven. A project management certification was hard in four.",
       "Twenty-eight postings is not the labor market. Every number I give you is a number about those twenty-eight."],
 ask=["Take one posting you are actually considering and underline every place its language matches your experience. Not a category. One posting."],
 opening="Cold open on the sample card. The counts are on screen before the first word.",
 cut="Cut to camera on “Twenty-eight postings is not the labor market.”",
),
(13, 3): dict(
 label="STUDY IT, SEE IT, OR BE GIVEN IT",
 card="V13_FS_05_THREE_KINDS_OF_GAP",
 stop=["Some of what you are missing is readable. Delivery methods. Published frameworks. The common tools. That is why the certifications exist."],
 hold=["Some of it you only pick up by being near it. You can read about how a trading desk works. The rhythm of one gets learned by sitting close to it.",
       "And some of it is closed to you until you are inside. One bank posting required knowledge of that company's own change management policies. Another required experienced knowledge of its own internal delivery process. No amount of reading gets you there.",
       "That is not a discouraging distinction. It tells you which gap is a study problem, which one is an access problem, and which one is a timing problem."],
 ask=["Take one posting you are actually considering and underline every place its language matches your experience. Not a category. One posting."],
 opening="Open on camera. The card builds one row at a time under the three kinds of gap.",
 cut="Cut to V13_FS_05_THREE_KINDS_OF_GAP on “Some of it you only pick up by being near it.”",
),
(14, 1): dict(
 label="OPPOSITE LOCKS",
 card="V14_FS_03_OPPOSITE_LOCKS",
 stop=["Two job postings. Both senior project roles. I collected both on the same day, September tenth, 2026, and both were already past their posted dates by then. So I am not sending you anywhere. I am reading."],
 hold=["The first, from Humana, says in writing that the person should be comfortable working on new projects with limited knowledge of the content and be able to learn quickly. The hard requirements are five years of project management and a degree. Everything about the subject matter is listed as preferred.",
       "The second, from J.P. Morgan Wealth Management, wants seven or more years of experience in the financial services industry. That one is hard. A project management background is listed as preferred.",
       "Same family of work. Opposite locks."],
 ask=["Take one posting and read it twice."],
 opening="Cold open on the two-column card with both requirement lists already visible.",
 cut="Cut to camera on “Same family of work. Opposite locks.”",
),
(14, 2): dict(
 label="PROVES OR SUGGESTS",
 card="V14_FS_04_PROVES_OR_SUGGESTS",
 stop=["A line proves something when a reader can check it. A date. A scope. A number with a method under it. A decision you made that somebody else could have made differently."],
 hold=["A line suggests something when the reader has to supply the belief. Strategic. Transformational. Extensive experience. Proven track record. None of those can be checked, and a careful reader treats them as decoration.",
       "Most resumes are mostly suggestion. That is normal. The fix is not to delete the suggestions. It is to know which of your lines are doing which job, so you never think you have proved something you have only implied."],
 ask=["Take one posting and read it twice."],
 opening="Cold open on the card with the left column filled and the right column empty.",
 cut="Cut to camera on “Most resumes are mostly suggestion.”",
),
(14, 3): dict(
 label="I DO NOT KNOW WHAT THEY THINK",
 card="V14_FS_01_THE_RULE",
 stop=["I am not going to tell you what a hiring manager thinks. I do not know. Nobody reading a posting knows."],
 hold=["What I can do is read what is written and separate what the words support from what the words only hint at. That is a smaller claim than most career advice makes, and it is the one the page actually earns.",
       "I am not saying the posting is the truth. Job descriptions are aspirational, they get copied between roles, and several postings I read carried blocks that clearly belonged to a different job."],
 ask=["Take one posting and read it twice."],
 opening="Open on camera, no card. The rule is delivered to the lens.",
 cut="Cut to V14_FS_01_THE_RULE on “What I can do is read what is written.”",
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
    ms = master_sentences(12)
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
