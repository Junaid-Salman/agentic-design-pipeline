# Agentic Design Pipeline for Web and Mobile Apps

Design web and mobile apps with Claude, from the logo to the screens. This kit contains two skills:

- **`/logo-design`** creates the brand first: discovery, distinct concepts, a refined logo as clean SVG, every variant and export (favicons, app and social icons) and a one-page brand guide. You choose which stages to run, so you only spend tokens where you want them.
- **`/design-brief`** turns a one-line screen request into a full design brief, asks only for what's missing, and builds the result in the right place: a design canvas, Figma, a clickable prototype, code, or native iOS screens.

Each skill works on its own. Used together, design-brief picks up the palette, typefaces and logo files that logo-design produced, so the screens match the brand.

The full guide (toolkit, routing table, brief template, workflows, prompt library) is the shared doc that came with this kit.

## What's inside

```
agentic-design-pipeline/
├── claude-code/skills/                 # for Claude Code (reads your repo, writes files)
│   ├── design-brief/SKILL.md
│   └── logo-design/                    # SKILL.md + scripts/ + references/
├── claude-app/                         # for the Claude app (Design canvas, artifacts)
│   ├── design-brief/SKILL.md
│   └── logo-design/
├── install.sh                          # Claude Code install, macOS/Linux
└── install.ps1                         # Claude Code install, Windows
```

## Use it in Claude Code

**1. Install the skills**

macOS / Linux:
```bash
bash install.sh                # both skills
bash install.sh logo-design    # or just one
```
Windows (PowerShell):
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
powershell -ExecutionPolicy Bypass -File install.ps1 logo-design
```
Or copy by hand: copy the whole skill folder from `claude-code/skills/<skill>/` to `~/.claude/skills/<skill>/` (all projects) or `.claude/skills/<skill>/` (one repo). Copy the folder, not just `SKILL.md`, because logo-design needs its `scripts/` and `references/`. Restart Claude Code.

logo-design also needs a few local tools to render and export. The install script tells you if any are missing:
```bash
# Ubuntu / Debian
sudo apt install -y librsvg2-bin python3-fonttools python3-pil nodejs npm
# macOS
brew install librsvg node && pip3 install fonttools pillow
```
On Windows, the simplest route is running Claude Code in WSL and using the Ubuntu command. design-brief needs nothing extra.

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
/logo-design logo for my booking app, Slotwise
/design-brief settings screen for my booking app
```
logo-design saves its work in `design/logo/` (concepts, masters, the export kit and `brand-guide.html`), next to the briefs design-brief saves in `design/briefs/`.

## Use it in the Claude app

Open the skills settings, choose to add or upload a skill, and upload the `claude-app/design-brief` and `claude-app/logo-design` folders, one at a time (zip each if the uploader asks for a zip). Then type `/logo-design` or `/design-brief` in a chat. The Claude app already has the tools logo-design's scripts need.

For the best results, also enable the **Design** and **Figma** plugins, and optionally these from the plugin directory: **Mobile App Design (iOS)**, **Mobile Design System**, **design-skills**.

## How logo-design works

It opens with one question about the output (**SVG logo**, **design brief + image-model prompts**, or **Figma** if connected) and which optional stages to run. Each stage shows its rough cost:

| Stage | What you get | Cost |
|---|---|---|
| Discovery questions | One short round on personality, audience and colours | Low, and prevents redoing the logo |
| Multiple concepts | 3–5 genuinely different directions on a proof sheet | Highest; untick for one strong concept |
| Variants & export kit | Icon, lockups, mono/reversed, favicons, app, touch and social icons, zipped | Low (scripted) |
| Mini brand guide | Clear space, minimum size, colours, fonts, don'ts | Medium |

Every concept is rendered and checked on light and dark backgrounds and at 16/32/64 px before you see it, and type is converted to outlines so the logo never depends on installed fonts.

## The brief design-brief writes

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
- Do the logo before the screens. A brand guide gives every later screen its colours and type.
