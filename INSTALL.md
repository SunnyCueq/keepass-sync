# 📦 Installationsanleitung | Installation Guide | Guía de Instalación

<div align="center">

**🌍 Languages | Idiomas | Sprachen: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[← Zurück zur Hauptdokumentation](README.md) • [Test-Anleitung](TEST.md)

</div>

---

## 🇩🇪 Deutsch

## Übersicht

Diese detaillierte Anleitung erklärt, wie du das KeePass Sync Script auf deinem System installierst und automatisch ausführen lässt.

## 🚀 Schnellstart mit Installer (Empfohlen)

Für unerfahrene Benutzer gibt es einen interaktiven Installer:

```bash
python3 install.py
```

Der Installer:
- ✅ Erkennt automatisch dein System
- ✅ Zeigt System-Spezifikationen
- ✅ Erkennt deine Sprache
- ✅ Führt dich durch die Konfiguration
- ✅ Unterstützt alle Protokolle (FTP, SFTP, SMB, SCP)
- ✅ Erstellt automatisch `config.json`

## Voraussetzungen

### Alle Systeme
- KeePassXC installiert (mit `keepassxc-cli`)
- Python 3.6+ installiert

### Protokoll-spezifische Anforderungen:

**FTP:**
- `lftp` installieren: `sudo pacman -S lftp` (Arch/CachyOS) oder `sudo apt install lftp` (Debian/Ubuntu)

**SFTP:**
- `lftp` installieren (wie oben)

**SMB/CIFS:**
- Linux/macOS: `smbclient` installieren: `sudo pacman -S samba` oder `sudo apt install samba-common`
- Windows: Native Unterstützung (optional: `pysmb` Python-Library)

**SCP:**
- Linux/macOS: `sshpass` installieren: `sudo pacman -S sshpass` oder `sudo apt install sshpass`
- Windows: `paramiko` Python-Library: `pip install paramiko`

### Linux
- Optional: Python 3.6+ für Cross-Platform-Version

### Windows
- PowerShell 5.1+ (vorinstalliert)
- Optional: Python 3.6+ für Cross-Platform-Version

### macOS
- Homebrew (optional, aber empfohlen)

---

## 🚀 Schnellinstallation (Empfohlen für Linux)

```bash
cd "/mnt/ssd2/Backup (SSD2)/Tools/Keepass Sync"
./linux/install.sh
```

Dieses Script installiert automatisch:
- ✅ Systemd Service (für Herunterfahren)
- ✅ Cron-Job für Leerlauf-Sync (alle 5 Minuten)

---

## Automatische Ausführung einrichten

### Linux - Systemd Service (Start/Beendigung)

Erstelle eine Service-Datei:

```bash
sudo nano /etc/systemd/system/keepass-sync.service
```

**Inhalt:**
```ini
[Unit]
Description=KeePass Sync Service
After=network.target

[Service]
Type=oneshot
User=dein-benutzername
WorkingDirectory=/pfad/zum/keepass-sync
ExecStart=/pfad/zum/keepass-sync/python/sync_ftp.py

[Install]
WantedBy=multi-user.target
```

**Aktivieren:**
```bash
sudo systemctl enable keepass-sync.service
sudo systemctl start keepass-sync.service
```

**Für automatische Ausführung bei Herunterfahren:**
Erstelle zusätzlich `/etc/systemd/system/keepass-sync-shutdown.service`:

```ini
[Unit]
Description=KeePass Sync on Shutdown
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=oneshot
User=dein-benutzername
WorkingDirectory=/pfad/zum/keepass-sync
ExecStart=/pfad/zum/keepass-sync/python/sync_ftp.py
TimeoutStartSec=0

[Install]
WantedBy=shutdown.target
```

### Linux - Cron (Zeitgesteuert)

**Für tägliche Ausführung um 6:00 Uhr:**
```bash
crontab -e
```

**Eintrag hinzufügen:**
```
0 6 * * * /pfad/zum/keepass-sync/python/sync_ftp.py >> /pfad/zum/keepass-sync/sync_cron.log 2>&1
```

**Für Ausführung im Leerlauf (alle 5 Minuten):**
```bash
# Installiere xprintidle (für X11) oder verwende systemd timer
sudo pacman -S xprintidle  # Arch/CachyOS
# Oder: sudo apt install xprintidle  # Debian/Ubuntu

# Dann in crontab:
*/5 * * * * if [ $(xprintidle 2>/dev/null || echo 0) -gt 300000 ]; then /pfad/zum/keepass-sync/python/sync_ftp.py; fi
```

