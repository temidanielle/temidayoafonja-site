#!/usr/bin/env python3
"""Shared Keep the Proof V2 icon set: one simple line style, navy with gold
accents. Authored once as SVG for the HTML outputs (handbook, Start Here) and
rasterized to PNG (via Chromium) for the .docx and the reportlab Tools PDF, so
the same icons appear across all four files. Icons always sit beside a text
label and never carry meaning on their own; accessible outputs get alt text."""
import os, subprocess, glob

NAVY = "#112345"
GOLD = "#C9A84C"

# Each value is the inner markup of a 24x24 viewBox. Navy strokes inherit the
# svg stroke; gold accents set their own stroke/fill.
_ICONS = {
    # --- the three steps ---
    "capture": '<circle cx="12" cy="12" r="8.5"/><path d="M12.6 6.5 L8.5 12.8 h3.1 L11 17.5 l4.4 -6.2 h-3.1 z" fill="%s" stroke="none"/>' % GOLD,
    "clarify": '<circle cx="11" cy="11" r="6"/><line x1="15.4" y1="15.4" x2="20" y2="20"/><circle cx="11" cy="11" r="2.1" fill="%s" stroke="none"/>' % GOLD,
    "carry": '<line x1="3.5" y1="12" x2="16" y2="12"/><path d="M13.5 7.5 L18.5 12 L13.5 16.5" stroke="%s"/>' % GOLD,
    # --- keep / care / never ---
    "keep": '<path d="M12 3 l7 3 v5 c0 5 -3 8 -7 10 c-4 -2 -7 -5 -7 -10 v-5 z"/><path d="M8.8 12 l2.4 2.4 L15.6 9.2" stroke="%s"/>' % GOLD,
    "care": '<path d="M12 3 l7 3 v5 c0 5 -3 8 -7 10 c-4 -2 -7 -5 -7 -10 v-5 z"/><line x1="12" y1="8" x2="12" y2="12.5" stroke="%s"/><circle cx="12" cy="15.5" r="0.7" fill="%s" stroke="none"/>' % (GOLD, GOLD),
    "never": '<circle cx="12" cy="12" r="8.5"/><line x1="6.4" y1="6.4" x2="17.6" y2="17.6" stroke="%s"/>' % GOLD,
    # --- pause ---
    "pause": '<rect x="8" y="7" width="2.4" height="10" rx="1"/><rect x="13.6" y="7" width="2.4" height="10" rx="1" fill="%s" stroke="none"/>' % GOLD,
    # --- proof line ---
    "proofline": '<line x1="5" y1="9.5" x2="15" y2="9.5"/><line x1="5" y1="14.5" x2="19" y2="14.5"/><circle cx="18" cy="9.5" r="1.7" fill="%s" stroke="none"/>' % GOLD,
    # --- reconstruct / already lost access ---
    "reconstruct": '<path d="M19 12 a7 7 0 1 1 -2.05 -4.95"/><path d="M17 3.2 V7.2 H13" stroke="%s"/>' % GOLD,
    # --- match your proof to a role ---
    "match": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1.4" fill="%s" stroke="none"/>' % GOLD,
    # --- put your record to work (four) ---
    "resume": '<path d="M7 3 h6.5 L18 7.5 V21 H7 z"/><path d="M13.3 3 V7.5 H18"/><line x1="9.2" y1="12" x2="15" y2="12" stroke="%s"/><line x1="9.2" y1="15" x2="15" y2="15" stroke="%s"/>' % (GOLD, GOLD),
    "about": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="10" r="2.6"/><path d="M6.8 17.5 a5.4 4.2 0 0 1 10.4 0" stroke="%s"/>' % GOLD,
    "interview": '<path d="M5 6 h14 a1 1 0 0 1 1 1 v7 a1 1 0 0 1 -1 1 h-7.5 L7.5 18.5 V15 H5 a1 1 0 0 1 -1 -1 V7 a1 1 0 0 1 1 -1 z"/><circle cx="9.5" cy="10.5" r="0.8" fill="%s" stroke="none"/><circle cx="12" cy="10.5" r="0.8" fill="%s" stroke="none"/><circle cx="14.5" cy="10.5" r="0.8" fill="%s" stroke="none"/>' % (GOLD, GOLD, GOLD),
    "promotion": '<polyline points="4,18.5 9,13.5 13,15.5 20,7"/><path d="M15.5 7 H20 V11.5" stroke="%s"/>' % GOLD,
    # --- words to stand on (open book) ---
    "words": '<path d="M12 6.5 C10 5 6.5 5 4.5 6.5 V18 C6.5 16.5 10 16.5 12 18 C14 16.5 17.5 16.5 19.5 18 V6.5 C17.5 5 14 5 12 6.5 Z"/><line x1="12" y1="6.5" x2="12" y2="18" stroke="%s"/>' % GOLD,
    # --- maintenance ---
    "monthly": '<rect x="4" y="5.5" width="16" height="14.5" rx="1.5"/><line x1="4" y1="9.5" x2="20" y2="9.5"/><line x1="8" y1="3.5" x2="8" y2="6.5"/><line x1="16" y1="3.5" x2="16" y2="6.5"/><circle cx="9" cy="13.5" r="1.2" fill="%s" stroke="none"/>' % GOLD,
    "quarterly": '<rect x="4" y="5.5" width="16" height="14.5" rx="1.5"/><line x1="4" y1="9.5" x2="20" y2="9.5"/><line x1="8" y1="3.5" x2="8" y2="6.5"/><line x1="16" y1="3.5" x2="16" y2="6.5"/><path d="M15.2 15.4 a3 3 0 1 1 -0.9 -2.1" stroke="%s"/><path d="M14.6 11.8 v1.9 h-1.9" stroke="%s"/>' % (GOLD, GOLD),
}

