#!/usr/bin/env python3
"""
Reconstruct the Capability Formation Field Kit PDF from the original.

The original was produced by ReportLab. This script reverse-engineers a
ReportLab generator from it: every page's content stream is parsed into a
list of drawing primitives (positioned text runs, filled rects, stroked
lines) and replayed onto a fresh ReportLab canvas at identical coordinates,
fonts, sizes and colours. The document uses only base-14 fonts (identical
metrics in ReportLab) and contains no raster images, so the replay is faithful.

The ONLY intentional content change is the first sentence of the boundary
rule. The original paragraph read:

    The boundary rule: within a point or two of the line on either axis, treat
    yourself as standing on the boundary and read both neighboring states.
    Boundary positions move fastest, in both directions.

The first sentence is replaced with:

    The boundary rule: if either score falls between 17 and 21, even a high one,
    treat yourself as standing on the boundary and read both neighboring states.

The second sentence is preserved verbatim. Same font (Helvetica 10), same
colour (navy #0F2347), same left margin (x=54), same leading (13pt), same
frame width (504pt) -> the paragraph re-wraps to two lines exactly as the
original did, so nothing below it moves.
"""
import re, zlib, sys
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import Color
import fitz  # pymupdf, used only to lift the interactive form-field specs

SRC = sys.argv[1] if len(sys.argv) > 1 else "original.pdf"
OUT = sys.argv[2] if len(sys.argv) > 2 else "new.pdf"

PAGE_W, PAGE_H = 612.0, 792.0
FRAME_LEFT = 54.0
FRAME_WIDTH = 504.0            # footer rule spans x=54..558
BOUNDARY_FONT = "Helvetica"
BOUNDARY_SIZE = 10.0
BOUNDARY_LEADING = 13.0        # y=268 -> y=255
BOUNDARY_Y_TOP = 268.0

OLD_L1 = "The boundary rule: within a point or two of the line on either axis, treat yourself as standing on the boundary and"
OLD_L2 = "read both neighboring states. Boundary positions move fastest, in both directions."
NEW_PARAGRAPH = ("The boundary rule: if either score falls between 17 and 21, even a high one, "
                 "treat yourself as standing on the boundary and read both neighboring states. "
                 "Small changes matter more near a boundary by construction.")   # EDIT B (v1.2)

