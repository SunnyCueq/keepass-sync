# 📖 Detaillierte Installations- und Setup-Anleitung - AutoIt Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![AutoIt](https://img.shields.io/badge/AutoIt-3.3+-1C1C1C.svg)](https://www.autoitscript.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](.)

> **Windows-native - Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

---

## 🇩🇪 Deutsch

### ⚠️ WICHTIG: Windows-Only

Die AutoIt-Variante läuft **NUR auf Windows**. Für Linux/macOS nutze die Python-, Go- oder Node.js-Variante.

### 📋 Inhaltsverzeichnis

1. [Systemanforderungen](#systemanforderungen)
2. [AutoIt Installation](#autoit-installation)
3. [JSON-Bibliotheken](#json-bibliotheken)
4. [Externe Dependencies](#externe-dependencies)
5. [Kompilierung](#kompilierung)
6. [Konfiguration](#konfiguration)
7. [Verwendung](#verwendung)
8. [Fehlerbehebung](#fehlerbehebung)
9. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Windows** | Windows 7 SP1+ | Windows 10/11 | x86, x64 |

#### Erforderliche Software

1. **AutoIt**
   - **Minimale Version**: 3.3.14.0+
   - **Empfohlene Version**: 3.3.16.1+ (aktuellste stabile Version)
   - **Download**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

2. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **WinSCP** (Optional, aber empfohlen)
   - **Minimale Version**: 5.19+
   - **Empfohlene Version**: 6.x+ (aktuellste Version)
   - **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

4. **Externe Tools** (optional, abhängig vom Protokoll):
   - **lftp**: Für FTP/SFTP (via Git Bash oder WSL)
   - **Native Windows SMB**: Für SMB/CIFS-Netzwerk-Shares (bereits integriert)

---

### 🤖 AutoIt Installation

#### Windows

##### Installer Download (Empfohlen)

1. **Download**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)
2. **Wähle**: AutoIt Full Installation (nicht nur AutoIt3.exe)
3. **Empfohlen**: "AutoIt Full Installation" mit SciTE Editor
4. **Führe Installer aus**: Folgen Sie den Anweisungen
5. **WICHTIG**: Stelle sicher, dass AutoIt im PATH ist (normalerweise automatisch)

##### Überprüfung

```powershell
# PowerShell oder CMD
AutoIt3.exe /version
# Sollte zeigen: AutoIt v3.3.x.x

# Überprüfe auch SciTE Editor (falls installiert)
# Starte SciTE Editor
```

##### Chocolatey (Alternative)

```powershell
# Installiere Chocolatey (falls nicht vorhanden)
# Siehe: https://chocolatey.org/install

# Installiere AutoIt
choco install autoit

# Überprüfe
AutoIt3.exe /version
```

**Link**: [Chocolatey AutoIt Package](https://community.chocolatey.org/packages/autoit)

##### SciTE Editor (Empfohlen)

SciTE ist ein Editor speziell für AutoIt-Scripts mit:
- Syntax-Highlighting
- Auto-Vervollständigung
- Kompilierung mit F7
- Fehleranzeige

**Installation**: Wird normalerweise mit AutoIt Full Installation installiert.

**Alternative**: [SciTE Standalone](https://www.scintilla.org/SciTEDownload.html)

---

### 📦 JSON-Bibliotheken

Die AutoIt-Variante benötigt JSON-Bibliotheken für das Parsen der `config.json`.

#### ✅ Enthaltene Bibliotheken

**WICHTIG**: Die benötigten Dateien sind **bereits im Repository enthalten**!

- **Json.au3** (Version 2021.11.20)
- **BinaryCall.au3** (Version 2014.7.24)

**Lage**: `autoit/Json.au3` und `autoit/BinaryCall.au3`

#### Überprüfung

```powershell
# Überprüfe ob Dateien vorhanden sind
dir autoit\Json.au3
dir autoit\BinaryCall.au3
```

**Hinweis**: Beide Dateien müssen im selben Verzeichnis wie `sync.au3` liegen, damit sie korrekt eingebunden werden.

#### Details zu den Bibliotheken

##### Json.au3

- **Version**: 2021.11.20 (20. November 2021)
- **Entwickler**: Ward
- **Abhängigkeit**: BinaryCall.au3
- **Funktionen**: Json_Decode(), Json_Get(), Json_Put()
- **Link**: [AutoIt Forum Topic #148114](https://www.autoitscript.com/forum/topic/148114-a-non-strict-json-udf-jsmn/)

##### BinaryCall.au3

- **Version**: 2014.7.24 (24. Juli 2014)
- **Entwickler**: Ward
- **Zweck**: Basis-Utility für Binary-Operationen
- **Benötigt von**: Json.au3

**Status**: Beide Bibliotheken sind funktionsfähig und getestet. Siehe `autoit/DEPENDENCIES.md` für Details.

---

### 📦 Externe Dependencies

#### 1. KeePassXC-CLI (ERFORDERLICH)

**Zweck**: Zum Mergen der KeePass-Datenbanken

##### Windows Installation

1. **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. **Wähle**: Windows Installer (.msi)
3. **Installiere**: Folgen Sie den Anweisungen
4. **WICHTIG**: Stelle sicher, dass `keepassxc-cli.exe` im PATH ist

##### Überprüfung

```powershell
# PowerShell oder CMD
keepassxc-cli version
# Sollte Version anzeigen: 2.7.x oder ähnlich

# Oder vollständiger Pfad
"C:\Program Files\KeePassXC\keepassxc-cli.exe" --version
```

**Links**:
- **Offizielle Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)
- **Dokumentation**: [https://keepassxc.org/docs/](https://keepassxc.org/docs/)

**PATH-Einstellung** (falls nötig):

```powershell
# Füge KeePassXC zu PATH hinzu
# Systemsteuerung → Umgebungsvariablen → PATH
# Füge hinzu: C:\Program Files\KeePassXC\
```

#### 2. WinSCP (Für FTP/SFTP - EMPFOHLEN)

**Zweck**: Datei-Übertragungen via FTP und SFTP auf Windows

##### Windows Installation

1. **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)
2. **Wähle**: Windows Installer
3. **WICHTIG**: Wähle "Portable" oder "Installation" mit "WinSCP.com" (Command-Line Tool)
4. **Installiere**: Folgen Sie den Anweisungen
5. **Überprüfe**: `WinSCP.com` sollte im PATH sein

##### Überprüfung

```powershell
# PowerShell oder CMD
WinSCP.com /version
# Sollte Version anzeigen
```

**Standard-Pfad**:
- Installation: `C:\Program Files (x86)\WinSCP\WinSCP.com`
- Portable: `C:\Pfad\zu\WinSCP\WinSCP.com`

##### Alternative: lftp (via Git Bash / WSL)

Wenn WinSCP nicht installiert werden soll:

**Option 1: Git Bash**

```bash
# In Git Bash
# lftp sollte verfügbar sein oder installierbar
```

**Option 2: WSL (Windows Subsystem for Linux)**

```bash
# In WSL
sudo apt install lftp
```

**Links**:
- **WinSCP**: [https://winscp.net/eng/index.php](https://winscp.net/eng/index.php)
- **WinSCP Documentation**: [https://winscp.net/eng/docs/start](https://winscp.net/eng/docs/start)

#### 3. Native Windows SMB (Für SMB/CIFS - Bereits vorhanden)

**Zweck**: Zugriff auf Windows-Netzwerk-Shares

Windows hat native SMB-Unterstützung über `net use` und UNC-Pfade. Keine zusätzliche Installation erforderlich.

**Verwendete Tools**:
- `net use` - Windows-Befehlszeilen-Tool für Netzwerk-Shares
- UNC-Pfade (`\\server\share`)

---

### 🔨 Kompilierung

#### Schritt-für-Schritt Anleitung

##### 1. Repository klonen oder Dateien herunterladen

```powershell
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync\autoit

# Option 2: Download ZIP
# Entpacke ZIP-Datei und navigiere zum autoit/ Verzeichnis
```

##### 2. Überprüfe AutoIt-Installation

```powershell
AutoIt3.exe /version
```

##### 3. Überprüfe JSON-Bibliotheken

```powershell
# Stelle sicher, dass diese Dateien vorhanden sind:
dir Json.au3
dir BinaryCall.au3
dir sync.au3
```

##### 4. Kompiliere das Script

**Methode 1: AutoIt3 Compiler (Kommandozeile)**

```powershell
# Navigiere zum autoit-Verzeichnis
cd autoit

# Kompiliere
AutoIt3.exe /in sync.au3 /out sync.exe

# Überprüfe
dir sync.exe
```

**Methode 2: SciTE Editor (Empfohlen)**

1. Öffne `sync.au3` in SciTE Editor
2. Drücke **F7** (oder Tools → Compile)
3. Die kompilierte `sync.exe` wird erstellt

**Methode 3: Kompilierung mit Compiler-Direktiven**

```powershell
# Mit Icon (optional)
AutoIt3.exe /in sync.au3 /out sync.exe /icon icon.ico

# Ohne Konsolenfenster (für GUI-Scripts)
AutoIt3.exe /in sync.au3 /out sync.exe /nopack
```

##### 5. Teste die kompilierte EXE

```powershell
.\sync.exe --version
# Sollte zeigen: KeePass Sync 1.1.0 (AutoIt)
```

---

### ⚙️ Konfiguration

#### 1. Erstelle config.json

```powershell
# Navigiere zum Hauptverzeichnis (ein Level nach oben)
cd ..

# Kopiere Beispiel-Config
copy config.example.json config.json

# Bearbeite config.json
notepad config.json  # Oder anderen Editor verwenden
```

**Wichtige Einstellungen**:

```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-passwort",
    "type": "ftp",  // "ftp", "sftp", "smb"
    "remotePath": "/keepass_passwords.kdbx",
    "port": 21
  },
  "local": {
    "localPath": "keepass_passwords.kdbx",
    "tempPath": "temp_keepass_passwords.kdbx",
    "backupDir": "backups",
    "maxBackups": 2
  },
  "keepass": {
    "databasePassword": "dein-keeppass-master-passwort",
    "keepassXCPath": "keepassxc-cli"
  },
  "settings": {
    "debug": false,
    "language": "de",
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

**Hinweis**: Die AutoIt-Variante unterstützt aktuell **kein SCP**. Nutze SFTP stattdessen.

---

### 💻 Verwendung

#### Basis-Befehle

```powershell
# Normale Synchronisation
.\sync.exe

# Verbindung testen (ohne Sync)
.\sync.exe --test

# Status anzeigen
.\sync.exe --status

# Alternative Config-Datei
.\sync.exe --config "C:\Pfad\zu\config.json"

# Version anzeigen
.\sync.exe --version
```

#### Als .au3 Script (ohne Kompilierung)

```powershell
# Führe direkt als Script aus
AutoIt3.exe sync.au3

# Mit Argumenten
AutoIt3.exe sync.au3 --test
```

#### Automatisierung

##### Task Scheduler (Windows)

1. **Öffne Task Scheduler** (taskschd.msc)
2. **Erstelle neue Aufgabe**
3. **Allgemein**:
   - Name: `KeePass Sync`
   - Ausführen als: Dein Benutzer
   - "Unabhängig von Benutzeranmeldung ausführen" (optional)
4. **Trigger**:
   - Neu → Zeitplan
   - Wiederholung: Täglich/Stündlich/etc.
5. **Aktionen**:
   - Aktion: Programm starten
   - Programm: `C:\Pfad\zum\sync.exe`
   - Argumente: (leer für normale Sync)
6. **Speichern**

**Beispiel: Stündlich**

```
Trigger: Wiederholen alle: 1 Stunde
Aktion: C:\Tools\KeePass Sync\autoit\sync.exe
```

---

### 🔍 Fehlerbehebung

#### "AutoIt3.exe: command not found"

**Problem**: AutoIt ist nicht installiert oder nicht im PATH

**Lösung**:
```powershell
# Überprüfe Installation
where AutoIt3.exe

# Falls nicht gefunden, installiere AutoIt (siehe oben)
# Oder füge zu PATH hinzu:
# Systemsteuerung → Umgebungsvariablen → PATH
# Füge hinzu: C:\Program Files (x86)\AutoIt3\
```

#### "Json.au3 nicht gefunden" oder "BinaryCall.au3 nicht gefunden"

**Problem**: JSON-Bibliotheken fehlen

**Lösung**:
```powershell
# Die Dateien sollten bereits im autoit/ Verzeichnis sein
dir autoit\Json.au3
dir autoit\BinaryCall.au3

# Falls fehlend, stelle sicher, dass sie im selben Verzeichnis wie sync.au3 sind
# Kopiere von Repository falls nötig
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```powershell
# Installiere KeePassXC (siehe oben)
# Überprüfe Installation
keepassxc-cli version

# Falls nicht gefunden, füge zu PATH hinzu:
# C:\Program Files\KeePassXC\
```

#### "WinSCP.com nicht gefunden"

**Problem**: WinSCP ist nicht installiert oder nicht im PATH

**Lösung**:
```powershell
# Installiere WinSCP (siehe oben)
# Überprüfe Installation
WinSCP.com /version

# Falls nicht gefunden, füge zu PATH hinzu:
# C:\Program Files (x86)\WinSCP\
```

**Alternative**: Nutze lftp via Git Bash oder WSL

#### Kompilierungsfehler

**Problem**: Fehler beim Kompilieren

**Lösung**:
```powershell
# Überprüfe Script auf Syntax-Fehler
# Öffne in SciTE Editor für bessere Fehleranzeige

# Überprüfe alle Includes
# Stelle sicher, dass Json.au3 und BinaryCall.au3 vorhanden sind
```

#### "SCP wird nicht unterstützt"

**Hinweis**: Die AutoIt-Variante unterstützt aktuell kein SCP-Protokoll.

**Lösung**: Nutze SFTP stattdessen (funktioniert mit WinSCP oder lftp).

---

### 🙏 Danksagungen

#### AutoIt

- **Entwickler**: AutoIt Team
- **Website**: [https://www.autoitscript.com/](https://www.autoitscript.com/)
- **Lizenz**: Freeware (closed source)
- **Download**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

#### SciTE Editor

- **Entwickler**: Neil Hodgson
- **Website**: [https://www.scintilla.org/SciTE.html](https://www.scintilla.org/SciTE.html)
- **Lizenz**: Historical Permission Notice and Disclaimer
- **Download**: [https://www.scintilla.org/SciTEDownload.html](https://www.scintilla.org/SciTEDownload.html)

#### Json.au3

- **Entwickler**: Ward
- **Version**: 2021.11.20
- **AutoIt Forum**: [Topic #148114](https://www.autoitscript.com/forum/topic/148114-a-non-strict-json-udf-jsmn/)
- **Lizenz**: (siehe Datei-Header)

#### BinaryCall.au3

- **Entwickler**: Ward
- **Version**: 2014.7.24
- **Lizenz**: (siehe Datei-Header)

#### KeePassXC

- **Entwickler**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **Lizenz**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### WinSCP

- **Entwickler**: Martin Přikryl
- **Website**: [https://winscp.net/](https://winscp.net/)
- **Lizenz**: GPL
- **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

---

<div align="center">

**🤖 AutoIt-Variante: Windows-native, GUI-fähig, keine Runtime nötig**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

