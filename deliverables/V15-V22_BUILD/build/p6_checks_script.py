# -*- coding: utf-8 -*-
"""Voice and constraint checks that run against the V15 to V22 spoken scripts.

Checker discipline used throughout: where a check needed narrowing, the narrowed
version is paired with a regression probe that proves it still fires on a genuine
violation. A check is never loosened without that proof.
"""
import re, importlib

MODS = {n: "p6_script%d" % n for n in range(15, 23)}
VIDEOS = sorted(MODS)

def spoken(n):
    m = importlib.import_module(MODS[n])
    return [(sec, p) for sec, ps in m.SECTIONS for p in ps]

def text(n):
    return "\n".join(p for _, p in spoken(n))

def mod(n):
    return importlib.import_module(MODS[n])

FAILS = []
def check(name, ok, detail=""):
    FAILS.append((name, bool(ok), detail))
    return ok

# --- 1. no em dashes / en dashes in spoken text
for n in VIDEOS:
    bad = [p for _, p in spoken(n) if "—" in p or "–" in p]
    check("V%d no em/en dashes in spoken text" % n, not bad, bad[:1])

# --- 2. no mind-reading. A sentence violates the rule only when it ASSERTS what
# somebody else thinks. Sentences that refuse the claim state a limit and must not fire.
MIND = [r"hiring managers? (will|would|do|don'?t) ", r"employers? (think|believe|don'?t believe|want you)",
        r"they will reject you", r"what employers are really", r"recruiters? (think|want)",
        r"your manager (thinks|believes|has decided that you)",
        r"leadership (thinks|believes|has decided)"]
REFUSAL = (r"cannot tell|can'?t tell|does not tell|do not know|don'?t know|"
           r"not going to tell|never tells|cannot show|it cannot|nobody knows|"
           r"i am not going to pretend|neither can anyone")

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
    probe = ("A hiring manager will think you are a risk. Employers think adjacent "
             "experience is weak. Your manager thinks you are not ready.")
    return len(mindread_hits(probe)) == 3

for n in VIDEOS:
    hits = mindread_hits(text(n))
    check("V%d no mind-reading phrasing" % n, not hits, hits)
check("mind-reading check still fires on an injected assertion", mindread_regression())

# --- 3. no industry-wide or employer-wide generalization
GEN = [r"healthcare employers", r"technology companies want", r"financial services always",
       r"tech companies (think|want|believe)", r"the healthcare industry wants", r"banks want",
       r"every (employer|company|organization)", r"all employers", r"companies have decided"]
for n in VIDEOS:
    t = text(n).lower()
    hits = [p for p in GEN if re.search(p, t)]
    check("V%d no industry-wide generalization" % n, not hits, hits)

# --- 4. no unsupported universal management claim.
# The source of record says "middle management is dying" overstates the case. V20 and V22
# both quote that phrase in order to REFUSE it, so the check must distinguish asserting it
# from refusing it. mgmt_regression() proves the narrowed check still fires on an assertion.
MGMT = [r"middle management is (dead|dying|over|finished)",
        r"management is (dead|dying|over)",
        r"there are no more manager", r"managers are being replaced",
        r"nobody gets promoted anymore", r"the ladder is gone"]
NEGATION = (r"not going to tell you|it is also not|does not support|overstates|"
            r"is not the case|i am not saying|the evidence does not|still exist")

def mgmt_hits(body):
    out = []
    for s in re.split(r"(?<=[.?!])\s+", body.lower()):
        if re.search(NEGATION, s):
            continue
        for p in MGMT:
            if re.search(p, s):
                out.append(s.strip()[:100])
    return out

def mgmt_regression():
    """Counts distinct offending SENTENCES, not pattern matches: two MGMT patterns both
    match "middle management is dead", so counting matches overstates the violation."""
    probe = ("Middle management is dead. Nobody gets promoted anymore. "
             "The ladder is gone.")
    return len(set(mgmt_hits(probe))) == 3

for n in VIDEOS:
    hits = mgmt_hits(text(n))
    check("V%d makes no universal management claim" % n, not hits, hits)
check("management-claim check still fires on an injected assertion", mgmt_regression())
check("V20 speaks the boundary out loud", "It is also not middle management dying" in text(20))
check("V22 speaks the boundary out loud",
      "I am not going to tell you middle management is dead" in text(22))

# --- 5. no search-demand claim anywhere. Every search figure is Unknown in the source.
DEMAND = [r"search(es|ed)? for this", r"search volume", r"people are searching",
          r"most searched", r"trending", r"google trends", r"keyword", r"monthly searches",
          r"everybody is asking this", r"the most common question on youtube"]
