# -*- coding: utf-8 -*-
"""Parse the three FINAL Sticky Realization masters straight out of the supplied .docx.

The spoken wording is never retyped here. It is read from the source documents so that
a diff against the upload is a byte comparison rather than a proofread.

Two of the source documents carry a formatting defect: a section label ran into the
first spoken sentence with no paragraph break ("READ THE LAST 90 DAYSThen look at..."
in V2, "KEEP THE PROOF, NOT THE PROPERTYSo here is the rule..." in V3). The same fusion
appears in the matching thought-block file, so it is in the source, not in one export.
FUSED below splits them. That is a formatting separation, not a wording change: the
label is NOT SPOKEN and the spoken text is preserved character for character.
"""
import zipfile, re, html, hashlib, io, os

UP = "/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
SRC = {
 1: dict(master="6b3a6c6c-V1_FINAL_Sticky_Realization_Recording_Master.docx",
         blocks="315ff2f2-V1_FINAL_Sticky_Realization_Thought_Blocks.docx",
         master_sha="3d2fae1d7a79d145d959cb33bf9c553241f95b770ac600622a9b9cc98fa186b6",
         blocks_sha="f5499eb9df8317a3d39c080927b1c840e4839055118f32cf0460ea38f59379be"),
 2: dict(master="83f978da-V2_FINAL_Sticky_Realization_Recording_Master.docx",
         blocks="56807557-V2_FINAL_Sticky_Realization_Thought_Blocks.docx",
         master_sha="3fc351e9d481e6eb20d1a78ebdbde16c034a7d10daf1f94b99edd53834d353f7",
         blocks_sha="34d6ee0956be2ca37a4f35407aed1702a308c2c0eaeb989fbaa86665461a46e2"),
 3: dict(master="0e3eb62b-V3_FINAL_Sticky_Realization_Recording_Master.docx",
         blocks="4b6a1e14-V3_FINAL_Sticky_Realization_Thought_Blocks.docx",
         master_sha="4500a3a0ab7a005abf8595cf7c76bf9faa25e9901a1f021fb96fcf528f46f139",
         blocks_sha="8ff72c32e738ef71d18d224cb6a6d949e9d9ca601cdb6927094b1c8fd3e1d00e"),
}

# label text -> the spoken sentence it was fused to, in the source documents
FUSED = {
 "READ THE LAST 90 DAYS": "Then look at the last 90 days of your actual work.",
 "KEEP THE PROOF, NOT THE PROPERTY": "So here is the rule: keep the proof, not the property.",
}

def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def paragraphs(path):
    x = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", x, re.S):
        t = html.unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S))).strip()
        if t:
            out.append(t)
    return out

def is_label(t):
    """A section label is short, fully upper-case, and carries no sentence punctuation."""
    return t.isupper() and len(t.split()) <= 8 and not t.endswith(".")

def split_fused(t):
    for lab, first in FUSED.items():
        if t.startswith(lab) and t[len(lab):].lstrip() == first:
            return lab, first
    return None

def master(n):
    """[(section_label, [spoken paragraph, ...]), ...] for one video."""
    ts = paragraphs(UP + SRC[n]["master"])
    head, body = ts[:4], ts[4:]
    out, cur, paras = [], None, []
    for t in body:
        f = split_fused(t)
        if f:
            if cur is not None:
                out.append((cur, paras))
            cur, paras = f[0], [f[1]]
            continue
        if is_label(t):
            if cur is not None:
                out.append((cur, paras))
            cur, paras = t, []
            continue
        paras.append(t)
    if cur is not None:
        out.append((cur, paras))
    return head, [(s, ps) for s, ps in out if ps]

def blocks(n):
    """[(section_label, [block, ...]), ...] exactly as supplied. No rewriting."""
    ts = paragraphs(UP + SRC[n]["blocks"])
    out, cur, bs = [], None, []
    for t in ts[4:]:
        if t.endswith("[NOT SPOKEN]"):
            lab = t[: -len("[NOT SPOKEN]")].strip()
            if re.match(r"^BLOCK\s+\d+$", lab):
                continue
            if lab.startswith("RECORDING DIRECTION"):
                continue
            if cur is not None:
                out.append((cur, bs))
            cur, bs = lab, []
            continue
        f = split_fused(t)
        if f:
            if cur is not None:
                out.append((cur, bs))
            cur, bs = f[0], [f[1]]
            continue
        bs.append(t)
    if cur is not None:
        out.append((cur, bs))
    return [(s, b) for s, b in out if b]

def spoken(n):
    return [(s, p) for s, ps in master(n)[1] for p in ps]

def words(n):
    return sum(len(p.split()) for _, p in spoken(n))

SENT_SPLIT = re.compile(u"(?<=[.?!][\u201d\u2019\"')\\]])\\s+|(?<=[.?!])\\s+")

def sentences(p):
    """Split on sentence punctuation, including punctuation inside a closing quote.

    The masters quote whole sentences, so a sentence can end … unit.” with the
    period before the closing curly quote. A plain (?<=[.?!])\\s+ lookbehind sees
    the quote character, not the period, and silently joins that sentence to the
    next one. That made a Shorts line that really was a verbatim consecutive run
    fail the verbatim check, because the line re-split differently from the way
    the master had been split. sentence_split_regression() proves the fix.
    """
    return [s.strip() for s in SENT_SPLIT.split(p.strip()) if s.strip()]

def sentence_split_regression():
    probe = (u"Imagine this sentence on a resume: \u201cI own the QBR process.\u201d "
             u"Inside the company, that may mean a lot.")
    return len(sentences(probe)) == 2

def master_sentences(n):
    return [s for _, p in spoken(n) for s in sentences(p)]

def verify(n):
    """Blocks must reproduce the master word for word, in order."""
    a = " ".join(p for _, p in spoken(n)).split()
    b = " ".join(x for _, bs in blocks(n) for x in bs).split()
    first = None
    if a != b:
        first = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]),
                     min(len(a), len(b)))
    return len(a), len(b), (a == b), first

def checksums_ok():
    bad = []
    for n, d in SRC.items():
        for k in ("master", "blocks"):
            got = sha256(UP + d[k])
            if got != d[k + "_sha"]:
                bad.append((n, k, got))
    return bad

if __name__ == "__main__":
    bad = checksums_ok()
    print("source checksums:", "all match" if not bad else bad)
    for n in (1, 2, 3):
        h, secs = master(n)
        nb = sum(len(b) for _, b in blocks(n))
        wa, wb, ok, first = verify(n)
        print("V%d  %2d sections  %3d spoken paras  %3d blocks  %4d words  parity %s%s"
              % (n, len(secs), sum(len(p) for _, p in secs), nb, wa,
                 "EXACT" if ok else "MISMATCH",
                 "" if ok else " at token %s (blocks %d)" % (first, wb)))
        print("     title: %s" % h[1])
        print("     %s" % h[3])
