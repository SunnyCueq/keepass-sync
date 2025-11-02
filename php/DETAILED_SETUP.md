# 📖 Detaillierte Installations- und Setup-Anleitung - PHP Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![PHP](https://img.shields.io/badge/PHP-7.4+-777BB4.svg?logo=php&logoColor=white)](https://www.php.net/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Server-basiert - Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

---

## 🇩🇪 Deutsch

### ⚠️ WICHTIGE SICHERHEITSWARNUNG

**Dieses Script verarbeitet SENSIBLE PASSWÖRTER auf einem SERVER!**

**GEFAHREN:**
- ⚠️ Bei Server-Kompromittierung = alle Passwörter weg
- ⚠️ PHP-Fehler könnten sensible Daten loggen
- ⚠️ Zugriff über Web = hohes Risiko
- ⚠️ Passwörter werden im RAM verarbeitet

**ANFORDERUNGEN:**
- ✅ Nur auf **VERTRAUENSWÜRDIGEM Server** verwenden (VPS/Dedicated)
- ✅ **KEIN Standard-Webhosting** (KeePassXC-CLI muss installierbar sein)
- ✅ Script sollte **NUR über Cronjob** laufen (nicht über Web)
- ✅ `.htaccess` mit Zugriffsbeschränkung (Apache)
- ✅ Nginx: `location` block mit `deny all`
- ✅ **HTTPS zwingend erforderlich** (wenn Web-Zugriff geplant)
- ✅ Regelmäßige Sicherheits-Updates

**EMPFOHLEN**: Für Desktop-Nutzung besser **Python-Variante** verwenden (sicherer)

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
    Order Deny,Allow
    Deny from all
</Files>

# Oder für Apache 2.4+
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

<div align="center">

**🐘 PHP-Variante: Server-basiert, ideal für Cronjobs**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

**⚠️ WICHTIG: Nur für vertrauenswürdige Server!**

</div>

