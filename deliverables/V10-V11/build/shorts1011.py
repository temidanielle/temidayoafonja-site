# -*- coding: utf-8 -*-
"""Three candidate Shorts per video, assembled from the script's own words.

Neither FINAL script carries a Shorts section, and the handoff is explicit
that no spoken wording may be invented for one. So every line below is a
whole sentence lifted verbatim from its parent video's spoken stream, and
verify() proves that against the script rather than asserting it.

Three means three. These are a selection bank, not a set to expand.

Each Short is built as STOP SCROLL, then HOLD ATTENTION, then ONE ASK, and
each has to stand alone: none of them is a trailer for the long-form video.
"""
import re
import v1011 as S

WPM = 165

# The angle each Short is built to, supplied in the handoff.
ANGLE = {
 (10, 1): ("DON'T PROVE YOURSELF YET", "Recognition and contradiction."),
 (10, 2): ("EXPERIENCED BUT NEW TO THE CONTEXT", "Distinction."),
 (10, 3): ("ASK YOUR MANAGER THIS BY DAY 90", "Practical instrument."),
 (11, 1): ("THIS ISN'T THE JOB", "Recognition."),
 (11, 2): ("EXPECTED VS ACTUAL", "Diagnostic."),
 (11, 3): ("WHAT IS THE COST OF ROLE DRIFT?", "Practical decision lens."),
}

# The boundary each video's Shorts must carry, in the parent video's terms.
BOUNDARY = {
 10: "The video does not require a visible win by day 90 and does not "
     "claim what every manager evaluates. A Short may not tighten either "
     "into a rule. The reversal is evidence gathering, not an instruction "
     "to leave.",
 11: "The employer and the manager are never the villain. A Short may not "
     "use bait-and-switch as a blanket label, may not imply that drift "
     "always means leaving, and may not drop the legitimate reasons a role "
     "changes or the real constraints that shape what is possible.",
}

EDITOR = {
 10: "Reuse the long-form cards reframed to 9:16 where one exists. The "
     "manager questions card carries straight over. Nothing that depicts a "
     "specific employer, and no stock office imagery.",
 11: "Reuse the EXPECTED against ACTUAL comparison and the clarification "
     "script card. If a Short shows one cost lens, the other three appear "
     "at least once before the ask, so no single lens reads as the whole "
     "test.",
}

SHORTS = {
 (10, 1): dict(
   stop=["And now you feel this pressure to prove they made the right "
         "decision.",
         "That pressure can make you do exactly the wrong thing."],
   hold=["You start talking too much about what worked at your last "
         "company.",
         "Or you go the other direction and stay quiet because you are "
         "afraid of getting something wrong.",
         "I do not think either one is the job of your first 90 days.",
         "Especially if you are experienced."],
   ask=["I think about that as READ. TEST. PROVE."]),
 (10, 2): dict(
   stop=["Then you walk into a new company and suddenly you do not know "
         "which meeting actually matters."],
   hold=["You do not know who really makes the decision.",
         "You do not know which rule is a real rule and which one is "
         "simply how the last person did it.",
         "You can be experienced and still be new to the context.",
         "Those two things can be true at the same time."],
   ask=["Your experience should help you ask better questions.",
        "It should not make you assume you already know the answers."]),
 (10, 3): dict(
   stop=["That question is broad enough to get you an answer like, "
         "“You’re doing great.”"],
   hold=["“What have you seen me pick up quickly?”",
         "“Where do I still need more context?”",
         "“Is there anything I am treating like my old environment "
         "that works differently here?”",
         "“What would you want to trust me with by the end of my "
         "first 90 days that you would not have trusted me with on day "
         "one?”"],
   ask=["That question turns the first 90 days into development, not "
        "performance theater."]),
 (11, 1): dict(
   stop=["You accepted one job. Then you started doing another."],
   hold=["Maybe the title is the same.", "Maybe the salary is the same.",
         "But three or six weeks in, the work itself feels materially "
         "different from what you thought you were saying yes to.",
         "Before you call it a bait-and-switch, I want you to slow the "
         "read down.",
         "Roles change. Priorities move. Managers inherit new problems. "
         "Organizations reorganize."],
   ask=["I use four questions for that: EXPECTED. ACTUAL. COST. CHOICE."]),
 (11, 2): dict(
   stop=["Start with EXPECTED. What did you reasonably believe you were "
         "accepting?"],
   hold=["Then write ACTUAL. What is the job asking from you now?",
         "Do not judge it from one bad week. Look for the recurring "
         "pattern.",
         "Sometimes the actual role is better than the one you expected.",
         "And sometimes the actual role is narrower."],
   ask=["The question is not, “Is this exactly what was written?” "
        "The question is, “Is the actual role still close enough to "
        "the role I agreed to build my life and career around?”"]),
 (11, 3): dict(
   stop=["Then ask COST. What does the difference actually cost you?"],
   hold=["Not every mismatch deserves the same response.",
         "I would look at four costs.",
         "CAPABILITY. Is this role building judgment, scope, and "
         "experience you want to carry forward?",
         "EVIDENCE. Will you be able to prove meaningful work from this "
         "version of the job?",
         "COMPENSATION. Has the scope changed enough that the pay, level, "
         "or agreement needs to be revisited?",
         "LIFE. Did the practical cost change: travel, hours, location, "
         "caregiving, health, or something else that mattered when you "
         "accepted?",
         "A mismatch can be manageable in one category and unacceptable "
         "in another."],
   ask=["You need to know which one you are actually reacting to."]),
}


def lines(n, num):
    d = SHORTS[(n, num)]
    return d["stop"] + d["hold"] + d["ask"]


def rows(n):
    out = []
    for num in (1, 2, 3):
        d = SHORTS[(n, num)]
        body = " ".join(lines(n, num))
        words = len(body.split())
        title, kind = ANGLE[(n, num)]
        out.append(dict(num=num, title=title, kind=kind, stop=d["stop"],
                        hold=d["hold"], ask=d["ask"], body=body,
                        words=words,
                        secs=int(round(words / float(WPM) * 60))))
    return out


def verify(n):
    """Every line must be a verbatim sentence of the parent video.

    The comparison is made on the normalized spoken text, so curly quotes
    and spacing cannot hide a paraphrase.
    """
    spoken = S._norm(S.spoken_text(n))
    bad = []
    for num in (1, 2, 3):
        for l in lines(n, num):
            if S._norm(l) not in spoken:
                bad.append((num, l[:70]))
    return bad


if __name__ == "__main__":
    for n in S.VIDEOS:
        bad = verify(n)
        print("NEW V%d  %s" % (n, "every Short line is verbatim script"
                               if not bad else "NOT VERBATIM: %s" % bad))
        for r in rows(n):
            print("   %d  %-36s %3d words  about 0:%02d"
                  % (r["num"], r["title"], r["words"], r["secs"]))
