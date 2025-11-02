# KeePass Sync - PowerShell Script für Windows
# Bevorzugt Python-Version, falls verfügbar

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location (Join-Path $ScriptDir "..")

# Prüfe ob Python verfügbar ist
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        if (Test-Path "python\sync_ftp.py") {
            python python\sync_ftp.py
            exit $LASTEXITCODE
        }
    }
}
catch {
    # Python nicht gefunden, fahre fort
}

# Fallback: Hinweis
Write-Host "Fehler: Python 3 nicht gefunden oder Python-Script nicht vorhanden." -ForegroundColor Red
Write-Host "Installiere Python von https://www.python.org/" -ForegroundColor Yellow
Write-Host ""
Write-Host "Hinweis: Die PowerShell-Version unterstützt aktuell nur JSON-Config."
Write-Host "Verwende die Python-Version für vollständige Funktionalität." -ForegroundColor Yellow
Read-Host "Drücken Sie Enter zum Beenden..."
exit 1
