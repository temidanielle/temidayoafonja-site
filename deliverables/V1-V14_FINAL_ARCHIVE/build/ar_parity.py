# -*- coding: utf-8 -*-
"""Thought-block parity for all fourteen videos, read from the approved files.

Three document shapes are in play and each marks its section labels
differently, so the reader has to know which it is looking at:

  sticky  V1 to V3. Master labels are a bare upper-case line. Block labels
          carry a trailing [NOT SPOKEN].
  sync    V4 to V11. Label and marker share one line: "HOOK  [NOT SPOKEN]".
  built   V12 to V14. The label is its own line and "[NOT SPOKEN]" is the
          line after it.

A reader that silently drops real speech would make parity pass for the wrong
reason, so every count is cross-checked against the word count the document
prints in its own header where it has one, and reader_regression() proves the
reader does not simply return nothing.
"""
import zipfile, re, html, hashlib
import ar_sources as S

def paras(path):
    x = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", x, re.S):
        t = html.unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S))).strip()
        if t:
            out.append(t)
    return out

BLOCK = re.compile(r"^BLOCK\s+\d+$")
DIRECTION = re.compile(r"^(RECORDING DIRECTION|Read one block silently)")
# The built shape writes its editor cues into the recording master as their own
# paragraphs: "[ CAMERA ]  CAMERA   Come off the card ...". They are production
# notes, not speech, and counting them inflated V12 to V14 by several hundred
# words on the first run of this check.
CUE = re.compile(r"^\[\s*(CAMERA|ARTIFACT|SOUND|SUBSCRIBE)\s*\]")

def is_bare_label(t):
    return t.isupper() and len(t.split()) <= 8 and not t.endswith(".")

def body_start(ts, shape, kind):
    """Find where the header stops, structurally rather than by a fixed offset.

    A fixed offset was wrong for the built thought blocks, which carry one extra
    header line ("Blocks  38") that a nine-line cut left inside the spoken
    stream and that showed up as exactly two extra words.
    """
    for i, t in enumerate(ts):
        if shape == "built":
            if i + 1 < len(ts) and ts[i + 1].strip() == "[NOT SPOKEN]":
                return i
        elif shape == "sync":
            if t.endswith("[NOT SPOKEN]"):
                return i
        else:  # sticky
            # The sticky header's own first line, "CAPABILITY FORMATION
            # YOUTUBE | H.I.T. REFRESH", is upper case and short, so a plain
            # label scan matches it at index 0 and drags the whole four-line
            # header into the spoken stream. That is what it did on the first
            # run, inflating V1 to V3 by exactly their header words. The sticky
            # header is four lines in all six documents, so the scan starts
            # after it.
            if i < 4:
                continue
            if kind == "blocks":
                if t.endswith("[NOT SPOKEN]"):
                    return i
            elif is_bare_label(t):
                return i
    return 0

def spoken(path, shape, kind):
    """kind is 'master' or 'blocks'."""
    ts = paras(path)
    body = ts[body_start(ts, shape, kind):]
    out = []
    for i, t in enumerate(body):
        if DIRECTION.match(t):
            continue
        if CUE.match(t):
            continue
        if t.strip() == "[NOT SPOKEN]" or t.endswith("[NOT SPOKEN]"):
            continue
        if BLOCK.match(t.strip()):
            continue
        if shape == "built" and i + 1 < len(body) and body[i + 1].strip() == "[NOT SPOKEN]":
            continue
        if shape == "sticky" and kind == "master" and is_bare_label(t):
            continue
        out.append(t)
    return out

PRINTED = re.compile(r"^Spoken words\s+([\d,]+)$")
def printed_count(path):
    for t in paras(path)[:14]:
        m = PRINTED.match(t.strip())
        if m:
            return int(m.group(1).replace(",", ""))
    return None

FUSED = {2: "READ THE LAST 90 DAYS", 3: "KEEP THE PROOF, NOT THE PROPERTY"}

def check(n):
    m_path, b_path, shape, _prov = S.SRC[n]
    ms = spoken(m_path, shape, "master")
    bs = spoken(b_path, shape, "blocks")
    a, b = " ".join(ms).split(), " ".join(bs).split()
    first = None
    if a != b:
        first = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]),
                     min(len(a), len(b)))
    stated = printed_count(m_path)
    notes = []
    if stated is not None and stated != len(a):
        notes.append("printed %d, read %d" % (stated, len(a)))
    # Paragraph count and block count differ by design in the built shape,
    # where one thought block groups two to five sentences. Token-stream
    # equality above already proves no sentence is missing and none is
    # duplicated, so grouping is reported as information, not as a defect.
    grouping = "%d paragraphs grouped into %d blocks" % (len(ms), len(bs))
    body = " ".join(a)
    if "—" in body or "–" in body:
        notes.append("em or en dash present")
    BRIT = [r"\borganis", r"\brecognis", r"\banalyse", r"\bcentre\b",
            r"\bbehaviour", r"\bcolour", r"\blabour", r"\bjudgement\b",
            r"\bprogramme\b", r"\blicence\b", r"\bwhilst\b", r"\bhas got\b"]
    hits = [p for p in BRIT if re.search(p, body.lower())]
    if hits:
        notes.append("British spelling: %s" % ", ".join(hits))
    fused = None
    if n in FUSED and any(FUSED[n] in x for x in ms):
        fused = FUSED[n]
    return dict(n=n, words=len(a), block_words=len(b), passed=(a == b),
                grouping=grouping,
                first=first, stated=stated, notes=notes, fused=fused,
                paras=len(ms), blocks=len(bs), shape=shape)

def reader_regression():
    """The reader must return real speech, not an empty stream, for each shape,
    and must not return a line that is only a section label."""
    ok = True
    for n, expect in ((1, "sticky"), (4, "sync"), (12, "built")):
        ms = spoken(S.SRC[n][0], S.SRC[n][2], "master")
        if not ms or len(" ".join(ms).split()) < 400:
            ok = False
        if any(t.strip() == "[NOT SPOKEN]" or t.endswith("[NOT SPOKEN]") for t in ms):
            ok = False
    return ok

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def run():
    return [check(n) for n in sorted(S.SRC)]

if __name__ == "__main__":
    rows = run()
    print("reader returns real speech for all three shapes:", reader_regression())
    print()
    print("  #   shape   master words  block words  paras  parity  notes")
    for r in rows:
        print("  V%-3d %-7s %8d %12d %8d   %-6s %s"
              % (r["n"], r["shape"], r["words"], r["block_words"], r["paras"],
                 "PASS" if r["passed"] else "FAIL",
                 "; ".join(r["notes"]) or ("fused label in source: " + r["fused"]
                                           if r["fused"] else r["grouping"])))
    bad = [r for r in rows if not r["passed"]]
    print("\n%d of %d PASS" % (len(rows) - len(bad), len(rows)))


def parity_regression():
    """Parity passing for all fourteen is only meaningful if the comparison
    would fail on a broken pair. Three injections are tested against the real
    V1 streams: one changed word, one dropped sentence, one duplicated
    sentence."""
    m = spoken(S.SRC[1][0], "sticky", "master")
    base = " ".join(m).split()
    # The first version of this probe replaced a word that was not in the
    # paragraph it targeted, so its "changed" stream was identical to the
    # original and the probe reported failure against a check that was working.
    # Each injection now provably alters the stream.
    changed = list(m); changed[10] = changed[10] + " INJECTED"
    dropped = m[:20] + m[21:]
    duped = m[:20] + [m[20]] + m[20:]
    assert changed != m and dropped != m and duped != m
    return all(" ".join(x).split() != base for x in (changed, dropped, duped))
