"""Minimal PNG reader (8-bit RGB/RGBA, no interlace) plus contrast helpers.
Used to QA the banner renders without a Pillow dependency."""
import zlib, struct

def read(path):
    d = open(path, 'rb').read()
    assert d[:8] == b'\x89PNG\r\n\x1a\n', 'not a png'
    pos, idat, pal = 8, b'', None
    w = h = depth = ctype = None
    while pos < len(d):
        ln, typ = struct.unpack('>I', d[pos:pos+4])[0], d[pos+4:pos+8]
        body = d[pos+8:pos+8+ln]
        if typ == b'IHDR':
            w, h, depth, ctype, _, _, il = struct.unpack('>IIBBBBB', body)
            assert depth == 8 and il == 0, 'need 8-bit non-interlaced'
        elif typ == b'PLTE': pal = body
        elif typ == b'IDAT': idat += body
        elif typ == b'IEND': break
        pos += 12 + ln
    nch = {0:1, 2:3, 3:1, 4:2, 6:4}[ctype]
    raw = zlib.decompress(idat)
    stride = w * nch
    out, prev = bytearray(), bytearray(stride)
    p = 0
    for _ in range(h):
        f = raw[p]; p += 1
        line = bytearray(raw[p:p+stride]); p += stride
        if f == 1:
            for i in range(nch, stride): line[i] = (line[i] + line[i-nch]) & 255
        elif f == 2:
            for i in range(stride): line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                a = line[i-nch] if i >= nch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = line[i-nch] if i >= nch else 0
                b = prev[i]; c = prev[i-nch] if i >= nch else 0
                pa, pb, pc = abs(b-c), abs(a-c), abs(a+b-2*c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 255
        out += line; prev = line
    return w, h, nch, bytes(out), pal

def px(img, x, y):
    w, h, nch, data, pal = img
    i = (y * w + x) * nch
    if pal is not None:
        j = data[i] * 3; return pal[j], pal[j+1], pal[j+2]
    return data[i], data[i+1], data[i+2]

def _lin(c):
    c /= 255.0
    return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055) ** 2.4

def lum(rgb):
    r, g, b = rgb
    return 0.2126*_lin(r) + 0.7152*_lin(g) + 0.0722*_lin(b)

def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)
