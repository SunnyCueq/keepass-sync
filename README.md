# 🔐 KeePass Sync - Synchronisiere deine Passwörter automatisch

<div align="center">

**🌍 Languages | Idiomas | Sprachen: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](.)

> **Synchronisiere deine KeePass-Datenbank automatisch zwischen mehreren Computern über einen FTP-Server.**

</div>

---

## 📖 Dokumentation | Documentation | Documentación

Die vollständige Dokumentation ist jetzt nach Sprachen aufgeteilt für bessere Übersichtlichkeit:

**Hauptdokumentation:**
- [🇩🇪 Deutsch](README.de.md) - Vollständige Anleitung auf Deutsch
- [🇬🇧 English](README.en.md) - Complete guide in English
- [🇪🇸 Español](README.es.md) - Guía completa en español

**Installation & Automatisierung:**
- [🇩🇪 Deutsch](docs/INSTALL.de.md) | [🇬🇧 English](docs/INSTALL.en.md) | [🇪🇸 Español](docs/INSTALL.es.md)

**Test-Anleitung:**
- [🇩🇪 Deutsch](docs/TEST.de.md) | [🇬🇧 English](docs/TEST.en.md) | [🇪🇸 Español](docs/TEST.es.md)

**PHP-Variante (für Server-Cronjobs):**
- [php/README.md](php/README.md) - Mit Sicherheits-Warnungen

---

## 🚀 Schnellstart

### 1. Installation

```bash
# Interaktiver Installer (empfohlen)
python3 install.py
```

### 2. Synchronisation

```bash
# Normale Sync
python3 python/sync_ftp.py

# Verbindung testen (ohne Backup)
python3 python/sync_ftp.py --test

# Status anzeigen
python3 python/sync_ftp.py --status
```

### 3. Automatische Ausführung

**Linux:**
```bash
./linux/install.sh  # Schnellinstallation
```

**Windows/macOS:** Siehe [docs/INSTALL.de.md](docs/INSTALL.de.md)

---

## 📡 Unterstützte Protokolle

- ✅ **FTP** (Standard)
- ✅ **SFTP** (SSH-verschlüsselt)
- ✅ **SMB/CIFS** (Windows-Netzwerk)
- ✅ **SCP** (SSH-basiert)

---

## 🌍 Unterstützte Sprachen

**12 Sprachen:** Deutsch, English, Español, Français, Italiano, Português, Nederlands, Polski, Русский, 中文, 日本語, 한국어

---

## ⚠️ PHP-Variante verfügbar

Für Server-basierte Cronjobs gibt es eine **PHP-Variante** mit deutlichen Sicherheits-Warnungen.

**⚠️ WICHTIG:** Nur für eigene Server (VPS/Dedicated) verwenden!

- [php/README.md](php/README.md) - Dokumentation & Sicherheits-Warnungen
- [php/sync.php](php/sync.php) - PHP-Script

---

<div align="center">

**Entwickelt für:** Linux, Windows, macOS  
**Version:** 1.1.0  
**Sprachen:** Deutsch, English, Español (+ 9 weitere)

**⭐ Wenn dir dieses Projekt gefällt, gib uns einen Stern auf GitHub!**

**🌍 Languages: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

</div>
