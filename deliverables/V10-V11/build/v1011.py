# -*- coding: utf-8 -*-
"""The two FINAL story-led scripts and their supplied Thought-Block copies.

Nothing here writes. The FINAL script is authoritative for spoken wording,
title, thumbnail, framework and section order. The Thought-Block copy is a
recording-format derivative that must carry the same words exactly and in
order; where they disagree the script wins and QA reports rather than
repairs.

Neither video has a former-roadmap number. They are new concepts and none
is invented anywhere in the build.
"""
import os, re, hashlib
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "_source", "files")

VIDEOS = (10, 11)
SCRIPT_START = "SCRIPT STARTS HERE"
NOT_SPOKEN = "[NOT SPOKEN]"
BLOCK_LABEL = re.compile(r"^BLOCK \d+\b")

FILES = {
 10: ("NEW_V10_First_90_Days_FINAL_Story_Led_Recording_Script.docx",
      "NEW_V10_First_90_Days_Thought_Block_Recording_Copy.docx"),
 11: ("NEW_V11_New_Job_Isnt_The_Job_FINAL_Story_Led_Recording_Script.docx",
      "NEW_V11_New_Job_Isnt_The_Job_Thought_Block_Recording_Copy.docx"),
}

# Supplied with the handoff. Verified, never assumed.
HANDOFF_SHA = "f3c094174b7c1d0856399c19618e26fa6e30180bc84f4f2ee7c70af6f04c7b82"
FILE_SHA = {
 "NEW_V10_First_90_Days_FINAL_Story_Led_Recording_Script.docx":
   "9a6a40bc42e46f2360b7ac7157ec3af15fccee8c4dcc7bb36954011af5969c7c",
 "NEW_V10_First_90_Days_Thought_Block_Recording_Copy.docx":
   "6a0b7befdc4df9e2ccb9f20e10185f59b1de3f519419202657f02210f41fc0ea",
 "NEW_V11_New_Job_Isnt_The_Job_FINAL_Story_Led_Recording_Script.docx":
   "d29197fcf43dde43428e032a07d6c7dd3b5303f70acc844301cc2ba268e14a06",
 "NEW_V11_New_Job_Isnt_The_Job_Thought_Block_Recording_Copy.docx":
   "3c300d69fd9f87d05de7de5b8db6cb27559577566b93fe7e6ebef8fe24b9b3b6",
 "NEW_V10-V11_Advisor_and_Code_Handoff.docx":
   "6744c44cda0d838f7a45da3e2c22a9acee89f084afdd7b96b9424e7b4a05020b",
 "CODE_BUILD_PROMPT_NEW_V10_V11.txt":
   "8f9a0647ac1a21d190b54bd2fd08ac4b13549be0b7d640909192441fd82d2266",
}
# Whitespace spoken-word counts stated in the build prompt.
STATED_WORDS = {10: 1486, 11: 1116}

_CACHE = {}


def script_path(n):
    return os.path.join(SRC, FILES[n][0])


def block_path(n):
    return os.path.join(SRC, FILES[n][1])


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _paras(path):
    d = Document(path)
    out = []
    for c in d.element.body.iterchildren():
        if c.tag == qn("w:p"):
            t = Paragraph(c, d).text.rstrip()
            if t.strip():
                out.append(t)
    return out


def _norm(t):
    return " ".join(t.replace("’", "'").replace("“", '"')
                    .replace("”", '"').split()).strip()


def _is_label(t):
    """An all-capitals production heading, never a spoken line."""
    s = t.strip()
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return True
    if s.startswith("[") and s.endswith("]"):
        return True
    return all(c.isupper() for c in letters) and len(s) < 90


