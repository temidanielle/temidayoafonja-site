# -*- coding: utf-8 -*-
"""Read the eighteen September 11 corrected-runtime Recording Masters.

These are the controlling source. This module reads them and never writes to
them. Every checksum is matched against the manifest taken at extraction
before any content is used.

Structure, shared with the earlier master sets:

    CAPABILITY FORMATION | ...
    <title>
    <kind> | <date>
    [meta table: key | value]
    RECORDING SCRIPT STARTS HERE
    <section heading>
    <thought block>
    ...
    <a tail section that is not spoken>
"""
import os, re, hashlib
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "_source")

# Videos 6, 7 and 8 were supplied compressed to roughly half the approved
# teaching. Their restored full-depth derivatives live beside the supplied
# files and are the spoken source of truth for those three videos. The
# supplied masters are untouched in _source/ and keep their checksums.
RESTORED_SRC = os.path.join(os.path.dirname(HERE), "_source_restored")
RESTORED = {
 6: "Video_6_RESTORED_Regular_Length_Recording_Master.docx",
 7: "Video_7_RESTORED_Regular_Length_Recording_Master.docx",
 8: "Video_8_RESTORED_Regular_Length_Recording_Master.docx",
}

VIDEOS = tuple(range(4, 22))
FIVE_MIN = (4, 5)                  # the only runtime experiment
REGULAR = tuple(range(6, 22))
RESTORED_DEPTH = tuple(range(15, 22))

FILES = {
 4:  "Video_4_FINAL_5_Minute_Test_Recording_Master.docx",
 5:  "Video_5_FINAL_5_Minute_Test_Recording_Master.docx",
 6:  "Video_6_FINAL_Revised_Recording_Master.docx",
 7:  "Video_7_FINAL_Revised_Recording_Master.docx",
 8:  "Video_8_FINAL_Revised_Recording_Master.docx",
 9:  "Video_9_FINAL_Revised_Recording_Master.docx",
 10: "Video_10_FINAL_Revised_Recording_Master.docx",
 11: "Video_11_FINAL_Revised_Recording_Master.docx",
 12: "Video_12_FINAL_Revised_Recording_Master.docx",
 13: "Video_13_FINAL_Revised_Recording_Master.docx",
 14: "Video_14_Which_Parts_of_Your_Experience_Actually_Transfer_FINAL_"
     "Recording_Master.docx",
 15: "Video_15_FINAL_Regular_Length_Recording_Master.docx",
 16: "Video_16_FINAL_Regular_Length_Recording_Master.docx",
 17: "Video_17_FINAL_Regular_Length_Recording_Master.docx",
 18: "Video_18_FINAL_Regular_Length_Recording_Master.docx",
 19: "Video_19_FINAL_Regular_Length_Recording_Master.docx",
 20: "Video_20_FINAL_Regular_Length_Recording_Master.docx",
 21: "Video_21_FINAL_Regular_Length_Recording_Master.docx",
}

RESEARCH = "what-really-transfers-research.md"

SCRIPT_START = "RECORDING SCRIPT STARTS HERE"
# Section labels that mark the end of the spoken script. Everything from one
# of these onward is production material and must never reach the recording
# copy. Two of them are easy to miss and were verified by reading the content:
# V9 to V13 close with "END OF SPOKEN SCRIPT", whose one block literally says
# "Do not read this line"; V15 to V21 close with "PRODUCTION GUARDRAILS".
# "WATCH NEXT | Final visual" in V9 to V13 IS spoken and is not listed here.
SCRIPT_END = ("END OF SPOKEN SCRIPT", "PRODUCTION GUARDRAILS",
              "EDITOR / VISUAL PRIORITIES", "MAJOR VISUAL",
              "RESEARCH INTEGRITY NOTES", "FINAL QA", "EDITOR NOTES",
              "PRODUCTION NOTES", "VISUAL PRIORITIES", "NOTES FOR")

_cache = {}


def path(n):
    """The file that is the spoken source of truth for this video."""
    if n in RESTORED:
        return os.path.join(RESTORED_SRC, RESTORED[n])
    return os.path.join(SRC, FILES[n])


def supplied_path(n):
    """The file as supplied on September 11, always. For V6, V7 and V8 this
    is the compressed master that the restoration supersedes; it is kept so
    its checksum can still be reported and so nothing pretends it never
    existed."""
    return os.path.join(SRC, FILES[n])


def filename(n):
    return RESTORED[n] if n in RESTORED else FILES[n]


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def manifest():
    out = {}
    for line in open(os.path.join(SRC, "SOURCE_HASHES.txt")):
        h, name = line.split(None, 1)
        out[name.strip()] = h
    return out


def restored_manifest():
    out = {}
    f = os.path.join(RESTORED_SRC, "RESTORED_SOURCE_HASHES.txt")
    for line in open(f):
        line = line.strip()
        if line:
            h, name = line.split(None, 1)
            out[name.strip()] = h
    return out


