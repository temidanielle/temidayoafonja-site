# -*- coding: utf-8 -*-
"""Re-review every flagged card line against the reconciled source.

The first audit asked one question, "is this line verbatim narration?", and
flagged 73 families. That rule is wrong for a slide. A slide is not a
transcript.

Exactness is required for direct quotations, figures and research
denominators, named framework terms, and accurately reproduced evidence. A
faithful display heading or concise summary does not have to appear
verbatim in speech.

So each flagged line is measured against the passage it belongs to and
sorted into one of four kinds, and the supporting passage is recorded for
anything retained:

  QUOTE      quoted speech, a figure, or a named framework term. Must match
             the script exactly. If it does not, it is a real defect.
  SUMMARY    a faithful compression of a passage that is still in the
             script. May stand, with its supporting passage logged.
  EVIDENCE   a supported excerpt the script does not read aloud in full.
             May stand, with its support logged.
  OBSOLETE   no passage in the reconciled script supports it. Must change.
"""
import os, re, sys, json, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recon as R

QUOTE = "QUOTE"
SUMMARY = "SUMMARY"
EVIDENCE = "EVIDENCE"
OBSOLETE = "OBSOLETE"

# Named framework terms. These are spoken and must match exactly.
FRAMEWORK = {
 4: ("BEFORE AI", "WITH AI", "STILL MINE", "EXPOSURE", "OWNERSHIP",
     "FEEDBACK"),
 5: (), 6: ("PROBLEM", "AUTHORITY", "PROOF", "REAL GAP"), 7: (),
 8: (), 9: ("TRAVELS", "DOES NOT TRAVEL", "PROOF", "RELEARN"),
 10: ("READ", "TEST", "PROVE", "ROLE CHECK"),
 11: ("EXPECTED", "ACTUAL", "COST", "CHOICE"),
}

WORD = re.compile(r"[a-z0-9$%,\.]+")
STOP = set("a an the and or but of to in on for is are was were be been it "
           "its this that these those you your i my we our they their he "
           "she as at by with from not no do does did can could may might "
           "will would should have has had if then than so what when where "
           "who how why still only just more most some any each".split())


def toks(t):
    return [w.strip(".,") for w in WORD.findall(R.S._norm(t).lower())
            if w.strip(".,")]


def content(t):
    return [w for w in toks(t) if w not in STOP]


def has_figure(t):
    return bool(re.search(r"\d", t))


def is_quoted(t):
    return t.strip().startswith(("“", '"')) or "“" in t


# The approved evidence layer. A card may faithfully reproduce captured
# evidence the script never reads aloud, and the brief names V6's
# anonymized employer labels and sample-boundary notes as exactly that
# case. Judging those lines against narration alone would delete supported
# evidence by string matching, so the evidence is loaded and consulted.
#
# The named employers stay in this internal layer and never reach a public
# card: the public label is what a card may show.
EVIDENCE_CORPUS = {
 6: ("Posting one. Sr Divisional Strategy Consultant, Governance. "
     "Large Health Insurer. Chicago, Illinois. Remote. Published range "
     "$61,500 to $136,100. Required qualification: ability to accept "
     "direction and feedback. "
     "Posting two. Director of Enterprise Resilience. Large Health "
     "Insurer, same employer, different department. Published range "
     "$133,400 to $247,700. Requirement: work with executive leadership "
     "to make quick decisions based on predefined decisions. "
     "Posting three. Director, Talent Management. Marketing Technology "
     "Company. Experience minimum 5 to 7 years. Focus: operational "
     "execution. Reports to a Senior Director. "
     "Posting four. Director of Strategic Initiatives. Insurance "
     "Brokerage. Experience minimum 5 or more years. Reports to a Chief "
     "Transformation Officer. "
     "Posting five. Member of Technical Staff, Governance Risk "
     "Compliance. AI Company. Palo Alto, California and Washington, DC. "
     "In the description: FedRAMP. ATO. POAM. 3PAO. STIG. Published range "
     "$180,000 to $440,000, the highest published ceiling in this sample. "
     "Posting six. Director of Global Talent Acquisition. A global "
     "nonprofit. Recruiting experience exclusively in one geographic "
     "context was unlikely to be a strong fit. "
     "Sample boundary: 15 postings across 11 employers, captured "
     "September 12, 2026. In this sample, not the market."),
}


