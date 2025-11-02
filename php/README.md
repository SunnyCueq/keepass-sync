# 🐘 KeePass Sync - PHP-Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

⚠️ **WARNUNG | WARNING | ADVERTENCIA:** Diese Variante verarbeitet sensible Passwörter auf einem Server! | This variant processes sensitive passwords on a server! | Esta variante procesa contraseñas sensibles en un servidor!

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
- ✅ **HTTPS zwingend erforderlich**
- ✅ Regelmäßige Sicherheits-Updates
- ✅ Logs regelmäßig prüfen

**EMPFOHLEN:** Für Desktop-Nutzung besser **Python-Variante** verwenden (sicherer)

### Wann macht PHP Sinn?

✅ **PHP ist sinnvoll wenn:**
- Du einen eigenen Server hast (VPS/Dedicated mit Root-Zugriff)
- Server-basierte Cronjobs gewünscht sind
- Bestehende PHP-Infrastruktur vorhanden ist
- Zentrale Synchronisation für mehrere Clients

❌ **PHP macht KEINEN Sinn wenn:**
- Standard Webhosting (kein Root-Zugriff)
- Sicherheit ist kritisch (Desktop besser)
- KeePassXC-CLI nicht installierbar

### Installation

#### 1. Voraussetzungen

- **KeePassXC** auf Server installieren:
  ```bash
  sudo apt install keepassxc  # Debian/Ubuntu
  sudo pacman -S keepassxc    # Arch/CachyOS
  ```

- **PHP CLI** muss verfügbar sein:
  ```bash
  php -v  # Sollte PHP 7.4+ zeigen
  ```

#### 2. Konfiguration

Die PHP-Variante nutzt die gleiche `config.json` wie die Python-Variante:

```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-ftp-passwort",
    "type": "ftp",
    "remotePath": "/keepass_passwords.kdbx"
  },
  "keepass": {
    "databasePassword": "dein-keeppass-master-passwort",
    "keepassXCPath": "keepassxc-cli"
  }
}
```

**Hinweis:** Die PHP-Variante unterstützt **nur FTP**. Für SFTP/SMB/SCP nutze die Python-Variante.

#### 3. Sicherheits-Konfiguration

**Apache (.htaccess):**
```apache
# php/sync.php vor Web-Zugriff schützen
<Files "sync.php">
    Order Deny,Allow
    Deny from all
</Files>

# Oder für Apache 2.4+
<Files "sync.php">
    Require all denied
</Files>
```

**Nginx:**
```nginx
location ~ /php/sync\.php$ {
    deny all;
    return 403;
}
```

**Zusätzlich:** Script ausführbar machen:
```bash
chmod +x php/sync.php
```

#### 4. Cronjob einrichten

**Beispiel (täglich um 3 Uhr):**
```bash
0 3 * * * /usr/bin/php /pfad/zum/keepass-sync/php/sync.php >> /pfad/zum/keepass-sync/sync_cron.log 2>&1
```

**Oder alle 6 Stunden:**
```bash
0 */6 * * * /usr/bin/php /pfad/zum/keepass-sync/php/sync.php >> /pfad/zum/keepass-sync/sync_cron.log 2>&1
```

**Cronjob hinzufügen:**
```bash
crontab -e
```

#### 5. Testen

```bash
# Manuell testen (CLI)
php php/sync.php

# Oder direkt
./php/sync.php
```

### Unterstützte Protokolle

- ✅ **FTP** - Native PHP-Unterstützung
- ❌ **SFTP** - Braucht `ssh2` Extension (nicht überall verfügbar)
- ❌ **SMB** - Nicht vorhanden in PHP
- ❌ **SCP** - Nicht vorhanden in PHP

**Empfehlung:** Für andere Protokolle nutze die Python-Variante.

### Apache vs Nginx

**Für Cronjobs:** Kein Unterschied - beide nutzen `php-cli`

**Für Web-API (nicht empfohlen):**
- **Apache:** `mod_php` oder `php-fpm`
- **Nginx:** `php-fpm`

### Fehlerbehebung

**"KeePassXC-CLI not found"**
- Installiere KeePassXC auf dem Server
- Oder setze korrekten Pfad in `config.json`

**"FTP login failed"**
- Prüfe Benutzername/Passwort
- Prüfe ob FTP-Server erreichbar ist
- Prüfe Firewall-Regeln

**"Could not connect to FTP server"**
- Prüfe Hostname/IP
- Prüfe Port (Standard: 21)
- Prüfe Firewall

### Logs

