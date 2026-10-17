---
name: design-brief
description: Turn a short design request into a full design brief, ask only for missing details, then build it in the right place (Design canvas, Figma, prototype, code or iOS).
---

# /design-brief

Turn a one-line design request ("/design-brief settings screen for my booking app") into a complete brief, confirm it, then build it with the right tool.

## 1. Fill the brief from what is already known

Start from the user's request, this conversation, and any project context you have (product, users, stack, existing design system). Fill every field you can without asking:

```
DESIGN: <what to make> for <web desktop / iOS / Android / responsive>
PRODUCT: <one line on what the app does>
USERS: <who, and the context they use it in>
JOB OF THIS SCREEN: <the one thing the user must get done here>
CONTENT: <real sample data: names, numbers, edge cases - never lorem ipsum>
SCREENS / STATES: <screens; plus empty, loading, error, success where they matter>
LOOK: <mood in concrete nouns from the subject's world, or "use my default design system">
CONSTRAINTS: <brand colors, fonts, framework, light/dark, WCAG AA>
OUTPUT: <Design canvas | Figma file | clickable prototype | code in <stack> | iOS screens>
VARIATIONS: <one | 3 distinct directions>
```

## 2. Ask only for what is missing and matters

- Ask at most 4 questions in one round (multiple-choice where possible). Never ask for something you already have.
- Always required: PRODUCT, USERS, JOB, OUTPUT. If any is missing, ask.
- Use these defaults instead of asking:
  - Platform: responsive web (1440 + 390) unless the request says mobile/iOS/Android.
  - Content: invent realistic sample data that fits the product, including one awkward edge case (a long name, zero results).
  - States: include empty and error for any screen that lists or submits data.
  - Look: the user's default design system if one exists; otherwise a direction drawn from the product's own world.
  - Constraints: WCAG AA, light and dark.
  - Variations: 3 directions for a first look at something new; 1 for a screen inside an existing system.
- If the user is not there to answer, use the defaults, say which ones you assumed, and continue.

## 3. Show the brief

Print the completed brief in a code block so the user can reuse it, then start building in the same turn. Do not wait for approval unless the output is expensive to redo (several screens in Figma, or code across many files) and something in the brief is still a guess.

## 4. Build it with the right tool

| OUTPUT / platform | Do this |
| --- | --- |
| Design canvas (default for "show me", mockups, options) | Create from the Design artifact type. List design systems first and use the one marked default. |
| Design system | Create from the Design System artifact type; offer to mark it default. |
| New mobile app with no design system yet | Use the mobile-design-system skill first (if installed), then design screens on top of it. |
| iOS screens or flows | Use the ios-flows skill to plan multi-step flows, then ios-screens to build (if installed). Frames 390x844, 44pt targets, safe areas, Dynamic Type. |
| Android screens | Material 3 patterns, 360x800 frames, top app bar and system back. |
| Figma | Needs a file link (or create a new file). Load figma-use and figma-generate-design; search the library and reuse components before drawing new ones. |
| Clickable prototype | One self-contained HTML page published as an artifact, with working navigation between screens. Follow frontend-design. |
| Code | Build in the named stack, using the design system's tokens; reuse existing components in the user's project. |

In every case follow the frontend-design guidance: plan palette, type, layout and principles first, check them against generic defaults, then build.

## 5. Close the loop

After delivering, give one line on what was made and offer the next step that fits:
- First look done -> "Pick a direction and I'll turn it into your design system."
- Screens done -> run design-critique (or ios-review for iOS) and accessibility-review, then apply the fixes.
- Ready for build -> design-handoff for a dev spec, or straight to code.

## Rules

- Real content always; placeholder text produces templated designs.
- Name the states, not just the screens.
- Keep the brief's own words when the user specified a look, even a common one.
- Iterate by reference ("option B, artboard 2: tighten the header") rather than regenerating everything.
