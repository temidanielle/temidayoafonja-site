# -*- coding: utf-8 -*-
"""Canonical verification for the Videos 4, 6 and 8 patch pass.

For each video this proves two things:
  (a) the derived script differs from its SOURCE ONLY in the paragraphs the
      PATCH authorises, and
  (b) the four delivered script files match that derivation literally.
"""
import sys
from docx import Document

B = "/tmp/patchpass/bundle/"

def source_paras(n):
    t = open(B + "SOURCE_Video_%s_Code_Prompt_HIT_Final.txt" % n, encoding="utf-8").read()
    a = t.index("BEGIN APPROVED VIDEO %s SCRIPT" % n) + len("BEGIN APPROVED VIDEO %s SCRIPT" % n)
    z = t.index("END APPROVED VIDEO %s SCRIPT" % n)
    return [l.strip() for l in t[a:z].split("\n\n") if l.strip()]

CFG = {
 "4": dict(root="/tmp/v4p", ver="v2.1", tel="Video4TeleprompterScriptwithslidemarkers_HIT_v2.1",
           rd="Video4ReadingScriptnomarkers_HIT_v2.1", markers=11, blocks=1,
           # The marker and the CTA block are ADJACENT in the script, so the
           # two authorised replacements form one merged 8 -> 4 diff block.
           expect=[
             ("replace",
              ["[SLIDE: Keep the Proof]",
               "And that is where Keep the Proof fits.",
               "If your career makes sense but the examples are hard to retrieve, Keep the Proof is a 60-minute career evidence system for capturing your work, your evidence and what that work shows while the context is still clear.",
               "It is not a tool for inventing a stronger story.",
               "It helps you preserve the proof behind the story you can actually support.",
               "Use only your own recollection and information you are permitted to retain.",
               "Do not take confidential, proprietary, customer, employee or employer-owned material.",
               "You can find Keep the Proof at temidayoafonja.com/keep-the-proof."],
              ["[SLIDE: Career Evidence Starter]",
               "If you want to try this on one real accomplishment, I made a free Career Evidence Starter.",
               "Set aside about 10 to 15 focused minutes and you will leave with one portable Proof Line.",
               "I\u2019ve linked it below."]),
           ]),
 "6": dict(root="/tmp/v6p", ver="v2.1", tel="Video6TeleprompterScriptwithslidemarkers_HIT_v2.1",
           rd="Video6ReadingScriptnomarkers_HIT_v2.1", markers=12, blocks=3,
           expect=[
             ("replace",
              ["Before you call more responsibility growth, check three things: did the problem get more complex, did your authority expand, and what did the work return to your career?"],
              ["Before you call more responsibility growth, run it through the CAR test: did the problem get more complex, did your authority expand, and what did the work return to your career?"]),
             ("replace", ["So use three tests.", "Complexity.", "Authority.", "Return."],
              ["I call this the CAR test: Complexity, Authority and Return."]),
             ("replace", ["Now put the three tests together."], ["Now put the CAR test together."]),
           ]),
 "8": dict(root="/tmp/v8p", ver="v2.1", tel="Video8TeleprompterScriptwithslidemarkers_HIT_v2.1",
           rd="Video8ReadingScriptnomarkers_HIT_v2.1", markers=12, blocks=3,
           expect=[
             ("replace", ["Capability. Context. Credential."],
              ["I think of these as the three Cs of an industry change: Capability, Context and Credential."]),
             ("replace", ["Here is the exercise I want you to do."],
              ["Here is how you apply the three Cs."]),
             ("replace", ["That is the balance."],
              ["That is the balance the three Cs are meant to protect."]),
           ]),
}

def docx_paras(p, drop):
    return [x.text.strip() for x in Document(p).paragraphs if x.text.strip()][drop:]

