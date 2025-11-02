# 🔐 KeePass Sync - Synchronize Your Passwords Automatically

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](.)

> **Automatically synchronize your KeePass database between multiple computers via an FTP server.**

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🛠️ Installation](#️-installation) • [❓ FAQ](#-frequently-asked-questions) • [🤝 Contributing](#-contributing)

</div>

---

### 🚀 Quick Start

#### 1. Prerequisites

- **KeePassXC** installed (from [keepassxc.org](https://keepassxc.org/))
- **Python 3** installed (usually pre-installed on Linux/macOS)
- **FTP credentials** for your server

#### 2. Configuration

**Option A: Interactive Installer (Recommended for beginners)**
```bash
python3 install.py
```
or
```bash
python3 python/installer.py
```

The installer:
- ✅ Automatically detects your system
- ✅ Shows system specifications
- ✅ Automatically detects your language
- ✅ Guides you through configuration
- ✅ Supports all protocols (FTP, SFTP, SMB, SCP)
- ✅ Automatically creates `config.json`

**Option B: Manual Configuration**
```bash
cp config.example.json config.json
```

Then open `config.json` and enter your data:
```json
{
  "ftp": {
    "host": "your-server.com",
    "user": "your-username",
    "password": "your-password",
    "type": "ftp",
    "comment": "Protocol options: 'ftp' (default), 'sftp', 'smb', 'scp'",
    "remotePath": "/keepass_passwords.kdbx"
  },
  "keepass": {
    "databasePassword": "your-keepass-master-password"
  }
}
```

#### 3. Testing

**Linux:**
```bash
# Test wrapper (preferred)
python3 sync.py

# Or .sh file directly
./linux/sync_ftp.sh

# Or Python script directly (with debug)
python3 python/sync_ftp.py
```

**Expected Output on Success:**
```
2025-11-02 17:XX:XX === KeePass Sync - Linux ===
2025-11-02 17:XX:XX Creating backup...
2025-11-02 17:XX:XX Backup successfully created
2025-11-02 17:XX:XX Starting download from server...
2025-11-02 17:XX:XX Download successful
2025-11-02 17:XX:XX Performing merge...
2025-11-02 17:XX:XX Merge completed successfully. Local file updated.
2025-11-02 17:XX:XX Starting upload to server...
2025-11-02 17:XX:XX Upload completed successfully.
2025-11-02 17:XX:XX Synchronization completed.
```

**Troubleshooting:**
- **"Configuration file not found"** → Make sure `config.json` exists
- **"KeePassXC-CLI not found"** → Install: `sudo pacman -S keepassxc` (Arch) or `sudo apt install keepassxc` (Debian)
- **"FTP client not found"** → Install: `sudo pacman -S lftp` (Arch) or `sudo apt install lftp` (Debian)

📖 **Detailed Test Guide:** [TEST.md](TEST.md)

#### 4. Automatic Installation

**🚀 Quick Installation (Linux - Recommended):**
```bash
./linux/install.sh
```

This automatically installs:
- ✅ Systemd Service (on shutdown)
- ✅ Cron Job (on idle, every 5 minutes)

**Windows - Task Scheduler:**
1. Open Task Scheduler (`taskschd.msc`)
2. "Create Task..." → Name: `KeePass Sync`
3. Trigger: "At startup", "Daily" or "On idle"
4. Action: `powershell.exe` → Arguments: `-NoProfile -ExecutionPolicy Bypass -File "C:\Path\windows\sync_ftp.ps1"`

**macOS - LaunchAgent:**
```bash
# Create ~/Library/LaunchAgents/com.user.keepass-sync.plist
# See INSTALL.md for full instructions
```

📖 **Complete Installation Guide for All Platforms:** [INSTALL.md](INSTALL.md)

### 📖 What does the script do?

The script synchronizes your KeePass database in 4 steps:

1. **🔒 Create Backup** - Backs up your local file
2. **⬇️ Download** - Fetches the latest version from the server
3. **🔄 Merge** - Intelligently combines all changes
4. **⬆️ Upload** - Saves the updated file back

**Important:** The script does **not** delete data. It automatically combines all changes from all devices!

### 🌍 Multi-language Support

The script supports **12 languages**: German (de), English (en), Spanish (es), French (fr), Italian (it), Portuguese (pt), Dutch (nl), Polish (pl), Russian (ru), Chinese (zh), Japanese (ja), Korean (ko).

Language is automatically detected or can be set in `config.json`:
```json
{
  "settings": {
    "language": "en"
  }
}
```

### 🎯 CLI Options & Features

The script offers various options for different use cases:

**Test connection (without sync):**
```bash
python3 python/sync_ftp.py --test
```
- ✅ Checks KeePassXC-CLI availability
- ✅ Checks local database
- ✅ Tests server connection
- ✅ No backup needed, no data changes

**Show status:**
```bash
python3 python/sync_ftp.py --status
```
Shows:
- Local DB information (size, age)
- Backup overview
- Configuration details

**Auto-watch file:**
```bash
python3 python/sync_ftp.py --watch
```
- Automatically starts sync when local database changes
- Configurable delay (default: 30 seconds)
- Runs continuously in background

**Normal synchronization:**
```bash
python3 python/sync_ftp.py        # Standard sync
python3 python/sync_ftp.py --sync # Explicit sync
python3 python/sync_ftp.py -v     # Verbose (debug output)
python3 python/sync_ftp.py -q     # Quiet (errors only)
```

**More options:**
```bash
python3 python/sync_ftp.py --config alt_config.json  # Alternative config
python3 python/sync_ftp.py --help                     # Show help
python3 python/sync_ftp.py --version                  # Show version
```

### 🔄 Improved Retry Logic

The script automatically retries failed operations:
- **Exponential Backoff**: 5s → 10s → 20s → max 60s
- **Configurable** in `config.json`:
```json
{
  "settings": {
    "max_retries": 3,
    "retry_delay": 5
  }
}
```
- Resilient against temporary network errors

### 📡 Supported Protocols

The script supports multiple transfer protocols:

- **FTP** (Default) - File Transfer Protocol
- **SFTP** - SSH File Transfer Protocol (encrypted)
- **SMB/CIFS** - Windows Network Shares
- **SCP** - Secure Copy Protocol (SSH-based)

Choose the protocol in `config.json` with `"type": "ftp"` (or `sftp`, `smb`, `scp`).

```json
{
  "settings": {
    "language": "en"  // "de", "en", or "es"
  }
}
```

### ⚙️ Advanced Configuration

In `config.json` you can also configure:

- `maxBackups`: Number of backups (default: 2)
- `cleanupLogs`: Automatically delete old logs (default: true)
- `maxLogAgeDays`: Delete logs older than X days (default: 7)
- `debug`: Enable debug mode (default: false)

### ❓ Frequently Asked Questions

**Q: Will I lose data if I work on multiple devices simultaneously?**  
A: No! The script intelligently combines all changes. New passwords are adopted from all sides.

**Q: How often should I synchronize?**  
A: At least once daily. Best to set up automatically (see INSTALL.md).

**Q: What if the connection to the server fails?**  
A: The script creates a backup first. Your local file remains unchanged.

**Q: Does it work with more than 2 computers?**  
A: Yes! As many as you want. The FTP server is the central source.

### 📝 Logs & Backups

- **Logs:** `sync_log.txt` (automatically cleaned up)
- **Backups:** `backups/` (only the 2 newest are kept)
- **Temporary files:** Automatically deleted

### 🔐 Security

⚠️ **Important:**
- The `config.json` contains passwords in plain text
- Make sure the file is not publicly accessible
- Linux/macOS: `chmod 600 config.json`
- Windows: Set appropriate permissions

---

---

## 📁 Verzeichnisstruktur | Directory Structure | Estructura de Directorios

```
keepass-sync/
├── config.json          # Configuración (¡aquí ingresar tus datos!)
├── config.example.json   # Ejemplo de configuración
├── README.md             # Esta documentación
├── TEST.md               # Guía de pruebas
├── INSTALL.md            # Guía de instalación
├── sync.py               # Wrapper multiplataforma
├── python/               # Versión Python (preferida)
│   └── sync_ftp.py
├── linux/                # Scripts Linux
│   ├── sync_ftp.sh
│   └── install.sh        # Instalación rápida
├── windows/              # Scripts Windows
├── mac/                  # Scripts macOS
├── lang/                 # Archivos de idioma (JSON)
│   ├── de.json
│   ├── en.json
│   └── es.json
└── backups/              # Respaldos automáticos (solo 2 más recientes)
```

## 🤝 Mitwirken | Contributing | Contribuir

### 🌟 Möchtest du helfen? | Want to help? | ¿Quieres ayudar?

Wir freuen uns über Beiträge! | We welcome contributions! | ¡Agradecemos las contribuciones!

**Wie du helfen kannst | How you can help | Cómo puedes ayudar:**

- 🐛 **Fehler melden** | **Report bugs** | **Reportar errores**
  - Öffne ein Issue auf GitHub | Open an issue on GitHub | Abre un issue en GitHub
  - Beschreibe das Problem | Describe the problem | Describe el problema

- 💡 **Verbesserungen vorschlagen** | **Suggest improvements** | **Sugerir mejoras**
  - Neue Features | New features | Nuevas funcionalidades
  - Code-Optimierungen | Code optimizations | Optimizaciones de código
  - Dokumentation | Documentation | Documentación

- 🌍 **Übersetzungen** | **Translations** | **Traducciones**
  - Neue Sprachen hinzufügen | Add new languages | Añadir nuevos idiomas
  - Übersetzungen verbessern | Improve translations | Mejorar traducciones

- 💻 **Code beitragen** | **Contribute code** | **Contribuir código**
  - Fork das Repository | Fork the repository | Haz fork del repositorio
  - Erstelle einen Pull Request | Create a pull request | Crea un pull request

- 📖 **Dokumentation verbessern** | **Improve documentation** | **Mejorar documentación**
  - Fehlende Informationen hinzufügen | Add missing information | Añadir información faltante
  - Beispiele verbessern | Improve examples | Mejorar ejemplos

### 📝 Übersetzungen beitragen | Contributing Translations | Contribuir Traducciones

Übersetzungen sind in `lang/*.json` Dateien gespeichert.  
Translations are stored in `lang/*.json` files.  
Las traducciones se almacenan en archivos `lang/*.json`.

**Neue Sprache hinzufügen | Add new language | Añadir nuevo idioma:**

1. Kopiere `lang/en.json` als Vorlage | Copy `lang/en.json` as template | Copia `lang/en.json` como plantilla
2. Übersetze alle Werte | Translate all values | Traduce todos los valores
3. Erstelle `lang/[code].json` (z.B. `lang/fr.json`) | Create `lang/[code].json` (e.g. `lang/fr.json`) | Crea `lang/[code].json` (ej. `lang/fr.json`)
4. Erstelle Pull Request | Create pull request | Crea pull request

**Verfügbare Sprachcodes | Available language codes | Códigos de idioma disponibles:**
- `de` - Deutsch | German | Alemán
- `en` - English | Inglés
- `es` - Español | Spanish | Español
- `fr` - Français | French | Francés ✅
- `it` - Italiano | Italian | Italiano ✅
- `pt` - Português | Portuguese | Portugués ✅
- `nl` - Nederlands | Dutch | Neerlandés ✅
- `pl` - Polski | Polish | Polaco ✅
- `ru` - Русский | Russian | Ruso ✅
- `zh` - 中文 | Chinese | Chino ✅
- `ja` - 日本語 | Japanese | Japonés ✅
- `ko` - 한국어 | Korean | Coreano ✅

---

## 📚 Weitere Informationen | More Information | Más Información

- **Test-Anleitung | Test Guide | Guía de Pruebas:** [TEST.md](TEST.md)
- **Installation & Automatisierung | Installation & Automation | Instalación y Automatización:** [INSTALL.md](INSTALL.md)
- **Wie funktioniert die Synchronisation? | How does synchronization work? | ¿Cómo funciona la sincronización?** Siehe unten | See below | Ver abajo

---

## 🔄 Wie funktioniert die Synchronisation? | How Synchronization Works | ¿Cómo Funciona la Sincronización?

### System-Architektur | System Architecture | Arquitectura del Sistema

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Hauptsystem │     │              │     │  Subsystem  │
│   Desktop   │◄───►│  FTP-Server  │◄───►│   Laptop    │
│             │     │   (Zentrale   │     │             │
│  Lokale DB  │     │    Quelle)    │     │  Lokale DB  │
└─────────────┘     └──────────────┘     └─────────────┘
```

### Synchronisations-Ablauf | Synchronization Process | Proceso de Sincronización

1. **Backup erstellen | Create Backup | Crear Respaldo**
   - Tägliche Sicherungskopie | Daily backup copy | Copia de respaldo diaria
   - Format: `backups/keepass_passwords_YYYYMMDD.kdbx`

2. **Download vom Server | Download from Server | Descargar del Servidor**
   - Lädt entfernte Datei herunter | Downloads remote file | Descarga archivo remoto
   - Kann Änderungen von anderen Systemen enthalten | May contain changes from other systems | Puede contener cambios de otros sistemas

3. **Merge durchführen | Perform Merge | Realizar Fusión**
   - Intelligente Zusammenführung | Intelligent merging | Fusión inteligente
   - Neue Einträge werden übernommen | New entries are adopted | Se adoptan nuevas entradas
   - Konflikte werden automatisch gelöst | Conflicts are automatically resolved | Los conflictos se resuelven automáticamente

4. **Upload zum Server | Upload to Server | Subir al Servidor**
   - Speichert aktualisierte Datei | Saves updated file | Guarda archivo actualizado
   - Alle Systeme haben jetzt die gleiche Version | All systems now have the same version | Todos los sistemas ahora tienen la misma versión

### Warum Merge statt Überschreiben? | Why Merge Instead of Overwrite? | ¿Por Qué Fusionar en Lugar de Sobrescribir?

**Vorteile | Advantages | Ventajas:**
- ✅ Keine Daten gehen verloren | No data is lost | No se pierden datos
- ✅ Änderungen auf mehreren Geräten werden kombiniert | Changes on multiple devices are combined | Los cambios en múltiples dispositivos se combinan
- ✅ Konflikte werden automatisch gelöst | Conflicts are automatically resolved | Los conflictos se resuelven automáticamente
- ✅ Du kannst von überall arbeiten | You can work from anywhere | Puedes trabajar desde cualquier lugar

---

<div align="center">

**Entwickelt für | Developed for | Desarrollado para:** Linux, Windows, macOS  
**Version:** 2.0  
**Sprachen | Languages | Idiomas:** Deutsch, English, Español

**⭐ Wenn dir dieses Projekt gefällt, gib uns einen Stern auf GitHub! | If you like this project, give us a star on GitHub! | Si te gusta este proyecto, ¡danos una estrella en GitHub!**

</div>


## 📁 Directory Structure

```
keepass-sync/
├── config.json          # Configuration (enter your data here!)
├── config.example.json   # Example configuration
├── README.de.md         # German documentation
├── README.en.md         # English documentation (this file)
├── README.es.md         # Spanish documentation
├── docs/                # Additional documentation
│   ├── INSTALL.de.md
│   ├── INSTALL.en.md
│   ├── INSTALL.es.md
│   ├── TEST.de.md
│   ├── TEST.en.md
│   └── TEST.es.md
├── sync.py              # Cross-Platform Wrapper
├── python/              # Python version (preferred)
│   └── sync_ftp.py
├── php/                 # PHP variant (for server cronjobs)
│   ├── sync.php
│   └── README.md
├── linux/               # Linux scripts
│   ├── sync_ftp.sh
│   └── install.sh       # Quick installation
├── windows/             # Windows scripts
├── mac/                 # macOS scripts
├── lang/                # Language files (JSON)
│   ├── de.json
│   ├── en.json
│   └── es.json
└── backups/             # Automatic backups (only 2 newest)
```

## 🤝 Contributing

### 🌟 Want to help?

We welcome contributions!

**How you can help:**

- 🐛 **Report bugs**
  - Open an issue on GitHub
  - Describe the problem

- 💡 **Suggest improvements**
  - New features
  - Code optimizations
  - Documentation

- 🌍 **Translations**
  - Add new languages
  - Improve translations

- 💻 **Contribute code**
  - Fork the repository
  - Create a pull request

- 📖 **Improve documentation**
  - Add missing information
  - Improve examples

### 📝 Contributing Translations

Translations are stored in `lang/*.json` files.

**Add new language:**

1. Copy `lang/en.json` as template
2. Translate all values
3. Create `lang/[code].json` (e.g. `lang/fr.json`)
4. Create pull request

**Available language codes:**
- `de` - Deutsch
- `en` - English
- `es` - Español
- `fr` - Français ✅
- `it` - Italiano ✅
- `pt` - Português ✅
- `nl` - Nederlands ✅
- `pl` - Polski ✅
- `ru` - Русский ✅
- `zh` - 中文 ✅
- `ja` - 日本語 ✅
- `ko` - 한국어 ✅

---

## 📚 More Information

- **Test Guide:** [docs/TEST.en.md](docs/TEST.en.md)
- **Installation & Automation:** [docs/INSTALL.en.md](docs/INSTALL.en.md)
- **PHP Variant:** [php/README.md](php/README.md) (for server cronjobs)

---

## 🔄 How Synchronization Works

### System Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Main System │     │              │     │  Subsystem  │
│   Desktop   │◄───►│  FTP-Server  │◄───►│   Laptop    │
│             │     │   (Central   │     │             │
│  Local DB   │     │    Source)   │     │  Local DB   │
└─────────────┘     └──────────────┘     └─────────────┘
```

### Synchronization Process

1. **Create Backup**
   - Daily backup copy
   - Format: `backups/keepass_passwords_YYYYMMDD.kdbx`

2. **Download from Server**
   - Downloads remote file
   - May contain changes from other systems

3. **Perform Merge**
   - Intelligent merging
   - New entries are adopted
   - Conflicts are automatically resolved

4. **Upload to Server**
   - Saves updated file
   - All systems now have the same version

### Why Merge Instead of Overwrite?

**Advantages:**
- ✅ No data is lost
- ✅ Changes on multiple devices are combined
- ✅ Conflicts are automatically resolved
- ✅ You can work from anywhere

---

<div align="center">

**Developed for:** Linux, Windows, macOS  
**Version:** 1.1.0  
**Languages:** German, English, Spanish (+ 9 more)

**⭐ If you like this project, give us a star on GitHub!**

**🌍 Languages: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

</div>
