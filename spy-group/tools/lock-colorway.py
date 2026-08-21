#!/usr/bin/env python3
"""Produce a standalone single-colorway copy of manifest/index.html.

The prototype page ships with a colorway picker so a reviewer can compare
Ink, Harbor, Slate and Field in place. To send one colorway on its own,
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
    'ink': {},
    'harbor': {
        'field-900': '#0F2833', 'field-800': '#163542', 'field-700': '#1E4453',
        'field-600': '#2F5D6E', 'bone': '#ECEFEF', 'bone-2': '#F7F9F9',
        'accent': '#E7A860', 'accent-ink': '#92561A', 'accent-hover': '#F2BC80',
        'sage': '#9CB8C4', 'ink': '#14262E', 'muted': '#4C5C64',
        'line': 'rgba(20,38,46,.16)', 'accent-rgb': '231,168,96',
        'sage-rgb': '156,184,196', 'bone-rgb': '236,239,239',
    },
    'slate': {
        'field-900': '#1B222C', 'field-800': '#232C38', 'field-700': '#2E3947',
        'field-600': '#435162', 'bone': '#EEEFF1', 'bone-2': '#F8F9FA',
        'accent': '#6BB2E8', 'accent-ink': '#1F5F91', 'accent-hover': '#8CC6F0',
        'sage': '#9AA6B5', 'ink': '#1A2029', 'muted': '#515964',
        'line': 'rgba(26,32,41,.16)', 'accent-rgb': '107,178,232',
        'sage-rgb': '154,166,181', 'bone-rgb': '238,239,241',
    },
    'field': {
        'field-900': '#182A22', 'field-800': '#20362C', 'field-700': '#284238',
        'field-600': '#3C5B4B', 'bone': '#EDEDE5', 'bone-2': '#F7F7F2',
        'accent': '#DFA03A', 'accent-ink': '#8C5A0F', 'accent-hover': '#EDB055',
        'sage': '#9DB2A5', 'ink': '#16211C', 'muted': '#4E5B54',
        'line': 'rgba(22,33,28,.16)', 'accent-rgb': '223,160,58',
        'sage-rgb': '157,178,165', 'bone-rgb': '237,237,229',
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
    baked = baked.replace('Default colorway: INK — neutral charcoal with a copper accent.',
                          f'Colorway: {colorway.upper()}. Baked in by tools/lock-colorway.py.')
    s = s.replace(root, baked)

    # 2. Drop the alternate colorway blocks.
    s = re.sub(r'\n/\* ── COLORWAYS ─+.*?\n:root\[data-palette="field"\]\{.*?\n\}\n', '\n', s, flags=re.S)

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
