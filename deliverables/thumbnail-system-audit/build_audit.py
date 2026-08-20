"""Three-video thumbnail system audit — evidence sheet.

Nothing here redesigns or alters any thumbnail. It documents what exists, what
the supplied candidates actually contain, and the evidence behind the findings.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD   = os.path.expanduser("~/.fonts/")
U    = "/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
R    = "/home/user/temidayoafonja-site/deliverables/video-1-slides/assets/"
V3   = "/home/user/temidayoafonja-site/deliverables/video-3-slides/thumbnail/"

NAVY=(15,35,70); CREAM=(245,240,232); GOLD=(201,168,76); DIM=(120,132,150)
RED=(176,42,30); GREEN=(24,110,72); PAPER=(250,247,241)

def f(sz,w="Regular"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w, sz)
def tw(d,t,fo):
    b=d.textbbox((0,0),t,font=fo); return b[2]-b[0]

SHEET = U+"6001a18e-D06EDCE604AA41DDAB5E39F7B2140791.png"
CAND  = {"WHAT STILL TRAVELS?":U+"a0eae78a-68FAF5F337634172A1CACFE71B54516B.png",
         "DON'T START FROM ZERO":U+"665cdc78-A8AD09C9AA8A4DC0BA06C0B135674D33.png",
         "YOUR EXPERIENCE COUNTS":U+"32446811-882C3CD3ABF7442882E3E44E4D5F23F3.png",
         "YOUR SKILLS ARE STALLING":U+"12f5ea72-DD8D67ED5A9C468DA16734C29B733899.png"}

W,H = 3000, 3460
s = Image.new("RGB",(W,H),PAPER); d = ImageDraw.Draw(s)

def head(y, t, sub=None):
    d.text((90,y), t, font=f(52,"Bold"), fill=NAVY)
    if sub: d.text((90,y+66), sub, font=f(30), fill=DIM)
    d.rectangle([90,y+(118 if sub else 70),W-90,y+(122 if sub else 74)], fill=GOLD)
    return y + (150 if sub else 100)

d.text((90,60), "THREE-VIDEO THUMBNAIL SYSTEM AUDIT", font=f(74,"ExtraBold"), fill=NAVY)
d.text((90,156), "Evidence sheet. No thumbnail was created, altered or redesigned to produce this.",
       font=f(32), fill=DIM)
d.rectangle([90,214,W-90,220], fill=GOLD)

# ---- BANNER
d.rectangle([90,250,W-90,430], fill=(253,238,236), outline=RED, width=4)
d.text((130,282), "FINDING: THE SUPPLIED VIDEO 1 AND VIDEO 2 CANDIDATES CONTAIN SYNTHETIC IMAGERY",
       font=f(40,"Bold"), fill=RED)
d.text((130,340), "They cannot be adopted as launch thumbnails without breaking the "
       "\"real photographs only\" rule. Evidence below.", font=f(30), fill=(140,40,30))
d.text((130,382), "No approved thumbnail exists for Video 1 or Video 2. Video 3 Final A is "
       "unaffected and remains valid.", font=f(30), fill=(140,40,30))

# ---- SECTION 1: real source photographs
y = head(480, "1. THE ONLY REAL PHOTOGRAPHS AVAILABLE",
         "Everything in the repository plus the approved Video 3 portrait. Four images, three outfits.")
reals = [("photo-headshot-green.png", R+"photo-headshot-green.png", "green BACKDROP, wine top"),
         ("photo-headshot-cream.png", R+"photo-headshot-cream.png", "cream backdrop, wine top"),
         ("photo-portrait-wine.png",  R+"photo-portrait-wine.png",  "room, wine top"),
         ("a55ff6e1...B5.png",        U+"a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png",
          "studio, caramel top (Video 3)")]
x = 90
for name, p, note in reals:
    im = Image.open(p).convert("RGB"); im.thumbnail((640,640))
    s.paste(im,(x,y)); d.rectangle([x,y,x+im.width,y+im.height], outline=(214,204,186), width=3)
    d.text((x,y+im.height+16), name, font=f(26,"Bold"), fill=NAVY)
    d.text((x,y+im.height+52), note, font=f(24), fill=DIM)
    x += 720
y += 700
d.rectangle([90,y,W-90,y+108], fill=(240,246,242), outline=GREEN, width=3)
d.text((124,y+18), "No purple-outfit photograph and no green-shirt photograph exists.",
       font=f(34,"Bold"), fill=GREEN)
d.text((124,y+62), "\"Green\" in the asset name is the BACKDROP. In all three repo photographs "
       "she wears the same wine top.", font=f(27), fill=(40,90,64))
y += 168

# ---- SECTION 2: evidence
y = head(y, "2. EVIDENCE OF SYNTHESIS", "Magnified from the supplied files at native resolution.")

def evid(x, y, img, cap, why, boxw=880):
    im = img.copy(); im.thumbnail((boxw, 520))
    s.paste(im,(x,y)); d.rectangle([x,y,x+im.width,y+im.height], outline=RED, width=4)
    d.text((x,y+im.height+16), cap, font=f(28,"Bold"), fill=RED)
    yy = y+im.height+56
    for line in why:
        d.text((x,yy), line, font=f(25), fill=(70,80,100)); yy += 34
    return im.height

sh = Image.open(SHEET)
c3 = Image.open(CAND["YOUR EXPERIENCE COUNTS"])

e1 = c3.crop((int(c3.width*0.56),int(c3.height*0.70),int(c3.width*0.78),int(c3.height*0.98)))
e1 = e1.resize((e1.width*3,e1.height*3), Image.LANCZOS)
evid(90, y, e1, "A. A different person as her career history",
     ["Middle inset of \"YOUR EXPERIENCE COUNTS\".", "Different face, different hair, business suit.",
      "This is not Temidayo."], 560)

e2 = sh.crop((415,355,706,622)); e2 = e2.resize((e2.width*3,e2.height*3), Image.LANCZOS)
evid(760, y, e2, "B. A pose and setting that never existed",
     ["Contact-sheet panel 2. Caramel top, but seated at",
      "a desk, finger to temple, full office behind.",
      "The real caramel photo is a plain studio headshot."], 700)

e3 = sh.crop((185,600,275,665)); e3 = e3.resize((e3.width*8,e3.height*8), Image.LANCZOS)
evid(1560, y, e3, "C. Pseudo-text on the papers",
     ["Same panel, magnified 8x. The sticky notes carry",
      "letter-shaped marks that spell nothing.",
      "This is a signature of image generation."], 700)

e4 = sh.crop((300,20,520,300)); e4 = e4.resize((e4.width*3,e4.height*3), Image.LANCZOS)
evid(2320, y, e4, "D. Garments that do not exist",
     ["Contact-sheet panel 1A insets: purple suit and",
      "green shirt. No such photograph was supplied.",
      "Fabricated to fill an expected visual story."], 580)
y += 700

# ---- SECTION 3: what the sheet claims
d.rectangle([90,y,W-90,y+150], fill=(253,238,236), outline=RED, width=4)
d.text((130,y+24), "THE SUPPLIED CONTACT SHEET CARRIES A FALSE ASSURANCE", font=f(38,"Bold"), fill=RED)
d.text((130,y+76), "Its footer reads: \"No part of Temidayo's appearance was generated or altered. "
       "All thumbnails use original", font=f(28), fill=(140,40,30))
d.text((130,y+112), "photographs only.\"  Items A to D above contradict that claim directly.",
       font=f(28), fill=(140,40,30))
y += 200

# ---- SECTION 4: video 3 stands
y = head(y, "3. VIDEO 3 IS UNAFFECTED",
         "Built only from the verified caramel studio portrait. Crop, Lanczos resize and placement.")
a = Image.open(V3+"VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png"); a.thumbnail((1200,700))
s.paste(a,(90,y)); d.rectangle([90,y,90+a.width,y+a.height], outline=GREEN, width=4)
d.text((90,y+a.height+18), "VIDEO 3 FINAL A — APPROVED", font=f(34,"Bold"), fill=GREEN)
tx = 1360
for t,st in [("1280 x 720, exactly 16:9","ok"),("200,945 bytes, 9.6% of the 2 MB limit","ok"),
             ("Pixel-identical to the approved contact sheet","ok"),
             ("Source: a55ff6e1...B5.png, 1254 x 1254","ok"),
             ("Nothing generated, reconstructed or retouched","ok")]:
    d.line([(tx+6,y+22),(tx+22,y+38)], fill=GREEN, width=8)
    d.line([(tx+22,y+38),(tx+54,y+6)], fill=GREEN, width=8)
    d.text((tx+82,y), t, font=f(30), fill=(60,70,90)); y += 62
y += 70

d.rectangle([90,H-150,W-90,H-90], fill=NAVY)
d.text((124,H-136), "No existing thumbnail was overwritten. No source photograph was modified. "
       "No website, slide, script or product file was changed.", font=f(27), fill=CREAM)
s.save(os.path.join(HERE,"THUMBNAIL_SYSTEM_AUDIT_EVIDENCE.png"))
print("built", s.size)
