# 🚀 Release-Vorlagen für GitHub

## Version 1.0.0 (Initial Release)

### Release Title:
```
v1.0.0 - Initial Release
```

oder

```
🚀 v1.0.0 - Initial Release: Cross-Platform KeePass Sync Tool
```

### Release Beschreibung:

```markdown
## 🎉 Initial Release - KeePass Sync v1.0.0

### ✨ Features

- ✅ **Cross-Platform Support** - Linux, Windows, macOS
- ✅ **Multi-Language** - Deutsch, English, Español
- ✅ **Automatic Backups** - Intelligent backup management (keeps only 2 newest)
- ✅ **Log Management** - Automatic cleanup of old logs
- ✅ **FTP Support** - Secure file synchronization via FTP
- ✅ **Easy Installation** - One-click installation scripts for Linux
- ✅ **Automation Ready** - Systemd, Cron, Task Scheduler support

### 📦 Was ist enthalten?

- Cross-platform Python script
- Platform-specific wrappers (Bash, PowerShell, Batch)
- Comprehensive documentation (multi-language)
- Example configuration file
- Installation scripts

### 🛠️ Installation

```bash
# Linux - Quick Install
./linux/install.sh

# Or manually
python3 sync.py
```

### 📖 Dokumentation

- [README.md](README.md) - Getting Started Guide
- [INSTALL.md](INSTALL.md) - Installation & Automation Guide
- [TEST.md](TEST.md) - Testing Guide

### 🌍 Supported Languages

- 🇩🇪 Deutsch
- 🇬🇧 English  
- 🇪🇸 Español

### 🔐 Requirements

- KeePassXC (with keepassxc-cli)
- Python 3.6+
- FTP Server Access

### 📝 Changelog

**Initial Release:**
- First stable version
- Cross-platform synchronization
- Multi-language support
- Automatic backup and log management
- FTP protocol support

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Full Changelog:** Initial release - [7ce4fda...v1.0.0](https://github.com/SunnyCueq/keepass-sync/compare/7ce4fda...v1.0.0)
```

---

## Version 1.1.0 (Feature Release - z.B. SFTP)

### Release Title:
```
🚀 v1.1.0 - SFTP Support & Improvements
```

### Release Beschreibung:

```markdown
## 🎉 v1.1.0 - SFTP Support & Improvements

### ✨ New Features

- ✅ **SFTP Support** - Secure File Transfer Protocol (SSH-based)
- ✅ **SCP Support** - Secure Copy Protocol
- ✅ **Protocol Selection** - Choose between FTP, SFTP, SCP in config
- ✅ **Enhanced Error Handling** - Better error messages and retry logic

### 🔧 Improvements

- Improved connection stability
- Better timeout handling
- Enhanced logging

### 🐛 Bug Fixes

- Fixed connection issues on some FTP servers
- Resolved path handling on Windows

### 📖 Documentation

- Updated INSTALL.md with SFTP setup instructions
- Added protocol comparison guide

### ⬇️ Download

**Installation:**
```bash
git pull origin main
# Or download from releases
```

**Full Changelog:** [v1.0.0...v1.1.0](https://github.com/SunnyCueq/keepass-sync/compare/v1.0.0...v1.1.0)
```

---

## Version 1.0.1 (Patch Release)

### Release Title:
```
🔧 v1.0.1 - Bug Fixes & Improvements
```

### Release Beschreibung:

```markdown
## 🔧 v1.0.1 - Bug Fixes & Improvements

### 🐛 Bug Fixes

- Fixed configuration file path detection on Windows
- Resolved encoding issues with non-ASCII characters
- Corrected backup cleanup logic

### 🔧 Improvements

- Better error messages
- Improved log formatting
- Enhanced documentation

### 📖 Documentation

- Updated troubleshooting section
- Added Windows-specific notes

**Full Changelog:** [v1.0.0...v1.0.1](https://github.com/SunnyCueq/keepass-sync/compare/v1.0.0...v1.0.1)
```

---

## 📋 Release Checklist

Vor jedem Release:

- [ ] Alle Änderungen in CHANGELOG.md dokumentiert
- [ ] Version in README.md aktualisiert
- [ ] Code getestet auf allen Plattformen
- [ ] Dokumentation aktualisiert
- [ ] Release Notes vorbereitet
- [ ] Tag erstellt: `git tag -a v1.0.0 -m "Release v1.0.0"`
- [ ] Tag gepusht: `git push origin v1.0.0`
- [ ] Release auf GitHub erstellt

---

## 💡 Tipps

- **Versionierung:** SemVer (Semantic Versioning)
  - `MAJOR.MINOR.PATCH`
  - Beispiel: `1.0.0` → `1.1.0` (Feature) → `1.1.1` (Patch) → `2.0.0` (Breaking Changes)

- **Release Title:** Kurz und prägnant
- **Beschreibung:** Markdown-Format, strukturiert, mit Highlights

