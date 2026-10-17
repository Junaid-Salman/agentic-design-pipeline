#!/usr/bin/env bash
# Installs the /design-brief skill for Claude Code (all projects).
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)/claude-code/skills/design-brief/SKILL.md"
DEST="$HOME/.claude/skills/design-brief"
mkdir -p "$DEST"
cp "$SRC" "$DEST/SKILL.md"
echo "Installed /design-brief to $DEST"
echo "Restart Claude Code, then try: /design-brief settings screen for my app"
