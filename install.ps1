# Installs the /design-brief skill for Claude Code (all projects).
$Src  = Join-Path $PSScriptRoot "claude-code\skills\design-brief\SKILL.md"
$Dest = Join-Path $env:USERPROFILE ".claude\skills\design-brief"
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
Copy-Item $Src (Join-Path $Dest "SKILL.md") -Force
Write-Host "Installed /design-brief to $Dest"
Write-Host "Restart Claude Code, then try: /design-brief settings screen for my app"
