# -*- coding: utf-8 -*-
"""Three candidate Shorts per video. A selection bank, not three uploads.

Every line is a run of consecutive whole sentences lifted verbatim from that
video's FINAL Sticky Realization master. Membership alone is not enough: two
real sentences pulled from different places and pushed together can assert
something the master never says, so verbatim_problems() requires an unbroken
run in the same order, and stitch_regression() proves it rejects a stitch.
"""
import re
import st_parse as P

WPM = 165             # ceiling rate used for the length limit
PLANNING_WPM = 150    # slower rate used for the planning estimate
CEILING_SECONDS = 55
WORD_CEILING = 150

# The refresh brief's suggested Short territories, one per candidate, in order.
TERRITORY = {
 (1, 1): "You can be experienced and new at the same time.",
 (1, 2): "Matching words are not enough.",
 (1, 3): "Better resume language does not create experience you have not had.",
 (2, 1): "Valuable here is not the same as legible elsewhere.",
 (2, 2): "Remove the company nouns.",
 (2, 3): "Proficiency is not always expansion.",
 (3, 1): "Keep the proof, not the property.",
 (3, 2): "The project name stays; the judgment disappears.",
 (3, 3): "A new logo is not automatically a new direction.",
}

# Each Short is built from index runs into the master sentence stream, so the
# lines are verbatim by construction rather than by proofreading.
SPEC = {
 (1, 1): dict(label="EXPERIENCED AND NEW", card="V1_08_EXPERIENCED_AND_NEW",
              stop=[(0, 1)], hold=[(86, 91)], ask=[(92, 92)],
              opening="Cold open on camera, no card. The first two lines are the whole setup.",
              cut="Cut to V1_08_EXPERIENCED_AND_NEW on \u201cYou can be experienced and new at the same time.\u201d"),
 (1, 2): dict(label="MATCHING WORDS ARE NOT ENOUGH", card="V1_03_MATCHING_WORDS",
              stop=[(25, 33)], hold=[(34, 35), (43, 45)], ask=[(92, 92)],
              opening="Open on the two-column card already built, so the overlap is visible before the correction.",
              cut="Cut to V1_03_MATCHING_WORDS on \u201cMatching words are not enough.\u201d"),
 (1, 3): dict(label="BETTER LANGUAGE IS NOT EXPERIENCE", card="V1_06C_ALL_GAPS",
              stop=[(51, 52)], hold=[(53, 55)], ask=[(92, 92)],
              opening="Open on camera, mid-thought. The gap card arrives as the destination context is listed.",
              cut="Cut to V1_06C_ALL_GAPS on the list of contexts, then back to camera for the correction."),
 (2, 1): dict(label="VALUABLE HERE, LEGIBLE ELSEWHERE", card="V2_01_VALUE_VS_LEGIBLE",
              stop=[(9, 14)], hold=[(23, 24)], ask=[(73, 73)],
              opening="Cold open on camera. No card until the realization.",
              cut="Cut to V2_01_VALUE_VS_LEGIBLE on \u201cThose things are valuable.\u201d"),
 (2, 2): dict(label="REMOVE THE COMPANY NOUNS", card="V2_04_UNDERNEATH",
              stop=[(28, 31)], hold=[(32, 36)], ask=[(73, 73)],
              opening="Open on the resume sentence, already on screen, constructed-example label showing.",
              cut="Cut to V2_04_UNDERNEATH on \u201cMaybe the real work is\u201d and hold to the end."),
 (2, 3): dict(label="PROFICIENCY IS NOT EXPANSION", card="V2_06D_ALL",
              stop=[(45, 51)], hold=[(52, 54)], ask=[(73, 73)],
              opening="Open on camera. The 90-day card builds under the questions.",
              cut="Cut to V2_06D_ALL on \u201cAsk: what unfamiliar problem did I have to solve?\u201d"),
 (3, 1): dict(label="KEEP THE PROOF, NOT THE PROPERTY", card="V3_03A_THE_RULE",
              stop=[(42, 45)], hold=[(46, 47)], ask=[(78, 78)],
              opening="Open on camera. The rule card lands on the rule and holds.",
              cut="Cut to V3_03A_THE_RULE on \u201cSo here is the rule\u201d."),
 (3, 2): dict(label="THE JUDGMENT DISAPPEARS", card="V3_02C_ALL",
              stop=[(34, 38)], hold=[(39, 43)], ask=[(78, 78)],
              opening="Cold open, quiet. The what-disappears card builds as each item is named.",
              cut="Cut to camera on \u201cThe project name stays. The judgment disappears.\u201d"),
 (3, 3): dict(label="A NEW LOGO IS NOT A NEW DIRECTION", card="V3_09_TEST_THE_NEXT_MOVE",
              stop=[(66, 68)], hold=[(69, 71)], ask=[(78, 78)],
              opening="Open on camera, mid-thought, no greeting.",
              cut="Cut to V3_09_TEST_THE_NEXT_MOVE on the two questions, then back to camera."),
}

def _run(n, a, b):
    return " ".join(P.master_sentences(n)[a:b + 1])

SHORTS = {}
for k, d in SPEC.items():
    n = k[0]
    SHORTS[k] = dict(label=d["label"], card=d["card"],
                     territory=TERRITORY[k],
                     stop=[_run(n, a, b) for a, b in d["stop"]],
                     hold=[_run(n, a, b) for a, b in d["hold"]],
                     ask=[_run(n, a, b) for a, b in d["ask"]],
                     opening=d["opening"], cut=d["cut"])

def lines(k):
    s = SHORTS[k]
    return s["stop"] + s["hold"] + s["ask"]

def words(k):
    return sum(len(x.split()) for x in lines(k))

