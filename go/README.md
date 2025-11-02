# 🐹 KeePass Sync - Go (Golang) Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Go](https://img.shields.io/badge/Go-1.16+-00ADD8.svg)](https://golang.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Single binary, keine Abhängigkeiten, schnell und cross-platform**

</div>

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](./README.md) - Schnell, portabel | Fast, portable | Rápido, portable ⭐ **Hier**
- [📦 Node.js](../nodejs/README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript
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
2. [Go Installation](#go-installation)
3. [Externe Dependencies](#externe-dependencies)
4. [Kompilierung](#kompilierung)
5. [Konfiguration](#konfiguration)
6. [Verwendung](#verwendung)
7. [Fehlerbehebung](#fehlerbehebung)
8. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Linux** | Alle modernen Distributionen | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Erforderliche Software

1. **Go (Golang)**
   - **Minimale Version**: 1.16+
   - **Empfohlene Version**: 1.21+ (aktuellste stabile Version)
   - **Download**: [https://golang.org/dl/](https://golang.org/dl/)

2. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Externe Tools** (abhängig vom verwendeten Protokoll):
   - **lftp**: Für FTP/SFTP-Übertragungen
   - **smbclient**: Für SMB/CIFS-Netzwerk-Shares
   - **sshpass** & **scp**: Für SCP-Übertragungen

---

### 🚀 Go Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Installiere Go über pacman
sudo pacman -S go

# Überprüfe die Installation
go version
# Sollte zeigen: go version go1.21.x linux/amd64 (oder ähnlich)
```

**Paketname**: `go`  
**Repository**: Community  
**Link**: [Arch Linux Go Package](https://archlinux.org/packages/community/x86_64/go/)

##### Debian / Ubuntu

```bash
# Aktualisiere Paketliste
sudo apt update

# Installiere Go
sudo apt install golang-go

# Überprüfe die Installation
go version
```

**Paketname**: `golang-go`  
**Repository**: Main  
**Link**: [Debian Go Package](https://packages.debian.org/golang-go)

**Alternative: Neueste Version installieren**

```bash
# Entferne alte Version (falls vorhanden)
sudo apt remove golang-go

# Download neueste Version von golang.org
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz

# Entpacke nach /usr/local
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz

# Füge zu PATH hinzu (dauerhaft)
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Überprüfe
go version
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install golang
```

##### openSUSE

```bash
sudo zypper install go
```

#### macOS

##### Homebrew (Empfohlen)

```bash
# Installiere Homebrew (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installiere Go
brew install go

# Überprüfe
go version
```

**Link**: [Homebrew Go Formula](https://formulae.brew.sh/formula/go)

##### Manueller Download

```bash
# Download von golang.org
# https://golang.org/dl/

# Installiere .pkg Datei
# Oder via Terminal:
cd ~/Downloads
tar -C /usr/local -xzf go1.21.5.darwin-amd64.tar.gz

# Füge zu PATH hinzu
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

##### Installer Download

1. **Download**: [https://golang.org/dl/](https://golang.org/dl/)
2. **Wähle**: `go1.21.5.windows-amd64.msi`
3. **Führe Installer aus**: Folgen Sie den Anweisungen
4. **PATH wird automatisch gesetzt**

##### Überprüfung

```powershell
# PowerShell oder CMD
go version
```

##### Chocolatey (Alternative)

```powershell
# Installiere Chocolatey (falls nicht vorhanden)
# Siehe: https://chocolatey.org/install

# Installiere Go
choco install golang

# Überprüfe
go version
```

**Link**: [Chocolatey Go Package](https://community.chocolatey.org/packages/golang)

---

### 📦 Externe Dependencies

Die Go-Variante verwendet externe Tools für Datei-Übertragungen. Je nach verwendetem Protokoll müssen unterschiedliche Tools installiert werden.

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
# Homebrew
brew install keepassxc
```

##### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Installiere KeePassXC
3. Stelle sicher, dass `keepassxc-cli.exe` im PATH ist

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

**Option 2: Native Windows Port**

- Download: [http://lftp.tech/](http://lftp.tech/)
- Oder nutze WinSCP (siehe unten)

#### 3. smbclient (Für SMB/CIFS - Optional)

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

#### 4. sshpass & scp (Für SCP - Optional)

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

**Option 3: WinSCP** (GUI-Alternative)

- Download: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

---

### 🔨 Kompilierung

#### Schritt-für-Schritt Anleitung

##### 1. Repository klonen oder Dateien herunterladen

```bash
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync/go

# Option 2: Download ZIP
# Entpacke ZIP-Datei und navigiere zum go/ Verzeichnis
cd keepass-sync/go
```

##### 2. Überprüfe Go-Installation

```bash
go version
# Sollte zeigen: go version go1.16.x oder höher
```

##### 3. Kompiliere das Programm

```bash
# Einfache Kompilierung (für aktuelles System)
go build -o keepass-sync sync.go

# Mit zusätzlichen Flags (empfohlen)
go build -ldflags="-s -w" -o keepass-sync sync.go
```

**Erklärung der Flags**:
- `-ldflags="-s -w"`: Entfernt Debug-Informationen und verringert Dateigröße

##### 4. Überprüfe das kompilierte Binary

```bash
# Linux/macOS
./keepass-sync --version

# Windows
keepass-sync.exe --version
```

**Erwartete Ausgabe**: `KeePass Sync 1.1.0 (Go)`

#### Cross-Platform Kompilierung

##### Für Windows (von Linux/macOS)

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync.exe sync.go
```

##### Für Linux (von macOS/Windows)

```bash
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

##### Für macOS (von Linux/Windows)

```bash
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

##### Für ARM64 (Apple Silicon / Raspberry Pi)

```bash
# macOS ARM64
GOOS=darwin GOARCH=arm64 go build -ldflags="-s -w" -o keepass-sync sync.go

# Linux ARM64
GOOS=linux GOARCH=arm64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

#### Installation (Optional)

##### Linux / macOS

```bash
# Kopiere Binary nach /usr/local/bin
sudo cp keepass-sync /usr/local/bin/

# Setze Ausführungsrechte (normalerweise bereits gesetzt)
chmod +x /usr/local/bin/keepass-sync

# Teste
keepass-sync --version
```

##### Windows

1. Kopiere `keepass-sync.exe` nach `C:\Program Files\KeePass Sync\`
2. Füge Verzeichnis zu PATH hinzu:
   - Systemsteuerung → Umgebungsvariablen → PATH → Neu
   - Pfad: `C:\Program Files\KeePass Sync\`

---

### ⚙️ Konfiguration

Die Go-Variante nutzt die gleiche `config.json` wie die Python-Variante.

#### Erstelle config.json

```bash
cd ..  # Zurück zum Hauptverzeichnis
cp config.example.json config.json
nano config.json  # Oder anderen Editor verwenden
```

**Wichtige Einstellungen**:

```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-passwort",
    "type": "ftp",  // "ftp", "sftp", "smb", "scp"
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

```bash
# Normale Synchronisation
./keepass-sync

# Verbindung testen (ohne Sync)
./keepass-sync --test

# Status anzeigen
./keepass-sync --status

# Alternative Config-Datei
./keepass-sync --config /pfad/zu/config.json

# Version anzeigen
./keepass-sync --version

# Hilfe
./keepass-sync --help
```

#### Automatisierung

##### Cron (Linux/macOS)

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * /pfad/zum/keepass-sync
```

##### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Zeitplan
4. Aktion: Programm starten → `keepass-sync.exe`

---

### 🔍 Fehlerbehebung

#### "go: command not found"

**Problem**: Go ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Linux/macOS: Füge zu PATH hinzu
export PATH=$PATH:/usr/local/go/bin

# Dauerhaft in ~/.bashrc oder ~/.zshrc
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Installiere KeePassXC (siehe oben)
# Überprüfe Installation
which keepassxc-cli
# Oder:
keepassxc-cli version
```

#### "lftp not found"

**Problem**: lftp ist nicht installiert

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
sudo pacman -S samba        # Arch/CachyOS
```

#### Kompilierungsfehler

**Problem**: Alte Go-Version oder Syntax-Fehler

**Lösung**:
```bash
# Aktualisiere Go
# Überprüfe Version (min. 1.16)
go version

# Kompiliere mit mehr Informationen
go build -v sync.go
```

---

### 🙏 Danksagungen

#### Go (Golang)

- **Entwickler**: Google Go Team
- **Website**: [https://golang.org/](https://golang.org/)
- **Lizenz**: BSD 3-Clause
- **Repository**: [https://github.com/golang/go](https://github.com/golang/go)

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

---

## 🇬🇧 English

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Go Installation](#go-installation-1)
3. [External Dependencies](#external-dependencies)
4. [Compilation](#compilation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Troubleshooting](#troubleshooting)
8. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Linux** | All modern distributions | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Required Software

1. **Go (Golang)**
   - **Minimum Version**: 1.16+
   - **Recommended Version**: 1.21+ (latest stable version)
   - **Download**: [https://golang.org/dl/](https://golang.org/dl/)

2. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **External Tools** (depending on the protocol used):
   - **lftp**: For FTP/SFTP transfers
   - **smbclient**: For SMB/CIFS network shares
   - **sshpass** & **scp**: For SCP transfers

---

### 🚀 Go Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Install Go via pacman
sudo pacman -S go

# Verify installation
go version
# Should show: go version go1.21.x linux/amd64 (or similar)
```

**Package name**: `go`  
**Repository**: Community  
**Link**: [Arch Linux Go Package](https://archlinux.org/packages/community/x86_64/go/)

##### Debian / Ubuntu

```bash
# Update package list
sudo apt update

# Install Go
sudo apt install golang-go

# Verify installation
go version
```

**Package name**: `golang-go`  
**Repository**: Main  
**Link**: [Debian Go Package](https://packages.debian.org/golang-go)

**Alternative: Install Latest Version**

```bash
# Remove old version (if present)
sudo apt remove golang-go

# Download latest version from golang.org
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz

# Extract to /usr/local
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz

# Add to PATH (permanently)
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Verify
go version
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install golang
```

##### openSUSE

```bash
sudo zypper install go
```

#### macOS

##### Homebrew (Recommended)

```bash
# Install Homebrew (if not present)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Go
brew install go

# Verify
go version
```

**Link**: [Homebrew Go Formula](https://formulae.brew.sh/formula/go)

##### Manual Download

```bash
# Download from golang.org
# https://golang.org/dl/

# Install .pkg file
# Or via Terminal:
cd ~/Downloads
tar -C /usr/local -xzf go1.21.5.darwin-amd64.tar.gz

# Add to PATH
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

##### Installer Download

1. **Download**: [https://golang.org/dl/](https://golang.org/dl/)
2. **Choose**: `go1.21.5.windows-amd64.msi`
3. **Run installer**: Follow the instructions
4. **PATH is automatically set**

##### Verification

```powershell
# PowerShell or CMD
go version
```

##### Chocolatey (Alternative)

```powershell
# Install Chocolatey (if not present)
# See: https://chocolatey.org/install

# Install Go
choco install golang

# Verify
go version
```

**Link**: [Chocolatey Go Package](https://community.chocolatey.org/packages/golang)

---

### 📦 External Dependencies

The Go variant uses external tools for file transfers. Different tools must be installed depending on the protocol used.

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
# Homebrew
brew install keepassxc
```

##### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Install KeePassXC
3. Ensure `keepassxc-cli.exe` is in PATH

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

**Option 2: Native Windows Port**

- Download: [http://lftp.tech/](http://lftp.tech/)
- Or use WinSCP (see below)

#### 3. smbclient (For SMB/CIFS - Optional)

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

#### 4. sshpass & scp (For SCP - Optional)

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

**Option 3: WinSCP** (GUI Alternative)

- Download: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

---

### 🔨 Compilation

#### Step-by-Step Guide

##### 1. Clone repository or download files

```bash
# Option 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync/go

# Option 2: Download ZIP
# Extract ZIP file and navigate to go/ directory
cd keepass-sync/go
```

##### 2. Verify Go installation

```bash
go version
# Should show: go version go1.16.x or higher
```

##### 3. Compile the program

```bash
# Simple compilation (for current system)
go build -o keepass-sync sync.go

# With additional flags (recommended)
go build -ldflags="-s -w" -o keepass-sync sync.go
```

**Flag explanation**:
- `-ldflags="-s -w"`: Removes debug information and reduces file size

##### 4. Verify compiled binary

```bash
# Linux/macOS
./keepass-sync --version

# Windows
keepass-sync.exe --version
```

**Expected output**: `KeePass Sync 1.1.0 (Go)`

#### Cross-Platform Compilation

##### For Windows (from Linux/macOS)

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync.exe sync.go
```

##### For Linux (from macOS/Windows)

```bash
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

##### For macOS (from Linux/Windows)

```bash
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

##### For ARM64 (Apple Silicon / Raspberry Pi)

```bash
# macOS ARM64
GOOS=darwin GOARCH=arm64 go build -ldflags="-s -w" -o keepass-sync sync.go

# Linux ARM64
GOOS=linux GOARCH=arm64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

#### Installation (Optional)

##### Linux / macOS

```bash
# Copy binary to /usr/local/bin
sudo cp keepass-sync /usr/local/bin/

# Set execute permissions (usually already set)
chmod +x /usr/local/bin/keepass-sync

# Test
keepass-sync --version
```

##### Windows

1. Copy `keepass-sync.exe` to `C:\Program Files\KeePass Sync\`
2. Add directory to PATH:
   - Control Panel → Environment Variables → PATH → New
   - Path: `C:\Program Files\KeePass Sync\`

---

### ⚙️ Configuration

The Go variant uses the same `config.json` as the Python variant.

#### Create config.json

```bash
cd ..  # Back to main directory
cp config.example.json config.json
nano config.json  # Or use another editor
```

**Important settings**:

```json
{
  "ftp": {
    "host": "your-server.com",
    "user": "your-username",
    "password": "your-password",
    "type": "ftp",  // "ftp", "sftp", "smb", "scp"
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

```bash
# Normal synchronization
./keepass-sync

# Test connection (without sync)
./keepass-sync --test

# Show status
./keepass-sync --status

# Alternative config file
./keepass-sync --config /path/to/config.json

# Show version
./keepass-sync --version

# Help
./keepass-sync --help
```

#### Automation

##### Cron (Linux/macOS)

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * /path/to/keepass-sync
```

##### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Schedule
4. Action: Start program → `keepass-sync.exe`

---

### 🔍 Troubleshooting

#### "go: command not found"

**Problem**: Go is not installed or not in PATH

**Solution**:
```bash
# Linux/macOS: Add to PATH
export PATH=$PATH:/usr/local/go/bin

# Permanently in ~/.bashrc or ~/.zshrc
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI is not installed or not in PATH

**Solution**:
```bash
# Install KeePassXC (see above)
# Verify installation
which keepassxc-cli
# Or:
keepassxc-cli version
```

#### "lftp not found"

**Problem**: lftp is not installed

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
sudo pacman -S samba        # Arch/CachyOS
```

#### Compilation errors

**Problem**: Old Go version or syntax errors

**Solution**:
```bash
# Update Go
# Check version (min. 1.16)
go version

# Compile with more information
go build -v sync.go
```

---

### 🙏 Acknowledgments

#### Go (Golang)

- **Developer**: Google Go Team
- **Website**: [https://golang.org/](https://golang.org/)
- **License**: BSD 3-Clause
- **Repository**: [https://github.com/golang/go](https://github.com/golang/go)

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

---

## 🇪🇸 Español

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de Go](#instalación-de-go)
3. [Dependencias Externas](#dependencias-externas)
4. [Compilación](#compilación)
5. [Configuración](#configuración)
6. [Uso](#uso)
7. [Solución de Problemas](#solución-de-problemas)
8. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Linux** | Todas las distribuciones modernas | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Software Requerido

1. **Go (Golang)**
   - **Versión Mínima**: 1.16+
   - **Versión Recomendada**: 1.21+ (última versión estable)
   - **Descarga**: [https://golang.org/dl/](https://golang.org/dl/)

2. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Herramientas Externas** (según el protocolo utilizado):
   - **lftp**: Para transferencias FTP/SFTP
   - **smbclient**: Para recursos compartidos de red SMB/CIFS
   - **sshpass** & **scp**: Para transferencias SCP

---

### 🚀 Instalación de Go

#### Linux

##### Arch Linux / CachyOS

```bash
# Instalar Go vía pacman
sudo pacman -S go

# Verificar instalación
go version
# Debería mostrar: go version go1.21.x linux/amd64 (o similar)
```

**Nombre del paquete**: `go`  
**Repositorio**: Community  
**Enlace**: [Arch Linux Go Package](https://archlinux.org/packages/community/x86_64/go/)

##### Debian / Ubuntu

```bash
# Actualizar lista de paquetes
sudo apt update

# Instalar Go
sudo apt install golang-go

# Verificar instalación
go version
```

**Nombre del paquete**: `golang-go`  
**Repositorio**: Main  
**Enlace**: [Debian Go Package](https://packages.debian.org/golang-go)

**Alternativa: Instalar Versión Más Reciente**

```bash
# Eliminar versión anterior (si existe)
sudo apt remove golang-go

# Descargar versión más reciente de golang.org
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz

# Extraer a /usr/local
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz

# Añadir a PATH (permanentemente)
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Verificar
go version
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install golang
```

##### openSUSE

```bash
sudo zypper install go
```

#### macOS

##### Homebrew (Recomendado)

```bash
# Instalar Homebrew (si no está presente)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Go
brew install go

# Verificar
go version
```

**Enlace**: [Homebrew Go Formula](https://formulae.brew.sh/formula/go)

##### Descarga Manual

```bash
# Descargar de golang.org
# https://golang.org/dl/

# Instalar archivo .pkg
# O vía Terminal:
cd ~/Downloads
tar -C /usr/local -xzf go1.21.5.darwin-amd64.tar.gz

# Añadir a PATH
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

##### Descarga del Instalador

1. **Descarga**: [https://golang.org/dl/](https://golang.org/dl/)
2. **Elige**: `go1.21.5.windows-amd64.msi`
3. **Ejecuta el instalador**: Sigue las instrucciones
4. **PATH se establece automáticamente**

##### Verificación

```powershell
# PowerShell o CMD
go version
```

##### Chocolatey (Alternativa)

```powershell
# Instalar Chocolatey (si no está presente)
# Ver: https://chocolatey.org/install

# Instalar Go
choco install golang

# Verificar
go version
```

**Enlace**: [Chocolatey Go Package](https://community.chocolatey.org/packages/golang)

---

### 📦 Dependencias Externas

La variante Go utiliza herramientas externas para transferencias de archivos. Deben instalarse diferentes herramientas según el protocolo utilizado.

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
# Homebrew
brew install keepassxc
```

##### Windows

1. Descarga: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Instala KeePassXC
3. Asegúrate de que `keepassxc-cli.exe` esté en PATH

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

**Opción 2: Puerto Nativo de Windows**

- Descarga: [http://lftp.tech/](http://lftp.tech/)
- O usa WinSCP (ver abajo)

#### 3. smbclient (Para SMB/CIFS - Opcional)

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

#### 4. sshpass & scp (Para SCP - Opcional)

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

**Opción 3: WinSCP** (Alternativa GUI)

- Descarga: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

---

### 🔨 Compilación

#### Guía Paso a Paso

##### 1. Clonar repositorio o descargar archivos

```bash
# Opción 1: Git Clone
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync/go

# Opción 2: Descargar ZIP
# Extraer archivo ZIP y navegar al directorio go/
cd keepass-sync/go
```

##### 2. Verificar instalación de Go

```bash
go version
# Debería mostrar: go version go1.16.x o superior
```

##### 3. Compilar el programa

```bash
# Compilación simple (para sistema actual)
go build -o keepass-sync sync.go

# Con flags adicionales (recomendado)
go build -ldflags="-s -w" -o keepass-sync sync.go
```

**Explicación de flags**:
- `-ldflags="-s -w"`: Elimina información de depuración y reduce tamaño del archivo

##### 4. Verificar binario compilado

```bash
# Linux/macOS
./keepass-sync --version

# Windows
keepass-sync.exe --version
```

**Salida esperada**: `KeePass Sync 1.1.0 (Go)`

#### Compilación Multiplataforma

##### Para Windows (desde Linux/macOS)

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync.exe sync.go
```

##### Para Linux (desde macOS/Windows)

```bash
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

##### Para macOS (desde Linux/Windows)

```bash
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

##### Para ARM64 (Apple Silicon / Raspberry Pi)

```bash
# macOS ARM64
GOOS=darwin GOARCH=arm64 go build -ldflags="-s -w" -o keepass-sync sync.go

# Linux ARM64
GOOS=linux GOARCH=arm64 go build -ldflags="-s -w" -o keepass-sync sync.go
```

#### Instalación (Opcional)

##### Linux / macOS

```bash
# Copiar binario a /usr/local/bin
sudo cp keepass-sync /usr/local/bin/

# Establecer permisos de ejecución (normalmente ya establecidos)
chmod +x /usr/local/bin/keepass-sync

# Probar
keepass-sync --version
```

##### Windows

1. Copiar `keepass-sync.exe` a `C:\Program Files\KeePass Sync\`
2. Añadir directorio a PATH:
   - Panel de Control → Variables de Entorno → PATH → Nuevo
   - Ruta: `C:\Program Files\KeePass Sync\`

---

### ⚙️ Configuración

La variante Go utiliza el mismo `config.json` que la variante Python.

#### Crear config.json

```bash
cd ..  # Volver al directorio principal
cp config.example.json config.json
nano config.json  # O usar otro editor
```

**Configuraciones importantes**:

```json
{
  "ftp": {
    "host": "tu-servidor.com",
    "user": "tu-usuario",
    "password": "tu-contraseña",
    "type": "ftp",  // "ftp", "sftp", "smb", "scp"
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

```bash
# Sincronización normal
./keepass-sync

# Probar conexión (sin sincronizar)
./keepass-sync --test

# Mostrar estado
./keepass-sync --status

# Archivo de configuración alternativo
./keepass-sync --config /ruta/a/config.json

# Mostrar versión
./keepass-sync --version

# Ayuda
./keepass-sync --help
```

#### Automatización

##### Cron (Linux/macOS)

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * /ruta/a/keepass-sync
```

##### Programador de Tareas (Windows)

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. Desencadenador: Programación
4. Acción: Iniciar programa → `keepass-sync.exe`

---

### 🔍 Solución de Problemas

#### "go: command not found"

**Problema**: Go no está instalado o no está en PATH

**Solución**:
```bash
# Linux/macOS: Añadir a PATH
export PATH=$PATH:/usr/local/go/bin

# Permanentemente en ~/.bashrc o ~/.zshrc
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
```

#### "keepassxc-cli: command not found"

**Problema**: KeePassXC-CLI no está instalado o no está en PATH

**Solución**:
```bash
# Instalar KeePassXC (ver arriba)
# Verificar instalación
which keepassxc-cli
# O:
keepassxc-cli version
```

#### "lftp not found"

**Problema**: lftp no está instalado

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
sudo pacman -S samba        # Arch/CachyOS
```

#### Errores de compilación

**Problema**: Versión antigua de Go o errores de sintaxis

**Solución**:
```bash
# Actualizar Go
# Verificar versión (mín. 1.16)
go version

# Compilar con más información
go build -v sync.go
```

---

### 🙏 Agradecimientos

#### Go (Golang)

- **Desarrollador**: Equipo de Google Go
- **Sitio Web**: [https://golang.org/](https://golang.org/)
- **Licencia**: BSD 3-Clause
- **Repositorio**: [https://github.com/golang/go](https://github.com/golang/go)

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

---

<div align="center">

**🐹 Go-Variante: Schnell, portabel, keine Runtime-Abhängigkeiten**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>