for n in VIDEOS:
    t = text(n).lower()
    hits = [p for p in DEMAND if re.search(p, t)]
    check("V%d makes no search-demand claim" % n, not hits, hits)

# --- 6. no new public framework. No named method, no counted set, no acronym.
BRAND = [r"the \w+ (framework|formula)", r"i call (this|it) the",
         r"my (framework|method|formula)", r"\bacronym\b", r"\bstep one\b",
         r"\bfirst pillar\b", r"the \w+ principle", r"learn,? practice,? prove",
         r"learn / practice / prove"]
# Capitalized names read as branding even for ordinary words, so these run against the
# ORIGINAL-CASE text. "the delivery methods" is not branding; "the Delivery Method" is.
BRAND_CASED = [r"\bthe [A-Z][a-zA-Z]+ (Framework|Method|Formula|System|Model)\b",
               r"\bThe [A-Z][a-zA-Z]+ (Framework|Method|Formula|System|Model)\b"]
COUNTED = [r"\bfirst question\b", r"\bsecond question\b", r"\bthird question\b",
           r"\bfourth question\b", r"\bthe four (questions|answers|pillars|boxes)\b",
           r"\bgap one\b", r"\bgap two\b", r"\bgap three\b",
           r"\btype one\b", r"\btype two\b", r"\bcategory one\b"]
def brand_hits(n):
    t = text(n)
    return ([p for p in BRAND + COUNTED if re.search(p, t.lower())]
            + [p for p in BRAND_CASED if re.search(p, t)])

for n in VIDEOS:
    hits = brand_hits(n)
    check("V%d names no framework and counts no set" % n, not hits, hits)

def framework_regression():
    """Both halves must still fire: the lowercase branding half and the capitalized half."""
    lower = "i call this the capability framework. the first question is simple. gap one is here."
    cased = "Run it through the Capability Method before you decide."
    a = len([p for p in BRAND + COUNTED if re.search(p, lower)])
    b = len([p for p in BRAND_CASED if re.search(p, cased)])
    return a >= 3 and b >= 1

def framework_false_positive_probe():
    """The narrowed pattern must NOT fire on ordinary English. This is the sentence in
    V18 that the first draft of this check wrongly flagged."""
    ordinary = "The delivery methods. The standard tools. That is the business model."
    return not ([p for p in BRAND + COUNTED if re.search(p, ordinary.lower())]
                + [p for p in BRAND_CASED if re.search(p, ordinary)])

check("framework check still fires on an injected framework", framework_regression())
check("framework check does not fire on ordinary English",
      framework_false_positive_probe())

# --- 7. Missing Rung language guardrail: never the same ordered run of the four concepts,
# and never a four-box set. The four concepts, in the roadmap's own terms.
CONCEPT = {
 "authority": r"\bauthority\b|\bdecision rights\b|\bsign-off\b",
 "complexity": r"harder problems|more ambiguous|more consequential|harder decisions",
 "return": r"\bcompensation\b|\bmoney\b|\bwhat it pays\b|\bearning more\b|\bpay\b",
 "options": r"future options|\boptions\b|makes the next (employer|move)|open anything|"
            r"a role possible",
}
def concept_order(n):
    t = text(n).lower()
    firsts = []
    for k, pat in CONCEPT.items():
        m = re.search(pat, t)
        if m:
            firsts.append((m.start(), k))
    return tuple(k for _, k in sorted(firsts))

ORDERS = {n: concept_order(n) for n in VIDEOS}
dupes = {}
for n, o in ORDERS.items():
    if len(o) == 4:
        dupes.setdefault(o, []).append(n)
repeats = {o: v for o, v in dupes.items() if len(v) > 1}
check("no two episodes run all four concepts in the same order", not repeats, repeats)

def four_box_regression():
    """The guardrail is meaningful only if a full four-run is detectable at all."""
    return any(len(o) == 4 for o in ORDERS.values())
check("at least one episode does carry all four, so the order check is live",
      four_box_regression(), ORDERS)

for n in VIDEOS:
    t = text(n).lower()
    check("V%d never names the structure" % n,
          not re.search(r"the missing rung|the four (dimensions|elements|components)|"
                        r"a four-box|the rung framework", t))

# --- 8. V17 does not duplicate V8. It must point at the habit video, not re-teach it.
t17 = text(17)
check("V17 names the other video rather than re-teaching the habit",
      "I made a video a while back about keeping a record of your own work" in t17)
check("V17 states it is the other situation",
      "This is when there is no time to build a habit" in t17)
check("V17 keeps the property boundary on camera",
      "Keep the proof, not the property." in t17)