def verify(n):
    """The spoken source must match its recorded hash, and for V6, V7 and V8
    the supplied compressed master must ALSO still match its original hash.
    A restoration that quietly edited the supplied file would pass the first
    check and fail the second."""
    if n in RESTORED:
        got = sha256(supplied_path(n))
        want = manifest()[FILES[n]]
        if got != want:
            raise SystemExit("V%d supplied master was modified: %s != %s"
                             % (n, got, want))
        got = sha256(path(n))
        want = restored_manifest()[RESTORED[n]]
        if got != want:
            raise SystemExit("V%d restored master changed on disk: %s != %s"
                             % (n, got, want))
        return got
    got, want = sha256(path(n)), manifest()[FILES[n]]
    if got != want:
        raise SystemExit("V%d master changed on disk: %s != %s"
                         % (n, got, want))
    return got


def verify_all():
    return {n: verify(n) for n in VIDEOS}


def research_hash():
    return sha256(os.path.join(SRC, RESEARCH))


def research_text():
    return open(os.path.join(SRC, RESEARCH), encoding="utf-8").read()


def _blocks(doc):
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield "p", Paragraph(child, doc)
        elif child.tag == qn("w:tbl"):
            yield "t", Table(child, doc)


def _is_heading(text):
    """A working section label, not speech."""
    if len(text) > 110 or "\n" in text:
        return False
    head = text.split(" | ", 1)[0]
    return head == head.upper() and any(c.isalnum() for c in head)


def read(n):
    if n in _cache:
        return _cache[n]
    verify(n)
    doc = Document(path(n))
    paras, meta, tables = [], {}, []
    for kind, b in _blocks(doc):
        if kind == "p":
            t = b.text.strip()
            if t:
                paras.append((b.style.name, t))
        else:
            rows = [[c.text.strip() for c in r.cells] for r in b.rows]
            tables.append(rows)
            if not meta:
                for r in rows:
                    if len(r) == 2:
                        meta[r[0]] = r[1]

    flat = [t for _, t in paras]
    start = flat.index(SCRIPT_START) + 1
    end = len(flat)
    for i in range(start, len(flat)):
        if any(flat[i].startswith(m) for m in SCRIPT_END):
            end = i
            break

    sections, cur = [], None
    for t in flat[start:end]:
        if _is_heading(t):
            cur = (t, [])
            sections.append(cur)
        else:
            if cur is None:
                cur = ("", [])
                sections.append(cur)
            cur[1].append(t)

    # The title is the last paragraph before the meta table that is neither
    # an all-caps label nor a pipe-separated eyebrow or byline.
    head = flat[:start - 1]
    cands = [t for t in head
             if " | " not in t and t != t.upper() and len(t) > 12]
    out = dict(num=n, file=filename(n), sha=sha256(path(n)),
               supplied_file=FILES[n],
               supplied_sha=sha256(supplied_path(n)),
               restored=(n in RESTORED),
               eyebrow=flat[0], title=(cands[-1] if cands else flat[1]),
               kind=flat[2] if len(flat) > 2 else "",
               meta=meta, tables=tables, sections=sections,
               tail=flat[end:])
    _cache[n] = out
    return out


def _meta(n, *keys, default=""):
    m = read(n)["meta"]
    for k in keys:
        for mk in m:
            if mk.lower().startswith(k.lower()):
                return m[mk]
    return default


def title(n):
    return _meta(n, "Title", "Recommended title") or read(n)["title"]


def thumbnail(n):
    return _meta(n, "Thumbnail")


def framework(n):
    return _meta(n, "Framework")


def cta(n):
    return _meta(n, "Primary CTA", "CTA")


def resource(n):
    return _meta(n, "Resource route", "Resource")


def watch_next(n):
    return _meta(n, "Watch Next")


def runtime_intent(n):
    """The runtime the master itself states, verbatim. Never invented."""
    return _meta(n, "Target runtime", "Target length", "Length plan",
                 "Runtime", "Length")


def blocks(n):
    return [b for _, bs in read(n)["sections"] for b in bs]


def sections(n):
    return read(n)["sections"]


def spoken_text(n):
    return "\n\n".join(blocks(n))


def word_count(n):
    return sum(len(b.split()) for b in blocks(n))


def estimate(n, fast=145.0, slow=130.0):
    w = word_count(n)
    def mmss(m):
        return "%d:%02d" % (int(m), round((m - int(m)) * 60))
    return w, mmss(w / fast), mmss(w / slow)


def final_line(n):
    return blocks(n)[-1]


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")
                  .replace("“", '"').replace("”", '"')
                  .replace("–", "-").replace("—", "-")).strip()


def contains(n, sentence):
    return _norm(sentence) in _norm(spoken_text(n))


def trigger_ok(n, sentence):
    """A trigger must sit inside ONE thought block, never across two takes."""
    s = _norm(sentence)
    return any(s in _norm(b) for b in blocks(n))


def mode(n):
    return "5-MINUTE RETENTION TEST" if n in FIVE_MIN else "REGULAR LONG-FORM"


if __name__ == "__main__":
    verify_all()
    print("%-4s %-6s %-62s %-30s %5s %s"
          % ("#", "MODE", "TITLE", "THUMBNAIL", "WORDS", "ESTIMATE"))
    for n in VIDEOS:
        w, f, s = estimate(n)
        print("V%-3d %-6s %-62s %-30s %5d %s to %s"
              % (n, "5MIN" if n in FIVE_MIN else "LONG", title(n)[:62],
                 thumbnail(n)[:30], w, f, s))
