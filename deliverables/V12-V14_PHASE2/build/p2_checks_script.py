# -*- coding: utf-8 -*-
"""Voice + constraint checks that run against the spoken scripts."""
import re, importlib

MODS = {12: "p2_script12", 13: "p2_script13", 14: "p2_script14"}

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
         r"\bthe four-line\b", r"my (framework|method|formula)"]
hits = [p for p in BRAND if re.search(p, t12)]
check("V12 does not brand the four questions", not hits, hits)
check("V12 states the proof-is-not-hired boundary", "does not get you hired" in t12)
check("V12 budgets the ten minutes on camera", "about the ten minutes" in t12)
check("V12 labels the artifact as not a real resume", "not a real resume" in t12)

# --- 7. V14 approved phrasings actually used
t14 = text(14).lower()
for ph in ["from this posting", "a reader could reasonably see",
           "what i still cannot tell", "it does not prove"]:
    check("V14 uses approved phrasing: %s" % ph, ph in t14)
check("V14 states the no-mind-reading rule out loud", "i do not know" in t14)

# --- 8. Watch Next routing
check("V12 watch-next names V13 by title",
      "which parts of your experience actually transfer to another industry?" in text(12).lower())
check("V13 watch-next points forward to the two-posting read",
      "two real postings side by side" in t13)
check("V14 watch-next names V12 by title",
      "turn one accomplishment into proof in 10 minutes" in t14)

# --- 9. word counts
COUNTS = {}
for n in MODS:
    COUNTS[n] = sum(len(p.split()) for _, p in spoken(n))
check("V12 speech-only fits under 10 minutes at 130 wpm", COUNTS[12] / 130 <= 10.0,
      "%d words = %.2f min" % (COUNTS[12], COUNTS[12] / 130))

if __name__ == "__main__":
    bad = [f for f in FAILS if not f[1]]
    for name, ok, detail in FAILS:
        print(("PASS " if ok else "FAIL ") + name + (("  " + str(detail)) if detail and not ok else ""))
    print("\n%d checks, %d failed" % (len(FAILS), len(bad)))
    print("word counts:", COUNTS)