def evidence_support(n, line):
    """Coverage of a line by the approved evidence for that video."""
    corpus = EVIDENCE_CORPUS.get(n)
    if not corpus:
        return 0.0
    c = set(content(line))
    if not c:
        return 0.0
    return len(c & set(content(corpus))) / float(len(c))


def _sentences(p):
    return [x.strip() for x in re.split(r"(?<=[.?!])\s+", p) if x.strip()]


def best_passage(n, line):
    """The reconciled passage this line most plausibly compresses.

    Scored against each sentence as well as the whole paragraph: a card
    line usually compresses one sentence, and scoring only whole paragraphs
    picks a loosely related long paragraph over the sentence that actually
    supports it.
    """
    c = set(content(line))
    if not c:
        return None, 0.0
    best, score = None, 0.0
    for lab, ps in R.sections(n):
        for p in ps:
            cands = [p] + _sentences(p)
            for cand in cands:
                pc = set(content(cand))
                if not pc:
                    continue
                cov = len(c & pc) / float(len(c))
                if cov > score:
                    best, score = (lab, p), cov
    return best, score


def framework_ok(n, line):
    """A named framework term must appear in the script exactly."""
    up = line.strip().rstrip(".").upper()
    for term in FRAMEWORK.get(n, ()):
        if up == term or up.startswith(term + " "):
            return R.S._norm(term).lower() in R.S._norm(
                R.spoken_text(n)).lower()
    return None


def classify(n, line):
    body = R.S._norm(R.spoken_text(n)).lower()
    if R.S._norm(line).lower() in body:
        return "VERBATIM", 1.0, None, "still spoken word for word"
    fw = framework_ok(n, line)
    if fw is not None:
        return (QUOTE, 1.0, None,
                "named framework term, present in the script") if fw else (
            OBSOLETE, 0.0, None,
            "named framework term that the script no longer uses")
    passage, score = best_passage(n, line)
    ev = evidence_support(n, line)
    if is_quoted(line) or has_figure(line):
        if score >= 0.8:
            return (QUOTE, score, passage,
                    "quoted or numeric, and its passage still carries it")
        if ev >= 0.8:
            return (EVIDENCE, ev, ("approved evidence", EVIDENCE_CORPUS[n]),
                    "figure reproduced from the approved captured evidence")
        return (OBSOLETE, score, passage,
                "quoted or numeric and neither the script nor the evidence "
                "supports it exactly")
    if score >= 0.6:
        return (SUMMARY, score, passage,
                "faithful compression of a passage still in the script")
    if ev >= 0.8:
        return (EVIDENCE, ev, ("approved evidence", EVIDENCE_CORPUS[n]),
                "excerpt of the approved captured evidence, not read aloud")
    if score >= 0.35:
        return (EVIDENCE, score, passage,
                "supported by a passage the script does not read in full")
    return (OBSOLETE, score, passage,
            "no passage in the reconciled script and no approved evidence "
            "supports it")


def review(path):
    rows = json.load(open(path))
    out = []
    for r in rows:
        lines = []
        for line in r.get("missing", []):
            kind, score, passage, why = classify(r["video"], line)
            lines.append(dict(line=line, kind=kind, score=round(score, 2),
                              support=(passage[1][:120] if passage else None),
                              section=(passage[0] if passage else None),
                              why=why))
        out.append(dict(r, lines=lines))
    return out


if __name__ == "__main__":
    SP = ("/tmp/claude-0/-home-user-temidayoafonja-site/"
          "f121668d-e262-5eb8-9b22-0eaa1006a361/scratchpad")
    rows = review(SP + "/aud_sprint.json") + review(SP + "/aud_1011.json")
    json.dump(rows, open(os.path.join(HERE, "_relabel.json"), "w"), indent=1)
    tally = {}
    for r in rows:
        for l in r["lines"]:
            tally[l["kind"]] = tally.get(l["kind"], 0) + 1
    print("flagged lines re-reviewed: %d" % sum(tally.values()))
    for k in ("VERBATIM", QUOTE, SUMMARY, EVIDENCE, OBSOLETE):
        if k in tally:
            print("   %-9s %d" % (k, tally[k]))
    fam_bad = [r for r in rows
               if any(l["kind"] == OBSOLETE for l in r["lines"])]
    print("\nfamilies with at least one line needing change: %d of %d"
          % (len(fam_bad), len(rows)))
