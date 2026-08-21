#!/usr/bin/env python3
"""Produce a standalone single-colorway copy of manifest/index.html.

The prototype page ships with a colorway picker so a reviewer can compare
the three Harbor steps in place. To send one colorway on its own,
this bakes the chosen token set into :root and strips the picker — its
CSS, its markup and its script — so the result is an ordinary page with no
review controls on it.

    python3 tools/lock-colorway.py harbor out/harbor.html

Run from the spy-group directory. The picker version stays the source of
truth; these copies are generated, never hand-edited.
"""
import re
import sys

# Only the slots that differ between colorways. Ink is the stylesheet's
# own :root, so locking to Ink just strips the picker.
COLORWAYS = {
    # Harbor Light is the stylesheet's own :root, so locking to it just
    # strips the picker. Keep these in step with the :root[data-palette]
    # blocks in manifest/index.html.
    'harbor-light': {},
    'harbor': {
        'field-900': '#0F2833', 'field-800': '#163542', 'field-700': '#1E4453',
        'field-600': '#2F5D6E', 'bone': '#ECEFEF', 'bone-2': '#F7F9F9',
        'accent': '#E7A860', 'accent-ink': '#92561A', 'accent-hover': '#F2BC80',
        'sage': '#9CB8C4', 'ink': '#14262E', 'muted': '#4C5C64',
        'line': 'rgba(20,38,46,.16)', 'accent-rgb': '231,168,96',
        'sage-rgb': '156,184,196', 'bone-rgb': '236,239,239',
    },
    'harbor-lighter': {
        'field-900': '#1F3647', 'field-800': '#28475D', 'field-700': '#315772',
        'field-600': '#487799', 'bone': '#EEF0F2', 'bone-2': '#F8FAFB',
        'accent': '#F0C79C', 'accent-ink': '#8E5A22', 'accent-hover': '#F6D5B2',
        'sage': '#B8CFD8', 'ink': '#17262F', 'muted': '#4E5D67',
        'line': 'rgba(23,38,47,.16)', 'accent-rgb': '240,199,156',
        'sage-rgb': '184,207,216', 'bone-rgb': '238,240,242',
    },
}

PLAIN_PROTO_CSS = """.proto{
  background:var(--field-900);color:var(--accent);
  font-family:var(--mono);font-size:11px;letter-spacing:.12em;
  text-transform:uppercase;text-align:center;padding:7px 16px;
  border-bottom:1px solid var(--field-600);
}
.proto span{color:var(--sage);}"""

PLAIN_PROTO_HTML = ('<div class="proto">Prototype for review <span>— identifiers marked '
                    '“pending” are placeholders, not live registration data</span></div>')


def lock(src, colorway):
    if colorway not in COLORWAYS:
        raise SystemExit(f'unknown colorway {colorway!r}; pick one of {", ".join(COLORWAYS)}')
    s = open(src, encoding='utf-8').read()

    # 1. Bake the chosen values into :root.
    root = s[s.index(':root {'):s.index('}', s.index(':root {')) + 1]
    baked = root
    for slot, value in COLORWAYS[colorway].items():
        baked, n = re.subn(rf'(--{re.escape(slot)}:)[^;]+;', rf'\g<1>{value};', baked, count=1)
        if n != 1:
            raise SystemExit(f'token --{slot} not found in :root')
    baked = re.sub(r'Default colorway: [^\n]+', 
                   f'Colorway: {colorway}. Baked in by tools/lock-colorway.py.', baked, count=1)
    s = s.replace(root, baked)

    # 2. Drop the alternate colorway blocks.
    s = re.sub(r'\n/\* ── COLORWAYS ─+.*?\n:root\[data-palette="harbor-lighter"\]\{.*?\n\}\n', '\n', s, flags=re.S)

    # 3. Drop the picker: stylesheet, markup, script.
    s = re.sub(r'\.proto\{.*?\.picker i\{[^}]*\}', PLAIN_PROTO_CSS, s, count=1, flags=re.S)
    s = re.sub(r'<div class="proto">.*?</div>', PLAIN_PROTO_HTML, s, count=1, flags=re.S)
    s = re.sub(r'\n<script>\n/\* Colorway picker\..*?\n</script>', '', s, count=1, flags=re.S)

    for leftover in ('data-palette', 'class="picker"', 'data-set='):
        if leftover in s:
            raise SystemExit(f'picker remnant left in output: {leftover}')
    return s


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    out = lock('manifest/index.html', sys.argv[1])
    open(sys.argv[2], 'w', encoding='utf-8').write(out)
    print(f'{sys.argv[2]}: {len(out) // 1024} KB')
