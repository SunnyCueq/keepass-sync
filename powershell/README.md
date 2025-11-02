# 💻 KeePass Sync - PowerShell Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![PowerShell](https://img.shields.io/badge/PowerShell-5.1+-5391FE.svg)](https://docs.microsoft.com/powershell/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](.)

> **Cross-Platform PowerShell, Windows-native, auch auf Linux/macOS**

</div>

---

## 🇩🇪 Deutsch

### Vorteile der PowerShell-Variante

✅ **Cross-Platform**: Windows, Linux (PowerShell Core), macOS  
✅ **Windows-Native**: Ideal für Windows-Umgebungen  
✅ **Keine Dependencies**: Nur PowerShell nötig  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry-Logic**: Exponential Backoff  
✅ **Alle Protokolle**: FTP, SFTP, SMB, SCP

### Installation

#### 1. PowerShell installieren

**Windows:**
- PowerShell 5.1+ ist bereits vorinstalliert
- Oder PowerShell 7+ von https://github.com/PowerShell/PowerShell

**Linux:**
```bash
# PowerShell Core installieren
# Ubuntu/Debian
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y powershell

# Arch/CachyOS
sudo pacman -S powershell-bin

# Oder per Snap
sudo snap install powershell --classic
```

**macOS:**
```bash
brew install --cask powershell
```

#### 2. Script ausführen

```powershell
cd powershell

# Windows (PowerShell 5.1+)
.\sync.ps1

# PowerShell Core (alle Plattformen)
pwsh sync.ps1
```

#### 3. Ausführungsrichtlinie setzen (Windows)

```powershell
# Temporär für aktuelle Session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Oder dauerhaft (mit Vorsicht)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Verwendung

```powershell
# Normale Synchronisation
.\sync.ps1

# Verbindung testen
.\sync.ps1 -Test

# Status anzeigen
.\sync.ps1 -Status

# Alternative Config
.\sync.ps1 -Config "C:\pfad\zu\config.json"

# Version
.\sync.ps1 -Version

# Hilfe
.\sync.ps1 -Help
```

### Konfiguration

Die PowerShell-Variante nutzt die gleiche `config.json` wie die Python-Variante.

### Voraussetzungen

**Windows:**
- **PowerShell 5.1+** oder **PowerShell 7+**
- **KeePassXC-CLI**: Muss im PATH verfügbar sein
- **WinSCP.com**: Für FTP/SFTP (empfohlen)
- **lftp**: Alternative (via Git Bash/WSL)
- **Windows SMB**: Native Unterstützung

**Linux/macOS (PowerShell Core):**
- **PowerShell Core 6+**
- **KeePassXC-CLI**: Muss installiert sein
- **lftp**: Für FTP/SFTP
- **smbclient**: Für SMB
- **sshpass** & **scp**: Für SCP

### Protokolle

✅ **FTP**: Über WinSCP (Windows) oder lftp (Linux/macOS)  
✅ **SFTP**: Über WinSCP (Windows) oder lftp (Linux/macOS)  
✅ **SMB**: Über Windows `net use` (Windows) oder smbclient (Linux/macOS)  
✅ **SCP**: Über sshpass/scp (Linux/macOS)

### Unterschiede zur Python-Variante

- ❌ **Datei-Überwachung (`-Watch`)**: Noch nicht implementiert
- ✅ **Alle anderen Features**: Gleich wie Python-Variante
- ✅ **Windows-Integration**: Besser für Windows-Netzwerk-Shares

### Fehlerbehebung

**"Execution Policy verhindert Ausführung" (Windows)**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**"WinSCP.com nicht gefunden" (Windows)**
- Download von https://winscp.net/eng/download.php
- Oder nutze lftp (via Git Bash oder WSL)

**"lftp not found" (Linux/macOS)**
```bash
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS
brew install lftp      # macOS
```

### Vorteile

✅ **Windows-Native**: Ideal für Windows-Umgebungen  
✅ **Cross-Platform**: Funktioniert auch auf Linux/macOS  
✅ **Keine Python/Node.js**: Nur PowerShell nötig  
✅ **Integriert**: Gut mit Windows-Tools integriert

---

## 🇬🇧 English

### Advantages of PowerShell Variant

✅ **Cross-Platform**: Windows, Linux (PowerShell Core), macOS  
✅ **Windows-Native**: Ideal for Windows environments  
✅ **No Dependencies**: Only PowerShell needed  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry Logic**: Exponential backoff  
✅ **All Protocols**: FTP, SFTP, SMB, SCP

### Installation

#### 1. Install PowerShell

**Windows:**
- PowerShell 5.1+ is pre-installed
- Or PowerShell 7+ from https://github.com/PowerShell/PowerShell

**Linux:**
```bash
# Install PowerShell Core
sudo snap install powershell --classic
```

**macOS:**
```bash
brew install --cask powershell
```

#### 2. Run Script

```powershell
cd powershell
.\sync.ps1
```

### Usage

```powershell
# Normal synchronization
.\sync.ps1

# Test connection
.\sync.ps1 -Test

# Show status
.\sync.ps1 -Status

# Alternative config
.\sync.ps1 -Config "C:\path\to\config.json"
```

### Requirements

**Windows:**
- **PowerShell 5.1+** or **PowerShell 7+**
- **KeePassXC-CLI**: Must be available in PATH
- **WinSCP.com**: For FTP/SFTP (recommended)

**Linux/macOS (PowerShell Core):**
- **PowerShell Core 6+**
- **KeePassXC-CLI**: Must be installed
- **lftp**: For FTP/SFTP
- **smbclient**: For SMB
- **sshpass** & **scp**: For SCP

---

## 🇪🇸 Español

### Ventajas de la Variante PowerShell

✅ **Multiplataforma**: Windows, Linux (PowerShell Core), macOS  
✅ **Nativo de Windows**: Ideal para entornos Windows  
✅ **Sin Dependencias**: Solo PowerShell necesario  
✅ **Argumentos CLI**: `--test`, `--status`, etc.  
✅ **Lógica de Reintento**: Retroceso exponencial  
✅ **Todos los Protocolos**: FTP, SFTP, SMB, SCP

### Instalación

#### 1. Instalar PowerShell

**Windows:**
- PowerShell 5.1+ ya está preinstalado

**Linux:**
```bash
sudo snap install powershell --classic
```

**macOS:**
```bash
brew install --cask powershell
```

#### 2. Ejecutar Script

```powershell
cd powershell
.\sync.ps1
```

---

<div align="center">

**💻 PowerShell-Variante: Cross-Platform, Windows-native, keine Dependencies**

</div>