### Windows - Task Scheduler (Empfohlen)

1. **Task Scheduler öffnen:**
   - Windows-Taste + R
   - `taskschd.msc` eingeben

2. **Neuen Task erstellen:**
   - Rechtsklick auf "Task Scheduler Library" → "Create Task..."

3. **Allgemein:**
   - Name: `KeePass Sync`
   - "Run whether user is logged on or not" aktivieren
   - "Run with highest privileges" aktivieren

4. **Trigger (Auslöser):**
   - **Bei Start:** "New..." → "At startup"
   - **Bei Anmeldung:** "New..." → "At log on"
   - **Täglich:** "New..." → "Daily" → Zeit wählen (z.B. 6:00)
   - **Bei Leerlauf:** "New..." → "On idle" → Wartezeit wählen (z.B. 10 Minuten)

5. **Aktion:**
   - "New..." → "Start a program"
   - Programm: `powershell.exe`
   - Argumente: `-NoProfile -ExecutionPolicy Bypass -File "C:\Pfad\zum\keepass-sync\windows\sync_ftp.ps1"`

6. **Bedingungen (optional):**
   - "Start the task only if the computer is on AC power" deaktivieren (für Laptops)
   - "Wake the computer to run this task" aktivieren (optional)

### Windows - Autostart (Einfacher)

Erstelle eine Verknüpfung:

1. Rechtsklick auf `windows/sync_ftp.bat` → "Create shortcut"
2. Verschiebe Verknüpfung nach: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
3. Rechtsklick auf Verknüpfung → "Properties" → "Run: Minimized"

### macOS - LaunchAgent (Empfohlen)

1. **Agent-Datei erstellen:**
   ```bash
   nano ~/Library/LaunchAgents/com.user.keepass-sync.plist
   ```

2. **Inhalt:**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.keepass-sync</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/pfad/zum/keepass-sync/python/sync_ftp.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>StartInterval</key>
       <integer>3600</integer>
       <key>StandardOutPath</key>
       <string>/pfad/zum/keepass-sync/sync_log.txt</string>
       <key>StandardErrorPath</key>
       <string>/pfad/zum/keepass-sync/sync_error.log</string>
   </dict>
   </plist>
   ```

3. **Aktivieren:**
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.keepass-sync.plist
   ```

### macOS - Cron (Alternativ)

```bash
crontab -e
```

**Eintrag:**
```
0 6 * * * /usr/bin/python3 /pfad/zum/keepass-sync/python/sync_ftp.py >> /pfad/zum/keepass-sync/sync_cron.log 2>&1
```

---

## Leerlauf-Erkennung

### Linux (X11)

Verwende `xprintidle`:
```bash
sudo pacman -S xprintidle  # Arch/CachyOS
```

Dann in Cron:
```
*/5 * * * * if [ $(xprintidle) -gt 300000 ]; then /pfad/zum/keepass-sync/python/sync_ftp.py; fi
```

### Windows

Task Scheduler hat eingebaute Leerlauf-Erkennung:
- Trigger → "On idle" → Wartezeit einstellen (z.B. 10 Minuten)

### macOS

Verwende `ioreg` für Leerlauf-Erkennung (komplexer, LaunchAgent mit StartInterval ist einfacher).

---

<div align="center">

**← [Zurück zur Hauptdokumentation](README.md) • [Test-Anleitung](TEST.md) →**

</div>

---

## 🇬🇧 English

## Overview

This detailed guide explains how to install and automatically run the KeePass Sync script on your system.

## 🚀 Quick Start with Installer (Recommended)

For inexperienced users, there's an interactive installer:

```bash
python3 install.py
```

The installer:
- ✅ Automatically detects your system
- ✅ Shows system specifications
- ✅ Detects your language
- ✅ Guides you through configuration
- ✅ Supports all protocols (FTP, SFTP, SMB, SCP)
- ✅ Automatically creates `config.json`

## Prerequisites

### All Systems
- KeePassXC installed (with `keepassxc-cli`)
- Python 3.6+ installed

### Protocol-specific Requirements:

**FTP:**
- Install `lftp`: `sudo pacman -S lftp` (Arch/CachyOS) or `sudo apt install lftp` (Debian/Ubuntu)