# Human-readable labels for alt text.
LABELS = {
    "capture": "Capture", "clarify": "Clarify", "carry": "Carry",
    "keep": "Keep", "care": "Care", "never": "Never",
    "pause": "Good place to pause", "proofline": "Proof Line",
    "reconstruct": "Reconstruct", "match": "Match your proof to a role",
    "resume": "Resume line", "about": "About section",
    "interview": "Interview answer", "promotion": "Promotion note",
    "words": "Words to Stand On", "monthly": "Monthly sweep",
    "quarterly": "Quarterly review",
}

def names():
    return list(_ICONS.keys())

def svg(name, px=15, cls="ico", label=None, stroke=NAVY, sw=1.7):
    """Inline SVG markup for HTML outputs. label -> accessible; else decorative."""
    inner = _ICONS[name]
    if label is None:
        aria = ' aria-hidden="true"'
    else:
        lbl = LABELS.get(name, name) if label is True else label
        aria = ' role="img" aria-label="%s"' % lbl
    return ('<svg class="%s" width="%s" height="%s" viewBox="0 0 24 24" fill="none" '
            'stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s>%s</svg>'
            ) % (cls, px, px, stroke, sw, aria, inner)

def _standalone_svg(name):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            'fill="none" stroke="%s" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
            ) % (NAVY, _ICONS[name])

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def render_pngs(out_dir, scale=6.0, pad_frac=0.14):
    """Rasterize every icon to a transparent, square PNG for the .docx and the
    reportlab Tools PDF. Renders each icon through Chromium print-to-pdf (which
    draws SVG fully and sharply), rasterizes with pypdfium2, keys out the white
    background, and centers the icon in a square canvas so they align."""
    import pypdfium2 as pdfium
    from PIL import Image
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, "_tmp")
    os.makedirs(tmp, exist_ok=True)
    made = {}
    for name in _ICONS:
        html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
                '@page{size:0.5in 0.5in;margin:0}*{margin:0;padding:0}'
                'html,body{width:0.5in;height:0.5in}svg{display:block;width:0.5in;height:0.5in}'
                '</style></head><body>%s</body></html>') % _standalone_svg(name)
        hp = os.path.join(tmp, name + ".html")
        open(hp, "w", encoding="utf-8").write(html)
        pdfp = os.path.join(tmp, name + ".pdf")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", "--print-to-pdf=" + pdfp, "file://" + hp],
            capture_output=True, text=True)
        img = pdfium.PdfDocument(pdfp)[0].render(scale=scale).to_pil().convert("RGBA")
        px = img.load()
        w, h = img.size
        for y in range(h):
            for x in range(w):
                r, g, b, _ = px[x, y]
                d = 255 - min(r, g, b)           # 0 on white, large on ink
                a = max(0, min(255, (d - 6) * 3))  # key white, keep navy+gold opaque
                px[x, y] = (r, g, b, a)
        bbox = img.getbbox()
        icon = img.crop(bbox)
        side = int(max(icon.size) * (1 + pad_frac * 2))
        canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        canvas.paste(icon, ((side - icon.width) // 2, (side - icon.height) // 2), icon)
        pngp = os.path.join(out_dir, name + ".png")
        canvas.save(pngp)
        made[name] = pngp
    return made

if __name__ == "__main__":
    d = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
    m = render_pngs(os.path.abspath(d))
    print("rendered", len(m), "icons to", os.path.abspath(d))
    for n, p in m.items():
        print(" ", n, os.path.getsize(p) if os.path.exists(p) else "MISSING")
