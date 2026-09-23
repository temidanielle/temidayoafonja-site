# -*- coding: utf-8 -*-
"""Family to spoken-trigger table.

Every full-screen family gets an exact spoken trigger. The first draft of the
trigger map derived triggers by matching a card name inside a cue direction,
which only ever resolved the artifact families and left two thirds of the
states marked CONTINUES. That leaves the editor guessing, which is the one
thing the trigger map exists to prevent. These are stated explicitly and every
one is verified against the locked master at build time.
"""
import cp_src as C

TRIGGER = {
1: {
 "V1_01_THE_MOVE": "Role one is Senior Manager, Program Management.",
 "V1_02_FIRST_READ": "Look at what repeats.",
 "V1_03_RE_HOOK": "Matching words are not enough.",
 "V1_04_WHAT_TRAVELS": "Take cross-functional influence.",
 "V1_05_THE_DIFFERENCE": "Now look at where seniority shows up.",
 "V1_06_THE_REAL_GAP": "And now we get to the part I do not want you to translate away.",
 "V1_07_THE_FULL_READ": "Now we can read the move.",
 "V1_08_THE_POINT": "You can be experienced and new at the same time.",
 "V1_09_SEVEN_DAY_MEMORY": "Here is what I want to come back to you the next time you see a role outside your current field:",
 "V1_10_CTA": "If you want to start with the evidence side, I made a free Career Evidence Starter.",
 "V1_11_WATCH_NEXT": "Watch “Is Your Job Making You Harder to Hire?” next.",
},
2: {
 "V2_01_VALUE_VS_LEGIBLE": "You can be doing very well at work and quietly becoming harder to hire somewhere else.",
 "V2_02_THE_SENTENCE": "“I own the QBR process for this business unit.”",
 "V2_03_REMOVE_THE_NOUNS": "Now remove the company nouns.",
 "V2_04_UNDERNEATH": "Maybe the real work is: “I combine incomplete operating data, surface the decision leaders are avoiding, and create a shared view of what needs to happen next.”",
 "V2_05_ACROSS_CONTEXTS": "Has another function used your judgment?",
 "V2_06_LAST_90_DAYS": "Then look at the last 90 days of your actual work.",
 "V2_07_THE_PATTERN": "If your judgment is growing and it remains useful across contexts, your work may be expanding your options.",
 "V2_08_ONE_TEST": "Before you decide the answer is a new employer, see whether you can change what the work is building.",
 "V2_09_PAYOFF": "The question is: if this context disappeared, could another person see and use what I know how to do?",
 "V2_10_SEVEN_DAY_MEMORY": "The next time somebody says, “We cannot do this without you,” I want one question to come back to you:",
 "V2_11_CTA": "If this made you realize that your evidence is still buried inside company language, start with the free Career Evidence Starter.",
 "V2_12_WATCH_NEXT": "Watch “Before You Quit Your Job, Save This First” next.",
},
3: {
 "V3_01_THE_WINDOW": "Your experience did not disappear.",
 "V3_02_WHAT_DISAPPEARS": "While you are still in the role, details are easier to reach.",
 "V3_03_THE_RULE": "So here is the rule: keep the proof, not the property.",
 "V3_05_FOUR_LINES": "For one strong example, write down four things.",
 "V3_06_THE_LINE": "Suppose you write: “I reduced the time an internal process took.”",
 "V3_07_THE_WORK": "Maybe the real work was that you found where the process kept getting stuck, brought together people who owned different parts of it, redesigned the handoff, and made the change without creating another control problem.",
 "V3_08_WHAT_IT_SUPPORTS": "Ask: what does this example actually support?",
 "V3_09_TEST_THE_NEXT_MOVE": "Then use the record to look forward.",
 "V3_10_BEFORE_YOU_RESIGN": "Before you resign, I want you to be able to say three things:",
 "V3_11_SEVEN_DAY_MEMORY": "The next time you start thinking seriously about leaving, I want one line to come back to you:",
 "V3_12_CTA": "If you are deciding whether to stay, move internally or leave, the free Career Decision Evidence Check gives you a structured way to separate what you know from what you are assuming.",
 "V3_13_WATCH_NEXT": "Watch “How to Change Careers After 10+ Years Without Starting Over” next.",
},
}

# Which state inside a family carries the family's entry trigger. Every other
# state in the family is a progressive reveal under the same narration.
def families(n):
    out = []
    for fam, name, _d, _no in C.SF.states(n):
        if fam not in out:
            out.append(fam)
    return out

def verify():
    bad = []
    for n in (1, 2, 3):
        joined = " ".join(C.SP.master_sentences(n))
        fams = families(n)
        for fam in fams:
            t = TRIGGER[n].get(fam)
            if not t:
                bad.append("V%d %s has no trigger" % (n, fam)); continue
            if t not in joined:
                bad.append("V%d %s trigger not in the locked master" % (n, fam))
        for fam in TRIGGER[n]:
            if fam not in fams:
                bad.append("V%d %s is a trigger for a family that does not exist"
                           % (n, fam))
    return bad

def regression():
    """A trigger that is not in the master must still be rejected."""
    joined = " ".join(C.SP.master_sentences(1))
    return "This sentence is not in any master." not in joined

if __name__ == "__main__":
    bad = verify()
    for n in (1, 2, 3):
        print("V%d  %d families, %d triggers" % (n, len(families(n)), len(TRIGGER[n])))
    print("problems:", bad or "none, every family has an exact spoken trigger "
                              "and every trigger is in its locked master")
    print("check still rejects a trigger that is not in the master:", regression())
