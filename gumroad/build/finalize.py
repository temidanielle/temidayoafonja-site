#!/usr/bin/env python3
"""Reduced-size tests, Image 01 1280x720 export, contact sheet, and programmatic
QA for the Gumroad merchandising system. Downscales use Lanczos."""
import os, hashlib
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.abspath(os.path.join(HERE,".."))
PNG=os.path.join(OUT,"png"); RED=os.path.join(OUT,"reduced")
os.makedirs(RED,exist_ok=True)
FONT=os.path.expanduser("~/.fonts/DM-Medium.ttf")

THUMB="fieldkit_gumroad_thumbnail_600x600"
IMGS=[("01","fieldkit_gumroad_01_recognition_1600x900"),
      ("02","fieldkit_gumroad_02_outputs_1600x900"),
      ("03","fieldkit_gumroad_03_product_proof_1600x900"),
      ("04","fieldkit_gumroad_04_evidence_method_1600x900"),
      ("05","fieldkit_gumroad_05_free_vs_fieldkit_1600x900"),
      ("06","fieldkit_gumroad_06_fieldkit_vs_live_1600x900")]

def lanczos(src,dst,size):
    Image.open(src).convert("RGB").resize(size,Image.LANCZOS).save(dst,"PNG")

# --- reduced tests ---
lanczos(f"{PNG}/{THUMB}.png", f"{RED}/fieldkit_gumroad_thumbnail_240x240.png",(240,240))
lanczos(f"{PNG}/{THUMB}.png", f"{RED}/fieldkit_gumroad_thumbnail_180x180.png",(180,180))
for _,n in IMGS:
    lanczos(f"{PNG}/{n}.png", f"{RED}/{n.rsplit('_',1)[0]}_640x360.png",(640,360))
# --- Image 01 1280x720 export (into png/) ---
lanczos(f"{PNG}/fieldkit_gumroad_01_recognition_1600x900.png",
        f"{PNG}/fieldkit_gumroad_01_recognition_1280x720.png",(1280,720))

# --- contact sheet: 7 assets in order ---
def label(draw,x,y,t):
    try: f=ImageFont.truetype(FONT,22)
    except: f=ImageFont.load_default()
    draw.text((x,y),t,fill="#0F2347",font=f)
cs_w=1720; pad=40; col_w=(cs_w-pad*3)//2
rows=[("1  Product-card thumbnail",f"{PNG}/{THUMB}.png"),
      ("2  Image 01: Recognition",f"{PNG}/fieldkit_gumroad_01_recognition_1600x900.png"),
      ("3  Image 02: Tangible outputs",f"{PNG}/fieldkit_gumroad_02_outputs_1600x900.png"),
      ("4  Image 03: Product proof",f"{PNG}/fieldkit_gumroad_03_product_proof_1600x900.png"),
      ("5  Image 04: Evidence method",f"{PNG}/fieldkit_gumroad_04_evidence_method_1600x900.png"),
      ("6  Image 05: Free vs $150",f"{PNG}/fieldkit_gumroad_05_free_vs_fieldkit_1600x900.png"),
      ("7  Image 06: $150 vs $500",f"{PNG}/fieldkit_gumroad_06_fieldkit_vs_live_1600x900.png")]
# layout: thumbnail on its own top row (square), then 6 landscape in 2 cols x 3 rows
thumb_h=col_w  # square uses col width
land_h=int(col_w*9/16)
sheet_h=pad + 30 + thumb_h + pad + (30+land_h+pad)*3 + 20
cs=Image.new("RGB",(cs_w,sheet_h),"#EFEAE0"); d=ImageDraw.Draw(cs)
# thumbnail centered top
label(d,pad,pad,rows[0][0])
th=Image.open(rows[0][1]).convert("RGB").resize((thumb_h,thumb_h),Image.LANCZOS)
cs.paste(th,(pad,pad+30))
# a caption block right of thumbnail
label(d,pad+thumb_h+40,pad+30,"Capability Formation Field Kit")
label(d,pad+thumb_h+40,pad+66,"Gumroad merchandising system")
label(d,pad+thumb_h+40,pad+110,"7 approved assets  |  contact sheet (review only)")
y=pad+30+thumb_h+pad
for i,(cap,path) in enumerate(rows[1:]):
    col=i%2; row=i//2
    x=pad+col*(col_w+pad); yy=y+row*(30+land_h+pad)
    label(d,x,yy,cap)
    im=Image.open(path).convert("RGB").resize((col_w,land_h),Image.LANCZOS)
    cs.paste(im,(x,yy+30))
cs.save(f"{OUT}/contact-sheet.png","PNG")

# --- programmatic QA ---
def info(p):
    im=Image.open(p); return im.size, im.mode, im.format, os.path.getsize(p), hashlib.md5(open(p,'rb').read()).hexdigest()[:12]
checks=[]
def expect(path,w,h):
    (sw,sh),mode,fmt,sz,md5=info(path)
    ok = (sw==w and sh==h and mode=="RGB" and fmt=="PNG")
    checks.append((os.path.relpath(path,OUT),f"{sw}x{sh}",mode,fmt,sz,"PASS" if ok else "FAIL"))
expect(f"{PNG}/{THUMB}.png",600,600)
expect(f"{RED}/fieldkit_gumroad_thumbnail_240x240.png",240,240)
expect(f"{RED}/fieldkit_gumroad_thumbnail_180x180.png",180,180)
for _,n in IMGS:
    expect(f"{PNG}/{n}.png",1600,900)
    expect(f"{RED}/{n.rsplit('_',1)[0]}_640x360.png",640,360)
expect(f"{PNG}/fieldkit_gumroad_01_recognition_1280x720.png",1280,720)
print(f"{'file':60s} {'dims':10s} {'mode':5s} {'fmt':4s} {'bytes':>8s}  result")
allok=True
for rel,dims,mode,fmt,sz,res in checks:
    if res=="FAIL": allok=False
    print(f"{rel:60s} {dims:10s} {mode:5s} {fmt:4s} {sz:8d}  {res}")
print("\nALL PASS" if allok else "\nFAILURES PRESENT")
