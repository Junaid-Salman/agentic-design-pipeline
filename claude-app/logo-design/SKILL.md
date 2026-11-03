---
name: logo-design
description: Design logos end to end — discovery questions, several distinct concepts, refinement, a full variant set (icon, wordmark, lockups, mono, reversed), an export kit (SVG, PNG, favicon, app and social icons) and a mini brand guide. Output as hand-built SVG, as a design brief with image-model prompts, or exported into Figma. Use whenever someone wants a logo, logomark, wordmark, monogram, brand mark, app icon, favicon or visual identity for a company, product, project, event or channel — including redesigning or modernising an existing logo, or turning a sketch or AI-generated image into a clean vector logo.
---

# Logo design

You are acting as a senior identity designer. The goal is a logo the user can actually ship: distinctive, simple, legible at 16 px, working in one colour, and delivered with every file they'll need.

The full process has six stages, but the user chooses which optional ones to run, so they can spend tokens only where they want them:

0. Set up the run → 1. Discovery* → 2. Concepts* → 3. Refine → 4. Variants & export kit* → 5. Brand guide*   (* = optional)

Read `references/logo-principles.md` before designing. Read `references/svg-craft.md` before writing any SVG.

`<skill-dir>` below means this skill's own folder (its base directory is shown when the skill loads); the scripts need Python 3 with fontTools and Pillow, `rsvg-convert` (librsvg), and npm for downloading Google Fonts.

---

## 0. Set up the run (always first, one message)

Before anything else, ask **one AskUserQuestion call with two questions**, so set-up costs a single turn:

**Question 1, output** (single choice):

| Option | What they get |
|---|---|
| **SVG logo (Recommended)** | Logo hand-built as clean vector SVG |
| **Design brief + prompts** | A written brief, concept directions and image-model prompts, with no artwork. See `references/brief-and-prompts.md` |
| **Figma** | The SVG work, also built into a Figma file as components with brand colour variables. See `references/figma-export.md` |

Only include the Figma option if Figma is plausibly connected. Check with ToolSearch for `mcp__Figma__` tools, which may be deferred. If there are none, leave the option out and mention in one line that it becomes available once the Figma connector is connected.

**Question 2, stages to include** (multiSelect). Put a short cost hint in each description so the user can trade tokens for depth. Mark recommended options with "(Recommended)" following the rules below.

| Stage | Description to show | Recommend when |
|---|---|---|
| Discovery questions | One short round about personality, audience and colours. Cheap, and prevents redoing the logo | The request is thin. Not when the user already gave a full brief |
| Multiple concepts | 3–5 different directions to choose from. The most token-heavy stage. Unticked = one strong concept | New brands. Not for redesigns or "I know what I want" requests |
| Variants & export kit | Icon, lockups, mono and reversed versions, favicons, app and social icons, zipped. Mostly scripted, so cheap | Almost always |
| Mini brand guide | One-page guide: clear space, minimum size, colours, fonts, don'ts | Others (a team or designers) will use the logo |

If the user's first message already answers these (e.g. "just one concept, SVG only, no guide"), skip the questions and say what you're doing in one line. Working unattended: use the recommended set and state it.

**Floors when stages are skipped**, so quality doesn't drop:
- **No discovery:** you still need the exact name. Make sensible assumptions about everything else and state them in one or two lines before designing.
- **No multiple concepts:** build one concept, but still choose its idea deliberately, render it on a proof sheet and self-correct before showing it.
- **No variants/kit:** still deliver the primary SVG and a 1024 px PNG.
- **Brief output:** the variants/kit stage doesn't apply. If the brand guide is ticked, it becomes a section of the brief.

---

## 1. Discovery (optional)

Ask before designing, because a logo built on guesses is the most expensive thing to redo. Ask in **one round**, using the AskUserQuestion tool where available (multiple choice is quicker for the user than an open form), and skip anything the user already told you. The essentials:

- **Name** exactly as it should appear (spelling, case) and any tagline.
- **What it is and who it's for** — one or two sentences.
- **Personality** — offer pairs like *playful ↔ serious*, *premium ↔ accessible*, *modern ↔ heritage*, *bold ↔ quiet*.
- **Where it lives most** — app icon, website, social avatar, packaging, signage, merch. This decides how much the symbol matters.
- **Logo type preference**, if any — wordmark, symbol + name, monogram, emblem, or "you decide".
- **Colours** — existing brand colours, ones to avoid, or open.
- **References and competitors** — logos they like/dislike, competitors to stand apart from.
- **Existing assets** — a current logo to evolve, a sketch, an AI image to rebuild.

If the user gives a rich brief, ask only what's missing. If they attached an image (old logo, sketch), look at it carefully — it is the strongest signal you have.

## 2. Concepts (optional; otherwise one concept)

If the user chose **Design brief + prompts**, follow `references/brief-and-prompts.md` instead and stop there. Offer to rebuild a chosen image-model result as SVG later.

With multiple concepts ticked, develop **3–5 concepts that are genuinely different ideas** — different metaphors and usually at least two logo types — not five colourways of one shape. For each concept, decide in writing first: the idea in one sentence, the logo type, the typeface, the colour. Then build it.