overall = True
for n, c in CFG.items():
    print("=" * 62)
    print("VIDEO %s" % n)
    sys.path.insert(0, c["root"])
    for m in ("script_text",):
        sys.modules.pop(m, None)
    import importlib
    st = importlib.import_module("script_text")
    importlib.reload(st)
    canon = st.LINES
    canon_spoken = [l for l in canon if not l.startswith("[SLIDE:")]
    canon_marks = [l for l in canon if l.startswith("[SLIDE:")]

    src = source_paras(n)
    # Enumerate the ACTUAL diff blocks. Videos 6 and 8 carry three separate
    # replacements, so a prefix/suffix span is not a valid test -- it would
    # report everything between the first and last edit as changed.
    import difflib
    sm = difflib.SequenceMatcher(a=src, b=canon, autojunk=False)
    blocks = [(tag, src[i1:i2], canon[j1:j2])
              for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]
    print("  authorised replacements expected: %d | diff blocks found: %d"
          % (c["blocks"], len(blocks)))
    for k, (tag, was, now) in enumerate(blocks, 1):
        print("     %d. %s  %d para -> %d para" % (k, tag, len(was), len(now)))
        print("        FROM %r" % (was[0][:66] if was else ""))
        print("        TO   %r" % (now[0][:66] if now else ""))
    exact = (len(blocks) == c["blocks"]
             and all((tag, was, now) == exp
                     for (tag, was, now), exp in zip(blocks, c["expect"])))
    overall &= exact
    print("  %-52s %s" % ("diff blocks match the authorised replacements",
                          "PASS" if exact else "FAIL"))

    LF = c["root"] + "/Video_%s_HIT_FINAL/LONG_FORM/" % n
    tel = open(LF + c["tel"] + ".txt", encoding="utf-8").read()
    rd = open(LF + c["rd"] + ".txt", encoding="utf-8").read()
    tp = [p.strip() for p in tel.split("\n\n") if p.strip()][1:]
    tel_spoken = [p for p in tp if not p.startswith("SLIDE  \u2014")]
    tel_marks = [p for p in tp if p.startswith("SLIDE  \u2014")]
    rd_paras = [p.strip() for p in rd.split("\n\n") if p.strip()]
    tel_docx = [p for p in docx_paras(LF + c["tel"] + ".docx", 4)
                if not p.startswith("SLIDE  \u2014")]
    rd_docx = docx_paras(LF + c["rd"] + ".docx", 4)

    def cmp(name, a, b):
        global overall
        ok = a == b
        overall &= ok
        print("  %-52s %s  (%d vs %d)" % (name, "PASS" if ok else "FAIL", len(a), len(b)))
        if not ok:
            for k, (x, y) in enumerate(zip(a, b)):
                if x != y:
                    print("     first diff %d:\n      A: %r\n      B: %r" % (k, x, y)); break

    cmp("patched canonical == teleprompter TXT minus markers", canon_spoken, tel_spoken)
    cmp("patched canonical == reading TXT", canon_spoken, rd_paras)
    cmp("teleprompter TXT minus markers == reading TXT", tel_spoken, rd_paras)
    cmp("teleprompter DOCX == teleprompter TXT", tel_docx, tel_spoken)
    cmp("reading DOCX == reading TXT", rd_docx, rd_paras)
    cmp("marker names and order",
        [m[len("[SLIDE:"):-1].strip() for m in canon_marks],
        [m[len("SLIDE  \u2014"):].strip() for m in tel_marks])
    ok_m = len(canon_marks) == c["markers"]
    overall &= ok_m
    print("  %-52s %s  (%d)" % ("exact marker count", "PASS" if ok_m else "FAIL", len(canon_marks)))
    print("  spoken paragraphs %d | spoken words %d"
          % (len(canon_spoken), sum(len(x.split()) for x in canon_spoken)))
    sys.path.remove(c["root"])

print("=" * 62)
print("CANONICAL VERIFICATION, VIDEOS 4/6/8:", "PASS" if overall else "FAIL")
