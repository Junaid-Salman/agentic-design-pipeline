# Logo principles — what separates a real logo from clip art

Read this before sketching concepts. It is the judgement layer; `svg-craft.md` is the execution layer.

## Contents
1. What a logo has to do
2. Choosing a logo type
3. Finding the idea
4. Form and construction
5. Typography
6. Colour
7. Self-critique checklist
8. Clichés to avoid (and when they're fine)

---

## 1. What a logo has to do

A logo is a signature, not an illustration. It identifies; it rarely explains. The tests that matter, roughly in order:

- **Distinctive** — could it be confused with a competitor or a stock icon? A blank-slate swoosh, globe or lightbulb fails this.
- **Simple** — can someone sketch it from memory after seeing it twice? Count the distinct shapes; fewer than five is a good sign.
- **Scalable** — it must survive at 16 px (favicon) and on a building. Hairlines, tiny gaps and fine detail die first.
- **Works in one colour** — if it needs a gradient or three colours to make sense, it isn't finished. Colour is added after the shape works in black.
- **Appropriate** — the personality matches the business. A law firm and a kids' snack brand can share a principle (simplicity) but not a temperament.
- **Durable** — avoids this year's trend tics (heavy gradients, glassmorphism, ultra-thin geometric line icons) unless the brand is deliberately of-the-moment.

## 2. Choosing a logo type

| Type | When it fits | Watch out |
|---|---|---|
| **Wordmark** (name in custom-ish type) | New brands that need name recognition; short or distinctive names (≤ ~10 letters) | Needs a typographic detail of its own or it's "just a font" |
| **Lettermark / monogram** | Long names, initials already used (IBM, HBO); app icons | Two- and three-letter monograms are crowded territory — need a real twist |
| **Symbol / pictorial mark** | Brands that will live as icons (apps, social avatars); concrete, ownable metaphor | Literal pictures (a tooth for a dentist) are generic; abstract the idea |
| **Abstract mark** | Broad or evolving offerings; tech, finance | Means nothing on day one — must be paired with the name for a long time |
| **Combination mark** | The default for most small businesses and products: symbol + wordmark | Design both halves to share geometry, weight and rhythm |
| **Emblem** (name inside a shape) | Heritage, crafts, food & drink, clubs, schools | Poor at small sizes; always design a simplified secondary mark |
| **Mascot** | Consumer and community brands with a playful voice | Hard to execute well in SVG; costly to keep consistent |

For most requests, explore at least two types across the concept set rather than five variations of one type.

## 3. Finding the idea

Good marks usually come from one specific, ownable idea, not a list of attributes. Ways in:

- **Name mining** — literal meaning, etymology, sounds, letter shapes (a negative-space arrow in a letter, a letter that doubles as an object).
- **What the business actually does** — the verb, not the noun. "Moves money quickly" gives you more than "bank".
- **Origin and place** — local landmarks, materials, patterns, scripts (e.g. motifs from Urdu calligraphy, Sindhi ajrak, Japanese mon), used with respect and not as costume.
- **The customer's outcome** — what changes for them.
- **A visual pun or dual reading** — two ideas in one shape (FedEx arrow, Toblerone bear). Powerful when it's discoverable but not required to get the mark.

Generate 10–20 rough ideas in your head or as a written list, discard the obvious first three, and develop the strongest 3–5 so each one is a *different* idea, not a different rendering of the same idea.

## 4. Form and construction

- **Build on a grid.** Use simple geometry (circles, squares, consistent radii, 45°/30° angles) and reuse the same measurements. Consistency reads as quality even when people can't say why.
- **Optical corrections.** Geometric perfection looks wrong:
  - Circles and points must overshoot the baseline/cap line by ~1–3% to look the same height as flat shapes.
  - Horizontal strokes should be slightly thinner than vertical ones to look equal.
  - A shape centred mathematically in a circle often looks low; nudge it up a little.
  - Sharp internal corners fill in at small sizes ("ink traps" help on bold marks).
- **Positive and negative space.** Design the gaps as deliberately as the shapes. Gaps narrower than ~6% of the mark's height disappear at favicon size.
- **Weight.** Match the stroke weight of the symbol to the stem weight of the wordmark, or make a clear, intentional contrast.
- **Balance.** Visually heavy shapes (dark, large, bottom-placed) need counterweight. Check the mark mirrored or upside down — imbalance becomes obvious.

## 5. Typography

- Start from a typeface with the right temperament, then customise: tighten or open tracking, shorten an ascender, merge two letters, cut a terminal, swap one glyph for a symbol. One or two meaningful modifications beat many small ones.
- **Tracking:** all-caps wordmarks usually need +5% to +12% tracking; lowercase wordmarks usually look better slightly tightened (−1% to −3%).
- **Kerning:** check every pair by eye. Problem pairs: AV, AW, LT, To, Ty, rn, ry, f-anything. The outline script doesn't apply advanced kerning — fix pairs manually.
- **Case** carries tone: lowercase = friendly/approachable, all caps = authoritative/stable, title case = neutral.
- **Licensing:** prefer typefaces under the SIL Open Font License (most Google Fonts) so the user can use the outlined logo commercially. Name the font in the brand guide.

Temperament shortcuts (Google Fonts, all OFL):
- Neutral/modern tech: Inter, Manrope, Plus Jakarta Sans, Geist
- Geometric/friendly: Poppins, Outfit, Urbanist, Sora
- Characterful grotesk: Space Grotesk, Bricolage Grotesque, Familjen Grotesk
- Editorial/premium serif: Fraunces, Playfair Display, DM Serif Display, Lora
- Technical/mono: JetBrains Mono, IBM Plex Mono, Space Mono
- Rounded/soft: Nunito, Quicksand, M PLUS Rounded 1c
- Condensed/bold: Oswald, Anton, Barlow Condensed

## 6. Colour

- Pick **one primary brand colour** that carries the mark, plus at most one accent. Name colours with hex, RGB and, if print matters, an approximate CMYK.
- Check contrast: the mark against white and against the brand's dark background should be at least 3:1 (WCAG non-text contrast).
- Colour meanings are cultural and loose; choose for differentiation from competitors first, association second.
- Design the reversed (white-on-colour/dark) version deliberately — some marks need a weight or shape tweak when reversed.
- Avoid pure #000000 for the "black" brand colour in screen use; a near-black (e.g. #111317) looks richer. Keep pure black for the mono print file.

## 7. Self-critique checklist

Before showing concepts, look at the proof sheet and answer honestly:

- [ ] Does each concept express a *different* idea?
- [ ] Is it legible and recognisable at 16 px and 32 px?
- [ ] Does it work in solid black on white and white on black?
- [ ] Is anything off-centre, unevenly weighted or accidentally tangent (shapes just touching)?
- [ ] Are there accidental readings (unfortunate letters, shapes, symbols — check in other scripts and languages relevant to the audience)?
- [ ] Is it too close to a famous logo or a known trademark? If it resembles one, change it — don't just mention it.
- [ ] Would the user be able to explain the idea in one sentence?

## 8. Clichés to avoid (and when they're fine)

Overused unless given a genuinely new twist: generic swooshes, globes, lightbulbs for "ideas", speech bubbles for "chat", gears for "engineering", shields for "security", leaves for "eco", brain/circuit hybrids for "AI", sparkles/four-point stars for "AI", interlocking rings, house-roof-over-text for real estate, the "abstract people holding hands".

They're fine when the user explicitly wants a familiar category signal (e.g. a clinic that must read as medical at a glance) — then make the execution distinctive.
