# -*- coding: utf-8 -*-
"""Apply the five authorized source-language corrections.

The supplied _source tree is never edited. This writes a corrected source
layer beside it and keeps a byte-identical copy of every pre-correction
file, so the change is auditable in both directions.

Each sentence is replaced in place inside a single run, so everything else
in the document, including the Thought-Block block labels and the
[NOT SPOKEN] markers, survives untouched. That is what makes the
regenerated Thought-Block copy match its corrected script exactly.
"""
import os, sys, shutil, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from docx import Document
import sprint as S

SRC = os.path.join(OUT, "_source")
DST = os.path.join(OUT, "_source_v2")
KEEP = os.path.join(DST, "_pre_correction")

# (new public number, current sentence, authorized replacement)
EDITS = (
 (6, "Then ask the question people sometimes skip because they want the "
     "move to work:",
     "Then ask the question that is easy to skip when you want the move "
     "to work:"),
 (8, "This happens because most people treat evidence like something they "
     "will collect later.",
     "This happens when evidence gets treated like something to collect "
     "later."),
 (8, "People wait because collecting evidence can feel self-promotional "
     "while you are employed.",
     "Collecting evidence while you are employed can feel self-promotional, "
     "which makes it easy to put off."),
 (9, "When people talk about changing industries, they usually ask one "
     "question:",
     "When you think about changing industries, the obvious first question "
     "is:"),
 (9, "And then there is the part people sometimes want to skip.",
     "And then there is the harder part of the audit."),
)
CORRECTED = sorted({n for n, _, _ in EDITS})


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def replace(path, old, new):
    """Swap one sentence inside the single run that holds it."""
    d = Document(path)
    hits = 0
    for p in d.paragraphs:
        for r in p.runs:
            if old in r.text:
                r.text = r.text.replace(old, new)
                hits += 1
    if hits != 1:
        raise SystemExit("%s: expected one occurrence of %r, found %d"
                         % (os.path.basename(path), old[:40], hits))
    d.save(path)


def main():
    for d in (DST, KEEP):
        if os.path.isdir(d):
            shutil.rmtree(d)
    for sub in ("sprint_scripts", "thought_blocks"):
        shutil.copytree(os.path.join(SRC, sub), os.path.join(DST, sub))
        shutil.copytree(os.path.join(SRC, sub), os.path.join(KEEP, sub))

    for n, old, new in EDITS:
        for kind, path in (("script", S.script_path(n)),
                           ("block", S.block_path(n))):
            p = path.replace(os.sep + "_source" + os.sep,
                             os.sep + "_source_v2" + os.sep)
            replace(p, old, new)
            print("  V%d %-6s  %s" % (n, kind, old[:52]))

    print("\ncorrected: %s      unchanged: %s"
          % (CORRECTED, [n for n in S.VIDEOS if n not in CORRECTED]))
    print("\nper-file hashes in the corrected layer")
    for n in S.VIDEOS:
        for kind, fn in (("script", S.script_path), ("block", S.block_path)):
            new = fn(n).replace(os.sep + "_source" + os.sep,
                                os.sep + "_source_v2" + os.sep)
            old = fn(n)
            a, b = sha256(old), sha256(new)
            tag = "corrected" if a != b else "byte-identical"
            print("  V%d %-6s %s  %s" % (n, kind, b, tag))
            if (n in CORRECTED) != (a != b):
                raise SystemExit("V%d %s changed unexpectedly" % (n, kind))
    print("\nonly the three corrected videos differ from the supplied source")


if __name__ == "__main__":
    main()