def wrap(text, font, size, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if stringWidth(t, font, size) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

# ---------------------------------------------------------------- PDF parsing
data = open(SRC, "rb").read()
# Byte offsets of every "N 0 obj" so we can read streams by exact /Length
# (a naive `.*?endstream` regex truncates compressed streams whose bytes
# happen to contain the markers "endobj"/"endstream").
offsets = {int(m.group(1)): m.start() for m in re.finditer(rb'(\d+)\s+0\s+obj', data)}

def header(num):
    s = offsets[num]
    e_stream = data.find(b'stream', s)
    e_obj = data.find(b'endobj', s)
    end = e_stream if (e_stream != -1 and (e_obj == -1 or e_stream < e_obj)) else e_obj
    return data[s:end]

# raw_objs headers (dict portion only) — safe for the page tree / font lookups
raw_objs = {n: header(n) for n in offsets}

def basefont(n):
    b = raw_objs.get(n, b"")
    bm = re.search(rb'/BaseFont\s*/([A-Za-z0-9\-+,]+)', b)
    return bm.group(1).decode() if bm else None

def resolve_length(num, hdr):
    m = re.search(rb'/Length\s+(\d+)\s+0\s+R', hdr)   # indirect length
    if m:
        lh = header(int(m.group(1)))                  # "N 0 obj\n<int>\n"
        im = re.search(rb'obj\s*(\d+)', lh)
        return int(im.group(1)) if im else None
    m = re.search(rb'/Length\s+(\d+)', hdr)           # direct length
    return int(m.group(1)) if m else None

def ascii85(raw):
    import base64
    body = raw.strip()
    if body.startswith(b'<~'):
        body = body[2:]
    end = body.find(b'~>')
    if end != -1:
        body = body[:end]
    body = b"".join(body.split())               # drop whitespace
    return base64.a85decode(body, adobe=False)

def apply_filters(raw, hdr):
    m = re.search(rb'/Filter\s*(\[[^\]]*\]|/\w+)', hdr)
    if not m:
        return raw
    names = re.findall(rb'/(\w+)', m.group(1))
    for f in names:
        f = f.decode()
        if f in ("FlateDecode", "Fl"):
            raw = zlib.decompress(raw)
        elif f in ("ASCII85Decode", "A85"):
            raw = ascii85(raw)
        else:
            raise ValueError("unhandled filter " + f)
    return raw

def stream_of(objnum):
    s = offsets[objnum]
    hdr = header(objnum)
    st = data.find(b'stream', s)
    # skip the EOL after 'stream' (\r\n or \n)
    p = st + len('stream')
    if data[p:p+2] == b'\r\n':
        p += 2
    elif data[p:p+1] in (b'\n', b'\r'):
        p += 1
    length = resolve_length(objnum, hdr)
    raw = data[p:p+length] if length else data[p:data.find(b'endstream', p)]
    return apply_filters(raw, hdr)

# page order
cat = [n for n, b in raw_objs.items() if b'/Catalog' in b][0]
proot = int(re.search(rb'/Pages\s+(\d+)\s+0\s+R', raw_objs[cat]).group(1))
order = []
def walk(n):
    b = raw_objs[n]
    if b'/Type' in b and b'/Pages' in b and b'/Kids' in b:
        kids = re.findall(rb'(\d+)\s+0\s+R', re.search(rb'/Kids\s*\[([^\]]*)\]', b).group(1))
        for k in kids:
            walk(int(k))
    else:
        order.append(n)
walk(proot)

def fontmap(pageobj):
    b = raw_objs[pageobj]
    fm = re.search(rb'/Font\s*<<(.*?)>>', b, re.S)
    if fm:
        dict_bytes = fm.group(1)
    else:
        # indirect font resource: /Font N 0 R  ->  object N is the tag dict
        ind = re.search(rb'/Font\s+(\d+)\s+0\s+R', b)
        if not ind:
            return {}
        fb = raw_objs[int(ind.group(1))]
        dm = re.search(rb'<<(.*)>>', fb, re.S)
        dict_bytes = dm.group(1) if dm else b""
    # tags are arbitrary names (F1.., but also helv/cour/hebo), not just F\d+
    return {k.decode(): basefont(int(v))
            for k, v in re.findall(rb'/([A-Za-z0-9]+)\s+(\d+)\s+0\s+R', dict_bytes)}

# ---------------------------------------------------------------- tokenizer
def tokenize(s):
    """Yield (kind, value) tokens for a decoded content stream (bytes)."""
    i, n = 0, len(s)
    while i < n:
        c = s[i:i+1]
        if c in b" \t\r\n":
            i += 1; continue
        if c == b"(":                                   # literal string
            depth, j, buf = 1, i+1, bytearray()
            while j < n and depth:
                ch = s[j]
                if ch == 0x5c:                          # backslash escape
                    nxt = s[j+1:j+2]
                    mp = {b"n": b"\n", b"r": b"\r", b"t": b"\t", b"b": b"\b",
                          b"f": b"\f", b"(": b"(", b")": b")", b"\\": b"\\"}
                    if nxt in mp:
                        buf += mp[nxt]; j += 2; continue
                    mo = re.match(rb'[0-7]{1,3}', s[j+1:j+4])
                    if mo:
                        buf.append(int(mo.group(0), 8) & 0xFF); j += 1 + len(mo.group(0)); continue
                    j += 1; continue
                if ch == 0x28:
                    depth += 1
                elif ch == 0x29:
                    depth -= 1
                    if depth == 0:
                        j += 1; break
                buf.append(ch); j += 1
            yield ("str", bytes(buf)); i = j; continue
        if c == b"[":
            j, parts = i+1, []
            while j < n and s[j:j+1] != b"]":
                if s[j:j+1] == b"(":
                    depth, k, buf = 1, j+1, bytearray()
                    while k < n and depth:
                        ch = s[k]
                        if ch == 0x5c:
                            buf.append(s[k+1]); k += 2; continue
                        if ch == 0x28: depth += 1
                        elif ch == 0x29:
                            depth -= 1
                            if depth == 0: k += 1; break
                        buf.append(ch); k += 1
                    parts.append(bytes(buf)); j = k
                else:
                    j += 1
            yield ("arr", parts); i = j+1; continue
        if c == b"/":
            m = re.match(rb'/([^\s/\[\]()<>{}]+)', s[i:])
            if m:
                yield ("name", m.group(1).decode()); i += m.end(); continue
            i += 1; continue
        if c in b"-+.0123456789":
            m = re.match(rb'[-+]?[0-9]*\.?[0-9]+', s[i:])
            if m:
                yield ("num", float(m.group(0))); i += m.end(); continue
        m = re.match(rb"[A-Za-z'\"*]+", s[i:])
        if m:
            yield ("op", m.group(0).decode()); i += m.end(); continue
        i += 1

# ---------------------------------------------------------------- matrix maths
IDENT = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
def mmul(A, B):
    """Return A then B (both [a b c d e f])."""
    a1, b1, c1, d1, e1, f1 = A
    a2, b2, c2, d2, e2, f2 = B
    return (a1*a2 + b1*c2,
            a1*b2 + b1*d2,
            c1*a2 + d1*c2,
            c1*b2 + d1*d2,
            e1*a2 + f1*c2 + e2,
            e1*b2 + f1*d2 + f2)
def xform(M, x, y):
    return (M[0]*x + M[2]*y + M[4], M[1]*x + M[3]*y + M[5])

# ---------------------------------------------------------------- interpreter
UNMAPPED = set()
def interpret(stream, fonts):
    """Return list of primitives for one page.

    Primitives:
      ('text', matrix6, font, size, fill, string)     matrix6 = textmatrix o CTM
      ('path', mode, subpaths, stroke, fill, lw)       subpaths built in device space
    """
    prims = []
    st = {"fill": (0, 0, 0), "stroke": (0, 0, 0), "lw": 1.0,
          "font": "Helvetica", "size": 10.0}
    ctm = IDENT
    gstack = []
    tmat = IDENT       # text matrix
    lmat = IDENT       # text line matrix
    leading = 0.0
    subpaths = []      # list of subpaths; each is list of ('m'/'l'/'c', pts...) in device space
    cur = None
    ops = []

    def moveto(x, y):
        nonlocal cur
        cur = [("m", xform(ctm, x, y))]
        subpaths.append(cur)
    def lineto(x, y):
        if cur is None: moveto(x, y)
        else: cur.append(("l", xform(ctm, x, y)))
    def curveto(x1, y1, x2, y2, x3, y3):
        if cur is None: moveto(x1, y1)
        cur.append(("c", xform(ctm, x1, y1), xform(ctm, x2, y2), xform(ctm, x3, y3)))
    def rect(x, y, w, h):
        nonlocal cur
        p = [("m", xform(ctm, x, y)), ("l", xform(ctm, x+w, y)),
             ("l", xform(ctm, x+w, y+h)), ("l", xform(ctm, x, y+h)), ("h",)]
        subpaths.append(p); cur = p
    def emit_path(mode):
        nonlocal subpaths, cur
        if subpaths:
            if mode == "fillstroke":
                prims.append(("path", "fill", subpaths, st["stroke"], st["fill"], st["lw"]))
                prims.append(("path", "stroke", subpaths, st["stroke"], st["fill"], st["lw"]))
            else:
                prims.append(("path", mode, subpaths, st["stroke"], st["fill"], st["lw"]))
        subpaths = []; cur = None
    def draw_text(txt):
        m = mmul(tmat, ctm)
        prims.append(("text", m, st["font"], st["size"], st["fill"], txt))

    for kind, val in tokenize(stream):
        if kind in ("num", "name", "str", "arr"):
            ops.append((kind, val)); continue
        op = val
        nums = [v for k, v in ops if k == "num"]
        names = [v for k, v in ops if k == "name"]
        strs = [v for k, v in ops if k == "str"]
        arrs = [v for k, v in ops if k == "arr"]
        if op == "q":
            gstack.append((dict(st), ctm))
        elif op == "Q":
            if gstack:
                s2, ctm = gstack.pop(); st.update(s2)
        elif op == "cm" and len(nums) == 6:
            ctm = mmul(tuple(nums), ctm)
        elif op == "rg" and len(nums) == 3:
            st["fill"] = tuple(nums)
        elif op == "g" and len(nums) == 1:
            st["fill"] = (nums[0],) * 3
        elif op == "k" and len(nums) == 4:
            st["fill"] = ("cmyk", tuple(nums))
        elif op == "RG" and len(nums) == 3:
            st["stroke"] = tuple(nums)
        elif op == "G" and len(nums) == 1:
            st["stroke"] = (nums[0],) * 3
        elif op == "K" and len(nums) == 4:
            st["stroke"] = ("cmyk", tuple(nums))
        elif op == "w" and nums:
            st["lw"] = nums[0]
        elif op == "re" and len(nums) == 4:
            rect(*nums)
        elif op == "m" and len(nums) == 2:
            moveto(*nums)
        elif op == "l" and len(nums) == 2:
            lineto(*nums)
        elif op == "c" and len(nums) == 6:
            curveto(*nums)
        elif op == "v" and len(nums) == 4:      # first ctrl = current pt
            last = cur[-1][-1] if cur else (0, 0)
            curveto(last[0], last[1], nums[0], nums[1], nums[2], nums[3])
        elif op == "y" and len(nums) == 4:      # second ctrl = endpoint
            curveto(nums[0], nums[1], nums[2], nums[3], nums[2], nums[3])
        elif op == "h":
            if cur is not None: cur.append(("h",))
        elif op in ("f", "F", "f*"):
            emit_path("fill")
        elif op in ("b", "b*", "B", "B*"):
            emit_path("fillstroke")
        elif op in ("S", "s"):
            emit_path("stroke")
        elif op == "n":
            subpaths = []; cur = None
        elif op == "BT":
            tmat = lmat = IDENT
        elif op == "ET":
            pass
        elif op == "Tf" and names and nums:
            if names[-1] not in fonts:
                UNMAPPED.add(names[-1])
            st["font"] = fonts.get(names[-1], "Helvetica"); st["size"] = nums[-1]
        elif op == "TL" and nums:
            leading = nums[0]
        elif op == "Tm" and len(nums) == 6:
            tmat = lmat = tuple(nums)
        elif op in ("Td", "TD") and len(nums) >= 2:
            if op == "TD":
                leading = -nums[1]
            lmat = mmul((1, 0, 0, 1, nums[0], nums[1]), lmat); tmat = lmat
        elif op == "T*":
            lmat = mmul((1, 0, 0, 1, 0, -leading), lmat); tmat = lmat
        elif op == "Tj" and strs:
            draw_text(strs[-1].decode("latin-1"))
        elif op == "'" and strs:                # T* then show
            lmat = mmul((1, 0, 0, 1, 0, -leading), lmat); tmat = lmat
            draw_text(strs[-1].decode("latin-1"))
        elif op == "TJ" and arrs:
            draw_text("".join(p.decode("latin-1") for p in arrs[-1]))
        ops = []
    return prims

# ---------------------------------------------------------------- boundary edit
new_lines = wrap(NEW_PARAGRAPH, BOUNDARY_FONT, BOUNDARY_SIZE, FRAME_WIDTH)
assert len(new_lines) == 2, f"expected 2 lines, got {len(new_lines)}: {new_lines}"
for L in new_lines:
    assert stringWidth(L, BOUNDARY_FONT, BOUNDARY_SIZE) <= FRAME_WIDTH

def apply_boundary_edit(prims):
    out, changed = [], 0
    for p in prims:
        if p[0] == "text" and p[5] == OLD_L1:
            out.append(("text", p[1], p[2], p[3], p[4], new_lines[0])); changed += 1
        elif p[0] == "text" and p[5] == OLD_L2:
            out.append(("text", p[1], p[2], p[3], p[4], new_lines[1])); changed += 1
        else:
            out.append(p)
    return out, changed

# --------------------------------------------------- Instrument v1.1 edits ----
# Six scoped text corrections for the v1.1 reissue. Each is a fixed-position
# text swap on the replayed primitives — no reflow of surrounding content, page
# count unchanged. Line breaks below are pre-measured at the box/column widths.
NAVY = (0.058824, 0.137255, 0.278431)
CREAM = (0.960784, 0.941176, 0.909804)

def _tp(x, f, font, size, fill, s):
    return ("text", (1.0, 0.0, 0.0, 1.0, x, f), font, size, fill, s)

# EDIT 1 (page 5) — evidence rule -> evidence protocol (2 lines -> 3, fits box)
E1_OLD1 = ("The evidence rule: under each score, write the single piece of evidence "
           "from the last ninety days that supports it. Any")
E1_OLD2 = ("3 or higher without evidence drops to a 2 (a 1 or a 2 needs no defense). "
           "An intention is not evidence.")
E1_NEW = [
    "The evidence protocol: under each score, write the evidence from the last ninety days. Every score, in both",
    "directions. A 4 or 5 needs a clear positive instance. A 3 needs the mixed or inconsistent pattern. A 1 or 2 needs what",
    "happened instead, a counterexample, or no qualifying instance. An intention is not evidence.",
]
# EDIT 2 (page 6) — add uncertainty rule above the "guess with decimal points" line
E2_ANCHOR = "A score without an evidence line is a guess with decimal points."
E2_NEW = [
    "If you cannot support a score either way, write your most defensible number and add a question mark: 3?, 4?, 2?. Do",
    "not force it downward and do not default to a 3. One or two marked items make the axis provisional; three or more",
    "mean you do not have ninety days of evidence on that axis. A finding about the window, not a low score.",
]
# EDIT 3 (page 9) — drop retention/effectiveness clause
E3_OLD = [
    "Four states, one common fact: the number was a map, and the move it pointed to worked. Full cases, including the",
    "organizational engagements behind the retention and effectiveness numbers, live at",
    "temidayoafonja.com/case-studies.",
]
E3_NEW = [
    "Four states, one common fact: the number was a map, and the move it pointed to worked. Full cases live at",
    "temidayoafonja.com/case-studies.",
]
# EDIT 4 (page 19) — Cohort -> live Capability Position Read
E4_OLD = [
    "self-assessment ever written. A professional read exists for exactly this reason. When the Capability Formation",
    "Cohort opens, that is the seat it fills, and Field Kit owners hear first.",
]
E4_NEW = [
    "self-assessment ever written. A calibrated read exists for exactly this reason. That is what the live Capability",
    "Position Read does: you score, you are corrected against evidence, and you score again.",
]
# EDIT 5 (page 23) — Cohort -> Capability Position Read (centred, cream)
E5_OLD = [
    "Both belong in other hands: a written read of your position, live calibration, and a dated",
    "ninety-day move plan. That is what the Capability Formation Cohort is being built to do,",
    "and Field Kit owners get first notice when it opens.",
]
# v1.2.4 page-23 close: the E5 block, the pointer, and the old "Until then" line
# are replaced by three paragraphs (P1/P2 body, P3 bold). Copy is verbatim; the
# closing gold statement + signature shift down into the page's lower third.
E5_CENTER = 306.0
E5_WRAP = 440.0
P23_P1 = ("Both belong in other hands: a live calibration, where you are corrected against "
          "evidence rather than against yourself. That is what the Capability Position Read does. "
          "The free live session at temidayoafonja.com runs the guided version in a room. "
          "The Private Capability Position Read runs it one to one, where Temidayo interprets "
          "your evidence with you and writes the Next-Move Note your self-read cannot produce on its own.")
P23_P2 = ("What the Field Kit gives you that neither session does is the system you keep. "
          "A live room happens once. This kit rescores every quarter. The scores move, "
          "the evidence lines change, and the position you are managing stays visible to you "
          "long after the room is over.")
P23_P3 = "Run the loop. A rescored quarter is worth more than a rushed next step."
P23_OLD_CLOSE = "Until then, run the loop. A rescored quarter is worth more than a rushed next step."

def _wrap_page(text, font, size, width):
    words = text.split(); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if stringWidth(t, font, size) <= width: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines
# EDIT 6 (page 2) — Cohort -> session (P.S. line, drawn glyph-by-glyph)
E6_OLD = "people who bring them get first notice when a Cohort opens."
E6_NEW = "people who bring them get first notice when a session opens."
E6_FONT, E6_SIZE, E6_F, E6_X = "Helvetica-Oblique", 10.0, 269.5, 54.0

def apply_v11_edits(idx, prims):
    applied = []
    def drop(strings):
        s = set(strings)
        return [p for p in prims if not (p[0] == "text" and p[5] in s)]
    def find(s):
        for p in prims:
            if p[0] == "text" and p[5] == s:
                return p
        return None

    if idx == 4:                                   # EDIT 1
        p1, p2 = find(E1_OLD1), find(E1_OLD2)
        if p1 and p2:
            m1, m2, fn, sz, fl = p1[1], p2[1], p1[2], p1[3], p1[4]
            lead = m1[5] - m2[5]
            prims = drop([E1_OLD1, E1_OLD2])
            prims += [_tp(m1[4], m1[5], fn, sz, fl, E1_NEW[0]),
                      _tp(m2[4], m2[5], fn, sz, fl, E1_NEW[1]),
                      _tp(m2[4], m2[5] - lead, fn, sz, fl, E1_NEW[2])]
            applied.append("EDIT1")
    elif idx == 5:                                 # EDIT 2 (addition)
        a = find(E2_ANCHOR)
        if a:
            af = a[1][5]
            for k, line in enumerate(E2_NEW):      # 3 lines, bottom just above anchor
                f = af + 45.0 - k * 11.5
                prims = prims + [_tp(54.0, f, "Helvetica-Oblique", 9.5, NAVY, line)]
            applied.append("EDIT2")
    elif idx == 8:                                 # EDIT 3
        p = find(E3_OLD[0])
        if p:
            fn, sz, fl = p[2], p[3], p[4]
            m = [find(s)[1] for s in E3_OLD]
            prims = drop(E3_OLD)
            prims += [_tp(m[0][4], m[0][5], fn, sz, fl, E3_NEW[0]),
                      _tp(m[1][4], m[1][5], fn, sz, fl, E3_NEW[1])]
            applied.append("EDIT3")
    elif idx == 18:                                # EDIT 4
        p = find(E4_OLD[0])
        if p:
            fn, sz, fl = p[2], p[3], p[4]
            m = [find(s)[1] for s in E4_OLD]
            prims = drop(E4_OLD)
            prims += [_tp(m[0][4], m[0][5], fn, sz, fl, E4_NEW[0]),
                      _tp(m[1][4], m[1][5], fn, sz, fl, E4_NEW[1])]
            applied.append("EDIT4")
    elif idx == 22:                                # EDIT 5 (v1.2.4) — page-23 close rewritten
        p = find(E5_OLD[0])
        if p:
            fn, sz, fl = p[2], p[3], p[4]          # Helvetica 11, cream
            prims = drop(E5_OLD)                    # remove the old cohort block
            prims = [q for q in prims               # remove the old bold closing line (now P3)
                     if not (q[0] == "text" and q[5] == P23_OLD_CLOSE)]
            H = 792.0; LEAD = 15.6; GAP = 27.6
            # Shift the closing gold statement + signature down by a uniform delta.
            # These source lines are placed glyph-by-glyph, so match them by their
            # original baseline band (yTop 515..585: gold 521.2, name 561.2, url 578.2)
            # rather than by string. New tops: 624 / 664 / 681 => +102.8pt.
            DELTA = 102.8
            def shifted(q):
                if q[0] == "text" and 515.0 <= (H - q[1][5]) <= 585.0:
                    mm = list(q[1]); mm[5] -= DELTA
                    return ("text", tuple(mm), q[2], q[3], q[4], q[5])
                return q
            prims = [shifted(q) for q in prims]
            def place(text, font, size, y_top):
                y = y_top; out = []
                for ln in _wrap_page(text, font, size, E5_WRAP):
                    x = E5_CENTER - stringWidth(ln, font, size) / 2.0
                    out.append(_tp(x, H - y, font, size, fl, ln)); y += LEAD
                return out, y - LEAD
            b1, e1 = place(P23_P1, "Helvetica", 11.0, 419.6)
            b2, e2 = place(P23_P2, "Helvetica", 11.0, e1 + GAP)
            b3, e3 = place(P23_P3, "Helvetica-Bold", 11.0, e2 + GAP)
            prims += b1 + b2 + b3
            applied.append("EDIT5")
    elif idx == 1:                                 # EDIT 6 (per-glyph P.S. line)
        glyphs = [p for p in prims if p[0] == "text" and abs(p[1][5] - E6_F) < 0.3
                  and p[2] == E6_FONT and abs(p[3] - E6_SIZE) < 0.1
                  and p[1][4] >= E6_X - 0.5]
        recon = "".join(p[5] for p in sorted(glyphs, key=lambda q: q[1][4]))
        if recon == E6_OLD:
            keep = [p for p in prims if p not in glyphs]
            keep.append(_tp(E6_X, E6_F, E6_FONT, E6_SIZE, glyphs[0][4], E6_NEW))
            prims = keep
            applied.append("EDIT6")
    return prims, applied

# ================= Instrument v1.2 reconciliation patch =================
NAVY12 = (0.058824, 0.137255, 0.278431)
GRAY12 = (0.101961, 0.101961, 0.101961)
RUST12 = (0.756863, 0.266667, 0.054902)
GOLD12 = (0.788235, 0.658824, 0.298039)
CREAM12 = (0.960784, 0.941176, 0.909804)

def _tp12(x, f, font, size, fill, s):
    return ("text", (1.0, 0.0, 0.0, 1.0, x, f), font, size, fill, s)

def _close12(a, b, tol=0.02):
    return isinstance(a, tuple) and len(a) == 3 and all(abs(a[i]-b[i]) < tol for i in range(3))

def _pbbox(p):
    xs, ys = [], []
    for sp in p[2]:
        for seg in sp:
            for pt in seg[1:]:
                if isinstance(pt, tuple):
                    xs.append(pt[0]); ys.append(pt[1])
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None

def _swap12(p, old, new):
    return ("text", p[1], p[2], p[3], p[4], new) if (p[0] == "text" and p[5] == old) else p

def _replace_block(prims, old_set, new_text, width, x=None, first_f=None,
                   leading=None, font=None, size=None, fill=None):
    matched = [p for p in prims if p[0] == "text" and p[5] in old_set]
    if len(matched) < len(old_set):
        return prims, 0
    matched.sort(key=lambda p: -p[1][5])
    ref = matched[0]
    X = x if x is not None else ref[1][4]
    F0 = first_f if first_f is not None else ref[1][5]
    fn = font or ref[2]; sz = size or ref[3]; fl = fill if fill is not None else ref[4]
    if leading is None:
        leading = (matched[0][1][5] - matched[1][1][5]) if len(matched) >= 2 else 13.0
    out = [p for p in prims if not (p[0] == "text" and p[5] in old_set)]
    lines = wrap(new_text, fn, sz, width)
    for k, ln in enumerate(lines):
        out.append(_tp12(X, F0 - k*leading, fn, sz, fl, ln))
    return out, len(lines)

CAPTURED_P12 = [None]   # original page-12 prims, kept for building page 24

def _rebuild_page12(prims):                     # EDIT K5 — page 12 becomes the rescore page
    out = []
    for p in prims:
        if p[0] == "text":
            s, fl, fn, sz, f = p[5], p[4], p[2], p[3], p[1][5]
            if s == ">_":
                continue
            if fn == "Courier":
                continue                          # instructions + prompt -> appendix
            if fn == "Helvetica" and abs(sz-10.5) < 0.1 and _close12(fl, GRAY12):
                continue                          # old intro paragraph
            if _close12(fl, RUST12) and "Self-honesty has a ceiling" in s:
                continue                          # old closing tagline
            if abs(f-738) < 2 and "Self-Calibration Prompt" in s:
                continue                          # old title
            if abs(f-718) < 2 and "Put an interrogator" in s:
                continue                          # old subtitle
            if s == "Statements I rescored after calibration, and why:":
                out.append(_tp12(p[1][4], 615.0, fn, sz, fl, s)); continue   # EDIT L: follow the body copy
            out.append(p)
        elif p[0] == "path":
            bb = _pbbox(p)
            if p[1] == "fill" and _close12(p[4], NAVY12) and bb and bb[3] < 650:
                continue                          # navy prompt panel
            if bb and bb[0] >= 53 and bb[2] <= 79 and bb[1] >= 725:
                continue                          # terminal icon box (moves with prompt)
            out.append(p)
        else:
            out.append(p)
    out.append(_tp12(88, 738, "Times-Bold", 19.0, CREAM12, "The Rescore Note"))
    out.append(_tp12(88, 718, "Helvetica", 10.0, GOLD12, "What the three checks changed"))
    body = ("Run the three misreadings against your twelve scores before you accept them. "
            "Where a score does not survive the check, change it and write why. A score you "
            "defended and kept is a finding too, so record those as well.")
    for k, ln in enumerate(wrap(body, "Helvetica", 10.5, 492)):
        out.append(_tp12(54, 675 - k*14, "Helvetica", 10.5, GRAY12, ln))
    out.append(_tp12(54, 66, "Times-BoldItalic", 11.5, RUST12,
                     "Self-honesty has a ceiling. The three checks raise it. They do not remove it."))
    out.append(_tp12(54, 52, "Helvetica-Oblique", 9.8, NAVY12,
                     "If you want something to argue with your numbers, the Self-Calibration Prompt is in the appendix. It is optional."))
    return out

def _build_page24(orig):                        # EDIT K/K6 — appendix page
    SHIFT = -77.0                                # move panel/instructions/prompt below the disclaimer
    out = []
    for p in orig:
        if p[0] == "text":
            s, fl, fn, sz, m, f = p[5], p[4], p[2], p[3], p[1], p[1][5]
            if fn == "Helvetica" and abs(sz-10.5) < 0.1 and _close12(fl, GRAY12):
                continue                          # drop old intro (replaced by disclaimer)
            if _close12(fl, RUST12) and "Self-honesty has a ceiling" in s:
                continue                          # drop tagline
            if abs(f-264.3) < 2 and "Statements I rescored" in s:
                continue                          # rescore heading stays on page 12
            if abs(f-738) < 2 and "Self-Calibration Prompt" in s:
                out.append(_tp12(88, 738, fn, sz, fl, "Appendix: The Self-Calibration Prompt")); continue
            if abs(f-31) < 2 and s.strip() == "12":
                out.append(_tp12(m[4], f, fn, sz, fl, "24")); continue
            if fn == "Courier":
                out.append(("text", (m[0], m[1], m[2], m[3], m[4], f+SHIFT), fn, sz, fl, s)); continue
            out.append(p)                         # keep subtitle, ">_", footer text
        elif p[0] == "path":
            bb = _pbbox(p)
            if p[1] == "fill" and _close12(p[4], NAVY12) and bb and bb[3] < 650:
                newsub = []
                for sp in p[2]:
                    ns = []
                    for seg in sp:
                        if seg[0] == "h":
                            ns.append(seg)
                        else:
                            ns.append((seg[0],) + tuple((pt[0], pt[1]+SHIFT) for pt in seg[1:]))
                    newsub.append(ns)
                out.append(("path", p[1], newsub, p[3], p[4], p[5])); continue
            out.append(p)
        else:
            out.append(p)
    disc = [
        "This appendix is optional. Nothing else in the kit requires an AI assistant, and a read completed without one is complete.",
        "If you use it, notice where the text goes. Your scores leave your control the moment you paste them, and the system on the other side may retain them. Paste numbers and evidence you would be comfortable having stored. Keep out your employer's name, your colleagues' names, and anything you hold in confidence.",
        "What this prompt does is keep asking for evidence after you have stopped asking yourself. That is useful and it is not calibration. It cannot correct its own author any more than you can, and it is built not to advise you. Judgment stays human.",
    ]
    f = 675.0
    for para in disc:
        for ln in wrap(para, "Helvetica", 10.5, 492):
            out.append(_tp12(54, f, "Helvetica", 10.5, GRAY12, ln)); f -= 14.0
        f -= 8.0
    return out

def apply_v12_edits(idx, prims):
    applied = []
    if idx == 2:                                  # K3 contents line
        new = "The three misreadings, worked examples, and the rescore note"
        prims = [_swap12(p, "The three misreadings, worked examples, and the self-calibration prompt", new) for p in prims]
        if any(p[0] == "text" and p[5] == new for p in prims):
            applied.append("K3")
    elif idx == 1:                                # P (v1.2.3) — page 2 P.S. line reworded (1 -> 2 lines) + signature nudge
        # Page 2 text is placed per glyph (see EDIT 6); collect the glyph run on this baseline.
        PF, PX = 474.5, 54.0                       # baseline f (yTop 317.5), left margin
        glyphs = [p for p in prims if p[0] == "text" and abs(p[1][5] - PF) < 0.4
                  and p[2] == "Helvetica" and abs(p[3] - 10.5) < 0.1 and p[1][4] >= PX - 0.5]
        if "".join(g[5] for g in sorted(glyphs, key=lambda g: g[1][4])).startswith("Score honestly"):
            fl = glyphs[0][4]
            SIGDROP = 10.0                          # nudge the signature block down so 2 lines don't crowd it
            keep = []
            for p in prims:
                if p in glyphs:
                    continue
                if p[0] == "text" and 428.0 <= p[1][5] <= 452.0:   # "Temidayo Afonja" (f=448) + "Founder..." (f=433)
                    m = list(p[1]); m[5] -= SIGDROP
                    keep.append(("text", tuple(m), p[2], p[3], p[4], p[5]))
                else:
                    keep.append(p)
            # break rebalanced after "statement" so line 2 is not the widow "ability." (words unchanged)
            newP = ["Score honestly. The number is a map of where you stand. It is real exposure, not a statement",
                    "about your ability."]
            keep += [_tp(PX, PF, "Helvetica", 10.5, fl, newP[0]),
                     _tp(PX, PF - 14.5, "Helvetica", 10.5, fl, newP[1])]   # line 2 at the block's 14.5pt leading
            prims = keep
            applied.append("P")
    elif idx == 6:                                # A
        prims, n = _replace_block(prims,
            {"Nineteen or higher is high on each axis. Your state, not your job title, is what",
             "determines your exposure."},
            "Nineteen or higher is high on each axis. Your current state reveals a form of exposure your job title cannot.",
            460)
        if n: applied.append("A")
    elif idx == 7:                                # C delete
        old = "How you treat exits determines what you attract at entry. Your state decides how soon that matters."
        b = len(prims); prims = [p for p in prims if not (p[0] == "text" and p[5] == old)]
        if len(prims) < b: applied.append("C")
    elif idx == 10:                               # D
        prims, n = _replace_block(prims,
            {'"My Optionality is 14. My capability is trapped in',
             'company language and low outside visibility. That is',
             'a fact about exposure, not a measure of worth. The',
             'score tells me what to fix."'},
            '"My Optionality is 14. A low Optionality score may reflect context-bound capability, weak translation, limited exposure, or a combination. It is not a verdict on my ability or worth. The score tells me what to investigate."',
            235)
        if n: applied.append("D")
    elif idx == 11:                               # K5 page 12 rebuild (+ capture for page 24)
        CAPTURED_P12[0] = list(prims)
        prims = _rebuild_page12(prims); applied.append("K5")
    elif idx == 13:                               # E
        prims, n = _replace_block(prims,
            {"Read those four questions again and notice what they are: Density and Optionality, asked from the",
             "institution's side of the table. The diagnostic you just scored is the same conversation, run on yourself first."},
            "These are questions institutional rooms often weigh. Density and Optionality help you read the formation and portability questions underneath them. The diagnostic you just scored runs that reading on yourself first.",
            492)
        if n: applied.append("E")
    elif idx == 14:                               # F + G
        prims, n = _replace_block(prims,
            {"Restructurings are decided quietly and announced suddenly, but they telegraph. None of these signals",
             "means a decision has been made about you. Each one means the category of decision is being prepared,",
             "and your state determines your exposure to it."},
            "None of these signals means a decision has been made about you, and none of them predicts one. They identify questions that should be answered before you treat a position as secure.",
            492)
        if n: applied.append("F")
        prims = [_swap12(p, "Early Signals", "Position Exposure Signals") for p in prims]
        prims = [_swap12(p, "Protective reading: test your state against what the institution is telegraphing",
                         "Questions to investigate, not predictions") for p in prims]
        applied.append("G")
        prims, nm = _replace_block(prims,                 # M (v1.2.1)
            {"What to do with a signal: nothing dramatic. Rescore. A Compounding position reads these signals as noise.",
             "A Fragile or Stagnant one reads them as a clock. Either way, the diagnostic tells you which, and the move",
             "stays yours to decide."},
            "What to do with a signal: nothing dramatic. Rescore. What weight a signal deserves depends on what your own two scores say, and that is what the rescore is for. The move stays yours to decide.",
            492)
        if nm: applied.append("M")
    elif idx == 16:                               # H
        prims, n = _replace_block(prims,
            {"The exposure: if the rollout consolidates my function, my Optionality score (14) decides how soft the landing is."},
            "The exposure: if the rollout consolidates my function, my Optionality score (14) helps shape how soft the landing is.",
            466)
        if n: applied.append("H")
        # Q (v1.2.3): a guidance line before the "The exposure:" prompt. The prompt unit and the
        # gold summary box below it shift down by S into the page's bottom whitespace; every
        # internal gap is preserved, nothing crosses onto page 18.
        S = 26.0
        def _shift(p, dy):
            if p[0] == "text":
                m = list(p[1]); m[5] -= dy
                return ("text", tuple(m), p[2], p[3], p[4], p[5])
            newsp = []
            for sp in p[2]:
                nseg = []
                for seg in sp:
                    if seg[0] in ("m", "l"):
                        nseg.append((seg[0], (seg[1][0], seg[1][1] - dy)))
                    elif seg[0] == "c":
                        nseg.append(("c",) + tuple((pt[0], pt[1] - dy) for pt in seg[1:]))
                    else:
                        nseg.append(seg)
                newsp.append(nseg)
            return ("path", p[1], newsp, p[3], p[4], p[5])
        def _ytop_top(p):                              # top-most yTop of a primitive
            if p[0] == "text":
                return 792.0 - p[1][5]
            ys = []
            for sp in p[2]:
                for seg in sp:
                    if seg[0] in ("m", "l"):
                        ys.append(seg[1][1])
                    elif seg[0] == "c":
                        ys += [pt[1] for pt in seg[1:]]
            return (792.0 - max(ys)) if ys else 1e9
        LO, HI = 448.0, 566.0                          # exposure prompt (454/466) + gold summary box (532-562)
        prims = [(_shift(p, S) if LO <= _ytop_top(p) <= HI else p) for p in prims]
        qtext = ["If you have a recent offer, a market search, or a comp benchmark to draw on, use it. If you don't, estimate in",
                 "months instead of dollars. That's still a real number."]
        for k, line in enumerate(qtext):               # sits where the exposure prompt used to start (yTop 454, 466)
            prims = prims + [_tp(54.0, 792.0 - (454.0 + 12.0 * k), "Helvetica", 9.5, NAVY12, line)]
        applied.append("Q")
    elif idx == 18:                               # I
        prims, n = _replace_block(prims,
            {"The honest note: this read cannot correct its own author. It is built from your scores, filtered through your blind",
             "spots, by the one person structurally unable to see them. That is not a flaw in you; it is a property of every",
             "self-assessment ever written. A calibrated read exists for exactly this reason. That is what the live Capability",
             "Position Read does: you score, you are corrected against evidence, and you score again."},
            "The honest note: this read cannot correct its own author. Self-assessment has a structural limitation: the same person is supplying both the evidence and the judgment. That does not make it useless. It means the reading needs a disciplined correction process. A calibrated read exists for exactly this reason. That is what the live Capability Position Read does: you score, you are corrected against evidence, and you score again.",
            492)
        if n: applied.append("I")
    # (v1.2.4) The page-23 pointer that EDIT N/O produced is retired: its message
    # ("runs live ... at temidayoafonja.com") is now carried by the rewritten
    # EDIT 5 prose, so no separate holding line is emitted.
    return prims, applied

# ---------------------------------------------------------------- render
def set_fill(c, col):
    if isinstance(col, tuple) and col and col[0] == "cmyk":
        c.setFillColorCMYK(*col[1])
    else:
        c.setFillColorRGB(*col)
def set_stroke(c, col):
    if isinstance(col, tuple) and col and col[0] == "cmyk":
        c.setStrokeColorCMYK(*col[1])
    else:
        c.setStrokeColorRGB(*col)

def build_path(c, subpaths):
    path = c.beginPath()
    for sp in subpaths:
        started = False
        for seg in sp:
            if seg[0] == "m":
                path.moveTo(*seg[1]); started = True
            elif seg[0] == "l":
                path.lineTo(*seg[1])
            elif seg[0] == "c":
                (x1, y1), (x2, y2), (x3, y3) = seg[1], seg[2], seg[3]
                path.curveTo(x1, y1, x2, y2, x3, y3)
            elif seg[0] == "h":
                path.close()
    return path

# ---------------------------------------------------------------- form fields
# Interactive AcroForm text fields live outside the page content streams, so a
# content-only replay would drop them. Lift their exact specs (native /Rect in
# bottom-left PDF coords, border/fill/text colour, font, flags) from the
# original and recreate them so the worksheet pages stay fillable.
_src = fitz.open(SRC)
def widgets_for(pageidx):
    specs = []
    for w in _src[pageidx].widgets():
        obj = _src.xref_object(w.xref)
        rm = re.search(r'/Rect\s*\[([^\]]*)\]', obj)
        x0, y0, x1, y1 = [float(v) for v in rm.group(1).split()]
        specs.append({
            "name": w.field_name, "value": w.field_value or "",
            "x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0,
            "border": w.border_color or [0, 0, 0],
            "bw": w.border_width or 1.0,
            "fill": w.fill_color, "text": w.text_color or [0, 0, 0],
            "fs": w.text_fontsize or 9.0, "flags": w.field_flags or 0,
        })
    for s in specs:
        if s["name"] == "recalibrated":          # EDIT L: field follows the body copy (keep w,h)
            s["y"] = 549.0                        # yTop 243..185; height 58 unchanged
    if pageidx == 16:                            # Q (v1.2.3): exposure + total boxes move down with the reflow
        for s in specs:
            if s["name"] in ("cost_exposure", "cost_total"):
                s["y"] -= 26.0                    # bottom-origin y down by S (= 26pt lower on the page)
    return specs

def draw_widgets(c, specs):
    af = c.acroForm
    for s in specs:
        af.textfield(
            name=s["name"], value=s["value"],
            x=s["x"], y=s["y"], width=s["w"], height=s["h"],
            borderStyle="solid", borderWidth=s["bw"],
            borderColor=Color(*s["border"]),
            fillColor=(Color(*s["fill"]) if s["fill"] else None),
            textColor=Color(*s["text"]),
            fontName="Helvetica", fontSize=s["fs"],
            fieldFlags=s["flags"], forceBorder=True,
        )

def render_prims(c, prims):
    for p in prims:
        if p[0] == "text":
            _, m, font, size, fill, text = p
            if not text:
                continue
            c.saveState()
            c.transform(*m)
            set_fill(c, fill)
            try:
                c.setFont(font or "Helvetica", size or 10)
            except Exception:
                c.setFont("Helvetica", size or 10)
            c.drawString(0, 0, text)
            c.restoreState()
        elif p[0] == "path":
            _, mode, subpaths, stroke, fill, lw = p
            c.saveState()
            c.setLineWidth(lw)
            if mode == "fill":
                set_fill(c, fill)
                c.drawPath(build_path(c, subpaths), stroke=0, fill=1)
            else:
                set_stroke(c, stroke)
                c.drawPath(build_path(c, subpaths), stroke=1, fill=0)
            c.restoreState()

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))
c.setTitle("The Capability Formation Field Kit")
c.setAuthor("Temidayo Afonja")                                   # EDIT J
c.setCreator("The Density Group")
c.setSubject("A self-diagnostic for reading your capability position")
c.setKeywords("capability formation, density, optionality, instrument v1.1")
total_changed = 0
v11_applied = []
v12_applied = []
for idx, pageobj in enumerate(order):
    body = raw_objs[pageobj]
    cont = int(re.search(rb'/Contents\s+(\d+)\s+0\s+R', body).group(1))
    fonts = fontmap(pageobj)
    prims = interpret(stream_of(cont), fonts)
    prims, ch = apply_boundary_edit(prims); total_changed += ch
    prims, applied = apply_v11_edits(idx, prims); v11_applied.extend(applied)
    prims, applied12 = apply_v12_edits(idx, prims); v12_applied.extend(applied12)
    render_prims(c, prims)
    draw_widgets(c, widgets_for(idx))            # rescore field stays on page 12 (K4)
    c.showPage()

