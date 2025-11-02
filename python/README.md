# 🐍 KeePass Sync - Python Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Hauptvariante - Vollständige Funktionalität, erweiterte Features**

</div>

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](./README.md) - Hauptvariante | Main variant | Variante principal ⭐ **Hier**
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
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
2. [Python Installation](#python-installation)
3. [Python Packages Installation](#python-packages-installation)
4. [Externe Dependencies](#externe-dependencies)
5. [Konfiguration](#konfiguration)
6. [Verwendung](#verwendung)
7. [Erweiterte Features](#erweiterte-features)
8. [Fehlerbehebung](#fehlerbehebung)
9. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Linux** | Alle modernen Distributionen | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Erforderliche Software

1. **Python**
   - **Minimale Version**: 3.6+
   - **Empfohlene Version**: 3.11+ (aktuellste stabile Version)
   - **Download**: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **pip** (Python Package Manager)
   - Wird normalerweise mit Python installiert
   - **Minimale Version**: 21.0+
   - **Empfohlene Version**: 23.0+ (aktuellste Version)

4. **Externe Tools** (abhängig vom verwendeten Protokoll):
   - **lftp**: Für FTP/SFTP-Übertragungen (Linux/macOS)
   - **smbclient**: Für SMB/CIFS-Netzwerk-Shares (Linux/macOS)
   - **sshpass** & **scp**: Für SCP-Übertragungen (Linux/macOS)
   - **WinSCP**: Für FTP/SFTP auf Windows (optional)

---

### 🐍 Python Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Installiere Python 3
sudo pacman -S python python-pip

# Überprüfe die Installation
python3 --version
# Sollte zeigen: Python 3.11.x (oder höher)

pip3 --version
# Sollte zeigen: pip 23.x.x
```

**Paketnamen**: 
- `python` - Python Interpreter
- `python-pip` - Python Package Manager

**Repository**: Extra/Community  
**Link**: [Arch Linux Python Package](https://archlinux.org/packages/extra/x86_64/python/)

##### Debian / Ubuntu

```bash
# Aktualisiere Paketliste
sudo apt update

# Installiere Python 3 und pip
sudo apt install python3 python3-pip python3-venv

# Überprüfe die Installation
python3 --version
pip3 --version
```

**Paketnamen**: 
- `python3` - Python Interpreter
- `python3-pip` - Python Package Manager
- `python3-venv` - Virtual Environment Support

**Repository**: Main  
**Link**: [Debian Python Package](https://packages.debian.org/python3)

**Alternative: Neueste Version von python.org**

```bash
# Für Python 3.11+ auf älteren Ubuntu/Debian Versionen
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install python3 python3-pip
```

##### openSUSE

```bash
sudo zypper install python3 python3-pip
```

#### macOS

##### Homebrew (Empfohlen)

```bash
# Installiere Homebrew (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installiere Python
brew install python3

# Überprüfe
python3 --version
pip3 --version
```

**Link**: [Homebrew Python Formula](https://formulae.brew.sh/formula/python@3.11)

**Hinweis**: macOS hat Python 2.7 vorinstalliert, aber Python 3 ist separat zu installieren.

##### Manueller Download

1. **Download**: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. **Wähle**: Python 3.11.x für macOS
3. **Führe .pkg Installer aus**: Folgen Sie den Anweisungen
4. **pip ist automatisch enthalten**

#### Windows

##### Installer Download (Empfohlen)

1. **Download**: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. **Wähle**: Python 3.11.x (Windows installer 64-bit)
3. **WICHTIG**: Bei Installation "Add Python to PATH" aktivieren!
4. **Führe Installer aus**: Folgen Sie den Anweisungen
5. **pip ist automatisch enthalten**

##### Überprüfung

```powershell
# PowerShell oder CMD
python --version
pip --version
```

##### Chocolatey (Alternative)

```powershell
# Installiere Chocolatey (falls nicht vorhanden)
# Siehe: https://chocolatey.org/install

# Installiere Python
choco install python3

# Überprüfe
python --version
pip --version
```

**Link**: [Chocolatey Python Package](https://community.chocolatey.org/packages/python3)

---

### 📦 Python Packages Installation

Die Python-Variante benötigt **optional** einige Python-Packages, abhängig von den verwendeten Features:

#### Optionale Packages (Feature-abhängig)

##### 1. pyinotify (Nur Linux - für Datei-Überwachung)

**Zweck**: Effiziente Datei-Überwachung auf Linux-Systemen

**Installation**:
```bash
pip3 install pyinotify
# Oder mit sudo (systemweit):
sudo pip3 install pyinotify
```

**Version**: 0.9.6+  
**Link**: [PyPI pyinotify](https://pypi.org/project/pyinotify/)  
**GitHub**: [https://github.com/seb-m/pyinotify](https://github.com/seb-m/pyinotify)

##### 2. watchdog (macOS/Windows - für Datei-Überwachung)

**Zweck**: Cross-Platform Datei-Überwachung

**Installation**:
```bash
# macOS/Linux
pip3 install watchdog

# Windows
pip install watchdog
```

**Version**: 3.0.0+  
**Link**: [PyPI watchdog](https://pypi.org/project/watchdog/)  
**GitHub**: [https://github.com/python-watchdog/watchdog](https://github.com/python-watchdog/watchdog)

##### 3. paramiko (Nur Windows - für SCP)

**Zweck**: SSH/SCP-Unterstützung auf Windows (Linux/macOS nutzen sshpass/scp)

**Installation**:
```bash
pip3 install paramiko
```

**Version**: 2.12.0+  
**Link**: [PyPI paramiko](https://pypi.org/project/paramiko/)  
**GitHub**: [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)

##### 4. pysmb (Nur Windows - für SMB)

**Zweck**: SMB/CIFS-Unterstützung auf Windows (Linux/macOS nutzen smbclient)

**Installation**:
```bash
pip3 install pysmb
```

**Version**: 1.2.9+  
**Link**: [PyPI pysmb](https://pypi.org/project/pysmb/)  
**GitHub**: [https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)

#### Installations-Übersicht

**Minimal (nur Basis-Funktionalität)**:
```bash
# Keine Python-Packages erforderlich!
# Script nutzt externe Tools (lftp, smbclient, etc.)
```

**Mit Datei-Überwachung (empfohlen)**:
```bash
# Linux
pip3 install pyinotify

# macOS/Windows
pip3 install watchdog
```

**Mit Windows SCP/SMB-Unterstützung**:
```bash
# Nur auf Windows
pip3 install paramiko pysmb
```

**Alle Features (vollständig)**:
```bash
# Linux
pip3 install pyinotify

# macOS
pip3 install watchdog

# Windows
pip3 install watchdog paramiko pysmb
```

#### Virtual Environment (Empfohlen für isolierte Installation)

```bash
# Erstelle Virtual Environment
python3 -m venv venv

# Aktiviere Virtual Environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Installiere Packages (falls gewünscht)
pip install pyinotify  # Linux
pip install watchdog   # macOS/Windows
pip install paramiko pysmb  # Windows (optional)
```

---

### 📦 Externe Dependencies

Die Python-Variante verwendet externe Tools für Datei-Übertragungen. Je nach verwendetem Protokoll müssen unterschiedliche Tools installiert werden.

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

Windows hat native SMB-Unterstützung. Für Python nutzt das Script `pysmb` (siehe oben).

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

**Option 3: paramiko** (Python-Package, siehe oben)

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
    "retry_delay": 5,
    "watch_delay": 30
  }
}
```

---

### 💻 Verwendung

#### Basis-Befehle

```bash
# Navigiere zum Python-Verzeichnis
cd python

# Normale Synchronisation
python3 sync_ftp.py

# Verbindung testen (ohne Sync)
python3 sync_ftp.py --test

# Status anzeigen
python3 sync_ftp.py --status

# Datei überwachen (automatischer Sync)
python3 sync_ftp.py --watch

# Alternative Config-Datei
python3 sync_ftp.py --config /pfad/zu/config.json

# Version anzeigen
python3 sync_ftp.py --version

# Hilfe
python3 sync_ftp.py --help
```

#### Automatisierung

##### Cron (Linux/macOS)

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * cd /pfad/zum/projekt/python && python3 sync_ftp.py

# Oder mit Logging
0 * * * * cd /pfad/zum/projekt/python && python3 sync_ftp.py >> /pfad/zum/projekt/sync_cron.log 2>&1
```

##### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Zeitplan
4. Aktion: Programm starten
   - Programm: `python.exe`
   - Argumente: `C:\Pfad\zum\projekt\python\sync_ftp.py`
   - Start in: `C:\Pfad\zum\projekt\python`

##### Systemd Service (Linux)

```bash
# Erstelle Service-Datei
sudo nano /etc/systemd/system/keepass-sync.service
```

**Inhalt**:
```ini
[Unit]
Description=KeePass Sync Service
After=network.target

[Service]
Type=oneshot
User=dein-benutzer
WorkingDirectory=/pfad/zum/projekt/python
ExecStart=/usr/bin/python3 sync_ftp.py
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Aktivieren**:
```bash
sudo systemctl enable keepass-sync.service
sudo systemctl start keepass-sync.service
```

---

### 🎯 Erweiterte Features

#### Datei-Überwachung (--watch)

Die Python-Variante unterstützt automatische Synchronisation bei Datei-Änderungen:

```bash
# Starte Überwachung
python3 sync_ftp.py --watch

# Mit benutzerdefinierter Verzögerung (in config.json)
# "watch_delay": 30  # Sekunden
```

**Funktionsweise**:
- **Linux**: Nutzt `pyinotify` (falls installiert) oder Polling
- **macOS/Windows**: Nutzt `watchdog` (falls installiert) oder Polling

#### Retry-Logic

Automatische Wiederholung bei Fehlern mit Exponential Backoff:

```json
{
  "settings": {
    "max_retries": 3,      // Anzahl Wiederholungen
    "retry_delay": 5       // Basis-Verzögerung in Sekunden
  }
}
```

**Beispiel**: Bei Fehler wird nach 5s, 10s, 20s wiederholt (max. 60s).

---

### 🔍 Fehlerbehebung

#### "python3: command not found"

**Problem**: Python ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Linux: Installiere Python
sudo apt install python3  # Debian/Ubuntu
sudo pacman -S python     # Arch/CachyOS

# macOS
brew install python3

# Windows: Füge Python zu PATH hinzu
# Systemsteuerung → Umgebungsvariablen → PATH
```

#### "pip3: command not found"

**Problem**: pip ist nicht installiert

**Lösung**:
```bash
# Linux
sudo apt install python3-pip  # Debian/Ubuntu
sudo pacman -S python-pip     # Arch/CachyOS

# macOS
python3 -m ensurepip --upgrade

# Windows: pip sollte mit Python installiert werden
python -m ensurepip --upgrade
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

#### "ModuleNotFoundError: No module named 'pyinotify'"

**Problem**: pyinotify ist nicht installiert (nur bei --watch auf Linux)

**Lösung**:
```bash
pip3 install pyinotify
```

**Hinweis**: Script funktioniert auch ohne pyinotify (nutzt dann Polling).

#### "ModuleNotFoundError: No module named 'watchdog'"

**Problem**: watchdog ist nicht installiert (nur bei --watch auf macOS/Windows)

**Lösung**:
```bash
pip3 install watchdog
```

**Hinweis**: Script funktioniert auch ohne watchdog (nutzt dann Polling).

#### "ModuleNotFoundError: No module named 'paramiko'"

**Problem**: paramiko ist nicht installiert (nur bei SCP auf Windows)

**Lösung**:
```bash
pip3 install paramiko
```

**Hinweis**: Auf Linux/macOS nutzt das Script sshpass/scp (externes Tool).

#### "ModuleNotFoundError: No module named 'pysmb'"

**Problem**: pysmb ist nicht installiert (nur bei SMB auf Windows)

**Lösung**:
```bash
pip3 install pysmb
```

**Hinweis**: Auf Linux/macOS nutzt das Script smbclient (externes Tool).

---

### 🙏 Danksagungen

#### Python

- **Entwickler**: Python Software Foundation
- **Website**: [https://www.python.org/](https://www.python.org/)
- **Lizenz**: PSF License
- **Repository**: [https://github.com/python/cpython](https://github.com/python/cpython)

#### KeePassXC

- **Entwickler**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **Lizenz**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### pyinotify

- **Entwickler**: seb-m
- **Website**: [https://github.com/seb-m/pyinotify](https://github.com/seb-m/pyinotify)
- **Lizenz**: MIT
- **PyPI**: [https://pypi.org/project/pyinotify/](https://pypi.org/project/pyinotify/)

#### watchdog

- **Entwickler**: python-watchdog Team
- **Website**: [https://github.com/python-watchdog/watchdog](https://github.com/python-watchdog/watchdog)
- **Lizenz**: Apache 2.0
- **PyPI**: [https://pypi.org/project/watchdog/](https://pypi.org/project/watchdog/)

#### paramiko

- **Entwickler**: paramiko Team
- **Website**: [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)
- **Lizenz**: LGPL
- **PyPI**: [https://pypi.org/project/paramiko/](https://pypi.org/project/paramiko/)

#### pysmb

- **Entwickler**: Michael Teo
- **Website**: [https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)
- **Lizenz**: GPL
- **PyPI**: [https://pypi.org/project/pysmb/](https://pypi.org/project/pysmb/)

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
2. [Python Installation](#python-installation-1)
3. [Python Packages Installation](#python-packages-installation)
4. [External Dependencies](#external-dependencies)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Advanced Features](#advanced-features)
8. [Troubleshooting](#troubleshooting)
9. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Linux** | All modern distributions | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Required Software

1. **Python**
   - **Minimum Version**: 3.6+
   - **Recommended Version**: 3.11+ (latest stable version)
   - **Download**: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **pip** (Python Package Manager)
   - Usually installed with Python
   - **Minimum Version**: 21.0+
   - **Recommended Version**: 23.0+ (latest version)

4. **External Tools** (depending on the protocol used):
   - **lftp**: For FTP/SFTP transfers (Linux/macOS)
   - **smbclient**: For SMB/CIFS network shares (Linux/macOS)
   - **sshpass** & **scp**: For SCP transfers (Linux/macOS)
   - **WinSCP**: For FTP/SFTP on Windows (optional)

---

### 🐍 Python Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Install Python 3
sudo pacman -S python python-pip

# Verify installation
python3 --version
# Should show: Python 3.11.x (or higher)

pip3 --version
# Should show: pip 23.x.x
```

**Package names**: 
- `python` - Python Interpreter
- `python-pip` - Python Package Manager

**Repository**: Extra/Community  
**Link**: [Arch Linux Python Package](https://archlinux.org/packages/extra/x86_64/python/)

##### Debian / Ubuntu

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

**Package names**: 
- `python3` - Python Interpreter
- `python3-pip` - Python Package Manager
- `python3-venv` - Virtual Environment Support

**Repository**: Main  
**Link**: [Debian Python Package](https://packages.debian.org/python3)

**Alternative: Latest Version from python.org**

```bash
# For Python 3.11+ on older Ubuntu/Debian versions
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install python3 python3-pip
```

##### openSUSE

```bash
sudo zypper install python3 python3-pip
```

#### macOS

##### Homebrew (Recommended)

```bash
# Install Homebrew (if not present)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3

# Verify
python3 --version
pip3 --version
```

**Link**: [Homebrew Python Formula](https://formulae.brew.sh/formula/python@3.11)

**Note**: macOS has Python 2.7 pre-installed, but Python 3 must be installed separately.

##### Manual Download

1. **Download**: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. **Choose**: Python 3.11.x for macOS
3. **Run .pkg installer**: Follow the instructions
4. **pip is automatically included**

#### Windows

##### Installer Download (Recommended)

1. **Download**: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. **Choose**: Python 3.11.x (Windows installer 64-bit)
3. **IMPORTANT**: Enable "Add Python to PATH" during installation!
4. **Run installer**: Follow the instructions
5. **pip is automatically included**

##### Verification

```powershell
# PowerShell or CMD
python --version
pip --version
```

##### Chocolatey (Alternative)

```powershell
# Install Chocolatey (if not present)
# See: https://chocolatey.org/install

# Install Python
choco install python3

# Verify
python --version
pip --version
```

**Link**: [Chocolatey Python Package](https://community.chocolatey.org/packages/python3)

---

### 📦 Python Packages Installation

The Python variant requires **optional** Python packages, depending on the features used:

#### Optional Packages (Feature-dependent)

##### 1. pyinotify (Linux only - for file monitoring)

**Purpose**: Efficient file monitoring on Linux systems

**Installation**:
```bash
pip3 install pyinotify
# Or with sudo (system-wide):
sudo pip3 install pyinotify
```

**Version**: 0.9.6+  
**Link**: [PyPI pyinotify](https://pypi.org/project/pyinotify/)  
**GitHub**: [https://github.com/seb-m/pyinotify](https://github.com/seb-m/pyinotify)

##### 2. watchdog (macOS/Windows - for file monitoring)

**Purpose**: Cross-platform file monitoring

**Installation**:
```bash
# macOS/Linux
pip3 install watchdog

# Windows
pip install watchdog
```

**Version**: 3.0.0+  
**Link**: [PyPI watchdog](https://pypi.org/project/watchdog/)  
**GitHub**: [https://github.com/python-watchdog/watchdog](https://github.com/python-watchdog/watchdog)

##### 3. paramiko (Windows only - for SCP)

**Purpose**: SSH/SCP support on Windows (Linux/macOS use sshpass/scp)

**Installation**:
```bash
pip3 install paramiko
```

**Version**: 2.12.0+  
**Link**: [PyPI paramiko](https://pypi.org/project/paramiko/)  
**GitHub**: [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)

##### 4. pysmb (Windows only - for SMB)

**Purpose**: SMB/CIFS support on Windows (Linux/macOS use smbclient)

**Installation**:
```bash
pip3 install pysmb
```

**Version**: 1.2.9+  
**Link**: [PyPI pysmb](https://pypi.org/project/pysmb/)  
**GitHub**: [https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)

#### Installation Overview

**Minimal (basic functionality only)**:
```bash
# No Python packages required!
# Script uses external tools (lftp, smbclient, etc.)
```

**With file monitoring (recommended)**:
```bash
# Linux
pip3 install pyinotify

# macOS/Windows
pip3 install watchdog
```

**With Windows SCP/SMB support**:
```bash
# Windows only
pip3 install paramiko pysmb
```

**All features (complete)**:
```bash
# Linux
pip3 install pyinotify

# macOS
pip3 install watchdog

# Windows
pip3 install watchdog paramiko pysmb
```

#### Virtual Environment (Recommended for isolated installation)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Install packages (if desired)
pip install pyinotify  # Linux
pip install watchdog   # macOS/Windows
pip install paramiko pysmb  # Windows (optional)
```

---

### 📦 External Dependencies

The Python variant uses external tools for file transfers. Different tools must be installed depending on the protocol used.

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

Windows has native SMB support. For Python, the script uses `pysmb` (see above).

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

**Option 3: paramiko** (Python package, see above)

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
    "retry_delay": 5,
    "watch_delay": 30
  }
}
```

---

### 💻 Usage

#### Basic Commands

```bash
# Navigate to Python directory
cd python

# Normal synchronization
python3 sync_ftp.py

# Test connection (without sync)
python3 sync_ftp.py --test

# Show status
python3 sync_ftp.py --status

# Watch file (automatic sync)
python3 sync_ftp.py --watch

# Alternative config file
python3 sync_ftp.py --config /path/to/config.json

# Show version
python3 sync_ftp.py --version

# Help
python3 sync_ftp.py --help
```

#### Automation

##### Cron (Linux/macOS)

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * cd /path/to/project/python && python3 sync_ftp.py

# Or with logging
0 * * * * cd /path/to/project/python && python3 sync_ftp.py >> /path/to/project/sync_cron.log 2>&1
```

##### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Schedule
4. Action: Start program
   - Program: `python.exe`
   - Arguments: `C:\Path\to\project\python\sync_ftp.py`
   - Start in: `C:\Path\to\project\python`

##### Systemd Service (Linux)

```bash
# Create service file
sudo nano /etc/systemd/system/keepass-sync.service
```

**Content**:
```ini
[Unit]
Description=KeePass Sync Service
After=network.target

[Service]
Type=oneshot
User=your-user
WorkingDirectory=/path/to/project/python
ExecStart=/usr/bin/python3 sync_ftp.py
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Enable**:
```bash
sudo systemctl enable keepass-sync.service
sudo systemctl start keepass-sync.service
```

---

### 🎯 Advanced Features

#### File Monitoring (--watch)

The Python variant supports automatic synchronization on file changes:

```bash
# Start monitoring
python3 sync_ftp.py --watch

# With custom delay (in config.json)
# "watch_delay": 30  # seconds
```

**How it works**:
- **Linux**: Uses `pyinotify` (if installed) or polling
- **macOS/Windows**: Uses `watchdog` (if installed) or polling

#### Retry Logic

Automatic retry on errors with exponential backoff:

```json
{
  "settings": {
    "max_retries": 3,      // Number of retries
    "retry_delay": 5       // Base delay in seconds
  }
}
```

**Example**: On error, retries after 5s, 10s, 20s (max. 60s).

---

### 🔍 Troubleshooting

#### "python3: command not found"

**Problem**: Python is not installed or not in PATH

**Solution**:
```bash
# Linux: Install Python
sudo apt install python3  # Debian/Ubuntu
sudo pacman -S python     # Arch/CachyOS

# macOS
brew install python3

# Windows: Add Python to PATH
# Control Panel → Environment Variables → PATH
```

#### "pip3: command not found"

**Problem**: pip is not installed

**Solution**:
```bash
# Linux
sudo apt install python3-pip  # Debian/Ubuntu
sudo pacman -S python-pip     # Arch/CachyOS

# macOS
python3 -m ensurepip --upgrade

# Windows: pip should be installed with Python
python -m ensurepip --upgrade
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

#### "ModuleNotFoundError: No module named 'pyinotify'"

**Problem**: pyinotify is not installed (only for --watch on Linux)

**Solution**:
```bash
pip3 install pyinotify
```

**Note**: Script works without pyinotify (uses polling then).

#### "ModuleNotFoundError: No module named 'watchdog'"

**Problem**: watchdog is not installed (only for --watch on macOS/Windows)

**Solution**:
```bash
pip3 install watchdog
```

**Note**: Script works without watchdog (uses polling then).

#### "ModuleNotFoundError: No module named 'paramiko'"

**Problem**: paramiko is not installed (only for SCP on Windows)

**Solution**:
```bash
pip3 install paramiko
```

**Note**: On Linux/macOS, the script uses sshpass/scp (external tool).

#### "ModuleNotFoundError: No module named 'pysmb'"

**Problem**: pysmb is not installed (only for SMB on Windows)

**Solution**:
```bash
pip3 install pysmb
```

**Note**: On Linux/macOS, the script uses smbclient (external tool).

---

### 🙏 Acknowledgments

#### Python

- **Developer**: Python Software Foundation
- **Website**: [https://www.python.org/](https://www.python.org/)
- **License**: PSF License
- **Repository**: [https://github.com/python/cpython](https://github.com/python/cpython)

#### KeePassXC

- **Developer**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **License**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### pyinotify

- **Developer**: seb-m
- **Website**: [https://github.com/seb-m/pyinotify](https://github.com/seb-m/pyinotify)
- **License**: MIT
- **PyPI**: [https://pypi.org/project/pyinotify/](https://pypi.org/project/pyinotify/)

#### watchdog

- **Developer**: python-watchdog Team
- **Website**: [https://github.com/python-watchdog/watchdog](https://github.com/python-watchdog/watchdog)
- **License**: Apache 2.0
- **PyPI**: [https://pypi.org/project/watchdog/](https://pypi.org/project/watchdog/)

#### paramiko

- **Developer**: paramiko Team
- **Website**: [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)
- **License**: LGPL
- **PyPI**: [https://pypi.org/project/paramiko/](https://pypi.org/project/paramiko/)

#### pysmb

- **Developer**: Michael Teo
- **Website**: [https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)
- **License**: GPL
- **PyPI**: [https://pypi.org/project/pysmb/](https://pypi.org/project/pysmb/)

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
2. [Instalación de Python](#instalación-de-python)
3. [Instalación de Paquetes Python](#instalación-de-paquetes-python)
4. [Dependencias Externas](#dependencias-externas)
5. [Configuración](#configuración)
6. [Uso](#uso)
7. [Características Avanzadas](#características-avanzadas)
8. [Solución de Problemas](#solución-de-problemas)
9. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Linux** | Todas las distribuciones modernas | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Software Requerido

1. **Python**
   - **Versión Mínima**: 3.6+
   - **Versión Recomendada**: 3.11+ (última versión estable)
   - **Descarga**: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **pip** (Gestor de Paquetes Python)
   - Normalmente se instala con Python
   - **Versión Mínima**: 21.0+
   - **Versión Recomendada**: 23.0+ (última versión)

4. **Herramientas Externas** (según el protocolo utilizado):
   - **lftp**: Para transferencias FTP/SFTP (Linux/macOS)
   - **smbclient**: Para recursos compartidos de red SMB/CIFS (Linux/macOS)
   - **sshpass** & **scp**: Para transferencias SCP (Linux/macOS)
   - **WinSCP**: Para FTP/SFTP en Windows (opcional)

---

### 🐍 Instalación de Python

#### Linux

##### Arch Linux / CachyOS

```bash
# Instalar Python 3
sudo pacman -S python python-pip

# Verificar instalación
python3 --version
# Debería mostrar: Python 3.11.x (o superior)

pip3 --version
# Debería mostrar: pip 23.x.x
```

**Nombres de paquetes**: 
- `python` - Intérprete Python
- `python-pip` - Gestor de Paquetes Python

**Repositorio**: Extra/Community  
**Enlace**: [Arch Linux Python Package](https://archlinux.org/packages/extra/x86_64/python/)

##### Debian / Ubuntu

```bash
# Actualizar lista de paquetes
sudo apt update

# Instalar Python 3 y pip
sudo apt install python3 python3-pip python3-venv

# Verificar instalación
python3 --version
pip3 --version
```

**Nombres de paquetes**: 
- `python3` - Intérprete Python
- `python3-pip` - Gestor de Paquetes Python
- `python3-venv` - Soporte de Entorno Virtual

**Repositorio**: Main  
**Enlace**: [Debian Python Package](https://packages.debian.org/python3)

**Alternativa: Versión Más Reciente de python.org**

```bash
# Para Python 3.11+ en versiones anteriores de Ubuntu/Debian
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

##### Fedora / RHEL / CentOS

```bash
sudo dnf install python3 python3-pip
```

##### openSUSE

```bash
sudo zypper install python3 python3-pip
```

#### macOS

##### Homebrew (Recomendado)

```bash
# Instalar Homebrew (si no está presente)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python3

# Verificar
python3 --version
pip3 --version
```

**Enlace**: [Homebrew Python Formula](https://formulae.brew.sh/formula/python@3.11)

**Nota**: macOS tiene Python 2.7 preinstalado, pero Python 3 debe instalarse por separado.

##### Descarga Manual

1. **Descarga**: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. **Elige**: Python 3.11.x para macOS
3. **Ejecuta el instalador .pkg**: Sigue las instrucciones
4. **pip está incluido automáticamente**

#### Windows

##### Descarga del Instalador (Recomendado)

1. **Descarga**: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. **Elige**: Python 3.11.x (instalador Windows 64-bit)
3. **IMPORTANTE**: ¡Activa "Add Python to PATH" durante la instalación!
4. **Ejecuta el instalador**: Sigue las instrucciones
5. **pip está incluido automáticamente**

##### Verificación

```powershell
# PowerShell o CMD
python --version
pip --version
```

##### Chocolatey (Alternativa)

```powershell
# Instalar Chocolatey (si no está presente)
# Ver: https://chocolatey.org/install

# Instalar Python
choco install python3

# Verificar
python --version
pip --version
```

**Enlace**: [Chocolatey Python Package](https://community.chocolatey.org/packages/python3)

---

### 📦 Instalación de Paquetes Python

La variante Python requiere **opcionalmente** algunos paquetes Python, dependiendo de las características utilizadas:

#### Paquetes Opcionales (dependientes de características)

##### 1. pyinotify (Solo Linux - para monitoreo de archivos)

**Propósito**: Monitoreo eficiente de archivos en sistemas Linux

**Instalación**:
```bash
pip3 install pyinotify
# O con sudo (sistema completo):
sudo pip3 install pyinotify
```

**Versión**: 0.9.6+  
**Enlace**: [PyPI pyinotify](https://pypi.org/project/pyinotify/)  
**GitHub**: [https://github.com/seb-m/pyinotify](https://github.com/seb-m/pyinotify)

##### 2. watchdog (macOS/Windows - para monitoreo de archivos)

**Propósito**: Monitoreo multiplataforma de archivos

**Instalación**:
```bash
# macOS/Linux
pip3 install watchdog

# Windows
pip install watchdog
```

**Versión**: 3.0.0+  
**Enlace**: [PyPI watchdog](https://pypi.org/project/watchdog/)  
**GitHub**: [https://github.com/python-watchdog/watchdog](https://github.com/python-watchdog/watchdog)

##### 3. paramiko (Solo Windows - para SCP)

**Propósito**: Soporte SSH/SCP en Windows (Linux/macOS usan sshpass/scp)

**Instalación**:
```bash
pip3 install paramiko
```

**Versión**: 2.12.0+  
**Enlace**: [PyPI paramiko](https://pypi.org/project/paramiko/)  
**GitHub**: [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)

##### 4. pysmb (Solo Windows - para SMB)

**Propósito**: Soporte SMB/CIFS en Windows (Linux/macOS usan smbclient)

**Instalación**:
```bash
pip3 install pysmb
```

**Versión**: 1.2.9+  
**Enlace**: [PyPI pysmb](https://pypi.org/project/pysmb/)  
**GitHub**: [https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)

#### Resumen de Instalación

**Mínimo (solo funcionalidad básica)**:
```bash
# ¡No se requieren paquetes Python!
# El script utiliza herramientas externas (lftp, smbclient, etc.)
```

**Con monitoreo de archivos (recomendado)**:
```bash
# Linux
pip3 install pyinotify

# macOS/Windows
pip3 install watchdog
```

**Con soporte SCP/SMB para Windows**:
```bash
# Solo Windows
pip3 install paramiko pysmb
```

**Todas las características (completo)**:
```bash
# Linux
pip3 install pyinotify

# macOS
pip3 install watchdog

# Windows
pip3 install watchdog paramiko pysmb
```

#### Entorno Virtual (Recomendado para instalación aislada)

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Instalar paquetes (si se desea)
pip install pyinotify  # Linux
pip install watchdog   # macOS/Windows
pip install paramiko pysmb  # Windows (opcional)
```

---

### 📦 Dependencias Externas

La variante Python utiliza herramientas externas para transferencias de archivos. Deben instalarse diferentes herramientas según el protocolo utilizado.

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

Windows tiene soporte SMB nativo. Para Python, el script usa `pysmb` (ver arriba).

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

**Opción 3: paramiko** (Paquete Python, ver arriba)

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
    "retry_delay": 5,
    "watch_delay": 30
  }
}
```

---

### 💻 Uso

#### Comandos Básicos

```bash
# Navegar al directorio Python
cd python

# Sincronización normal
python3 sync_ftp.py

# Probar conexión (sin sincronizar)
python3 sync_ftp.py --test

# Mostrar estado
python3 sync_ftp.py --status

# Monitorear archivo (sincronización automática)
python3 sync_ftp.py --watch

# Archivo de configuración alternativo
python3 sync_ftp.py --config /ruta/a/config.json

# Mostrar versión
python3 sync_ftp.py --version

# Ayuda
python3 sync_ftp.py --help
```

#### Automatización

##### Cron (Linux/macOS)

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * cd /ruta/a/proyecto/python && python3 sync_ftp.py

# O con registro
0 * * * * cd /ruta/a/proyecto/python && python3 sync_ftp.py >> /ruta/a/proyecto/sync_cron.log 2>&1
```

##### Programador de Tareas (Windows)

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. Desencadenador: Programación
4. Acción: Iniciar programa
   - Programa: `python.exe`
   - Argumentos: `C:\Ruta\a\proyecto\python\sync_ftp.py`
   - Iniciar en: `C:\Ruta\a\proyecto\python`

##### Servicio Systemd (Linux)

```bash
# Crear archivo de servicio
sudo nano /etc/systemd/system/keepass-sync.service
```

**Contenido**:
```ini
[Unit]
Description=KeePass Sync Service
After=network.target

[Service]
Type=oneshot
User=tu-usuario
WorkingDirectory=/ruta/a/proyecto/python
ExecStart=/usr/bin/python3 sync_ftp.py
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Activar**:
```bash
sudo systemctl enable keepass-sync.service
sudo systemctl start keepass-sync.service
```

---

### 🎯 Características Avanzadas

#### Monitoreo de Archivos (--watch)

La variante Python admite sincronización automática en cambios de archivos:

```bash
# Iniciar monitoreo
python3 sync_ftp.py --watch

# Con retraso personalizado (en config.json)
# "watch_delay": 30  # segundos
```

**Funcionamiento**:
- **Linux**: Usa `pyinotify` (si está instalado) o polling
- **macOS/Windows**: Usa `watchdog` (si está instalado) o polling

#### Lógica de Reintento

Reintento automático en errores con retroceso exponencial:

```json
{
  "settings": {
    "max_retries": 3,      // Número de reintentos
    "retry_delay": 5       // Retraso base en segundos
  }
}
```

**Ejemplo**: En caso de error, reintenta después de 5s, 10s, 20s (máx. 60s).

---

### 🔍 Solución de Problemas

#### "python3: command not found"

**Problema**: Python no está instalado o no está en PATH

**Solución**:
```bash
# Linux: Instalar Python
sudo apt install python3  # Debian/Ubuntu
sudo pacman -S python     # Arch/CachyOS

# macOS
brew install python3

# Windows: Añadir Python a PATH
# Panel de Control → Variables de Entorno → PATH
```

#### "pip3: command not found"

**Problema**: pip no está instalado

**Solución**:
```bash
# Linux
sudo apt install python3-pip  # Debian/Ubuntu
sudo pacman -S python-pip     # Arch/CachyOS

# macOS
python3 -m ensurepip --upgrade

# Windows: pip debería instalarse con Python
python -m ensurepip --upgrade
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

#### "ModuleNotFoundError: No module named 'pyinotify'"

**Problema**: pyinotify no está instalado (solo para --watch en Linux)

**Solución**:
```bash
pip3 install pyinotify
```

**Nota**: El script funciona sin pyinotify (usa polling entonces).

#### "ModuleNotFoundError: No module named 'watchdog'"

**Problema**: watchdog no está instalado (solo para --watch en macOS/Windows)

**Solución**:
```bash
pip3 install watchdog
```

**Nota**: El script funciona sin watchdog (usa polling entonces).

#### "ModuleNotFoundError: No module named 'paramiko'"

**Problema**: paramiko no está instalado (solo para SCP en Windows)

**Solución**:
```bash
pip3 install paramiko
```

**Nota**: En Linux/macOS, el script usa sshpass/scp (herramienta externa).

#### "ModuleNotFoundError: No module named 'pysmb'"

**Problema**: pysmb no está instalado (solo para SMB en Windows)

**Solución**:
```bash
pip3 install pysmb
```

**Nota**: En Linux/macOS, el script usa smbclient (herramienta externa).

---

### 🙏 Agradecimientos

#### Python

- **Desarrollador**: Python Software Foundation
- **Sitio Web**: [https://www.python.org/](https://www.python.org/)
- **Licencia**: PSF License
- **Repositorio**: [https://github.com/python/cpython](https://github.com/python/cpython)

#### KeePassXC

- **Desarrollador**: Equipo de KeePassXC
- **Sitio Web**: [https://keepassxc.org/](https://keepassxc.org/)
- **Licencia**: GPL-2.0 / GPL-3.0
- **Repositorio**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### pyinotify

- **Desarrollador**: seb-m
- **Sitio Web**: [https://github.com/seb-m/pyinotify](https://github.com/seb-m/pyinotify)
- **Licencia**: MIT
- **PyPI**: [https://pypi.org/project/pyinotify/](https://pypi.org/project/pyinotify/)

#### watchdog

- **Desarrollador**: Equipo python-watchdog
- **Sitio Web**: [https://github.com/python-watchdog/watchdog](https://github.com/python-watchdog/watchdog)
- **Licencia**: Apache 2.0
- **PyPI**: [https://pypi.org/project/watchdog/](https://pypi.org/project/watchdog/)

#### paramiko

- **Desarrollador**: Equipo paramiko
- **Sitio Web**: [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)
- **Licencia**: LGPL
- **PyPI**: [https://pypi.org/project/paramiko/](https://pypi.org/project/paramiko/)

#### pysmb

- **Desarrollador**: Michael Teo
- **Sitio Web**: [https://github.com/miketeo/pysmb](https://github.com/miketeo/pysmb)
- **Licencia**: GPL
- **PyPI**: [https://pypi.org/project/pysmb/](https://pypi.org/project/pysmb/)

#### lftp

- **Desarrollador**: Alexander V. Lukyanov
- **Sitio Web**: [https://lftp.yar.ru/](https://lftp.yar.ru/)
- **Licenz**: GPL-3.0
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

**🐍 Python-Variante: Hauptvariante - Vollständigste Funktionalität**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

