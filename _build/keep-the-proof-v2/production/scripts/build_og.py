#!/usr/bin/env python3
"""Regenerate og-keep-the-proof.png (1200x630) for V2."""
import subprocess, os, base64
ROOT="/home/user/temidayoafonja-site"
FONTS=f"file://{ROOT}/fonts"
# embed the V2 cover as data URI
cover_b64 = base64.b64encode(open(f"{ROOT}/keep-the-proof-v2-cover.png","rb").read()).decode()
NAVY="#112345"; CREAM="#F5F1E8"; GOLD="#C9A84C"
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-600-normal-latin-abcaa8.woff2') format('woff2');font-weight:600;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-italic-latin-4db21d.woff2') format('woff2');font-weight:400;font-style:italic;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-500-normal-latin-1c49a6.woff2') format('woff2');font-weight:500;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1200px;height:630px;overflow:hidden;}}
.og{{width:1200px;height:630px;background:{NAVY};display:flex;align-items:center;position:relative;font-family:'DM Sans',sans-serif;}}
.left{{padding:0 0 0 70px;width:720px;}}
.eyebrow{{color:{GOLD};font-weight:500;letter-spacing:.28em;font-size:17px;margin-bottom:26px;}}
.headline{{font-family:'Cormorant',serif;font-weight:600;color:{CREAM};font-size:56px;line-height:1.04;margin-bottom:26px;}}
.rule{{width:60px;height:3px;background:{GOLD};margin-bottom:22px;}}
.desc{{font-family:'Cormorant',serif;font-style:italic;color:#d8d0bf;font-size:26px;line-height:1.25;}}
.site{{position:absolute;left:70px;bottom:44px;color:{GOLD};font-weight:500;letter-spacing:.06em;font-size:18px;}}
.right{{position:absolute;right:64px;top:50%;transform:translateY(-50%);}}
.right img{{height:470px;box-shadow:0 24px 60px rgba(0,0,0,.5);border-radius:3px;}}
</style></head><body>
<div class="og">
  <div class="left">
    <div class="eyebrow">KEEP THE PROOF</div>
    <div class="headline">Build the evidence before<br>you need to prove your value.</div>
    <div class="rule"></div>
    <div class="desc">A guided system for building<br>your professional record.</div>
  </div>
  <div class="site">temidayoafonja.com</div>
  <div class="right"><img src="data:image/png;base64,{cover_b64}"></div>
</div>
</body></html>'''
open("/tmp/og.html","w").write(html)
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
# screenshot at exact size
r=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox",
   "--force-device-scale-factor=1","--window-size=1200,630",
   "--screenshot=/tmp/og_new.png","--default-background-color=00000000",
   "file:///tmp/og.html"],capture_output=True,text=True)
print("rc",r.returncode, r.stderr[-300:] if r.returncode else "")
from PIL import Image
im=Image.open("/tmp/og_new.png").convert("RGB")
print("shot size", im.size)
im=im.resize((1200,630))
im.save(f"{ROOT}/og-keep-the-proof.png")
print("saved og", os.path.getsize(f"{ROOT}/og-keep-the-proof.png"))
