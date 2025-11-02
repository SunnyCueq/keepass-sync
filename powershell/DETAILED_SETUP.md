# 📖 Detaillierte Installations- und Setup-Anleitung - PowerShell Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![PowerShell](https://img.shields.io/badge/PowerShell-5.1+-5391FE.svg?logo=powershell&logoColor=white)](https://docs.microsoft.com/powershell/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](.)

> **Cross-Platform - Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

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

<div align="center">

**💻 PowerShell-Variante: Cross-Platform, Windows-native, keine Dependencies**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

