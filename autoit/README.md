# 🤖 KeePass Sync - AutoIt Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![AutoIt](https://img.shields.io/badge/AutoIt-3.3+-1C1C1C.svg)](https://www.autoitscript.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](.)

> **Windows-native, GUI-fähig, keine zusätzlichen Runtime-Umgebungen**

</div>

---

## 🇩🇪 Deutsch

### ⚠️ WICHTIG: Windows-Only

Die AutoIt-Variante läuft **NUR auf Windows**. Für Linux/macOS nutze die Python-, Go- oder Node.js-Variante.

### Vorteile der AutoIt-Variante

✅ **Windows-Native**: Keine Python/Node.js nötig  
✅ **GUI-Fähig**: Kann GUI-Dialoge anzeigen (nicht implementiert)  
✅ **Kompiliert**: Kann zu .exe kompiliert werden  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry-Logic**: Exponential Backoff  
✅ **Protokolle**: FTP, SFTP, SMB (SCP nicht unterstützt)

### Installation

#### 1. AutoIt installieren

```powershell
# Download von https://www.autoitscript.com/site/autoit/downloads/
# Oder per Chocolatey:
choco install autoit
```

#### 2. Kompilieren

```powershell
cd autoit

# Mit AutoIt3-Compiler
AutoIt3.exe /in sync.au3 /out sync.exe

# Oder mit Full SciTE-Editor:
# Öffne sync.au3 in SciTE
# Drücke F7 (Tools -> Compile)
```

#### 3. JSON.au3 Include

✅ **Die benötigten Dateien sind bereits enthalten:**
- `Json.au3` - JSON-Parser für AutoIt
- `BinaryCall.au3` - Dependency für Json.au3

Die Dateien liegen bereits im `autoit/` Verzeichnis und werden automatisch eingebunden.

### Verwendung

```powershell
# Normale Synchronisation
.\sync.exe

# Oder als .au3 Script
AutoIt3.exe sync.au3

# Verbindung testen
.\sync.exe --test

# Status anzeigen
.\sync.exe --status

# Alternative Config
.\sync.exe --config "C:\pfad\zu\config.json"
```

### Konfiguration

Die AutoIt-Variante nutzt die gleiche `config.json` wie die Python-Variante.

### Voraussetzungen

- **AutoIt 3.3+**: Muss installiert sein
- **KeePassXC-CLI**: Muss im PATH verfügbar sein
- **WinSCP.com**: Für FTP/SFTP (empfohlen)
- **lftp**: Alternative für FTP/SFTP (via Git Bash/WSL)
- **Windows SMB**: Native Unterstützung für SMB

### Protokolle

✅ **FTP**: Über WinSCP oder lftp  
✅ **SFTP**: Über WinSCP oder lftp  
✅ **SMB**: Über Windows `net use`  
❌ **SCP**: Nicht unterstützt (nutze SFTP)

### Unterschiede zur Python-Variante

- ❌ **Datei-Überwachung (`--watch`)**: Nicht implementiert
- ❌ **SCP**: Nicht unterstützt
- ✅ **Windows-Integration**: Besser für Windows-Umgebungen
- ✅ **GUI-Fähig**: Kann GUI-Dialoge anzeigen (später erweiterbar)

### Fehlerbehebung

**"JSON.au3 nicht gefunden"**
- Die Dateien `Json.au3` und `BinaryCall.au3` sind bereits im `autoit/` Verzeichnis enthalten
- Falls Probleme auftreten, stelle sicher, dass beide Dateien im selben Verzeichnis wie `sync.au3` liegen

**"WinSCP.com nicht gefunden"**
```powershell
# Download von https://winscp.net/eng/download.php
# Oder nutze lftp (via Git Bash oder WSL)
```

**"KeePassXC-CLI not found"**
```powershell
# Installiere KeePassXC von https://keepassxc.org/download/
# Stelle sicher, dass keepassxc-cli.exe im PATH ist
```

### Vorteil für Windows-User

Die AutoIt-Variante ist ideal für Windows-User, die:
- ✅ Keine Python/Node.js installieren möchten
- ✅ Native Windows-Tools bevorzugen
- ✅ GUI-Integration wünschen (später erweiterbar)

---

## 🇬🇧 English

### ⚠️ IMPORTANT: Windows-Only

The AutoIt variant runs **ONLY on Windows**. For Linux/macOS, use the Python, Go, or Node.js variant.

### Advantages of AutoIt Variant

✅ **Windows-Native**: No Python/Node.js needed  
✅ **GUI-Capable**: Can display GUI dialogs (not implemented)  
✅ **Compiled**: Can be compiled to .exe  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry Logic**: Exponential backoff  
✅ **Protocols**: FTP, SFTP, SMB (SCP not supported)

### Installation

#### 1. Install AutoIt

```powershell
# Download from https://www.autoitscript.com/site/autoit/downloads/
# Or via Chocolatey:
choco install autoit
```

#### 2. Compile

```powershell
cd autoit
AutoIt3.exe /in sync.au3 /out sync.exe
```

**Note:** The required `Json.au3` and `BinaryCall.au3` files are already included in the `autoit/` directory.

### Usage

```powershell
# Normal synchronization
.\sync.exe

# Or as .au3 script
AutoIt3.exe sync.au3

# Test connection
.\sync.exe --test

# Show status
.\sync.exe --status
```

### Requirements

- **AutoIt 3.3+**: Must be installed
- **KeePassXC-CLI**: Must be available in PATH
- **WinSCP.com**: For FTP/SFTP (recommended)
- **lftp**: Alternative for FTP/SFTP (via Git Bash/WSL)
- **Windows SMB**: Native support for SMB

### Protocols

✅ **FTP**: Via WinSCP or lftp  
✅ **SFTP**: Via WinSCP or lftp  
✅ **SMB**: Via Windows `net use`  
❌ **SCP**: Not supported (use SFTP)

---

## 🇪🇸 Español

### ⚠️ IMPORTANTE: Solo Windows

La variante AutoIt funciona **SOLO en Windows**. Para Linux/macOS, usa la variante Python, Go o Node.js.

### Ventajas de la Variante AutoIt

✅ **Nativo de Windows**: Sin necesidad de Python/Node.js  
✅ **Capaz de GUI**: Puede mostrar diálogos GUI (no implementado)  
✅ **Compilado**: Puede compilarse a .exe  
✅ **Argumentos CLI**: `--test`, `--status`, etc.  
✅ **Lógica de Reintento**: Retroceso exponencial  
✅ **Protocolos**: FTP, SFTP, SMB (SCP no soportado)

### Instalación

#### 1. Instalar AutoIt

```powershell
# Descargar de https://www.autoitscript.com/site/autoit/downloads/
```

#### 2. Compilar

```powershell
cd autoit
AutoIt3.exe /in sync.au3 /out sync.exe
```

---

<div align="center">

**🤖 AutoIt-Variante: Windows-native, GUI-fähig, keine Runtime nötig**

</div>