def seconds(k, rate=WPM):
    return words(k) / float(rate) * 60.0

# ---- one-ask rule: count INSTRUCTIONS, not verbs.
# An instruction can arrive after a leading clause: "And before you close your
# laptop for the last time, take one permitted example and write down ...". That
# is one ask, not zero. An earlier version anchored the verb to the very start of
# the sentence and scored all three V3 Shorts as having no ask at all, which was
# a counter defect and not a Shorts defect. imperative_regression() below proves
# the widened pattern still counts two separate instructions as two.
VERB = (r"(pick|take|answer|write|underline|read|name|choose|mark|list|"
        r"start|stop|put|do|remove|separate|ask|keep|capture)\b")
LEAD = r"(?:and\s+)?(?:[a-z][^,]{0,70},\s+)?"
IMPERATIVE = r"^" + LEAD + VERB
def actions(k):
    count = 0
    for line in SHORTS[k]["ask"]:
        for s in P.sentences(line):
            t = s.strip().lower()
            if re.match(IMPERATIVE, t):
                count += 1
            if re.search(r"\bthen\b\s+[a-z]*\s*(ask|write|do|read|pick|take|mark|put)\b", t):
                count += 1
            if re.search(r",\s*and\s+(ask|write|do|read|pick|take|mark|underline)\b", t):
                count += 1
    return count

OPENERS = r"^(that|this|those|these|it|they|he|she|there)\b"
def antecedent_problems(k):
    body = lines(k)
    first = P.sentences(body[0])[0].strip().lower()
    return [first[:70]] if re.match(OPENERS, first) else []

def _tokens(n):
    return " ".join(p for _s, p in P.spoken(n)).split()

def _is_run(line, toks):
    w = line.split()
    return any(toks[i:i + len(w)] == w for i in range(len(toks) - len(w) + 1))

def verbatim_problems(k):
    """Each line must appear as an unbroken run of the master's own words.

    The comparison is on the token stream, not on the sentence list. The masters
    break a quoted sentence onto its own paragraph, so "Imagine this sentence on
    a resume:" and the quoted line are two entries in the sentence stream but one
    sentence once they are read together. A sentence-level comparison failed that
    line although it is word for word from the master and in order, which was a
    granularity error in the check rather than a defect in the Short. A
    contiguous token run is the stricter reading of "verbatim consecutive": it
    still rejects sentences pulled from different places and pushed together,
    which stitch_regression() proves.
    """
    toks = _tokens(k[0])
    return [line for line in lines(k) if not _is_run(line, toks)]

def imperative_regression():
    """Two genuinely separate instructions must still count as two, and a
    sentence carrying no instruction at all must still count as none."""
    import types
    probe_two = ["Take one accomplishment. Then write three sentences."]
    probe_none = ["That is a harder question. It is also a much more useful one."]
    def count(ls):
        n = 0
        for line in ls:
            for s_ in P.sentences(line):
                t = s_.strip().lower()
                if re.match(IMPERATIVE, t):
                    n += 1
                if re.search(r"\bthen\b\s+[a-z]*\s*(ask|write|do|read|pick|take|mark|put)\b", t):
                    n += 1
                if re.search(r",\s*and\s+(ask|write|do|read|pick|take|mark|underline)\b", t):
                    n += 1
        return n
    return count(probe_two) >= 2 and count(probe_none) == 0

def stitch_regression():
    """Two real master passages that are not adjacent must still be rejected."""
    toks = _tokens(1)
    ms = P.master_sentences(1)
    return not _is_run(ms[0] + " " + ms[-1], toks)

def territory_ok(k):
    """The candidate has to actually sit on the territory the brief suggested."""
    body = " ".join(lines(k)).lower()
    key = {
     (1, 1): "experienced and new at the same time",
     (1, 2): "matching words are not enough",
     (1, 3): "better resume language does not create experience",
     (2, 1): "harder to hire somewhere else",
     (2, 2): "remove the company nouns",
     (2, 3): "proficiency is not always the same as expansion",
     (3, 1): "keep the proof, not the property",
     (3, 2): "the judgment disappears",
     (3, 3): "a new logo is not automatically a new direction",
    }[k]
    return key in body

def audit():
    return [dict(key=k, label=SHORTS[k]["label"], words=words(k),
                 sec_165=seconds(k, WPM), sec_150=seconds(k, PLANNING_WPM),
                 actions=actions(k), verbatim=verbatim_problems(k),
                 antecedent=antecedent_problems(k), territory=territory_ok(k))
            for k in sorted(SHORTS)]

if __name__ == "__main__":
    fails = 0
    for r in audit():
        p = []
        if r["words"] >= WORD_CEILING: p.append("WORDS>=%d" % WORD_CEILING)
        if r["sec_165"] > CEILING_SECONDS: p.append("OVER 55s AT 165WPM")
        if r["actions"] != 1: p.append("ACTIONS=%d" % r["actions"])
        if r["verbatim"]: p.append("NOT VERBATIM: %s" % r["verbatim"][0][:50])
        if r["antecedent"]: p.append("DANGLING: %s" % r["antecedent"][0])
        if not r["territory"]: p.append("OFF TERRITORY")
        fails += len(p)
        print("V%d S%d  %-34s %3dw  %4.1fs@165  %4.1fs@150  acts=%d  %s"
              % (r["key"][0], r["key"][1], r["label"], r["words"], r["sec_165"],
                 r["sec_150"], r["actions"], " ".join(p) or "OK"))
    print("\nstitch check still rejects a non-adjacent pair:", stitch_regression())
    print("sentence splitter handles a quoted sentence:", P.sentence_split_regression())
    print("ask counter still separates two instructions:", imperative_regression())
    print("problems:", fails)
