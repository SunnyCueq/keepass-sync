# 💼 KeePass Sync - COBOL Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![COBOL](https://img.shields.io/badge/COBOL-GnuCOBOL%202.0+-FF6A00.svg)](https://gnucobol.sourceforge.io/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Mainframe-lightgrey.svg)](.)

> **Legacy & Mainframe Support - Für Enterprise-Umgebungen**

</div>

---

## ⚠️ HINWEIS: Spezielle Zielgruppe

Die COBOL-Variante ist primär für **Mainframe- und Legacy-Systeme** gedacht. Für moderne Systeme empfohlen: **Python**, **Go** oder **Node.js**.

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
- [📦 Node.js](../nodejs/README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript
- [🤖 AutoIt](../autoit/README.md) - Windows-native | Windows-native | Windows nativo
- [💻 PowerShell](../powershell/README.md) - Windows-Scripting | Windows Scripting | Scripting Windows
- [⚙️ C/C++](../cpp/README.md) - Native Performance | Native Performance | Rendimiento nativo
- [🐘 PHP](../php/README.md) - Server Cronjobs | Server Cronjobs | Cronjobs servidor
- [💼 COBOL](./README.md) - Legacy & Mainframe | Legacy & Mainframe | Legacy y Mainframe ⭐ **Hier**

### Hauptdokumentation | Main Documentation | Documentación Principal

- [🏠 Hauptseite](../README.md) | [Main Page](../README.en.md) | [Página Principal](../README.es.md)
- [📖 Installationsanleitung](../docs/INSTALL.de.md) | [Installation Guide](../docs/INSTALL.en.md) | [Guía de Instalación](../docs/INSTALL.es.md)
- [🧪 Test-Anleitung](../docs/TEST.de.md) | [Test Guide](../docs/TEST.en.md) | [Guía de Pruebas](../docs/TEST.es.md)

---

## 🇩🇪 Deutsch

### ⚠️ WICHTIG: Basis-Implementierung

Die COBOL-Variante ist eine **Basis-Implementierung** für Mainframe- und Legacy-Systeme. Für Produktionsnutzung sollten spezifische Anpassungen für die Zielumgebung vorgenommen werden.

### 📋 Inhaltsverzeichnis

1. [Systemanforderungen](#systemanforderungen)
2. [GnuCOBOL Installation](#gnucobol-installation)
3. [Externe Dependencies](#externe-dependencies)
4. [Kompilierung](#kompilierung)
5. [Konfiguration](#konfiguration)
6. [Verwendung](#verwendung)
7. [Mainframe-Besonderheiten](#mainframe-besonderheiten)
8. [Fehlerbehebung](#fehlerbehebung)
9. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Linux** | Alle modernen Distributionen | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64, z/Architecture |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **Mainframe** | z/OS, OS/390, MVS | z/OS 2.3+ | z/Architecture |

#### Erforderliche Software

1. **GnuCOBOL** (früher OpenCOBOL)
   - **Minimale Version**: 2.0+
   - **Empfohlene Version**: 3.1+ (aktuellste Version)
   - **Download**: [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
   - **Mainframe**: IBM Enterprise COBOL für z/OS (kommerziell)

2. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
   - **Mainframe**: Kann über USS (Unix System Services) installiert werden

3. **Externe Tools** (abhängig vom Protokoll):
   - **lftp**: Für FTP/SFTP-Übertragungen
   - **smbclient**: Für SMB/CIFS-Netzwerk-Shares
   - **sshpass** & **scp**: Für SCP-Übertragungen

---

### 💼 GnuCOBOL Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Installiere GnuCOBOL
sudo pacman -S gnucobol

# Überprüfe die Installation
cobc --version
# Sollte zeigen: cobc 3.1.x oder ähnlich
```

**Paketname**: `gnucobol`  
**Repository**: Community  
**Link**: [Arch Linux GnuCOBOL Package](https://archlinux.org/packages/community/x86_64/gnucobol/)

##### Debian / Ubuntu

```bash
# Aktualisiere Paketliste
sudo apt update

# Installiere GnuCOBOL
sudo apt install open-cobol  # Oder gnucobol

# Überprüfe
cobc --version
```

**Paketnamen**:
- `open-cobol` - GnuCOBOL (alter Name)
- `gnucobol` - GnuCOBOL (neuer Name)

**Repository**: Universe  
**Link**: [Debian GnuCOBOL Package](https://packages.debian.org/gnucobol)

**Alternative: Aus Quellen kompilieren**

```bash
# Download
wget https://sourceforge.net/projects/gnucobol/files/gnucobol/3.1/gnucobol-3.1.tar.xz/download

# Kompiliere
tar -xf gnucobol-3.1.tar.xz
cd gnucobol-3.1
./configure
make
sudo make install
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install gnucobol
```

##### openSUSE

```bash
sudo zypper install open-cobol
```

#### macOS

##### Homebrew (Empfohlen)

```bash
# Installiere Homebrew (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installiere GnuCOBOL
brew install gnucobol

# Überprüfe
cobc --version
```

**Link**: [Homebrew GnuCOBOL Formula](https://formulae.brew.sh/formula/gnucobol)

##### MacPorts (Alternative)

```bash
sudo port install gnucobol
```

#### Windows

##### Cygwin / MSYS2

```bash
# In MSYS2 Terminal
pacman -S mingw-w64-x86_64-gnucobol

# Füge zu PATH hinzu: C:\msys64\mingw64\bin
```

##### Manueller Download

1. **Download**: [https://sourceforge.net/projects/gnucobol/](https://sourceforge.net/projects/gnucobol/)
2. **Wähle**: Windows Build
3. **Installiere**: Folgen Sie den Anweisungen
4. **Füge zu PATH hinzu**: `C:\Program Files\GnuCOBOL\bin`

#### Mainframe (z/OS)

**IBM Enterprise COBOL** (kommerziell):

1. **Lizenz**: Erfordert IBM-Lizenz
2. **Installation**: Über SMP/E oder andere IBM-Installationsmethoden
3. **Compiler**: `igyc` (IBM Enterprise COBOL)

**GnuCOBOL via USS**:

1. **USS (Unix System Services)** muss aktiviert sein
2. **Installiere**: GnuCOBOL aus Quellen (siehe Linux-Anleitung)
3. **Compiler**: `cobc`

**Links**:
- **IBM Enterprise COBOL**: [IBM Documentation](https://www.ibm.com/docs/en/cobol-zos)
- **z/OS Unix System Services**: [IBM z/OS USS](https://www.ibm.com/docs/en/zos/2.4.0?topic=system-zos-unix-system-services)

---

### 📦 Externe Dependencies

#### 1. KeePassXC-CLI (ERFORDERLICH)

**Zweck**: Zum Mergen der KeePass-Datenbanken

##### Linux

```bash
# Debian/Ubuntu
sudo apt install keepassxc

# Arch/CachyOS
sudo pacman -S keepassxc

# Fedora
sudo dnf install keepassxc
```

**Überprüfung**:
```bash
keepassxc-cli version
```

**Links**:
- **Offizielle Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

##### Mainframe (z/OS)

**Via USS (Unix System Services)**:

```bash
# In USS Shell
# Installiere über Portage oder kompiliere aus Quellen
# Siehe: https://keepassxc.org/download/
```

#### 2. lftp (Für FTP/SFTP - EMPFOHLEN)

**Zweck**: Datei-Übertragungen via FTP und SFTP

##### Linux

```bash
# Debian/Ubuntu
sudo apt install lftp

# Arch/CachyOS
sudo pacman -S lftp

# Fedora
sudo dnf install lftp
```

**Links**:
- **lftp**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### Mainframe

**FTP ist nativ in z/OS verfügbar**:

```bash
# z/OS FTP Client
ftp hostname
```

**SFTP**: Kann über USS installiert werden.

#### 3. smbclient (Für SMB/CIFS - Optional)

**Zweck**: Zugriff auf Windows-Netzwerk-Shares

##### Linux

```bash
# Debian/Ubuntu
sudo apt install smbclient

# Arch/CachyOS
sudo pacman -S samba
```

**Mainframe**: SMB/CIFS über USS möglich.

---

### 🔨 Kompilierung

#### Linux / macOS

##### Mit Makefile (Empfohlen)

```bash
cd cobol

# Kompiliere
make

# Überprüfe
./keepass-sync --version  # Falls implementiert
```

##### Manuell

```bash
cd cobol

# Kompiliere
cobc -x sync.cbl -o keepass-sync

# Überprüfe
file keepass-sync
# Sollte zeigen: ELF executable
```

##### Mit Debug-Informationen

```bash
cobc -x -g sync.cbl -o keepass-sync
```

#### Windows

##### MSYS2 / MinGW

```bash
# In MSYS2 Terminal
cd cobol
cobc -x sync.cbl -o keepass-sync.exe
```

#### Mainframe (z/OS)

##### IBM Enterprise COBOL

```bash
# JCL oder TSO
IGYC INPUT=sync.cbl,LIBRARY=SYSLIB,OUTPUT=keepass-sync
```

##### GnuCOBOL (USS)

```bash
# In USS Shell
cd cobol
cobc -x sync.cbl -o keepass-sync
```

---

### ⚙️ Konfiguration

**WICHTIG**: Die COBOL-Variante verwendet eine **vereinfachte Konfiguration**. JSON-Parsing erfordert externe Tools oder Bibliotheken.

#### Option 1: Externes JSON-Tool

```bash
# Verwende jq oder Python-Script zur Config-Erstellung
python3 -c "import json; print(json.load(open('config.json'))['ftp']['host'])"
```

#### Option 2: Hardcoded im Programm

Editiere `sync.cbl` und setze Werte direkt:

```cobol
MOVE "dein-server.com" TO WS-CONFIG-HOST
MOVE "dein-benutzername" TO WS-CONFIG-USER
MOVE "dein-passwort" TO WS-CONFIG-PASSWORD
MOVE "/keepass_passwords.kdbx" TO WS-CONFIG-REMOTE
MOVE "ftp" TO WS-CONFIG-PROTOCOL
```

#### Option 3: Umgebungsvariablen

```bash
export KEEPASS_HOST="dein-server.com"
export KEEPASS_USER="dein-benutzername"
export KEEPASS_PASSWORD="dein-passwort"
```

**Im Programm lesen**:
```cobol
ACCEPT WS-CONFIG-HOST FROM ENVIRONMENT "KEEPASS_HOST"
ACCEPT WS-CONFIG-USER FROM ENVIRONMENT "KEEPASS_USER"
ACCEPT WS-CONFIG-PASSWORD FROM ENVIRONMENT "KEEPASS_PASSWORD"
```

---

### 💻 Verwendung

#### Linux / macOS

```bash
cd cobol

# Kompiliertes Programm ausführen
./keepass-sync

# Mit Logging
./keepass-sync >> sync_log.txt 2>&1
```

#### Windows

```powershell
cd cobol

# Ausführen
.\keepass-sync.exe
```

#### Mainframe (z/OS)

##### TSO / ISPF

```
TSO EXEC cobol/keepass-sync
```

##### USS

```bash
cd cobol
./keepass-sync
```

##### JCL

```jcl
//SYNC    EXEC PGM=KEEPASS-SYNC
//STEPLIB  DD DSN=COBOL.LOADLIB,DISP=SHR
//SYSOUT   DD SYSOUT=*
```

#### Automatisierung

##### Cron (Linux/macOS)

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * cd /pfad/zum/projekt/cobol && ./keepass-sync
```

##### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Zeitplan
4. Aktion: Programm starten
   - Programm: `C:\Pfad\zum\cobol\keepass-sync.exe`

##### z/OS Batch Job

```jcl
//KPSYNC   JOB (ACCT),'KEEPASS SYNC',CLASS=A
//STEP1    EXEC PGM=KEEPASS-SYNC
//STEPLIB  DD DSN=COBOL.LOADLIB,DISP=SHR
//SYSOUT   DD SYSOUT=*
```

---

### 🖥️ Mainframe-Besonderheiten

#### z/OS Unix System Services (USS)

**Pfade**:
- Unix-Pfade: `/u/user1/keepass/`
- VSAM/Dataset: `USER1.KEEPASS.DATA`

**Konvertierung**:
```bash
# Unix zu MVS
/u/user1/keepass/config.json -> USER1.KEEPASS.CONFIG
```

#### Dataset-Organisation

**Sequentiell**: Für Log-Dateien
**Partitioniert**: Für Load-Libraries

#### JCL-Integration

**Parameter-Übergabe**:
```jcl
//SYNC    EXEC PGM=KEEPASS-SYNC,PARM='HOST=server.com'
```

**Im Programm**:
```cobol
ACCEPT WS-CONFIG-HOST FROM COMMAND-LINE
```

#### VSAM-Integration

**VSAM-Datasets** können für Konfiguration verwendet werden:
```cobol
SELECT CONFIG-FILE ASSIGN TO "USER1.KEEPASS.CONFIG"
    ORGANIZATION IS INDEXED
    ACCESS MODE IS SEQUENTIAL
    RECORD KEY IS WS-CONFIG-KEY
```

---

### 🔍 Fehlerbehebung

#### "cobc: command not found"

**Problem**: GnuCOBOL ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Linux
sudo apt install gnucobol  # Debian/Ubuntu
sudo pacman -S gnucobol    # Arch/CachyOS

# macOS
brew install gnucobol

# Überprüfe
which cobc
cobc --version
```

#### Kompilierungsfehler

**Problem**: Syntax-Fehler im COBOL-Code

**Lösung**:
```bash
# Mit Debug-Informationen kompilieren
cobc -x -g -v sync.cbl -o keepass-sync

# Überprüfe Fehlermeldungen
# COBOL ist case-insensitive, aber auf Spalten achten!
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Installiere KeePassXC (siehe oben)
# Überprüfe
which keepassxc-cli
keepassxc-cli version

# Mainframe: Via USS installieren
```

#### JSON-Parsing-Probleme

**Problem**: COBOL hat keine native JSON-Unterstützung

**Lösung**:
- **Option 1**: Verwende externes Tool (`jq`, `python`)
- **Option 2**: Hardcode-Werte im Programm
- **Option 3**: Verwende COBOL-JSON-Bibliothek (falls verfügbar)

#### Mainframe-spezifische Fehler

**Problem**: Dataset nicht gefunden

**Lösung**:
```cobol
* Überprüfe Dataset-Namen und Organisation
SELECT CONFIG-FILE ASSIGN TO "USER1.KEEPASS.CONFIG"
    ORGANIZATION IS SEQUENTIAL
    FILE STATUS IS WS-STATUS.

IF WS-STATUS NOT = "00"
    DISPLAY "ERROR: Dataset not found: " WS-STATUS
    STOP RUN
END-IF.
```

---

### 🙏 Danksagungen

#### GnuCOBOL

- **Entwickler**: GnuCOBOL Project
- **Website**: [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
- **Lizenz**: LGPL 3.0
- **Repository**: [https://sourceforge.net/projects/gnucobol/](https://sourceforge.net/projects/gnucobol/)

#### IBM Enterprise COBOL

- **Entwickler**: IBM
- **Website**: [https://www.ibm.com/products/cobol](https://www.ibm.com/products/cobol)
- **Lizenz**: Proprietär (IBM)

#### COBOL Standard

- **Entwickler**: ISO COBOL Committee
- **Standard**: ISO/IEC 1989:2014 (COBOL 2014)
- **Link**: [ISO/IEC 1989](https://www.iso.org/standard/63139.html)

#### KeePassXC

- **Entwickler**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **Lizenz**: GPL-2.0 / GPL-3.0

---

## 🇬🇧 English

### ⚠️ IMPORTANT: Basic Implementation

The COBOL variant is a **basic implementation** for mainframe and legacy systems. For production use, specific adaptations for the target environment should be made.

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [GnuCOBOL Installation](#gnucobol-installation-1)
3. [External Dependencies](#external-dependencies)
4. [Compilation](#compilation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Mainframe-Specific Features](#mainframe-specific-features)
8. [Troubleshooting](#troubleshooting)
9. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Linux** | All modern distributions | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64, z/Architecture |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **Mainframe** | z/OS, OS/390, MVS | z/OS 2.3+ | z/Architecture |

#### Required Software

1. **GnuCOBOL** (formerly OpenCOBOL)
   - **Minimum Version**: 2.0+
   - **Recommended Version**: 3.1+ (latest version)
   - **Download**: [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
   - **Mainframe**: IBM Enterprise COBOL for z/OS (commercial)

2. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
   - **Mainframe**: Can be installed via USS (Unix System Services)

3. **External Tools** (depending on protocol):
   - **lftp**: For FTP/SFTP transfers
   - **smbclient**: For SMB/CIFS network shares
   - **sshpass** & **scp**: For SCP transfers

---

### 💼 GnuCOBOL Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Install GnuCOBOL
sudo pacman -S gnucobol

# Verify installation
cobc --version
# Should show: cobc 3.1.x or similar
```

**Package name**: `gnucobol`  
**Repository**: Community  
**Link**: [Arch Linux GnuCOBOL Package](https://archlinux.org/packages/community/x86_64/gnucobol/)

##### Debian / Ubuntu

```bash
# Update package list
sudo apt update

# Install GnuCOBOL
sudo apt install open-cobol  # Or gnucobol

# Verify
cobc --version
```

**Package names**:
- `open-cobol` - GnuCOBOL (old name)
- `gnucobol` - GnuCOBOL (new name)

**Repository**: Universe  
**Link**: [Debian GnuCOBOL Package](https://packages.debian.org/gnucobol)

**Alternative: Compile from source**

```bash
# Download
wget https://sourceforge.net/projects/gnucobol/files/gnucobol/3.1/gnucobol-3.1.tar.xz/download

# Compile
tar -xf gnucobol-3.1.tar.xz
cd gnucobol-3.1
./configure
make
sudo make install
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install gnucobol
```

##### openSUSE

```bash
sudo zypper install open-cobol
```

#### macOS

##### Homebrew (Recommended)

```bash
# Install Homebrew (if not present)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install GnuCOBOL
brew install gnucobol

# Verify
cobc --version
```

**Link**: [Homebrew GnuCOBOL Formula](https://formulae.brew.sh/formula/gnucobol)

##### MacPorts (Alternative)

```bash
sudo port install gnucobol
```

#### Windows

##### Cygwin / MSYS2

```bash
# In MSYS2 Terminal
pacman -S mingw-w64-x86_64-gnucobol

# Add to PATH: C:\msys64\mingw64\bin
```

##### Manual Download

1. **Download**: [https://sourceforge.net/projects/gnucobol/](https://sourceforge.net/projects/gnucobol/)
2. **Choose**: Windows Build
3. **Install**: Follow the instructions
4. **Add to PATH**: `C:\Program Files\GnuCOBOL\bin`

#### Mainframe (z/OS)

**IBM Enterprise COBOL** (commercial):

1. **License**: Requires IBM license
2. **Installation**: Via SMP/E or other IBM installation methods
3. **Compiler**: `igyc` (IBM Enterprise COBOL)

**GnuCOBOL via USS**:

1. **USS (Unix System Services)** must be enabled
2. **Install**: GnuCOBOL from source (see Linux instructions)
3. **Compiler**: `cobc`

**Links**:
- **IBM Enterprise COBOL**: [IBM Documentation](https://www.ibm.com/docs/en/cobol-zos)
- **z/OS Unix System Services**: [IBM z/OS USS](https://www.ibm.com/docs/en/zos/2.4.0?topic=system-zos-unix-system-services)

---

### 📦 External Dependencies

#### 1. KeePassXC-CLI (REQUIRED)

**Purpose**: For merging KeePass databases

##### Linux

```bash
# Debian/Ubuntu
sudo apt install keepassxc

# Arch/CachyOS
sudo pacman -S keepassxc

# Fedora
sudo dnf install keepassxc
```

**Verification**:
```bash
keepassxc-cli version
```

**Links**:
- **Official Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

##### Mainframe (z/OS)

**Via USS (Unix System Services)**:

```bash
# In USS Shell
# Install via Portage or compile from source
# See: https://keepassxc.org/download/
```

#### 2. lftp (For FTP/SFTP - RECOMMENDED)

**Purpose**: File transfers via FTP and SFTP

##### Linux

```bash
# Debian/Ubuntu
sudo apt install lftp

# Arch/CachyOS
sudo pacman -S lftp

# Fedora
sudo dnf install lftp
```

**Links**:
- **lftp**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### Mainframe

**FTP is natively available in z/OS**:

```bash
# z/OS FTP Client
ftp hostname
```

**SFTP**: Can be installed via USS.

#### 3. smbclient (For SMB/CIFS - Optional)

**Purpose**: Access to Windows network shares

##### Linux

```bash
# Debian/Ubuntu
sudo apt install smbclient

# Arch/CachyOS
sudo pacman -S samba
```

**Mainframe**: SMB/CIFS possible via USS.

---

### 🔨 Compilation

#### Linux / macOS

##### With Makefile (Recommended)

```bash
cd cobol

# Compile
make

# Verify
./keepass-sync --version  # If implemented
```

##### Manual

```bash
cd cobol

# Compile
cobc -x sync.cbl -o keepass-sync

# Verify
file keepass-sync
# Should show: ELF executable
```

##### With Debug Information

```bash
cobc -x -g sync.cbl -o keepass-sync
```

#### Windows

##### MSYS2 / MinGW

```bash
# In MSYS2 Terminal
cd cobol
cobc -x sync.cbl -o keepass-sync.exe
```

#### Mainframe (z/OS)

##### IBM Enterprise COBOL

```bash
# JCL or TSO
IGYC INPUT=sync.cbl,LIBRARY=SYSLIB,OUTPUT=keepass-sync
```

##### GnuCOBOL (USS)

```bash
# In USS Shell
cd cobol
cobc -x sync.cbl -o keepass-sync
```

---

### ⚙️ Configuration

**IMPORTANT**: The COBOL variant uses a **simplified configuration**. JSON parsing requires external tools or libraries.

#### Option 1: External JSON Tool

```bash
# Use jq or Python script for config creation
python3 -c "import json; print(json.load(open('config.json'))['ftp']['host'])"
```

#### Option 2: Hardcoded in Program

Edit `sync.cbl` and set values directly:

```cobol
MOVE "your-server.com" TO WS-CONFIG-HOST
MOVE "your-username" TO WS-CONFIG-USER
MOVE "your-password" TO WS-CONFIG-PASSWORD
MOVE "/keepass_passwords.kdbx" TO WS-CONFIG-REMOTE
MOVE "ftp" TO WS-CONFIG-PROTOCOL
```

#### Option 3: Environment Variables

```bash
export KEEPASS_HOST="your-server.com"
export KEEPASS_USER="your-username"
export KEEPASS_PASSWORD="your-password"
```

**Read in program**:
```cobol
ACCEPT WS-CONFIG-HOST FROM ENVIRONMENT "KEEPASS_HOST"
ACCEPT WS-CONFIG-USER FROM ENVIRONMENT "KEEPASS_USER"
ACCEPT WS-CONFIG-PASSWORD FROM ENVIRONMENT "KEEPASS_PASSWORD"
```

---

### 💻 Usage

#### Linux / macOS

```bash
cd cobol

# Run compiled program
./keepass-sync

# With logging
./keepass-sync >> sync_log.txt 2>&1
```

#### Windows

```powershell
cd cobol

# Execute
.\keepass-sync.exe
```

#### Mainframe (z/OS)

##### TSO / ISPF

```
TSO EXEC cobol/keepass-sync
```

##### USS

```bash
cd cobol
./keepass-sync
```

##### JCL

```jcl
//SYNC    EXEC PGM=KEEPASS-SYNC
//STEPLIB  DD DSN=COBOL.LOADLIB,DISP=SHR
//SYSOUT   DD SYSOUT=*
```

#### Automation

##### Cron (Linux/macOS)

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * cd /path/to/project/cobol && ./keepass-sync
```

##### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Schedule
4. Action: Start program
   - Program: `C:\Path\to\cobol\keepass-sync.exe`

##### z/OS Batch Job

```jcl
//KPSYNC   JOB (ACCT),'KEEPASS SYNC',CLASS=A
//STEP1    EXEC PGM=KEEPASS-SYNC
//STEPLIB  DD DSN=COBOL.LOADLIB,DISP=SHR
//SYSOUT   DD SYSOUT=*
```

---

### 🖥️ Mainframe-Specific Features

#### z/OS Unix System Services (USS)

**Paths**:
- Unix paths: `/u/user1/keepass/`
- VSAM/Dataset: `USER1.KEEPASS.DATA`

**Conversion**:
```bash
# Unix to MVS
/u/user1/keepass/config.json -> USER1.KEEPASS.CONFIG
```

#### Dataset Organization

**Sequential**: For log files
**Partitioned**: For load libraries

#### JCL Integration

**Parameter passing**:
```jcl
//SYNC    EXEC PGM=KEEPASS-SYNC,PARM='HOST=server.com'
```

**In program**:
```cobol
ACCEPT WS-CONFIG-HOST FROM COMMAND-LINE
```

#### VSAM Integration

**VSAM datasets** can be used for configuration:
```cobol
SELECT CONFIG-FILE ASSIGN TO "USER1.KEEPASS.CONFIG"
    ORGANIZATION IS INDEXED
    ACCESS MODE IS SEQUENTIAL
    RECORD KEY IS WS-CONFIG-KEY
```

---

### 🔍 Troubleshooting

#### "cobc: command not found"

**Problem**: GnuCOBOL is not installed or not in PATH

**Solution**:
```bash
# Linux
sudo apt install gnucobol  # Debian/Ubuntu
sudo pacman -S gnucobol    # Arch/CachyOS

# macOS
brew install gnucobol

# Verify
which cobc
cobc --version
```

#### Compilation errors

**Problem**: Syntax errors in COBOL code

**Solution**:
```bash
# Compile with debug information
cobc -x -g -v sync.cbl -o keepass-sync

# Check error messages
# COBOL is case-insensitive, but watch columns!
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI is not installed or not in PATH

**Solution**:
```bash
# Install KeePassXC (see above)
# Verify
which keepassxc-cli
keepassxc-cli version

# Mainframe: Install via USS
```

#### JSON parsing problems

**Problem**: COBOL has no native JSON support

**Solution**:
- **Option 1**: Use external tool (`jq`, `python`)
- **Option 2**: Hardcode values in program
- **Option 3**: Use COBOL-JSON library (if available)

#### Mainframe-specific errors

**Problem**: Dataset not found

**Solution**:
```cobol
* Check dataset name and organization
SELECT CONFIG-FILE ASSIGN TO "USER1.KEEPASS.CONFIG"
    ORGANIZATION IS SEQUENTIAL
    FILE STATUS IS WS-STATUS.

IF WS-STATUS NOT = "00"
    DISPLAY "ERROR: Dataset not found: " WS-STATUS
    STOP RUN
END-IF.
```

---

### 🙏 Acknowledgments

#### GnuCOBOL

- **Developer**: GnuCOBOL Project
- **Website**: [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
- **License**: LGPL 3.0
- **Repository**: [https://sourceforge.net/projects/gnucobol/](https://sourceforge.net/projects/gnucobol/)

#### IBM Enterprise COBOL

- **Developer**: IBM
- **Website**: [https://www.ibm.com/products/cobol](https://www.ibm.com/products/cobol)
- **License**: Proprietary (IBM)

#### COBOL Standard

- **Developer**: ISO COBOL Committee
- **Standard**: ISO/IEC 1989:2014 (COBOL 2014)
- **Link**: [ISO/IEC 1989](https://www.iso.org/standard/63139.html)

#### KeePassXC

- **Developer**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **License**: GPL-2.0 / GPL-3.0

---

## 🇪🇸 Español

### ⚠️ IMPORTANTE: Implementación Básica

La variante COBOL es una **implementación básica** para sistemas mainframe y legacy. Para uso en producción, se deben hacer adaptaciones específicas para el entorno objetivo.

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de GnuCOBOL](#instalación-de-gnucobol)
3. [Dependencias Externas](#dependencias-externas)
4. [Compilación](#compilación)
5. [Configuración](#configuración)
6. [Uso](#uso)
7. [Características Específicas de Mainframe](#características-específicas-de-mainframe)
8. [Solución de Problemas](#solución-de-problemas)
9. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Linux** | Todas las distribuciones modernas | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64, z/Architecture |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **Mainframe** | z/OS, OS/390, MVS | z/OS 2.3+ | z/Architecture |

#### Software Requerido

1. **GnuCOBOL** (anteriormente OpenCOBOL)
   - **Versión Mínima**: 2.0+
   - **Versión Recomendada**: 3.1+ (última versión)
   - **Descarga**: [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
   - **Mainframe**: IBM Enterprise COBOL para z/OS (comercial)

2. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
   - **Mainframe**: Puede instalarse vía USS (Unix System Services)

3. **Herramientas Externas** (según el protocolo):
   - **lftp**: Para transferencias FTP/SFTP
   - **smbclient**: Para recursos compartidos de red SMB/CIFS
   - **sshpass** & **scp**: Para transferencias SCP

---

### 💼 Instalación de GnuCOBOL

#### Linux

##### Arch Linux / CachyOS

```bash
# Instalar GnuCOBOL
sudo pacman -S gnucobol

# Verificar instalación
cobc --version
# Debería mostrar: cobc 3.1.x o similar
```

**Nombre del paquete**: `gnucobol`  
**Repositorio**: Community  
**Enlace**: [Paquete Arch Linux GnuCOBOL](https://archlinux.org/packages/community/x86_64/gnucobol/)

##### Debian / Ubuntu

```bash
# Actualizar lista de paquetes
sudo apt update

# Instalar GnuCOBOL
sudo apt install open-cobol  # O gnucobol

# Verificar
cobc --version
```

**Nombres de paquetes**:
- `open-cobol` - GnuCOBOL (nombre antiguo)
- `gnucobol` - GnuCOBOL (nombre nuevo)

**Repositorio**: Universe  
**Enlace**: [Paquete Debian GnuCOBOL](https://packages.debian.org/gnucobol)

**Alternativa: Compilar desde fuentes**

```bash
# Descargar
wget https://sourceforge.net/projects/gnucobol/files/gnucobol/3.1/gnucobol-3.1.tar.xz/download

# Compilar
tar -xf gnucobol-3.1.tar.xz
cd gnucobol-3.1
./configure
make
sudo make install
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install gnucobol
```

##### openSUSE

```bash
sudo zypper install open-cobol
```

#### macOS

##### Homebrew (Recomendado)

```bash
# Instalar Homebrew (si no está presente)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar GnuCOBOL
brew install gnucobol

# Verificar
cobc --version
```

**Enlace**: [Homebrew GnuCOBOL Formula](https://formulae.brew.sh/formula/gnucobol)

##### MacPorts (Alternativa)

```bash
sudo port install gnucobol
```

#### Windows

##### Cygwin / MSYS2

```bash
# En Terminal MSYS2
pacman -S mingw-w64-x86_64-gnucobol

# Añadir a PATH: C:\msys64\mingw64\bin
```

##### Descarga Manual

1. **Descarga**: [https://sourceforge.net/projects/gnucobol/](https://sourceforge.net/projects/gnucobol/)
2. **Elige**: Compilación Windows
3. **Instala**: Sigue las instrucciones
4. **Añade a PATH**: `C:\Program Files\GnuCOBOL\bin`

#### Mainframe (z/OS)

**IBM Enterprise COBOL** (comercial):

1. **Licencia**: Requiere licencia IBM
2. **Instalación**: Vía SMP/E u otros métodos de instalación IBM
3. **Compilador**: `igyc` (IBM Enterprise COBOL)

**GnuCOBOL vía USS**:

1. **USS (Unix System Services)** debe estar activado
2. **Instala**: GnuCOBOL desde fuentes (ver instrucciones Linux)
3. **Compilador**: `cobc`

**Enlaces**:
- **IBM Enterprise COBOL**: [Documentación IBM](https://www.ibm.com/docs/en/cobol-zos)
- **z/OS Unix System Services**: [IBM z/OS USS](https://www.ibm.com/docs/en/zos/2.4.0?topic=system-zos-unix-system-services)

---

### 📦 Dependencias Externas

#### 1. KeePassXC-CLI (REQUERIDO)

**Propósito**: Para fusionar bases de datos KeePass

##### Linux

```bash
# Debian/Ubuntu
sudo apt install keepassxc

# Arch/CachyOS
sudo pacman -S keepassxc

# Fedora
sudo dnf install keepassxc
```

**Verificación**:
```bash
keepassxc-cli version
```

**Enlaces**:
- **Sitio Web Oficial**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

##### Mainframe (z/OS)

**Vía USS (Unix System Services)**:

```bash
# En Shell USS
# Instalar vía Portage o compilar desde fuentes
# Ver: https://keepassxc.org/download/
```

#### 2. lftp (Para FTP/SFTP - RECOMENDADO)

**Propósito**: Transferencias de archivos vía FTP y SFTP

##### Linux

```bash
# Debian/Ubuntu
sudo apt install lftp

# Arch/CachyOS
sudo pacman -S lftp

# Fedora
sudo dnf install lftp
```

**Enlaces**:
- **lftp**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### Mainframe

**FTP está disponible nativamente en z/OS**:

```bash
# Cliente FTP z/OS
ftp hostname
```

**SFTP**: Puede instalarse vía USS.

#### 3. smbclient (Para SMB/CIFS - Opcional)

**Propósito**: Acceso a recursos compartidos de red Windows

##### Linux

```bash
# Debian/Ubuntu
sudo apt install smbclient

# Arch/CachyOS
sudo pacman -S samba
```

**Mainframe**: SMB/CIFS posible vía USS.

---

### 🔨 Compilación

#### Linux / macOS

##### Con Makefile (Recomendado)

```bash
cd cobol

# Compilar
make

# Verificar
./keepass-sync --version  # Si está implementado
```

##### Manual

```bash
cd cobol

# Compilar
cobc -x sync.cbl -o keepass-sync

# Verificar
file keepass-sync
# Debería mostrar: ELF executable
```

##### Con Información de Depuración

```bash
cobc -x -g sync.cbl -o keepass-sync
```

#### Windows

##### MSYS2 / MinGW

```bash
# En Terminal MSYS2
cd cobol
cobc -x sync.cbl -o keepass-sync.exe
```

#### Mainframe (z/OS)

##### IBM Enterprise COBOL

```bash
# JCL o TSO
IGYC INPUT=sync.cbl,LIBRARY=SYSLIB,OUTPUT=keepass-sync
```

##### GnuCOBOL (USS)

```bash
# En Shell USS
cd cobol
cobc -x sync.cbl -o keepass-sync
```

---

### ⚙️ Configuración

**IMPORTANTE**: La variante COBOL utiliza una **configuración simplificada**. El análisis JSON requiere herramientas externas o bibliotecas.

#### Opción 1: Herramienta JSON Externa

```bash
# Usar jq o script Python para creación de config
python3 -c "import json; print(json.load(open('config.json'))['ftp']['host'])"
```

#### Opción 2: Hardcodeado en el Programa

Edita `sync.cbl` y establece valores directamente:

```cobol
MOVE "tu-servidor.com" TO WS-CONFIG-HOST
MOVE "tu-usuario" TO WS-CONFIG-USER
MOVE "tu-contraseña" TO WS-CONFIG-PASSWORD
MOVE "/keepass_passwords.kdbx" TO WS-CONFIG-REMOTE
MOVE "ftp" TO WS-CONFIG-PROTOCOL
```

#### Opción 3: Variables de Entorno

```bash
export KEEPASS_HOST="tu-servidor.com"
export KEEPASS_USER="tu-usuario"
export KEEPASS_PASSWORD="tu-contraseña"
```

**Leer en el programa**:
```cobol
ACCEPT WS-CONFIG-HOST FROM ENVIRONMENT "KEEPASS_HOST"
ACCEPT WS-CONFIG-USER FROM ENVIRONMENT "KEEPASS_USER"
ACCEPT WS-CONFIG-PASSWORD FROM ENVIRONMENT "KEEPASS_PASSWORD"
```

---

### 💻 Uso

#### Linux / macOS

```bash
cd cobol

# Ejecutar programa compilado
./keepass-sync

# Con registro
./keepass-sync >> sync_log.txt 2>&1
```

#### Windows

```powershell
cd cobol

# Ejecutar
.\keepass-sync.exe
```

#### Mainframe (z/OS)

##### TSO / ISPF

```
TSO EXEC cobol/keepass-sync
```

##### USS

```bash
cd cobol
./keepass-sync
```

##### JCL

```jcl
//SYNC    EXEC PGM=KEEPASS-SYNC
//STEPLIB  DD DSN=COBOL.LOADLIB,DISP=SHR
//SYSOUT   DD SYSOUT=*
```

#### Automatización

##### Cron (Linux/macOS)

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * cd /ruta/a/proyecto/cobol && ./keepass-sync
```

##### Programador de Tareas (Windows)

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. Desencadenador: Programación
4. Acción: Iniciar programa
   - Programa: `C:\Ruta\a\cobol\keepass-sync.exe`

##### Trabajo Batch z/OS

```jcl
//KPSYNC   JOB (ACCT),'KEEPASS SYNC',CLASS=A
//STEP1    EXEC PGM=KEEPASS-SYNC
//STEPLIB  DD DSN=COBOL.LOADLIB,DISP=SHR
//SYSOUT   DD SYSOUT=*
```

---

### 🖥️ Características Específicas de Mainframe

#### z/OS Unix System Services (USS)

**Rutas**:
- Rutas Unix: `/u/user1/keepass/`
- VSAM/Dataset: `USER1.KEEPASS.DATA`

**Conversión**:
```bash
# Unix a MVS
/u/user1/keepass/config.json -> USER1.KEEPASS.CONFIG
```

#### Organización de Dataset

**Secuencial**: Para archivos de registro
**Particionado**: Para bibliotecas de carga

#### Integración JCL

**Paso de parámetros**:
```jcl
//SYNC    EXEC PGM=KEEPASS-SYNC,PARM='HOST=server.com'
```

**En el programa**:
```cobol
ACCEPT WS-CONFIG-HOST FROM COMMAND-LINE
```

#### Integración VSAM

**Datasets VSAM** pueden usarse para configuración:
```cobol
SELECT CONFIG-FILE ASSIGN TO "USER1.KEEPASS.CONFIG"
    ORGANIZATION IS INDEXED
    ACCESS MODE IS SEQUENTIAL
    RECORD KEY IS WS-CONFIG-KEY
```

---

### 🔍 Solución de Problemas

#### "cobc: command not found"

**Problema**: GnuCOBOL no está instalado o no está en PATH

**Solución**:
```bash
# Linux
sudo apt install gnucobol  # Debian/Ubuntu
sudo pacman -S gnucobol    # Arch/CachyOS

# macOS
brew install gnucobol

# Verificar
which cobc
cobc --version
```

#### Errores de compilación

**Problema**: Errores de sintaxis en código COBOL

**Solución**:
```bash
# Compilar con información de depuración
cobc -x -g -v sync.cbl -o keepass-sync

# Revisar mensajes de error
# ¡COBOL no distingue mayúsculas, pero cuidar columnas!
```

#### "keepassxc-cli: command not found"

**Problema**: KeePassXC-CLI no está instalado o no está en PATH

**Solución**:
```bash
# Instalar KeePassXC (ver arriba)
# Verificar
which keepassxc-cli
keepassxc-cli version

# Mainframe: Instalar vía USS
```

#### Problemas de análisis JSON

**Problema**: COBOL no tiene soporte JSON nativo

**Solución**:
- **Opción 1**: Usar herramienta externa (`jq`, `python`)
- **Opción 2**: Hardcodear valores en el programa
- **Opción 3**: Usar biblioteca COBOL-JSON (si está disponible)

#### Errores específicos de mainframe

**Problema**: Dataset no encontrado

**Solución**:
```cobol
* Verificar nombre y organización del dataset
SELECT CONFIG-FILE ASSIGN TO "USER1.KEEPASS.CONFIG"
    ORGANIZATION IS SEQUENTIAL
    FILE STATUS IS WS-STATUS.

IF WS-STATUS NOT = "00"
    DISPLAY "ERROR: Dataset not found: " WS-STATUS
    STOP RUN
END-IF.
```

---

### 🙏 Agradecimientos

#### GnuCOBOL

- **Desarrollador**: Proyecto GnuCOBOL
- **Sitio Web**: [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
- **Licencia**: LGPL 3.0
- **Repositorio**: [https://sourceforge.net/projects/gnucobol/](https://sourceforge.net/projects/gnucobol/)

#### IBM Enterprise COBOL

- **Desarrollador**: IBM
- **Sitio Web**: [https://www.ibm.com/products/cobol](https://www.ibm.com/products/cobol)
- **Licencia**: Propietaria (IBM)

#### Estándar COBOL

- **Desarrollador**: Comité ISO COBOL
- **Estándar**: ISO/IEC 1989:2014 (COBOL 2014)
- **Enlace**: [ISO/IEC 1989](https://www.iso.org/standard/63139.html)

#### KeePassXC

- **Desarrollador**: Equipo de KeePassXC
- **Sitio Web**: [https://keepassxc.org/](https://keepassxc.org/)
- **Licencia**: GPL-2.0 / GPL-3.0

---

<div align="center">

**💼 COBOL-Variante: Legacy & Mainframe Support, für Enterprise-Umgebungen**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

**⚠️ HINWEIS: Für Mainframe- und Legacy-Systeme. Für moderne Systeme: Python/Go/Node.js empfohlen.**

</div>

