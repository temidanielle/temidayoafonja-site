"""Scale the keyed portrait to its exact placement size for the master artwork.

Resampling happens here rather than in the renderer so the composite uses a
premultiplied Lanczos resize (no white bleed out of the transparent ground) plus
a light post-scale sharpen to recover the detail the upscale costs. No other
change is made to the portrait.

    python3 build/scale-portrait.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

HERE = Path(__file__).resolve().parent.parent
SRC = HERE / 'assets' / 'temidayo-portrait-cutout.png'
OUT = HERE / 'assets' / 'temidayo-portrait-1600.png'
TARGET = (1600, 1419)          # matches the <image> box in what-still-travels.svg

im = Image.open(SRC).convert('RGBA')
a = np.asarray(im).astype(np.float64) / 255.0
alpha = a[..., 3:4]

# premultiply so fully transparent pixels cannot bleed their colour inward
pm = np.dstack([a[..., :3] * alpha, alpha])
pm_img = Image.fromarray((pm * 255).round().astype(np.uint8), 'RGBA')
pm_img = pm_img.resize(TARGET, Image.LANCZOS)

b = np.asarray(pm_img).astype(np.float64) / 255.0
al = b[..., 3:4]
rgb = np.divide(b[..., :3], np.maximum(al, 1e-6))       # un-premultiply
rgb = np.clip(rgb, 0, 1)
out = Image.fromarray(
    np.dstack([rgb * 255, al * 255]).round().astype(np.uint8), 'RGBA')

# light unsharp on colour only; alpha is left as resampled
rgb_img, a_img = out.convert('RGB'), out.getchannel('A')
rgb_img = rgb_img.filter(ImageFilter.UnsharpMask(radius=2.0, percent=45, threshold=3))
rgb_img.putalpha(a_img)
rgb_img.save(OUT)
print(f'wrote {OUT.relative_to(HERE)} {rgb_img.size}')
