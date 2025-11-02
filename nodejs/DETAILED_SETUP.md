# 📖 Detaillierte Installations- und Setup-Anleitung - Node.js/JavaScript Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Node.js](https://img.shields.io/badge/Node.js-12.0+-339933.svg?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

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

<div align="center">

**📦 Node.js-Variante: Modern, asynchron, NPM-Ecosystem (optional)**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

