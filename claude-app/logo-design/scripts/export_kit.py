#!/usr/bin/env python3
"""Build a ready-to-hand-over logo kit from master SVG files.

Name the masters by role inside one folder (any subset works):
  icon.svg        the symbol / app-icon mark on its own (square-ish)
  primary.svg     the main lockup
  horizontal.svg  icon + wordmark side by side
  stacked.svg     icon above wordmark
  wordmark.svg    name only
  app-icon.svg    optional: full-bleed square for app/touch/avatar icons (use when the
                  mark is itself a tile, or the icon needs its own background). Platforms
                  round the corners themselves, so draw it square with no corner radius.

Usage:
  python export_kit.py masters/ --name northwind --out northwind-logo-kit \
      --brand "#0F4C81" --bg "#FFFFFF" --dark "#0B1220"

Produces:
  svg/        colour, black and white versions of every master
  png/        colour/black/white at 512, 1024, 2048 px wide (transparent)
  favicon/    favicon.ico (16/32/48), favicon.svg, apple-touch-icon.png (180),
              icon-192.png, icon-512.png, maskable-512.png, site.webmanifest snippet
  social/     og-image.png (1200x630), avatar-400.png (square profile picture)
  <name>-logo-kit.zip
The black/white versions are made by recolouring every fill and stroke, which
is right for single-colour marks; if a multi-colour mark depends on overlaps or
cut-outs, check the mono files in the proof sheet and hand-make them if needed.
"""
import argparse, io, json, os, re, shutil, subprocess, zipfile
from PIL import Image

ROLES = ["icon", "primary", "horizontal", "stacked", "wordmark"]  # app-icon.svg handled separately


def recolor(svg, color):
    svg = re.sub(r'(fill|stroke)="(?!none)(?!url)[^"]*"', lambda m: f'{m.group(1)}="{color}"', svg)
    svg = re.sub(r'(fill|stroke)\s*:\s*(?!none)(?!url)[^;"]+', lambda m: f'{m.group(1)}:{color}', svg)
    svg = re.sub(r'stop-color="[^"]*"', f'stop-color="{color}"', svg)
    return svg


def png(svg_text, width=None, height=None):
    cmd = ["rsvg-convert", "-f", "png", "-a"]
    if width:
        cmd += ["-w", str(width)]
    if height:
        cmd += ["-h", str(height)]
    out = subprocess.run(cmd, input=svg_text.encode(), capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(out)).convert("RGBA")


def on_canvas(mark, size, bg, scale):
    """Place a mark centred on a square canvas, mark occupying `scale` of it."""
    canvas = Image.new("RGBA", size, bg)
    m = mark.copy()
    m.thumbnail((int(size[0] * scale), int(size[1] * scale)), Image.LANCZOS)
    canvas.paste(m, ((size[0] - m.width) // 2, (size[1] - m.height) // 2), m)
    return canvas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("masters")
    ap.add_argument("--name", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--bg", default="#FFFFFF", help="background for app/touch icons")
    ap.add_argument("--dark", default="#111317", help="background for the dark social/avatar variant")
    ap.add_argument("--brand", default=None, help="brand colour (used for maskable icon background if --icon-on-brand)")
    ap.add_argument("--icon-on-brand", action="store_true", help="put a white icon on the brand colour for app icons")
    a = ap.parse_args()

    out = a.out or f"{a.name}-logo-kit"
    shutil.rmtree(out, ignore_errors=True)
    for sub in ("svg", "png", "favicon", "social"):
        os.makedirs(os.path.join(out, sub), exist_ok=True)

    masters = {r: open(os.path.join(a.masters, f"{r}.svg")).read()
               for r in ROLES if os.path.exists(os.path.join(a.masters, f"{r}.svg"))}
    if not masters:
        raise SystemExit("no master SVGs found (expected icon.svg, primary.svg, ...)")

    made = []
    for role, svg in masters.items():
        for variant, text in (("color", svg), ("black", recolor(svg, "#000000")), ("white", recolor(svg, "#FFFFFF"))):
            base = f"{a.name}-{role}-{variant}"
            p = os.path.join(out, "svg", base + ".svg")
            open(p, "w").write(text)
            made.append(p)
            for w in (512, 1024, 2048):
                pp = os.path.join(out, "png", f"{base}-{w}.png")
                png(text, width=w).save(pp)
                made.append(pp)

    icon_role = "icon" if "icon" in masters else next(iter(masters))
    icon_svg = masters[icon_role]
    if a.icon_on_brand and a.brand:
        icon_svg_app, app_bg = recolor(icon_svg, "#FFFFFF"), a.brand
    else:
        icon_svg_app, app_bg = icon_svg, a.bg
    big = png(icon_svg_app, width=1024)
    app_path = os.path.join(a.masters, "app-icon.svg")
    full_bleed = png(open(app_path).read(), width=1024) if os.path.exists(app_path) else None

    def app_icon(size, scale):
        if full_bleed is not None:
            return full_bleed.resize(size, Image.LANCZOS)
        return on_canvas(big, size, app_bg, scale)

    fav = os.path.join(out, "favicon")
    # favicon: transparent, mark fills ~90% so it stays readable at 16px
    fav_src = png(icon_svg, width=512)
    ico = on_canvas(fav_src, (256, 256), (0, 0, 0, 0), 0.92)
    ico.save(os.path.join(fav, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    shutil.copy(os.path.join(a.masters, f"{icon_role}.svg"), os.path.join(fav, "favicon.svg"))
    app_icon((180, 180), 0.72).convert("RGB").save(os.path.join(fav, "apple-touch-icon.png"))
    app_icon((192, 192), 0.72).save(os.path.join(fav, "icon-192.png"))
    app_icon((512, 512), 0.72).save(os.path.join(fav, "icon-512.png"))
    app_icon((1024, 1024), 0.72).convert("RGB").save(os.path.join(fav, "app-store-1024.png"))
    # maskable: safe zone is the central 80% circle, so keep the mark within ~56%.
    # A full-bleed app icon is assumed to have been drawn with that safe zone in mind.
    app_icon((512, 512), 0.56).save(os.path.join(fav, "maskable-512.png"))
    manifest = {"icons": [
        {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    open(os.path.join(fav, "site.webmanifest"), "w").write(json.dumps(manifest, indent=2))
    open(os.path.join(fav, "head-snippet.html"), "w").write(
        '<link rel="icon" href="/favicon.ico" sizes="any">\n'
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
        '<link rel="manifest" href="/site.webmanifest">\n')

    soc = os.path.join(out, "social")
    lock_role = next((r for r in ("horizontal", "primary", "stacked", "wordmark") if r in masters), icon_role)
    lock = png(masters[lock_role], width=1600)
    on_canvas(lock, (1200, 630), a.bg, 0.6).convert("RGB").save(os.path.join(soc, "og-image.png"))
    app_icon((400, 400), 0.62).convert("RGB").save(os.path.join(soc, "avatar-400.png"))
    white_lock = png(recolor(masters[lock_role], "#FFFFFF"), width=1600)
    on_canvas(white_lock, (1200, 630), a.dark, 0.6).convert("RGB").save(os.path.join(soc, "og-image-dark.png"))

    zpath = f"{out}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(out):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, os.path.dirname(out) or "."))
    count = sum(len(f) for _, _, f in os.walk(out))
    print(json.dumps({"kit": out, "zip": zpath, "files": count, "roles": list(masters)}))


if __name__ == "__main__":
    main()
