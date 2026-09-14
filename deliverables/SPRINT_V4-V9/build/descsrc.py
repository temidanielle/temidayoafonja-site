# -*- coding: utf-8 -*-
"""The approved revised YouTube descriptions, September 14, 2026.

These supersede the description copy this build previously authored. The
wording, emojis, resource names and URLs are taken verbatim; nothing here
rewrites them. The parser only separates the blocks so each package can
carry its own.
"""
import os, re, hashlib
from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "_source_desc",
                   "NEW_V4-V9_YouTube_Descriptions_REVISED_Resources_"
                   "Emojis_COMBINED.docx")
SHA = "00dc05299438b4770ead7751c28ac1684f803bbf913f30d55b71d2b6ef26be0d"

HEAD = "CAPABILITY FORMATION | YOUTUBE"
START = "COPY-READY YOUTUBE DESCRIPTION"
WATCH, PLAYLIST = "\U0001F3A5 Watch next", "\U0001F4FA Playlist"
NOTE = "PUBLISHING NOTE"
VIDEO_URL = "[PASTE VIDEO URL AFTER UPLOAD]"
PLAYLIST_URL = "[PASTE PLAYLIST URL AFTER UPLOAD]"
NUM = re.compile(r"^NEW V(\d+) \| FORMER ROADMAP V(\d+)$")

# The utility emojis, and what each one labels. They are navigation
# devices, not decoration, so the set is closed.
EMOJI = {"\U0001F9ED": "Free career decision check",
         "\U0001F9F0": "Free evidence starter",
         "\U0001F4D8": "Career evidence system"}
_CACHE = {}


def sha256(p=SRC):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _paras():
    return [p.text.rstrip() for p in Document(SRC).paragraphs]


def read():
    """new public number -> the approved description block."""
    if _CACHE:
        return _CACHE
    ps = _paras()
    starts = [i for i, t in enumerate(ps) if t == HEAD]
    for k, i in enumerate(starts):
        j = starts[k + 1] if k + 1 < len(starts) else len(ps)
        blk = [t for t in ps[i:j] if t.strip()]
        m = NUM.match(blk[1])
        n, former = int(m.group(1)), int(m.group(2))
        title = blk[2]
        thumb = blk[3].split(":", 1)[1].strip()
        b0 = blk.index(START) + 1
        body, resource = [], None
        k2 = b0
        while blk[k2] != WATCH:
            t = blk[k2]
            if t[:1] in EMOJI:
                resource = dict(emoji=t[:1], label=t[1:].strip(),
                                name=blk[k2 + 1], blurb=blk[k2 + 2],
                                url=blk[k2 + 3])
                k2 += 4
                continue
            body.append(t)
            k2 += 1
        w = blk.index(WATCH)
        p = blk.index(PLAYLIST)
        nt = blk.index(NOTE)
        _CACHE[n] = dict(
            new=n, former=former, title=title, thumbnail=thumb, body=body,
            resource=resource, watch_next=blk[w + 1], watch_url=blk[w + 2],
            playlist=blk[p + 1], playlist_url=blk[p + 2], note=blk[nt + 1])
    return _CACHE


def block(n):
    return read()[n]


def lines(n):
    """The copy-ready description, in order, exactly as approved."""
    d = block(n)
    out = list(d["body"])
    if d["resource"]:
        r = d["resource"]
        out += ["", r["emoji"] + " " + r["label"], r["name"], r["blurb"],
                r["url"]]
    out += ["", WATCH, d["watch_next"], d["watch_url"],
            "", PLAYLIST, d["playlist"], d["playlist_url"]]
    return out


if __name__ == "__main__":
    print("source sha256 %s  %s" % (sha256(), "verified" if sha256() == SHA
                                    else "MISMATCH"))
    for n, d in sorted(read().items()):
        r = d["resource"]
        print("\nNEW V%d (former V%d)  %s" % (n, d["former"], d["title"]))
        print("   thumbnail : %s" % d["thumbnail"])
        print("   body      : %d paragraphs" % len(d["body"]))
        print("   resource  : %s" % (("%s %s -> %s" % (r["emoji"], r["name"],
                                                       r["url"]))
                                     if r else "none, intentionally"))
        print("   watch next: %s" % d["watch_next"])
        print("   playlist  : %s | %s" % (d["playlist"], d["playlist_url"]))
