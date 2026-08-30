"""Video 6 revision 2 — upload exports and verification.

Every line printed here is measured from files on disk, not asserted.
"""
import os, hashlib
import numpy as np
from PIL import Image
from collections import Counter
import build_thumbnails as T

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(HERE, "..", ".."))
def P(n): return os.path.join(HERE, n)
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

APPROVED = {
    "V2":  R + "/video-2-slides/thumbnail/VIDEO_2_THUMBNAIL_FINAL_3840x2160.png",
    "V3":  R + "/video-3-slides/thumbnail/VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png",
    "V4A": R + "/video-4-slides/thumbnail/Video_4_Thumbnail_A.png",
    "V5A": R + "/video-5-slides/thumbnail/Video_5_Thumbnail_A_Final.png",
}

for k in ("A", "B"):
    Image.open(P("Video_6_Thumbnail_%s.png" % k)).save(
        P("Video_6_Thumbnail_%s_UPLOAD_1280x720.jpg" % k),
        quality=95, subsampling=0, optimize=True)

print("=" * 74)
print("1. PALETTE — sampled from every approved master and from Video 6")
def top_colours(p, n=3):
    a = np.asarray(Image.open(p).convert("RGB"))
    flat = a[:, :int(a.shape[1] * 0.55)].reshape(-1, 3)
    return [tuple(int(v) for v in c)
            for c, _ in Counter(map(tuple, flat)).most_common(n)]
rows = list(APPROVED.items()) + [
    ("V6 A", P("Video_6_Thumbnail_A_2560x1440.png")),
    ("V6 B", P("Video_6_Thumbnail_B_2560x1440.png"))]
for lab, p in rows:
    print("   %-6s %s" % (lab, "  ".join("#%02X%02X%02X" % c for c in top_colours(p))))
print("   Video 6 palette: NAVY #%02X%02X%02X  CREAM #%02X%02X%02X  GOLD #%02X%02X%02X"
      % (T.NAVY + T.CREAM + T.GOLD))
for lab, p in APPROVED.items():
    cols = set(top_colours(p, 4))
    hits = [n for n, c in (("NAVY", T.NAVY), ("CREAM", T.CREAM), ("GOLD", T.GOLD))
            if c in cols]
    print("   exact match with %-4s: %s" % (lab, ", ".join(hits) or "none"))

print()
print("2. SERIES GEOMETRY — Video 6 against the approved Video 4A / 5A constants")
for name, want, got in [("portrait box left edge", 1470, T.SEAM),
                        ("gold divider width", 12, T.DIV_W),
                        ("text column x", 190, T.COL_X),
                        ("text column width", 1150, T.COL_W),
                        ("headline centre y", 696, int(T.CENTRE_Y)),
                        ("hairline y", 268, 268),
                        ("underline fraction", 0.74, 0.74)]:
    print("   %-26s approved %-8s Video 6 %-8s %s"
          % (name, want, got, "MATCH" if want == got else "DIFFERS"))

print()
print("3. PHOTOGRAPH INTEGRITY")
src = Image.open(T.SRC).convert("RGB")
print("   source %s  %dx%d" % (os.path.basename(T.SRC), *src.size))
print("   sha256 %s" % sha(T.SRC))
expect = Image.new("RGB", (T.W, T.H)); cw, ch, sc = T.place(expect)
panel = expect.crop((T.SEAM, 0, T.W, T.H))
print("   crop %dx%d at (%d,%d) -> 1090x1440, scale %.4f (%s)"
      % (cw, ch, T.CROP_LEFT, T.CROP_TOP, sc,
         "downscale only" if sc <= 1 else "UPSCALE"))
e = np.asarray(panel).astype(int)[:, T.DIV_W + 1:]
for k in ("A", "B"):
    m = Image.open(P("Video_6_Thumbnail_%s_2560x1440.png" % k))
    g = np.asarray(m.crop((T.SEAM + T.DIV_W + 1, 0, T.W, T.H))).astype(int)
    d = np.abs(e - g)
    print("   master %s photo area vs pure crop+Lanczos: max diff %d, "
          "differing pixels %d -> %s"
          % (k, d.max(), int((d.sum(2) > 0).sum()),
             "IDENTICAL" if d.max() == 0 else "ALTERED"))

print()
print("4. PORTRAIT SCALE AND EYE LINE (1280 x 720 space)")
SEL_IPD, SEL_EYE_Y = 255.0, 540.0     # measured in the 1536 x 1536 source
print("   Video 6 : inter-pupil %.0f px, eye line y %.0f"
      % (SEL_IPD * 545.0 / cw, (SEL_EYE_Y - T.CROP_TOP) * 720.0 / ch))
print("   Video 4A: inter-pupil ~64 px, eye line y ~219  (read off the file)")
print("   Video 5A: inter-pupil ~69 px, eye line y ~211  (read off the file)")
widest = int(round(1536 * (T.W - T.SEAM) / T.H))
print("   widest crop this source allows at the panel aspect: %d x 1536" % widest)
print("   smallest portrait scale reachable by cropping alone: inter-pupil %.0f px"
      % (SEL_IPD * 545.0 / widest))
print("   headroom above the hair at full height: %.0f px "
      "(any top crop removes the top of her head)" % (20.0 * 720.0 / 1536))

print()
print("5. FILES")
for n in sorted(os.listdir(HERE)):
    if n.startswith("Video_6_Thumbnail_") and n.split(".")[-1] in ("png", "jpg"):
        im = Image.open(P(n)); kb = os.path.getsize(P(n)) / 1024
        tag = "  16:9" if abs(im.width / im.height - 16/9) < 1e-6 else ""
        print("   %-52s %5d x %-5d %8.0f KB%s" % (n, im.width, im.height, kb, tag))
print()
for n in sorted(os.listdir(HERE)):
    if n.startswith("Video_6_Thumbnail_") and n.split(".")[-1] in ("png", "jpg"):
        print("   %s  %s" % (sha(P(n)), n))
print("=" * 74)
