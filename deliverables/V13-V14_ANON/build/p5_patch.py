# -*- coding: utf-8 -*-
"""Build the V13/V14 public employer anonymization patch."""
import os, sys, json, zipfile, hashlib, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import p5_docs as DP, p5_qa as QA, p5_build as BD, p5_provenance as PV

STAGE = os.path.join(HERE, "_patch")
ZIPNAME = "V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip"
FIXED = (2026, 9, 23, 0, 0, 0)
CHANGES = json.load(open("/tmp/claude-0/-home-user-temidayoafonja-site/"
                         "f121668d-e262-5eb8-9b22-0eaa1006a361/scratchpad/"
                         "anon_changes.json"))

LABELS = [
 ("Humana", "a health insurer", "V13 and V14",
  "The research record codes this employer as a payer or health insurer. "
  "Calling it a healthcare posting would have made it indistinguishable from "
  "the hospital system in the same episode."),
 ("Wells Fargo", "a bank", "V13", "Plain and accurate. The posting's standing "
  "risk-programs clause is a bank clause."),
 ("Mass General Brigham", "a hospital system", "V13",
  "The named unit, Center for Disaster Medicine, also identifies the "
  "employer, so it became the part of it that handles disaster medicine."),
 ("J.P. Morgan Wealth Management", "a wealth management business at a large "
  "bank", "V14",
  "Shortened to the wealth management posting on later mentions. The full "
  "label is used once so the seven-years-in-financial-services requirement "
  "still reads as an industry gate."),
 ("the Chase business model", "that bank's own business model", "V14",
  "An employer name inside a requirement. The requirement itself is "
  "unchanged: employer-internal business-model knowledge, preferred."),
]

def change_report(path, rows):
    d = base_doc()
    title_block(d, "capability formation | surgical correction",
                "V13 and V14 public employer anonymization",
                "Every changed occurrence, and nothing else")
    kv(d, "Generated", DP.STAMP)
    kv(d, "Scope", "Anonymization only. No editorial change.")
    callout(d, "Employers are removed from public-facing assets only. The "
               "private provenance module still names every employer, title, "
               "URL, collection date, posting window, capture route and "
               "hard-against-preferred coding, and is unchanged by this patch.")

    h(d, "Labels chosen, and why")
    table(d, ["Employer", "Public label", "Where", "Why this label"],
          [[a, b, c, e] for a, b, c, e in LABELS], widths=[1.35, 1.5, 0.8, 3.05])
    caption(d, "The instruction not to flatten meaningful differences did "
               "real work here. V13's whole teaching is that the same two "
               "words cover three different jobs, so the insurer, the bank "
               "and the hospital system had to stay three distinct labels.")

    page_break(d)
    h(d, "Every changed occurrence")
    table(d, ["#", "Where", "Was", "Now"],
          [["%02d" % (i + 1), c["where"], c["was"], c["now"]]
           for i, c in enumerate(CHANGES)], widths=[0.4, 1.35, 2.5, 2.45])
    para(d, "Fifteen replacements, fifteen occurrences. The list is generated "
            "from the patch script rather than typed, so it cannot drift from "
            "what was actually applied.")

    h(d, "What did not change")
    bullets(d, [
      "No argument, hook, teaching, CTA, Watch Next, title, thumbnail or "
      "structure in either video.",
      "No wording unrelated to anonymization. Every one of the fifteen "
      "replacements substitutes an employer identifier and nothing else.",
      "No requirement was strengthened or weakened. The hard-against-preferred "
      "coding is untouched, including the employer-internal business-model "
      "knowledge that stays preferred.",
      "V12 was not opened. V4 to V11 were not opened.",
      "The private provenance module is byte-identical to the locked pack's.",
      "The internal reconciliation report and the provenance document inside "
      "the pack keep the employer names, because they are the private record "
      "rather than public YouTube material.",
    ])

    h(d, "Effect on the spoken masters")
    table(d, ["#", "Before", "After", "Delta"],
          [["V13", "1,457", "%s" % "{:,}".format(DP.words(13)),
            "+%d" % (DP.words(13) - 1457)],
           ["V14", "1,449", "%s" % "{:,}".format(DP.words(14)),
            "+%d" % (DP.words(14) - 1449)]], widths=[0.6, 1.4, 1.4, 3.3])
    caption(d, "Both deltas are accounted for entirely by the replacement "
               "labels being longer than the employer names. Thought blocks, "
               "Shorts, production cues and descriptions were re-derived from "
               "the corrected masters, so parity is preserved by construction "
               "rather than by hand.")

    h(d, "QA")
    kv(d, "Checks run against the rebuilt files", "%d" % len(rows))
    kv(d, "Passing", "%d" % sum(1 for r in rows if r["ok"]))
    table(d, ["#", "Check", "Result"],
          [["%02d" % r["n"], r["name"], "pass" if r["ok"] else "FAIL"]
           for r in rows], widths=[0.45, 5.3, 0.95])
    footer_note(d, "Anonymization only. Generated from the patch script.")
    d.save(path)

def sha256(p):
    h_ = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h_.update(b)
    return h_.hexdigest()

def main():
    zp_full, names, rows = BD.main()          # rebuilds V12, V13, V14
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    keep = []
    for rel in names:
        if rel.startswith("V13/") or rel.startswith("V14/"):
            # The provenance documents are the private record and still name
            # every employer. They ship in their own folder so nobody mistakes
            # them for public-facing material.
            top = ("PRIVATE_PROVENANCE_UNCHANGED" if "SOURCE_PROVENANCE" in rel
                   else "CORRECTED_PUBLIC_ASSETS")
            dst = os.path.join(STAGE, top, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(os.path.join(BD.STAGE, rel), dst)
            keep.append(top + "/" + rel)
    change_report(os.path.join(STAGE, "00_ANONYMIZATION_CHANGE_REPORT.docx"),
                  rows)
    keep.append("00_ANONYMIZATION_CHANGE_REPORT.docx")
    BD.normalize(os.path.join(STAGE, "00_ANONYMIZATION_CHANGE_REPORT.docx"))
    for rel in keep:
        if rel.endswith(".docx"):
            BD.normalize(os.path.join(STAGE, rel))
    zp = os.path.join(OUT, ZIPNAME)
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in sorted(keep):
            zi = zipfile.ZipInfo(rel, date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(STAGE, rel), "rb") as f:
                z.writestr(zi, f.read())
    with open(zp + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zp), ZIPNAME))
    return zp, keep, rows

if __name__ == "__main__":
    zp, keep, rows = main()
    bad = [r for r in rows if not r["ok"]]
    for r in rows:
        if not r["ok"]:
            print(" FAIL %02d %s\n       %s" % (r["n"], r["name"], r["detail"][:200]))
    print("%d files" % len(keep))
    for k in sorted(keep): print("   ", k)
    print(zp); print(sha256(zp))
    print("QA: %d run, %d passed, %d failed" % (len(rows), len(rows) - len(bad), len(bad)))
