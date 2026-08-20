"""Derivatives, placement simulations and reference sheets for the Video 3 thumbnail.

Reads the two masters produced by build_thumbnails.py. Every simulation below is a
mock of YouTube surface geometry drawn locally. Where a real surface would show a
view count or an upload date, the words "views" and "date" appear literally,
because no real figures exist for an unpublished video.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD   = os.path.expanduser("~/.fonts/")
TITLE = "3 Things to Do Before Quitting Your Job"
CHAN  = "Temidayo Afonja"

def f(sz, w="Regular"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)

def tw(d, t, fo):
    b = d.textbbox((0,0), t, font=fo); return b[2]-b[0]

def wrap(d, text, fo, width, maxlines=2):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if tw(d, trial, fo) <= width: cur = trial
        else:
            lines.append(cur); cur = w_
            if len(lines) == maxlines: break
    if cur and len(lines) < maxlines: lines.append(cur)
    if len(lines) == maxlines and tw(d, lines[-1], fo) > width - 40:
        while lines[-1] and tw(d, lines[-1] + "...", fo) > width:
            lines[-1] = lines[-1][:-1]
        lines[-1] += "..."
    return lines

M = {n: Image.open(os.path.join(HERE, "VIDEO_3_THUMBNAIL_FINAL_%s_3840x2160.png" % n))
     for n in ("A","B")}

# ------------------------------------------------------------ 1. derivatives
manifest = []
def note(fn, what):
    p = os.path.join(HERE, fn)
    manifest.append((fn, os.path.getsize(p), what))

for n, im in M.items():
    note("VIDEO_3_THUMBNAIL_FINAL_%s_3840x2160.png" % n, "Master, lossless PNG")

    hq = os.path.join(HERE, "VIDEO_3_THUMBNAIL_FINAL_%s_3840x2160_q95.jpg" % n)
    im.save(hq, "JPEG", quality=95, subsampling=0, optimize=True)
    note(os.path.basename(hq), "High quality JPG, 4:4:4 chroma, quality 95")

    up = os.path.join(HERE, "VIDEO_3_THUMBNAIL_FINAL_%s_UPLOAD_1280x720.jpg" % n)
    small = im.resize((1280,720), Image.LANCZOS)
    q = 95
    while q >= 60:
        small.save(up, "JPEG", quality=q, subsampling=0, optimize=True, progressive=True)
        if os.path.getsize(up) <= 2*1024*1024: break
        q -= 3
    note(os.path.basename(up),
         "YouTube upload file, 1280x720, JPG quality %d, %.0f KB, under the 2 MB limit"
         % (q, os.path.getsize(up)/1024))

    for px in (640, 360, 200):
        fn = "preview-%s-%dpx.png" % (n.lower(), px)
        im.resize((px, round(px*9/16)), Image.LANCZOS).save(os.path.join(HERE, fn))
        note(fn, "Legibility preview at %d px wide" % px)

# ------------------------------------------------------- 2. surface mock-ups
def theme(dark):
    return dict(bg=(15,15,15) if dark else (255,255,255),
                fg=(241,241,241) if dark else (15,15,15),
                mut=(170,170,170) if dark else (96,96,96),
                line=(48,48,48) if dark else (229,229,229))

def thumb(im, w):
    return im.resize((w, round(w*9/16)), Image.LANCZOS)

def mobile_feed(im, dark):
    T = theme(dark); PW = 1080
    c = Image.new("RGB", (PW, 980), T["bg"]); d = ImageDraw.Draw(c)
    d.rectangle([0,0,PW,120], fill=T["bg"])
    d.text((40,46), "Home", font=f(38,"Bold"), fill=T["fg"])
    d.line([(0,120),(PW,120)], fill=T["line"])
    t = thumb(im, PW); c.paste(t, (0,150))
    y = 150 + t.height
    d.rounded_rectangle([PW-146, y-56, PW-24, y-16], 8, fill=(0,0,0))
    d.text((PW-134, y-50), "9:50", font=f(24,"Bold"), fill=(255,255,255))
    d.ellipse([32, y+34, 128, y+130], fill=(200,178,140))
    fo = f(34,"Bold")
    for i,l in enumerate(wrap(d, TITLE, fo, PW-230)):
        d.text((156, y+34+i*46), l, font=fo, fill=T["fg"])
    d.text((156, y+140), CHAN + "  ·  views  ·  date", font=f(28), fill=T["mut"])
    return c

def search_row(im, dark):
    T = theme(dark); PW = 1080
    c = Image.new("RGB", (PW, 620), T["bg"]); d = ImageDraw.Draw(c)
    d.rounded_rectangle([32,34,PW-32,124], 45, outline=T["line"], width=3)
    d.text((80,62), "quitting my job", font=f(32), fill=T["mut"])
    t = thumb(im, 470); c.paste(t, (32,180))
    d.rounded_rectangle([432, 180+t.height-52, 486, 180+t.height-14], 6, fill=(0,0,0))
    d.text((440, 180+t.height-48), "9:50", font=f(20,"Bold"), fill=(255,255,255))
    fo = f(32,"Bold")
    for i,l in enumerate(wrap(d, TITLE, fo, PW-560)):
        d.text((530, 186+i*44), l, font=fo, fill=T["fg"])
    d.text((530, 290), CHAN, font=f(26), fill=T["mut"])
    d.text((530, 332), "views  ·  date", font=f(26), fill=T["mut"])
    return c

def right_column(im, dark):
    T = theme(dark); PW = 820
    c = Image.new("RGB", (PW, 730), T["bg"]); d = ImageDraw.Draw(c)
    d.text((28,26), "Up next", font=f(30,"Bold"), fill=T["fg"])
    for r in range(3):
        y = 90 + r*160
        src = im if r == 1 else im
        t = thumb(src, 336); c.paste(t, (28,y))
        if r != 1:
            t2 = t.copy(); t2 = t2.point(lambda v: int(v*0.45 + 128*0.55))
            c.paste(t2, (28,y))
        fo = f(26,"Bold")
        for i,l in enumerate(wrap(d, TITLE, fo, PW-420)):
            d.text((392, y+4+i*36), l, font=fo, fill=T["fg"] if r==1 else T["mut"])
        d.text((392, y+92), CHAN, font=f(23), fill=T["mut"])
    d.text((28, 668), "middle row is this thumbnail; rows above and below are dimmed placeholders",
           font=f(19), fill=T["mut"])
    return c

for n, im in M.items():
    for dark in (False, True):
        tag = "dark" if dark else "light"
        panels = [("Mobile home feed", mobile_feed(im, dark)),
                  ("Mobile search results", search_row(im, dark)),
                  ("Desktop right column", right_column(im, dark))]
        gap, pad = 60, 70
        SW = pad*2 + sum(p.width for _,p in panels) + gap*(len(panels)-1)
        SH = pad + 150 + max(p.height for _,p in panels) + 90
        T = theme(dark)
        s = Image.new("RGB", (SW,SH), (24,24,24) if dark else (250,247,241))
        d = ImageDraw.Draw(s)
        head = (245,240,232) if dark else (15,35,70)
        d.text((pad,50), "FINAL %s — PLACEMENT SIMULATIONS — %s MODE" % (n, tag.upper()),
               font=f(46,"Bold"), fill=head)
        d.rectangle([pad,120,SW-pad,124], fill=(201,168,76))
        x = pad
        for label, p in panels:
            s.paste(p, (x,190))
            d.rectangle([x,190,x+p.width,190+p.height], outline=T["line"], width=2)
            d.text((x,150), label, font=f(30,"Bold"), fill=head)
            x += p.width + gap
        d.text((pad, SH-60), "Surface geometry is mocked locally. \"views\" and \"date\" are "
               "placeholders; no real figures exist for an unpublished video. 9:50 is the estimated runtime.",
               font=f(24), fill=(150,150,150) if dark else (120,132,150))
        fn = "placement-%s-%s.png" % (n.lower(), tag)
        s.save(os.path.join(HERE, fn))
        note(fn, "Final %s on mobile feed, mobile search and desktop right column, %s mode" % (n, tag))

# --------------------------------------------- 3. 200 px side by side + sheet
NAVY=(15,35,70); DIMC=(120,132,150); GOLDC=(201,168,76)
c = Image.new("RGB", (1900, 900), (250,247,241)); d = ImageDraw.Draw(c)
d.text((70,56), "AT 200 PIXELS WIDE", font=f(52,"Bold"), fill=NAVY)
d.text((70,124), "Native 200 px on the left of each pair, then the same pixels enlarged "
                 "four times so nothing is hidden by scale.", font=f(28), fill=DIMC)
d.rectangle([70,182,1830,186], fill=GOLDC)
for i,(n,im) in enumerate(sorted(M.items())):
    x = 70 + i*900; y = 250
    sm = im.resize((200,113), Image.LANCZOS)
    c.paste(sm,(x,y)); d.rectangle([x,y,x+200,y+113], outline=(214,204,186), width=2)
    c.paste(sm.resize((640,362), Image.NEAREST),(x+40,y+160))
    d.rectangle([x+40,y+160,x+680,y+522], outline=(214,204,186), width=2)
    d.text((x, y+545), "FINAL %s" % n, font=f(38,"Bold"), fill=NAVY)
c.save(os.path.join(HERE, "comparison-200px.png"))
note("comparison-200px.png", "Final A and Final B side by side at 200 px, native and enlarged")

SW, SH = 3400, 2500
s = Image.new("RGB", (SW,SH), (250,247,241)); d = ImageDraw.Draw(s)
d.text((90,66), "VIDEO 3 THUMBNAIL — FINAL MASTERS", font=f(60,"Bold"), fill=NAVY)
d.text((90,152), "Built from the approved portrait "
       "a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png, 1254 x 1254. "
       "Crop, Lanczos resize and placement only.", font=f(34), fill=DIMC)
d.rectangle([90,232,SW-90,236], fill=GOLDC)
tw_, th_ = 1520, 855
for i,(n,im) in enumerate(sorted(M.items())):
    x = 90 + i*(tw_+120); y = 310
    s.paste(im.resize((tw_,th_), Image.LANCZOS), (x,y))
    d.rectangle([x,y,x+tw_,y+th_], outline=(214,204,186), width=3)
    lab = ("FINAL A, recommended" if n=="A" else "FINAL B, alternate")
    note_ = ("Portrait right, navy headline on cream, gold seam and underscore."
             if n=="A" else
             "Portrait left, navy panel right, WAIT carried in gold.")
    d.text((x, y+th_+30), lab, font=f(44,"Bold"), fill=NAVY)
    d.text((x, y+th_+92), note_, font=f(30), fill=DIMC)
d.text((90,1350), "STEPPED DOWN: 640, 360, 200 PX", font=f(44,"Bold"), fill=NAVY)
for i,(n,im) in enumerate(sorted(M.items())):
    x = 90 + i*(tw_+120); y = 1430
    for px in (640,360,200):
        t = im.resize((px, round(px*9/16)), Image.LANCZOS)
        s.paste(t,(x,y)); d.rectangle([x,y,x+px,y+t.height], outline=(214,204,186), width=2)
        d.text((x+px+22, y+t.height-34), "%d px" % px, font=f(26), fill=DIMC)
        y += t.height + 26
    d.text((x, y+10), "FINAL %s" % n, font=f(34,"Bold"), fill=NAVY)
d.text((90,SH-150), "No part of the photograph was generated, reconstructed, retouched or "
       "extended. No substitute image was used.", font=f(30), fill=DIMC)
s.save(os.path.join(HERE, "contact-sheet-final.png"))
note("contact-sheet-final.png", "Both finals, plus each stepped down through 640, 360 and 200 px")

for fn, sz, what in manifest:
    print("%-58s %8.1f KB  %s" % (fn, sz/1024, what))
