# 💻 KeePass Sync - PowerShell Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![PowerShell](https://img.shields.io/badge/PowerShell-5.1+-5391FE.svg?logo=powershell&logoColor=white)](https://docs.microsoft.com/powershell/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](.)

> **Cross-Platform, Windows-native, keine Dependencies**

</div>

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
- [📦 Node.js](../nodejs/README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript
- [🤖 AutoIt](../autoit/README.md) - Windows-native | Windows-native | Windows nativo
- [💻 PowerShell](./README.md) - Windows-Scripting | Windows Scripting | Scripting Windows ⭐ **Hier**
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
2. [PowerShell Installation](#powershell-installation)
3. [Externe Dependencies](#externe-dependencies)
4. [Konfiguration](#konfiguration)
5. [Verwendung](#verwendung)
6. [Execution Policy](#execution-policy)
7. [Fehlerbehebung](#fehlerbehebung)
8. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Windows** | Windows 7+ | Windows 10/11 | x64 |
| **Linux** | Alle modernen Distributionen | Ubuntu 20.04+, Debian 11+, Arch Linux | x64, ARM64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x64, ARM64 (Apple Silicon) |

#### Erforderliche Software

1. **PowerShell**
   - **Windows**: PowerShell 5.1+ (vorinstalliert) oder PowerShell 7+
   - **Linux/macOS**: PowerShell Core 6+ oder PowerShell 7+
   - **Download**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

2. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Externe Tools** (abhängig vom verwendeten Protokoll):
   - **WinSCP**: Für FTP/SFTP auf Windows (empfohlen)
   - **lftp**: Für FTP/SFTP auf Linux/macOS
   - **smbclient**: Für SMB/CIFS-Netzwerk-Shares (Linux/macOS)
   - **sshpass** & **scp**: Für SCP-Übertragungen (Linux/macOS)
   - **Native Windows SMB**: Für SMB auf Windows (bereits integriert)

---

### 💻 PowerShell Installation

#### Windows

##### PowerShell 5.1 (Vorinstalliert)

Windows 10/11 haben PowerShell 5.1 bereits vorinstalliert.

**Überprüfung**:
```powershell
# PowerShell
$PSVersionTable.PSVersion
# Sollte zeigen: 5.1.x

# Oder
powershell --version
```

##### PowerShell 7+ (Empfohlen - Cross-Platform)

**Download**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

1. **Wähle**: Windows x64 Installer (.msi)
2. **Installiere**: Folgen Sie den Anweisungen
3. **Überprüfe**:
```powershell
pwsh --version
# Sollte zeigen: PowerShell 7.x.x
```

##### Chocolatey (Alternative)

```powershell
# Installiere PowerShell 7
choco install powershell-core

# Überprüfe
pwsh --version
```

**Link**: [Chocolatey PowerShell Package](https://community.chocolatey.org/packages/powershell-core)

##### Winget (Windows Package Manager)

```powershell
winget install Microsoft.PowerShell
```

#### Linux

##### Ubuntu / Debian

```bash
# PowerShell 7 Installation
# Download Microsoft GPG key
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

# Register Microsoft repository
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/microsoft-prod.list

# Aktualisiere Paketliste
sudo apt update

# Installiere PowerShell
sudo apt install powershell

# Überprüfe
pwsh --version
```

**Link**: [Microsoft PowerShell Installation Guide](https://learn.microsoft.com/powershell/scripting/install/install-ubuntu)

##### Arch Linux / CachyOS

```bash
# Installiere PowerShell
sudo pacman -S powershell-bin

# Oder AUR
yay -S powershell-bin

# Überprüfe
pwsh --version
```

**Link**: [Arch Linux PowerShell Package](https://aur.archlinux.org/packages/powershell-bin)

##### Fedora / RHEL / CentOS

```bash
# Register Microsoft repository
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo

# Installiere PowerShell
sudo dnf install powershell

# Überprüfe
pwsh --version
```

##### Snap (Universal)

```bash
# Installiere via Snap
sudo snap install powershell --classic

# Überprüfe
pwsh --version
```

#### macOS

##### Homebrew (Empfohlen)

```bash
# Installiere Homebrew (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installiere PowerShell
brew install --cask powershell

# Überprüfe
pwsh --version
```

**Link**: [Homebrew PowerShell Cask](https://formulae.brew.sh/cask/powershell)

##### Manueller Download

1. **Download**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)
2. **Wähle**: macOS .pkg Installer
3. **Installiere**: Folgen Sie den Anweisungen
4. **Überprüfe**: `pwsh --version`

---

### 📦 Externe Dependencies

#### 1. KeePassXC-CLI (ERFORDERLICH)

**Zweck**: Zum Mergen der KeePass-Datenbanken

##### Windows

1. **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. **Installiere**: Windows Installer (.msi)
3. **Stelle sicher**: `keepassxc-cli.exe` ist im PATH

**Überprüfung**:
```powershell
keepassxc-cli version
```

**Links**:
- **Offizielle Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

##### Linux

```bash
# Debian/Ubuntu
sudo apt install keepassxc

# Arch/CachyOS
sudo pacman -S keepassxc

# Fedora
sudo dnf install keepassxc
```

##### macOS

```bash
brew install keepassxc
```

#### 2. WinSCP (Für FTP/SFTP auf Windows - EMPFOHLEN)

**Zweck**: Datei-Übertragungen via FTP und SFTP

##### Windows Installation

1. **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)
2. **Installiere**: Windows Installer
3. **WICHTIG**: Stelle sicher, dass `WinSCP.com` im PATH ist

**Überprüfung**:
```powershell
WinSCP.com /version
```

**Links**:
- **WinSCP**: [https://winscp.net/](https://winscp.net/)
- **Dokumentation**: [https://winscp.net/eng/docs/start](https://winscp.net/eng/docs/start)

#### 3. lftp (Für FTP/SFTP auf Linux/macOS - EMPFOHLEN)

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
- **GitHub**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)

##### macOS

```bash
brew install lftp
```

#### 4. smbclient (Für SMB/CIFS auf Linux/macOS - Optional)

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

**Links**:
- **Samba**: [https://www.samba.org/](https://www.samba.org/)

##### macOS

```bash
brew install samba
```

**Hinweis**: Windows hat native SMB-Unterstützung über `net use`.

#### 5. sshpass & scp (Für SCP auf Linux/macOS - Optional)

**Zweck**: Sichere Datei-Übertragungen via SSH

##### Linux

```bash
# Debian/Ubuntu
sudo apt install sshpass openssh-client

# Arch/CachyOS
sudo pacman -S sshpass openssh
```

**Links**:
- **sshpass**: [https://sourceforge.net/projects/sshpass/](https://sourceforge.net/projects/sshpass/)
- **OpenSSH**: [https://www.openssh.com/](https://www.openssh.com/)

##### macOS

```bash
# scp ist bereits installiert
brew install hudochenkov/sshpass/sshpass
```

---

### ⚙️ Konfiguration

#### 1. Repository klonen oder Dateien herunterladen

```powershell
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Option 2: Download ZIP
# Entpacke ZIP-Datei
```

#### 2. Erstelle config.json

```powershell
# Kopiere Beispiel-Config
Copy-Item config.example.json config.json

# Bearbeite config.json
notepad config.json  # Oder anderen Editor
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

---

### 💻 Verwendung

#### Basis-Befehle

```powershell
# Navigiere zum powershell-Verzeichnis
cd powershell

# Normale Synchronisation
.\sync.ps1

# Verbindung testen
.\sync.ps1 -Test

# Status anzeigen
.\sync.ps1 -Status

# Alternative Config
.\sync.ps1 -Config "C:\Pfad\zu\config.json"

# Version
.\sync.ps1 -Version

# Hilfe
.\sync.ps1 -Help
```

#### Mit PowerShell Core (pwsh)

```powershell
# PowerShell 7+
pwsh sync.ps1

# Mit Argumenten
pwsh sync.ps1 -Test
```

#### Automatisierung

##### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Zeitplan
4. Aktion: Programm starten
   - Programm: `powershell.exe` (oder `pwsh.exe`)
   - Argumente: `-File "C:\Pfad\zum\sync.ps1"`
   - Start in: `C:\Pfad\zum\powershell`

##### Cron (Linux/macOS)

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * /usr/bin/pwsh /pfad/zum/powershell/sync.ps1
```

---

### 🔒 Execution Policy

#### Windows

PowerShell hat eine **Execution Policy**, die Scripts blockieren kann.

##### Überprüfung

```powershell
Get-ExecutionPolicy
```

##### Temporär ändern (für aktuelle Session)

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

##### Permanente Änderung (für aktuellen Benutzer)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Erklärung**:
- **Bypass**: Erlaubt alle Scripts (nur für aktuelle Session)
- **RemoteSigned**: Erlaubt lokale Scripts, Remote-Scripts müssen signiert sein (empfohlen)

##### Alternative: Script direkt ausführen

```powershell
# Umgeht Execution Policy
powershell -ExecutionPolicy Bypass -File sync.ps1
```

---

### 🔍 Fehlerbehebung

#### "Execution Policy verhindert Ausführung"

**Problem**: PowerShell blockiert Scripts

**Lösung**:
```powershell
# Siehe "Execution Policy" Abschnitt oben
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### "powershell: command not found" (Linux/macOS)

**Problem**: PowerShell Core ist nicht installiert

**Lösung**:
```bash
# Installiere PowerShell Core (siehe Installation oben)
# Dann nutze:
pwsh sync.ps1
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```powershell
# Windows: Füge zu PATH hinzu
# C:\Program Files\KeePassXC\

# Linux/macOS: Installiere über Paketmanager
```

#### "WinSCP.com nicht gefunden"

**Problem**: WinSCP ist nicht installiert oder nicht im PATH

**Lösung**:
```powershell
# Installiere WinSCP (siehe oben)
# Füge zu PATH hinzu: C:\Program Files (x86)\WinSCP\
```

#### "lftp not found" (Linux/macOS)

**Problem**: lftp ist nicht installiert

**Lösung**:
```bash
# Linux
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS

# macOS
brew install lftp
```

---

### 🙏 Danksagungen

#### PowerShell

- **Entwickler**: Microsoft
- **Website**: [https://docs.microsoft.com/powershell/](https://docs.microsoft.com/powershell/)
- **GitHub**: [https://github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell)
- **Lizenz**: MIT

#### KeePassXC

- **Entwickler**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **Lizenz**: GPL-2.0 / GPL-3.0

#### WinSCP

- **Entwickler**: Martin Přikryl
- **Website**: [https://winscp.net/](https://winscp.net/)
- **Lizenz**: GPL

#### lftp

- **Entwickler**: Alexander V. Lukyanov
- **Website**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **Lizenz**: GPL-3.0

#### Samba (smbclient)

- **Entwickler**: Samba Team
- **Website**: [https://www.samba.org/](https://www.samba.org/)
- **Lizenz**: GPL-3.0

#### OpenSSH (scp/sshpass)

- **Entwickler**: OpenBSD Project
- **Website**: [https://www.openssh.com/](https://www.openssh.com/)
- **Lizenz**: BSD 2-Clause

---

## 🇬🇧 English

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [PowerShell Installation](#powershell-installation-1)
3. [External Dependencies](#external-dependencies)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Execution Policy](#execution-policy-1)
7. [Troubleshooting](#troubleshooting)
8. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Windows** | Windows 7+ | Windows 10/11 | x64 |
| **Linux** | All modern distributions | Ubuntu 20.04+, Debian 11+, Arch Linux | x64, ARM64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x64, ARM64 (Apple Silicon) |

#### Required Software

1. **PowerShell**
   - **Windows**: PowerShell 5.1+ (pre-installed) or PowerShell 7+
   - **Linux/macOS**: PowerShell Core 6+ or PowerShell 7+
   - **Download**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

2. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **External Tools** (depending on the protocol used):
   - **WinSCP**: For FTP/SFTP on Windows (recommended)
   - **lftp**: For FTP/SFTP on Linux/macOS
   - **smbclient**: For SMB/CIFS network shares (Linux/macOS)
   - **sshpass** & **scp**: For SCP transfers (Linux/macOS)
   - **Native Windows SMB**: For SMB on Windows (already integrated)

---

### 💻 PowerShell Installation

#### Windows

##### PowerShell 5.1 (Pre-installed)

Windows 10/11 already have PowerShell 5.1 pre-installed.

**Verification**:
```powershell
# PowerShell
$PSVersionTable.PSVersion
# Should show: 5.1.x

# Or
powershell --version
```

##### PowerShell 7+ (Recommended - Cross-Platform)

**Download**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

1. **Choose**: Windows x64 Installer (.msi)
2. **Install**: Follow the instructions
3. **Verify**:
```powershell
pwsh --version
# Should show: PowerShell 7.x.x
```

##### Chocolatey (Alternative)

```powershell
# Install PowerShell 7
choco install powershell-core

# Verify
pwsh --version
```

**Link**: [Chocolatey PowerShell Package](https://community.chocolatey.org/packages/powershell-core)

##### Winget (Windows Package Manager)

```powershell
winget install Microsoft.PowerShell
```

#### Linux

##### Ubuntu / Debian

```bash
# PowerShell 7 Installation
# Download Microsoft GPG key
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

# Register Microsoft repository
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/microsoft-prod.list

# Update package list
sudo apt update

# Install PowerShell
sudo apt install powershell

# Verify
pwsh --version
```

**Link**: [Microsoft PowerShell Installation Guide](https://learn.microsoft.com/powershell/scripting/install/install-ubuntu)

##### Arch Linux / CachyOS

```bash
# Install PowerShell
sudo pacman -S powershell-bin

# Or AUR
yay -S powershell-bin

# Verify
pwsh --version
```

**Link**: [Arch Linux PowerShell Package](https://aur.archlinux.org/packages/powershell-bin)

##### Fedora / RHEL / CentOS

```bash
# Register Microsoft repository
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo

# Install PowerShell
sudo dnf install powershell

# Verify
pwsh --version
```

##### Snap (Universal)

```bash
# Install via Snap
sudo snap install powershell --classic

# Verify
pwsh --version
```

#### macOS

##### Homebrew (Recommended)

```bash
# Install Homebrew (if not present)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install PowerShell
brew install --cask powershell

# Verify
pwsh --version
```

**Link**: [Homebrew PowerShell Cask](https://formulae.brew.sh/cask/powershell)

##### Manual Download

1. **Download**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)
2. **Choose**: macOS .pkg Installer
3. **Install**: Follow the instructions
4. **Verify**: `pwsh --version`

---

### 📦 External Dependencies

#### 1. KeePassXC-CLI (REQUIRED)

**Purpose**: For merging KeePass databases

##### Windows

1. **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. **Install**: Windows Installer (.msi)
3. **Ensure**: `keepassxc-cli.exe` is in PATH

**Verification**:
```powershell
keepassxc-cli version
```

**Links**:
- **Official Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

##### Linux

```bash
# Debian/Ubuntu
sudo apt install keepassxc

# Arch/CachyOS
sudo pacman -S keepassxc

# Fedora
sudo dnf install keepassxc
```

##### macOS

```bash
brew install keepassxc
```

#### 2. WinSCP (For FTP/SFTP on Windows - RECOMMENDED)

**Purpose**: File transfers via FTP and SFTP

##### Windows Installation

1. **Download**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)
2. **Install**: Windows Installer
3. **IMPORTANT**: Ensure `WinSCP.com` is in PATH

**Verification**:
```powershell
WinSCP.com /version
```

**Links**:
- **WinSCP**: [https://winscp.net/](https://winscp.net/)
- **Documentation**: [https://winscp.net/eng/docs/start](https://winscp.net/eng/docs/start)

#### 3. lftp (For FTP/SFTP on Linux/macOS - RECOMMENDED)

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
- **GitHub**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)

##### macOS

```bash
brew install lftp
```

#### 4. smbclient (For SMB/CIFS on Linux/macOS - Optional)

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

**Links**:
- **Samba**: [https://www.samba.org/](https://www.samba.org/)

##### macOS

```bash
brew install samba
```

**Note**: Windows has native SMB support via `net use`.

#### 5. sshpass & scp (For SCP on Linux/macOS - Optional)

**Purpose**: Secure file transfers via SSH

##### Linux

```bash
# Debian/Ubuntu
sudo apt install sshpass openssh-client

# Arch/CachyOS
sudo pacman -S sshpass openssh
```

**Links**:
- **sshpass**: [https://sourceforge.net/projects/sshpass/](https://sourceforge.net/projects/sshpass/)
- **OpenSSH**: [https://www.openssh.com/](https://www.openssh.com/)

##### macOS

```bash
# scp is already installed
brew install hudochenkov/sshpass/sshpass
```

---

### ⚙️ Configuration

#### 1. Clone repository or download files

```powershell
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Option 2: Download ZIP
# Extract ZIP file
```

#### 2. Create config.json

```powershell
# Copy example config
Copy-Item config.example.json config.json

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

---

### 💻 Usage

#### Basic Commands

```powershell
# Navigate to powershell directory
cd powershell

# Normal synchronization
.\sync.ps1

# Test connection
.\sync.ps1 -Test

# Show status
.\sync.ps1 -Status

# Alternative config
.\sync.ps1 -Config "C:\Path\to\config.json"

# Version
.\sync.ps1 -Version

# Help
.\sync.ps1 -Help
```

#### With PowerShell Core (pwsh)

```powershell
# PowerShell 7+
pwsh sync.ps1

# With arguments
pwsh sync.ps1 -Test
```

#### Automation

##### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Schedule
4. Action: Start program
   - Program: `powershell.exe` (or `pwsh.exe`)
   - Arguments: `-File "C:\Path\to\sync.ps1"`
   - Start in: `C:\Path\to\powershell`

##### Cron (Linux/macOS)

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * /usr/bin/pwsh /path/to/powershell/sync.ps1
```

---

### 🔒 Execution Policy

#### Windows

PowerShell has an **Execution Policy** that can block scripts.

##### Verification

```powershell
Get-ExecutionPolicy
```

##### Change temporarily (for current session)

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

##### Permanent change (for current user)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Explanation**:
- **Bypass**: Allows all scripts (only for current session)
- **RemoteSigned**: Allows local scripts, remote scripts must be signed (recommended)

##### Alternative: Run script directly

```powershell
# Bypasses Execution Policy
powershell -ExecutionPolicy Bypass -File sync.ps1
```

---

### 🔍 Troubleshooting

#### "Execution Policy prevents script execution"

**Problem**: PowerShell blocks scripts

**Solution**:
```powershell
# See "Execution Policy" section above
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### "powershell: command not found" (Linux/macOS)

**Problem**: PowerShell Core is not installed

**Solution**:
```bash
# Install PowerShell Core (see installation above)
# Then use:
pwsh sync.ps1
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI is not installed or not in PATH

**Solution**:
```powershell
# Windows: Add to PATH
# C:\Program Files\KeePassXC\

# Linux/macOS: Install via package manager
```

#### "WinSCP.com not found"

**Problem**: WinSCP is not installed or not in PATH

**Solution**:
```powershell
# Install WinSCP (see above)
# Add to PATH: C:\Program Files (x86)\WinSCP\
```

#### "lftp not found" (Linux/macOS)

**Problem**: lftp is not installed

**Solution**:
```bash
# Linux
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS

# macOS
brew install lftp
```

---

### 🙏 Acknowledgments

#### PowerShell

- **Developer**: Microsoft
- **Website**: [https://docs.microsoft.com/powershell/](https://docs.microsoft.com/powershell/)
- **GitHub**: [https://github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell)
- **License**: MIT

#### KeePassXC

- **Developer**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **License**: GPL-2.0 / GPL-3.0

#### WinSCP

- **Developer**: Martin Přikryl
- **Website**: [https://winscp.net/](https://winscp.net/)
- **License**: GPL

#### lftp

- **Developer**: Alexander V. Lukyanov
- **Website**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **License**: GPL-3.0

#### Samba (smbclient)

- **Developer**: Samba Team
- **Website**: [https://www.samba.org/](https://www.samba.org/)
- **License**: GPL-3.0

#### OpenSSH (scp/sshpass)

- **Developer**: OpenBSD Project
- **Website**: [https://www.openssh.com/](https://www.openssh.com/)
- **License**: BSD 2-Clause

---

## 🇪🇸 Español

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de PowerShell](#instalación-de-powershell)
3. [Dependencias Externas](#dependencias-externas)
4. [Configuración](#configuración)
5. [Uso](#uso)
6. [Política de Ejecución](#política-de-ejecución)
7. [Solución de Problemas](#solución-de-problemas)
8. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Windows** | Windows 7+ | Windows 10/11 | x64 |
| **Linux** | Todas las distribuciones modernas | Ubuntu 20.04+, Debian 11+, Arch Linux | x64, ARM64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x64, ARM64 (Apple Silicon) |

#### Software Requerido

1. **PowerShell**
   - **Windows**: PowerShell 5.1+ (preinstalado) o PowerShell 7+
   - **Linux/macOS**: PowerShell Core 6+ o PowerShell 7+
   - **Descarga**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

2. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Herramientas Externas** (según el protocolo utilizado):
   - **WinSCP**: Para FTP/SFTP en Windows (recomendado)
   - **lftp**: Para FTP/SFTP en Linux/macOS
   - **smbclient**: Para recursos compartidos de red SMB/CIFS (Linux/macOS)
   - **sshpass** & **scp**: Para transferencias SCP (Linux/macOS)
   - **SMB Nativo de Windows**: Para SMB en Windows (ya integrado)

---

### 💻 Instalación de PowerShell

#### Windows

##### PowerShell 5.1 (Preinstalado)

Windows 10/11 ya tienen PowerShell 5.1 preinstalado.

**Verificación**:
```powershell
# PowerShell
$PSVersionTable.PSVersion
# Debería mostrar: 5.1.x

# O
powershell --version
```

##### PowerShell 7+ (Recomendado - Multiplataforma)

**Descarga**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)

1. **Elige**: Instalador Windows x64 (.msi)
2. **Instala**: Sigue las instrucciones
3. **Verifica**:
```powershell
pwsh --version
# Debería mostrar: PowerShell 7.x.x
```

##### Chocolatey (Alternativa)

```powershell
# Instalar PowerShell 7
choco install powershell-core

# Verificar
pwsh --version
```

**Enlace**: [Chocolatey PowerShell Package](https://community.chocolatey.org/packages/powershell-core)

##### Winget (Administrador de Paquetes de Windows)

```powershell
winget install Microsoft.PowerShell
```

#### Linux

##### Ubuntu / Debian

```bash
# Instalación de PowerShell 7
# Descargar clave GPG de Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

# Registrar repositorio de Microsoft
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/microsoft-prod.list

# Actualizar lista de paquetes
sudo apt update

# Instalar PowerShell
sudo apt install powershell

# Verificar
pwsh --version
```

**Enlace**: [Guía de Instalación de Microsoft PowerShell](https://learn.microsoft.com/powershell/scripting/install/install-ubuntu)

##### Arch Linux / CachyOS

```bash
# Instalar PowerShell
sudo pacman -S powershell-bin

# O AUR
yay -S powershell-bin

# Verificar
pwsh --version
```

**Enlace**: [Paquete Arch Linux PowerShell](https://aur.archlinux.org/packages/powershell-bin)

##### Fedora / RHEL / CentOS

```bash
# Registrar repositorio de Microsoft
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo

# Instalar PowerShell
sudo dnf install powershell

# Verificar
pwsh --version
```

##### Snap (Universal)

```bash
# Instalar vía Snap
sudo snap install powershell --classic

# Verificar
pwsh --version
```

#### macOS

##### Homebrew (Recomendado)

```bash
# Instalar Homebrew (si no está presente)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar PowerShell
brew install --cask powershell

# Verificar
pwsh --version
```

**Enlace**: [Homebrew PowerShell Cask](https://formulae.brew.sh/cask/powershell)

##### Descarga Manual

1. **Descarga**: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)
2. **Elige**: Instalador macOS .pkg
3. **Instala**: Sigue las instrucciones
4. **Verifica**: `pwsh --version`

---

### 📦 Dependencias Externas

#### 1. KeePassXC-CLI (REQUERIDO)

**Propósito**: Para fusionar bases de datos KeePass

##### Windows

1. **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. **Instala**: Instalador Windows (.msi)
3. **Asegúrate**: `keepassxc-cli.exe` está en PATH

**Verificación**:
```powershell
keepassxc-cli version
```

**Enlaces**:
- **Sitio Web Oficial**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

##### Linux

```bash
# Debian/Ubuntu
sudo apt install keepassxc

# Arch/CachyOS
sudo pacman -S keepassxc

# Fedora
sudo dnf install keepassxc
```

##### macOS

```bash
brew install keepassxc
```

#### 2. WinSCP (Para FTP/SFTP en Windows - RECOMENDADO)

**Propósito**: Transferencias de archivos vía FTP y SFTP

##### Instalación en Windows

1. **Descarga**: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)
2. **Instala**: Instalador Windows
3. **IMPORTANTE**: Asegúrate de que `WinSCP.com` esté en PATH

**Verificación**:
```powershell
WinSCP.com /version
```

**Enlaces**:
- **WinSCP**: [https://winscp.net/](https://winscp.net/)
- **Documentación**: [https://winscp.net/eng/docs/start](https://winscp.net/eng/docs/start)

#### 3. lftp (Para FTP/SFTP en Linux/macOS - RECOMENDADO)

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
- **GitHub**: [https://github.com/lavv17/lftp](https://github.com/lavv17/lftp)

##### macOS

```bash
brew install lftp
```

#### 4. smbclient (Para SMB/CIFS en Linux/macOS - Opcional)

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

**Enlaces**:
- **Samba**: [https://www.samba.org/](https://www.samba.org/)

##### macOS

```bash
brew install samba
```

**Nota**: Windows tiene soporte SMB nativo vía `net use`.

#### 5. sshpass & scp (Para SCP en Linux/macOS - Opcional)

**Propósito**: Transferencias seguras de archivos vía SSH

##### Linux

```bash
# Debian/Ubuntu
sudo apt install sshpass openssh-client

# Arch/CachyOS
sudo pacman -S sshpass openssh
```

**Enlaces**:
- **sshpass**: [https://sourceforge.net/projects/sshpass/](https://sourceforge.net/projects/sshpass/)
- **OpenSSH**: [https://www.openssh.com/](https://www.openssh.com/)

##### macOS

```bash
# scp ya está instalado
brew install hudochenkov/sshpass/sshpass
```

---

### ⚙️ Configuración

#### 1. Clonar repositorio o descargar archivos

```powershell
# Opción 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Opción 2: Descargar ZIP
# Extraer archivo ZIP
```

#### 2. Crear config.json

```powershell
# Copiar config de ejemplo
Copy-Item config.example.json config.json

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

---

### 💻 Uso

#### Comandos Básicos

```powershell
# Navegar al directorio powershell
cd powershell

# Sincronización normal
.\sync.ps1

# Probar conexión
.\sync.ps1 -Test

# Mostrar estado
.\sync.ps1 -Status

# Config alternativo
.\sync.ps1 -Config "C:\Ruta\a\config.json"

# Versión
.\sync.ps1 -Version

# Ayuda
.\sync.ps1 -Help
```

#### Con PowerShell Core (pwsh)

```powershell
# PowerShell 7+
pwsh sync.ps1

# Con argumentos
pwsh sync.ps1 -Test
```

#### Automatización

##### Programador de Tareas (Windows)

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. Desencadenador: Programación
4. Acción: Iniciar programa
   - Programa: `powershell.exe` (o `pwsh.exe`)
   - Argumentos: `-File "C:\Ruta\a\sync.ps1"`
   - Iniciar en: `C:\Ruta\a\powershell`

##### Cron (Linux/macOS)

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * /usr/bin/pwsh /ruta/a/powershell/sync.ps1
```

---

### 🔒 Política de Ejecución

#### Windows

PowerShell tiene una **Política de Ejecución** que puede bloquear scripts.

##### Verificación

```powershell
Get-ExecutionPolicy
```

##### Cambiar temporalmente (para sesión actual)

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

##### Cambio permanente (para usuario actual)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Explicación**:
- **Bypass**: Permite todos los scripts (solo para sesión actual)
- **RemoteSigned**: Permite scripts locales, scripts remotos deben estar firmados (recomendado)

##### Alternativa: Ejecutar script directamente

```powershell
# Omite la Política de Ejecución
powershell -ExecutionPolicy Bypass -File sync.ps1
```

---

### 🔍 Solución de Problemas

#### "La Política de Ejecución impide la ejecución del script"

**Problema**: PowerShell bloquea scripts

**Solución**:
```powershell
# Ver sección "Política de Ejecución" arriba
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### "powershell: command not found" (Linux/macOS)

**Problema**: PowerShell Core no está instalado

**Solución**:
```bash
# Instalar PowerShell Core (ver instalación arriba)
# Luego usa:
pwsh sync.ps1
```

#### "keepassxc-cli: command not found"

**Problema**: KeePassXC-CLI no está instalado o no está en PATH

**Solución**:
```powershell
# Windows: Añadir a PATH
# C:\Program Files\KeePassXC\

# Linux/macOS: Instalar vía gestor de paquetes
```

#### "WinSCP.com no encontrado"

**Problema**: WinSCP no está instalado o no está en PATH

**Solución**:
```powershell
# Instalar WinSCP (ver arriba)
# Añadir a PATH: C:\Program Files (x86)\WinSCP\
```

#### "lftp not found" (Linux/macOS)

**Problema**: lftp no está instalado

**Solución**:
```bash
# Linux
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS

# macOS
brew install lftp
```

---

### 🙏 Agradecimientos

#### PowerShell

- **Desarrollador**: Microsoft
- **Sitio Web**: [https://docs.microsoft.com/powershell/](https://docs.microsoft.com/powershell/)
- **GitHub**: [https://github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell)
- **Licencia**: MIT

#### KeePassXC

- **Desarrollador**: Equipo de KeePassXC
- **Sitio Web**: [https://keepassxc.org/](https://keepassxc.org/)
- **Licencia**: GPL-2.0 / GPL-3.0

#### WinSCP

- **Desarrollador**: Martin Přikryl
- **Sitio Web**: [https://winscp.net/](https://winscp.net/)
- **Licencia**: GPL

#### lftp

- **Desarrollador**: Alexander V. Lukyanov
- **Sitio Web**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **Licenz**: GPL-3.0

#### Samba (smbclient)

- **Desarrollador**: Equipo de Samba
- **Sitio Web**: [https://www.samba.org/](https://www.samba.org/)
- **Licenza**: GPL-3.0

#### OpenSSH (scp/sshpass)

- **Desarrollador**: Proyecto OpenBSD
- **Sitio Web**: [https://www.openssh.com/](https://www.openssh.com/)
- **Licencia**: BSD 2-Clause

---

<div align="center">

**💻 PowerShell-Variante: Cross-Platform, Windows-native, keine Dependencies**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>
