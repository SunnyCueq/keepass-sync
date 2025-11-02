#!/bin/bash
# KeePass Sync - macOS Script
# Bevorzugt Python-Version, falls verfügbar

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

# Prüfe ob Python verfügbar ist und nutze Python-Version
if command -v python3 &> /dev/null || command -v python &> /dev/null; then
    PYTHON_CMD=$(command -v python3 2>/dev/null || command -v python 2>/dev/null)
    if [ -f "python/sync_ftp.py" ]; then
        $PYTHON_CMD python/sync_ftp.py
        exit $?
    fi
fi

# Fallback: Hinweis
echo "Fehler: Python 3 nicht gefunden oder Python-Script nicht vorhanden."
echo "Installiere Python 3: brew install python3"
echo "Oder verwende die Bash-Version direkt (benötigt Anpassungen für JSON-Config)"
exit 1
