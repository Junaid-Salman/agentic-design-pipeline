# Design brief + generation prompts output

Use this when the user wants strategy and direction rather than finished artwork — to hand to a human designer or to feed an image model (Midjourney, Ideogram, Recraft, GPT-image, Figma's generate_image, etc.).

Save it as `design/logo/brief.md` so it can be shared, edited and versioned with the project. Keep it tight: a designer should be able to read it in five minutes.

## Brief structure

1. **Brand snapshot** — name, one-line description, audience, where the logo will mostly live (app icon, website, packaging, signage, social).
2. **Personality** — 3–5 adjectives *and* their opposites ("confident, not loud"). Opposites stop designers drifting.
3. **Positioning** — 2–3 competitors and what their logos look like; the gap this brand should occupy.
4. **Must-haves and must-avoids** — required elements, colours to avoid, clichés to avoid, cultural or legal sensitivities.
5. **Concept directions** — 3–5 directions, each with: a name, the core idea in one sentence, logo type (wordmark, symbol, combination…), suggested typeface(s), colour direction, and why it fits. Include a rough description of the shape so a designer can sketch it.
6. **Deliverables expected** — the variant and export list from SKILL.md, so the designer quotes the full job.
7. **Evaluation criteria** — the checklist from `logo-principles.md` §7, phrased as questions to ask of each submission.

## Image-model prompts

Write one prompt per direction, plus 2 variations each. Logos come out of image models best when the prompt is specific about *form*, not adjectives. Pattern:

```
Flat vector logo, [logo type], for "[Brand]", [what the brand is in 5 words].
[Concrete description of the mark: shapes, how they combine, negative-space idea].
[Typography: style of letterforms, case, weight]. [Colour: 1–2 named colours with hex].
Centered on a plain white background, minimal, no gradients, no shadows, no mockup,
no extra text, crisp edges, simple enough to work at 16px.
```

Tips to include for the user:
- Image models often misspell names. Generate the symbol alone ("no text") and set the name in real type afterwards — this skill can then rebuild the chosen result as a clean SVG.
- Ask for "vector, flat, solid colours" every time; image models drift to 3D and gradients.
- Ideogram and Recraft handle text and vector style best; Recraft can export SVG directly.
- Anything an image model produces is a raster sketch. Offer to trace or redraw the chosen one as a real SVG master — that's where this skill's SVG output picks up.

## Figma image generation

If the Figma connector is available and the user wants images inside Figma, the `generate_image` tool can produce sketches from these prompts. Load the Figma skills first (see `figma-export.md`). Treat the results as concept sketches, not final logos.
