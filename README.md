# 🔐 KeePass Sync - Synchronisiere deine Passwörter automatisch

<div align="center">

**🌍 Languages | Idiomas | Sprachen: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](.)

> **Synchronisiere deine KeePass-Datenbank automatisch zwischen mehreren Computern über einen FTP-Server.**

[🚀 Schnellstart](#-schnellstart) • [📖 Dokumentation](#-dokumentation) • [🛠️ Installation](#️-installation) • [❓ FAQ](#-häufige-fragen) • [🤝 Mitwirken](#-mitwirken)

</div>

---

## 🇩🇪 Deutsch

### 🚀 Schnellstart

#### 1. Voraussetzungen

- **KeePassXC** installiert (von [keepassxc.org](https://keepassxc.org/))
- **Python 3** installiert (meist vorinstalliert auf Linux/macOS)
- **FTP-Zugangsdaten** für deinen Server

#### 2. Konfiguration

**Option A: Interaktiver Installer (Empfohlen für Anfänger)**
```bash
python3 install.py
```
oder
```bash
python3 python/installer.py
```

Der Installer:
- ✅ Erkennt automatisch dein System
- ✅ Zeigt System-Spezifikationen an
- ✅ Erkennt automatisch deine Sprache
- ✅ Führte dich durch die Konfiguration
- ✅ Unterstützt alle Protokolle (FTP, SFTP, SMB, SCP)
- ✅ Erstellt automatisch `config.json`

**Option B: Manuelle Konfiguration**
```bash
cp config.example.json config.json
```

Dann öffne `config.json` und trage deine Daten ein:
```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-passwort",
    "type": "ftp",
    "comment": "Protokoll-Optionen: 'ftp' (Standard), 'sftp', 'smb', 'scp'",
    "remotePath": "/keepass_passwords.kdbx"
  },
  "keepass": {
    "databasePassword": "dein-keeppass-master-passwort"
  }
}
```

#### 3. Testen

**Linux:**
```bash
# Wrapper testen (bevorzugt)
python3 sync.py

# Oder .sh Datei direkt
./linux/sync_ftp.sh

# Oder Python-Script direkt (mit Debug)
python3 python/sync_ftp.py
```

**Erwartete Ausgabe bei Erfolg:**
```
2025-11-02 17:XX:XX === KeePass Sync - Linux ===
2025-11-02 17:XX:XX Backup wird erstellt...
2025-11-02 17:XX:XX Backup erfolgreich erstellt
2025-11-02 17:XX:XX Starte Download vom Server...
2025-11-02 17:XX:XX Download erfolgreich
2025-11-02 17:XX:XX Führe Merge durch...
2025-11-02 17:XX:XX Merge erfolgreich abgeschlossen. Lokale Datei aktualisiert.
2025-11-02 17:XX:XX Starte Upload zum Server...
2025-11-02 17:XX:XX Upload erfolgreich abgeschlossen.
2025-11-02 17:XX:XX Synchronisation abgeschlossen.
```

**Fehlerbehebung:**
- **"Konfigurationsdatei nicht gefunden"** → Stelle sicher, dass `config.json` existiert
- **"KeePassXC-CLI nicht gefunden"** → Installiere: `sudo pacman -S keepassxc` (Arch) oder `sudo apt install keepassxc` (Debian)
- **"FTP-Client nicht gefunden"** → Installiere: `sudo pacman -S lftp` (Arch) oder `sudo apt install lftp` (Debian)

📖 **Detaillierte Test-Anleitung:** [TEST.md](TEST.md)

#### 4. Automatische Installation

**🚀 Schnellinstallation (Linux - Empfohlen):**
```bash
./linux/install.sh
```

Dies installiert automatisch:
- ✅ Systemd Service (bei Herunterfahren)
- ✅ Cron-Job (bei Leerlauf, alle 5 Minuten)

**Windows - Task Scheduler:**
1. Task Scheduler öffnen (`taskschd.msc`)
2. "Create Task..." → Name: `KeePass Sync`
3. Trigger: "At startup", "Daily" oder "On idle"
4. Action: `powershell.exe` → Argumente: `-NoProfile -ExecutionPolicy Bypass -File "C:\Pfad\windows\sync_ftp.ps1"`

**macOS - LaunchAgent:**
```bash
# Erstelle ~/Library/LaunchAgents/com.user.keepass-sync.plist
# Siehe INSTALL.md für vollständige Anleitung
```

📖 **Vollständige Installationsanleitung für alle Plattformen:** [INSTALL.md](INSTALL.md)

### 📖 Was macht das Script?

Das Script synchronisiert deine KeePass-Datenbank in 4 Schritten:

1. **🔒 Backup erstellen** - Sichert deine lokale Datei
2. **⬇️ Download** - Holt die neueste Version vom Server
3. **🔄 Merge** - Kombiniert intelligent alle Änderungen
4. **⬆️ Upload** - Speichert die aktualisierte Datei zurück

**Wichtig:** Das Script löscht **keine** Daten. Es kombiniert alle Änderungen von allen Geräten automatisch!

### 🌍 Mehrsprachigkeit

Das Script unterstützt **Deutsch**, **Englisch** und **Spanisch**. Die Sprache wird automatisch erkannt oder kann in `config.json` eingestellt werden:

### 📡 Unterstützte Protokolle

Das Script unterstützt mehrere Übertragungsprotokolle:

- **FTP** (Standard) - File Transfer Protocol
- **SFTP** - SSH File Transfer Protocol (verschlüsselt)
- **SMB/CIFS** - Windows-Netzwerk-Freigaben
- **SCP** - Secure Copy Protocol (SSH-basiert)

Wähle das Protokoll in `config.json` mit `"type": "ftp"` (oder `sftp`, `smb`, `scp`).

```json
{
  "settings": {
    "language": "de"  // "de", "en" oder "es"
  }
}
```

### ⚙️ Erweiterte Konfiguration

In `config.json` kannst du zusätzlich einstellen:

- `maxBackups`: Anzahl der Backups (Standard: 2)
- `cleanupLogs`: Alte Logs automatisch löschen (Standard: true)
- `maxLogAgeDays`: Logs älter als X Tage löschen (Standard: 7)
- `debug`: Debug-Modus aktivieren (Standard: false)

### ❓ Häufige Fragen

**F: Verliere ich Daten, wenn ich auf mehreren Geräten gleichzeitig arbeite?**  
A: Nein! Das Script kombiniert alle Änderungen intelligent. Neue Passwörter werden von allen Seiten übernommen.

**F: Wie oft sollte ich synchronisieren?**  
A: Mindestens einmal täglich. Am besten automatisch einrichten (siehe INSTALL.md).

**F: Was ist, wenn die Verbindung zum Server fehlschlägt?**  
A: Das Script erstellt vorher ein Backup. Deine lokale Datei bleibt unverändert.

**F: Funktioniert das mit mehr als 2 Computern?**  
A: Ja! So viele wie du möchtest. Der FTP-Server ist die zentrale Quelle.

### 📝 Logs & Backups

- **Logs:** `sync_log.txt` (wird automatisch aufgeräumt)
- **Backups:** `backups/` (nur die 2 neuesten werden behalten)
- **Temporäre Dateien:** Werden automatisch gelöscht

### 🔐 Sicherheit

⚠️ **Wichtig:**
- Die `config.json` enthält Passwörter im Klartext
- Stelle sicher, dass die Datei nicht öffentlich zugänglich ist
- Linux/macOS: `chmod 600 config.json`
- Windows: Rechte entsprechend setzen

---

## 🇬🇧 English

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

The script supports **German**, **English**, and **Spanish**. Language is automatically detected or can be set in `config.json`:

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

## 🇪🇸 Español

### 🚀 Inicio Rápido

#### 1. Requisitos Previos

- **KeePassXC** instalado (de [keepassxc.org](https://keepassxc.org/))
- **Python 3** instalado (generalmente pre-instalado en Linux/macOS)
- **Credenciales FTP** para tu servidor

#### 2. Configuración

**Opción A: Instalador Interactivo (Recomendado para principiantes)**
```bash
python3 install.py
```
o
```bash
python3 python/installer.py
```

El instalador:
- ✅ Detecta automáticamente tu sistema
- ✅ Muestra especificaciones del sistema
- ✅ Detecta automáticamente tu idioma
- ✅ Te guía a través de la configuración
- ✅ Soporta todos los protocolos (FTP, SFTP, SMB, SCP)
- ✅ Crea automáticamente `config.json`

**Opción B: Configuración Manual**
```bash
cp config.example.json config.json
```

Luego abre `config.json` e ingresa tus datos:
```json
{
  "ftp": {
    "host": "tu-servidor.com",
    "user": "tu-usuario",
    "password": "tu-contraseña",
    "type": "ftp",
    "comment": "Opciones de protocolo: 'ftp' (por defecto), 'sftp', 'smb', 'scp'",
    "remotePath": "/keepass_passwords.kdbx"
  },
  "keepass": {
    "databasePassword": "tu-contraseña-maestra-keepass"
  }
}
```

#### 3. Pruebas

**Linux:**
```bash
# Probar wrapper (preferido)
python3 sync.py

# O archivo .sh directamente
./linux/sync_ftp.sh

# O script Python directamente (con debug)
python3 python/sync_ftp.py
```

**Salida Esperada en Éxito:**
```
2025-11-02 17:XX:XX === KeePass Sync - Linux ===
2025-11-02 17:XX:XX Creando respaldo...
2025-11-02 17:XX:XX Respaldo creado exitosamente
2025-11-02 17:XX:XX Iniciando descarga desde el servidor...
2025-11-02 17:XX:XX Descarga exitosa
2025-11-02 17:XX:XX Realizando fusión...
2025-11-02 17:XX:XX Fusión completada exitosamente. Archivo local actualizado.
2025-11-02 17:XX:XX Iniciando carga al servidor...
2025-11-02 17:XX:XX Carga completada exitosamente.
2025-11-02 17:XX:XX Sincronización completada.
```

**Solución de Problemas:**
- **"Archivo de configuración no encontrado"** → Asegúrate de que `config.json` existe
- **"KeePassXC-CLI no encontrado"** → Instala: `sudo pacman -S keepassxc` (Arch) o `sudo apt install keepassxc` (Debian)
- **"Cliente FTP no encontrado"** → Instala: `sudo pacman -S lftp` (Arch) o `sudo apt install lftp` (Debian)

📖 **Guía de Pruebas Detallada:** [TEST.md](TEST.md)

#### 4. Instalación Automática

**🚀 Instalación Rápida (Linux - Recomendado):**
```bash
./linux/install.sh
```

Esto instala automáticamente:
- ✅ Servicio Systemd (al apagar)
- ✅ Tarea Cron (en reposo, cada 5 minutos)

**Windows - Programador de Tareas:**
1. Abre Programador de Tareas (`taskschd.msc`)
2. "Crear tarea..." → Nombre: `KeePass Sync`
3. Desencadenador: "Al iniciar", "Diariamente" o "En reposo"
4. Acción: `powershell.exe` → Argumentos: `-NoProfile -ExecutionPolicy Bypass -File "C:\Ruta\windows\sync_ftp.ps1"`

**macOS - LaunchAgent:**
```bash
# Crea ~/Library/LaunchAgents/com.user.keepass-sync.plist
# Ver INSTALL.md para instrucciones completas
```

📖 **Guía de Instalación Completa para Todas las Plataformas:** [INSTALL.md](INSTALL.md)

### 📖 ¿Qué hace el script?

El script sincroniza tu base de datos KeePass en 4 pasos:

1. **🔒 Crear Respaldo** - Respalda tu archivo local
2. **⬇️ Descargar** - Obtiene la última versión del servidor
3. **🔄 Fusionar** - Combina inteligentemente todos los cambios
4. **⬆️ Subir** - Guarda el archivo actualizado de vuelta

**Importante:** ¡El script **no** elimina datos! Combina automáticamente todos los cambios de todos los dispositivos.

### 🌍 Soporte Multiidioma

El script soporta **Alemán**, **Inglés** y **Español**. El idioma se detecta automáticamente o se puede configurar en `config.json`:

### 📡 Protocolos Soportados

El script soporta múltiples protocolos de transferencia:

- **FTP** (Por defecto) - Protocolo de transferencia de archivos
- **SFTP** - Protocolo de transferencia de archivos SSH (encriptado)
- **SMB/CIFS** - Recursos compartidos de red Windows
- **SCP** - Protocolo de copia segura (basado en SSH)

Elige el protocolo en `config.json` con `"type": "ftp"` (o `sftp`, `smb`, `scp`).

```json
{
  "settings": {
    "language": "es"  // "de", "en" o "es"
  }
}
```

### ⚙️ Configuración Avanzada

En `config.json` también puedes configurar:

- `maxBackups`: Número de respaldos (por defecto: 2)
- `cleanupLogs`: Eliminar logs antiguos automáticamente (por defecto: true)
- `maxLogAgeDays`: Eliminar logs más antiguos que X días (por defecto: 7)
- `debug`: Activar modo debug (por defecto: false)

### ❓ Preguntas Frecuentes

**P: ¿Perderé datos si trabajo en múltiples dispositivos simultáneamente?**  
R: ¡No! El script combina inteligentemente todos los cambios. Las nuevas contraseñas se adoptan de todos los lados.

**P: ¿Con qué frecuencia debo sincronizar?**  
R: Al menos una vez al día. Mejor configurarlo automáticamente (ver INSTALL.md).

**P: ¿Qué pasa si falla la conexión al servidor?**  
R: El script crea un respaldo primero. Tu archivo local permanece sin cambios.

**P: ¿Funciona con más de 2 computadoras?**  
R: ¡Sí! Las que quieras. El servidor FTP es la fuente central.

### 📝 Logs y Respaldos

- **Logs:** `sync_log.txt` (se limpian automáticamente)
- **Respaldos:** `backups/` (solo se mantienen los 2 más recientes)
- **Archivos temporales:** Se eliminan automáticamente

### 🔐 Seguridad

⚠️ **Importante:**
- El `config.json` contiene contraseñas en texto plano
- Asegúrate de que el archivo no sea accesible públicamente
- Linux/macOS: `chmod 600 config.json`
- Windows: Establece los permisos apropiados

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
- `fr` - Français | French | Francés (noch nicht implementiert | not yet implemented | aún no implementado)
- `it` - Italiano | Italian (noch nicht implementiert | not yet implemented | aún no implementado)

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
