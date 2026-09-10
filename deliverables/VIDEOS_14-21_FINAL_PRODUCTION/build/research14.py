# -*- coding: utf-8 -*-
"""Verify every Video 14 research claim against the supplied research archive.

Nothing about V14's numbers, examples or boundaries is taken on trust. Each
claim below is checked against the text of what-really-transfers-research.md
at build time, so a claim cannot survive in the package if the archive does
not support it.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters1421 as M


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("“", '"')
                  .replace("”", '"').replace("—", "-").replace("–", "-"))


# (claim, one or more fragments that must all appear in the archive)
CLAIMS = [
 ("28 postings retained",
  ["Retained | 28", "Every count and percentage below uses 28"]),
 ("10 healthcare, 10 financial services, 8 technology",
  ["Retained - healthcare | 10", "Retained - financial services | 10",
   "Retained - technology | 8"]),
 ("Collection date September 10, 2026",
  ["Collection date (all) | September 10, 2026"]),
 ("The target was 30 and was not reached",
  ["Target was 30 (10/10/10). Actual retained is **28**"]),
 ("Manage risk means a project risk register in one healthcare posting",
  ["At **Humana**, the Senior Project Manager runs a project risk register: "
   "if a risk is mishandled, a project slips"]),
 ("Manage risk means enterprise risk programs at one financial employer",
  ["Credit, Market, Financial Crimes, Operational, Regulatory Compliance"]),
 ("Manage risk means patient movement during an infectious-disease surge",
  ["helps run patient movement \"during infectious disease surge events",
   "Duty Officer during infectious-disease surge"]),
 ("One healthcare employer accepts limited content knowledge",
  ["comfortable working on new projects with limited knowledge/expertise of "
   "the content"]),
 ("One wealth-management posting gates on financial services experience",
  ["JPMorgan's Wealth Management PM requires 7+ years of financial services "
   "and lists project-management background as merely preferred"]),
 ("Same-industry experience is a hard gate in 6 of 28",
  ["HARD: 6/28", "direct same-industry experience is a hard gate in only 6 "
   "of 28 postings"]),
 ("The five shared capabilities",
  ["plan ownership, influence without authority, the mechanics of risk/issue "
   "management, executive governance communication, and delivery-method "
   "discipline"]),
 ("Governance means two different things",
  ["maintain a robust and auditable governance process",
   "lead a governance structure that drives effective executive "
   "decision-making"]),
 ("The sample cannot show two roles are interchangeable",
  ["It cannot show that any two of these roles are interchangeable"]),
 ("The sample cannot show a candidate would be hired",
  ["or that an adjacent-experience candidate would be interviewed, let alone "
   "hired"]),
 ("The sample is a convenience sample and not representative",
  ["It is not representative of any industry or of the US labor market",
   "are a convenience sample"]),
 ("Counts are counts within these 28 postings",
  ["Every count is a count *within these 28 postings*"]),
 ("Several postings are dated 2025 or early 2026 or came from mirrors",
  ["Several postings are dated 2025 or early 2026, or are captured from ATS "
   "mirrors rather than live employer pages"]),
 ("The number must be 28, never 30",
  ["The number must be 28, never 30. Do not use \"30.\""]),
 ("The question title is the recommended packaging",
  ["Which Parts of Your Experience Actually Transfer to Another Industry?"]),
 ("WHAT REALLY TRANSFERS? fits the evidence",
  ["Keep **\"WHAT REALLY TRANSFERS?\"** - it fits the evidence exactly"]),
]

EMPLOYERS_IN_MASTER = ["Humana", "Wells Fargo", "Mass General Brigham",
                       "JPMorgan"]


def verify():
    """Returns (rows, ok). Each row is (claim, supported, missing fragment)."""
    text = _norm(M.research_text())
    rows, ok = [], True
    for claim, frags in CLAIMS:
        missing = [f for f in frags if _norm(f) not in text]
        rows.append((claim, not missing, missing[0] if missing else ""))
        ok = ok and not missing
    return rows, ok


def employer_traceability():
    """Every employer the master's notes allow on screen must be in the
    archive."""
    text = M.research_text()
    return [(e, e in text) for e in EMPLOYERS_IN_MASTER]


def forbidden_in_package(units):
    """Claims that must appear nowhere in the V14 package."""
    bad = []
    for u in units:
        if re.search(r"\b30 (job descriptions|postings)\b", u, re.I):
            bad.append(("uses 30 rather than 28", u[:100]))
        if re.search(r"I Compared 30 Job Descriptions", u):
            bad.append(("restores the retired numerical title", u[:100]))
        if re.search(r"\b\d+(\.\d+)?\s*(%|percent)\b", u) and \
           re.search(r"employer|posting|sample|industry", u, re.I):
            bad.append(("converts the sample into a percentage", u[:100]))
        if re.search(r"would be hired|guarantees? (a )?(job|interview)|"
                     r"proves? that .{0,40}transfers?", u, re.I) and \
           not re.search(r"does not|cannot|not prove|no(t)? claim", u, re.I):
            bad.append(("overstates what the sample shows", u[:100]))
    return bad


if __name__ == "__main__":
    rows, ok = verify()
    for claim, good, miss in rows:
        print("%-5s %s" % ("OK" if good else "MISS", claim))
        if miss:
            print("       missing: %s" % miss[:100])
    print()
    for e, found in employer_traceability():
        print("%-5s %s traceable to the research archive"
              % ("OK" if found else "MISS", e))
    print("\nall claims supported:", ok)
