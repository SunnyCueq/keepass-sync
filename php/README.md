# 🐘 KeePass Sync - PHP Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![PHP](https://img.shields.io/badge/PHP-7.4+-777BB4.svg?logo=php&logoColor=white)](https://www.php.net/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Server-basiert, ideal für Cronjobs**

</div>

---

## ⚠️ WICHTIGE SICHERHEITSWARNUNG ⚠️

**Dieses Script verarbeitet SENSIBLE PASSWÖRTER auf einem SERVER!**

**GEFAHREN:**
- ⚠️ Bei Server-Kompromittierung = alle Passwörter weg
- ⚠️ PHP-Fehler könnten sensible Daten loggen
- ⚠️ Zugriff über Web = hohes Risiko

**ANFORDERUNGEN:**
- ✅ Nur auf **VERTRAUENSWÜRDIGEM Server** verwenden (VPS/Dedicated)
- ✅ **KEIN Standard-Webhosting** (KeePassXC-CLI muss installierbar sein)
- ✅ Script sollte **NUR über Cronjob** laufen (nicht über Web)
- ✅ `.htaccess` mit Zugriffsbeschränkung (Apache) - bereits enthalten
- ✅ Nginx: `location` block mit `deny all` - Beispiel enthalten
- ✅ **HTTPS zwingend erforderlich** (wenn Web-Zugriff geplant)

