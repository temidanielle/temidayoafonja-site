# -*- coding: utf-8 -*-
"""Shorts corrections for Videos 4 to 7, against the September 9 lock.

The existing Shorts are the base. This module imports them and applies only
targeted corrections, so "corrections only" is provable rather than asserted:
`report()` prints every Short with its status, and anything not listed in
PATCHES is carried through untouched.

A Short is a separate vertical take for someone who has never seen the long
video, so it legitimately paraphrases. Paraphrase is not a defect. A Short is
corrected only when it contradicts the locked script, quotes a premise the
locked script removed, or duplicates another Short weakly.
"""
import importlib.util, copy

D = "/home/user/temidayoafonja-site/deliverables/"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


_A = _load("_sh45", D + "new-videos-4-5-swap/build/shorts.py")
_B = _load("_sh67", D + "new-videos-6-7-v2/build/shorts.py")
BASE = {4: _A.SHORTS[4], 5: _A.SHORTS[5], 6: _B.SHORTS[6], 7: _B.SHORTS[7]}

SPM = 165.0


def seconds(s):
    return sum(len(p.split()) for p in s["script"]) / SPM * 60.0


# (video, short number) -> the corrected fields, plus why
PATCHES = {
(4, 1): dict(
    status="REBUILD",
    why="Genuine contradiction. The Short's whole argument was the retired "
        "rule \"stop explaining your career in order\", and it said explaining "
        "moves in order makes a career sound like a list of departures. The "
        "locked script uses compressed Chapters in the ninety-second answer on "
        "purpose. Rebuilt on the script's actual opening problem.",
    title="Introduction or Defense?",
    slug="V4_Short_01_Introduction_Or_Defense",
    onscreen="INTRODUCTION, OR DEFENSE?",
    hook="You are halfway through answering \"walk me through your "
         "background,\" and you notice something.",
    script=[
      "You are halfway through answering \"walk me through your background,\" "
      "and you notice something.",
      "You are explaining why you left each job, and you still have not said "
      "what all that work has built in you.",
      "So you add more context. Why the industry changed. Why the next title "
      "looked different.",
      "And now your answer feels less like an introduction and more like a "
      "defense.",
      "Here is the fix. You do not need to pretend every move was planned.",
      "You need to show what stayed consistent through the moves that actually "
      "happened.",
      "That consistent thing has a name. It is your Spine, and it does not "
      "change depending on who is asking."],
    ending="It does not change depending on who is asking.",
    visual="Open tight on camera. Full-screen callout on \"less like an "
           "introduction and more like a defense,\" camera hidden. Back to her "
           "for the fix.",
    sound="One soft impact as the full-screen line lands.",
    note="Rebuilt for the September 9 lock. Carries the script's opening beat "
         "instead of the retired ordering rule."),

(4, 2): dict(
    status="COPY UPDATE",
    why="Obsolete reference. The hook framed the answer as a reply to \"so "
        "what do you do?\", a question the locked script does not use, and it "
        "said no job titles or employer list while the script's own modeled "
        "answer names three contexts. The template, the stop, and the "
        "next-question line are all still spoken and are kept.",
    hook="Here is a twenty-second introduction to a whole career, in three "
         "sentences.",
    script=[
      "Here is a twenty-second introduction to a whole career, in three "
      "sentences.",
      "You need three things. The work pattern. Just enough context to show "
      "range. Where you are pointed now.",
      "Mine sounds like this. I get brought in when the evidence is incomplete "
      "and an important decision still has to be made. I have done that in "
      "audit, life sciences, and technology. Today I use that same lens "
      "through my own firm.",
      "Your version is: I, and then the work pattern. I have done that in, and "
      "then two or three contexts. Today I, and then your current direction.",
      "And then stop. Leave room for the next question.",
      "Your first answer does not have to contain your whole career. It has to "
      "give the other person a clear place to begin.",
      "If the answer lands, they will ask another question. Let them."],
    note="Corrected for the September 9 lock. The retired \"so what do you "
         "do?\" framing was replaced with the script's own quick-introduction "
         "framing, and the modeled answer now matches the master verbatim."),

(4, 6): dict(
    status="COPY UPDATE",
    why="Obsolete reference. The closing used a door metaphor, \"the story is "
        "what opens the door, the proof is what holds it open,\" which is not "
        "in the locked script. Replaced with the script's own formulation.",
    script=[
      "A story explains. Proof supports.",
      "Eventually somebody is going to say: tell me more about that.",
      "That is the moment when your evidence has to carry the answer.",
      "A good career story cannot substitute for work you did not do.",
      "So yes, build the versions. Get the wording right. Say them out loud "
      "until the apologizing stops.",
      "And then make sure there is something underneath them.",
      "The story gets you to the next question. Your evidence answers it."],
    ending="The story gets you to the next question. Your evidence answers it.",
    note="Corrected for the September 9 lock. The closing now uses the "
         "script's own line instead of a metaphor the master does not carry."),

(6, 1): dict(
    status="REBUILD",
    why="Obsolete premise. The entire Short was built on \"an internal move "
        "can look safe because the logo does not change,\" which the locked "
        "script removed. The script now opens on the offer itself and the "
        "one-year question.",
    title="A Year From Now",
    slug="V6_Short_01_A_Year_From_Now",
    onscreen="NEW TITLE, SAME WORK?",
    hook="You are offered an internal role. Same company. Better title. Maybe "
         "more money.",
    script=[
      "You are offered an internal role. Same company. Better title. Maybe "
      "more money.",
      "It feels like progress because something is changing.",
      "But before I said yes, I would want one question answered.",
      "A year from now, what will I be able to do, decide, or prove that I "
      "cannot do today?",
      "Because an internal move can change your title without changing your "
      "career.",
      "You can get a new title, a new manager, and a new team, and still do "
      "almost exactly the same class of work.",
      "That move may still be right for pay, flexibility, stability, or "
      "manager fit. Those are legitimate reasons.",
      "Just do not call it growth automatically. Test the work, not the "
      "label."],
    ending="Test the work, not the label.",
    visual="Open on camera. Full-screen NEW TITLE, SAME WORK? on the hook, "
           "camera hidden. Full-screen one-year question on that line. Back to "
           "her for the close.",
    sound="One soft whoosh on the thumbnail line, one restrained accent on the "
          "one-year question.",
    note="Rebuilt for the September 9 lock. Carries the script's new opening "
         "and its one-year question."),

(6, 2): dict(
    status="COPY UPDATE",
    why="Two corrections. The hook said \"ask three questions\" where the "
        "script says \"test three things,\" and the reading line said \"a "
        "strong growth case\" where the script now says the developmental case "
        "is strong. The three questions themselves are unchanged.",
    hook="Before you take an internal role, test three things.",
    script=[
      "Before you take an internal role, test three things.",
      "Will the work change? Will my judgment expand? Will the evidence "
      "travel?",
      "Will the work change means: what is actually different on an ordinary "
      "Monday? New problems, new systems, new stakeholders, a new part of the "
      "business you can see.",
      "Will my judgment expand means: what will I be trusted to notice, weigh, "
      "recommend, or own?",
      "Will the evidence travel means: could I explain what changed without "
      "relying on internal acronyms, relationships, or reputation?",
      "Three clear yeses and the developmental case is strong. Two tells you "
      "which dimension to investigate or negotiate.",
      "Zero or one may be movement without much growth. That can still be the "
      "right choice. Just be accurate about what the work is giving you."],
    note="Corrected for the September 9 lock. Wording aligned to the script's "
         "\"test three things\" and \"the developmental case is strong,\" and "
         "the zero-or-one reading keeps the script's MAY BE."),

(6, 3): dict(
    status="COPY UPDATE",
    why="Obsolete reference. The Short carried \"neither one is unimportant\" "
        "and a cross-functional meeting example, both of which the locked "
        "script removed. The report example and the core distinction remain "
        "and are kept.",
    script=[
      "Dependable people often get more responsibility before they get more "
      "judgment.",
      "More tasks can mean volume, coordination, and absorption.",
      "More judgment means interpreting incomplete information, weighing "
      "tradeoffs, recommending a direction, or owning the consequence when the "
      "instructions stop being clear.",
      "Preparing a report is work. Deciding which pattern in the report "
      "matters, explaining the consequence, and recommending what happens next "
      "requires different judgment.",
      "So before an internal move, ask which decisions belong to the role.",
      "And check the authority around that judgment. If you are accountable "
      "for an outcome but cannot influence the decisions, priorities, "
      "resources, or people that produce it, keep investigating.",
      "If the answer is simply, you will have more to manage, that is not "
      "enough information."],
    ending="That is not enough information.",
    note="Corrected for the September 9 lock. The removed example and the "
         "removed \"neither one is unimportant\" line are gone; the authority "
         "check the script adds is now included."),

(6, 4): dict(
    status="COPY UPDATE",
    why="Obsolete reference. The closing said words like strategic do not tell "
        "you what you will become able to do; the locked script now says they "
        "are not enough if nobody can tell you what will actually be "
        "different.",
    script=[
      "Before you accept an internal role, ask one very practical question.",
      "What will actually be different on an ordinary Monday?",
      "Not whether the title sounds more senior. What will be different on a "
      "normal working day.",
      "Ask what problems you will own, what systems you will learn, which "
      "stakeholders you will have to influence, and what part of the business "
      "will become visible from the new seat.",
      "A move can be significant even if the title barely changes. A new "
      "customer, operating model, regulation, or decision process can expand "
      "your range.",
      "Words like strategic, visible, and high impact are not enough if nobody "
      "can tell you what will actually be different.",
      "If nobody can name it, the title may be changing more than your "
      "career."],
    ending="The title may be changing more than your career.",
    note="Corrected for the September 9 lock."),

(6, 5): dict(
    status="REBUILD",
    why="Obsolete premise. The Short was built on \"inside your company, "
        "everybody may know you are the person who can get something done, and "
        "another employer does not inherit that reputation,\" which the locked "
        "script removed, along with its explicit confidential-material "
        "sentence. Rebuilt on the interview thought experiment the script now "
        "uses, which carries the same boundary through the phrase \"the "
        "permitted result.\"",
    title="Will the Evidence Travel?",
    slug="V6_Short_05_Will_The_Evidence_Travel",
    onscreen="WILL THE EVIDENCE TRAVEL?",
    hook="Imagine that a year from now you are interviewing somewhere else.",
    script=[
      "Imagine that a year from now you are interviewing somewhere else.",
      "Could you explain what changed, without relying on internal acronyms, "
      "relationships, or reputation?",
      "That is the third question to ask before you take an internal role. "
      "Will the evidence travel?",
      "You should be able to name four things: the problem, your role, the "
      "judgment you used, and the permitted result.",
      "I would look for three kinds of evidence. Result: what changed, "
      "improved, stabilized, or became possible. Judgment: what did you "
      "notice, weigh, recommend, or decide. Range: what new context or problem "
      "can you now handle.",
      "The strongest internal moves eventually let you say: I entered a new "
      "context, I was trusted to make this kind of judgment, here is what "
      "changed.",
      "So before you accept, ask how success is measured, and what a strong "
      "first year would let you point to."],
    ending="Ask what a strong first year would let you point to.",
    visual="Camera for the thought experiment. Full-screen three-part reveal "
           "on result, judgment and range, camera hidden. Back to her for the "
           "close.",
    sound="One restrained click per evidence type.",
    note="Rebuilt for the September 9 lock. Nothing here suggests keeping "
         "confidential, proprietary, customer, employee or employer-owned "
         "material: the script's own phrase is the permitted result."),

(6, 6): dict(
    status="COPY UPDATE",
    why="The Short expanded the script's line into \"you may not need to leave "
        "your company to build a very different career chapter.\" The locked "
        "script says it twice, exactly, as \"You may not need to leave. But "
        "the work does need to change.\" Tightened to the spoken line.",
    hook="You may not need to leave. But the work does need to change.",
    script=[
      "You may not need to leave. But the work does need to change.",
      "An internal move can absolutely be a real career move. The employer is "
      "only one part of the context.",
      "The work, the decisions, the stakeholders, the systems, and the "
      "evidence can change even when the logo does not.",
      "And do not assume the external option automatically wins. A new "
      "employer can give you a new logo and the same work.",
      "Compare the actual access to different work, stronger judgment, and "
      "clearer evidence.",
      "That comparison is the decision. Not internal versus external.",
      "You may not need to leave. But the work does need to change."],
    ending="You may not need to leave. But the work does need to change.",
    note="Corrected for the September 9 lock. Now opens and closes on the "
         "script's own line."),

(7, 2): dict(
    status="COPY UPDATE",
    why="The reading line said \"you probably have a real growth case.\" The "
        "locked script says the career case for growth is visible, and the "
        "master's own visual map says GROWTH CASE VISIBLE. The CAR "
        "explanation itself is unchanged.",
    script=[
      "When your job gets bigger, run the CAR test.",
      "C is for Complexity. Did the problem become more complex, or did the "
      "volume simply increase?",
      "A is for Authority. Did your ability to influence or decide expand with "
      "the responsibility?",
      "R is for Return. What did the extra work return to your capability, "
      "your evidence, or your recognition?",
      "If all three are expanding, the career case for growth is visible. The "
      "work may still be demanding, but you can see what it is building.",
      "If the volume grew and those three did not, the role has expanded "
      "mainly as workload.",
      "That may be acceptable for a short season. Just give the season a "
      "boundary and a review date."],
    note="Corrected for the September 9 lock. \"A real growth case\" became "
         "the script's conditional \"the career case for growth is "
         "visible.\""),
}


def build():
    out = {}
    for n in (4, 5, 6, 7):
        rows = []
        for s in BASE[n]:
            s = copy.deepcopy(s)
            p = PATCHES.get((n, s["n"]))
            if p:
                p = dict(p)
                s["status"] = p.pop("status")
                s["why"] = p.pop("why")
                s.update(p)
            else:
                s["status"] = "REUSE"
                s["why"] = ("Semantically aligned with the locked script. It "
                            "paraphrases for a standalone vertical audience, "
                            "which is intended, and asserts nothing the script "
                            "denies.")
            rows.append(s)
        out[n] = rows
    return out


SHORTS = build()


def report():
    for n in (4, 5, 6, 7):
        print("VIDEO %d" % n)
        for s in SHORTS[n]:
            print("  %s%d %-11s %-44s %4.1fs  hook==first line: %s"
                  % (s["pr"], s["n"], s["status"], s["title"][:44],
                     seconds(s), s["hook"] == s["script"][0]))


if __name__ == "__main__":
    report()