# EDIT K / K6 — new appendix page 24 (no form fields)
assert CAPTURED_P12[0] is not None, "page 12 was not captured"
render_prims(c, _build_page24(CAPTURED_P12[0]))
c.showPage()
c.save()

# EDIT J — language + viewer preference (screen readers announce the title)
_md = fitz.open(OUT)
_cat = _md.pdf_catalog()
_md.xref_set_key(_cat, "Lang", "(en-GB)")
_md.xref_set_key(_cat, "ViewerPreferences", "<</DisplayDocTitle true>>")
_md.save(OUT + ".tmp", garbage=0, deflate=True)
_md.close()
import os as _os
_os.replace(OUT + ".tmp", OUT)

print(f"Wrote {OUT}; boundary text lines changed: {total_changed} (expected 2)")
if UNMAPPED:
    print("WARNING: unmapped font tags (defaulted to Helvetica):", sorted(UNMAPPED))
assert total_changed == 2, "boundary substitution did not hit exactly 2 lines"
print("v1.1 edits applied:", v11_applied)
print("v1.2 edits applied:", sorted(set(v12_applied)))
EXPECT12 = {"A", "C", "D", "E", "F", "G", "H", "I", "K3", "K5", "M", "P", "Q"}
assert set(v12_applied) == EXPECT12, f"v1.2 mismatch: {sorted(set(v12_applied))} vs {sorted(EXPECT12)}"