**SFTP:**
- Install `lftp` (as above)

**SMB/CIFS:**
- Linux/macOS: Install `smbclient`: `sudo pacman -S samba` or `sudo apt install samba-common`
- Windows: Native support (optional: `pysmb` Python library)

**SCP:**
- Linux/macOS: Install `sshpass`: `sudo pacman -S sshpass` or `sudo apt install sshpass`
- Windows: `paramiko` Python library: `pip install paramiko`

### Linux
- Optional: Python 3.6+ for cross-platform version

### Windows
- PowerShell 5.1+ (pre-installed)
- Optional: Python 3.6+ for cross-platform version

### macOS
- Homebrew (optional but recommended)

---

## 🚀 Quick Installation (Recommended for Linux)

```bash
cd "/mnt/ssd2/Backup (SSD2)/Tools/Keepass Sync"
./linux/install.sh
```

This script automatically installs:
- ✅ Systemd Service (on shutdown)
- ✅ Cron Job for idle sync (every 5 minutes)

---

## Setting Up Automatic Execution

### Linux - Systemd Service (Start/Shutdown)

Create a service file:

```bash
sudo nano /etc/systemd/system/keepass-sync.service
```

**Content:**
```ini
[Unit]
Description=KeePass Sync Service
After=network.target

[Service]
Type=oneshot
User=your-username
WorkingDirectory=/path/to/keepass-sync
ExecStart=/path/to/keepass-sync/python/sync_ftp.py

[Install]
WantedBy=multi-user.target
```

**Enable:**
```bash
sudo systemctl enable keepass-sync.service
sudo systemctl start keepass-sync.service
```

**For automatic execution on shutdown:**
Also create `/etc/systemd/system/keepass-sync-shutdown.service`:

```ini
[Unit]
Description=KeePass Sync on Shutdown
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=oneshot
User=your-username
WorkingDirectory=/path/to/keepass-sync
ExecStart=/path/to/keepass-sync/python/sync_ftp.py
TimeoutStartSec=0

[Install]
WantedBy=shutdown.target
```

### Linux - Cron (Scheduled)

**For daily execution at 6:00 AM:**
```bash
crontab -e
```

**Add entry:**
```
0 6 * * * /path/to/keepass-sync/python/sync_ftp.py >> /path/to/keepass-sync/sync_cron.log 2>&1
```

**For execution on idle (every 5 minutes):**
```bash
# Install xprintidle (for X11) or use systemd timer
sudo pacman -S xprintidle  # Arch/CachyOS
# Or: sudo apt install xprintidle  # Debian/Ubuntu

# Then in crontab:
*/5 * * * * if [ $(xprintidle 2>/dev/null || echo 0) -gt 300000 ]; then /path/to/keepass-sync/python/sync_ftp.py; fi
```

### Windows - Task Scheduler (Recommended)

1. **Open Task Scheduler:**
   - Windows Key + R
   - Type `taskschd.msc`

2. **Create new task:**
   - Right-click "Task Scheduler Library" → "Create Task..."

3. **General:**
   - Name: `KeePass Sync`
   - Enable "Run whether user is logged on or not"
   - Enable "Run with highest privileges"

4. **Triggers:**
   - **At startup:** "New..." → "At startup"
   - **At log on:** "New..." → "At log on"
   - **Daily:** "New..." → "Daily" → Choose time (e.g. 6:00)
   - **On idle:** "New..." → "On idle" → Choose wait time (e.g. 10 minutes)

5. **Action:**
   - "New..." → "Start a program"
   - Program: `powershell.exe`
   - Arguments: `-NoProfile -ExecutionPolicy Bypass -File "C:\Path\to\keepass-sync\windows\sync_ftp.ps1"`

6. **Conditions (optional):**
   - Disable "Start the task only if the computer is on AC power" (for laptops)
   - Enable "Wake the computer to run this task" (optional)

### Windows - Autostart (Simpler)

Create a shortcut:

1. Right-click `windows/sync_ftp.bat` → "Create shortcut"
2. Move shortcut to: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
3. Right-click shortcut → "Properties" → "Run: Minimized"

### macOS - LaunchAgent (Recommended)

1. **Create agent file:**
   ```bash
   nano ~/Library/LaunchAgents/com.user.keepass-sync.plist
   ```

