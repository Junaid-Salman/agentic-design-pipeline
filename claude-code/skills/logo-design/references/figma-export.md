# Exporting the logo system to Figma

Use this only when the user picked the Figma output and the Figma MCP tools are available. Build the SVG masters first (same process as the SVG output); Figma is a destination, not where the design is invented.

## 1. Check the connection

Figma tools are often deferred. Their prefix depends on how the server was added (`mcp__Figma__` in the Claude app, often `mcp__figma__` in Claude Code), so search for "figma" if the exact names below don't match. Load them in one call:

`ToolSearch` → `select:mcp__Figma__whoami,mcp__Figma__create_new_file,mcp__Figma__create_session,mcp__Figma__use_figma,mcp__Figma__get_screenshot`

If none come back, or `whoami` fails with an auth error, tell the user the Figma connector isn't connected (in the Claude app: connector settings; in Claude Code: `claude plugin install figma@claude-plugins-official` or `claude mcp add`), then deliver the SVG kit instead. Never stall the whole job on Figma.

## 2. Load the required Figma skills

The Figma plugin requires its own skills before writing: load `figma:figma-use` and `figma:figma-generate-design` with the Skill tool (and `figma:figma-create-new-file` before `create_new_file`). Follow their rules — they cover session creation, `skillNames` logging, colours in 0–1 range, font loading and returning node IDs.

## 3. Target file

- If the user gave a Figma URL, extract the fileKey from it.
- Otherwise create a new Design file named "<Brand> — Logo".
- Call `create_session` with the fileKey before any other file tool, and reuse the session id.

## 4. What to build (one `use_figma` call per section is fine)

Put everything on a page called **Logo**, laid out left to right in auto-layout frames so nothing overlaps:

1. **Masters** — each final SVG imported with `figma.createNodeFromSvg(svg)`. Give the SVG explicit `width`/`height` equal to the intended size, otherwise it imports at viewBox size. Rename each frame (`Logo / Horizontal / Color`, etc.) and convert each one to a component (`figma.createComponentFromNode`) so the user can reuse them.
2. **Variants** — colour, black, white (white sits on a dark frame).
3. **Colour styles / variables** — create a "Brand" variable collection with the palette (scope colour variables to fills) and bind the logo fills to them where practical.
4. **Clear space & minimum size** — a frame showing the primary lockup with a clear-space boundary (dashed rectangle) and a note of the minimum size.
5. **Concepts (optional)** — the rejected concepts on a separate frame labelled "Explorations", if the user wants a record.

Return all created node IDs from every call. After building, take one `get_screenshot` of the page to check nothing overlaps or imported at the wrong size, fix once if needed, then share the file link with the user.

## 5. Also deliver files

Even with Figma, still run `export_kit.py` into `design/logo/`: Figma is for editing, the kit is for using the logo today (favicons, social images).