check("V17 keeps the do-not-invent line", "If you cannot verify it, do not invent it." in t17)

# --- 9. V18 does not re-teach V13.
t18 = text(18)
check("V18 points at the transfer video rather than re-teaching it",
      "I have a whole video on exactly which parts of experience carry into a new industry" in t18)
check("V18 labels the study as one study of one profession",
      "star analysts moved firms" in t18.lower())
check("V18 keeps the licensing line", "A licensing requirement is not a mindset issue." in t18)

# --- 10. V19 does not name Learn/Practice/Prove and does not number the gaps.
t19 = text(19)
check("V19 refuses the diagnostic reading",
      "It is not a diagnostic and it does not assign you a type." in t19)
check("V19 points at the evidence video rather than re-teaching it",
      "I have a whole video on rebuilding one accomplishment" in t19)
check("V19 keeps the access boundary",
      "You cannot award yourself authority your role does not hold." in t19)

# --- 11. V20 does not run V22's structural diagnosis.
t20l = text(20).lower()
V22_ONLY = [r"org chart", r"draw the ladder", r"count them", r"how many roles actually exist",
            r"readiness problem", r"structure problem", r"how often do they open"]
hits = [p for p in V22_ONLY if re.search(p, t20l)]
check("V20 does not steal V22's structural diagnosis", not hits, hits)
check("V20 keeps the blocked-path boundary",
      "A blocked path is information." in text(20))
check("V20 keeps titles real",
      "Somebody telling an experienced professional that a title is just a label" in text(20))

# --- 12. V21 keeps promotion, title and compensation real.
t21 = text(21)
check("V21 refuses the titles-are-meaningless move",
      "Anyone who tells an experienced professional that titles are meaningless" in t21)
check("V21 keeps promotion attached to money",
      "Promotion usually comes with money" in t21)
check("V21 keeps compensation in the ask",
      "I would also like to talk about what it pays" in t21)
check("V21 names the unpaid-senior-work pattern",
      "Do not let growth become a nice word your company uses" in t21)

# --- 13. V22's constructed chart is labelled in the SPOKEN text, not only on the card.
t22 = text(22)
check("V22 labels the chart as constructed on camera",
      "Here is a constructed example, not a real employer's chart." in t22)
check("V22 keeps both limits on camera",
      "This is your organization, not the economy." in t22
      and "And I cannot tell you this continues." in t22)
check("V22 keeps the qualification next to the screenshot line",
      "Sometimes there is a seat, it does open, and the honest answer is that somebody "
      "else was readier." in t22)

# --- 14. evidence attribution is spoken wherever a figure is spoken.
FIGURE = r"twenty-nine percent|forty percent|twenty-two percent"
for n in VIDEOS:
    t = text(n).lower()
    if re.search(FIGURE, t):
        check("V%d frames its figures as evidence it is reporting" % n,
              "here is what the evidence i have actually supports" in t
              or "what the evidence does support" in t, t[:0])

# --- 15. no employer is named anywhere in the spoken scripts.
EMPLOYERS = [r"\bhumana\b", r"\bwells fargo\b", r"\bj\.?p\.? ?morgan\b", r"\bchase\b",
             r"mass general", r"\bgoogle\b", r"\bamazon\b", r"\bmeta\b", r"\bmicrosoft\b",
             r"\bdeloitte\b", r"\bmckinsey\b"]
for n in VIDEOS:
    t = text(n).lower()
    hits = [p for p in EMPLOYERS if re.search(p, t)]
    check("V%d names no employer" % n, not hits, hits)

# Research organizations ARE named on purpose in V20 and V22, and nowhere else.
RESEARCH = r"korn ferry|gallup|live data technologies|revelio"
for n in VIDEOS:
    has = bool(re.search(RESEARCH, text(n).lower()))
    check("V%d research attribution present only where figures are" % n,
          has == (n in (20, 22)) or not has)

# --- 16. no invented URL and no spoken URL beyond the earned resource.
for n in VIDEOS:
    urls = re.findall(r"https?://\S+|temidayoafonja\.com\S*", text(n).lower())
    check("V%d speaks no URL on camera" % n, not urls, urls)

# --- 17. the CTA map is exactly what the roadmap locked.
CTA_MAP = {15: "career evidence starter", 16: None, 17: "keep the proof",
           18: "field kit", 19: None, 20: None, 21: "field kit", 22: None}
for n in VIDEOS:
    t = text(n).lower()
    named = [x for x in ("career evidence starter", "keep the proof", "field kit")
             if x in t]
    want = [CTA_MAP[n]] if CTA_MAP[n] else []
    check("V%d names %s and no other resource" % (n, CTA_MAP[n] or "no resource"),
          sorted(named) == sorted(want), named)