**EMPFOHLEN**: Für Desktop-Nutzung besser **Python-Variante** verwenden (sicherer)

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
- [📦 Node.js](../nodejs/README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript
- [🤖 AutoIt](../autoit/README.md) - Windows-native | Windows-native | Windows nativo
- [💻 PowerShell](../powershell/README.md) - Windows-Scripting | Windows Scripting | Scripting Windows
- [⚙️ C/C++](../cpp/README.md) - Native Performance | Native Performance | Rendimiento nativo
- [🐘 PHP](./README.md) - Server Cronjobs | Server Cronjobs | Cronjobs servidor ⭐ **Hier**
- [💼 COBOL](../cobol/README.md) - Legacy & Mainframe | Legacy & Mainframe | Legacy y Mainframe

### Hauptdokumentation | Main Documentation | Documentación Principal

- [🏠 Hauptseite](../README.md) | [Main Page](../README.en.md) | [Página Principal](../README.es.md)
- [📖 Installationsanleitung](../docs/INSTALL.de.md) | [Installation Guide](../docs/INSTALL.en.md) | [Guía de Instalación](../docs/INSTALL.es.md)
- [🧪 Test-Anleitung](../docs/TEST.de.md) | [Test Guide](../docs/TEST.en.md) | [Guía de Pruebas](../docs/TEST.es.md)

---

## 🇩🇪 Deutsch

### 📋 Inhaltsverzeichnis

1. [Systemanforderungen](#systemanforderungen)
2. [PHP Installation](#php-installation)
3. [PHP CLI vs Web-PHP](#php-cli-vs-web-php)
4. [KeePassXC-CLI Installation](#keepassxc-cli-installation)
5. [Webserver-Konfiguration](#webserver-konfiguration)
6. [Konfiguration](#konfiguration)
7. [Cronjob Einrichtung](#cronjob-einrichtung)
8. [Verwendung](#verwendung)
9. [Fehlerbehebung](#fehlerbehebung)
10. [Danksagungen](#danksagungen)

---

### 🔧 Systemanforderungen

#### Minimale Systemanforderungen

| Betriebssystem | Minimal | Empfohlen | Architektur |
|----------------|---------|-----------|-------------|
| **Linux** | Alle modernen Distributionen | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x64, ARM64 |

#### Erforderliche Software

1. **PHP**
   - **Minimale Version**: 7.4+
   - **Empfohlene Version**: 8.1+ oder 8.2+ (aktuellste stabile Version)
   - **WICHTIG**: PHP CLI (Command Line Interface) muss verfügbar sein
   - **Download**: [https://www.php.net/downloads.php](https://www.php.net/downloads.php)

2. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)
   - **WICHTIG**: Muss auf dem Server installiert sein
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Webserver** (Optional, nur für Web-Zugriff - NICHT empfohlen)
   - **Apache**: 2.4+ mit mod_php
   - **Nginx**: 1.18+ mit PHP-FPM
   - **WICHTIG**: Script sollte NUR über Cronjob laufen, nicht über Web!

---

### 🐘 PHP Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Installiere PHP und PHP CLI
sudo pacman -S php php-cli

# Überprüfe
php --version
# Sollte zeigen: PHP 8.2.x (CLI) oder ähnlich

php-cli --version
```

**Paketnamen**: 
- `php` - PHP mit CLI
- `php-cli` - PHP Command Line Interface

**Repository**: Extra  
**Link**: [Arch Linux PHP Package](https://archlinux.org/packages/extra/x86_64/php/)

##### Debian / Ubuntu

```bash
# Aktualisiere Paketliste
sudo apt update

# Installiere PHP CLI
sudo apt install php-cli php-json

# Überprüfe
php --version
```

**Paketnamen**:
- `php-cli` - PHP Command Line Interface
- `php-json` - JSON-Unterstützung (normalerweise bereits in php-cli enthalten)

**Repository**: Main  
**Link**: [Debian PHP Package](https://packages.debian.org/php-cli)

**Alternative: Neueste PHP-Version (PHP 8.1/8.2)**

```bash
# Für PHP 8.2
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install php8.2-cli
```

**Link**: [Ondřej Surý PPA](https://launchpad.net/~ondrej/+archive/ubuntu/php)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install php-cli php-json
```

##### openSUSE

```bash
sudo zypper install php7-cli php7-json
```

#### macOS

##### Homebrew (Empfohlen)

```bash
# Installiere PHP
brew install php

# Überprüfe
php --version
```

**Link**: [Homebrew PHP Formula](https://formulae.brew.sh/formula/php)

##### XAMPP / MAMP (Alternative)

**NICHT empfohlen** für Cronjobs, aber möglich.

#### Windows

##### XAMPP (Empfohlen für Windows)

1. **Download**: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
2. **Installiere**: XAMPP mit PHP
3. **Überprüfe**: `C:\xampp\php\php.exe --version`

**Link**: [XAMPP](https://www.apachefriends.org/)

##### PHP Standalone

1. **Download**: [https://windows.php.net/download/](https://windows.php.net/download/)
2. **Wähle**: PHP 8.x Thread Safe ZIP
3. **Entpacke**: Nach `C:\php\`
4. **Füge zu PATH hinzu**: `C:\php\`

##### Chocolatey (Alternative)

```powershell
choco install php
```

---

### 📋 PHP CLI vs Web-PHP

#### PHP CLI (Command Line Interface)

**WICHTIG**: Für KeePass Sync wird **PHP CLI** benötigt, NICHT Web-PHP!

**Unterschiede**:
- **PHP CLI**: Läuft in der Kommandozeile, keine Webserver-Abhängigkeiten
- **Web-PHP**: Läuft über Webserver (Apache/Nginx), hat andere Umgebungsvariablen

**Überprüfung**:
```bash
# PHP CLI
php -v
# Sollte zeigen: "PHP 8.x.x (cli)"

# Web-PHP (falls installiert)
php -i | grep "Server API"
# Sollte zeigen: "Server API => CLI" (für CLI)
```

#### Warum PHP CLI?

- Script läuft über **Cronjob**, nicht über Web
- Keine Webserver-Konfiguration nötig
- Direkter Zugriff auf Dateisystem
- Bessere Performance

---

### 🔐 KeePassXC-CLI Installation auf Server

#### Linux

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
- **KeePassXC**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### macOS

```bash
brew install keepassxc
```

#### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Installiere KeePassXC
3. Stelle sicher, dass `keepassxc-cli.exe` im PATH ist

---

### 🌐 Webserver-Konfiguration (NUR für Web-Schutz)

**WICHTIG**: Script sollte **NUR über Cronjob** laufen. Falls Web-Zugriff möglich ist, muss dieser blockiert werden!

#### Apache (.htaccess)

**Datei**: `php/.htaccess` (bereits im Repository enthalten)

```apache
# Verhindert den direkten Zugriff auf sync.php über den Webbrowser
<Files "sync.php">
    Require all denied
</Files>
```

**Überprüfung**:
```bash
# Teste ob Web-Zugriff blockiert ist
curl http://dein-server.de/php/sync.php
# Sollte 403 Forbidden oder 404 zeigen
```

#### Nginx

**Datei**: `php/nginx.conf` (Beispiel im Repository enthalten)

```nginx
# Beispiel Nginx Konfiguration
location ~ /php/sync.php {
    deny all;
    return 404;  # Optional: Zeige 404 statt 403
}
```

**Integration in Server-Block**:
```nginx
server {
    # ... andere Konfiguration ...
    
    # Schutz für sync.php
    location ~ /php/sync.php {
        deny all;
        return 404;
    }
}
```

**Link**: [Nginx Documentation](https://nginx.org/en/docs/)

---

### ⚙️ Konfiguration

#### 1. Repository auf Server klonen oder Dateien hochladen

```bash
# Via SSH
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Oder: Dateien per FTP/SFTP hochladen
```

#### 2. Erstelle config.json

```bash
# Kopiere Beispiel-Config
cp config.example.json config.json

# Bearbeite config.json
nano config.json  # Oder anderen Editor
```

**Wichtige Einstellungen**:

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
    "cleanupLogs": true,
    "maxLogAgeDays": 7
  }
}
```

**Hinweis**: Die PHP-Variante unterstützt aktuell **nur FTP**. Für SFTP/SMB/SCP nutze die Python-Variante.

---

### ⏰ Cronjob Einrichtung

#### Linux / macOS

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * cd /pfad/zum/projekt/php && /usr/bin/php sync.php >> /pfad/zum/projekt/php/sync_cron.log 2>&1

# Oder mit absoluten Pfaden
0 * * * * /usr/bin/php /pfad/zum/projekt/php/sync.php >> /pfad/zum/projekt/php/sync_cron.log 2>&1
```

**Cronjob-Syntax**:
```
* * * * * Befehl
│ │ │ │ │
│ │ │ │ └─── Wochentag (0-7, Sonntag=0 oder 7)
│ │ │ └───── Monat (1-12)
│ │ └─────── Tag (1-31)
│ └───────── Stunde (0-23)
└─────────── Minute (0-59)
```

**Beispiele**:
```bash
# Jede Stunde
0 * * * * /usr/bin/php /pfad/zum/projekt/php/sync.php

# Alle 6 Stunden
0 */6 * * * /usr/bin/php /pfad/zum/projekt/php/sync.php

# Täglich um 2 Uhr morgens
0 2 * * * /usr/bin/php /pfad/zum/projekt/php/sync.php

# Jeden Montag um 3 Uhr morgens
0 3 * * 1 /usr/bin/php /pfad/zum/projekt/php/sync.php
```

#### Windows

**Task Scheduler**:

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. **Trigger**: Zeitplan (z.B. stündlich)
4. **Aktion**: Programm starten
   - Programm: `C:\xampp\php\php.exe` (oder Pfad zu php.exe)
   - Argumente: `C:\Pfad\zum\projekt\php\sync.php`
   - Start in: `C:\Pfad\zum\projekt\php`

---

### 💻 Verwendung

#### Manuell ausführen

```bash
# Navigiere zum php-Verzeichnis
cd php

# Führe Script aus
php sync.php

# Mit Logging
php sync.php >> sync_manual.log 2>&1
```

#### Überprüfung

```bash
# Überprüfe ob Script läuft
ps aux | grep sync.php  # Linux/macOS

# Überprüfe Logs
tail -f sync_log.txt
```

---

### 🔍 Fehlerbehebung

#### "php: command not found"

**Problem**: PHP CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Linux
sudo apt install php-cli  # Debian/Ubuntu
sudo pacman -S php        # Arch/CachyOS

# macOS
brew install php

# Überprüfe
which php
php --version
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI ist nicht installiert oder nicht im PATH

**Lösung**:
```bash
# Installiere KeePassXC (siehe oben)
# Überprüfe
which keepassxc-cli
keepassxc-cli version

# Falls nicht gefunden, füge zu PATH hinzu
export PATH=$PATH:/usr/bin  # Anpassen je nach Installation
```

#### "Parse error" oder JSON-Fehler

**Problem**: PHP-Version zu alt oder JSON-Extension fehlt

**Lösung**:
```bash
# Überprüfe PHP-Version (min. 7.4)
php --version

# Überprüfe JSON-Extension
php -m | grep json

# Falls fehlt, installiere
sudo apt install php-json  # Debian/Ubuntu
```

#### Cronjob läuft nicht

**Problem**: Cronjob wird nicht ausgeführt

**Lösung**:
```bash
# Überprüfe Crontab
crontab -l

# Überprüfe Cron-Service
sudo systemctl status cron  # Debian/Ubuntu
sudo systemctl status crond # RHEL/CentOS

# Überprüfe Logs
sudo tail -f /var/log/syslog | grep CRON  # Debian/Ubuntu
sudo tail -f /var/log/cron  # RHEL/CentOS
```

#### "Permission denied"

**Problem**: Dateiberechtigungen falsch

**Lösung**:
```bash
# Setze Berechtigungen
chmod 644 config.json
chmod 755 php/
chmod 755 backups/

# Für Script (ausführbar)
chmod +x php/sync.php  # Optional
```

---

### 🙏 Danksagungen

#### PHP

- **Entwickler**: PHP Group
- **Website**: [https://www.php.net/](https://www.php.net/)
- **Lizenz**: PHP License
- **Repository**: [https://github.com/php/php-src](https://github.com/php/php-src)

#### KeePassXC

- **Entwickler**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **Lizenz**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### Apache

- **Entwickler**: Apache Software Foundation
- **Website**: [https://httpd.apache.org/](https://httpd.apache.org/)
- **Lizenz**: Apache 2.0

#### Nginx

- **Entwickler**: Nginx, Inc.
- **Website**: [https://nginx.org/](https://nginx.org/)
- **Lizenz**: BSD 2-Clause

---

## 🇬🇧 English

### ⚠️ IMPORTANT SECURITY WARNING ⚠️

**This script processes SENSITIVE PASSWORDS on a SERVER!**

**DANGERS:**
- ⚠️ If server is compromised = all passwords gone
- ⚠️ PHP errors could log sensitive data
- ⚠️ Web access = high risk

**REQUIREMENTS:**
- ✅ Use only on **TRUSTED SERVER** (VPS/Dedicated)
- ✅ **NO standard web hosting** (KeePassXC-CLI must be installable)
- ✅ Script should run **ONLY via Cronjob** (not via web)
- ✅ `.htaccess` with access restriction (Apache) - already included
- ✅ Nginx: `location` block with `deny all` - example included
- ✅ **HTTPS mandatory** (if web access planned)

**RECOMMENDED**: For desktop use, better use **Python variant** (safer)

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [PHP Installation](#php-installation-1)
3. [PHP CLI vs Web-PHP](#php-cli-vs-web-php-1)
4. [KeePassXC-CLI Installation](#keepassxc-cli-installation-1)
5. [Web Server Configuration](#web-server-configuration)
6. [Configuration](#configuration)
7. [Cronjob Setup](#cronjob-setup)
8. [Usage](#usage)
9. [Troubleshooting](#troubleshooting)
10. [Acknowledgments](#acknowledgments)

---

### 🔧 System Requirements

#### Minimum System Requirements

| Operating System | Minimum | Recommended | Architecture |
|-----------------|---------|-------------|--------------|
| **Linux** | All modern distributions | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x64, ARM64 |

#### Required Software

1. **PHP**
   - **Minimum Version**: 7.4+
   - **Recommended Version**: 8.1+ or 8.2+ (latest stable version)
   - **IMPORTANT**: PHP CLI (Command Line Interface) must be available
   - **Download**: [https://www.php.net/downloads.php](https://www.php.net/downloads.php)

2. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)
   - **IMPORTANT**: Must be installed on the server
   - **Download**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Web Server** (Optional, only for web access - NOT recommended)
   - **Apache**: 2.4+ with mod_php
   - **Nginx**: 1.18+ with PHP-FPM
   - **IMPORTANT**: Script should run ONLY via Cronjob, not via web!

---

### 🐘 PHP Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Install PHP and PHP CLI
sudo pacman -S php php-cli

# Verify
php --version
# Should show: PHP 8.2.x (CLI) or similar

php-cli --version
```

**Package names**: 
- `php` - PHP with CLI
- `php-cli` - PHP Command Line Interface

**Repository**: Extra  
**Link**: [Arch Linux PHP Package](https://archlinux.org/packages/extra/x86_64/php/)

##### Debian / Ubuntu

```bash
# Update package list
sudo apt update

# Install PHP CLI
sudo apt install php-cli php-json

# Verify
php --version
```

**Package names**:
- `php-cli` - PHP Command Line Interface
- `php-json` - JSON support (usually already in php-cli)

**Repository**: Main  
**Link**: [Debian PHP Package](https://packages.debian.org/php-cli)

**Alternative: Latest PHP Version (PHP 8.1/8.2)**

```bash
# For PHP 8.2
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install php8.2-cli
```

**Link**: [Ondřej Surý PPA](https://launchpad.net/~ondrej/+archive/ubuntu/php)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install php-cli php-json
```

##### openSUSE

```bash
sudo zypper install php7-cli php7-json
```

#### macOS

##### Homebrew (Recommended)

```bash
# Install PHP
brew install php

# Verify
php --version
```

**Link**: [Homebrew PHP Formula](https://formulae.brew.sh/formula/php)

##### XAMPP / MAMP (Alternative)

**NOT recommended** for cronjobs, but possible.

#### Windows

##### XAMPP (Recommended for Windows)

1. **Download**: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
2. **Install**: XAMPP with PHP
3. **Verify**: `C:\xampp\php\php.exe --version`

**Link**: [XAMPP](https://www.apachefriends.org/)

##### PHP Standalone

1. **Download**: [https://windows.php.net/download/](https://windows.php.net/download/)
2. **Choose**: PHP 8.x Thread Safe ZIP
3. **Extract**: To `C:\php\`
4. **Add to PATH**: `C:\php\`

##### Chocolatey (Alternative)

```powershell
choco install php
```

---

### 📋 PHP CLI vs Web-PHP

#### PHP CLI (Command Line Interface)

**IMPORTANT**: For KeePass Sync, **PHP CLI** is required, NOT Web-PHP!

**Differences**:
- **PHP CLI**: Runs in command line, no web server dependencies
- **Web-PHP**: Runs via web server (Apache/Nginx), has different environment variables

**Verification**:
```bash
# PHP CLI
php -v
# Should show: "PHP 8.x.x (cli)"

# Web-PHP (if installed)
php -i | grep "Server API"
# Should show: "Server API => CLI" (for CLI)
```

#### Why PHP CLI?

- Script runs via **Cronjob**, not via web
- No web server configuration needed
- Direct file system access
- Better performance

---

### 🔐 KeePassXC-CLI Installation on Server

#### Linux

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
- **KeePassXC**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### macOS

```bash
brew install keepassxc
```

#### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Install KeePassXC
3. Ensure `keepassxc-cli.exe` is in PATH

---

### 🌐 Web Server Configuration (ONLY for Web Protection)

**IMPORTANT**: Script should run **ONLY via Cronjob**. If web access is possible, it must be blocked!

#### Apache (.htaccess)

**File**: `php/.htaccess` (already included in repository)

```apache
# Prevents direct access to sync.php via web browser
<Files "sync.php">
    Require all denied
</Files>
```

**Verification**:
```bash
# Test if web access is blocked
curl http://your-server.com/php/sync.php
# Should show 403 Forbidden or 404
```

#### Nginx

**File**: `php/nginx.conf` (example included in repository)

```nginx
# Example Nginx configuration
location ~ /php/sync.php {
    deny all;
    return 404;  # Optional: Show 404 instead of 403
}
```

**Integration in server block**:
```nginx
server {
    # ... other configuration ...
    
    # Protection for sync.php
    location ~ /php/sync.php {
        deny all;
        return 404;
    }
}
```

**Link**: [Nginx Documentation](https://nginx.org/en/docs/)

---

### ⚙️ Configuration

#### 1. Clone repository on server or upload files

```bash
# Via SSH
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# Or: Upload files via FTP/SFTP
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
    "password": "your-ftp-password",
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
    "databasePassword": "your-keepass-master-password",
    "keepassXCPath": "keepassxc-cli"
  },
  "settings": {
    "debug": false,
    "language": "en",
    "cleanupLogs": true,
    "maxLogAgeDays": 7
  }
}
```

**Note**: The PHP variant currently supports **only FTP**. For SFTP/SMB/SCP, use the Python variant.

---

### ⏰ Cronjob Setup

#### Linux / macOS

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * cd /path/to/project/php && /usr/bin/php sync.php >> /path/to/project/php/sync_cron.log 2>&1

# Or with absolute paths
0 * * * * /usr/bin/php /path/to/project/php/sync.php >> /path/to/project/php/sync_cron.log 2>&1
```

**Cronjob syntax**:
```
* * * * * Command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday=0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

**Examples**:
```bash
# Every hour
0 * * * * /usr/bin/php /path/to/project/php/sync.php

# Every 6 hours
0 */6 * * * /usr/bin/php /path/to/project/php/sync.php

# Daily at 2 AM
0 2 * * * /usr/bin/php /path/to/project/php/sync.php

# Every Monday at 3 AM
0 3 * * 1 /usr/bin/php /path/to/project/php/sync.php
```

#### Windows

**Task Scheduler**:

1. Open Task Scheduler
2. Create new task
3. **Trigger**: Schedule (e.g., hourly)
4. **Action**: Start program
   - Program: `C:\xampp\php\php.exe` (or path to php.exe)
   - Arguments: `C:\Path\to\project\php\sync.php`
   - Start in: `C:\Path\to\project\php`

---

### 💻 Usage

#### Manual execution

```bash
# Navigate to php directory
cd php

# Run script
php sync.php

# With logging
php sync.php >> sync_manual.log 2>&1
```

#### Verification

```bash
# Check if script is running
ps aux | grep sync.php  # Linux/macOS

# Check logs
tail -f sync_log.txt
```

---

### 🔍 Troubleshooting

#### "php: command not found"

**Problem**: PHP CLI is not installed or not in PATH

**Solution**:
```bash
# Linux
sudo apt install php-cli  # Debian/Ubuntu
sudo pacman -S php        # Arch/CachyOS

# macOS
brew install php

# Verify
which php
php --version
```

#### "keepassxc-cli: command not found"

**Problem**: KeePassXC-CLI is not installed or not in PATH

**Solution**:
```bash
# Install KeePassXC (see above)
# Verify
which keepassxc-cli
keepassxc-cli version

# If not found, add to PATH
export PATH=$PATH:/usr/bin  # Adjust according to installation
```

#### "Parse error" or JSON error

**Problem**: PHP version too old or JSON extension missing

**Solution**:
```bash
# Check PHP version (min. 7.4)
php --version

# Check JSON extension
php -m | grep json

# If missing, install
sudo apt install php-json  # Debian/Ubuntu
```

#### Cronjob not running

**Problem**: Cronjob is not executed

**Solution**:
```bash
# Check crontab
crontab -l

# Check cron service
sudo systemctl status cron  # Debian/Ubuntu
sudo systemctl status crond # RHEL/CentOS

# Check logs
sudo tail -f /var/log/syslog | grep CRON  # Debian/Ubuntu
sudo tail -f /var/log/cron  # RHEL/CentOS
```

#### "Permission denied"

**Problem**: File permissions incorrect

**Solution**:
```bash
# Set permissions
chmod 644 config.json
chmod 755 php/
chmod 755 backups/

# For script (executable)
chmod +x php/sync.php  # Optional
```

---

### 🙏 Acknowledgments

#### PHP

- **Developer**: PHP Group
- **Website**: [https://www.php.net/](https://www.php.net/)
- **License**: PHP License
- **Repository**: [https://github.com/php/php-src](https://github.com/php/php-src)

#### KeePassXC

- **Developer**: KeePassXC Team
- **Website**: [https://keepassxc.org/](https://keepassxc.org/)
- **License**: GPL-2.0 / GPL-3.0
- **Repository**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### Apache

- **Developer**: Apache Software Foundation
- **Website**: [https://httpd.apache.org/](https://httpd.apache.org/)
- **License**: Apache 2.0

#### Nginx

- **Developer**: Nginx, Inc.
- **Website**: [https://nginx.org/](https://nginx.org/)
- **License**: BSD 2-Clause

---

## 🇪🇸 Español

### ⚠️ ADVERTENCIA IMPORTANTE DE SEGURIDAD ⚠️

**¡Este script procesa CONTRASEÑAS SENSIBLES en un SERVIDOR!**

**PELIGROS:**
- ⚠️ Si el servidor se compromete = todas las contraseñas perdidas
- ⚠️ Los errores de PHP podrían registrar datos sensibles
- ⚠️ Acceso web = alto riesgo

**REQUISITOS:**
- ✅ Usar solo en **SERVIDOR DE CONFIANZA** (VPS/Dedicado)
- ✅ **NO hosting web estándar** (KeePassXC-CLI debe ser instalable)
- ✅ El script debe ejecutarse **SOLO vía Cronjob** (no vía web)
- ✅ `.htaccess` con restricción de acceso (Apache) - ya incluido
- ✅ Nginx: bloque `location` con `deny all` - ejemplo incluido
- ✅ **HTTPS obligatorio** (si se planifica acceso web)

**RECOMENDADO**: Para uso en escritorio, mejor usar **variante Python** (más segura)

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de PHP](#instalación-de-php)
3. [PHP CLI vs Web-PHP](#php-cli-vs-web-php-1)
4. [Instalación de KeePassXC-CLI](#instalación-de-keepassxc-cli)
5. [Configuración del Servidor Web](#configuración-del-servidor-web)
6. [Configuración](#configuración)
7. [Configuración de Cronjob](#configuración-de-cronjob)
8. [Uso](#uso)
9. [Solución de Problemas](#solución-de-problemas)
10. [Agradecimientos](#agradecimientos)

---

### 🔧 Requisitos del Sistema

#### Requisitos Mínimos del Sistema

| Sistema Operativo | Mínimo | Recomendado | Arquitectura |
|-------------------|--------|-------------|--------------|
| **Linux** | Todas las distribuciones modernas | Ubuntu 20.04+, Debian 11+, Arch Linux | x86_64, ARM64 |
| **Windows** | Windows 7+ | Windows 10/11 | x86_64 |
| **macOS** | macOS 10.13+ | macOS 11+ | x64, ARM64 |

#### Software Requerido

1. **PHP**
   - **Versión Mínima**: 7.4+
   - **Versión Recomendada**: 8.1+ o 8.2+ (última versión estable)
   - **IMPORTANTE**: PHP CLI (Interfaz de Línea de Comandos) debe estar disponible
   - **Descarga**: [https://www.php.net/downloads.php](https://www.php.net/downloads.php)

2. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)
   - **IMPORTANTE**: Debe estar instalado en el servidor
   - **Descarga**: [https://keepassxc.org/download/](https://keepassxc.org/download/)

3. **Servidor Web** (Opcional, solo para acceso web - NO recomendado)
   - **Apache**: 2.4+ con mod_php
   - **Nginx**: 1.18+ con PHP-FPM
   - **IMPORTANTE**: ¡El script debe ejecutarse SOLO vía Cronjob, no vía web!

---

### 🐘 Instalación de PHP

#### Linux

##### Arch Linux / CachyOS

```bash
# Instalar PHP y PHP CLI
sudo pacman -S php php-cli

# Verificar
php --version
# Debería mostrar: PHP 8.2.x (CLI) o similar

php-cli --version
```

**Nombres de paquetes**: 
- `php` - PHP con CLI
- `php-cli` - Interfaz de Línea de Comandos PHP

**Repositorio**: Extra  
**Enlace**: [Paquete Arch Linux PHP](https://archlinux.org/packages/extra/x86_64/php/)

##### Debian / Ubuntu

```bash
# Actualizar lista de paquetes
sudo apt update

# Instalar PHP CLI
sudo apt install php-cli php-json

# Verificar
php --version
```

**Nombres de paquetes**:
- `php-cli` - Interfaz de Línea de Comandos PHP
- `php-json` - Soporte JSON (normalmente ya incluido en php-cli)

**Repositorio**: Main  
**Enlace**: [Paquete Debian PHP](https://packages.debian.org/php-cli)

**Alternativa: Última Versión de PHP (PHP 8.1/8.2)**

```bash
# Para PHP 8.2
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install php8.2-cli
```

**Enlace**: [Ondřej Surý PPA](https://launchpad.net/~ondrej/+archive/ubuntu/php)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install php-cli php-json
```

##### openSUSE

```bash
sudo zypper install php7-cli php7-json
```

#### macOS

##### Homebrew (Recomendado)

```bash
# Instalar PHP
brew install php

# Verificar
php --version
```

**Enlace**: [Homebrew PHP Formula](https://formulae.brew.sh/formula/php)

##### XAMPP / MAMP (Alternativa)

**NO recomendado** para cronjobs, pero posible.

#### Windows

##### XAMPP (Recomendado para Windows)

1. **Descarga**: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
2. **Instala**: XAMPP con PHP
3. **Verifica**: `C:\xampp\php\php.exe --version`

**Enlace**: [XAMPP](https://www.apachefriends.org/)

##### PHP Standalone

1. **Descarga**: [https://windows.php.net/download/](https://windows.php.net/download/)
2. **Elige**: PHP 8.x Thread Safe ZIP
3. **Extrae**: A `C:\php\`
4. **Añade a PATH**: `C:\php\`

##### Chocolatey (Alternativa)

```powershell
choco install php
```

---

### 📋 PHP CLI vs Web-PHP

#### PHP CLI (Interfaz de Línea de Comandos)

**IMPORTANTE**: ¡Para KeePass Sync se requiere **PHP CLI**, NO Web-PHP!

**Diferencias**:
- **PHP CLI**: Se ejecuta en la línea de comandos, sin dependencias del servidor web
- **Web-PHP**: Se ejecuta vía servidor web (Apache/Nginx), tiene otras variables de entorno

**Verificación**:
```bash
# PHP CLI
php -v
# Debería mostrar: "PHP 8.x.x (cli)"

# Web-PHP (si está instalado)
php -i | grep "Server API"
# Debería mostrar: "Server API => CLI" (para CLI)
```

#### ¿Por qué PHP CLI?

- El script se ejecuta vía **Cronjob**, no vía web
- No se requiere configuración del servidor web
- Acceso directo al sistema de archivos
- Mejor rendimiento

---

### 🔐 Instalación de KeePassXC-CLI en el Servidor

#### Linux

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
- **KeePassXC**: [https://keepassxc.org/](https://keepassxc.org/)
- **GitHub**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### macOS

```bash
brew install keepassxc
```

#### Windows

1. Descarga: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Instala KeePassXC
3. Asegúrate de que `keepassxc-cli.exe` esté en PATH

---

### 🌐 Configuración del Servidor Web (SOLO para Protección Web)

**IMPORTANTE**: ¡El script debe ejecutarse **SOLO vía Cronjob**! Si el acceso web es posible, debe ser bloqueado.

#### Apache (.htaccess)

**Archivo**: `php/.htaccess` (ya incluido en el repositorio)

```apache
# Previene el acceso directo a sync.php vía navegador web
<Files "sync.php">
    Require all denied
</Files>
```

**Verificación**:
```bash
# Probar si el acceso web está bloqueado
curl http://tu-servidor.com/php/sync.php
# Debería mostrar 403 Forbidden o 404
```

#### Nginx

**Archivo**: `php/nginx.conf` (ejemplo incluido en el repositorio)

```nginx
# Ejemplo de configuración Nginx
location ~ /php/sync.php {
    deny all;
    return 404;  # Opcional: Mostrar 404 en lugar de 403
}
```

**Integración en bloque del servidor**:
```nginx
server {
    # ... otra configuración ...
    
    # Protección para sync.php
    location ~ /php/sync.php {
        deny all;
        return 404;
    }
}
```

**Enlace**: [Documentación Nginx](https://nginx.org/en/docs/)

---

### ⚙️ Configuración

#### 1. Clonar repositorio en el servidor o subir archivos

```bash
# Vía SSH
git clone https://github.com/SunnyCueq/keepass-sync.git
cd keepass-sync

# O: Subir archivos vía FTP/SFTP
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
    "password": "tu-contraseña-ftp",
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
    "databasePassword": "tu-contraseña-maestra-keepass",
    "keepassXCPath": "keepassxc-cli"
  },
  "settings": {
    "debug": false,
    "language": "es",
    "cleanupLogs": true,
    "maxLogAgeDays": 7
  }
}
```

**Nota**: La variante PHP actualmente admite **solo FTP**. Para SFTP/SMB/SCP, usa la variante Python.

---

### ⏰ Configuración de Cronjob

#### Linux / macOS

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * cd /ruta/a/proyecto/php && /usr/bin/php sync.php >> /ruta/a/proyecto/php/sync_cron.log 2>&1

# O con rutas absolutas
0 * * * * /usr/bin/php /ruta/a/proyecto/php/sync.php >> /ruta/a/proyecto/php/sync_cron.log 2>&1
```

**Sintaxis de Cronjob**:
```
* * * * * Comando
│ │ │ │ │
│ │ │ │ └─── Día de la semana (0-7, Domingo=0 o 7)
│ │ │ └───── Mes (1-12)
│ │ └─────── Día (1-31)
│ └───────── Hora (0-23)
└─────────── Minuto (0-59)
```

**Ejemplos**:
```bash
# Cada hora
0 * * * * /usr/bin/php /ruta/a/proyecto/php/sync.php

# Cada 6 horas
0 */6 * * * /usr/bin/php /ruta/a/proyecto/php/sync.php

# Diariamente a las 2 AM
0 2 * * * /usr/bin/php /ruta/a/proyecto/php/sync.php

# Cada lunes a las 3 AM
0 3 * * 1 /usr/bin/php /ruta/a/proyecto/php/sync.php
```

#### Windows

**Programador de Tareas**:

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. **Desencadenador**: Programación (p. ej., horario)
4. **Acción**: Iniciar programa
   - Programa: `C:\xampp\php\php.exe` (o ruta a php.exe)
   - Argumentos: `C:\Ruta\a\proyecto\php\sync.php`
   - Iniciar en: `C:\Ruta\a\proyecto\php`

---

### 💻 Uso

#### Ejecución manual

```bash
# Navegar al directorio php
cd php

# Ejecutar script
php sync.php

# Con registro
php sync.php >> sync_manual.log 2>&1
```

#### Verificación

```bash
# Verificar si el script está ejecutándose
ps aux | grep sync.php  # Linux/macOS

# Verificar logs
tail -f sync_log.txt
```

---

### 🔍 Solución de Problemas

#### "php: command not found"

**Problema**: PHP CLI no está instalado o no está en PATH

**Solución**:
```bash
# Linux
sudo apt install php-cli  # Debian/Ubuntu
sudo pacman -S php        # Arch/CachyOS

# macOS
brew install php

# Verificar
which php
php --version
```

#### "keepassxc-cli: command not found"

**Problema**: KeePassXC-CLI no está instalado o no está en PATH

**Solución**:
```bash
# Instalar KeePassXC (ver arriba)
# Verificar
which keepassxc-cli
keepassxc-cli version

# Si no se encuentra, añadir a PATH
export PATH=$PATH:/usr/bin  # Ajustar según instalación
```

#### "Parse error" o error JSON

**Problema**: Versión de PHP demasiado antigua o extensión JSON faltante

**Solución**:
```bash
# Verificar versión de PHP (mín. 7.4)
php --version

# Verificar extensión JSON
php -m | grep json

# Si falta, instalar
sudo apt install php-json  # Debian/Ubuntu
```

#### Cronjob no se ejecuta

**Problema**: Cronjob no se ejecuta

**Solución**:
```bash
# Verificar crontab
crontab -l

# Verificar servicio cron
sudo systemctl status cron  # Debian/Ubuntu
sudo systemctl status crond # RHEL/CentOS

# Verificar logs
sudo tail -f /var/log/syslog | grep CRON  # Debian/Ubuntu
sudo tail -f /var/log/cron  # RHEL/CentOS
```

#### "Permission denied"

**Problema**: Permisos de archivo incorrectos

**Solución**:
```bash
# Establecer permisos
chmod 644 config.json
chmod 755 php/
chmod 755 backups/

# Para script (ejecutable)
chmod +x php/sync.php  # Opcional
```

---

### 🙏 Agradecimientos

#### PHP

- **Desarrollador**: Grupo PHP
- **Sitio Web**: [https://www.php.net/](https://www.php.net/)
- **Licencia**: Licencia PHP
- **Repositorio**: [https://github.com/php/php-src](https://github.com/php/php-src)

#### KeePassXC

- **Desarrollador**: Equipo de KeePassXC
- **Sitio Web**: [https://keepassxc.org/](https://keepassxc.org/)
- **Licencia**: GPL-2.0 / GPL-3.0
- **Repositorio**: [https://github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

#### Apache

- **Desarrollador**: Fundación Apache Software
- **Sitio Web**: [https://httpd.apache.org/](https://httpd.apache.org/)
- **Licencia**: Apache 2.0

#### Nginx

- **Desarrollador**: Nginx, Inc.
- **Sitio Web**: [https://nginx.org/](https://nginx.org/)
- **Licencia**: BSD 2-Clause

---

<div align="center">

**🐘 PHP-Variante: Server-basiert, ideal für Cronjobs**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

**⚠️ WICHTIG: Nur für vertrauenswürdige Server!**

</div>
