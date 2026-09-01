# -*- coding: utf-8 -*-
"""Canonical source verification for the Video 1 v3.1 patch.

The v3.1 spoken script is DERIVED from the approved v3.0 canonical
(Video_1_Code_Prompt_HIT_Final.txt) by replacing only the CTA slide marker and
the three-paragraph CTA block. This proves (a) the derivation touched nothing
else, and (b) the four delivered script files match that derivation literally.
"""
from docx import Document

C = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
     "b9cd8431-Video_1_Code_Prompt_HIT_Final.txt")
txt = open(C, encoding="utf-8").read()
b = txt.index("BEGIN APPROVED VIDEO 1 SCRIPT") + len("BEGIN APPROVED VIDEO 1 SCRIPT")
e = txt.index("END APPROVED VIDEO 1 SCRIPT")
v30 = [l.strip() for l in txt[b:e].split("\n\n") if l.strip()]

OLD_MARKER = "[SLIDE: Capability Formation Field Kit]"
NEW_MARKER = "[SLIDE: Career Evidence Starter]"
OLD_BLOCK = [
 "If these questions show you that you need a fuller read of what your current work is building and how portable it may be, the Capability Formation Field Kit gives you a private, evidence-led assessment using the last 90 days of your actual work.",
 "It helps you see what is growing, what appears portable and what may need attention before your next move.",
 "You can find it at temidayoafonja.com/fieldkit.",
]
NEW_BLOCK = [
 "If you want to try this on one real accomplishment, I made a free Career Evidence Starter.",
 "It takes about 10 to 15 focused minutes and helps you turn one piece of work into a portable Proof Line.",
 "I\u2019ve linked it below.",
]
i = v30.index(OLD_MARKER)
canon = v30[:i] + [NEW_MARKER] + NEW_BLOCK + v30[i + 4:]
canon_spoken = [l for l in canon if not l.startswith("[SLIDE:")]
canon_marks = [l for l in canon if l.startswith("[SLIDE:")]

LF = "Video_1_HIT_FINAL/LONG_FORM/"
tel = open(LF + "Video1TeleprompterScriptwithslidemarkers_HIT_v3.1.txt", encoding="utf-8").read()
rd = open(LF + "Video1ReadingScriptnomarkers_HIT_v3.1.txt", encoding="utf-8").read()
tel_paras = [p.strip() for p in tel.split("\n\n") if p.strip()][1:]
tel_spoken = [p for p in tel_paras if not p.startswith("SLIDE  \u2014")]
tel_marks = [p for p in tel_paras if p.startswith("SLIDE  \u2014")]
rd_paras = [p.strip() for p in rd.split("\n\n") if p.strip()]

def docx_paras(path, drop):
    return [p.text.strip() for p in Document(path).paragraphs if p.text.strip()][drop:]
tel_docx = [p for p in docx_paras(LF + "Video1TeleprompterScriptwithslidemarkers_HIT_v3.1.docx", 4)
            if not p.startswith("SLIDE  \u2014")]
rd_docx = docx_paras(LF + "Video1ReadingScriptnomarkers_HIT_v3.1.docx", 4)

res = []
def cmp(name, a, b_):
    ok = a == b_
    res.append(ok)
    print("%-54s %s  (%d vs %d)" % (name, "PASS" if ok else "FAIL", len(a), len(b_)))
    if not ok:
        for k, (x, y) in enumerate(zip(a, b_)):
            if x != y:
                print("   first diff at %d:\n    A: %r\n    B: %r" % (k, x, y)); break
    return ok

# (a) the derivation changed only the marker and the three CTA paragraphs
diff = [k for k, (x, y) in enumerate(zip(v30, canon)) if x != y]
only_cta = (len(v30) == len(canon) and diff == [i, i + 1, i + 2, i + 3])
res.append(only_cta)
print("%-54s %s  (indices %s)" % ("only the CTA marker + 3 paragraphs differ from v3.0",
                                  "PASS" if only_cta else "FAIL", diff))
cmp("patched canonical == teleprompter TXT minus markers", canon_spoken, tel_spoken)
cmp("patched canonical == reading TXT", canon_spoken, rd_paras)
cmp("teleprompter TXT minus markers == reading TXT", tel_spoken, rd_paras)
cmp("teleprompter DOCX == teleprompter TXT", tel_docx, tel_spoken)
cmp("reading DOCX == reading TXT", rd_docx, rd_paras)
cmp("marker names and order",
    [m[len("[SLIDE:"):-1].strip() for m in canon_marks],
    [m[len("SLIDE  \u2014"):].strip() for m in tel_marks])
cmp("marker positions",
    [k for k, l in enumerate(canon) if l.startswith("[SLIDE:")],
    [k for k, p in enumerate(tel_paras) if p.startswith("SLIDE  \u2014")])

allc = "".join(canon_spoken)
print("\ncurly apostrophes %d | curly quotes %d | em dashes %d | en dashes %d"
      % (allc.count("\u2019"), allc.count("\u201c") + allc.count("\u201d"),
         allc.count("\u2014"), allc.count("\u2013")))
print("markers: %d | spoken paragraphs: %d | spoken words: %d"
      % (len(canon_marks), len(canon_spoken), sum(len(x.split()) for x in canon_spoken)))
print("\nCANONICAL SOURCE VERIFICATION: %s" % ("PASS" if all(res) else "FAIL"))