2. **Content:**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.keepass-sync</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/path/to/keepass-sync/python/sync_ftp.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>StartInterval</key>
       <integer>3600</integer>
       <key>StandardOutPath</key>
       <string>/path/to/keepass-sync/sync_log.txt</string>
       <key>StandardErrorPath</key>
       <string>/path/to/keepass-sync/sync_error.log</string>
   </dict>
   </plist>
   ```

3. **Enable:**
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.keepass-sync.plist
   ```

### macOS - Cron (Alternative)

```bash
crontab -e
```

**Entry:**
```
0 6 * * * /usr/bin/python3 /path/to/keepass-sync/python/sync_ftp.py >> /path/to/keepass-sync/sync_cron.log 2>&1
```

---

## Idle Detection

### Linux (X11)

Use `xprintidle`:
```bash
sudo pacman -S xprintidle  # Arch/CachyOS
```

Then in Cron:
```
*/5 * * * * if [ $(xprintidle) -gt 300000 ]; then /path/to/keepass-sync/python/sync_ftp.py; fi
```

### Windows

Task Scheduler has built-in idle detection:
- Trigger → "On idle" → Set wait time (e.g. 10 minutes)

### macOS

Use `ioreg` for idle detection (more complex, LaunchAgent with StartInterval is simpler).

---

<div align="center">

**← [Back to Main Documentation](README.md) • [Test Guide](TEST.md) →**

</div>

---

## 🇪🇸 Español

## Resumen

Esta guía detallada explica cómo instalar y ejecutar automáticamente el script de sincronización de KeePass en tu sistema.

## 🚀 Inicio Rápido con Instalador (Recomendado)

Para usuarios sin experiencia, hay un instalador interactivo:

```bash
python3 install.py
```

El instalador:
- ✅ Detecta automáticamente tu sistema
- ✅ Muestra especificaciones del sistema
- ✅ Detecta tu idioma
- ✅ Te guía a través de la configuración
- ✅ Soporta todos los protocolos (FTP, SFTP, SMB, SCP)
- ✅ Crea automáticamente `config.json`

## Requisitos Previos

### Todos los Sistemas
- KeePassXC instalado (con `keepassxc-cli`)
- Python 3.6+ instalado

### Requisitos Específicos por Protocolo:

**FTP:**
- Instalar `lftp`: `sudo pacman -S lftp` (Arch/CachyOS) o `sudo apt install lftp` (Debian/Ubuntu)

**SFTP:**
- Instalar `lftp` (como arriba)

**SMB/CIFS:**
- Linux/macOS: Instalar `smbclient`: `sudo pacman -S samba` o `sudo apt install samba-common`
- Windows: Soporte nativo (opcional: biblioteca Python `pysmb`)

**SCP:**
- Linux/macOS: Instalar `sshpass`: `sudo pacman -S sshpass` o `sudo apt install sshpass`
- Windows: Bibliotec Python `paramiko`: `pip install paramiko`

### Linux
- Opcional: Python 3.6+ para versión multiplataforma

### Windows
- PowerShell 5.1+ (pre-instalado)
- Opcional: Python 3.6+ para versión multiplataforma

### macOS
- Homebrew (opcional pero recomendado)

---

## 🚀 Instalación Rápida (Recomendado para Linux)

```bash
cd "/mnt/ssd2/Backup (SSD2)/Tools/Keepass Sync"
./linux/install.sh
```

Este script instala automáticamente:
- ✅ Servicio Systemd (al apagar)
- ✅ Tarea Cron para sincronización en reposo (cada 5 minutos)

---

## Configurar Ejecución Automática

### Linux - Servicio Systemd (Inicio/Apagado)

Crea un archivo de servicio:

```bash
sudo nano /etc/systemd/system/keepass-sync.service
```

**Contenido:**
```ini
[Unit]
Description=KeePass Sync Service
After=network.target

[Service]
Type=oneshot
User=tu-usuario
WorkingDirectory=/ruta/a/keepass-sync
ExecStart=/ruta/a/keepass-sync/python/sync_ftp.py

[Install]
WantedBy=multi-user.target
```

**Activar:**
```bash
sudo systemctl enable keepass-sync.service
sudo systemctl start keepass-sync.service
```

**Para ejecución automática al apagar:**
También crea `/etc/systemd/system/keepass-sync-shutdown.service`:

