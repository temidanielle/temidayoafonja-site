# -*- coding: utf-8 -*-
"""Explicit family-to-trigger table for V12, V13 and V14.

Their card copy is written as compressed on-screen labels, not as verbatim
speech, so no inference from card text to spoken sentence can work. The first
attempt tried it and left most cards with no trigger, which is exactly what the
trigger-map standard forbids. These are stated and every one is verified
against its own locked master at build time.

V4 to V11 need nothing here: their triggers come from the resolved event list,
which already carries an exact entry phrase per event.
"""
import ap_src as A

TRIGGER = {
12: {
 "V12_FS_01_THE_LINE": "“Led a cross-functional transformation that improved on-time delivery by 18 percent.”",
 "V12_FS_02_TWO_PILES": "Look at that line again and split it into two piles.",
 "V12_FS_03_MINE_TO_DECIDE": "What was mine to decide?",
 "V12_FS_04_NOT_OBVIOUS": "Then ask what was not obvious.",
 "V12_FS_05_HOW_YOU_KNOW": "On-time delivery reached 89 percent is the result.",
 "V12_FS_06_THE_REWRITE": "Same made-up accomplishment.",
 "V12_FS_07_BEFORE_AND_AFTER": "Nothing got inflated.",
 "V12_FS_08_TEN_MINUTES": "Here is how the ten minutes actually go.",
 "V12_FS_09_THE_BOUNDARY": "One thing I am not going to promise you.",
 "V12_WATCH_NEXT": "Watch “Which Parts of Your Experience Actually Transfer to Another Industry?” next.",
},
13: {
 "V13_FS_01_THE_SAMPLE": "About fifty-five postings surfaced in the search.",
 "V13_FS_02_THREE_RISKS": "Three job postings.",
 "V13_FS_03_WHAT_TRAVELS": "Now the useful part.",
 "V13_FS_04_WHERE_IT_BREAKS": "What does not travel is knowing what wrong looks like before it happens.",
 "V13_FS_05_THREE_KINDS_OF_GAP": "So sort your own experience the way those postings sort it.",
 "V13_FS_06_HARD_OR_PREFERRED": "In this set, direct same-industry experience was a hard requirement in six of the twenty-eight.",
 "V13_FS_07_WHAT_NOT_TO_CLAIM": "Which brings me to what not to say.",
 "V13_FS_08_THE_SECOND_QUESTION": "Then for each match ask a second question.",
 "V13_WATCH_NEXT": "And if you want to see what that reading looks like, watch “I Read Two Similar Jobs. They Wanted Different Proof” next.",
},
14: {
 "V14_FS_01_THE_RULE": "I am not going to tell you what a hiring manager thinks.",
 "V14_FS_02_POSTING_ONE": "Start with the health insurer's posting.",
 "V14_FS_03_SIDE_BY_SIDE": "Read those again.",
 "V14_FS_04_WHAT_A_READER_CAN_CHECK": "From this posting, a reader could reasonably see that somebody who has run complex projects without supervision for five years has what this employer actually requires.",
 "V14_FS_05_AFTER_EACH_POSTING": "So instead of telling you what employers want, I am going to read both of these out loud and stop after each one to ask two things.",
 "V14_FS_06_WHAT_IM_NOT_SAYING": "Neither one told me what anybody thinks.",
 "V14_FS_07_TWO_PASSES": "Take one posting and read it twice.",
 "V14_WATCH_NEXT": "Watch “How to Turn One Accomplishment Into Proof in 10 Minutes” next.",
},
}

def verify():
    bad = []
    for n in (12, 13, 14):
        joined = " ".join(A.master_sentences(n))
        cards = [c[0] for c in A._mod(n).FULLSCREEN[n]]
        for cid in cards:
            t = TRIGGER[n].get(cid)
            if not t:
                bad.append("V%d %s has no trigger" % (n, cid))
            elif t not in joined:
                bad.append("V%d %s trigger not in the master: %s" % (n, cid, t[:60]))
        for cid in TRIGGER[n]:
            if cid not in cards:
                bad.append("V%d %s is a trigger for a card that does not exist" % (n, cid))
    return bad

def regression():
    joined = " ".join(A.master_sentences(12))
    return "This sentence is in no master." not in joined

if __name__ == "__main__":
    bad = verify()
    for n in (12, 13, 14):
        print("V%d  %d cards, %d triggers" % (n, len(A._mod(n).FULLSCREEN[n]), len(TRIGGER[n])))
    print("problems:", bad or "none")
    print("check still rejects a trigger that is not in the master:", regression())
