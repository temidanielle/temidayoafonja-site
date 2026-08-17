"""Build every deliverable for the "What still travels?" thumbnail.

    cd youtube/what-still-travels && python3 build/build.py

Requires: python3 + pillow + numpy + scipy, and a Chromium-capable playwright
reachable on NODE_PATH (see RENDER below). Every output in ./exports is
regenerated from ./what-still-travels.svg and ./assets/source, so the SVG stays
the single editable source of truth.
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent.parent      # youtube/what-still-travels
ROOT = HERE.parent.parent                          # repository root
REL = HERE.relative_to(ROOT).as_posix()
EXPORTS = HERE / 'exports'
MASTER = EXPORTS / 'what-still-travels-3840x2160.png'

NODE_PATH = '/opt/node22/lib/node_modules'


def run(cmd, **kw):
    print('$', ' '.join(str(c) for c in cmd))
    subprocess.run(cmd, check=True, cwd=HERE, **kw)


def render(src, out, w, h, dsf=1):
    run(['node', 'build/render.mjs', f'{REL}/{src}', f'{REL}/{out}', str(w), str(h), str(dsf)],
        env={'NODE_PATH': NODE_PATH, 'PATH': '/opt/node22/bin:/usr/bin:/bin',
             'PLAYWRIGHT_BROWSERS_PATH': '/opt/pw-browsers'})


# ── 1. portrait ─────────────────────────────────────────────────────────────
run([sys.executable, 'build/prep-portrait.py'])
run([sys.executable, 'build/scale-portrait.py'])

# ── 2. master artwork ───────────────────────────────────────────────────────
render('what-still-travels.svg', 'exports/what-still-travels-3840x2160.png', 3840, 2160)

# ── 3. previews, Lanczos down from the master ───────────────────────────────
master = Image.open(MASTER).convert('RGB')
for width in (360, 200):
    height = round(width * 9 / 16)
    p = EXPORTS / f'preview-{width}.png'
    master.resize((width, height), Image.LANCZOS).save(p)
    print(f'wrote {p.relative_to(HERE)} {width}x{height}')

# ── 3b. upload file ─────────────────────────────────────────────────────────
# YouTube caps custom thumbnails at 2 MB, which the 3840px PNG master exceeds.
# 1920x1080 at q92 with 4:4:4 chroma keeps the serif edges clean well inside it.
upload = EXPORTS / 'what-still-travels-1920x1080-upload.jpg'
master.resize((1920, 1080), Image.LANCZOS).save(
    upload, 'JPEG', quality=92, subsampling=0, optimize=True, progressive=False)
print(f'wrote {upload.relative_to(HERE)} '
      f'({upload.stat().st_size / 1024:.0f} KB, limit 2048 KB)')

# ── 4. placement simulations ────────────────────────────────────────────────
# Rendered at deviceScaleFactor 2, so the thumbnail is downsampled to the same
# device pixels a current phone or laptop screen would give it.
render('build/sim-mobile.html', 'exports/sim-mobile-home-feed.png', 412, 915, 2)
render('build/sim-desktop.html', 'exports/sim-desktop-home-feed.png', 1280, 720, 2)
render('build/sim-right-column.html', 'exports/sim-right-column.png', 402, 640, 2)

print('\nall deliverables written to', EXPORTS.relative_to(ROOT))
