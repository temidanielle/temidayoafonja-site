# Card generator

Renders the six Capability Audit quote cards and the Density teaser card from
one template system, so future card runs are a single command.

```bash
pip install Pillow          # once
python3 tools/cards/generate_cards.py
```

Outputs seven PNGs to the repository root:

- `quote_look_safe.png`, `quote_compounding_corner.png`,
  `quote_advice_kindness.png`, `quote_retention_risk.png`,
  `quote_competitor_twice.png`, `quote_title_travel.png` — portrait 2160×2700
- `teaser_density.png` — landscape 2245×1587

Fonts (Cormorant Garamond, Montserrat) are bundled under `fonts/` so rendering
is fully offline and deterministic. Palette, sizes, and copy live at the top of
`generate_cards.py`; edit there to adjust the whole set.
