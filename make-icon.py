"""Generate the home screen icons. Run: python3 make-icon.py

A red pot with a blue offset shadow on off-white, matching the app's broken-grid look.
iOS uses icon-180.png; the 512 is for the manifest.
"""

from PIL import Image, ImageDraw

BG = (245, 244, 240)
RED = (255, 61, 26)
BLUE = (26, 26, 255)
INK = (16, 16, 16)


def pot(d, s, dx, dy, fill, outline=None):
    lw = int(s * 0.045)
    def box(x0, y0, x1, y1, r=0):
        d.rounded_rectangle([s * x0 + dx, s * y0 + dy, s * x1 + dx, s * y1 + dy], radius=r, fill=fill)
    box(0.22, 0.44, 0.78, 0.76)          # body
    box(0.12, 0.52, 0.22, 0.52 + lw / s)  # left handle
    box(0.78, 0.52, 0.88, 0.52 + lw / s)  # right handle
    box(0.20, 0.38, 0.80, 0.38 + lw / s)  # lid
    for x in (0.36, 0.5, 0.64):          # steam
        d.rectangle([s * x - lw / 2 + dx, s * 0.16 + dy, s * x + lw / 2 + dx, s * 0.31 + dy], fill=fill)


def build(size: int) -> Image.Image:
    s = size * 4  # draw at 4x then downscale for smooth edges
    img = Image.new("RGB", (s, s), BG)
    d = ImageDraw.Draw(img)
    off = int(s * 0.035)
    pot(d, s, off * 2, off * 2, INK)   # hard shadow
    pot(d, s, off, off, BLUE)          # offset layer
    pot(d, s, 0, 0, RED)
    return img.resize((size, size), Image.LANCZOS)


for n in (180, 512):
    build(n).save(f"icon-{n}.png")
    print(f"wrote icon-{n}.png")
