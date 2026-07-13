from PIL import Image, ImageDraw

SIZE = 1024
NAVY = (0x0F, 0x23, 0x47)
GOLD = (0xC9, 0xA8, 0x4C)
STROKE = 3
RADII = [120, 190, 260, 330, 400]

img = Image.new("RGB", (SIZE, SIZE), NAVY)
draw = ImageDraw.Draw(img)

cx = cy = SIZE // 2

for i, r in enumerate(sorted(RADII)):
    bbox = [cx - r, cy - r, cx + r, cy + r]
    if i == 0:
        # Innermost circle filled solid gold
        draw.ellipse(bbox, fill=GOLD)
    else:
        # Outlines only
        draw.ellipse(bbox, outline=GOLD, width=STROKE)

img.save("publication_logo_1024.png")
print("Saved publication_logo_1024.png")
