# -*- coding: utf-8 -*-
"""The V22 and V23 sources, read from the supplied documents.

Nothing here writes. The two UPDATED 50CHAR script documents are the only
authority for spoken wording, title and thumbnail. The advisor overview is
read for rationale and the capture packet for evidence, and neither is ever
allowed to change a spoken line.
"""
import os, re, hashlib
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "_source", "V22_V23_CODE_BUILD_INPUTS_2026-09-13")

INPUT_ZIP_SHA = ("eb84bbb49566e30de403343071da8893ff577fb3fb537f7452ba77ca"
                 "986c9a1d")
CAPTURE_DATE = "September 12, 2026"
BUILD_DATE = "September 13, 2026"

FILES = {
    22: "Authoritative_Scripts/V22_UPDATED_50CHAR_Advisor_Review_Title_"
        "Thumbnail_and_Script.docx",
    23: "Authoritative_Scripts/V23_UPDATED_50CHAR_Advisor_Review_Title_"
        "Thumbnail_and_Script.docx",
}
OVERVIEW = ("Authoritative_Scripts/V22-V23_UPDATED_50CHAR_Advisor_Overview_"
            "and_Editorial_Rationale.docx")
PACKET = "Evidence/Internal_Source_Capture_Packet.docx"
SCREENS = "Visual_Reference_Only"

VIDEOS = (22, 23)
START = "SCRIPT STARTS HERE"
# "0:00 · COLD OPEN" and friends. The timestamps are editorial navigation
# markers supplied with the script; they are not runtime and never spoken.
MARK = re.compile(r"^(\d+:\d\d)\s*[·•\-]\s*(.+)$")

# Older packaging that must never reappear in anything this build writes.
SUPERSEDED_TITLES = (
    "How to Read a Job Description for What Actually Matters So Fast, "
    "It Feels Like Cheating",
    "How to Turn One Accomplishment Into Career Proof So Fast, "
    "It Feels Like Cheating",
)
SUPERSEDED_THUMBNAIL = "ONE WIN → PROOF"


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
    meta, spoken, started = {}, [], False
    for kind, b in _blocks(d):
        if kind == "T":
            for r in b.rows:
                cells = [c.text.strip() for c in r.cells]
                if len(cells) == 2 and cells[0]:
                    meta[cells[0].upper()] = cells[1]
            continue
        t = b.text.strip()
        if not t:
            continue
        if t == START:
            started = True
            continue
        if not started:
            continue
        m = MARK.match(t)
        if m:
            spoken.append(("MARK", m.group(1), m.group(2).strip()))
        else:
            spoken.append(("SAY", t))
    _CACHE[n] = dict(meta=meta, stream=spoken, sha=sha256(path(n)))
    return _CACHE[n]


def title(n):
    return read(n)["meta"]["TITLE"]


def thumbnail(n):
    return read(n)["meta"]["THUMBNAIL"]


def sections(n):
    """[(marker, label, [spoken paragraphs])] in spoken order."""
    out, cur = [], None
    for item in read(n)["stream"]:
        if item[0] == "MARK":
            cur = (item[1], item[2], [])
            out.append(cur)
        elif cur is not None:
            cur[2].append(item[1])
    return out


def paragraphs(n):
    return [i[1] for i in read(n)["stream"] if i[0] == "SAY"]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    return sum(len(p.split()) for p in paragraphs(n))


def markers(n):
    return [(m, lab) for m, lab, _ in sections(n)]


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def trigger_ok(n, trigger):
    """A cue must be a whole spoken paragraph of this script, matched once."""
    q = _norm(trigger)
    return sum(1 for p in paragraphs(n) if _norm(p) == q) == 1


def contains(n, phrase):
    return _norm(phrase) in _norm(spoken_text(n))


def estimate(n, low=130, high=145):
    w = word_count(n)
    def mmss(wpm):
        s = int(round(w / float(wpm) * 60))
        return "%d:%02d" % (s // 60, s % 60)
    return mmss(high), mmss(low)


# ------------------------------------------------------------ other sources
def _plain(p):
    d = Document(p)
    out = []
    for kind, b in _blocks(d):
        if kind == "P":
            t = b.text.strip()
            if t:
                out.append(t)
        else:
            for r in b.rows:
                out.append(" | ".join(c.text.strip() for c in r.cells))
    return out


def overview_lines():
    return _plain(os.path.join(SRC, OVERVIEW))


def packet_lines():
    return _plain(os.path.join(SRC, PACKET))


def screenshots():
    d = os.path.join(SRC, SCREENS)
    return sorted(os.path.join(d, f) for f in os.listdir(d)
                  if f.lower().endswith(".png"))


def manifest():
    rows = []
    for rel in (list(FILES.values()) + [OVERVIEW, PACKET]
                + [os.path.join(SCREENS, os.path.basename(s))
                   for s in screenshots()]):
        p = os.path.join(SRC, rel)
        rows.append((rel.replace("\\", "/"), sha256(p), os.path.getsize(p)))
    return rows


if __name__ == "__main__":
    for n in VIDEOS:
        print("V%d  %s" % (n, title(n)))
        print("    thumbnail  %s" % thumbnail(n))
        print("    sections   %d" % len(sections(n)))
        print("    paragraphs %d" % len(paragraphs(n)))
        print("    words      %d" % word_count(n))
        print("    estimate   %s to %s" % estimate(n))
        print("    sha        %s" % read(n)["sha"])
        for m, lab, ps in sections(n):
            print("      %-6s %-34s %2d paras %4d words"
                  % (m, lab, len(ps), sum(len(p.split()) for p in ps)))
