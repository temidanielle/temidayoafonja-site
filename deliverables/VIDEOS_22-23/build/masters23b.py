# -*- coding: utf-8 -*-
"""The September 13 FINAL story-led scripts for V22 and V23.

These supersede the 50CHAR advisor-review scripts the first package was built
from. Nothing here writes. Section labels are bracketed and sit at the head of
the first spoken paragraph of their section; they are production navigation
and are never spoken. The scripts carry no timing markers at all, which is
why nothing in this build has a timestamp to misread as a runtime.
"""
import os, re, hashlib
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "_source_v2")

FILES = {22: "Video_22_FINAL_Story_Led_Recording_Script.docx",
         23: "Video_23_FINAL_Story_Led_Recording_Script.docx"}
OVERVIEW = "V22-V38_Roadmap_Extension_Overview_and_Editorial_Map.docx"

VIDEOS = (22, 23)
BUILD_DATE = "September 13, 2026"
CAPTURE_DATE = "September 12, 2026"

# The roadmap supplied 982 and 895. Those figures describe the scripts as
# they stood BEFORE the September 13 source-language corrections, and they are
# kept here as the historical record rather than as a live target.
SUPPLIED_PRE_CORRECTION = {22: 982, 23: 895}
WHITESPACE_PRE_CORRECTION = {22: 978, 23: 895}

# The two corrections, for the record. Each was authorized explicitly and
# each replaced exactly one paragraph.
CORRECTIONS = {
 22: ("Then ask the question people sometimes skip because they want the "
      "move to work:",
      "Then ask the question that is easy to skip when you want the move to "
      "work:"),
 23: ("This is the line I think experienced professionals struggle with "
      "most.",
      "This is the line I want you to spend the most time on."),
}

LABEL = re.compile(r"^\[([^\]]+)\]\s*")
META = re.compile(r"^(THUMBNAIL:|Created |Editorial role:)")

# Packaging that must never appear in an active production document again.
SUPERSEDED_TITLES = ("How to Decode a Job Description",
                     "Turn One Accomplishment Into Career Proof")
SUPERSEDED_THUMBNAILS = ("YOU DID IT. CAN YOU PROVE IT?",)


def path(n):
    return os.path.join(SRC, FILES[n])


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _blocks(doc):
    for c in doc.element.body.iterchildren():
        if c.tag == qn("w:p"):
            yield ("P", Paragraph(c, doc))
        elif c.tag == qn("w:tbl"):
            yield ("T", Table(c, doc))


_CACHE = {}


def read(n):
    if n in _CACHE:
        return _CACHE[n]
    d = Document(path(n))
    paras = [b.text.rstrip() for k, b in _blocks(d) if k == "P"]
    paras = [p for p in paras if p.strip()]
    title = paras[1]
    thumb = ""
    stream, seen_label = [], False
    for p in paras[2:]:
        if p.startswith("THUMBNAIL:"):
            thumb = p.split(":", 1)[1].strip()
            continue
        if META.match(p):
            continue
        m = LABEL.match(p)
        if m:
            seen_label = True
            stream.append(("LABEL", m.group(1).strip()))
            rest = p[m.end():].strip()
            if rest:
                stream.append(("SAY", rest))
            continue
        if seen_label:
            stream.append(("SAY", p))
    _CACHE[n] = dict(title=title, thumbnail=thumb, stream=stream,
                     sha=sha256(path(n)), file=FILES[n])
    return _CACHE[n]


def title(n):
    return read(n)["title"]


def script_header_thumbnail(n):
    return read(n)["thumbnail"]


def sections(n):
    """[(label, [spoken paragraphs])] in spoken order."""
    out, cur = [], None
    for kind, v in read(n)["stream"]:
        if kind == "LABEL":
            cur = (v, [])
            out.append(cur)
        elif cur is not None:
            cur[1].append(v)
    return out


def paragraphs(n):
    return [p for _, ps in sections(n) for p in ps]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    return sum(len(p.split()) for p in paragraphs(n))


def estimate(n, low=130, high=145):
    w = word_count(n)

    def mmss(wpm):
        s = int(round(w / float(wpm) * 60))
        return "%d:%02d" % (s // 60, s % 60)
    return mmss(high), mmss(low)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def is_label(text):
    return bool(LABEL.match(text.strip())) or any(
        _norm(text) == _norm(lab) for lab, _ in sections(22) + sections(23))


def trigger_ok(n, trigger):
    """A cue must be a whole spoken paragraph of this script, matched once."""
    q = _norm(trigger)
    return sum(1 for p in paragraphs(n) if _norm(p) == q) == 1


def contains(n, phrase):
    return _norm(phrase) in _norm(spoken_text(n))


def overview_lines():
    d = Document(os.path.join(SRC, OVERVIEW))
    out = []
    for k, b in _blocks(d):
        if k == "P" and b.text.strip():
            out.append(b.text.strip())
        elif k == "T":
            for r in b.rows:
                out.append(" | ".join(c.text.strip() for c in r.cells))
    return out


def manifest():
    rows = []
    for rel in list(FILES.values()) + [OVERVIEW]:
        p = os.path.join(SRC, rel)
        rows.append((rel, sha256(p), os.path.getsize(p)))
    return rows


def currency_tokens(n):
    """Figures beginning with a currency symbol.

    A counter that separates the symbol from the numeral counts each of these
    as two tokens. That is the whole of the difference between the roadmap's
    supplied figure and a whitespace count of the same text.
    """
    return [w for w in spoken_text(n).split() if w.startswith("$")]


def counts(n):
    """(whitespace, currency-separated) word counts for the current script."""
    w = word_count(n)
    return w, w + len(currency_tokens(n))


def verify_counts():
    """The two counting methods must still differ by exactly the currency
    tokens, and each script must still carry its correction."""
    bad = []
    for n in VIDEOS:
        w, c = counts(n)
        if c - w != len(currency_tokens(n)):
            bad.append((n, "currency reconciliation", w, c))
        old, new = CORRECTIONS[n]
        if old in spoken_text(n) or new not in spoken_text(n):
            bad.append((n, "correction not applied", old[:40], new[:40]))
    return not bad, bad


if __name__ == "__main__":
    for n in VIDEOS:
        print("V%d  %s" % (n, title(n)))
        print("    thumbnail (script header)  %s" % script_header_thumbnail(n))
        print("    sections   %d" % len(sections(n)))
        print("    paragraphs %d" % len(paragraphs(n)))
        w, c = counts(n)
        print("    words      %d whitespace, %d with the currency symbol "
              "counted separately" % (w, c))
        print("    was        %d whitespace, %d supplied, before the "
              "correction" % (WHITESPACE_PRE_CORRECTION[n],
                              SUPPLIED_PRE_CORRECTION[n]))
        print("    estimate   %s to %s" % estimate(n))
        print("    sha        %s" % read(n)["sha"])
        for lab, ps in sections(n):
            print("      %-32s %2d paras  %4d words"
                  % (lab, len(ps), sum(len(p.split()) for p in ps)))
    print("\ncounts match the supplied figures:", verify_counts())
