#!/bin/bash
# KeePass Sync - Linux Script
# Bevorzugt Python-Version, falls verfügbar

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$BASE_DIR"

# Prüfe ob Python verfügbar ist und nutze Python-Version
if command -v python3 &> /dev/null; then
    if [ -f "python/sync_ftp.py" ]; then
        python3 python/sync_ftp.py
        exit $?
    fi
fi

# Fallback: Hinweis
echo "Fehler: Python 3 nicht gefunden oder Python-Script nicht vorhanden."
echo "Installiere Python 3: sudo apt install python3"
echo "Oder verwende die Bash-Version direkt (benötigt Anpassungen für JSON-Config)"
exit 1
