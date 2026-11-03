# Installs the Agentic Design Pipeline skills for Claude Code (all projects).
#   powershell -ExecutionPolicy Bypass -File install.ps1                 # install every skill
#   powershell -ExecutionPolicy Bypass -File install.ps1 logo-design     # install only the named skill(s)
$Root     = Join-Path $PSScriptRoot "claude-code\skills"
$DestRoot = Join-Path $env:USERPROFILE ".claude\skills"
$Available = Get-ChildItem -Directory $Root | ForEach-Object { $_.Name }
$Skills = if ($args.Count -gt 0) { $args } else { $Available }

New-Item -ItemType Directory -Force -Path $DestRoot | Out-Null
foreach ($skill in $Skills) {
    if ($Available -notcontains $skill) {
        Write-Error "Unknown skill: $skill (available: $($Available -join ', '))"
        exit 1
    }
    $Dest = Join-Path $DestRoot $skill
    if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
    Copy-Item -Recurse (Join-Path $Root $skill) $Dest
    Write-Host "Installed /$skill to $Dest"
}

if ($Skills -contains "logo-design") {
    $missing = @()
    if (-not (Get-Command rsvg-convert -ErrorAction SilentlyContinue)) { $missing += "rsvg-convert" }
    $py = Get-Command python3 -ErrorAction SilentlyContinue
    if (-not $py) { $py = Get-Command python -ErrorAction SilentlyContinue }
    if (-not $py) { $missing += "Python 3" }
    else {
        & $py.Source -c "import fontTools, PIL" 2>$null
        if ($LASTEXITCODE -ne 0) { $missing += "Python packages fonttools, pillow" }
    }
    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) { $missing += "npm (for downloading Google Fonts)" }
    if ($missing.Count -gt 0) {
        Write-Host ""
        Write-Host "logo-design needs: $($missing -join ', ')"
        Write-Host "  Easiest on Windows: run Claude Code in WSL (Ubuntu) and install with apt there."
        Write-Host "  Native Windows: pip install fonttools pillow; rsvg-convert via MSYS2 (pacman -S mingw-w64-x86_64-librsvg), added to PATH."
    }
}

Write-Host ""
Write-Host "Restart Claude Code, then try: /design-brief settings screen for my app  or  /logo-design logo for my app"
