# -*- coding: utf-8 -*-
"""Canonical source verification for Video 7, run in the same build pass.

Compares the approved script extracted from Video_7_Code_Prompt_HIT_Final.txt
against the four delivered script files, literally: every word, punctuation
mark, apostrophe, quotation mark, em dash, capitalisation, paragraph order and
marker name and position.
"""
from docx import Document

F = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
     "5b35ceab-Video_7_Code_Prompt_HIT_Final.txt")
txt = open(F, encoding="utf-8").read()
b = txt.index("BEGIN APPROVED VIDEO 7 SCRIPT") + len("BEGIN APPROVED VIDEO 7 SCRIPT")
e = txt.index("END APPROVED VIDEO 7 SCRIPT")
canon = [l.strip() for l in txt[b:e].split("\n\n") if l.strip()]
canon_spoken = [l for l in canon if not l.startswith("[SLIDE:")]
canon_marks = [l for l in canon if l.startswith("[SLIDE:")]

LF = "Video_7_HIT_FINAL/LONG_FORM/"
tel = open(LF + "Video7TeleprompterScriptwithslidemarkers_HIT_v2.0.txt",
           encoding="utf-8").read()
rd = open(LF + "Video7ReadingScriptnomarkers_HIT_v2.0.txt", encoding="utf-8").read()

# The TXT header is one blank-line-separated block of two lines.
tel_paras = [p.strip() for p in tel.split("\n\n") if p.strip()][1:]
tel_spoken = [p for p in tel_paras if not p.startswith("SLIDE  \u2014")]
tel_marks = [p for p in tel_paras if p.startswith("SLIDE  \u2014")]
rd_paras = [p.strip() for p in rd.split("\n\n") if p.strip()]

def docx_paras(path, drop_head):
    """Spoken paragraphs out of a script DOCX, minus its header block."""
    d = Document(path)
    ps = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    return ps[drop_head:]

# header: title / subtitle / lead-in note = 3 paragraphs in both script DOCX
tel_docx = docx_paras(LF + "Video7TeleprompterScriptwithslidemarkers_HIT_v2.0.docx", 4)
rd_docx = docx_paras(LF + "Video7ReadingScriptnomarkers_HIT_v2.0.docx", 4)
tel_docx_spoken = [p for p in tel_docx if not p.startswith("SLIDE  \u2014")]

results = []
def cmp(name, a, b):
    ok = a == b
    results.append((name, ok))
    print("%-52s %s  (%d vs %d)" % (name, "PASS" if ok else "FAIL", len(a), len(b)))
    if not ok:
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print("   first diff at %d:\n    A: %r\n    B: %r" % (i, x, y))
                break
        if len(a) != len(b):
            longer = a if len(a) > len(b) else b
            print("   extra: %r" % (longer[min(len(a), len(b)):][:2],))
    return ok

cmp("canonical spoken == teleprompter TXT minus markers", canon_spoken, tel_spoken)
cmp("canonical spoken == reading TXT", canon_spoken, rd_paras)
cmp("teleprompter TXT minus markers == reading TXT", tel_spoken, rd_paras)
cmp("teleprompter DOCX == teleprompter TXT", tel_docx_spoken, tel_spoken)
cmp("reading DOCX == reading TXT", rd_docx, rd_paras)
cmp("marker names and order",
    [m[len("[SLIDE:"):-1].strip() for m in canon_marks],
    [m[len("SLIDE  \u2014"):].strip() for m in tel_marks])
cmp("marker positions",
    [i for i, l in enumerate(canon) if l.startswith("[SLIDE:")],
    [i for i, p in enumerate(tel_paras) if p.startswith("SLIDE  \u2014")])

allc = "".join(canon_spoken)
print("\ncurly apostrophes %d | curly quotes %d | em dashes %d | en dashes %d"
      % (allc.count("\u2019"), allc.count("\u201c") + allc.count("\u201d"),
         allc.count("\u2014"), allc.count("\u2013")))
print("canonical spoken paragraphs: %d" % len(canon_spoken))
print("canonical spoken word count: %d" % sum(len(s.split()) for s in canon_spoken))
ok = all(r[1] for r in results)
print("\nCANONICAL SOURCE VERIFICATION: %s" % ("PASS" if ok else "FAIL"))
