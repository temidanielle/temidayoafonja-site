# -*- coding: utf-8 -*-
"""Voice + constraint checks that run against the spoken scripts."""
import re, importlib

MODS = {12: "p3_script12", 13: "p3_script13", 14: "p3_script14"}

def spoken(n):
    m = importlib.import_module(MODS[n])
    return [(sec, p) for sec, ps in m.SECTIONS for p in ps]

def text(n):
    return "\n".join(p for _, p in spoken(n))

FAILS = []
def check(name, ok, detail=""):
    FAILS.append((name, bool(ok), detail))
    return ok

# --- 1. no em dashes / en dashes in spoken text
for n in MODS:
    bad = [p for _, p in spoken(n) if "—" in p or "–" in p]
    check("V%d no em/en dashes in spoken text" % n, not bad, bad[:1])

# --- 2. mind-reading bans (all three, hard ban in V14)
# A sentence only violates the rule when it ASSERTS what a reader thinks. Sentences that
# refuse the claim ("It cannot tell you that a hiring manager would waive a requirement")
# state the limitation and must not be flagged. Scope fixed after the V13 limitation
# sentence tripped the first draft of this check; see mindread_regression() below, which
# proves the narrowed check still fires on a genuine assertion.
MIND = [r"hiring managers? (will|would|do|don'?t) ", r"employers? (think|believe|don'?t believe|want you)",
        r"they will reject you", r"what employers are really", r"recruiters? (think|want)"]
REFUSAL = (r"cannot tell|can'?t tell|does not tell|do not know|don'?t know|"
           r"not going to tell|never tells|cannot show|it cannot|nobody knows")

def mindread_hits(body):
    out = []
    for s in re.split(r"(?<=[.?!])\s+", body.lower()):
        if re.search(REFUSAL, s):
            continue
        for p in MIND:
            if re.search(p, s):
                out.append((p, s.strip()[:90]))
    return out

def mindread_regression():
    """The narrowed check must still fire on a plain assertion."""
    probe = "A hiring manager will think you are a risk. Employers think adjacent experience is weak."
    return len(mindread_hits(probe)) == 2

for n in MODS:
    hits = mindread_hits(text(n))
    check("V%d no mind-reading phrasing" % n, not hits, hits)
check("mind-reading check still fires on an injected assertion", mindread_regression())

# --- 3. industry generalization ban (V13/V14 especially)
GEN = [r"healthcare employers", r"technology companies want", r"financial services always",
       r"tech companies (think|want|believe)", r"the healthcare industry wants", r"banks want"]
for n in MODS:
    t = text(n).lower()
    hits = [p for p in GEN if re.search(p, t)]
    check("V%d no industry-wide generalization" % n, not hits, hits)

# --- 4. V13 denominators preserved exactly
t13 = text(13).lower()
for tok in ["fifty-five", "forty", "twenty-eight", "eighteen entries",
            "ten healthcare", "ten financial services", "eight technology"]:
    check("V13 denominator present: %s" % tok, tok in t13)
check("V13 states collection date", "september tenth, 2026" in t13)
check("V13 sample-not-market disclaimer", "is not the labor market" in t13)

# --- 5. no live-posting claim
LIVE = [r"these (jobs|roles|postings) are (open|live|hiring)", r"currently hiring", r"go apply to (these|them)",
        r"still open", r"you can apply to (these|them)"]
for n in (13, 14):
    t = text(n).lower()
    hits = [p for p in LIVE if re.search(p, t)]
    check("V%d never calls the postings live" % n, not hits, hits)
check("V13 discloses closed/stale postings", "already closed" in t13)
check("V14 discloses past posted dates", "past their posted dates" in text(14).lower())

# --- 6. V12 must not brand the four questions
t12 = text(12).lower()
BRAND = [r"the \w+ (framework|method|formula|system|model)", r"i call (this|it) the",
         r"\bthe four-line\b", r"my (framework|method|formula)", r"\bacronym\b"]
hits = [p for p in BRAND if re.search(p, t12)]
check("V12 does not brand the prompts as a framework", not hits, hits)
check("V12 states the proof-is-not-hired boundary", "does not get you hired" in t12)
# The reconciliation replaced the literal phrase "About the ten minutes", so this checks
# the substance instead of the wording: one spoken paragraph that allocates the ten
# minutes across all four prompts. ten_minute_regression() proves it fails without one.
def _ten_minute_budget(paras):
    for p in paras:
        low = p.lower()
        if "ten minutes" in low and all(x in low for x in (
                "what was true before", "what was yours to decide",
                "not obvious", "what changed and how you know")):
            return p
    return None

def ten_minute_regression():
    return _ten_minute_budget(["Here is how the ten minutes actually go."]) is None

check("V12 budgets the ten minutes on camera",
      _ten_minute_budget([p for _, p in spoken(12)]) is not None and ten_minute_regression())
check("V12 labels the artifact as not a real resume", "not a real resume" in t12)

