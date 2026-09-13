# -*- coding: utf-8 -*-
"""Spoken-word count for all 18 September 13 thought blocks, from the ZIP.

Counted from the original files as supplied, not from any working copy, so
the number cannot be an artifact of something this build did to them.

TOKENIZATION, STATED EXPLICITLY

A spoken word is a run of non-whitespace characters inside a BLOCK body.
Nothing else is counted:

  the document header lines               excluded
  the recording direction line            excluded
  [NOT SPOKEN] section labels             excluded
  the "BLOCK n" label itself              excluded

A hyphenated compound such as "financial-crimes" is ONE word, which is how
Word and every whitespace tokenizer count it. Splitting hyphens instead
gives 1379 for Video 14 and splitting on letter runs gives 1382, so neither
explains a one-word difference.
"""
import os, re, sys, hashlib, zipfile
from docx import Document

ZIP = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
       "6701e1a7-YouTube_V4-V21_Story_Led_Conversational_Scripts_and_"
       "Thought_Blocks_FINAL_1.zip")
NAME = "Video_%d_Thought_Block_Recording_Copy_Story_Led.docx"

# The counts stated in the September 13 change log.
CHANGE_LOG = {4: 874, 5: 867, 6: 1340, 7: 1345, 8: 1413, 9: 1278, 10: 1229,
              11: 1302, 12: 1299, 13: 1377, 14: 1365, 15: 1493, 16: 1311,
              17: 1432, 18: 1400, 19: 1577, 20: 1413, 21: 1437}


def blocks_from(fh):
    d = Document(fh)
    flat = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    out, skipped = [], []
    for t in flat:
        if t.startswith("[NOT SPOKEN]"):
            continue
        m = re.match(r"^BLOCK\s+(\d+)\s*(?:\n(.*))?$", t, re.S)
        if m:
            out.append((int(m.group(1)), (m.group(2) or "").strip()))
        elif t.startswith("BLOCK"):
            skipped.append(t)
    return out, skipped


def survey():
    rows = []
    with zipfile.ZipFile(ZIP) as z:
        for n in range(4, 22):
            member = next(x for x in z.namelist()
                          if x.endswith(NAME % n))
            raw = z.read(member)
            import io
            blocks, skipped = blocks_from(io.BytesIO(raw))
            words = sum(len(b.split()) for _, b in blocks)
            nums = [i for i, _ in blocks]
            rows.append(dict(
                video=n, words=words, blocks=len(blocks),
                logged=CHANGE_LOG[n], sha=hashlib.sha256(raw).hexdigest(),
                gaps=[i for i in range(min(nums), max(nums) + 1)
                      if i not in nums],
                empty=[i for i, b in blocks if not b],
                unparsed=skipped))
    return rows


if __name__ == "__main__":
    rows = survey()
    print("%-4s %-8s %-8s %-9s %-7s %s"
          % ("V", "WORDS", "LOGGED", "AGREES", "BLOCKS", "SHA-256 (16)"))
    for r in rows:
        print("%-4s %-8d %-8d %-9s %-7d %s"
              % ("V%d" % r["video"], r["words"], r["logged"],
                 "yes" if r["words"] == r["logged"] else
                 "NO %+d" % (r["words"] - r["logged"]),
                 r["blocks"], r["sha"][:16]))
    bad = [r for r in rows if r["gaps"] or r["empty"] or r["unparsed"]]
    print("\nblocks with a numbering gap, an empty body, or an unparsed "
          "label: %d" % len(bad))
    off = [r for r in rows if r["words"] != r["logged"]]
    print("videos where the count differs from the change log: %s"
          % ([r["video"] for r in off] or "none"))
