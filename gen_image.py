#!/usr/bin/env python3
"""Generate license.png (1024x1024) for gta6-meme-x-01 v6 — authored fresh."""
from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1024
img = Image.new("RGB", (W, H), (18, 28, 46))
d = ImageDraw.Draw(img, "RGBA")

def font(size, bold=False):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()

# background: deep navy gradient bands + subtle stars
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(18+10*t), int(28+14*t), int(46+22*t)))
for i in range(90):
    x = (i * 137) % W; y = (i * 211) % 700
    d.ellipse([x, y, x+3, y+3], fill=(255, 255, 255, 60))

# card
x0, y0, x1, y1 = 72, 150, 952, 800
d.rounded_rectangle([x0, y0, x1, y1], radius=36, fill=(232, 238, 245), outline=(255, 215, 0), width=6)
# hologram shimmer diagonal
for i in range(0, 500, 26):
    d.polygon([(x0+120+i, y0), (x0+170+i, y0), (x0+40+i, y1), (x0-10+i, y1)], fill=(120, 200, 255, 18))
# header
d.text((x0+36, y0+22), "LEONIDA  •  STATE OF LEONIDA", font=font(30, True), fill=(12, 60, 120))
d.text((x0+36, y0+62), "DRIVER'S LICENSE", font=font(52, True), fill=(10, 30, 70))
d.text((x0+36, y0+122), "RENEWAL — GTA VI EDITION", font=font(26, True), fill=(180, 30, 30))
# gold seal
cx, cy = 860, 250
d.ellipse([cx-52, cy-52, cx+52, cy+52], outline=(200, 160, 0), width=5, fill=(255, 240, 180))
d.text((cx-32, cy-14), "LEONIDA", font=font(16, True), fill=(140, 100, 0))
d.text((cx-22, cy+12), "SEAL", font=font(20, True), fill=(140, 100, 0))

# photo area: silhouette of Lucia
px0, py0, px1, py1 = x0+36, y0+180, x0+236, y0+420
d.rounded_rectangle([px0, py0, px1, py1], radius=12, fill=(90, 130, 170), outline=(10, 30, 70), width=3)
# head + shoulders silhouette
d.ellipse([px0+62, py0+28, px0+138, py0+128], fill=(30, 30, 40))
d.pieslice([px0+18, py0+130, px0+182, py0+300], 180, 360, fill=(30, 30, 40))
# long hair hint
d.polygon([(px0+62, py0+40), (px0+45, py0+150), (px0+70, py0+150)], fill=(30, 30, 40))
d.polygon([(px0+138, py0+40), (px0+155, py0+150), (px0+130, py0+150)], fill=(30, 30, 40))
d.text((px0+28, py1-34), "L. CAMINOS", font=font(22, True), fill=(255, 255, 255))

# fields
fx = x0+270
rows = [
    ("NAME", "LUCIA CAMINOS"),
    ("DL No.", "L-2013-0926"),
    ("DOB", "04/12/1995"),
    ("ISSUED", "09/17/2013"),
    ("EXPIRES", "05/26/2026"),
]
yy = y0+180
for label, val in rows:
    d.text((fx, yy), label, font=font(22, True), fill=(100, 110, 130))
    d.text((fx, yy+26), val, font=font(32, True), fill=(10, 30, 70))
    yy += 58
# endorsement banner
by0 = y0+500
d.rounded_rectangle([x0+36, by0, x1-36, by0+86], radius=14, fill=(255, 215, 0))
d.text((x0+60, by0+10), "ENDORSEMENT:", font=font(26, True), fill=(120, 20, 20))
d.text((x0+60, by0+42), "GTA VI — VALID ONLY AFTER 13 YEARS", font=font(30, True), fill=(120, 20, 20))

# fee strip below card
fy0 = 830
d.rounded_rectangle([72, fy0, 952, fy0+86], radius=16, fill=(255, 255, 255), outline=(255, 215, 0), width=4)
d.text((100, fy0+14), "RENEWAL FEE  $13.00", font=font(38, True), fill=(10, 30, 70))
d.text((100, fy0+52), "PAID BY MY AI AGENT", font=font(24, True), fill=(180, 30, 30))

# caption + make.fun footer
d.text((72, 936), "She waited 13 years for GTA VI —", font=font(30, True), fill=(255, 255, 255))
d.text((72, 972), "her license expired before the game came out.", font=font(30, True), fill=(255, 255, 255))
# ghost (simple make.fun ghost) + footer, bottom-right clear of caption
gx, gy = 860, 925
d.ellipse([gx, gy, gx+80, gy+62], fill=(255, 255, 255))
d.polygon([(gx, gy+36), (gx+80, gy+36), (gx+80, gy+76), (gx+60, gy+58), (gx+40, gy+76), (gx+20, gy+58), (gx, gy+76)], fill=(255, 255, 255))
d.ellipse([gx+20, gy+20, gx+31, gy+34], fill=(0, 0, 0))
d.ellipse([gx+49, gy+20, gx+60, gy+34], fill=(0, 0, 0))
d.text((700, 948), "make.fun", font=font(24, True), fill=(255, 255, 255))

img.save("/home/hatch/workspace/makefun/gta6-meme-x-01-v6-work/license.png")
print("saved license.png", img.size)
