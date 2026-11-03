#!/usr/bin/env python3
"""Render SVG logos into one PNG proof sheet so they can be judged side by side.

For each SVG it shows: the logo large on light, the logo on dark, and a
small-size strip (64/32/16 px) to check legibility at favicon scale.

Usage:
  python proof_sheet.py concept-a.svg concept-b.svg concept-c.svg -o concepts.png
  python proof_sheet.py logo.svg --labels "Final" --dark "#0E1116" -o proof.png
  python proof_sheet.py mark.svg --no-small -o review.png

Look at the result with your image-viewing tool before showing anyone. The
small strip is the quickest way to catch a mark that falls apart when tiny.
"""
import argparse, io, os, re, subprocess
from PIL import Image, ImageDraw, ImageFont


def render(svg_path, width=None, height=None, recolor=None):
    data = open(svg_path, "rb").read()
    if recolor:
        # crude reverse: swap every explicit fill/stroke colour except 'none' for recolor
        txt = data.decode()
        txt = re.sub(r'(fill|stroke)="(?!none)(#[0-9a-fA-F]{3,8}|[a-z]+)"', lambda m: f'{m.group(1)}="{recolor}"', txt)
        txt = re.sub(r'(fill|stroke):\s*(?!none)(#[0-9a-fA-F]{3,8})', lambda m: f'{m.group(1)}:{recolor}', txt)
        data = txt.encode()
    cmd = ["rsvg-convert", "-f", "png", "-a"]
    if width:
        cmd += ["-w", str(width)]
    if height:
        cmd += ["-h", str(height)]
    png = subprocess.run(cmd, input=data, capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(png)).convert("RGBA")


def fit(img, box_w, box_h):
    img = img.copy()
    img.thumbnail((box_w, box_h), Image.LANCZOS)
    return img


def font(size):
    for p in ["/usr/share/fonts/opentype/inter/Inter-Medium.otf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svgs", nargs="+")
    ap.add_argument("-o", "--out", default="proof.png")
    ap.add_argument("--labels", nargs="*")
    ap.add_argument("--light", default="#FFFFFF")
    ap.add_argument("--dark", default="#111317")
    ap.add_argument("--reverse-color", default="#FFFFFF",
                    help="recolour the logo to this on the dark panel; pass 'none' to show it as-is (for marks already designed for dark)")
    ap.add_argument("--no-small", action="store_true")
    a = ap.parse_args()
    if a.reverse_color and a.reverse_color.lower() == "none":
        a.reverse_color = None

    cell_w, cell_h, pad = 520, 300, 28
    small_h = 0 if a.no_small else 96
    label_h = 44
    row_h = label_h + cell_h + small_h + pad
    W = pad + 2 * (cell_w + pad)
    H = pad + row_h * len(a.svgs)
    sheet = Image.new("RGB", (W, H), "#ECEDEF")
    d = ImageDraw.Draw(sheet)
    f_label, f_small = font(22), font(14)

    for i, path in enumerate(a.svgs):
        y = pad + i * row_h
        label = (a.labels[i] if a.labels and i < len(a.labels) else os.path.splitext(os.path.basename(path))[0])
        d.text((pad, y + 8), label, fill="#222", font=f_label)
        y += label_h
        big = render(path, width=900)
        for j, (bg, recolor) in enumerate([(a.light, None), (a.dark, a.reverse_color)]):
            x = pad + j * (cell_w + pad)
            panel = Image.new("RGB", (cell_w, cell_h), bg)
            img = fit(render(path, width=900, recolor=recolor) if recolor else big, cell_w - 80, cell_h - 80)
            panel.paste(img, ((cell_w - img.width) // 2, (cell_h - img.height) // 2), img)
            sheet.paste(panel, (x, y))
        if not a.no_small:
            sy = y + cell_h + 12
            x = pad
            for px in (64, 32, 16):
                im = render(path, height=px)
                tile = Image.new("RGB", (max(im.width, px) + 16, px + 16), a.light)
                tile.paste(im, (8, 8), im)
                sheet.paste(tile, (x, sy))
                d.text((x, sy + px + 18), f"{px}px", fill="#555", font=f_small)
                x += tile.width + 24
    sheet.save(a.out)
    print(a.out)


if __name__ == "__main__":
    main()
