---
name: design-brief
description: Turn a short design request into a full design brief, ask only for missing details, then build it - HTML prototype, code in this project, Figma, or iOS screens. Use when the user types /design-brief or asks to design a screen, flow, page or app.
argument-hint: "<what to design, e.g. settings screen for my booking app>"
---

# /design-brief

Turn a one-line design request into a complete brief, confirm it, then build it with the right tool.

Request: $ARGUMENTS

## 1. Fill the brief from what is already known

Start from the request, this conversation, and the project itself. Before asking anything, look at:
- `README`, `CLAUDE.md`, `package.json` / `pubspec.yaml` / `*.xcodeproj` for product, stack and platform
- existing tokens or theme files (`tailwind.config.*`, `theme.*`, `tokens.*`, CSS variables, `Color+*.swift`)
- existing components folder, so new screens reuse them

Fill every field you can:

```
DESIGN: <what to make> for <web desktop / iOS / Android / responsive>
PRODUCT: <one line on what the app does>
USERS: <who, and the context they use it in>
JOB OF THIS SCREEN: <the one thing the user must get done here>
CONTENT: <real sample data: names, numbers, edge cases - never lorem ipsum>
SCREENS / STATES: <screens; plus empty, loading, error, success where they matter>
LOOK: <mood in concrete nouns from the subject's world, or "use the project's existing tokens">
CONSTRAINTS: <brand colors, fonts, framework, light/dark, WCAG AA>
OUTPUT: <HTML prototype | code in this project | Figma | iOS screens>
VARIATIONS: <one | 3 distinct directions>
```

## 2. Ask only for what is missing and matters

- Ask at most 4 questions in one round, multiple-choice where possible. Never ask for something the project or conversation already answers.
- Always required: PRODUCT, USERS, JOB, OUTPUT. If any is missing, ask.
- Use these defaults instead of asking:
  - Platform: responsive web (1440 + 390) unless the request or project says mobile.
  - Content: realistic sample data that fits the product, plus one awkward edge case (a long name, zero results).
  - States: empty and error for any screen that lists or submits data.
  - Look: the project's existing tokens if any; otherwise a direction drawn from the product's own world.
  - Constraints: WCAG AA, light and dark.
  - Variations: 3 directions for a first look at something new; 1 for a screen inside an existing system.
  - Output: code in this project if it has a UI stack; otherwise an HTML prototype.

## 3. Show the brief

Print the completed brief in a code block, and save it to `design/briefs/<slug>.md` so it can be reused. Then start building in the same turn. Wait for approval only when the output is expensive to redo (many screens, or changes across many files) and something in the brief is still a guess.

## 4. Build it

Plan before building: a palette of 4-6 named hex values (or the project's tokens), type families and their roles, a layout concept, and the one thing that makes this design specific to the product. Check the plan against generic defaults (cream background + serif + terracotta accent; black + neon accent; rows of identical rounded cards with soft grey shadows; ALL-CAPS eyebrow labels everywhere) and revise any part that would fit any product. If a `frontend-design` skill is available, follow it.

| OUTPUT / platform | Do this |
| --- | --- |
| HTML prototype | One self-contained file at `design/prototypes/<slug>.html`: inline CSS/JS, working navigation between screens, light/dark, responsive to 390px. For 3 directions, one file per direction. Open it in a browser if a browser tool is available and screenshot to check. |
| Code in this project | Build in the existing stack and folder conventions; reuse existing components and tokens; add new tokens to the token file rather than hard-coding values. |
| Figma | Requires the Figma MCP server. Get a file link (or create a file). Load the figma-use and figma-generate-design skills if installed; search the library and reuse components before drawing new ones. |
| iOS screens or flows | If the ios-flows / ios-screens skills are installed, use ios-flows to plan multi-step flows and ios-screens to build. Otherwise: 390x844 frames, 44pt targets, safe areas, Dynamic Type, tab bar + navigation stack, sheets for secondary tasks. |
| Android screens | Material 3 patterns, 360x800, top app bar, system back. |
| New mobile app, no design system yet | If a mobile-design-system skill is installed, run it first, then design screens on top of it. |

## 5. Check and close the loop

Before reporting done: verify contrast (4.5:1 text, 3:1 UI), visible focus, touch targets, and that every state in the brief exists.

Then give one line on what was made, with the file paths, and offer the next step that fits:
- First look done -> "Pick a direction and I'll turn it into tokens for the project."
- Screens done -> a design critique and accessibility pass, then apply the fixes.
- Ready to build -> a handoff spec, or implement directly.

## Rules

- Real content always; placeholder text produces templated designs.
- Name the states, not just the screens.
- If the user specified a look, follow their words exactly, even a common one.
- Iterate by reference ("direction B: tighten the header") rather than regenerating everything.
