# -*- coding: utf-8 -*-
"""Source-language integrity: unsupported audience-behavior phrasing.

Two sentences reached production from an approved source because they asserted
what a population of people does and why. This finds that shape and nothing
adjacent to it.

What counts as a finding: a sentence that states, as fact, what some group of
people does, feels, thinks or struggles with, without a bound on where the
claim comes from.

What does NOT count, because each is legitimate in this channel:
  quoted employer language    the posting's own words, in quotation marks
  bounded observation         tied to the sample, the postings, the research
  possibility                 may, might, can, could, some, sometimes, often
                              applied to a situation rather than to people
  viewer instruction          addressed to you, including "we" used to bring
                              the viewer alongside a named action
"""
import re

# The subject of an unsupported behavior claim.
GROUP = (r"(?:people|professionals|experienced professionals|candidates|"
         r"most people|many people|everyone|nobody|no one|we|you all|"
         r"applicants|job seekers|hiring managers|employers|recruiters|"
         r"men|women|workers|managers)")
# Verbs that assert an inner state or a habitual behavior.
BEHAVIOR = (r"(?:struggle|struggles|skip|skips|assume|assumes|think|thinks|"
            r"feel|feels|believe|believes|fear|fears|want|wants|avoid|"
            r"avoids|forget|forgets|tend|tends|undersell|undersells|"
            r"overestimate|overestimates|underestimate|underestimates|"
            r"fail|fails|never|always)")
CLAIM = re.compile(
    r"\b%s\b[^.?!]{0,40}?\b%s\b" % (GROUP, BEHAVIOR), re.I)

# A bound that makes an observation legitimate.
BOUND = re.compile(
    r"\b(in the (job )?postings?|in the sample|of the \d+|\d+ of \d+|"
    r"i (read|studied|reviewed)|for this research|the postings i|"
    r"in that (same )?posting|one posting|the posting (said|says|states)|"
    r"this posting|the description|the requirement)\b", re.I)
# A possibility rather than an assertion. Frequency hedges are deliberately
# NOT here: "people sometimes skip this because they want the move to work"
# still asserts what people do and why, it just softens how often. Only a
# bound on where the claim comes from excuses that shape.
MODAL = re.compile(r"\b(may|might|could|would|can|whether|perhaps|maybe)\b",
                   re.I)
# Addressed to the viewer.
VIEWER = re.compile(r"\b(you|your|yours)\b", re.I)
QUOTED = re.compile(r"[\"“][^\"”]{6,}[\"”]")


def _sentences(text):
    for chunk in text.split("\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        for s in re.split(r"(?<=[.?!:])\s+", chunk):
            if s.strip():
                yield s.strip()


def findings(text):
    """[(sentence, matched phrase)] for unsupported behavior claims."""
    out = []
    for s in _sentences(text):
        m = CLAIM.search(s)
        if not m:
            continue
        span = s[max(0, m.start() - 60):m.end() + 60]
        if QUOTED.search(s) and m.start() > s.find('"') >= 0:
            continue
        if BOUND.search(span):
            continue
        if MODAL.search(s[:m.start()] + s[m.start():m.end()]):
            continue
        if VIEWER.search(s[:m.end()]):
            continue
        out.append((s, m.group(0)))
    return out


if __name__ == "__main__":
    import masters23b as M
    print("=== the corrected scripts")
    for n in M.VIDEOS:
        f = findings(M.spoken_text(n))
        print("V%d: %d finding(s)" % (n, len(f)))
        for s, hit in f:
            print("    %r  <- %r" % (s[:88], hit))
    print()
    print("=== the sentences this check exists for")
    for n, (old, new) in M.CORRECTIONS.items():
        print("V%d before: %d finding(s)  %r"
              % (n, len(findings(old)), old[:70]))
        print("V%d after : %d finding(s)  %r"
              % (n, len(findings(new)), new[:70]))
    LEGIT = [
      'In that same posting, one of the key verbs was "supporting."',
      "Several senior roles in the postings I studied clearly described "
      "support or execution postures.",
      "In the job postings I reviewed, employers often asked for more than "
      "outcomes.",
      "A new employer may care most about your judgment.",
      "You might assume a Director at that level owns every crisis decision.",
      "We are used to answering, “What were you responsible for?”",
      "It cannot tell you whether a manager would flex on a requirement, "
      "whether bias will shape the decision, or whether the team culture "
      "matches the posting.",
      "Employers said candidates whose recruiting experience was exclusively "
      "in one geographic context were unlikely to be a strong fit.",
      "Write four lines: Problem. Authority. Proof. Real gap.",
      "This method will not tell you who will get hired.",
      "In the sample, employers often wanted a mechanism alongside the "
      "result.",
      "One posting in the sample said candidates want a clearer scope.",
      "A manager might assume the title describes the authority.",
    ]
    print()
    print("=== must stay silent")
    for s_ in LEGIT:
        f = findings(s_)
        print("  %-7s %s" % ("FLAGS" if f else "silent", s_[:86]))
    print()
    print("=== must fire")
    VIOLATIONS = [
      "People often assume the title tells you the level.",
      "Most people skip this step.",
      "Experienced professionals struggle with this line.",
      "Candidates always want more authority than they had.",
      "Everyone forgets the before state.",
    ]
    for s_ in VIOLATIONS:
        f = findings(s_)
        print("  %-7s %s" % ("FIRES" if f else "SILENT", s_[:86]))

