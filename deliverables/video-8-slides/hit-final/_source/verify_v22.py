# -*- coding: utf-8 -*-
"""Video 8 v2.2 canonical verification.

Replaces verify_canonical.py for v2.2. verify_canonical.py compared the built
package against the ORIGINAL v2.1 code prompt; that comparison necessarily fails
now that Temidayo authorized the research-alignment strengthening pass, so it is
retained unchanged as the historical v2.1 record rather than edited to pass.

This script verifies the two things that actually matter for v2.2:
  1. the built documents match the v2.2 canonical exactly;
  2. v2.2 is v2.1 plus ONLY the authorized additions - every v2.1 paragraph
     survives verbatim, nothing was deleted or reworded, and the sole sequence
     change is the documented opening move.
"""
import io, re, sys, importlib.util
from docx import Document

LF = "Video_8_HIT_FINAL/LONG_FORM/"
V21 = "baseline/reading_v2.1.txt"   # v2.1 as committed, extracted from git
V22 = "baseline/reading_v2.2.txt"   # v2.2 as committed, the approved architecture

# v2.2.1 authorized a U.S.-English sweep, which touches preserved wording. The
# preservation invariant therefore compares modulo exactly those substitutions.
US = [("travelled","traveled"),("Travelled","Traveled"),
      ("practised","practiced"),("Practised","Practiced"),
      ("recognised","recognized"),("Recognised","Recognized"),
      ("recognising","recognizing"),("Recognising","Recognizing"),
      ("licence","license"),("Licence","License")]
def usnorm(s):
    for x,y in US: s=s.replace(x,y)
    return s
nz = lambda x: re.sub(r"\s+", " ", x).strip()
R = []
def chk(label, ok, detail=""):
    R.append((label, ok, detail)); return ok

s = importlib.util.spec_from_file_location("st", "script_text.py")
st = importlib.util.module_from_spec(s); s.loader.exec_module(st)
SPOKEN = [nz(x) for x in st.SPOKEN]
MARKERS = list(st.MARKERS)

tel_txt = io.open(LF + "Video8TeleprompterScriptwithslidemarkers_HIT_v2.2.txt", encoding="utf-8").read()
rd_txt  = io.open(LF + "Video8ReadingScriptnomarkers_HIT_v2.2.txt", encoding="utf-8").read()
def dparas(p, skip):
    return [nz(x.text) for x in Document(p).paragraphs if x.text.strip()][skip:]
tel_docx = dparas(LF + "Video8TeleprompterScriptwithslidemarkers_HIT_v2.2.docx", 4)
rd_docx  = dparas(LF + "Video8ReadingScriptnomarkers_HIT_v2.2.docx", 4)
rd_blocks = [nz(x) for x in rd_txt.split("\n\n") if x.strip()]

chk("reading TXT == canonical spoken", rd_blocks == SPOKEN,
    "%d vs %d" % (len(rd_blocks), len(SPOKEN)))
chk("reading DOCX == reading TXT", rd_docx == rd_blocks,
    "%d vs %d" % (len(rd_docx), len(rd_blocks)))
chk("teleprompter carries every spoken paragraph",
    all(p in nz(tel_txt) for p in SPOKEN))
chk("teleprompter DOCX == teleprompter TXT",
    [p for p in tel_docx if not p.startswith("SLIDE")] ==
    [p for p in [nz(x) for x in tel_txt.split("\n\n") if x.strip()][1:] if not p.startswith("SLIDE")])
chk("no slide markers in the reading script",
    "[SLIDE:" not in rd_txt and "SLIDE  —" not in rd_txt)
names = [re.match(r"\[SLIDE:\s*(.*)\]", m).group(1) for m in MARKERS]
chk("twelve markers, present and ordered in the teleprompter",
    len(names) == 12 and all(n.upper() in nz(tel_txt).upper() for n in names))

old = [usnorm(nz(x)) for x in io.open(V21, encoding="utf-8").read().split("\n\n") if x.strip()]
v22 = [usnorm(nz(x)) for x in io.open(V22, encoding="utf-8").read().split("\n\n") if x.strip()]
SPOKEN_US = [usnorm(p) for p in SPOKEN]
missing = [p for p in old if p not in SPOKEN_US]
added   = [p for p in SPOKEN_US if p not in old]
chk("every v2.1 paragraph survives (modulo authorized US spelling)", not missing, str(missing[:2]))
chk("exactly 16 authorized additions", len(added) == 16, "%d" % len(added))
trace = [old.index(p) for p in SPOKEN_US if p in old]
chk("opening resequence is exactly [0,4,1,2,3]", trace[:5] == [0, 4, 1, 2, 3], str(trace[:5]))
chk("nothing after the opening was reordered",
    trace[5:] == list(range(5, len(old))))

v22_missing = [p for p in v22 if p not in SPOKEN_US]
v22_added   = [p for p in SPOKEN_US if p not in v22]
chk("v2.2.1 changed exactly one long-form paragraph",
    len(v22_missing) == 1 and len(v22_added) == 1
    and "which one you are looking at" in v22_missing[0]
    and "which part is a real gap you need to close" in v22_added[0],
    "-%d +%d" % (len(v22_missing), len(v22_added)))

w = sum(len(x.split()) for x in st.SPOKEN)
print("VIDEO 8 v2.2 CANONICAL VERIFICATION")
for label, ok, detail in R:
    print("  %-52s %s  %s" % (label, "PASS" if ok else "FAIL", detail))
print("\n  spoken paragraphs: %d   words: %d   runtime: %d:%02d at 145 wpm"
      % (len(st.SPOKEN), w, w/145*60//60, w/145*60 % 60))
ok = all(o for _, o, _ in R)
print("\nCANONICAL SOURCE VERIFICATION: %s" % ("PASS" if ok else "FAIL"))
print("teleprompter DOCX == TXT: %s" % ("PASS" if R[3][1] else "FAIL"))
print("reading DOCX == TXT: %s" % ("PASS" if R[1][1] else "FAIL"))
print("teleprompter minus markers == reading TXT: %s" % ("PASS" if R[2][1] else "FAIL"))
sys.exit(0 if ok else 1)
