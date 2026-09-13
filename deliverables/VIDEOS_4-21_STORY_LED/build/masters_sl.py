# -*- coding: utf-8 -*-
"""The September 13 story-led scripts, and their matching thought blocks.

These are the spoken source of truth for Videos 4 to 21. They control the
opening, the scene order, the bridges, where the framework lands, the
examples, the application moments, the closing, the CTA wording and the Watch
Next intent. Where the pre-story-led production package disagrees with them,
they win.

Nothing here writes to a source file. Every document is read and hashed, and
the hash is checked against the manifest taken at intake, so a script cannot
drift underneath the build.
"""
import os, re, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "_source")

VIDEOS = tuple(range(4, 22))
SHORT_TEST = (4, 5)                 # the retention test, and only these two
LONG_FORM = tuple(range(6, 22))
FULLER_DEPTH = tuple(range(15, 22))

SCRIPT = "Video_%d_FINAL_Story_Led_Conversational_Recording_Script.docx"
BLOCKS = "Video_%d_Thought_Block_Recording_Copy_Story_Led.docx"
CHANGELOG = "V4-V21_Storytelling_Lens_Change_Log_and_QA.docx"

START = "RECORDING SCRIPT STARTS HERE"
END = "END OF SPOKEN SCRIPT"
NOT_SPOKEN = "[NOT SPOKEN]"

_cache = {}


def path(n, blocks=False):
    return os.path.join(SRC, (BLOCKS if blocks else SCRIPT) % n)


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def manifest():
    out = {}
    for line in open(os.path.join(SRC, "SOURCE_HASHES.txt")):
        line = line.strip()
        if line:
            h, name = line.split(None, 1)
            out[name.strip()] = h
    return out


def verify(n):
    m = manifest()
    for p, name in ((path(n), SCRIPT % n), (path(n, True), BLOCKS % n)):
        got = sha256(p)
        if got != m[name]:
            raise SystemExit("%s changed on disk: %s != %s"
                             % (name, got, m[name]))
    return True


def verify_all():
    return all(verify(n) for n in VIDEOS)


def _is_label(t):
    """A section label is a production aid. It is never spoken.

    Two shapes appear in these scripts. Most are capitalized words before a
    pipe, such as "HOOK | New field does not mean zero". The numbered ones
    are "1 | Capability: What underlying work can you prove?", where the part
    before the pipe is a digit and carries no case at all. Testing only the
    capitalization of the head misses every numbered label and leaks it into
    the spoken script, which would put a production aid in front of the
    camera.
    """
    head = t.split("|")[0].strip()
    # "1 | Capability: What underlying work can you prove?"
    if "|" in t and re.fullmatch(r"\d+", head):
        return len(t) < 90
    hl = [c for c in head if c.isalpha()]
    if not hl:
        return False
    # "HOOK | New field does not mean zero", and "ACTION AND RESOURCE",
    # which carries no pipe at all.
    return (sum(1 for c in hl if c.isupper()) / float(len(hl)) > 0.85
            and len(head) < 60)


def read(n):
    """{title, thumbnail, lens, sections, spoken, sha}"""
    if n in _cache:
        return _cache[n]
    d = Document(path(n))
    flat = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    meta = {}
    for t in d.tables:
        for r in t.rows:
            c = [x.text.strip() for x in r.cells]
            if len(c) >= 2 and c[0]:
                meta[c[0]] = c[1]
    try:
        i = flat.index(START) + 1
    except ValueError:
        raise SystemExit("V%d: no %r marker" % (n, START))
    sections, cur = [], None
    for t in flat[i:]:
        if t.startswith(END):
            break
        if _is_label(t):
            cur = (t, [])
            sections.append(cur)
            continue
        if cur is None:
            cur = ("(before the first label)", [])
            sections.append(cur)
        cur[1].append(t)
    out = dict(num=n, file=SCRIPT % n, sha=sha256(path(n)),
               eyebrow=flat[0], title=flat[1], meta=meta,
               thumbnail=meta.get("Thumbnail", ""),
               lens=meta.get("Editorial lens", ""),
               sections=sections)
    _cache[n] = out
    return out


def title(n):
    return read(n)["title"]


def thumbnail(n):
    return read(n)["thumbnail"]


def sections(n):
    return read(n)["sections"]


def paragraphs(n):
    return [p for _, ps in sections(n) for p in ps]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    return sum(len(p.split()) for p in paragraphs(n))


def estimate(n, fast=145.0, slow=130.0):
    w = word_count(n)
    mm = lambda x: "%d:%02d" % (int(x) // 60, int(x) % 60)
    return w, mm(w / fast * 60), mm(w / slow * 60)


def mode(n):
    return ("SHORTER RETENTION TEST" if n in SHORT_TEST
            else "REGULAR LONG-FORM")


# ---------------------------------------------------------- thought blocks
def blocks(n):
    """[(section label or None, block text)] from the thought-block copy."""
    d = Document(path(n, True))
    flat = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    out, label = [], None
    for t in flat:
        if t.startswith(NOT_SPOKEN):
            label = t[len(NOT_SPOKEN):].strip()
            continue
        m = re.match(r"^BLOCK\s+\d+\s*\n(.*)$", t, re.S)
        if m:
            out.append((label, m.group(1).strip()))
    return out


def block_text(n):
    return [b for _, b in blocks(n)]


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'")
                  .replace("“", '"').replace("”", '"')).strip()


def blocks_match_script(n):
    """The thought block must say exactly what the script says, in order.

    Returns (ok, detail). This is the check that keeps the recording copy and
    the script from drifting apart, which is the one failure that would put
    unapproved words in front of the camera.
    """
    # A thought block is a unit of delivery, not a copy of a paragraph. A
    # long spoken paragraph is deliberately split across two blocks so the
    # reader can breathe. So block boundaries may differ from paragraph
    # boundaries; the words and their order may not. Comparing the two word
    # streams tests exactly that and nothing else.
    a = _norm(" ".join(paragraphs(n))).split()
    b = _norm(" ".join(block_text(n))).split()
    if a == b:
        return True, ("%d blocks carry the script's %d spoken words exactly, "
                      "in order" % (len(block_text(n)), len(a)))
    import difflib
    sm = difflib.SequenceMatcher(None, a, b)
    ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
    first = ops[0] if ops else None
    detail = "script %d words, blocks %d words, %d differing runs" % (
        len(a), len(b), len(ops))
    if first:
        tag, i1, i2, j1, j2 = first
        detail += ". first: %s script %r vs block %r" % (
            tag, " ".join(a[i1:i2])[:70], " ".join(b[j1:j2])[:70])
    return False, detail


def contains(n, sentence):
    return _norm(sentence) in _norm(spoken_text(n))


def trigger_ok(n, sentence):
    """A trigger must sit inside ONE spoken paragraph, never spanning two."""
    q = _norm(sentence)
    return any(q in _norm(p) for p in paragraphs(n))