# --- 7. V14 approved phrasings actually used
t14 = text(14).lower()
for ph in ["from this posting", "a reader could reasonably see",
           "what i still cannot tell", "it does not tell me"]:
    check("V14 uses approved phrasing: %s" % ph, ph in t14)
check("V14 states the no-mind-reading rule out loud", "i do not know" in t14)

# --- 8. Watch Next routing
check("V12 watch-next names V13 by title",
      "which parts of your experience actually transfer to another industry?" in text(12).lower())
check("V13 watch-next points forward to the two-posting read",
      "two real postings side by side" in text(13).lower())
check("V14 watch-next names V12 by title",
      "turn one accomplishment into proof in 10 minutes" in t14)

# --- 9. word counts
COUNTS = {}
for n in MODS:
    COUNTS[n] = sum(len(p.split()) for _, p in spoken(n))
check("V12 speech-only fits under 10 minutes at 130 wpm", COUNTS[12] / 130 <= 10.0,
      "%d words = %.2f min" % (COUNTS[12], COUNTS[12] / 130))


# --- 10. reconciliation: V12 carries no counted or named question set
t12 = text(12).lower()
COUNTED = [r"\bfirst question\b", r"\bsecond question\b", r"\bthird question\b",
           r"\bfourth question\b", r"\bfour questions\b", r"\bfour answers\b",
           r"\bthose four\b", r"\bthe four\b"]
hits = [p for p in COUNTED if re.search(p, t12)]
check("V12 presents no counted or named question set", not hits, hits)

# --- 11. reconciliation: V14 retires the proves/suggests system and the gate vocabulary
t14 = text(14).lower()
VOCAB = [r"\bproves\b", r"\bsuggests\b", r"\bthe gate\b", r"\bgating\b", r"\bhard gate\b",
         r"read for the lock", r"opposite locks", r"\bimplication\b"]
hits = [p for p in VOCAB if re.search(p, t14)]
check("V14 carries no proves/suggests or gate/lock vocabulary", not hits, hits)

# --- 12. reconciliation: V13 loses the report-like phrases the review named
t13 = text(13).lower()
REPORTY = ["shared spine", "control artifact", "coordination rhythm", "gates on",
           "failure modes are observed"]
hits = [p for p in REPORTY if p in t13]
check("V13 loses the report-like phrases", not hits, hits)

# --- 13. no unsupported population claim about resumes
for n in MODS:
    hits = [m.group(0) for m in re.finditer(r"most resumes[^.]*", text(n).lower())]
    check("V%d makes no unsupported claim about most resumes" % n, not hits, hits)

# --- 14. lines the brief said not to rewrite are still word for word present
PRESERVED = {
12: ["You did the work. I believe you. The sentence does not.",
     "What was mine to decide?",
     "Change the emphasis. Do not change the truth.",
     "You already did the work.",
     "Put it back."],
13: ["Same two words. Three different jobs.",
     "What does not travel is knowing what wrong looks like before it happens.",
     "You can carry the method. You cannot carry the instinct for what counts as a risk in a room you have never been in.",
     "The real question is not whether your experience transfers. It is whether it transfers to this posting.",
     "Your experience is not worth less than you thought. It is more specific than you thought. Say the specific thing."],
14: ["I am not going to tell you what a hiring manager thinks. I do not know.",
     "If you have four, that is a fact about you and that posting, and no amount of good writing changes it.",
     "The posting is silent on that, and silence is not a no."],
}
for n, lines_ in PRESERVED.items():
    miss = [x for x in lines_ if x not in text(n)]
    check("V%d preserves every line the brief said not to rewrite" % n, not miss, miss)

# --- 15. V14 keeps one brief human bridge, and keeps it brief
bridge = "I have had to learn this in my own moves too."
present = bridge in text(14)
para = [p for _, p in spoken(14) if bridge in p]
short_enough = bool(para) and len(para[0].split()) <= 45
check("V14 carries one brief human bridge", present and short_enough,
      "%d words" % (len(para[0].split()) if para else 0))
check("V14 human bridge appears exactly once", text(14).count(bridge) == 1)

# --- 16. V13 keeps every denominator the brief listed
for tok in ["fifty-five", "forty", "twenty-eight", "eighteen entries",
            "ten healthcare", "ten financial services", "eight technology"]:
    check("V13 denominator preserved: %s" % tok, tok in t13)

# --- 17. no episode names watch-me-read as a public method
for n in MODS:
    check("V%d never names a public methodology" % n,
          "watch-me-read" not in text(n).lower())

if __name__ == "__main__":
    bad = [f for f in FAILS if not f[1]]
    for name, ok, detail in FAILS:
        print(("PASS " if ok else "FAIL ") + name + (("  " + str(detail)) if detail and not ok else ""))
    print("\n%d checks, %d failed" % (len(FAILS), len(bad)))
    print("word counts:", COUNTS)
