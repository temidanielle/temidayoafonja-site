#!/usr/bin/env python3
"""Content + structure QA for the Keep the Proof v1.0.1 PDFs."""
import sys, re, fitz

HB = sys.argv[1]; LG = sys.argv[2]

def load(path):
    d = fitz.open(path)
    pages = [d[i].get_text() for i in range(d.page_count)]
    # normalize whitespace so table-cell / justified line breaks don't hide phrases
    txt = re.sub(r"\s+", " ", "\n".join(pages))
    return d, txt, pages

fails = []
def check(cond, label):
    print(("PASS" if cond else "FAIL"), "-", label)
    if not cond: fails.append(label)

for name, path in [("HANDBOOK", HB), ("LEDGER", LG)]:
    d, txt, pages = load(path)
    print(f"\n===== {name}  ({path.split('/')[-1]}) =====")
    print("pages:", d.page_count, "| bookmarks:", len(d.get_toc()))
    # em dashes
    check("—" not in txt, "no em dash (U+2014) in customer-facing text")
    # cover text present
    check(len(pages[0].strip()) > 20, "cover page has visible text")
    # no unintended blank pages
    blanks = [i+1 for i,p in enumerate(pages) if len(p.strip()) < 3]
    check(len(blanks) == 0, f"no blank/near-empty pages (found: {blanks})")
    # resume spelling preserved (no accented forms)
    check("résumé" not in txt and "resumé" not in txt, "no accented resume spelling")
    # no stale $75 field kit
    check("$75" not in txt and "75 Field" not in txt, "no stale $75 reference")
    # no prohibited content
    # Prohibited *features* (scoring, states, maps, audits). The boundary page
    # legitimately names stay-or-leave as OUT of scope, so that phrase is allowed.
    for term in ["Optionality", "Career Portability Map", "Role Relevance Audit", "Four Career States",
                 "Density score", "the Depth Trap", "Density and Optionality", "AI Role Relevance"]:
        check(term not in txt, f"prohibited feature absent: {term!r}")
    # version stamp 1.0.1 present, 1.0.0 absent
    check("1.0.1" in txt, "version 1.0.1 stamped in visible copy")
    check("Version 1.0.0" not in txt, "no visible Version 1.0.0")
    # metadata version
    md = d.metadata or {}
    check("1.0.1" in (md.get("keywords") or ""), "PDF metadata keywords carry v1.0.1")

# handbook-specific content
d, txt, pages = load(HB)
print("\n===== HANDBOOK content specifics =====")
check("resume" in txt.lower(), "'resume' spelling present in handbook")
# permission rule consistency
for phrase in [
    "Permission comes before protection",
    "A secure personal device does not make information yours to retain",
    "Seek permission, use only what is already public, or leave it out",
    "Generalizing information does not create permission",
    "Never paste", ]:
    check(phrase in txt, f"permission phrase present: {phrase!r}")
# CARE tier no longer offers generalize as a solution
check("Generalize, seek permission" not in txt, "old CARE 'Generalize, seek permission' wording removed")
# author positioning
check("where talent decisions get made" in txt, "positioning 'where talent decisions get made' present")
check("decide what people are worth" not in txt, "'decide what people are worth' removed")
check("eighteen years" in txt and "18 years" not in txt, "'eighteen years' prose, no '18 years'")
check("a separate tool from The Density Group" in txt, "boundary 'separate tool from The Density Group'")
# verifier wording
check("Verifier role or permitted public reference" in txt, "verifier field wording present")
check("Do not store a colleague" in txt, "verifier helper 'do not store a colleague' present")
check("A person or public fact that could verify this" not in txt, "old verifier wording removed")
check("Name the permitted source or location" in txt, "permitted-evidence helper present")
# voice replacements
check("Evidence holds up when it gives someone else something concrete to examine" in txt, "voice: evidence-holds-up line present")
check("Evidence survives scrutiny" not in txt, "voice: old 'Evidence survives scrutiny' removed")
check("Effort is input. Outcome is evidence" not in txt, "voice: old 'Effort is input' removed")
check(txt.count("Permission comes first. Everything else is craft.") == 1, "'Permission comes first...' appears exactly once")
# six examples
for who in ["Devin", "Maya", "Theo", "Grace", "Priya", "Sam"]:
    check(who in txt, f"example present: {who}")
# twenty full-entry fields taught (labels)
for fld in ["Situation or need", "Why it mattered", "Actions taken", "People and functions involved",
            "Outcome or observable change", "Problem prevented", "Team result vs. your honest part",
            "Internal wording, before translation", "Portable-language version", "Confidentiality and permission check"]:
    check(fld in txt, f"full-entry field taught: {fld!r}")
# no internal 'page N' cross references that could go stale
import re
pagerefs = re.findall(r"\bpage\s+\d+\b", txt, re.I)
check(len(pagerefs) == 0, f"no hard 'page N' cross-references (found: {pagerefs})")

print("\n================ RESULT ================")
print("FAILURES:", len(fails))
for f in fails: print("  -", f)
sys.exit(1 if fails else 0)