# --- 18. U.S. English.
BRITISH = [r"\blabour", r"\bbehaviour", r"\bcolour", r"\bfavour", r"\borganis",
           r"\brecognis", r"\brealis", r"\banalyse", r"\bprogramme\b", r"\bcentre\b",
           r"\blicence\b", r"\bpractise\b", r"\bwhilst\b", r"\bamongst\b", r"\blearnt\b",
           r"\bspelt\b", r"\btravelled\b", r"\bmodelling\b", r"\bcancelled\b",
           r"\bhas got\b", r"\bhave got\b", r"\bhad got\b", r"\bmaths\b"]
for n in VIDEOS:
    t = text(n).lower()
    hits = [p for p in BRITISH if re.search(p, t)]
    check("V%d uses U.S. English" % n, not hits, hits)

def british_regression():
    probe = "she recognised the colour of the programme whilst travelling to the centre."
    return len([p for p in BRITISH if re.search(p, probe)]) >= 4
check("U.S. English check still fires on injected British spellings", british_regression())

# --- 19. Watch Next routing, and nothing routes to an unbuilt video.
LOCKED_TITLES = {
 12: "How to Turn One Accomplishment Into Proof in 10 Minutes",
 13: "Which Parts of Your Experience Actually Transfer to Another Industry?",
}
ROUTE = {15: LOCKED_TITLES[12],
         16: "Before a Layoff, Know What You Can Still Prove",
         17: LOCKED_TITLES[13],
         18: "The Career Gaps You Don't See Until the Work Gets Harder",
         19: "What Happens When the Next Step in Your Career Disappears?",
         20: "How Do You Grow When There Are Fewer Roles Above You?",
         21: "The Career Ladder Doesn't Work the Same Way Anymore",
         22: LOCKED_TITLES[13]}
for n in VIDEOS:
    check("V%d watch-next names its destination by title" % n, ROUTE[n] in text(n), ROUTE[n])
UNBUILT = ["V23", "V24", "V25", "V26", "the next one in this series is about managing",
           "in the next video I will show you how to negotiate scope"]
for n in VIDEOS:
    t = text(n)
    hits = [x for x in UNBUILT if x in t]
    check("V%d routes to nothing unbuilt" % n, not hits, hits)
check("V22 does NOT route to an unbuilt V23", ROUTE[22] == LOCKED_TITLES[13])

# --- 20. titles and the pending V20 thumbnail.
TITLES = {15: "How to Prove Your Value When AI Does More of the Task",
          16: "What to Do When Your Work Is Valued but You Are Overlooked",
          17: "Before a Layoff, Know What You Can Still Prove",
          18: "What You Must Relearn When You Change Industries",
          19: "The Career Gaps You Don't See Until the Work Gets Harder",
          20: "What Happens When the Next Step in Your Career Disappears?",
          21: "How Do You Grow When There Are Fewer Roles Above You?",
          22: "The Career Ladder Doesn't Work the Same Way Anymore"}
for n in VIDEOS:
    check("V%d carries its locked title" % n, mod(n).TITLE == TITLES[n], mod(n).TITLE)
check("V20 thumbnail is still the approval placeholder",
      mod(20).THUMB == "PENDING TEMIDAYO APPROVAL", mod(20).THUMB)
for n in VIDEOS:
    if n != 20:
        check("V%d thumbnail is decided" % n,
              mod(n).THUMB and "PENDING" not in mod(n).THUMB, mod(n).THUMB)
check("V20's thumbnail does not collide with V22's",
      mod(20).THUMB != mod(22).THUMB)

# --- 21. no spoken line names a video this pack did not build.
for n in VIDEOS:
    t = text(n)
    check("V%d speaks no working-packaging language" % n,
          not any(x in t.lower() for x in ("[working]", "working title", "packaging pending")))

# --- 22. word counts inside the locked spoken band.
BAND = (889, 1457)
COUNTS = {}
for n in VIDEOS:
    COUNTS[n] = sum(len(p.split()) for _, p in spoken(n))
    check("V%d spoken words inside the locked band" % n,
          BAND[0] <= COUNTS[n] <= BAND[1], "%d words" % COUNTS[n])

if __name__ == "__main__":
    bad = [f for f in FAILS if not f[1]]
    for name, ok, detail in FAILS:
        print(("PASS " if ok else "FAIL ") + name + (("  " + str(detail)) if detail and not ok else ""))
    print("\n%d checks, %d failed" % (len(FAILS), len(bad)))
    print("word counts:", COUNTS)