- **PHP-Logs:** `php_error.log` (im php-Verzeichnis)
- **Sync-Logs:** `sync_log.txt` (im Hauptverzeichnis)
- **Cron-Logs:** `sync_cron.log` (wenn in Cronjob konfiguriert)

---

## 🇬🇧 English

### ⚠️ IMPORTANT SECURITY WARNING

**This script processes SENSITIVE PASSWORDS on a SERVER!**

**RISKS:**
- ⚠️ Server compromise = all passwords lost
- ⚠️ PHP errors might log sensitive data
- ⚠️ Web access = high risk
- ⚠️ Passwords processed in RAM

**REQUIREMENTS:**
- ✅ Only use on **TRUSTED server** (VPS/Dedicated)
- ✅ **NO standard web hosting** (KeePassXC-CLI must be installable)
- ✅ Script should **ONLY run via Cronjob** (not via web)
- ✅ `.htaccess` with access restrictions (Apache)
- ✅ Nginx: `location` block with `deny all`
- ✅ **HTTPS mandatory**
- ✅ Regular security updates
- ✅ Regular log checks

**RECOMMENDED:** For desktop use, better use **Python variant** (safer)

### When does PHP make sense?

✅ **PHP is useful if:**
- You have your own server (VPS/Dedicated with root access)
- Server-based cronjobs desired
- Existing PHP infrastructure available
- Central synchronization for multiple clients

❌ **PHP does NOT make sense if:**
- Standard web hosting (no root access)
- Security is critical (desktop better)
- KeePassXC-CLI not installable

### Installation

#### 1. Prerequisites

- **Install KeePassXC** on server:
  ```bash
  sudo apt install keepassxc  # Debian/Ubuntu
  sudo pacman -S keepassxc    # Arch/CachyOS
  ```

- **PHP CLI** must be available:
  ```bash
  php -v  # Should show PHP 7.4+
  ```

#### 2. Configuration

The PHP variant uses the same `config.json` as the Python variant.

**Note:** The PHP variant supports **FTP only**. For SFTP/SMB/SCP use the Python variant.

#### 3. Security Configuration

**Apache (.htaccess):**
```apache
<Files "sync.php">
    Require all denied
</Files>
```

**Nginx:**
```nginx
location ~ /php/sync\.php$ {
    deny all;
    return 403;
}
```

#### 4. Setup Cronjob

**Example (daily at 3 AM):**
```bash
0 3 * * * /usr/bin/php /path/to/keepass-sync/php/sync.php >> /path/to/keepass-sync/sync_cron.log 2>&1
```

#### 5. Testing

```bash
php php/sync.php
```

---

## 🇪🇸 Español

### ⚠️ ADVERTENCIA DE SEGURIDAD IMPORTANTE

**¡Este script procesa CONTRASEÑAS SENSIBLES en un SERVIDOR!**

**RIESGOS:**
- ⚠️ Compromiso del servidor = todas las contraseñas perdidas
- ⚠️ Errores PHP podrían registrar datos sensibles
- ⚠️ Acceso web = alto riesgo
- ⚠️ Contraseñas procesadas en RAM

**REQUISITOS:**
- ✅ Solo usar en servidor **CONFIABLE** (VPS/Dedicado)
- ✅ **NO hosting web estándar** (KeePassXC-CLI debe ser instalable)
- ✅ El script debe ejecutarse **SOLO vía Cronjob** (no vía web)

**RECOMENDADO:** Para uso en escritorio, mejor usar **variante Python** (más seguro)

### Instalación

1. Instalar KeePassXC en servidor
2. Configurar `config.json` (igual que Python-Variante)
3. Configurar seguridad (.htaccess o Nginx)
4. Configurar Cronjob

**Nota:** La variante PHP solo admite **FTP**. Para SFTP/SMB/SCP usa la variante Python.

---

## 🔒 Sicherheit | Security | Seguridad

**WICHTIG | IMPORTANT | IMPORTANTE:**

1. ✅ Script NUR über CLI ausführen (Web-Zugriff verhindern)
2. ✅ .htaccess oder Nginx-Konfiguration setzen
3. ✅ HTTPS verwenden (wenn Web-API genutzt)
4. ✅ Regelmäßige Backups
5. ✅ Logs regelmäßig prüfen
6. ✅ Server-Sicherheit gewährleisten

**NICHT:**
- ❌ Script über Web aufrufen
- ❌ Passwörter im Log speichern
- ❌ Öffentlichen Zugriff erlauben

---

**← Zurück zur Hauptdokumentation:** [README.de.md](../README.de.md) | [README.en.md](../README.en.md) | [README.es.md](../README.es.md)

