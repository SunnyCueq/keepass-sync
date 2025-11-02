# 📦 KeePass Sync - Node.js/JavaScript Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Node.js](https://img.shields.io/badge/Node.js-12.0+-339933.svg?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Modern, asynchron, NPM-Ecosystem (optional)**

</div>

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
- [📦 Node.js](./README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript ⭐ **Hier**
- [🤖 AutoIt](../autoit/README.md) - Windows-native | Windows-native | Windows nativo
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

### 📋 Inhaltsverzeichnis

1. [Systemanforderungen](#systemanforderungen)
2. [Node.js Installation](#nodejs-installation)
3. [Externe Dependencies](#externe-dependencies)
4. [Konfiguration](#konfiguration)
5. [Verwendung](#verwendung)
6. [Fehlerbehebung](#fehlerbehebung)
7. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Linux** | Alle modernen Distributionen | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Erforderliche Software

1. **Node.js**
   - **Minimale Version**: 12.0.0+
   - **Empfohlene Version**: 18.x LTS oder 20.x (aktuellste LTS)
   - **Download**: [https://nodejs.org/](https://nodejs.org/)

2. **npm** (Node Package Manager)
   - Wird normalerweise mit Node.js installiert
   - **Minimale Version**: 6.0.0+
   - **Empfohlene Version**: 9.0.0+ (aktuellste Version)

3. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

4. **Externe Tools** (abhängig vom verwendeten Protokoll):
   - **lftp**: Für FTP/SFTP-Übertragungen (Linux/macOS)
   - **smbclient**: Für SMB/CIFS-Netzwerk-Shares (Linux/macOS)
   - **sshpass** & **scp**: Für SCP-Übertragungen (Linux/macOS)
   - **WinSCP** oder **lftp**: Für FTP/SFTP auf Windows

---

### 🚀 Node.js Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Installiere Node.js und npm
sudo pacman -S nodejs npm

# Überprüfe die Installation
node --version
# Sollte zeigen: v18.x.x oder v20.x.x

npm --version
# Sollte zeigen: 9.x.x oder höher
```

**Paketnamen**: 
- `nodejs` - Node.js Runtime
- `npm` - Node Package Manager

**Repository**: Community  
**Link**: [Arch Linux Node.js Package](https://archlinux.org/packages/community/x86_64/nodejs/)

##### Debian / Ubuntu

```bash
# Aktualisiere Paketliste
sudo apt update

# Installiere Node.js und npm
sudo apt install nodejs npm

# Überprüfe die Installation
node --version
npm --version
```

**Paketnamen**: 
- `nodejs` - Node.js Runtime
- `npm` - Node Package Manager

**Repository**: Universe  
**Link**: [Debian Node.js Package](https://packages.debian.org/nodejs)

**Alternative: NodeSource Repository (für neueste LTS-Version)**

```bash
# Für Node.js 20.x LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Überprüfe
node --version
npm --version
```

**Link**: [NodeSource](https://github.com/nodesource/distributions)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install nodejs npm
```

**Alternative: NodeSource Repository**

```bash
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs
```

##### openSUSE

```bash
sudo zypper install nodejs18 npm18
```

#### macOS

##### Homebrew (Empfohlen)

```bash
# Installiere Homebrew (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installiere Node.js (enthält npm)
brew install node

# Überprüfe
node --version
npm --version
```

**Link**: [Homebrew Node Formula](https://formulae.brew.sh/formula/node)

##### Manueller Download

1. **Download**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **Wähle**: macOS Installer (.pkg) für deine Architektur
3. **Führe .pkg Installer aus**: Folgen Sie den Anweisungen
4. **npm ist automatisch enthalten**

##### nvm (Node Version Manager - Optional)

```bash
# Installiere nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Lade nvm
source ~/.zshrc  # oder ~/.bashrc

# Installiere Node.js LTS
nvm install --lts
nvm use --lts

# Überprüfe
node --version
npm --version
```

**Link**: [nvm GitHub](https://github.com/nvm-sh/nvm)

#### Windows

##### Installer Download (Empfohlen)

1. **Download**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **Wähle**: Windows Installer (.msi) - 64-bit
3. **Empfohlen**: LTS Version (z.B. 20.x LTS)
4. **Führe Installer aus**: Folgen Sie den Anweisungen
5. **WICHTIG**: "Add to PATH" sollte aktiviert sein
6. **npm ist automatisch enthalten**

##### Überprüfung

```powershell
# PowerShell oder CMD
node --version
npm --version
```

##### Chocolatey (Alternative)

```powershell
# Installiere Chocolatey (falls nicht vorhanden)
# Siehe: https://chocolatey.org/install

# Installiere Node.js LTS
choco install nodejs-lts

# Überprüfe
node --version
npm --version
```

**Link**: [Chocolatey Node.js Package](https://community.chocolatey.org/packages/nodejs-lts)

##### nvm-windows (Node Version Manager - Optional)

1. **Download**: [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
2. **Installiere**: nvm-setup.exe
3. **Verwendung**:
```powershell
nvm install lts
nvm use lts
node --version
```

**Link**: [nvm-windows GitHub](https://github.com/coreybutler/nvm-windows)

---

### 📦 Optional: NPM Packages

**WICHTIG**: Die Node.js-Variante benötigt **KEINE NPM-Packages** für die Basis-Funktionalität!

Das Script nutzt externe Tools (lftp, smbclient, etc.) statt NPM-Packages. Die in `package.json` aufgeführten Packages (`basic-ftp`, `ssh2-sftp-client`) sind **optional** und nur für erweiterte Funktionen, wenn externe Tools nicht verfügbar sind.

#### Optional: Packages installieren (nur wenn externe Tools fehlen)

```bash
# Navigiere zum nodejs-Verzeichnis
cd nodejs

# Installiere optionale Packages
npm install

# Oder nur spezifische Packages
npm install basic-ftp       # Für FTP (falls lftp nicht verfügbar)
npm install ssh2-sftp-client  # Für SFTP (falls lftp nicht verfügbar)
```

**Hinweis**: Die Variante funktioniert **auch OHNE** diese Packages, nutzt dann externe Tools (lftp, smbclient, etc.).

---

### 📦 Externe Dependencies

Die Node.js-Variante verwendet externe Tools für Datei-Übertragungen. Je nach verwendetem Protokoll müssen unterschiedliche Tools installiert werden.

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
- **Dokumentation**: [https://keepassxc.org/docs/](https://keepassxc.org/docs/)

##### macOS

```bash
brew install keepassxc
```

##### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Installiere KeePassXC
3. Stelle sicher, dass `keepassxc-cli.exe` im PATH ist

#### 2. lftp (Für FTP/SFTP - Linux/macOS - EMPFOHLEN)

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

**Version**: Normalerweise 4.9.0+  
**Überprüfung**:
```bash
lftp --version
```

**Links**:
- **Offizielle Website**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **GitHub**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)
- **Dokumentation**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### macOS

```bash
brew install lftp
```

##### Windows

**Option 1: Git Bash / WSL**

```bash
# In Git Bash oder WSL
apt install lftp  # WSL
# Oder: pacman -S lftp  # In Arch-basierten WSL
```

**Option 2: WinSCP** (siehe unten)

#### 3. smbclient (Für SMB/CIFS - Linux/macOS - Optional)

**Zweck**: Zugriff auf Windows-Netzwerk-Shares

##### Linux

```bash
# Debian/Ubuntu
sudo apt install smbclient

# Arch/CachyOS
sudo pacman -S samba

# Fedora
sudo dnf install samba-client
```

**Version**: Normalerweise 4.x+  
**Überprüfung**:
```bash
smbclient --version
```

**Links**:
- **Samba Projekt**: [https://www.samba.org/](https://www.samba.org/)
- **Dokumentation**: [https://www.samba.org/samba/docs/](https://www.samba.org/samba/docs/)

##### macOS

```bash
# macOS hat SMB-Unterstützung bereits integriert
# Für smbclient:
brew install samba
```

##### Windows

Windows hat native SMB-Unterstützung. Keine Installation nötig.

#### 4. sshpass & scp (Für SCP - Linux/macOS - Optional)

**Zweck**: Sichere Datei-Übertragungen via SSH

##### Linux

```bash
# Debian/Ubuntu
sudo apt install sshpass openssh-client

# Arch/CachyOS
sudo pacman -S sshpass openssh

# Fedora
sudo dnf install sshpass openssh-clients
```

**Überprüfung**:
```bash
sshpass -V
scp -V
```

**Links**:
- **sshpass**: [https://sourceforge.net/projects/sshpass/](https://sourceforge.net/projects/sshpass/)
- **OpenSSH**: [https://www.openssh.com/](https://www.openssh.com/)

##### macOS

```bash
# scp ist bereits installiert (Teil von macOS)
# sshpass installieren:
brew install hudochenkov/sshpass/sshpass
```

##### Windows

**Option 1: Git Bash** (hat scp bereits)

**Option 2: WSL**

```bash
sudo apt install sshpass openssh-client
```

---

### ⚙️ Konfiguration

#### 1. Repository klonen oder Dateien herunterladen

```bash
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Option 2: Download ZIP
# Entpacke ZIP-Datei und navigiere zum Hauptverzeichnis
```

#### 2. Erstelle config.json

```bash
# Kopiere Beispiel-Config
cp config.example.json config.json

# Bearbeite config.json
nano config.json  # Oder anderen Editor verwenden
```

**Wichtige Einstellungen**:

```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-passwort",
    "type": "ftp",
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

#### 3. Script ausführbar machen (Linux/macOS - Optional)

```bash
cd nodejs
chmod +x sync.js
```

---

### 💻 Verwendung

#### Basis-Befehle

```bash
# Navigiere zum nodejs-Verzeichnis
cd nodejs

# Normale Synchronisation
node sync.js

# Verbindung testen (ohne Sync)
node sync.js --test

# Status anzeigen
node sync.js --status

# Alternative Config-Datei
node sync.js --config /pfad/zu/config.json

# Version anzeigen
node sync.js --version

# Hilfe
node sync.js --help
```

#### Mit ausführbar gemacht (Linux/macOS)

```bash
cd nodejs

# Direkt ausführen
./sync.js

# Mit Argumenten
./sync.js --test
./sync.js --status
```

#### Automatisierung

##### Cron (Linux/macOS)

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * cd /pfad/zum/projekt/nodejs && /usr/bin/node sync.js
```

##### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Zeitplan
4. Aktion: Programm starten
   - Programm: `node.exe`
   - Argumente: `C:\Pfad\zum\projekt\nodejs\sync.js`
   - Start in: `C:\Pfad\zum\projekt\nodejs`

---

### 🔍 Fehlerbehebung

#### "node: command not found"

**Problem**: Node.js ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Linux: Installiere Node.js
sudo apt install nodejs npm  # Debian/Ubuntu
sudo pacman -S nodejs npm    # Arch/CachyOS

# macOS
brew install node

# Windows: Füge Node.js zu PATH hinzu
# Systemsteuerung → Umgebungsvariablen → PATH
```

#### "npm: command not found"

**Problem**: npm ist nicht installiert

**Lösung**:
```bash
# npm sollte mit Node.js installiert werden
# Überprüfe Node.js Installation
node --version

# Falls npm fehlt, installiere npm separat
# Linux
sudo apt install npm  # Debian/Ubuntu

# macOS/Windows: Reinstalliere Node.js
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Installiere KeePassXC (siehe oben)
# Überprüfe Installation
which keepassxc-cli  # Linux/macOS
# Oder:
keepassxc-cli version
```

#### "lftp not found"

**Problem**: lftp ist nicht installiert (nur bei FTP/SFTP-Protokoll)

**Lösung**:
```bash
# Linux
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS

# macOS
brew install lftp
```

#### "smbclient not found"

**Problem**: SMB-Client ist nicht installiert (nur bei SMB-Protokoll)

**Lösung**:
```bash
# Linux
sudo apt install smbclient  # Debian/Ubuntu
sudo pacman -S samba       # Arch/CachyOS
```

#### "sshpass not found" oder "scp: command not found"

**Problem**: SSH-Tools sind nicht installiert (nur bei SCP-Protokoll)

**Lösung**:
```bash
# Linux
sudo apt install sshpass openssh-client  # Debian/Ubuntu
sudo pacman -S sshpass openssh           # Arch/CachyOS
```

---

### 🙏 Danksagungen

#### Node.js

- **Entwickler**: OpenJS Foundation
- **Website**: [https://nodejs.org/](https://nodejs.org/)
- **Lizenz**: MIT
- **Repository**: [https://github.com/nodejs/node](https://github.com/nodejs/node)

#### npm

- **Entwickler**: npm, Inc.
- **Website**: [https://www.npmjs.com/](https://www.npmjs.com/)
- **Lizenz**: Artistic-2.0
- **Repository**: [https://github.com/npm/cli](https://github.com/npm/cli)

#### KeePassXC

- **Entwickler**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **Lizenz**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### lftp

- **Entwickler**: Alexander V. Lukyanov
- **Website**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **Lizenz**: GPL-3.0
- **Repository**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)

#### Samba (smbclient)

- **Entwickler**: Samba Team
- **Website**: [https://www.samba.org/](https://www.samba.org/)
- **Lizenz**: GPL-3.0
- **Repository**: [https://github.com/samba-team/samba](https://github.com/samba-team/samba)

#### OpenSSH (scp/sshpass)

- **Entwickler**: OpenBSD Project
- **Website**: [https://www.openssh.com/](https://www.openssh.com/)
- **Lizenz**: BSD 2-Clause
- **Repository**: [https://github.com/openssh/openssh-portable](https://github.com/openssh/openssh-portable)

#### Optional: NPM Packages (wenn verwendet)

- **basic-ftp**: [https://github.com/patrickjuchli/basic-ftp](https://github.com/patrickjuchli/basic-ftp)
- **ssh2-sftp-client**: [https://github.com/theophilusx/ssh2-sftp-client](https://github.com/theophilusx/ssh2-sftp-client)

---

## 🇬🇧 English

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Node.js Installation](#nodejs-installation-1)
3. [External Dependencies](#external-dependencies)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Troubleshooting](#troubleshooting)
7. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Linux** | All modern distributions | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Required Software

1. **Node.js**
   - **Minimum Version**: 12.0.0+
   - **Recommended Version**: 18.x LTS or 20.x (latest LTS)
   - **Download**: [https://nodejs.org/](https://nodejs.org/)

2. **npm** (Node Package Manager)
   - Usually installed with Node.js
   - **Minimum Version**: 6.0.0+
   - **Recommended Version**: 9.0.0+ (latest version)

3. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

4. **External Tools** (depending on the protocol used):
   - **lftp**: For FTP/SFTP transfers (Linux/macOS)
   - **smbclient**: For SMB/CIFS network shares (Linux/macOS)
   - **sshpass** & **scp**: For SCP transfers (Linux/macOS)
   - **WinSCP** or **lftp**: For FTP/SFTP on Windows

---

### 🚀 Node.js Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Install Node.js and npm
sudo pacman -S nodejs npm

# Verify installation
node --version
# Should show: v18.x.x or v20.x.x

npm --version
# Should show: 9.x.x or higher
```

**Package names**: 
- `nodejs` - Node.js Runtime
- `npm` - Node Package Manager

**Repository**: Community  
**Link**: [Arch Linux Node.js Package](https://archlinux.org/packages/community/x86_64/nodejs/)

##### Debian / Ubuntu

```bash
# Update package list
sudo apt update

# Install Node.js and npm
sudo apt install nodejs npm

# Verify installation
node --version
npm --version
```

**Package names**: 
- `nodejs` - Node.js Runtime
- `npm` - Node Package Manager

**Repository**: Universe  
**Link**: [Debian Node.js Package](https://packages.debian.org/nodejs)

**Alternative: NodeSource Repository (for latest LTS version)**

```bash
# For Node.js 20.x LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify
node --version
npm --version
```

**Link**: [NodeSource](https://github.com/nodesource/distributions)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install nodejs npm
```

**Alternative: NodeSource Repository**

```bash
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs
```

##### openSUSE

```bash
sudo zypper install nodejs18 npm18
```

#### macOS

##### Homebrew (Recommended)

```bash
# Install Homebrew (if not present)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js (includes npm)
brew install node

# Verify
node --version
npm --version
```

**Link**: [Homebrew Node Formula](https://formulae.brew.sh/formula/node)

##### Manual Download

1. **Download**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **Choose**: macOS Installer (.pkg) for your architecture
3. **Run .pkg installer**: Follow the instructions
4. **npm is automatically included**

##### nvm (Node Version Manager - Optional)

```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Load nvm
source ~/.zshrc  # or ~/.bashrc

# Install Node.js LTS
nvm install --lts
nvm use --lts

# Verify
node --version
npm --version
```

**Link**: [nvm GitHub](https://github.com/nvm-sh/nvm)

#### Windows

##### Installer Download (Recommended)

1. **Download**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **Choose**: Windows Installer (.msi) - 64-bit
3. **Recommended**: LTS version (e.g., 20.x LTS)
4. **Run installer**: Follow the instructions
5. **IMPORTANT**: "Add to PATH" should be enabled
6. **npm is automatically included**

##### Verification

```powershell
# PowerShell or CMD
node --version
npm --version
```

##### Chocolatey (Alternative)

```powershell
# Install Chocolatey (if not present)
# See: https://chocolatey.org/install

# Install Node.js LTS
choco install nodejs-lts

# Verify
node --version
npm --version
```

**Link**: [Chocolatey Node.js Package](https://community.chocolatey.org/packages/nodejs-lts)

##### nvm-windows (Node Version Manager - Optional)

1. **Download**: [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
2. **Install**: nvm-setup.exe
3. **Usage**:
```powershell
nvm install lts
nvm use lts
node --version
```

**Link**: [nvm-windows GitHub](https://github.com/coreybutler/nvm-windows)

---

### 📦 Optional: NPM Packages

**IMPORTANT**: The Node.js variant requires **NO NPM PACKAGES** for basic functionality!

The script uses external tools (lftp, smbclient, etc.) instead of NPM packages. The packages listed in `package.json` (`basic-ftp`, `ssh2-sftp-client`) are **optional** and only for extended features when external tools are not available.

#### Optional: Install packages (only if external tools are missing)

```bash
# Navigate to nodejs directory
cd nodejs

# Install optional packages
npm install

# Or only specific packages
npm install basic-ftp       # For FTP (if lftp not available)
npm install ssh2-sftp-client  # For SFTP (if lftp not available)
```

**Note**: The variant works **EVEN WITHOUT** these packages, then uses external tools (lftp, smbclient, etc.).

---

### 📦 External Dependencies

The Node.js variant uses external tools for file transfers. Different tools must be installed depending on the protocol used.

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
- **Documentation**: [https://keepassxc.org/docs/](https://keepassxc.org/docs/)

##### macOS

```bash
brew install keepassxc
```

##### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Install KeePassXC
3. Ensure `keepassxc-cli.exe` is in PATH

#### 2. lftp (For FTP/SFTP - Linux/macOS - RECOMMENDED)

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

**Version**: Usually 4.9.0+  
**Verification**:
```bash
lftp --version
```

**Links**:
- **Official Website**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **GitHub**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)
- **Documentation**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### macOS

```bash
brew install lftp
```

##### Windows

**Option 1: Git Bash / WSL**

```bash
# In Git Bash or WSL
apt install lftp  # WSL
# Or: pacman -S lftp  # In Arch-based WSL
```

**Option 2: WinSCP** (see below)

#### 3. smbclient (For SMB/CIFS - Linux/macOS - Optional)

**Purpose**: Access to Windows network shares

##### Linux

```bash
# Debian/Ubuntu
sudo apt install smbclient

# Arch/CachyOS
sudo pacman -S samba

# Fedora
sudo dnf install samba-client
```

**Version**: Usually 4.x+  
**Verification**:
```bash
smbclient --version
```

**Links**:
- **Samba Project**: [https://www.samba.org/](https://www.samba.org/)
- **Documentation**: [https://www.samba.org/samba/docs/](https://www.samba.org/samba/docs/)

##### macOS

```bash
# macOS has SMB support already integrated
# For smbclient:
brew install samba
```

##### Windows

Windows has native SMB support. No installation needed.

#### 4. sshpass & scp (For SCP - Linux/macOS - Optional)

**Purpose**: Secure file transfers via SSH

##### Linux

```bash
# Debian/Ubuntu
sudo apt install sshpass openssh-client

# Arch/CachyOS
sudo pacman -S sshpass openssh

# Fedora
sudo dnf install sshpass openssh-clients
```

**Verification**:
```bash
sshpass -V
scp -V
```

**Links**:
- **sshpass**: [https://sourceforge.net/projects/sshpass/](https://sourceforge.net/projects/sshpass/)
- **OpenSSH**: [https://www.openssh.com/](https://www.openssh.com/)

##### macOS

```bash
# scp is already installed (part of macOS)
# Install sshpass:
brew install hudochenkov/sshpass/sshpass
```

##### Windows

**Option 1: Git Bash** (has scp already)

**Option 2: WSL**

```bash
sudo apt install sshpass openssh-client
```

---

### ⚙️ Configuration

#### 1. Clone repository or download files

```bash
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Option 2: Download ZIP
# Extract ZIP file and navigate to main directory
```

#### 2. Create config.json

```bash
# Copy example config
cp config.example.json config.json

# Edit config.json
nano config.json  # Or use another editor
```

**Important settings**:

```json
{
  "ftp": {
    "host": "your-server.com",
    "user": "your-username",
    "password": "your-password",
    "type": "ftp",
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

#### 3. Make script executable (Linux/macOS - Optional)

```bash
cd nodejs
chmod +x sync.js
```

---

### 💻 Usage

#### Basic Commands

```bash
# Navigate to nodejs directory
cd nodejs

# Normal synchronization
node sync.js

# Test connection (without sync)
node sync.js --test

# Show status
node sync.js --status

# Alternative config file
node sync.js --config /path/to/config.json

# Show version
node sync.js --version

# Help
node sync.js --help
```

#### With executable flag (Linux/macOS)

```bash
cd nodejs

# Run directly
./sync.js

# With arguments
./sync.js --test
./sync.js --status
```

#### Automation

##### Cron (Linux/macOS)

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * cd /path/to/project/nodejs && /usr/bin/node sync.js
```

##### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Schedule
4. Action: Start program
   - Program: `node.exe`
   - Arguments: `C:\Path\to\project\nodejs\sync.js`
   - Start in: `C:\Path\to\project\nodejs`

---

### 🔍 Troubleshooting

#### "node: command not found"

**Problem**: Node.js is not installed or not in PATH

**Solution**:
```bash
# Linux: Install Node.js
sudo apt install nodejs npm  # Debian/Ubuntu
sudo pacman -S nodejs npm    # Arch/CachyOS

# macOS
brew install node

# Windows: Add Node.js to PATH
# Control Panel → Environment Variables → PATH
```

#### "npm: command not found"

**Problem**: npm is not installed

**Solution**:
```bash
# npm should be installed with Node.js
# Check Node.js installation
node --version

# If npm is missing, install npm separately
# Linux
sudo apt install npm  # Debian/Ubuntu

# macOS/Windows: Reinstall Node.js
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI is not installed or not in PATH

**Solution**:
```bash
# Install KeePassXC (see above)
# Verify installation
which keepassxc-cli  # Linux/macOS
# Or:
keepassxc-cli version
```

#### "lftp not found"

**Problem**: lftp is not installed (only for FTP/SFTP protocol)

**Solution**:
```bash
# Linux
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS

# macOS
brew install lftp
```

#### "smbclient not found"

**Problem**: SMB client is not installed (only for SMB protocol)

**Solution**:
```bash
# Linux
sudo apt install smbclient  # Debian/Ubuntu
sudo pacman -S samba       # Arch/CachyOS
```

#### "sshpass not found" or "scp: command not found"

**Problem**: SSH tools are not installed (only for SCP protocol)

**Solution**:
```bash
# Linux
sudo apt install sshpass openssh-client  # Debian/Ubuntu
sudo pacman -S sshpass openssh           # Arch/CachyOS
```

---

### 🙏 Acknowledgments

#### Node.js

- **Developer**: OpenJS Foundation
- **Website**: [https://nodejs.org/](https://nodejs.org/)
- **License**: MIT
- **Repository**: [https://github.com/nodejs/node](https://github.com/nodejs/node)

#### npm

- **Developer**: npm, Inc.
- **Website**: [https://www.npmjs.com/](https://www.npmjs.com/)
- **License**: Artistic-2.0
- **Repository**: [https://github.com/npm/cli](https://github.com/npm/cli)

#### KeePassXC

- **Developer**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **License**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### lftp

- **Developer**: Alexander V. Lukyanov
- **Website**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **License**: GPL-3.0
- **Repository**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)

#### Samba (smbclient)

- **Developer**: Samba Team
- **Website**: [https://www.samba.org/](https://www.samba.org/)
- **License**: GPL-3.0
- **Repository**: [https://github.com/samba-team/samba](https://github.com/samba-team/samba)

#### OpenSSH (scp/sshpass)

- **Developer**: OpenBSD Project
- **Website**: [https://www.openssh.com/](https://www.openssh.com/)
- **License**: BSD 2-Clause
- **Repository**: [https://github.com/openssh/openssh-portable](https://github.com/openssh/openssh-portable)

#### Optional: NPM Packages (if used)

- **basic-ftp**: [https://github.com/patrickjuchli/basic-ftp](https://github.com/patrickjuchli/basic-ftp)
- **ssh2-sftp-client**: [https://github.com/theophilusx/ssh2-sftp-client](https://github.com/theophilusx/ssh2-sftp-client)

---

## 🇪🇸 Español

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de Node.js](#instalación-de-nodejs)
3. [Dependencias Externas](#dependencias-externas)
4. [Configuración](#configuración)
5. [Uso](#uso)
6. [Solución de Problemas](#solución-de-problemas)
7. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Linux** | Todas las distribuciones modernas | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Software Requerido

1. **Node.js**
   - **Versión Mínima**: 12.0.0+
   - **Versión Recomendada**: 18.x LTS o 20.x (última LTS)
   - **Descarga**: [https://nodejs.org/](https://nodejs.org/)

2. **npm** (Gestor de Paquetes Node)
   - Normalmente se instala con Node.js
   - **Versión Mínima**: 6.0.0+
   - **Versión Recomendada**: 9.0.0+ (última versión)

3. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

4. **Herramientas Externas** (según el protocolo utilizado):
   - **lftp**: Para transferencias FTP/SFTP (Linux/macOS)
   - **smbclient**: Para recursos compartidos de red SMB/CIFS (Linux/macOS)
   - **sshpass** & **scp**: Para transferencias SCP (Linux/macOS)
   - **WinSCP** o **lftp**: Para FTP/SFTP en Windows

---

### 🚀 Instalación de Node.js

#### Linux

##### Arch Linux / CachyOS

```bash
# Instalar Node.js y npm
sudo pacman -S nodejs npm

# Verificar instalación
node --version
# Debería mostrar: v18.x.x o v20.x.x

npm --version
# Debería mostrar: 9.x.x o superior
```

**Nombres de paquetes**: 
- `nodejs` - Runtime Node.js
- `npm` - Gestor de Paquetes Node

**Repositorio**: Community  
**Enlace**: [Arch Linux Node.js Package](https://archlinux.org/packages/community/x86_64/nodejs/)

##### Debian / Ubuntu

```bash
# Actualizar lista de paquetes
sudo apt update

# Instalar Node.js y npm
sudo apt install nodejs npm

# Verificar instalación
node --version
npm --version
```

**Nombres de paquetes**: 
- `nodejs` - Runtime Node.js
- `npm` - Gestor de Paquetes Node

**Repositorio**: Universe  
**Enlace**: [Debian Node.js Package](https://packages.debian.org/nodejs)

**Alternativa: Repositorio NodeSource (para última versión LTS)**

```bash
# Para Node.js 20.x LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verificar
node --version
npm --version
```

**Enlace**: [NodeSource](https://github.com/nodesource/distributions)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install nodejs npm
```

**Alternativa: Repositorio NodeSource**

```bash
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs
```

##### openSUSE

```bash
sudo zypper install nodejs18 npm18
```

#### macOS

##### Homebrew (Recomendado)

```bash
# Instalar Homebrew (si no está presente)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Node.js (incluye npm)
brew install node

# Verificar
node --version
npm --version
```

**Enlace**: [Homebrew Node Formula](https://formulae.brew.sh/formula/node)

##### Descarga Manual

1. **Descarga**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **Elige**: Instalador macOS (.pkg) para tu arquitectura
3. **Ejecuta el instalador .pkg**: Sigue las instrucciones
4. **npm está incluido automáticamente**

##### nvm (Node Version Manager - Opcional)

```bash
# Instalar nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Cargar nvm
source ~/.zshrc  # o ~/.bashrc

# Instalar Node.js LTS
nvm install --lts
nvm use --lts

# Verificar
node --version
npm --version
```

**Enlace**: [nvm GitHub](https://github.com/nvm-sh/nvm)

#### Windows

##### Descarga del Instalador (Recomendado)

1. **Descarga**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **Elige**: Instalador Windows (.msi) - 64-bit
3. **Recomendado**: Versión LTS (p. ej., 20.x LTS)
4. **Ejecuta el instalador**: Sigue las instrucciones
5. **IMPORTANTE**: "Add to PATH" debe estar activado
6. **npm está incluido automáticamente**

##### Verificación

```powershell
# PowerShell o CMD
node --version
npm --version
```

##### Chocolatey (Alternativa)

```powershell
# Instalar Chocolatey (si no está presente)
# Ver: https://chocolatey.org/install

# Instalar Node.js LTS
choco install nodejs-lts

# Verificar
node --version
npm --version
```

**Enlace**: [Chocolatey Node.js Package](https://community.chocolatey.org/packages/nodejs-lts)

##### nvm-windows (Node Version Manager - Opcional)

1. **Descarga**: [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
2. **Instala**: nvm-setup.exe
3. **Uso**:
```powershell
nvm install lts
nvm use lts
node --version
```

**Enlace**: [nvm-windows GitHub](https://github.com/coreybutler/nvm-windows)

---

### 📦 Opcional: Paquetes NPM

**IMPORTANTE**: ¡La variante Node.js **NO requiere paquetes NPM** para la funcionalidad básica!

El script utiliza herramientas externas (lftp, smbclient, etc.) en lugar de paquetes NPM. Los paquetes listados en `package.json` (`basic-ftp`, `ssh2-sftp-client`) son **opcionales** y solo para funciones extendidas cuando las herramientas externas no están disponibles.

#### Opcional: Instalar paquetes (solo si faltan herramientas externas)

```bash
# Navegar al directorio nodejs
cd nodejs

# Instalar paquetes opcionales
npm install

# O solo paquetes específicos
npm install basic-ftp       # Para FTP (si lftp no está disponible)
npm install ssh2-sftp-client  # Para SFTP (si lftp no está disponible)
```

**Nota**: La variante funciona **INCLUSO SIN** estos paquetes, entonces usa herramientas externas (lftp, smbclient, etc.).

---

### 📦 Dependencias Externas

La variante Node.js utiliza herramientas externas para transferencias de archivos. Deben instalarse diferentes herramientas según el protocolo utilizado.

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
- **Documentación**: [https://keepassxc.org/docs/](https://keepassxc.org/docs/)

##### macOS

```bash
brew install keepassxc
```

##### Windows

1. Descarga: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Instala KeePassXC
3. Asegúrate de que `keepassxc-cli.exe` esté en PATH

#### 2. lftp (Para FTP/SFTP - Linux/macOS - RECOMENDADO)

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

**Versión**: Normalmente 4.9.0+  
**Verificación**:
```bash
lftp --version
```

**Enlaces**:
- **Sitio Web Oficial**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **GitHub**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)
- **Documentación**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### macOS

```bash
brew install lftp
```

##### Windows

**Opción 1: Git Bash / WSL**

```bash
# En Git Bash o WSL
apt install lftp  # WSL
# O: pacman -S lftp  # En WSL basado en Arch
```

**Opción 2: WinSCP** (ver abajo)

#### 3. smbclient (Para SMB/CIFS - Linux/macOS - Opcional)

**Propósito**: Acceso a recursos compartidos de red Windows

##### Linux

```bash
# Debian/Ubuntu
sudo apt install smbclient

# Arch/CachyOS
sudo pacman -S samba

# Fedora
sudo dnf install samba-client
```

**Versión**: Normalmente 4.x+  
**Verificación**:
```bash
smbclient --version
```

**Enlaces**:
- **Proyecto Samba**: [https://www.samba.org/](https://www.samba.org/)
- **Documentación**: [https://www.samba.org/samba/docs/](https://www.samba.org/samba/docs/)

##### macOS

```bash
# macOS tiene soporte SMB ya integrado
# Para smbclient:
brew install samba
```

##### Windows

Windows tiene soporte SMB nativo. No se requiere instalación.

#### 4. sshpass & scp (Para SCP - Linux/macOS - Opcional)

**Propósito**: Transferencias seguras de archivos vía SSH

##### Linux

```bash
# Debian/Ubuntu
sudo apt install sshpass openssh-client

# Arch/CachyOS
sudo pacman -S sshpass openssh

# Fedora
sudo dnf install sshpass openssh-clients
```

**Verificación**:
```bash
sshpass -V
scp -V
```

**Enlaces**:
- **sshpass**: [https://sourceforge.net/projects/sshpass/](https://sourceforge.net/projects/sshpass/)
- **OpenSSH**: [https://www.openssh.com/](https://www.openssh.com/)

##### macOS

```bash
# scp ya está instalado (parte de macOS)
# Instalar sshpass:
brew install hudochenkov/sshpass/sshpass
```

##### Windows

**Opción 1: Git Bash** (ya tiene scp)

**Opción 2: WSL**

```bash
sudo apt install sshpass openssh-client
```

---

### ⚙️ Configuración

#### 1. Clonar repositorio o descargar archivos

```bash
# Opción 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Opción 2: Descargar ZIP
# Extraer archivo ZIP y navegar al directorio principal
```

#### 2. Crear config.json

```bash
# Copiar config de ejemplo
cp config.example.json config.json

# Editar config.json
nano config.json  # O usar otro editor
```

**Configuraciones importantes**:

```json
{
  "ftp": {
    "host": "tu-servidor.com",
    "user": "tu-usuario",
    "password": "tu-contraseña",
    "type": "ftp",
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

#### 3. Hacer script ejecutable (Linux/macOS - Opcional)

```bash
cd nodejs
chmod +x sync.js
```

---

### 💻 Uso

#### Comandos Básicos

```bash
# Navegar al directorio nodejs
cd nodejs

# Sincronización normal
node sync.js

# Probar conexión (sin sincronizar)
node sync.js --test

# Mostrar estado
node sync.js --status

# Archivo de configuración alternativo
node sync.js --config /ruta/a/config.json

# Mostrar versión
node sync.js --version

# Ayuda
node sync.js --help
```

#### Con flag ejecutable (Linux/macOS)

```bash
cd nodejs

# Ejecutar directamente
./sync.js

# Con argumentos
./sync.js --test
./sync.js --status
```

#### Automatización

##### Cron (Linux/macOS)

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * cd /ruta/a/proyecto/nodejs && /usr/bin/node sync.js
```

##### Programador de Tareas (Windows)

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. Desencadenador: Programación
4. Acción: Iniciar programa
   - Programa: `node.exe`
   - Argumentos: `C:\Ruta\a\proyecto\nodejs\sync.js`
   - Iniciar en: `C:\Ruta\a\proyecto\nodejs`

---

### 🔍 Solución de Problemas

#### "node: command not found"

**Problema**: Node.js no está instalado o no está en PATH

**Solución**:
```bash
# Linux: Instalar Node.js
sudo apt install nodejs npm  # Debian/Ubuntu
sudo pacman -S nodejs npm    # Arch/CachyOS

# macOS
brew install node

# Windows: Añadir Node.js a PATH
# Panel de Control → Variables de Entorno → PATH
```

#### "npm: command not found"

**Problema**: npm no está instalado

**Solución**:
```bash
# npm debería instalarse con Node.js
# Verificar instalación de Node.js
node --version

# Si falta npm, instalar npm por separado
# Linux
sudo apt install npm  # Debian/Ubuntu

# macOS/Windows: Reinstalar Node.js
```

#### "keepassxc-cli: command not found"

**Problema**: KeePassXC-CLI no está instalado o no está en PATH

**Solución**:
```bash
# Instalar KeePassXC (ver arriba)
# Verificar instalación
which keepassxc-cli  # Linux/macOS
# O:
keepassxc-cli version
```

#### "lftp not found"

**Problema**: lftp no está instalado (solo para protocolo FTP/SFTP)

**Solución**:
```bash
# Linux
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS

# macOS
brew install lftp
```

#### "smbclient not found"

**Problema**: Cliente SMB no está instalado (solo para protocolo SMB)

**Solución**:
```bash
# Linux
sudo apt install smbclient  # Debian/Ubuntu
sudo pacman -S samba       # Arch/CachyOS
```

#### "sshpass not found" o "scp: command not found"

**Problema**: Herramientas SSH no están instaladas (solo para protocolo SCP)

**Solución**:
```bash
# Linux
sudo apt install sshpass openssh-client  # Debian/Ubuntu
sudo pacman -S sshpass openssh           # Arch/CachyOS
```

---

### 🙏 Agradecimientos

#### Node.js

- **Desarrollador**: OpenJS Foundation
- **Sitio Web**: [https://nodejs.org/](https://nodejs.org/)
- **Licencia**: MIT
- **Repositorio**: [https://github.com/nodejs/node](https://github.com/nodejs/node)

#### npm

- **Desarrollador**: npm, Inc.
- **Sitio Web**: [https://www.npmjs.com/](https://www.npmjs.com/)
- **Licencia**: Artistic-2.0
- **Repositorio**: [https://github.com/npm/cli](https://github.com/npm/cli)

#### KeePassXC

- **Desarrollador**: Equipo de KeePassXC
- **Sitio Web**: [https://keepassxc.org/](https://keepassxc.org/)
- **Licencia**: GPL-2.0 / GPL-3.0
- **Repositorio**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### lftp

- **Desarrollador**: Alexander V. Lukyanov
- **Sitio Web**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **Licencia**: GPL-3.0
- **Repositorio**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)

#### Samba (smbclient)

- **Desarrollador**: Equipo de Samba
- **Sitio Web**: [https://www.samba.org/](https://www.samba.org/)
- **Licencia**: GPL-3.0
- **Repositorio**: [https://github.com/samba-team/samba](https://github.com/samba-team/samba)

#### OpenSSH (scp/sshpass)

- **Desarrollador**: Proyecto OpenBSD
- **Sitio Web**: [https://www.openssh.com/](https://www.openssh.com/)
- **Licencia**: BSD 2-Clause
- **Repositorio**: [https://github.com/openssh/openssh-portable](https://github.com/openssh/openssh-portable)

#### Opcional: Paquetes NPM (si se usan)

- **basic-ftp**: [https://github.com/patrickjuchli/basic-ftp](https://github.com/patrickjuchli/basic-ftp)
- **ssh2-sftp-client**: [https://github.com/theophilusx/ssh2-sftp-client](https://github.com/theophilusx/ssh2-sftp-client)

---

<div align="center">

**📦 Node.js-Variante: Modern, asynchron, NPM-Ecosystem (optional)**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>
