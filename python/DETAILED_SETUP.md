# 📖 Detaillierte Installations- und Setup-Anleitung - Python Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Hauptvariante - Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

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

<div align="center">

**🐍 Python-Variante: Hauptvariante - Vollständigste Funktionalität**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

