# 🤖 KeePass Sync - AutoIt Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![AutoIt](https://img.shields.io/badge/AutoIt-3.3+-1C1C1C.svg)](https://www.autoitscript.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](.)

> **Windows-native, GUI-fähig, keine Runtime nötig**

</div>

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
- [📦 Node.js](../nodejs/README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript
- [🤖 AutoIt](./README.md) - Windows-native | Windows-native | Windows nativo ⭐ **Hier**
- [💻 PowerShell](../powershell/README.md) - Windows-Scripting | Windows Scripting | Scripting Windows
- [⚙️ C/C++](../cpp/README.md) - Native Performance | Native Performance | Rendimiento nativo
- [🐘 PHP](../php/README.md) - Server Cronjobs | Server Cronjobs | Cronjobs servidor
- [💼 COBOL](../cobol/README.md) - Legacy & Mainframe | Legacy & Mainframe | Legacy y Mainframe

### Hauptdokumentation | Main Documentation | Documentación Principal

- [🏠 Hauptseite](../README.md) | [Main Page](../README.en.md) | [Página Principal](../README.es.md)
- [📖 Installationsanleitung](../docs/INSTALL.de.md) | [Installation Guide](../docs/INSTALL.en.md) | [Guía de Instalación](../docs/INSTALL.es.md)
- [🧪 Test-Anleitung](../docs/TEST.de.md) | [Test Guide](../docs/TEST.en.md) | [Guía de Pruebas](../docs/TEST.es.md)

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

## 🇬🇧 English

### ⚠️ IMPORTANT: Windows Only

The AutoIt variant runs **ONLY on Windows**. For Linux/macOS, use the Python, Go, or Node.js variant.

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [AutoIt Installation](#autoit-installation-1)
3. [JSON Libraries](#json-libraries)
4. [External Dependencies](#external-dependencies)
5. [Compilation](#compilation)
6. [Configuration](#configuration)
7. [Usage](#usage)
8. [Troubleshooting](#troubleshooting)
9. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Windows** | Windows 7 SP1+ | Windows 10/11 | x86, x64 |

#### Required Software

1. **AutoIt**
   - **Minimum Version**: 3.3.14.0+
   - **Recommended Version**: 3.3.16.1+ (latest stable version)
   - **Download**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

2. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **WinSCP** (Optional, but recommended)
   - **Minimum Version**: 5.19+
   - **Recommended Version**: 6.x+ (latest version)
   - **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

4. **External Tools** (optional, depending on protocol):
   - **lftp**: For FTP/SFTP (via Git Bash or WSL)
   - **Native Windows SMB**: For SMB/CIFS network shares (already integrated)

---

### 🤖 AutoIt Installation

#### Windows

##### Installer Download (Recommended)

1. **Download**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)
2. **Choose**: AutoIt Full Installation (not just AutoIt3.exe)
3. **Recommended**: "AutoIt Full Installation" with SciTE Editor
4. **Run installer**: Follow the instructions
5. **IMPORTANT**: Ensure AutoIt is in PATH (usually automatic)

##### Verification

```powershell
# PowerShell or CMD
AutoIt3.exe /version
# Should show: AutoIt v3.3.x.x

# Also check SciTE Editor (if installed)
# Start SciTE Editor
```

##### Chocolatey (Alternative)

```powershell
# Install Chocolatey (if not present)
# See: https://chocolatey.org/install

# Install AutoIt
choco install autoit

# Verify
AutoIt3.exe /version
```

**Link**: [Chocolatey AutoIt Package](https://community.chocolatey.org/packages/autoit)

##### SciTE Editor (Recommended)

SciTE is an editor specifically for AutoIt scripts with:
- Syntax highlighting
- Auto-completion
- Compilation with F7
- Error display

**Installation**: Usually installed with AutoIt Full Installation.

**Alternative**: [SciTE Standalone](https://www.scintilla.org/SciTEDownload.html)

---

### 📦 JSON Libraries

The AutoIt variant requires JSON libraries for parsing `config.json`.

#### ✅ Included Libraries

**IMPORTANT**: The required files are **already included in the repository**!

- **Json.au3** (Version 2021.11.20)
- **BinaryCall.au3** (Version 2014.7.24)

**Location**: `autoit/Json.au3` and `autoit/BinaryCall.au3`

#### Verification

```powershell
# Check if files are present
dir autoit\Json.au3
dir autoit\BinaryCall.au3
```

**Note**: Both files must be in the same directory as `sync.au3` to be correctly included.

#### Library Details

##### Json.au3

- **Version**: 2021.11.20 (November 20, 2021)
- **Developer**: Ward
- **Dependency**: BinaryCall.au3
- **Functions**: Json_Decode(), Json_Get(), Json_Put()
- **Link**: [AutoIt Forum Topic #148114](https://www.autoitscript.com/forum/topic/148114-a-non-strict-json-udf-jsmn/)

##### BinaryCall.au3

- **Version**: 2014.7.24 (July 24, 2014)
- **Developer**: Ward
- **Purpose**: Base utility for binary operations
- **Required by**: Json.au3

**Status**: Both libraries are functional and tested. See `autoit/DEPENDENCIES.md` for details.

---

### 📦 External Dependencies

#### 1. KeePassXC-CLI (REQUIRED)

**Purpose**: For merging KeePass databases

##### Windows Installation

1. **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. **Choose**: Windows Installer (.msi)
3. **Install**: Follow the instructions
4. **IMPORTANT**: Ensure `keepassxc-cli.exe` is in PATH

##### Verification

```powershell
# PowerShell or CMD
keepassxc-cli version
# Should show version: 2.7.x or similar

# Or full path
"C:\Program Files\KeePassXC\keepassxc-cli.exe" --version
```

**Links**:
- **Official Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)
- **Documentation**: [https://keepassxc.org/docs/](https://keepassxc.org/docs/)

**PATH Setting** (if needed):

```powershell
# Add KeePassXC to PATH
# Control Panel → Environment Variables → PATH
# Add: C:\Program Files\KeePassXC\
```

#### 2. WinSCP (For FTP/SFTP - RECOMMENDED)

**Purpose**: File transfers via FTP and SFTP on Windows

##### Windows Installation

1. **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)
2. **Choose**: Windows Installer
3. **IMPORTANT**: Choose "Portable" or "Installation" with "WinSCP.com" (Command-Line Tool)
4. **Install**: Follow the instructions
5. **Verify**: `WinSCP.com` should be in PATH

##### Verification

```powershell
# PowerShell or CMD
WinSCP.com /version
# Should show version
```

**Standard Path**:
- Installation: `C:\Program Files (x86)\WinSCP\WinSCP.com`
- Portable: `C:\Path\to\WinSCP\WinSCP.com`

##### Alternative: lftp (via Git Bash / WSL)

If WinSCP should not be installed:

**Option 1: Git Bash**

```bash
# In Git Bash
# lftp should be available or installable
```

**Option 2: WSL (Windows Subsystem for Linux)**

```bash
# In WSL
sudo apt install lftp
```

**Links**:
- **WinSCP**: [https://winscp.net/eng/index.php](https://winscp.net/eng/index.php)
- **WinSCP Documentation**: [https://winscp.net/eng/docs/start](https://winscp.net/eng/docs/start)

#### 3. Native Windows SMB (For SMB/CIFS - Already Present)

**Purpose**: Access to Windows network shares

Windows has native SMB support via `net use` and UNC paths. No additional installation required.

**Tools Used**:
- `net use` - Windows command-line tool for network shares
- UNC paths (`\\server\share`)

---

### 🔨 Compilation

#### Step-by-Step Guide

##### 1. Clone repository or download files

```powershell
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync\autoit

# Option 2: Download ZIP
# Extract ZIP file and navigate to autoit/ directory
```

##### 2. Verify AutoIt installation

```powershell
AutoIt3.exe /version
```

##### 3. Verify JSON libraries

```powershell
# Ensure these files are present:
dir Json.au3
dir BinaryCall.au3
dir sync.au3
```

##### 4. Compile the script

**Method 1: AutoIt3 Compiler (Command Line)**

```powershell
# Navigate to autoit directory
cd autoit

# Compile
AutoIt3.exe /in sync.au3 /out sync.exe

# Verify
dir sync.exe
```

**Method 2: SciTE Editor (Recommended)**

1. Open `sync.au3` in SciTE Editor
2. Press **F7** (or Tools → Compile)
3. The compiled `sync.exe` will be created

**Method 3: Compilation with compiler directives**

```powershell
# With icon (optional)
AutoIt3.exe /in sync.au3 /out sync.exe /icon icon.ico

# Without console window (for GUI scripts)
AutoIt3.exe /in sync.au3 /out sync.exe /nopack
```

##### 5. Test the compiled EXE

```powershell
.\sync.exe --version
# Should show: KeePass Sync 1.1.0 (AutoIt)
```

---

### ⚙️ Configuration

#### 1. Create config.json

```powershell
# Navigate to main directory (one level up)
cd ..

# Copy example config
copy config.example.json config.json

# Edit config.json
notepad config.json  # Or use another editor
```

**Important settings**:

```json
{
  "ftp": {
    "host": "your-server.com",
    "user": "your-username",
    "password": "your-password",
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
    "databasePassword": "your-keepass-master-password",
    "keepassXCPath": "keepassxc-cli"
  },
  "settings": {
    "debug": false,
    "language": "en",
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

**Note**: The AutoIt variant currently does **not support SCP**. Use SFTP instead.

---

### 💻 Usage

#### Basic Commands

```powershell
# Normal synchronization
.\sync.exe

# Test connection (without sync)
.\sync.exe --test

# Show status
.\sync.exe --status

# Alternative config file
.\sync.exe --config "C:\Path\to\config.json"

# Show version
.\sync.exe --version
```

#### As .au3 Script (without compilation)

```powershell
# Run directly as script
AutoIt3.exe sync.au3

# With arguments
AutoIt3.exe sync.au3 --test
```

#### Automation

##### Task Scheduler (Windows)

1. **Open Task Scheduler** (taskschd.msc)
2. **Create new task**
3. **General**:
   - Name: `KeePass Sync`
   - Run as: Your user
   - "Run whether user is logged on or not" (optional)
4. **Triggers**:
   - New → Schedule
   - Repeat: Daily/Hourly/etc.
5. **Actions**:
   - Action: Start program
   - Program: `C:\Path\to\sync.exe`
   - Arguments: (empty for normal sync)
6. **Save**

**Example: Hourly**

```
Trigger: Repeat every: 1 hour
Action: C:\Tools\KeePass Sync\autoit\sync.exe
```

---

### 🔍 Troubleshooting

#### "AutoIt3.exe: command not found"

**Problem**: AutoIt is not installed or not in PATH

**Solution**:
```powershell
# Check installation
where AutoIt3.exe

# If not found, install AutoIt (see above)
# Or add to PATH:
# Control Panel → Environment Variables → PATH
# Add: C:\Program Files (x86)\AutoIt3\
```

#### "Json.au3 not found" or "BinaryCall.au3 not found"

**Problem**: JSON libraries are missing

**Solution**:
```powershell
# Files should already be in autoit/ directory
dir autoit\Json.au3
dir autoit\BinaryCall.au3

# If missing, ensure they are in the same directory as sync.au3
# Copy from repository if needed
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI is not installed or not in PATH

**Solution**:
```powershell
# Install KeePassXC (see above)
# Verify installation
keepassxc-cli version

# If not found, add to PATH:
# C:\Program Files\KeePassXC\
```

#### "WinSCP.com not found"

**Problem**: WinSCP is not installed or not in PATH

**Solution**:
```powershell
# Install WinSCP (see above)
# Verify installation
WinSCP.com /version

# If not found, add to PATH:
# C:\Program Files (x86)\WinSCP\
```

**Alternative**: Use lftp via Git Bash or WSL

#### Compilation errors

**Problem**: Error during compilation

**Solution**:
```powershell
# Check script for syntax errors
# Open in SciTE Editor for better error display

# Check all includes
# Ensure Json.au3 and BinaryCall.au3 are present
```

#### "SCP not supported"

**Note**: The AutoIt variant currently does not support the SCP protocol.

**Solution**: Use SFTP instead (works with WinSCP or lftp).

---

### 🙏 Acknowledgments

#### AutoIt

- **Developer**: AutoIt Team
- **Website**: [https://www.autoitscript.com/](https://www.autoitscript.com/)
- **License**: Freeware (closed source)
- **Download**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

#### SciTE Editor

- **Developer**: Neil Hodgson
- **Website**: [https://www.scintilla.org/SciTE.html](https://www.scintilla.org/SciTE.html)
- **License**: Historical Permission Notice and Disclaimer
- **Download**: [https://www.scintilla.org/SciTEDownload.html](https://www.scintilla.org/SciTEDownload.html)

#### Json.au3

- **Developer**: Ward
- **Version**: 2021.11.20
- **AutoIt Forum**: [Topic #148114](https://www.autoitscript.com/forum/topic/148114-a-non-strict-json-udf-jsmn/)
- **License**: (see file header)

#### BinaryCall.au3

- **Developer**: Ward
- **Version**: 2014.7.24
- **License**: (see file header)

#### KeePassXC

- **Developer**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **License**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### WinSCP

- **Developer**: Martin Přikryl
- **Website**: [https://winscp.net/](https://winscp.net/)
- **License**: GPL
- **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

---

## 🇪🇸 Español

### ⚠️ IMPORTANTE: Solo Windows

La variante AutoIt funciona **SOLO en Windows**. Para Linux/macOS, usa la variante Python, Go o Node.js.

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de AutoIt](#instalación-de-autoit)
3. [Bibliotecas JSON](#bibliotecas-json)
4. [Dependencias Externas](#dependencias-externas)
5. [Compilación](#compilación)
6. [Configuración](#configuración)
7. [Uso](#uso)
8. [Solución de Problemas](#solución-de-problemas)
9. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Windows** | Windows 7 SP1+ | Windows 10/11 | x86, x64 |

#### Software Requerido

1. **AutoIt**
   - **Versión Mínima**: 3.3.14.0+
   - **Versión Recomendada**: 3.3.16.1+ (última versión estable)
   - **Descarga**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

2. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **WinSCP** (Opcional, pero recomendado)
   - **Versión Mínima**: 5.19+
   - **Versión Recomendada**: 6.x+ (última versión)
   - **Descarga**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

4. **Herramientas Externas** (opcional, según el protocolo):
   - **lftp**: Para FTP/SFTP (vía Git Bash o WSL)
   - **SMB Nativo de Windows**: Para recursos compartidos de red SMB/CIFS (ya integrado)

---

### 🤖 Instalación de AutoIt

#### Windows

##### Descarga del Instalador (Recomendado)

1. **Descarga**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)
2. **Elige**: AutoIt Full Installation (no solo AutoIt3.exe)
3. **Recomendado**: "AutoIt Full Installation" con Editor SciTE
4. **Ejecuta el instalador**: Sigue las instrucciones
5. **IMPORTANTE**: Asegúrate de que AutoIt esté en PATH (normalmente automático)

##### Verificación

```powershell
# PowerShell o CMD
AutoIt3.exe /version
# Debería mostrar: AutoIt v3.3.x.x

# También verifica el Editor SciTE (si está instalado)
# Inicia el Editor SciTE
```

##### Chocolatey (Alternativa)

```powershell
# Instalar Chocolatey (si no está presente)
# Ver: https://chocolatey.org/install

# Instalar AutoIt
choco install autoit

# Verificar
AutoIt3.exe /version
```

**Enlace**: [Chocolatey AutoIt Package](https://community.chocolatey.org/packages/autoit)

##### Editor SciTE (Recomendado)

SciTE es un editor específico para scripts AutoIt con:
- Resaltado de sintaxis
- Autocompletado
- Compilación con F7
- Visualización de errores

**Instalación**: Normalmente se instala con AutoIt Full Installation.

**Alternativa**: [SciTE Standalone](https://www.scintilla.org/SciTEDownload.html)

---

### 📦 Bibliotecas JSON

La variante AutoIt requiere bibliotecas JSON para analizar `config.json`.

#### ✅ Bibliotecas Incluidas

**IMPORTANTE**: ¡Los archivos necesarios **ya están incluidos en el repositorio**!

- **Json.au3** (Versión 2021.11.20)
- **BinaryCall.au3** (Versión 2014.7.24)

**Ubicación**: `autoit/Json.au3` y `autoit/BinaryCall.au3`

#### Verificación

```powershell
# Verificar si los archivos están presentes
dir autoit\Json.au3
dir autoit\BinaryCall.au3
```

**Nota**: Ambos archivos deben estar en el mismo directorio que `sync.au3` para ser incluidos correctamente.

#### Detalles de las Bibliotecas

##### Json.au3

- **Versión**: 2021.11.20 (20 de noviembre de 2021)
- **Desarrollador**: Ward
- **Dependencia**: BinaryCall.au3
- **Funciones**: Json_Decode(), Json_Get(), Json_Put()
- **Enlace**: [AutoIt Forum Topic #148114](https://www.autoitscript.com/forum/topic/148114-a-non-strict-json-udf-jsmn/)

##### BinaryCall.au3

- **Versión**: 2014.7.24 (24 de julio de 2014)
- **Desarrollador**: Ward
- **Propósito**: Utilidad base para operaciones binarias
- **Requerido por**: Json.au3

**Estado**: Ambas bibliotecas son funcionales y probadas. Ver `autoit/DEPENDENCIES.md` para detalles.

---

### 📦 Dependencias Externas

#### 1. KeePassXC-CLI (REQUERIDO)

**Propósito**: Para fusionar bases de datos KeePass

##### Instalación en Windows

1. **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. **Elige**: Instalador Windows (.msi)
3. **Instala**: Sigue las instrucciones
4. **IMPORTANTE**: Asegúrate de que `keepassxc-cli.exe` esté en PATH

##### Verificación

```powershell
# PowerShell o CMD
keepassxc-cli version
# Debería mostrar versión: 2.7.x o similar

# O ruta completa
"C:\Program Files\KeePassXC\keepassxc-cli.exe" --version
```

**Enlaces**:
- **Sitio Web Oficial**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)
- **Documentación**: [https://keepassxc.org/docs/](https://keepassxc.org/docs/)

**Configuración PATH** (si es necesario):

```powershell
# Añadir KeePassXC a PATH
# Panel de Control → Variables de Entorno → PATH
# Añadir: C:\Program Files\KeePassXC\
```

#### 2. WinSCP (Para FTP/SFTP - RECOMENDADO)

**Propósito**: Transferencias de archivos vía FTP y SFTP en Windows

##### Instalación en Windows

1. **Descarga**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)
2. **Elige**: Instalador Windows
3. **IMPORTANTE**: Elige "Portable" o "Installation" con "WinSCP.com" (Herramienta de Línea de Comandos)
4. **Instala**: Sigue las instrucciones
5. **Verifica**: `WinSCP.com` debería estar en PATH

##### Verificación

```powershell
# PowerShell o CMD
WinSCP.com /version
# Debería mostrar versión
```

**Ruta Estándar**:
- Instalación: `C:\Program Files (x86)\WinSCP\WinSCP.com`
- Portable: `C:\Ruta\a\WinSCP\WinSCP.com`

##### Alternativa: lftp (vía Git Bash / WSL)

Si no se desea instalar WinSCP:

**Opción 1: Git Bash**

```bash
# En Git Bash
# lftp debería estar disponible o ser instalable
```

**Opción 2: WSL (Subsistema de Windows para Linux)**

```bash
# En WSL
sudo apt install lftp
```

**Enlaces**:
- **WinSCP**: [https://winscp.net/eng/index.php](https://winscp.net/eng/index.php)
- **Documentación WinSCP**: [https://winscp.net/eng/docs/start](https://winscp.net/eng/docs/start)

#### 3. SMB Nativo de Windows (Para SMB/CIFS - Ya Presente)

**Propósito**: Acceso a recursos compartidos de red Windows

Windows tiene soporte SMB nativo vía `net use` y rutas UNC. No se requiere instalación adicional.

**Herramientas Utilizadas**:
- `net use` - Herramienta de línea de comandos de Windows para recursos compartidos de red
- Rutas UNC (`\\server\share`)

---

### 🔨 Compilación

#### Guía Paso a Paso

##### 1. Clonar repositorio o descargar archivos

```powershell
# Opción 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync\autoit

# Opción 2: Descargar ZIP
# Extraer archivo ZIP y navegar al directorio autoit/
```

##### 2. Verificar instalación de AutoIt

```powershell
AutoIt3.exe /version
```

##### 3. Verificar bibliotecas JSON

```powershell
# Asegúrate de que estos archivos estén presentes:
dir Json.au3
dir BinaryCall.au3
dir sync.au3
```

##### 4. Compilar el script

**Método 1: Compilador AutoIt3 (Línea de Comandos)**

```powershell
# Navegar al directorio autoit
cd autoit

# Compilar
AutoIt3.exe /in sync.au3 /out sync.exe

# Verificar
dir sync.exe
```

**Método 2: Editor SciTE (Recomendado)**

1. Abre `sync.au3` en el Editor SciTE
2. Presiona **F7** (o Herramientas → Compilar)
3. Se creará el `sync.exe` compilado

**Método 3: Compilación con directivas del compilador**

```powershell
# Con icono (opcional)
AutoIt3.exe /in sync.au3 /out sync.exe /icon icon.ico

# Sin ventana de consola (para scripts GUI)
AutoIt3.exe /in sync.au3 /out sync.exe /nopack
```

##### 5. Probar el EXE compilado

```powershell
.\sync.exe --version
# Debería mostrar: KeePass Sync 1.1.0 (AutoIt)
```

---

### ⚙️ Configuración

#### 1. Crear config.json

```powershell
# Navegar al directorio principal (un nivel arriba)
cd ..

# Copiar config de ejemplo
copy config.example.json config.json

# Editar config.json
notepad config.json  # O usar otro editor
```

**Configuraciones importantes**:

```json
{
  "ftp": {
    "host": "tu-servidor.com",
    "user": "tu-usuario",
    "password": "tu-contraseña",
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
    "databasePassword": "tu-contraseña-maestra-keepass",
    "keepassXCPath": "keepassxc-cli"
  },
  "settings": {
    "debug": false,
    "language": "es",
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

**Nota**: La variante AutoIt actualmente **no admite SCP**. Usa SFTP en su lugar.

---

### 💻 Uso

#### Comandos Básicos

```powershell
# Sincronización normal
.\sync.exe

# Probar conexión (sin sincronizar)
.\sync.exe --test

# Mostrar estado
.\sync.exe --status

# Archivo de configuración alternativo
.\sync.exe --config "C:\Ruta\a\config.json"

# Mostrar versión
.\sync.exe --version
```

#### Como Script .au3 (sin compilación)

```powershell
# Ejecutar directamente como script
AutoIt3.exe sync.au3

# Con argumentos
AutoIt3.exe sync.au3 --test
```

#### Automatización

##### Programador de Tareas (Windows)

1. **Abrir Programador de Tareas** (taskschd.msc)
2. **Crear nueva tarea**
3. **General**:
   - Nombre: `KeePass Sync`
   - Ejecutar como: Tu usuario
   - "Ejecutar independientemente de si el usuario ha iniciado sesión o no" (opcional)
4. **Desencadenadores**:
   - Nuevo → Programación
   - Repetir: Diario/Horario/etc.
5. **Acciones**:
   - Acción: Iniciar programa
   - Programa: `C:\Ruta\a\sync.exe`
   - Argumentos: (vacío para sincronización normal)
6. **Guardar**

**Ejemplo: Cada hora**

```
Desencadenador: Repetir cada: 1 hora
Acción: C:\Tools\KeePass Sync\autoit\sync.exe
```

---

### 🔍 Solución de Problemas

#### "AutoIt3.exe: command not found"

**Problema**: AutoIt no está instalado o no está en PATH

**Solución**:
```powershell
# Verificar instalación
where AutoIt3.exe

# Si no se encuentra, instala AutoIt (ver arriba)
# O añade a PATH:
# Panel de Control → Variables de Entorno → PATH
# Añade: C:\Program Files (x86)\AutoIt3\
```

#### "Json.au3 no encontrado" o "BinaryCall.au3 no encontrado"

**Problema**: Faltan bibliotecas JSON

**Solución**:
```powershell
# Los archivos deberían estar ya en el directorio autoit/
dir autoit\Json.au3
dir autoit\BinaryCall.au3

# Si faltan, asegúrate de que estén en el mismo directorio que sync.au3
# Copia del repositorio si es necesario
```

#### "keepassxc-cli: command not found"

**Problema**: KeePassXC-CLI no está instalado o no está en PATH

**Solución**:
```powershell
# Instala KeePassXC (ver arriba)
# Verificar instalación
keepassxc-cli version

# Si no se encuentra, añade a PATH:
# C:\Program Files\KeePassXC\
```

#### "WinSCP.com no encontrado"

**Problema**: WinSCP no está instalado o no está en PATH

**Solución**:
```powershell
# Instala WinSCP (ver arriba)
# Verificar instalación
WinSCP.com /version

# Si no se encuentra, añade a PATH:
# C:\Program Files (x86)\WinSCP\
```

**Alternativa**: Usa lftp vía Git Bash o WSL

#### Errores de compilación

**Problema**: Error durante la compilación

**Solución**:
```powershell
# Verificar script por errores de sintaxis
# Abre en Editor SciTE para mejor visualización de errores

# Verifica todos los includes
# Asegúrate de que Json.au3 y BinaryCall.au3 estén presentes
```

#### "SCP no soportado"

**Nota**: La variante AutoIt actualmente no admite el protocolo SCP.

**Solución**: Usa SFTP en su lugar (funciona con WinSCP o lftp).

---

### 🙏 Agradecimientos

#### AutoIt

- **Desarrollador**: Equipo AutoIt
- **Sitio Web**: [https://www.autoitscript.com/](https://www.autoitscript.com/)
- **Licencia**: Freeware (código cerrado)
- **Descarga**: [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

#### Editor SciTE

- **Desarrollador**: Neil Hodgson
- **Sitio Web**: [https://www.scintilla.org/SciTE.html](https://www.scintilla.org/SciTE.html)
- **Licencia**: Historical Permission Notice and Disclaimer
- **Descarga**: [https://www.scintilla.org/SciTEDownload.html](https://www.scintilla.org/SciTEDownload.html)

#### Json.au3

- **Desarrollador**: Ward
- **Versión**: 2021.11.20
- **AutoIt Forum**: [Topic #148114](https://www.autoitscript.com/forum/topic/148114-a-non-strict-json-udf-jsmn/)
- **Licencia**: (ver encabezado del archivo)

#### BinaryCall.au3

- **Desarrollador**: Ward
- **Versión**: 2014.7.24
- **Licencia**: (ver encabezado del archivo)

#### KeePassXC

- **Desarrollador**: Equipo de KeePassXC
- **Sitio Web**: [https://keepassxc.org/](https://keepassxc.org/)
- **Licencia**: GPL-2.0 / GPL-3.0
- **Repositorio**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### WinSCP

- **Desarrollador**: Martin Přikryl
- **Sitio Web**: [https://winscp.net/](https://winscp.net/)
- **Licencia**: GPL
- **Descarga**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

---

<div align="center">

**🤖 AutoIt-Variante: Windows-native, GUI-fähig, keine Runtime nötig**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>
