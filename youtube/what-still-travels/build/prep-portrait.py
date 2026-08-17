"""Prepare the approved studio portrait for the thumbnail composite.

    python3 build/prep-portrait.py

  in:  assets/source/temidayo-studio-portrait-1268x1240.png
  out: assets/temidayo-portrait-cutout.png   (keyed, corrected, trimmed)

Operations are limited to what the brief allows: keying the studio's white
circular ground, edge decontamination, a clean crop, exposure correction and
colour balance. Face, age, skin texture, expression and proportions are
untouched — nothing here reshapes, smooths or repaints the subject.
"""
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

HERE = Path(__file__).resolve().parent.parent
SRC = HERE / 'assets' / 'source' / 'temidayo-studio-portrait-1268x1240.png'
OUT = HERE / 'assets' / 'temidayo-portrait-cutout.png'

im = Image.open(SRC).convert('RGB')
a = np.asarray(im).astype(np.float64)
h, w, _ = a.shape
lum = a.mean(2)
mx = a.max(2); mn = a.min(2)

# ---- 1. locate the white circular field -------------------------------------
white_px = (lum > 235) & ((mx - mn) < 12)
ys, xs = np.where(white_px)
cx = (xs.min() + xs.max()) / 2.0
r = (xs.max() - xs.min()) / 2.0
cy = ys.min() + r
yy, xx = np.mgrid[0:h, 0:w]
dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
inside = dist <= (r - 3)
print(f'disc centre=({cx:.1f},{cy:.1f}) r={r:.1f}')

# ---- 2. key the background ---------------------------------------------------
# Everything around the subject is achromatic: the white field, the soft drop
# shadow at the disc edge and the black surround. She is warm/chromatic
# throughout, so a border-seeded flood fill over achromatic pixels keys cleanly
# without touching her.
achromatic = (mx - mn) < 24
seed = np.zeros_like(achromatic)
seed[0, :] = seed[-1, :] = True
seed[:, 0] = seed[:, -1] = True
seed &= achromatic
bg = ndimage.binary_propagation(seed, mask=achromatic)
bg = ndimage.binary_closing(bg, structure=np.ones((3, 3)), border_value=1)
print(f'keyed background: {bg.mean():.3f} of frame')

subject = ndimage.binary_fill_holes(~bg)   # eyes, teeth, neutral catchlights
lab, n = ndimage.label(subject)
if n > 1:                                   # drop specks
    sizes = ndimage.sum(subject, lab, range(1, n + 1))
    subject = lab == (int(np.argmax(sizes)) + 1)
print(f'subject coverage of disc: {(subject & inside).sum() / inside.sum():.3f}')

# ---- 3. soft alpha with a slight contraction ---------------------------------
# Pixels on the silhouette are a blend of subject and white ground; contracting
# by 2px before feathering removes them rather than carrying a bright rim onto
# the navy ground.
core = ndimage.binary_erosion(subject, iterations=2)
alpha = ndimage.gaussian_filter(core.astype(np.float64), 1.0)
alpha = np.clip((alpha - 0.40) / 0.34, 0, 1)

# ---- 4. decontaminate the remaining edge pixels ------------------------------
# A partially transparent pixel is a mix of subject and white ground:
#   C = a*F + (1-a)*255   ->   F = (C - (1-a)*255) / a
edge = (alpha > 0.02) & (alpha < 0.995)
fg = a.copy()
af = alpha[..., None]
with np.errstate(invalid='ignore', divide='ignore'):
    unmixed = (a - (1 - af) * 255.0) / np.maximum(af, 1e-6)
fg[edge] = np.clip(unmixed[edge], 0, 255)

# ---- 5. crop -----------------------------------------------------------------
# Bottom limit: the last row where the silhouette is still clear of the source's
# circular mask, so the composite never shows that clipped arc. She bleeds off
# the foot of the canvas instead.
rim_band = inside & ~ndimage.binary_erosion(inside, iterations=10)
touch = [y for y in range(h) if (subject[y] & rim_band[y]).any() and y > cy]
crop_bottom = (min(touch) if touch else int(cy + r)) - 6
sy, sx = np.where(alpha > 0.5)
crop_top, crop_left = max(sy.min() - 24, 0), max(sx.min() - 24, 0)
crop_right = min(sx.max() + 25, w)
print(f'crop x[{crop_left}:{crop_right}] y[{crop_top}:{crop_bottom}]')
fg = fg[crop_top:crop_bottom, crop_left:crop_right]
alpha = alpha[crop_top:crop_bottom, crop_left:crop_right]

# ---- 6. exposure and colour balance -----------------------------------------
x = fg / 255.0
ground = a[bg][:, :3].mean(0)               # measured cast of the studio white
x = np.clip(x * (ground.mean() / ground), 0, 1)          # neutral grey balance
x = np.clip((x - 0.5) * 1.06 + 0.5 + 0.02, 0, 1)         # +2% exposure, 1.06 contrast

# Deep-shadow lift. Half of her silhouette (dark hair, the shadow-side shoulder)
# sits within ~18 luma of the navy ground; a small lift in the darkest values
# only separates her from it without touching midtones or skin texture, and
# without any halo, glow or gradient behind her.
shadow = np.clip(1.0 - x.mean(2, keepdims=True) / 0.235, 0, 1) ** 1.5
x = np.clip(x + 0.038 * shadow, 0, 1)

rgba = np.dstack([x * 255.0, alpha * 255.0]).astype(np.uint8)
out = Image.fromarray(rgba, 'RGBA')

# trim to the silhouette so the placement box in the SVG is exactly her extent
ys, xs = np.where(np.asarray(out)[..., 3] > 0)
out = out.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1))
out.save(OUT)
print(f'wrote {OUT.relative_to(HERE)} {out.size}')
