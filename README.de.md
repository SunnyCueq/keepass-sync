# 🔐 KeePass Sync - Synchronisiere deine Passwörter automatisch

<div align="center">

**🌍 Sprachen: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](.)

> **Synchronisiere deine KeePass-Datenbank automatisch zwischen mehreren Computern über einen FTP-Server.**

[🚀 Schnellstart](#-schnellstart) • [📖 Dokumentation](#-dokumentation) • [🛠️ Installation](#️-installation) • [❓ FAQ](#-häufige-fragen) • [🤝 Mitwirken](#-mitwirken)

</div>

---

## 🚀 Schnellstart

### 1. Voraussetzungen

- **KeePassXC** installiert (von [keepassxc.org](https://keepassxc.org/))
- **Python 3** installiert (meist vorinstalliert auf Linux/macOS)
- **FTP-Zugangsdaten** für deinen Server

### 2. Konfiguration

**Option A: Interaktiver Installer (Empfohlen für Anfänger)**
```bash
python3 install.py
```
oder
```bash
python3 python/installer.py
```

Der Installer:
- ✅ Erkennt automatisch dein System
- ✅ Zeigt System-Spezifikationen an
- ✅ Erkennt automatisch deine Sprache
- ✅ Führt dich durch die Konfiguration
- ✅ Unterstützt alle Protokolle (FTP, SFTP, SMB, SCP)
- ✅ Erstellt automatisch `config.json`

**Option B: Manuelle Konfiguration**
```bash
cp config.example.json config.json
```

Dann öffne `config.json` und trage deine Daten ein:
```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-passwort",
    "type": "ftp",
    "comment": "Protokoll-Optionen: 'ftp' (Standard), 'sftp', 'smb', 'scp'",
    "remotePath": "/keepass_passwords.kdbx"
  },
  "keepass": {
    "databasePassword": "dein-keeppass-master-passwort"
  }
}
```

### 3. Testen

**Linux:**
```bash
# Wrapper testen (bevorzugt)
python3 sync.py

# Oder .sh Datei direkt
./linux/sync_ftp.sh

# Oder Python-Script direkt (mit Debug)
python3 python/sync_ftp.py
```

**Erwartete Ausgabe bei Erfolg:**
```
2025-11-02 17:XX:XX === KeePass Sync - Linux ===
2025-11-02 17:XX:XX Backup wird erstellt...
2025-11-02 17:XX:XX Backup erfolgreich erstellt
2025-11-02 17:XX:XX Starte Download vom Server...
2025-11-02 17:XX:XX Download erfolgreich
2025-11-02 17:XX:XX Führe Merge durch...
2025-11-02 17:XX:XX Merge erfolgreich abgeschlossen. Lokale Datei aktualisiert.
2025-11-02 17:XX:XX Starte Upload zum Server...
2025-11-02 17:XX:XX Upload erfolgreich abgeschlossen.
2025-11-02 17:XX:XX Synchronisation abgeschlossen.
```

**Tipp:** Teste zuerst die Verbindung ohne Backup:
```bash
python3 python/sync_ftp.py --test
```

**Fehlerbehebung:**
- **"Konfigurationsdatei nicht gefunden"** → Stelle sicher, dass `config.json` existiert
- **"KeePassXC-CLI nicht gefunden"** → Installiere: `sudo pacman -S keepassxc` (Arch) oder `sudo apt install keepassxc` (Debian)
- **"FTP-Client nicht gefunden"** → Installiere: `sudo pacman -S lftp` (Arch) oder `sudo apt install lftp` (Debian)
- **Datei-Überwachung funktioniert nicht** → Installiere: `pip install pyinotify` (Linux) oder `pip install watchdog` (alle Plattformen)

📖 **Detaillierte Test-Anleitung:** [docs/TEST.de.md](docs/TEST.de.md)

### 4. Automatische Installation

**🚀 Schnellinstallation (Linux - Empfohlen):**
```bash
./linux/install.sh
```

Dies installiert automatisch:
- ✅ Systemd Service (bei Herunterfahren)
- ✅ Cron-Job (bei Leerlauf, alle 5 Minuten)

**Windows - Task Scheduler:**
1. Task Scheduler öffnen (`taskschd.msc`)
2. "Create Task..." → Name: `KeePass Sync`
3. Trigger: "At startup", "Daily" oder "On idle"
4. Action: `powershell.exe` → Argumente: `-NoProfile -ExecutionPolicy Bypass -File "C:\Pfad\windows\sync_ftp.ps1"`

**macOS - LaunchAgent:**
```bash
# Erstelle ~/Library/LaunchAgents/com.user.keepass-sync.plist
# Siehe docs/INSTALL.de.md für vollständige Anleitung
```

📖 **Vollständige Installationsanleitung für alle Plattformen:** [docs/INSTALL.de.md](docs/INSTALL.de.md)

## 📖 Was macht das Script?

Das Script synchronisiert deine KeePass-Datenbank in 4 Schritten:

1. **🔒 Backup erstellen** - Sichert deine lokale Datei
2. **⬇️ Download** - Holt die neueste Version vom Server
3. **🔄 Merge** - Kombiniert intelligent alle Änderungen
4. **⬆️ Upload** - Speichert die aktualisierte Datei zurück

**Wichtig:** Das Script löscht **keine** Daten. Es kombiniert alle Änderungen von allen Geräten automatisch!

## 🌍 Mehrsprachigkeit

Das Script unterstützt **12 Sprachen**: Deutsch (de), English (en), Español (es), Français (fr), Italiano (it), Português (pt), Nederlands (nl), Polski (pl), Русский (ru), 中文 (zh), 日本語 (ja), 한국어 (ko).

Die Sprache wird automatisch erkannt oder kann in `config.json` eingestellt werden:
```json
{
  "settings": {
    "language": "de"
  }
}
```

## 🎯 CLI-Optionen & Features

Das Script bietet verschiedene Optionen für unterschiedliche Anwendungsfälle:

**Verbindung testen (ohne Sync):**
```bash
python3 python/sync_ftp.py --test
```
- ✅ Prüft KeePassXC-CLI Verfügbarkeit
- ✅ Prüft lokale Datenbank
- ✅ Testet Server-Verbindung
- ✅ Kein Backup nötig, keine Datenänderung

**Status anzeigen:**
```bash
python3 python/sync_ftp.py --status
```
Zeigt:
- Lokale DB-Informationen (Größe, Alter)
- Backup-Übersicht
- Konfigurations-Details

**Datei automatisch überwachen:**
```bash
python3 python/sync_ftp.py --watch
```
- Startet automatisch Sync bei Änderung der lokalen Datenbank
- Verzögerung konfigurierbar (Standard: 30 Sekunden)
- Läuft dauerhaft im Hintergrund

**Normale Synchronisation:**
```bash
python3 python/sync_ftp.py        # Standard-Sync
python3 python/sync_ftp.py --sync # Explizit Sync
python3 python/sync_ftp.py -v     # Verbose (Debug-Ausgabe)
python3 python/sync_ftp.py -q     # Quiet (nur Fehler)
```

**Weitere Optionen:**
```bash
python3 python/sync_ftp.py --config alt_config.json  # Alternative Config
python3 python/sync_ftp.py --help                     # Hilfe anzeigen
python3 python/sync_ftp.py --version                  # Version anzeigen
```

## 🔄 Verbesserte Retry-Logic

Das Script versucht automatisch, fehlgeschlagene Operationen erneut auszuführen:
- **Exponential Backoff**: 5s → 10s → 20s → max 60s
- **Konfigurierbar** in `config.json`:
```json
{
  "settings": {
    "max_retries": 3,
    "retry_delay": 5
  }
}
```
- Resilient gegen temporäre Netzwerkfehler

## 📡 Unterstützte Protokolle

Das Script unterstützt mehrere Übertragungsprotokolle:

- **FTP** (Standard) - File Transfer Protocol
- **SFTP** - SSH File Transfer Protocol (verschlüsselt)
- **SMB/CIFS** - Windows-Netzwerk-Freigaben
- **SCP** - Secure Copy Protocol (SSH-basiert)

Wähle das Protokoll in `config.json` mit `"type": "ftp"` (oder `sftp`, `smb`, `scp`).

## ⚙️ Erweiterte Konfiguration

In `config.json` kannst du zusätzlich einstellen:

- `maxBackups`: Anzahl der Backups (Standard: 2)
- `cleanupLogs`: Alte Logs automatisch löschen (Standard: true)
- `maxLogAgeDays`: Logs älter als X Tage löschen (Standard: 7)
- `debug`: Debug-Modus aktivieren (Standard: false)

## ❓ Häufige Fragen

**F: Verliere ich Daten, wenn ich auf mehreren Geräten gleichzeitig arbeite?**  
A: Nein! Das Script kombiniert alle Änderungen intelligent. Neue Passwörter werden von allen Seiten übernommen.

**F: Wie oft sollte ich synchronisieren?**  
A: Mindestens einmal täglich. Am besten automatisch einrichten (siehe docs/INSTALL.de.md).

**F: Was ist, wenn die Verbindung zum Server fehlschlägt?**  
A: Das Script erstellt vorher ein Backup. Deine lokale Datei bleibt unverändert.

**F: Funktioniert das mit mehr als 2 Computern?**  
A: Ja! So viele wie du möchtest. Der FTP-Server ist die zentrale Quelle.

## 📝 Logs & Backups

- **Logs:** `sync_log.txt` (wird automatisch aufgeräumt)
- **Backups:** `backups/` (nur die 2 neuesten werden behalten)
- **Temporäre Dateien:** Werden automatisch gelöscht

## 🔐 Sicherheit

⚠️ **Wichtig:**
- Die `config.json` enthält Passwörter im Klartext
- Stelle sicher, dass die Datei nicht öffentlich zugänglich ist
- Linux/macOS: `chmod 600 config.json`
- Windows: Rechte entsprechend setzen

---

## 📁 Verzeichnisstruktur

```
keepass-sync/
├── config.json          # Konfiguration (hier deine Daten eintragen!)
├── config.example.json   # Beispiel-Konfiguration
├── README.de.md         # Diese Dokumentation (Deutsch)
├── README.en.md         # English documentation
├── README.es.md         # Documentación en español
├── docs/                # Weitere Dokumentation
│   ├── INSTALL.de.md
│   ├── INSTALL.en.md
│   ├── INSTALL.es.md
│   ├── TEST.de.md
│   ├── TEST.en.md
│   └── TEST.es.md
├── sync.py              # Cross-Platform Wrapper
├── python/              # Python-Version (bevorzugt)
│   └── sync_ftp.py
├── php/                 # PHP-Variante (für Server-Cronjobs)
│   └── sync.php
├── linux/               # Scripts Linux
│   ├── sync_ftp.sh
│   └── install.sh       # Schnellinstallation
├── windows/             # Scripts Windows
├── mac/                 # Scripts macOS
├── lang/                # Sprachdateien (JSON)
│   ├── de.json
│   ├── en.json
│   └── es.json
└── backups/             # Automatische Backups (nur 2 neueste)
```

## 🤝 Mitwirken

### 🌟 Möchtest du helfen?

Wir freuen uns über Beiträge!

**Wie du helfen kannst:**

- 🐛 **Fehler melden**
  - Öffne ein Issue auf GitHub
  - Beschreibe das Problem

- 💡 **Verbesserungen vorschlagen**
  - Neue Features
  - Code-Optimierungen
  - Dokumentation

- 🌍 **Übersetzungen**
  - Neue Sprachen hinzufügen
  - Übersetzungen verbessern

- 💻 **Code beitragen**
  - Fork das Repository
  - Erstelle einen Pull Request

- 📖 **Dokumentation verbessern**
  - Fehlende Informationen hinzufügen
  - Beispiele verbessern

### 📝 Übersetzungen beitragen

Übersetzungen sind in `lang/*.json` Dateien gespeichert.

**Neue Sprache hinzufügen:**

1. Kopiere `lang/en.json` als Vorlage
2. Übersetze alle Werte
3. Erstelle `lang/[code].json` (z.B. `lang/fr.json`)
4. Erstelle Pull Request

**Verfügbare Sprachcodes:**
- `de` - Deutsch
- `en` - English
- `es` - Español
- `fr` - Français ✅
- `it` - Italiano ✅
- `pt` - Português ✅
- `nl` - Nederlands ✅
- `pl` - Polski ✅
- `ru` - Русский ✅
- `zh` - 中文 ✅
- `ja` - 日本語 ✅
- `ko` - 한국어 ✅

---

## 📚 Weitere Informationen

- **Test-Anleitung:** [docs/TEST.de.md](docs/TEST.de.md)
- **Installation & Automatisierung:** [docs/INSTALL.de.md](docs/INSTALL.de.md)
- **PHP-Variante:** [php/README.md](php/README.md) (für Server-Cronjobs)

---

## 🔄 Wie funktioniert die Synchronisation?

### System-Architektur

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Hauptsystem │     │              │     │  Subsystem  │
│   Desktop   │◄───►│  FTP-Server  │◄───►│   Laptop    │
│             │     │   (Zentrale   │     │             │
│  Lokale DB  │     │    Quelle)    │     │  Lokale DB  │
└─────────────┘     └──────────────┘     └─────────────┘
```

### Synchronisations-Ablauf

1. **Backup erstellen**
   - Tägliche Sicherungskopie
   - Format: `backups/keepass_passwords_YYYYMMDD.kdbx`

2. **Download vom Server**
   - Lädt entfernte Datei herunter
   - Kann Änderungen von anderen Systemen enthalten

3. **Merge durchführen**
   - Intelligente Zusammenführung
   - Neue Einträge werden übernommen
   - Konflikte werden automatisch gelöst

4. **Upload zum Server**
   - Speichert aktualisierte Datei
   - Alle Systeme haben jetzt die gleiche Version

### Warum Merge statt Überschreiben?

**Vorteile:**
- ✅ Keine Daten gehen verloren
- ✅ Änderungen auf mehreren Geräten werden kombiniert
- ✅ Konflikte werden automatisch gelöst
- ✅ Du kannst von überall arbeiten

---

<div align="center">

**Entwickelt für:** Linux, Windows, macOS  
**Version:** 1.1.0  
**Sprachen:** Deutsch, English, Español (+ 9 weitere)

**⭐ Wenn dir dieses Projekt gefällt, gib uns einen Stern auf GitHub!**

**🌍 Sprachen: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

</div>

