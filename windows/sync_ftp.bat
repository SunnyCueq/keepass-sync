@echo off
REM KeePass Sync - Windows Script
REM Bevorzugt Python-Version, falls verfügbar

cd /d "%~dp0\.."

REM Prüfe ob Python verfügbar ist
python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    if exist "python\sync_ftp.py" (
        python python\sync_ftp.py
        exit /b %ERRORLEVEL%
    )
)

REM Fallback: PowerShell
if exist "windows\sync_ftp.ps1" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "windows\sync_ftp.ps1"
    exit /b %ERRORLEVEL%
)

echo Fehler: Python nicht gefunden oder Scripts nicht vorhanden.
echo Installiere Python von https://www.python.org/
pause
exit /b 1
