"""Generate the home screen icons. Run: python3 make-icon.py

A yellow pot on black, to match the Ritual look. iOS uses icon-180.png; the 512 is for the manifest.
"""

from PIL import Image, ImageDraw

YELLOW = (255, 255, 0)


def build(size: int) -> Image.Image:
    s = size * 4  # draw at 4x then downscale for smooth edges
    img = Image.new("RGB", (s, s), (0, 0, 0))
    d = ImageDraw.Draw(img)
    lw = int(s * 0.04)

    # pot body
    d.rounded_rectangle([s * 0.22, s * 0.42, s * 0.78, s * 0.74], radius=int(s * 0.06), fill=YELLOW)
    # handles
    d.rectangle([s * 0.12, s * 0.5, s * 0.22, s * 0.5 + lw], fill=YELLOW)
    d.rectangle([s * 0.78, s * 0.5, s * 0.88, s * 0.5 + lw], fill=YELLOW)
    # lid line
    d.rectangle([s * 0.2, s * 0.37, s * 0.8, s * 0.37 + lw], fill=YELLOW)
    # steam
    for x in (0.36, 0.5, 0.64):
        d.rectangle([s * x - lw / 2, s * 0.16, s * x + lw / 2, s * 0.30], fill=YELLOW)

    return img.resize((size, size), Image.LANCZOS)


for n in (180, 512):
    build(n).save(f"icon-{n}.png")
    print(f"wrote icon-{n}.png")
