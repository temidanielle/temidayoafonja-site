# -*- coding: utf-8 -*-
"""Prove every narrowed check still fails against a genuine violation.

A check that was corrected for scope has to be shown firing, or the
correction cannot be told apart from switching it off.
"""
import os, shutil, tempfile, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qa23 as QA
import frames23 as F
import masters23 as M
import geocheck23 as G
from docx import Document

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def with_line(pkg, rel, text):
    """Copy the package and add one offending line to one document."""
    tmp = tempfile.mkdtemp()
    dst = os.path.join(tmp, os.path.basename(pkg))
    shutil.copytree(pkg, dst)
    p = os.path.join(dst, rel)
    d = Document(p)
    d.add_paragraph(text)
    d.save(p)
    return tmp, dst


CASES = [
 ("No labor-market generalization",
  "This is representative of the labor market and most employers write "
  "roles this way."),
 ("The ceiling claim is bounded to this sample",
  "That is the highest in the market."),
 ("No external branding, interface or icon set is used",
  "Add a progress bar and a quiz interface across the bottom of the card."),
 ("No music license, thumbnail result or performance claim",
  "We secured a music license for the bed and expect a click-through rate "
  "above nine percent."),
 ("No claim about who wrote the predefined decisions",
  "Somebody else made the predefined decisions before the incident."),
 ("The Central Time qualifier travels with the 7 or 8 a.m. figure",
  "That means recurring 7 or 8 a.m. meetings for anyone who takes the job."),
 ("Superseded packaging appears only where it is marked superseded",
  "How to Read a Job Description for What Actually Matters So Fast, It "
  "Feels Like Cheating"),
 ("U.S. English throughout what this build authored",
  "The colour system and the programme were organised for the team."),
 ("No em dashes in what this build authored",
  "The verb tells you the level — not the title."),
]


def main():
    n = 22
    pkg = os.path.join(PKG, "V22")
    geo, _, _, _ = G.check(n)
    base = {k: v for k, v, _ in QA.run(n, pkg, geo, _pngs(pkg))}
    bad_base = [k for k, v in base.items() if not v]
    print("clean package failures: %s" % (bad_base or "none"))
    fails = 0
    for name, line in CASES:
        tmp, dst = with_line(pkg, os.path.join(
            "07_Evidence", "Claim_Boundary_Notes.docx"), line)
        try:
            res = {k: v for k, v, _ in QA.run(n, dst, geo, _pngs(dst))}
            fired = not res.get(name, True)
            print("%-62s %s" % (name[:62], "FIRES" if fired else "SILENT"))
            fails += 0 if fired else 1
        finally:
            shutil.rmtree(tmp)
    print("\nchecks that stayed silent on a real violation: %d" % fails)
    return fails == 0


def _pngs(pkg):
    d = os.path.join(pkg, "04_Visual_Assets")
    return [os.path.join(d, f) for f in sorted(os.listdir(d))
            if f.endswith(".png")]


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
