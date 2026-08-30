"""Video 6 thumbnail upload exports and integrity verification.

Produces the 1280 x 720 JPG upload files and prints the evidence recorded in
VIDEO_6_THUMBNAIL_QA_README.md. Nothing here is asserted from intent; each
line is measured from the files on disk.
"""
import os, hashlib
import numpy as np
from PIL import Image, ImageDraw
import build_thumbnails as T

HERE = os.path.dirname(os.path.abspath(__file__))
def P(n): return os.path.join(HERE, n)
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ------------------------------------------------------------------- exports
for k in ("A", "B"):
    im = Image.open(P("Video_6_Thumbnail_%s.png" % k))
    assert im.size == (1280, 720)
    im.save(P("Video_6_Thumbnail_%s_UPLOAD_1280x720.jpg" % k),
            quality=95, subsampling=0, optimize=True)

print("=" * 70)
print("1. DIMENSIONS AND FILE SIZES")
for n in sorted(os.listdir(HERE)):
    if n.startswith("Video_6_Thumbnail_") and n.split(".")[-1] in ("png", "jpg"):
        im = Image.open(P(n))
        w, h = im.size
        ar = "%.6f" % (w / h)
        kb = os.path.getsize(P(n)) / 1024
        tag = "  16:9 EXACT" if (w, h) in ((1280, 720), (2560, 1440)) else ""
        print(f"   {n:46s} {w:5d} x {h:<5d} ar {ar} {kb:8.0f} KB{tag}")

print()
print("2. PHOTOGRAPH INTEGRITY")
src = Image.open(T.SRC).convert("RGB")
print(f"   source          : {os.path.basename(T.SRC)}")
print(f"   source size     : {src.size[0]} x {src.size[1]}  ({src.mode})")
print(f"   source sha256   : {sha(T.SRC)}")
expect = T.photo_panel(T.W - T.PANEL_X, T.H, 310)
pw, ph = expect.size
crop_w = int(round(src.height * pw / ph))
print(f"   crop taken      : {crop_w} x {src.height} at x=310  (native pixels)")
print(f"   panel rendered  : {pw} x {ph}   scale {pw / crop_w:.4f}  "
      f"({'downscale only' if pw <= crop_w else 'UPSCALE'})")
e = np.asarray(expect).astype(int)
for k in ("A", "B"):
    m = Image.open(P("Video_6_Thumbnail_%s_2560x1440.png" % k))
    got = np.asarray(m.crop((T.PANEL_X, 0, T.W, T.H))).astype(int)
    d = np.abs(e - got)
    print(f"   master {k} photo panel vs pure crop+Lanczos: max diff {d.max()}, "
          f"differing pixels {(d.sum(2) > 0).sum()}"
          f"   -> {'IDENTICAL' if d.max() == 0 else 'ALTERED'}")

print()
print("3. PALETTE — colours present in the navy panel (text area only)")
for k in ("A", "B"):
    m = np.asarray(Image.open(P("Video_6_Thumbnail_%s_2560x1440.png" % k))
                   .crop((0, 0, T.PANEL_X, T.H))).astype(int)
    flat = m.reshape(-1, 3)
    for name, c in (("NAVY  #0F2346", T.NAVY), ("CREAM #F5F1E8", T.CREAM),
                    ("GOLD  #C9A84C", T.GOLD)):
        n = int((flat == np.array(c)).all(1).sum())
        print(f"   {k}  {name}  exact-match pixels: {n:>9,}")
    other = int((~np.isin(flat, [T.NAVY, T.CREAM, T.GOLD]).all(1)).sum())
    print(f"   {k}  anti-aliased edge pixels between those three: "
          f"{other:,} ({100*other/len(flat):.2f}% of the panel)")

print()
print("4. TYPE GEOMETRY AND MOBILE LEGIBILITY")
d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
s1 = T.fit("MORE WORK", T.MAXW)
_, h1, _, _ = T.cap(d, "MORE WORK", T.f(s1))
rows = [("MORE WORK (both)", h1)]
s2 = s1 + 40
while True:
    gw, gh, _, _ = T.cap(d, "GROWTH", T.f(s2))
    ne = int(round(gh * 0.86))
    if T.MARGIN + int(round(ne*1.02)) + int(ne*0.42) + gw <= T.PANEL_X - T.GUTTER:
        break
    s2 -= 2
gwA, ghA, _, _ = T.cap(d, "GROWTH", T.f(s2))
rows += [("GROWTH (A)", ghA), ("not-equal mark (A)", int(round(ghA * 0.86)))]
s3 = T.fit("GROWTH", T.MAXW - 92)
gwB, ghB, _, _ = T.cap(d, "GROWTH", T.f(s3))
rows += [("GROWTH (B)", ghB), ("not-equal mark (B)", int(round(h1 * 1.02)))]
print(f"   {'element':22s} {'@2560':>7s} {'@1280':>7s} {'@200px':>8s} {'@160px':>8s}")
for name, hh in rows:
    print(f"   {name:22s} {hh:7d} {hh/2:7.1f} {hh/12.8:8.2f} {hh/16:8.2f}")
print("   (cap height in pixels; 160 px is the narrowest phone-feed width)")

print()
print("5. CLEARANCE FROM THE PHOTO SEAM (panel edge at x=1470 of 2560)")
for k, right in (("A", T.MARGIN + int(round(int(round(ghA*0.86))*1.02))
                       + int(int(round(ghA*0.86))*0.42) + gwA),
                 ("B", T.MARGIN + gwB + 46)):
    print(f"   {k}: widest element ends at x={right}, "
          f"clear space to seam = {T.PANEL_X - right} px @2560 "
          f"({(T.PANEL_X - right)/2:.0f} px @1280)")

print()
print("6. SHA-256 OF DELIVERED IMAGE FILES")
for n in sorted(os.listdir(HERE)):
    if n.startswith("Video_6_Thumbnail_") and n.split(".")[-1] in ("png", "jpg"):
        print(f"   {sha(P(n))}  {n}")
print("=" * 70)
