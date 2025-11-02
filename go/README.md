# 🐹 KeePass Sync - Go (Golang) Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Go](https://img.shields.io/badge/Go-1.16+-00ADD8.svg)](https://golang.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Single binary, keine Abhängigkeiten, schnell und cross-platform**

</div>

---

## 🇩🇪 Deutsch

### Vorteile der Go-Variante

✅ **Single Binary**: Keine Python/Node.js-Abhängigkeiten nötig  
✅ **Schnell**: Kompiliert zu nativen Code  
✅ **Cross-Platform**: Ein Code, alle Plattformen  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry-Logic**: Exponential Backoff bei Fehlern  
✅ **Alle Protokolle**: FTP, SFTP, SMB, SCP

### Installation

#### 1. Go installieren

```bash
# Linux (Arch/CachyOS)
sudo pacman -S go

# Linux (Debian/Ubuntu)
sudo apt install golang-go

# macOS
brew install go

# Windows
# Download von https://golang.org/dl/
```

#### 2. Kompilieren

```bash
cd go
go build -o keepass-sync sync.go
```

**Cross-Platform Kompilierung:**

```bash
# Für Windows (von Linux/macOS)
GOOS=windows GOARCH=amd64 go build -o keepass-sync.exe sync.go

# Für Linux (von macOS/Windows)
GOOS=linux GOARCH=amd64 go build -o keepass-sync sync.go

# Für macOS (von Linux/Windows)
GOOS=darwin GOARCH=amd64 go build -o keepass-sync sync.go
```

#### 3. Installation (optional)

```bash
# Linux/macOS
sudo cp keepass-sync /usr/local/bin/

# Windows
# Kopiere keepass-sync.exe nach C:\Program Files\KeePass Sync\
```

### Verwendung

```bash
# Normale Synchronisation
./keepass-sync

# Verbindung testen
./keepass-sync --test

# Status anzeigen
./keepass-sync --status

# Alternative Config
./keepass-sync --config /pfad/zu/config.json

# Version
./keepass-sync --version
```

### Konfiguration

Die Go-Variante nutzt die gleiche `config.json` wie die Python-Variante:

```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-ftp-passwort",
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

### Voraussetzungen

- **KeePassXC-CLI**: Muss im PATH verfügbar sein
- **lftp**: Für FTP/SFTP (Linux/macOS)
- **smbclient**: Für SMB (Linux/macOS)
- **sshpass** & **scp**: Für SCP (Linux/macOS)
- **WinSCP** oder **lftp**: Für FTP/SFTP auf Windows

### Unterschiede zur Python-Variante

- ❌ **Datei-Überwachung (`--watch`)**: Noch nicht implementiert
- ✅ **Alle anderen Features**: Gleich wie Python-Variante
- ✅ **Performance**: Schneller (native Binary)
- ✅ **Abhängigkeiten**: Keine Python/Pip-Pakete nötig

### Fehlerbehebung

**"lftp not found"**
```bash
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS
```

**"KeePassXC-CLI not found"**
```bash
sudo apt install keepassxc  # Debian/Ubuntu
sudo pacman -S keepassxc    # Arch/CachyOS
```

---

## 🇬🇧 English

### Advantages of Go Variant

✅ **Single Binary**: No Python/Node.js dependencies needed  
✅ **Fast**: Compiled to native code  
✅ **Cross-Platform**: One code, all platforms  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry Logic**: Exponential backoff on errors  
✅ **All Protocols**: FTP, SFTP, SMB, SCP

### Installation

#### 1. Install Go

```bash
# Linux (Arch/CachyOS)
sudo pacman -S go

# Linux (Debian/Ubuntu)
sudo apt install golang-go

# macOS
brew install go

# Windows
# Download from https://golang.org/dl/
```

#### 2. Compile

```bash
cd go
go build -o keepass-sync sync.go
```

**Cross-Platform Compilation:**

```bash
# For Windows (from Linux/macOS)
GOOS=windows GOARCH=amd64 go build -o keepass-sync.exe sync.go

# For Linux (from macOS/Windows)
GOOS=linux GOARCH=amd64 go build -o keepass-sync sync.go

# For macOS (from Linux/Windows)
GOOS=darwin GOARCH=amd64 go build -o keepass-sync sync.go
```

#### 3. Installation (optional)

```bash
# Linux/macOS
sudo cp keepass-sync /usr/local/bin/

# Windows
# Copy keepass-sync.exe to C:\Program Files\KeePass Sync\
```

### Usage

```bash
# Normal synchronization
./keepass-sync

# Test connection
./keepass-sync --test

# Show status
./keepass-sync --status

# Alternative config
./keepass-sync --config /path/to/config.json

# Version
./keepass-sync --version
```

### Configuration

The Go variant uses the same `config.json` as the Python variant.

### Requirements

- **KeePassXC-CLI**: Must be available in PATH
- **lftp**: For FTP/SFTP (Linux/macOS)
- **smbclient**: For SMB (Linux/macOS)
- **sshpass** & **scp**: For SCP (Linux/macOS)
- **WinSCP** or **lftp**: For FTP/SFTP on Windows

### Differences from Python Variant

- ❌ **File Watching (`--watch`)**: Not yet implemented
- ✅ **All other features**: Same as Python variant
- ✅ **Performance**: Faster (native binary)
- ✅ **Dependencies**: No Python/Pip packages needed

---

## 🇪🇸 Español

### Ventajas de la Variante Go

✅ **Binario Único**: Sin dependencias de Python/Node.js  
✅ **Rápido**: Compilado a código nativo  
✅ **Multiplataforma**: Un código, todas las plataformas  
✅ **Argumentos CLI**: `--test`, `--status`, etc.  
✅ **Lógica de Reintento**: Retroceso exponencial en errores  
✅ **Todos los Protocolos**: FTP, SFTP, SMB, SCP

### Instalación

#### 1. Instalar Go

```bash
# Linux (Arch/CachyOS)
sudo pacman -S go

# Linux (Debian/Ubuntu)
sudo apt install golang-go

# macOS
brew install go

# Windows
# Descargar de https://golang.org/dl/
```

#### 2. Compilar

```bash
cd go
go build -o keepass-sync sync.go
```

### Uso

```bash
# Sincronización normal
./keepass-sync

# Probar conexión
./keepass-sync --test

# Mostrar estado
./keepass-sync --status
```

---

<div align="center">

**⚡ Go-Variante: Schnell, portabel, keine Abhängigkeiten**

</div>