def read(n):
    if n in _CACHE:
        return _CACHE[n]
    ps = _paras(script_path(n))
    meta = {"title": ps[2],
            "thumbnail": ps[3].split(":", 1)[1].strip(),
            "new": int(re.search(r"V(\d+)", ps[1]).group(1))}
    i0 = ps.index(SCRIPT_START) + 1
    sections, cur, notes = [], None, []
    for t in ps[i0:]:
        if NOT_SPOKEN in t:
            notes.append(t)
            continue
        if _is_label(t):
            cur = (t.strip(), [])
            sections.append(cur)
            continue
        if cur is None:
            cur = ("OPEN", [])
            sections.append(cur)
        cur[1].append(t)
    _CACHE[n] = dict(meta=meta, sections=sections, notes=notes,
                     sha=sha256(script_path(n)),
                     file=os.path.basename(script_path(n)))
    return _CACHE[n]


def title(n):
    return read(n)["meta"]["title"]


def thumbnail(n):
    return read(n)["meta"]["thumbnail"]


def sections(n):
    return read(n)["sections"]


def paragraphs(n):
    return [p for _, ps in sections(n) for p in ps]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    return len(spoken_text(n).split())


def estimate(n):
    """Arithmetic on the script at 130 to 145 words per minute.

    This is not a runtime. Nothing has been recorded, edited or exported.
    """
    w = word_count(n)
    fast, slow = w / 145.0 * 60, w / 130.0 * 60
    return ("%d:%02d" % (fast // 60, fast % 60),
            "%d:%02d" % (slow // 60, slow % 60))


def watch_next(n):
    """The destination named on the final full-screen card, as written."""
    for t in read(n)["notes"]:
        m = re.match(r"\[FINAL FULL-SCREEN WATCH NEXT:\s*(.+?)\]", t)
        if m:
            return m.group(1).strip()
    raise SystemExit("V%d: no final Watch Next card in the script" % n)


DIRECTION = "Read one block silently"


def block_paragraphs(n):
    """The spoken stream of the Thought-Block copy, labels removed.

    The copy carries no SCRIPT STARTS HERE marker, so the document header
    and the recording direction are skipped by finding the direction line
    and starting after it. Everything above it is front matter, not speech.
    """
    ps = _paras(block_path(n))
    start = 0
    for i, t in enumerate(ps):
        if t.startswith(DIRECTION):
            start = i + 1
            break
    else:
        raise SystemExit("V%d: no recording direction line in the "
                         "Thought-Block copy" % n)
    out = []
    for t in ps[start:]:
        if NOT_SPOKEN in t or BLOCK_LABEL.match(t.strip()) or _is_label(t):
            continue
        out.append(t)
    return out


def blocks_match(n):
    a = [_norm(x) for x in paragraphs(n)]
    b = [_norm(x) for x in block_paragraphs(n)]
    if a == b:
        return True, "%d paragraphs, identical and in order" % len(a)
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return False, "paragraph %d differs:\n  script: %s\n  block : %s" \
                          % (i, x[:90], y[:90])
    return False, "length differs: script %d, block %d" % (len(a), len(b))


def contains(n, frag):
    return _norm(frag).lower() in _norm(spoken_text(n)).lower()


if __name__ == "__main__":
    print("handoff.zip %s" % ("verified" if sha256(
        os.path.join(OUT, "_source", "handoff.zip")) == HANDOFF_SHA
        else "MISMATCH"))
    for nm, want in sorted(FILE_SHA.items()):
        got = sha256(os.path.join(SRC, nm))
        print("  %-62s %s" % (nm[:62], "ok" if got == want else "MISMATCH"))
    for n in VIDEOS:
        w = word_count(n)
        ok, det = blocks_match(n)
        print("\nNEW V%d  %s" % (n, title(n)))
        print("   thumbnail   : %s" % thumbnail(n))
        print("   sections    : %d" % len(sections(n)))
        print("   paragraphs  : %d" % len(paragraphs(n)))
        print("   spoken words: %d   stated %d   %s"
              % (w, STATED_WORDS[n],
                 "match" if w == STATED_WORDS[n] else "DIFFERS"))
        print("   watch next  : %s" % watch_next(n))
        print("   blocks      : %s  %s" % (ok, det if not ok else det))
