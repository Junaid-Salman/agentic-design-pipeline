#!/usr/bin/env bash
# Installs the Agentic Design Pipeline skills for Claude Code (all projects).
#   bash install.sh                 # install every skill
#   bash install.sh logo-design     # install only the named skill(s)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)/claude-code/skills"
DEST_ROOT="$HOME/.claude/skills"

if [ "$#" -gt 0 ]; then SKILLS=("$@"); else SKILLS=($(ls "$ROOT")); fi

mkdir -p "$DEST_ROOT"
for skill in "${SKILLS[@]}"; do
  if [ ! -d "$ROOT/$skill" ]; then
    echo "Unknown skill: $skill (available: $(ls "$ROOT" | tr '\n' ' '))" >&2
    exit 1
  fi
  rm -rf "${DEST_ROOT:?}/$skill"
  cp -r "$ROOT/$skill" "$DEST_ROOT/$skill"
  echo "Installed /$skill to $DEST_ROOT/$skill"
done

# logo-design renders and exports with a few local tools; warn if any are missing.
if [ -d "$DEST_ROOT/logo-design" ] && printf '%s\n' "${SKILLS[@]}" | grep -qx logo-design; then
  missing=()
  command -v rsvg-convert >/dev/null || missing+=("rsvg-convert")
  python3 -c "import fontTools, PIL" 2>/dev/null || missing+=("python3 fontTools/Pillow")
  command -v npm >/dev/null || missing+=("npm (for downloading Google Fonts)")
  if [ "${#missing[@]}" -gt 0 ]; then
    echo
    echo "logo-design needs: ${missing[*]}"
    echo "  Ubuntu/Debian: sudo apt install -y librsvg2-bin python3-fonttools python3-pil nodejs npm"
    echo "  macOS:         brew install librsvg node && pip3 install fonttools pillow"
  fi
fi

echo
echo "Restart Claude Code, then try: /design-brief settings screen for my app  or  /logo-design logo for my app"
