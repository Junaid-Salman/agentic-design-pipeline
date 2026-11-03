#!/usr/bin/env python3
"""Convert text into SVG outline paths so a logo never depends on an installed font.

Usage:
  python outline_text.py "Northwind" --family "Space Grotesk" --weight 600 \
      --size 96 --tracking 0.02 --out wordmark.svg
  python outline_text.py "acme" --font /path/to/Font.ttf --size 120 --fragment

Font resolution order:
  1. --font PATH (ttf / otf / woff)
  2. a locally installed family (fc-match)
  3. the Google font from npm (@fontsource/<family>) — needs network access to npm

Output: a standalone SVG (default) or, with --fragment, just a <g> you can paste
into a larger logo file. The path is placed with its baseline at y=size and its
left edge at x=0; the printed JSON gives width/ascent/descent for layout math.
"""
import argparse, json, os, re, subprocess, sys, tarfile, tempfile, glob

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

CACHE = os.path.expanduser("~/.cache/logo-design-fonts")


def slug(family):
    return re.sub(r"[^a-z0-9]+", "-", family.lower()).strip("-")


def from_fc(family, weight, italic):
    try:
        out = subprocess.run(["fc-match", "-f", "%{file}|%{family}|%{weight}", f"{family}:{'italic' if italic else 'roman'}"],
                             capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return None
    path, fam, _ = (out.split("|") + ["", "", ""])[:3]
    if family.lower() not in fam.lower():
        return None
    # Prefer an exact weight file in the same directory.
    wanted = {100: "Thin", 200: "ExtraLight", 300: "Light", 400: "Regular", 500: "Medium",
              600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}.get(weight, "Regular")
    d = os.path.dirname(path)
    for cand in glob.glob(os.path.join(d, "*")):
        name = os.path.basename(cand).replace(" ", "")
        if family.replace(" ", "").lower() in name.lower() and f"-{wanted}{'Italic' if italic else ''}." in name:
            return cand
    # Exact weight not installed locally: let the npm fallback fetch the right one.
    return None


def from_npm(family, weight, italic):
    s = slug(family)
    dest = os.path.join(CACHE, s)
    if not os.path.isdir(dest):
        os.makedirs(CACHE, exist_ok=True)
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(["npm", "pack", f"@fontsource/{s}", "--silent"], cwd=tmp,
                               capture_output=True, text=True, timeout=120)
            tgz = [f for f in os.listdir(tmp) if f.endswith(".tgz")]
            if r.returncode != 0 or not tgz:
                return None
            with tarfile.open(os.path.join(tmp, tgz[0])) as t:
                t.extractall(dest, filter="data")
    style = "italic" if italic else "normal"
    files = glob.glob(os.path.join(dest, "package", "files", f"{s}-latin-{weight}-{style}.woff"))
    if not files:
        files = sorted(glob.glob(os.path.join(dest, "package", "files", f"{s}-latin-*-{style}.woff")))
        if not files:
            return None
        print(f"warning: weight {weight} not found, using {os.path.basename(files[0])}", file=sys.stderr)
    return files[0]


def resolve(args):
    if args.font:
        return args.font
    return from_fc(args.family, args.weight, args.italic) or from_npm(args.family, args.weight, args.italic)


def outline(font_path, text, size, tracking, word_space=0.0, kerning=True):
    font = TTFont(font_path)
    upm = font["head"].unitsPerEm
    scale = size / upm
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    kern = {}
    if kerning and "kern" in font:
        for table in font["kern"].kernTables:
            kern.update(getattr(table, "kernTable", {}))
    pen = SVGPathPen(gs)
    bpen = BoundsPen(gs)
    x = 0.0
    prev = None
    names = []
    for ch in text:
        g = cmap.get(ord(ch))
        if g is None:
            raise SystemExit(f"glyph for {ch!r} missing in {font_path}")
        if prev and (prev, g) in kern:
            x += kern[(prev, g)]
        t = (scale, 0, 0, -scale, x * scale, size)  # flip y, baseline at y=size
        gs[g].draw(TransformPen(pen, t))
        gs[g].draw(TransformPen(bpen, t))
        x += hmtx[g][0] + tracking * upm + (word_space * upm if ch == ' ' else 0)
        prev = g
        names.append(g)
    width = (x - tracking * upm) * scale
    os2 = font["OS/2"]
    meta = {
        "font": os.path.basename(font_path),
        "advance_width": round(width, 2),
        "ink_bounds": [round(v, 2) for v in (bpen.bounds or (0, 0, 0, 0))],
        "cap_height": round(getattr(os2, "sCapHeight", 0) * scale, 2),
        "x_height": round(getattr(os2, "sxHeight", 0) * scale, 2),
        "baseline_y": size,
        "note": "GPOS kerning is not applied; check pairs like AV/To/LT by eye and nudge with --tracking or manual transforms.",
    }
    return pen.getCommands(), meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text")
    ap.add_argument("--family", default="Inter")
    ap.add_argument("--weight", type=int, default=600)
    ap.add_argument("--italic", action="store_true")
    ap.add_argument("--font", help="explicit font file path")
    ap.add_argument("--size", type=float, default=100, help="font size in SVG units")
    ap.add_argument("--tracking", type=float, default=0.0, help="letter spacing in em (0.02 = +2%%)")
    ap.add_argument("--word-space", type=float, default=0.0,
                    help="extra space added at each space character, in em; negative tracking also squeezes word gaps, so +0.05 to +0.15 often helps")
    ap.add_argument("--fill", default="#111111")
    ap.add_argument("--fragment", action="store_true", help="emit only a <g> element")
    ap.add_argument("--out")
    args = ap.parse_args()

    path = resolve(args)
    if not path:
        raise SystemExit(f"could not find font '{args.family}' locally or on npm; pass --font")
    d, meta = outline(path, args.text, args.size, args.tracking, args.word_space)
    g = f'<g id="wordmark" fill="{args.fill}"><path d="{d}"/></g>'
    if args.fragment:
        svg = g
    else:
        x0, y0, x1, y1 = meta["ink_bounds"]
        pad = args.size * 0.1
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0 - pad:.2f} {y0 - pad:.2f} '
               f'{x1 - x0 + 2 * pad:.2f} {y1 - y0 + 2 * pad:.2f}">{g}</svg>')
    if args.out:
        with open(args.out, "w") as f:
            f.write(svg + "\n")
    else:
        print(svg)
    print(json.dumps(meta), file=sys.stderr)


if __name__ == "__main__":
    main()
