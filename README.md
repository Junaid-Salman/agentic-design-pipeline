# Agentic Design Pipeline for Web and Mobile Apps

Design web and mobile app screens with Claude by writing a brief instead of a wish. This kit contains one skill, `/design-brief`, that turns a one-line request into a full design brief, asks only for what's missing, and builds the result in the right place: a design canvas, Figma, a clickable prototype, code, or native iOS screens.

The full guide (toolkit, routing table, brief template, workflows, prompt library) is the shared doc that came with this kit.

## What's inside

```
agentic-design-pipeline/
├── claude-code/skills/design-brief/SKILL.md   # for Claude Code (reads your repo, writes files)
├── claude-app/design-brief/SKILL.md           # for the Claude app (Design canvas, artifacts)
├── install.sh                                 # Claude Code install, macOS/Linux
└── install.ps1                                # Claude Code install, Windows
```

## Use it in Claude Code

**1. Install the skill**

macOS / Linux:
```bash
bash install.sh
```
Windows (PowerShell):
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```
Or copy by hand: `claude-code/skills/design-brief/SKILL.md` → `~/.claude/skills/design-brief/SKILL.md` (all projects) or `.claude/skills/design-brief/SKILL.md` (one repo). Restart Claude Code.

**2. Connect Figma (optional, recommended)**

```bash
claude plugin install figma@claude-plugins-official
```
Restart, type `/plugin` → **Installed** → `figma` → Enter twice → **Allow access** in the browser.

If plugins are blocked for your organization, add only the MCP server:
```bash
claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp
```
Then `/mcp` → **figma** → **Authenticate**. Check with `claude mcp list`.

Source: [Figma MCP setup guide](https://help.figma.com/hc/en-us/articles/39888612464151)

**3. Run it**
```
/design-brief settings screen for my booking app
```

## Use it in the Claude app

Open the skills settings, choose to add or upload a skill, and upload the `claude-app/design-brief` folder (zip it if the uploader asks for a zip). Then type `/design-brief` in a chat.

For the best results, also enable the **Design** and **Figma** plugins, and optionally these from the plugin directory: **Mobile App Design (iOS)**, **Mobile Design System**, **design-skills**.

## The brief it writes

```
DESIGN: <what to make> for <web desktop / iOS / Android / responsive>
PRODUCT: <one line on what the app does>
USERS: <who, and the context they use it in>
JOB OF THIS SCREEN: <the one thing the user must get done here>
CONTENT: <real sample data: names, numbers, edge cases>
SCREENS / STATES: <screens; plus empty, loading, error, success>
LOOK: <mood in concrete nouns, or "use my design system">
CONSTRAINTS: <brand colors, fonts, framework, light/dark, WCAG AA>
OUTPUT: <canvas | Figma | prototype | code | iOS screens>
VARIATIONS: <one | 3 distinct directions>
```

You can also paste this template into any chat without installing anything.

## Tips

- Give real content. Placeholder text produces templated designs.
- Ask for states (empty, loading, error), not just screens.
- Build a design system first; every later screen stays consistent with it.
- Iterate by reference: "direction B, tighten the header" beats "make it better".
