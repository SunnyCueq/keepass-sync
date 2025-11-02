# 📦 KeePass Sync - Node.js/JavaScript Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Node.js](https://img.shields.io/badge/Node.js-12.0+-339933.svg)](https://nodejs.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Asynchron, event-driven, ideal für moderne JavaScript-Umgebungen**

</div>

---

## 🇩🇪 Deutsch

### Vorteile der Node.js-Variante

✅ **Asynchron**: Event-driven, nicht-blockierend  
✅ **Modern**: JavaScript ES6+, async/await  
✅ **NPM-Ecosystem**: Viele verfügbare Pakete  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry-Logic**: Exponential Backoff  
✅ **Alle Protokolle**: FTP, SFTP, SMB, SCP

### Installation

#### 1. Node.js installieren

```bash
# Linux (Arch/CachyOS)
sudo pacman -S nodejs npm

# Linux (Debian/Ubuntu)
sudo apt install nodejs npm

# macOS
brew install node

# Windows
# Download von https://nodejs.org/
```

#### 2. Script ausführen

```bash
cd nodejs

# Direkt ausführen (keine Dependencies nötig für Basis-Funktionalität)
node sync.js

# Oder mit npm (optional für erweiterte FTP-Funktionen)
npm install  # Installiert optionale Pakete (basic-ftp, ssh2-sftp-client)
```

#### 3. Ausführbar machen (Linux/macOS)

```bash
chmod +x sync.js
./sync.js
```

### Verwendung

```bash
# Normale Synchronisation
node sync.js

# Verbindung testen
node sync.js --test

# Status anzeigen
./sync.js --status

# Alternative Config
node sync.js --config /pfad/zu/config.json

# Hilfe
node sync.js --help
```

### Konfiguration

Die Node.js-Variante nutzt die gleiche `config.json` wie die Python-Variante.

### Voraussetzungen

- **Node.js 12.0+**: Muss installiert sein
- **KeePassXC-CLI**: Muss im PATH verfügbar sein
- **lftp**: Für FTP/SFTP (Linux/macOS)
- **smbclient**: Für SMB (Linux/macOS)
- **sshpass** & **scp**: Für SCP (Linux/macOS)
- **WinSCP** oder **lftp**: Für FTP/SFTP auf Windows

### Optionale NPM-Pakete

Für erweiterte FTP-Funktionen (falls lftp nicht verfügbar):

```bash
npm install basic-ftp ssh2-sftp-client
```

**Hinweis:** Die Variante funktioniert auch OHNE diese Pakete, nutzt dann lftp/externe Tools.

### Unterschiede zur Python-Variante

- ❌ **Datei-Überwachung (`--watch`)**: Noch nicht implementiert
- ✅ **Alle anderen Features**: Gleich wie Python-Variante
- ✅ **Asynchron**: Bessere Performance bei I/O-Operationen

### Fehlerbehebung

**"node: command not found"**
```bash
sudo apt install nodejs npm  # Debian/Ubuntu
sudo pacman -S nodejs npm    # Arch/CachyOS
```

---

## 🇬🇧 English

### Advantages of Node.js Variant

✅ **Asynchronous**: Event-driven, non-blocking  
✅ **Modern**: JavaScript ES6+, async/await  
✅ **NPM Ecosystem**: Many available packages  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry Logic**: Exponential backoff  
✅ **All Protocols**: FTP, SFTP, SMB, SCP

### Installation

#### 1. Install Node.js

```bash
# Linux (Arch/CachyOS)
sudo pacman -S nodejs npm

# Linux (Debian/Ubuntu)
sudo apt install nodejs npm

# macOS
brew install node

# Windows
# Download from https://nodejs.org/
```

#### 2. Run Script

```bash
cd nodejs
node sync.js
```

### Usage

```bash
# Normal synchronization
node sync.js

# Test connection
node sync.js --test

# Show status
node sync.js --status

# Alternative config
node sync.js --config /path/to/config.json

# Help
node sync.js --help
```

### Requirements

- **Node.js 12.0+**: Must be installed
- **KeePassXC-CLI**: Must be available in PATH
- **lftp**: For FTP/SFTP (Linux/macOS)
- **smbclient**: For SMB (Linux/macOS)
- **sshpass** & **scp**: For SCP (Linux/macOS)
- **WinSCP** or **lftp**: For FTP/SFTP on Windows

---

## 🇪🇸 Español

### Ventajas de la Variante Node.js

✅ **Asíncrono**: Basado en eventos, no bloqueante  
✅ **Moderno**: JavaScript ES6+, async/await  
✅ **Ecosistema NPM**: Muchos paquetes disponibles  
✅ **Argumentos CLI**: `--test`, `--status`, etc.  
✅ **Lógica de Reintento**: Retroceso exponencial  
✅ **Todos los Protocolos**: FTP, SFTP, SMB, SCP

### Instalación

#### 1. Instalar Node.js

```bash
# Linux (Arch/CachyOS)
sudo pacman -S nodejs npm

# Linux (Debian/Ubuntu)
sudo apt install nodejs npm

# macOS
brew install node
```

#### 2. Ejecutar Script

```bash
cd nodejs
node sync.js
```

---

<div align="center">

**📦 Node.js-Variante: Modern, asynchron, NPM-Ecosystem**

</div>