```ini
[Unit]
Description=KeePass Sync on Shutdown
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=oneshot
User=tu-usuario
WorkingDirectory=/ruta/a/keepass-sync
ExecStart=/ruta/a/keepass-sync/python/sync_ftp.py
TimeoutStartSec=0

[Install]
WantedBy=shutdown.target
```

### Linux - Cron (Programado)

**Para ejecución diaria a las 6:00 AM:**
```bash
crontab -e
```

**Añadir entrada:**
```
0 6 * * * /ruta/a/keepass-sync/python/sync_ftp.py >> /ruta/a/keepass-sync/sync_cron.log 2>&1
```

**Para ejecución en reposo (cada 5 minutos):**
```bash
# Instalar xprintidle (para X11) o usar systemd timer
sudo pacman -S xprintidle  # Arch/CachyOS
# O: sudo apt install xprintidle  # Debian/Ubuntu

# Luego en crontab:
*/5 * * * * if [ $(xprintidle 2>/dev/null || echo 0) -gt 300000 ]; then /ruta/a/keepass-sync/python/sync_ftp.py; fi
```

### Windows - Programador de Tareas (Recomendado)

1. **Abrir Programador de Tareas:**
   - Tecla Windows + R
   - Escribir `taskschd.msc`

2. **Crear nueva tarea:**
   - Clic derecho en "Biblioteca del Programador de tareas" → "Crear tarea..."

3. **General:**
   - Nombre: `KeePass Sync`
   - Activar "Ejecutar si el usuario ha iniciado sesión o no"
   - Activar "Ejecutar con los privilegios más altos"

4. **Desencadenadores:**
   - **Al iniciar:** "Nuevo..." → "Al iniciar"
   - **Al iniciar sesión:** "Nuevo..." → "Al iniciar sesión"
   - **Diariamente:** "Nuevo..." → "Diariamente" → Elegir hora (ej. 6:00)
   - **En reposo:** "Nuevo..." → "En reposo" → Elegir tiempo de espera (ej. 10 minutos)

5. **Acción:**
   - "Nuevo..." → "Iniciar un programa"
   - Programa: `powershell.exe`
   - Argumentos: `-NoProfile -ExecutionPolicy Bypass -File "C:\Ruta\a\keepass-sync\windows\sync_ftp.ps1"`

6. **Condiciones (opcional):**
   - Desactivar "Iniciar la tarea solo si el equipo está conectado a la alimentación de CA" (para portátiles)
   - Activar "Activar el equipo para ejecutar esta tarea" (opcional)

### Windows - Autostart (Más Simple)

Crear un acceso directo:

1. Clic derecho en `windows/sync_ftp.bat` → "Crear acceso directo"
2. Mover acceso directo a: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
3. Clic derecho en acceso directo → "Propiedades" → "Ejecutar: Minimizado"

### macOS - LaunchAgent (Recomendado)

1. **Crear archivo de agente:**
   ```bash
   nano ~/Library/LaunchAgents/com.user.keepass-sync.plist
   ```

2. **Contenido:**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.keepass-sync</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/ruta/a/keepass-sync/python/sync_ftp.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>StartInterval</key>
       <integer>3600</integer>
       <key>StandardOutPath</key>
       <string>/ruta/a/keepass-sync/sync_log.txt</string>
       <key>StandardErrorPath</key>
       <string>/ruta/a/keepass-sync/sync_error.log</string>
   </dict>
   </plist>
   ```

3. **Activar:**
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.keepass-sync.plist
   ```

### macOS - Cron (Alternativa)

```bash
crontab -e
```

**Entrada:**
```
0 6 * * * /usr/bin/python3 /ruta/a/keepass-sync/python/sync_ftp.py >> /ruta/a/keepass-sync/sync_cron.log 2>&1
```

---

## Detección de Reposo

### Linux (X11)

Usar `xprintidle`:
```bash
sudo pacman -S xprintidle  # Arch/CachyOS
```

Luego en Cron:
```
*/5 * * * * if [ $(xprintidle) -gt 300000 ]; then /ruta/a/keepass-sync/python/sync_ftp.py; fi
```

### Windows

El Programador de Tareas tiene detección de reposo integrada:
- Desencadenador → "En reposo" → Establecer tiempo de espera (ej. 10 minutos)

### macOS

Usar `ioreg` para detección de reposo (más complejo, LaunchAgent con StartInterval es más simple).

---

<div align="center">

**← [Volver a Documentación Principal](README.md) • [Guía de Pruebas](TEST.md) →**

</div>