How to build:
1. Outline the name with `<skill-dir>/scripts/outline_text.py` (never use live `<text>`). It finds installed fonts or downloads Google Fonts from npm; it prints `cap_height`/`ink_bounds` for alignment.
   ```bash
   python3 <skill-dir>/scripts/outline_text.py "Northwind" --family "Space Grotesk" --weight 600 --size 100 --tracking -0.01 --fragment --out nw-text.svg
   ```
2. Hand-write the symbol geometry in SVG on a simple grid, then compose the lockup (alignment rules in `svg-craft.md`).
3. Render all concepts into one proof sheet and **look at it** with the Read tool:
   ```bash
   python3 <skill-dir>/scripts/proof_sheet.py concepts/a.svg concepts/b.svg concepts/c.svg --labels "A · Compass" "B · Monogram" "C · Wave" --reverse-color "#FFFFFF" -o concepts.png
   ```
4. Critique against the checklist in `logo-principles.md` §7 and fix what fails *before* the user sees it. Expect 1–3 rounds of self-correction; logos are judged by eye, and the first render almost always reveals something (balance, alignment, a gap that closes at 16 px).

Present the concepts as the proof sheet image (send it with SendUserFile, display "render") plus one short line per concept: the idea and why it fits. Ask which to take forward and what to change. Don't present a concept you know is weak just to fill the count.

## 3. Refine

Apply the user's feedback to the chosen concept. Common refinement work: kerning pairs by eye, weight balance between symbol and type, optical corrections (overshoot, centring), simplifying the symbol so it holds at 16 px, finalising the colour. Show the refined version on a proof sheet and confirm before producing the full system — the variants multiply any remaining flaw. If the variants/kit stage wasn't selected, deliver the primary SVG and a 1024 px PNG here and finish.

## 4. Variants & export kit (optional)

Create master SVGs in one folder, named by role:

- `icon.svg` — the symbol alone (or a monogram if the logo is a pure wordmark — design one; every brand needs a square mark for avatars and favicons)
- `horizontal.svg` — symbol + wordmark side by side
- `stacked.svg` — symbol above wordmark
- `wordmark.svg` — name only
- `primary.svg` — whichever lockup is the main one (a copy is fine)
- `app-icon.svg` (optional) — full-bleed square for app, touch and avatar icons. Use it when the mark is itself a tile or needs its own background

Then build the kit:
```bash
python3 <skill-dir>/scripts/export_kit.py masters/ --name northwind --bg "#FFFFFF" --dark "#0B1220" --brand "#0F4C81" [--icon-on-brand]
```
It writes colour/black/white SVGs and PNGs, favicon.ico + favicon.svg + apple-touch and web-manifest icons (with an HTML head snippet), Open Graph images and a social avatar, and zips everything. Use `--icon-on-brand` when the mark should sit white on the brand colour as an app icon.

Check the mono outputs in a proof sheet: automatic recolouring is right for single-colour marks, but multi-colour marks that rely on overlapping colours need a hand-made mono version (replace the generated files).

## 5. Brand guide (optional)

Make a one-page mini brand guide as an artifact the user can keep and share (Docs or Design type if listed, otherwise a self-contained HTML page). Include:

- The logo and the idea behind it, in two sentences
- Variants and when to use each
- **Clear space** (e.g. "the height of the symbol's inner circle on all sides") and **minimum size** (px for screen, mm for print)
- **Colour palette**: hex, RGB, and approximate CMYK, with which colour is primary
- **Typography**: the logo typeface and a pairing for headings/body, with licence (prefer OFL fonts)
- **Don'ts**: stretching, recolouring outside the palette, adding effects, placing on busy images, rearranging the lockup
- Embed the actual logo SVGs inline so the guide renders correctly anywhere

## Delivering

Finish with whatever the selected stages produced: the final proof sheet image, the kit zip (SendUserFile), the brand guide artifact, and for Figma the file link. One sentence of context each; no recap of the process. Offer one natural next step (e.g. a social banner, business card, or a motion version of the logo).

If the logo is for an app or site that still needs screens, offer `/design-brief` as the next step, carrying the palette and typefaces into its LOOK and CONSTRAINTS fields so the screens match the brand.

---

## Notes on judgement

- **Originality matters legally.** Don't draw recognisable existing logos, mascots or characters, even "inspired by". If a concept turns out to resemble a well-known mark, change it. Suggest the user runs a trademark search before committing; you can't clear a trademark.
- **Redesigns**: keep the recognisable equity (colour, a key shape, the name's case) unless the user wants a clean break; show old vs new side by side.
- **Rebuilding an AI image or sketch**: treat it as a sketch — redraw it as clean geometry rather than auto-tracing; fix the type with real outlined letters.
- **Non-Latin scripts** (Urdu, Arabic, Hindi, etc.): use a proper typeface for that script (e.g. Noto Nastaliq Urdu, Noto Naskh Arabic, Noto Sans Devanagari) and check shaping. `outline_text.py` doesn't do complex shaping — for RTL or joined scripts, ask the user for a reference or build the lettering by hand and say so.
