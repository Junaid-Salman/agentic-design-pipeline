# SVG craft — building logos that are clean, editable and production-ready

## File rules

- **One logo per file**, with a tight `viewBox` around the artwork plus a small, consistent margin. No `width`/`height` attributes on the root (lets the logo scale), or set them equal to the viewBox if a tool needs them.
- **No live text.** `<text>` depends on fonts the viewer may not have. Always outline type with `scripts/outline_text.py` and paste the resulting `<path>` in.
- **No raster images, filters, masks-for-effects or `<foreignObject>`.** Masks and clip-paths are acceptable only for real cut-outs, and even then prefer a single compound path (`fill-rule="evenodd"`) because Figma, Illustrator and favicon generators all handle plain paths best.
- **Flat colour.** Use `fill="#RRGGBB"` attributes, not CSS classes or `<style>` blocks (they get stripped or ignored by some tools, and the recolouring scripts look for attributes). Gradients only if the concept truly depends on them, and always ship a flat version.
- **Strokes vs fills.** Strokes are fine while designing, but outline them before the final master if the mark will be scaled non-uniformly or imported into tools — or keep `vector-effect` out entirely and keep strokes uniform-scaled only. In practice: final masters should be fills.
- **Precision.** Round coordinates to 1–2 decimals. Work on a sensible grid (e.g. a 100 or 240 unit square for icons) so measurements are reusable.
- **IDs and groups.** Group logically (`<g id="symbol">`, `<g id="wordmark">`) so the Figma import and later edits stay clean.

## Building geometry well

- Prefer primitives (`circle`, `rect` with `rx`, `polygon`) while exploring; convert to paths only when combining.
- For arcs: `A rx ry rotation large-arc sweep x y`. Draw a quick helper circle first, then trace with arcs on it so curves stay concentric.
- Consistent corner radii: pick one or two radius values and use them everywhere.
- Negative space: build the outer shape, then subtract with a second subpath in the same `<path>` using `fill-rule="evenodd"`, rather than painting a white shape on top. Painted-white "cut-outs" break on coloured backgrounds **and** vanish in every one-colour version: when the mark is recoloured white for a dark background, a white sun on a blue tile becomes a blank white tile. This matters most for badge/app-tile marks (a symbol inside a rounded square or circle) — the inner symbol must be a hole in the container, not a shape on top of it. The reversed panel of the proof sheet is the test for this.
- Overshoot: make round elements ~2% taller than flat ones of the "same" height.

## Composing lockups

Use the numbers printed by `outline_text.py` (`cap_height`, `x_height`, `ink_bounds`) for alignment:

- Size by **ink**, not by the drawing grid: if the symbol only fills 70% of its 100-unit grid, scaling the grid to 1.4× cap height leaves the visible mark too small. Measure the symbol's real bounds.
- **Word spacing:** negative tracking also tightens the space between words, so a two-word name can read as one at small sizes. Use `--word-space 0.08`–`0.15` with tightened tracking, and check the 16–32 px strip.
- **Horizontal lockup:** symbol height ≈ 1.2–1.6× the wordmark cap height; centre the symbol on the cap-height middle (not on the full text box). Gap between symbol and text ≈ 0.5–0.8× cap height.
- **Stacked lockup:** symbol width ≈ 0.4–0.6× wordmark width; gap ≈ 0.4–0.6× cap height.
- Place text with `<g transform="translate(x,y)">` around the outlined path; the path's baseline sits at `y = size`.

Example skeleton:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 160">
  <g id="symbol" fill="#0F4C81">
    <path d="..." fill-rule="evenodd"/>
  </g>
  <g id="wordmark" fill="#111317" transform="translate(176 22)">
    <path d="...outlined text..."/>
  </g>
</svg>
```

## Checking your work

- Render every concept with `scripts/proof_sheet.py` and **look at the PNG** (open it with the Read tool). You cannot judge a logo from its source code. Common problems only visible in the render: lopsided balance, gaps closing at 16 px, text baseline misaligned with the symbol, colours vibrating.
- Validate XML quickly: `rsvg-convert file.svg > /dev/null` fails loudly on broken markup.
- Iterate: it is normal to adjust a concept 2–3 times after seeing it before showing it.
