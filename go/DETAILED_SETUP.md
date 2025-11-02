# 📖 Detaillierte Installations- und Setup-Anleitung - Go (Golang) Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Go](https://img.shields.io/badge/Go-1.16+-00ADD8.svg)](https://golang.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

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

<div align="center">

**🐹 Go-Variante: Schnell, portabel, keine Runtime-Abhängigkeiten**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

