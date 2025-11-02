# ⚙️ KeePass Sync - C/C++ Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![C++](https://img.shields.io/badge/C%2B%2B-11+-00599C.svg?logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Native Performance, minimaler Memory-Footprint**

</div>

---

## 📚 Navigation | Navegación | Navigation

### Varianten | Variants | Variantes

**Wähle deine Programmiersprache | Choose your language | Elige tu lenguaje:**

- [🐍 Python](../python/README.md) - Hauptvariante | Main variant | Variante principal
- [🐹 Go (Golang)](../go/README.md) - Schnell, portabel | Fast, portable | Rápido, portable
- [📦 Node.js](../nodejs/README.md) - JavaScript Runtime | JavaScript Runtime | Runtime JavaScript
- [🤖 AutoIt](../autoit/README.md) - Windows-native | Windows-native | Windows nativo
- [💻 PowerShell](../powershell/README.md) - Windows-Scripting | Windows Scripting | Scripting Windows
- [⚙️ C/C++](./README.md) - Native Performance | Native Performance | Rendimiento nativo ⭐ **Hier**
- [🐘 PHP](../php/README.md) - Server Cronjobs | Server Cronjobs | Cronjobs servidor
- [💼 COBOL](../cobol/README.md) - Legacy & Mainframe | Legacy & Mainframe | Legacy y Mainframe

### Hauptdokumentation | Main Documentation | Documentación Principal

- [🏠 Hauptseite](../README.md) | [Main Page](../README.en.md) | [Página Principal](../README.es.md)
- [📖 Installationsanleitung](../docs/INSTALL.de.md) | [Installation Guide](../docs/INSTALL.en.md) | [Guía de Instalación](../docs/INSTALL.es.md)
- [🧪 Test-Anleitung](../docs/TEST.de.md) | [Test Guide](../docs/TEST.en.md) | [Guía de Pruebas](../docs/TEST.es.md)

---

## 🇩🇪 Deutsch

### ⚠️ HINWEIS: Basis-Implementierung

Die C/C++-Variante ist eine **Basis-Implementierung** mit vereinfachtem JSON-Parser. Für Produktionsnutzung sollte `jsoncpp` oder eine andere JSON-Library verwendet werden.

### 📋 Inhaltsverzeichnis

1. [Systemanforderungen](#systemanforderungen)
2. [C++ Compiler Installation](#c-compiler-installation)
3. [Build-Systeme](#build-systeme)
4. [JSON-Library (Optional)](#json-library-optional)
5. [Externe Dependencies](#externe-dependencies)
6. [Kompilierung](#kompilierung)
7. [Konfiguration](#konfiguration)
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
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Erforderliche Software

1. **C++ Compiler**
   - **Minimale Version**: C++11 kompatibel
   - **GCC**: 4.8.1+ (Linux/macOS)
   - **Clang**: 3.3+ (Linux/macOS)
   - **MSVC**: Visual Studio 2015+ (Windows)

2. **Build-System** (Optional, aber empfohlen)
   - **Make**: Für Makefile
   - **CMake**: 3.10+ (für CMakeLists.txt)

3. **KeePassXC-CLI**
   - **Minimale Version**: 2.6.0+
   - **Empfohlene Version**: 2.7.0+ (aktuellste Version)

4. **Externe Tools** (abhängig vom Protokoll):
   - **lftp**: Für FTP/SFTP-Übertragungen
   - **smbclient**: Für SMB/CIFS-Netzwerk-Shares
   - **sshpass** & **scp**: Für SCP-Übertragungen

---

### 🔨 C++ Compiler Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Installiere GCC und Make
sudo pacman -S gcc make cmake

# Überprüfe
gcc --version
# Sollte zeigen: gcc 11.x.x oder höher

make --version
cmake --version
```

**Paketnamen**: 
- `gcc` - GCC Compiler
- `make` - Make Build-Tool
- `cmake` - CMake Build-System

**Link**: [Arch Linux GCC Package](https://archlinux.org/packages/core/x86_64/gcc/)

##### Debian / Ubuntu

```bash
# Installiere Build-Essentials
sudo apt update
sudo apt install build-essential cmake

# Überprüfe
gcc --version
make --version
cmake --version
```

**Paketnamen**:
- `build-essential` - Enthält gcc, g++, make, etc.
- `cmake` - CMake Build-System

**Link**: [Debian Build-Essential](https://packages.debian.org/build-essential)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install gcc gcc-c++ make cmake
```

##### openSUSE

```bash
sudo zypper install gcc gcc-c++ make cmake
```

#### macOS

##### Xcode Command Line Tools (Empfohlen)

```bash
# Installiere Command Line Tools
xcode-select --install

# Überprüfe
gcc --version
# Oder:
clang --version
```

**Link**: [Xcode Command Line Tools](https://developer.apple.com/xcode/)

##### Homebrew (Alternative)

```bash
# Installiere GCC
brew install gcc

# Installiere CMake
brew install cmake

# Überprüfe
gcc-11 --version  # Version kann variieren
cmake --version
```

**Link**: [Homebrew GCC Formula](https://formulae.brew.sh/formula/gcc)

#### Windows

##### Visual Studio (Empfohlen)

1. **Download**: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
2. **Wähle**: Visual Studio Community (kostenlos)
3. **Bei Installation**: Wähle "Desktop development with C++" Workload
4. **Überprüfe**: Öffne "Developer Command Prompt for VS"
```powershell
cl
# Sollte Compiler-Version zeigen
```

**Link**: [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/)

##### MinGW-w64 (Alternative)

1. **Download**: [https://www.mingw-w64.org/downloads/](https://www.mingw-w64.org/downloads/)
2. **Oder**: MSYS2 installieren (enthält MinGW-w64)
3. **MSYS2**: [https://www.msys2.org/](https://www.msys2.org/)

**Installation via MSYS2**:
```bash
# In MSYS2 Terminal
pacman -S mingw-w64-x86_64-gcc
pacman -S mingw-w64-x86_64-make
pacman -S mingw-w64-x86_64-cmake

# Füge zu PATH hinzu: C:\msys64\mingw64\bin
```

**Link**: [MinGW-w64](https://www.mingw-w64.org/)
**Link**: [MSYS2](https://www.msys2.org/)

##### Chocolatey (Alternative)

```powershell
# Installiere MinGW oder Visual Studio Build Tools
choco install mingw

# Oder Visual Studio Build Tools
choco install visualstudio2019buildtools
```

---

### 📦 Build-Systeme

#### Make (Einfach, für Makefile)

**Makefile ist bereits im Repository enthalten**: `cpp/Makefile`

**Verwendung**:
```bash
cd cpp
make
```

#### CMake (Empfohlen, für größere Projekte)

**CMakeLists.txt ist bereits im Repository enthalten**: `cpp/CMakeLists.txt`

**Verwendung**:
```bash
cd cpp
mkdir build
cd build
cmake ..
make  # Linux/macOS
# Oder: cmake --build . --config Release  # Windows
```

---

### 📚 JSON-Library (Optional)

#### jsoncpp (Empfohlen für Produktion)

Die Basis-Implementierung nutzt einen vereinfachten JSON-Parser. Für bessere Funktionalität kann `jsoncpp` verwendet werden.

##### Linux

```bash
# Debian/Ubuntu
sudo apt install libjsoncpp-dev

# Arch/CachyOS
sudo pacman -S jsoncpp

# Fedora
sudo dnf install jsoncpp-devel
```

##### macOS

```bash
brew install jsoncpp
```

##### Windows

**vcpkg** (Empfohlen):
```powershell
# Installiere vcpkg
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat

# Installiere jsoncpp
.\vcpkg install jsoncpp:x64-windows
```

**Link**: [vcpkg](https://github.com/microsoft/vcpkg)

**Kompilierung mit jsoncpp**:
```bash
# Linux/macOS
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp

# Windows (vcpkg)
# Siehe vcpkg-Dokumentation für Include-Pfade
```

---

### 📦 Externe Dependencies

#### 1. KeePassXC-CLI (ERFORDERLICH)

**Zweck**: Zum Mergen der KeePass-Datenbanken

##### Linux

```bash
sudo apt install keepassxc  # Debian/Ubuntu
sudo pacman -S keepassxc    # Arch/CachyOS
sudo dnf install keepassxc  # Fedora
```

**Links**:
- **KeePassXC**: [https://keepassxc.org/](https://keepassxc.org/)

##### macOS

```bash
brew install keepassxc
```

##### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Installiere KeePassXC
3. Stelle sicher, dass `keepassxc-cli.exe` im PATH ist

#### 2. lftp (Für FTP/SFTP - EMPFOHLEN)

**Zweck**: Datei-Übertragungen via FTP und SFTP

##### Linux

```bash
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS
sudo dnf install lftp  # Fedora
```

**Links**:
- **lftp**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### macOS

```bash
brew install lftp
```

##### Windows

**Via WSL oder Git Bash**:
```bash
# In WSL
sudo apt install lftp
```

#### 3. smbclient (Für SMB/CIFS - Optional)

**Zweck**: Zugriff auf Windows-Netzwerk-Shares

##### Linux

```bash
sudo apt install smbclient  # Debian/Ubuntu
sudo pacman -S samba       # Arch/CachyOS
```

**Links**:
- **Samba**: [https://www.samba.org/](https://www.samba.org/)

##### macOS

```bash
brew install samba
```

##### Windows

Windows hat native SMB-Unterstützung.

---

### 🔨 Kompilierung

#### Methode 1: Mit Makefile (Einfach)

```bash
cd cpp

# Kompiliere
make

# Überprüfe
./keepass-sync --version
```

#### Methode 2: Mit CMake (Empfohlen)

```bash
cd cpp
mkdir build
cd build

# Konfiguriere
cmake ..

# Kompiliere
make  # Linux/macOS
# Oder: cmake --build . --config Release  # Windows

# Überprüfe
./keepass-sync --version
```

#### Methode 3: Manuell

```bash
cd cpp

# Linux/macOS
g++ -std=c++11 -Wall -O2 -o keepass-sync sync.cpp

# Windows (MinGW)
g++ -std=c++11 -Wall -O2 -o keepass-sync.exe sync.cpp
```

#### Cross-Platform Kompilierung

**Für Windows (von Linux/macOS)**:
```bash
# Installiere MinGW Cross-Compiler
sudo apt install mingw-w64  # Debian/Ubuntu

# Kompiliere
x86_64-w64-mingw32-g++ -std=c++11 -o keepass-sync.exe sync.cpp
```

---

### ⚙️ Konfiguration

Die C++-Variante nutzt die gleiche `config.json` wie die Python-Variante.

**WICHTIG**: Der vereinfachte JSON-Parser unterstützt nicht alle JSON-Features. Für komplexe Konfigurationen nutze `jsoncpp`.

**Beispiel config.json**:

```json
{
  "ftp": {
    "host": "dein-server.com",
    "user": "dein-benutzername",
    "password": "dein-passwort",
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
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

---

### 💻 Verwendung

```bash
# Normale Synchronisation
./keepass-sync

# Verbindung testen
./keepass-sync --test

# Status anzeigen
./keepass-sync --status

# Version
./keepass-sync --version

# Hilfe
./keepass-sync --help
```

#### Automatisierung

##### Cron (Linux/macOS)

```bash
# Öffne Crontab
crontab -e

# Füge hinzu (jede Stunde)
0 * * * * cd /pfad/zum/projekt/cpp && ./keepass-sync
```

##### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Zeitplan
4. Aktion: Programm starten
   - Programm: `C:\Pfad\zum\keepass-sync.exe`
   - Start in: `C:\Pfad\zum\cpp`

---

### 🔍 Fehlerbehebung

#### Kompilierungsfehler

**Problem**: C++11 nicht unterstützt

**Lösung**:
```bash
# Überprüfe Compiler-Version
gcc --version  # Sollte 4.8.1+ sein

# Aktualisiere Compiler falls nötig
```

#### "jsoncpp not found"

**Problem**: jsoncpp nicht installiert (optional)

**Lösung**: Die Basis-Variante funktioniert OHNE jsoncpp, nutzt vereinfachten Parser.

#### "lftp not found"

**Problem**: lftp ist nicht installiert

**Lösung**: Siehe Installation oben

#### Linker-Fehler

**Problem**: Bibliotheken nicht gefunden

**Lösung**:
```bash
# Mit jsoncpp (falls verwendet)
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp

# Überprüfe Library-Pfade
pkg-config --libs jsoncpp  # Linux
```

---

### 🙏 Danksagungen

#### C++ Standard

- **Entwickler**: ISO C++ Committee
- **Website**: [https://isocpp.org/](https://isocpp.org/)
- **Standard**: C++11 / C++14 / C++17

#### GCC

- **Entwickler**: GNU Project
- **Website**: [https://gcc.gnu.org/](https://gcc.gnu.org/)
- **Lizenz**: GPL

#### Clang

- **Entwickler**: LLVM Project
- **Website**: [https://clang.llvm.org/](https://clang.llvm.org/)
- **Lizenz**: Apache 2.0

#### Visual Studio

- **Entwickler**: Microsoft
- **Website**: [https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/)

#### CMake

- **Entwickler**: Kitware
- **Website**: [https://cmake.org/](https://cmake.org/)
- **Lizenz**: BSD 3-Clause

#### jsoncpp (Optional)

- **Entwickler**: jsoncpp Contributors
- **Website**: [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp)
- **Lizenz**: Public Domain / MIT

---

## 🇬🇧 English

### ⚠️ NOTE: Basic Implementation

The C/C++ variant is a **basic implementation** with a simplified JSON parser. For production use, `jsoncpp` or another JSON library should be used.

### 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [C++ Compiler Installation](#c-compiler-installation-1)
3. [Build Systems](#build-systems)
4. [JSON Library (Optional)](#json-library-optional-1)
5. [External Dependencies](#external-dependencies)
6. [Compilation](#compilation)
7. [Configuration](#configuration)
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
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Required Software

1. **C++ Compiler**
   - **Minimum Version**: C++11 compatible
   - **GCC**: 4.8.1+ (Linux/macOS)
   - **Clang**: 3.3+ (Linux/macOS)
   - **MSVC**: Visual Studio 2015+ (Windows)

2. **Build System** (Optional, but recommended)
   - **Make**: For Makefile
   - **CMake**: 3.10+ (for CMakeLists.txt)

3. **KeePassXC-CLI**
   - **Minimum Version**: 2.6.0+
   - **Recommended Version**: 2.7.0+ (latest version)

4. **External Tools** (depending on protocol):
   - **lftp**: For FTP/SFTP transfers
   - **smbclient**: For SMB/CIFS network shares
   - **sshpass** & **scp**: For SCP transfers

---

### 🔨 C++ Compiler Installation

#### Linux

##### Arch Linux / CachyOS

```bash
# Install GCC and Make
sudo pacman -S gcc make cmake

# Verify
gcc --version
# Should show: gcc 11.x.x or higher

make --version
cmake --version
```

**Package names**: 
- `gcc` - GCC Compiler
- `make` - Make Build Tool
- `cmake` - CMake Build System

**Link**: [Arch Linux GCC Package](https://archlinux.org/packages/core/x86_64/gcc/)

##### Debian / Ubuntu

```bash
# Install build essentials
sudo apt update
sudo apt install build-essential cmake

# Verify
gcc --version
make --version
cmake --version
```

**Package names**:
- `build-essential` - Contains gcc, g++, make, etc.
- `cmake` - CMake Build System

**Link**: [Debian Build-Essential](https://packages.debian.org/build-essential)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install gcc gcc-c++ make cmake
```

##### openSUSE

```bash
sudo zypper install gcc gcc-c++ make cmake
```

#### macOS

##### Xcode Command Line Tools (Recommended)

```bash
# Install Command Line Tools
xcode-select --install

# Verify
gcc --version
# Or:
clang --version
```

**Link**: [Xcode Command Line Tools](https://developer.apple.com/xcode/)

##### Homebrew (Alternative)

```bash
# Install GCC
brew install gcc

# Install CMake
brew install cmake

# Verify
gcc-11 --version  # Version may vary
cmake --version
```

**Link**: [Homebrew GCC Formula](https://formulae.brew.sh/formula/gcc)

#### Windows

##### Visual Studio (Recommended)

1. **Download**: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
2. **Choose**: Visual Studio Community (free)
3. **During installation**: Select "Desktop development with C++" workload
4. **Verify**: Open "Developer Command Prompt for VS"
```powershell
cl
# Should show compiler version
```

**Link**: [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/)

##### MinGW-w64 (Alternative)

1. **Download**: [https://www.mingw-w64.org/downloads/](https://www.mingw-w64.org/downloads/)
2. **Or**: Install MSYS2 (contains MinGW-w64)
3. **MSYS2**: [https://www.msys2.org/](https://www.msys2.org/)

**Installation via MSYS2**:
```bash
# In MSYS2 Terminal
pacman -S mingw-w64-x86_64-gcc
pacman -S mingw-w64-x86_64-make
pacman -S mingw-w64-x86_64-cmake

# Add to PATH: C:\msys64\mingw64\bin
```

**Link**: [MinGW-w64](https://www.mingw-w64.org/)
**Link**: [MSYS2](https://www.msys2.org/)

##### Chocolatey (Alternative)

```powershell
# Install MinGW or Visual Studio Build Tools
choco install mingw

# Or Visual Studio Build Tools
choco install visualstudio2019buildtools
```

---

### 📦 Build Systems

#### Make (Simple, for Makefile)

**Makefile is already included in the repository**: `cpp/Makefile`

**Usage**:
```bash
cd cpp
make
```

#### CMake (Recommended, for larger projects)

**CMakeLists.txt is already included in the repository**: `cpp/CMakeLists.txt`

**Usage**:
```bash
cd cpp
mkdir build
cd build
cmake ..
make  # Linux/macOS
# Or: cmake --build . --config Release  # Windows
```

---

### 📚 JSON Library (Optional)

#### jsoncpp (Recommended for production)

The basic implementation uses a simplified JSON parser. For better functionality, `jsoncpp` can be used.

##### Linux

```bash
# Debian/Ubuntu
sudo apt install libjsoncpp-dev

# Arch/CachyOS
sudo pacman -S jsoncpp

# Fedora
sudo dnf install jsoncpp-devel
```

##### macOS

```bash
brew install jsoncpp
```

##### Windows

**vcpkg** (Recommended):
```powershell
# Install vcpkg
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat

# Install jsoncpp
.\vcpkg install jsoncpp:x64-windows
```

**Link**: [vcpkg](https://github.com/microsoft/vcpkg)

**Compilation with jsoncpp**:
```bash
# Linux/macOS
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp

# Windows (vcpkg)
# See vcpkg documentation for include paths
```

---

### 📦 External Dependencies

#### 1. KeePassXC-CLI (REQUIRED)

**Purpose**: For merging KeePass databases

##### Linux

```bash
sudo apt install keepassxc  # Debian/Ubuntu
sudo pacman -S keepassxc    # Arch/CachyOS
sudo dnf install keepassxc  # Fedora
```

**Links**:
- **KeePassXC**: [https://keepassxc.org/](https://keepassxc.org/)

##### macOS

```bash
brew install keepassxc
```

##### Windows

1. Download: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Install KeePassXC
3. Ensure `keepassxc-cli.exe` is in PATH

#### 2. lftp (For FTP/SFTP - RECOMMENDED)

**Purpose**: File transfers via FTP and SFTP

##### Linux

```bash
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS
sudo dnf install lftp  # Fedora
```

**Links**:
- **lftp**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### macOS

```bash
brew install lftp
```

##### Windows

**Via WSL or Git Bash**:
```bash
# In WSL
sudo apt install lftp
```

#### 3. smbclient (For SMB/CIFS - Optional)

**Purpose**: Access to Windows network shares

##### Linux

```bash
sudo apt install smbclient  # Debian/Ubuntu
sudo pacman -S samba       # Arch/CachyOS
```

**Links**:
- **Samba**: [https://www.samba.org/](https://www.samba.org/)

##### macOS

```bash
brew install samba
```

##### Windows

Windows has native SMB support.

---

### 🔨 Compilation

#### Method 1: With Makefile (Simple)

```bash
cd cpp

# Compile
make

# Verify
./keepass-sync --version
```

#### Method 2: With CMake (Recommended)

```bash
cd cpp
mkdir build
cd build

# Configure
cmake ..

# Compile
make  # Linux/macOS
# Or: cmake --build . --config Release  # Windows

# Verify
./keepass-sync --version
```

#### Method 3: Manual

```bash
cd cpp

# Linux/macOS
g++ -std=c++11 -Wall -O2 -o keepass-sync sync.cpp

# Windows (MinGW)
g++ -std=c++11 -Wall -O2 -o keepass-sync.exe sync.cpp
```

#### Cross-Platform Compilation

**For Windows (from Linux/macOS)**:
```bash
# Install MinGW cross-compiler
sudo apt install mingw-w64  # Debian/Ubuntu

# Compile
x86_64-w64-mingw32-g++ -std=c++11 -o keepass-sync.exe sync.cpp
```

---

### ⚙️ Configuration

The C++ variant uses the same `config.json` as the Python variant.

**IMPORTANT**: The simplified JSON parser does not support all JSON features. For complex configurations, use `jsoncpp`.

**Example config.json**:

```json
{
  "ftp": {
    "host": "your-server.com",
    "user": "your-username",
    "password": "your-password",
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
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

---

### 💻 Usage

```bash
# Normal synchronization
./keepass-sync

# Test connection
./keepass-sync --test

# Show status
./keepass-sync --status

# Version
./keepass-sync --version

# Help
./keepass-sync --help
```

#### Automation

##### Cron (Linux/macOS)

```bash
# Open crontab
crontab -e

# Add (every hour)
0 * * * * cd /path/to/project/cpp && ./keepass-sync
```

##### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Schedule
4. Action: Start program
   - Program: `C:\Path\to\keepass-sync.exe`
   - Start in: `C:\Path\to\cpp`

---

### 🔍 Troubleshooting

#### Compilation errors

**Problem**: C++11 not supported

**Solution**:
```bash
# Check compiler version
gcc --version  # Should be 4.8.1+

# Update compiler if necessary
```

#### "jsoncpp not found"

**Problem**: jsoncpp not installed (optional)

**Solution**: The basic variant works WITHOUT jsoncpp, uses simplified parser.

#### "lftp not found"

**Problem**: lftp is not installed

**Solution**: See installation above

#### Linker errors

**Problem**: Libraries not found

**Solution**:
```bash
# With jsoncpp (if used)
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp

# Check library paths
pkg-config --libs jsoncpp  # Linux
```

---

### 🙏 Acknowledgments

#### C++ Standard

- **Developer**: ISO C++ Committee
- **Website**: [https://isocpp.org/](https://isocpp.org/)
- **Standard**: C++11 / C++14 / C++17

#### GCC

- **Developer**: GNU Project
- **Website**: [https://gcc.gnu.org/](https://gcc.gnu.org/)
- **License**: GPL

#### Clang

- **Developer**: LLVM Project
- **Website**: [https://clang.llvm.org/](https://clang.llvm.org/)
- **License**: Apache 2.0

#### Visual Studio

- **Developer**: Microsoft
- **Website**: [https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/)

#### CMake

- **Developer**: Kitware
- **Website**: [https://cmake.org/](https://cmake.org/)
- **License**: BSD 3-Clause

#### jsoncpp (Optional)

- **Developer**: jsoncpp Contributors
- **Website**: [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp)
- **License**: Public Domain / MIT

---

## 🇪🇸 Español

### ⚠️ NOTA: Implementación Básica

La variante C/C++ es una **implementación básica** con un analizador JSON simplificado. Para uso en producción, se debe usar `jsoncpp` u otra biblioteca JSON.

### 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación del Compilador C++](#instalación-del-compilador-c)
3. [Sistemas de Compilación](#sistemas-de-compilación)
4. [Biblioteca JSON (Opcional)](#biblioteca-json-opcional)
5. [Dependencias Externas](#dependencias-externas)
6. [Compilación](#compilación)
7. [Configuración](#configuración)
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
| **macOS** | macOS 10.13+ | macOS 11+ | x86_64, ARM64 (Apple Silicon) |

#### Software Requerido

1. **Compilador C++**
   - **Versión Mínima**: Compatible con C++11
   - **GCC**: 4.8.1+ (Linux/macOS)
   - **Clang**: 3.3+ (Linux/macOS)
   - **MSVC**: Visual Studio 2015+ (Windows)

2. **Sistema de Compilación** (Opcional, pero recomendado)
   - **Make**: Para Makefile
   - **CMake**: 3.10+ (para CMakeLists.txt)

3. **KeePassXC-CLI**
   - **Versión Mínima**: 2.6.0+
   - **Versión Recomendada**: 2.7.0+ (última versión)

4. **Herramientas Externas** (según el protocolo):
   - **lftp**: Para transferencias FTP/SFTP
   - **smbclient**: Para recursos compartidos de red SMB/CIFS
   - **sshpass** & **scp**: Para transferencias SCP

---

### 🔨 Instalación del Compilador C++

#### Linux

##### Arch Linux / CachyOS

```bash
# Instalar GCC y Make
sudo pacman -S gcc make cmake

# Verificar
gcc --version
# Debería mostrar: gcc 11.x.x o superior

make --version
cmake --version
```

**Nombres de paquetes**: 
- `gcc` - Compilador GCC
- `make` - Herramienta Make Build
- `cmake` - Sistema de Compilación CMake

**Enlace**: [Paquete Arch Linux GCC](https://archlinux.org/packages/core/x86_64/gcc/)

##### Debian / Ubuntu

```bash
# Instalar build essentials
sudo apt update
sudo apt install build-essential cmake

# Verificar
gcc --version
make --version
cmake --version
```

**Nombres de paquetes**:
- `build-essential` - Contiene gcc, g++, make, etc.
- `cmake` - Sistema de Compilación CMake

**Enlace**: [Debian Build-Essential](https://packages.debian.org/build-essential)

##### Fedora / RHEL / CentOS

```bash
sudo dnf install gcc gcc-c++ make cmake
```

##### openSUSE

```bash
sudo zypper install gcc gcc-c++ make cmake
```

#### macOS

##### Xcode Command Line Tools (Recomendado)

```bash
# Instalar Command Line Tools
xcode-select --install

# Verificar
gcc --version
# O:
clang --version
```

**Enlace**: [Xcode Command Line Tools](https://developer.apple.com/xcode/)

##### Homebrew (Alternativa)

```bash
# Instalar GCC
brew install gcc

# Instalar CMake
brew install cmake

# Verificar
gcc-11 --version  # La versión puede variar
cmake --version
```

**Enlace**: [Homebrew GCC Formula](https://formulae.brew.sh/formula/gcc)

#### Windows

##### Visual Studio (Recomendado)

1. **Descarga**: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
2. **Elige**: Visual Studio Community (gratis)
3. **Durante la instalación**: Elige la carga de trabajo "Desktop development with C++"
4. **Verifica**: Abre "Developer Command Prompt for VS"
```powershell
cl
# Debería mostrar la versión del compilador
```

**Enlace**: [Descargas Visual Studio](https://visualstudio.microsoft.com/downloads/)

##### MinGW-w64 (Alternativa)

1. **Descarga**: [https://www.mingw-w64.org/downloads/](https://www.mingw-w64.org/downloads/)
2. **O**: Instala MSYS2 (contiene MinGW-w64)
3. **MSYS2**: [https://www.msys2.org/](https://www.msys2.org/)

**Instalación vía MSYS2**:
```bash
# En Terminal MSYS2
pacman -S mingw-w64-x86_64-gcc
pacman -S mingw-w64-x86_64-make
pacman -S mingw-w64-x86_64-cmake

# Añade a PATH: C:\msys64\mingw64\bin
```

**Enlace**: [MinGW-w64](https://www.mingw-w64.org/)
**Enlace**: [MSYS2](https://www.msys2.org/)

##### Chocolatey (Alternativa)

```powershell
# Instalar MinGW o Visual Studio Build Tools
choco install mingw

# O Visual Studio Build Tools
choco install visualstudio2019buildtools
```

---

### 📦 Sistemas de Compilación

#### Make (Simple, para Makefile)

**Makefile ya está incluido en el repositorio**: `cpp/Makefile`

**Uso**:
```bash
cd cpp
make
```

#### CMake (Recomendado, para proyectos más grandes)

**CMakeLists.txt ya está incluido en el repositorio**: `cpp/CMakeLists.txt`

**Uso**:
```bash
cd cpp
mkdir build
cd build
cmake ..
make  # Linux/macOS
# O: cmake --build . --config Release  # Windows
```

---

### 📚 Biblioteca JSON (Opcional)

#### jsoncpp (Recomendado para producción)

La implementación básica usa un analizador JSON simplificado. Para mejor funcionalidad, se puede usar `jsoncpp`.

##### Linux

```bash
# Debian/Ubuntu
sudo apt install libjsoncpp-dev

# Arch/CachyOS
sudo pacman -S jsoncpp

# Fedora
sudo dnf install jsoncpp-devel
```

##### macOS

```bash
brew install jsoncpp
```

##### Windows

**vcpkg** (Recomendado):
```powershell
# Instalar vcpkg
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat

# Instalar jsoncpp
.\vcpkg install jsoncpp:x64-windows
```

**Enlace**: [vcpkg](https://github.com/microsoft/vcpkg)

**Compilación con jsoncpp**:
```bash
# Linux/macOS
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp

# Windows (vcpkg)
# Ver documentación de vcpkg para rutas de inclusión
```

---

### 📦 Dependencias Externas

#### 1. KeePassXC-CLI (REQUERIDO)

**Propósito**: Para fusionar bases de datos KeePass

##### Linux

```bash
sudo apt install keepassxc  # Debian/Ubuntu
sudo pacman -S keepassxc    # Arch/CachyOS
sudo dnf install keepassxc  # Fedora
```

**Enlaces**:
- **KeePassXC**: [https://keepassxc.org/](https://keepassxc.org/)

##### macOS

```bash
brew install keepassxc
```

##### Windows

1. Descarga: [https://keepassxc.org/download/](https://keepassxc.org/download/)
2. Instala KeePassXC
3. Asegúrate de que `keepassxc-cli.exe` esté en PATH

#### 2. lftp (Para FTP/SFTP - RECOMENDADO)

**Propósito**: Transferencias de archivos vía FTP y SFTP

##### Linux

```bash
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS
sudo dnf install lftp  # Fedora
```

**Enlaces**:
- **lftp**: [https://lftp.yar.ru/](https://lftp.yar.ru/)

##### macOS

```bash
brew install lftp
```

##### Windows

**Vía WSL o Git Bash**:
```bash
# En WSL
sudo apt install lftp
```

#### 3. smbclient (Para SMB/CIFS - Opcional)

**Propósito**: Acceso a recursos compartidos de red Windows

##### Linux

```bash
sudo apt install smbclient  # Debian/Ubuntu
sudo pacman -S samba       # Arch/CachyOS
```

**Enlaces**:
- **Samba**: [https://www.samba.org/](https://www.samba.org/)

##### macOS

```bash
brew install samba
```

##### Windows

Windows tiene soporte SMB nativo.

---

### 🔨 Compilación

#### Método 1: Con Makefile (Simple)

```bash
cd cpp

# Compilar
make

# Verificar
./keepass-sync --version
```

#### Método 2: Con CMake (Recomendado)

```bash
cd cpp
mkdir build
cd build

# Configurar
cmake ..

# Compilar
make  # Linux/macOS
# O: cmake --build . --config Release  # Windows

# Verificar
./keepass-sync --version
```

#### Método 3: Manual

```bash
cd cpp

# Linux/macOS
g++ -std=c++11 -Wall -O2 -o keepass-sync sync.cpp

# Windows (MinGW)
g++ -std=c++11 -Wall -O2 -o keepass-sync.exe sync.cpp
```

#### Compilación Multiplataforma

**Para Windows (desde Linux/macOS)**:
```bash
# Instalar compilador cruzado MinGW
sudo apt install mingw-w64  # Debian/Ubuntu

# Compilar
x86_64-w64-mingw32-g++ -std=c++11 -o keepass-sync.exe sync.cpp
```

---

### ⚙️ Configuración

La variante C++ utiliza el mismo `config.json` que la variante Python.

**IMPORTANTE**: El analizador JSON simplificado no admite todas las características JSON. Para configuraciones complejas, usa `jsoncpp`.

**Ejemplo config.json**:

```json
{
  "ftp": {
    "host": "tu-servidor.com",
    "user": "tu-usuario",
    "password": "tu-contraseña",
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
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

---

### 💻 Uso

```bash
# Sincronización normal
./keepass-sync

# Probar conexión
./keepass-sync --test

# Mostrar estado
./keepass-sync --status

# Versión
./keepass-sync --version

# Ayuda
./keepass-sync --help
```

#### Automatización

##### Cron (Linux/macOS)

```bash
# Abrir crontab
crontab -e

# Añadir (cada hora)
0 * * * * cd /ruta/a/proyecto/cpp && ./keepass-sync
```

##### Programador de Tareas (Windows)

1. Abrir Programador de Tareas
2. Crear nueva tarea
3. Desencadenador: Programación
4. Acción: Iniciar programa
   - Programa: `C:\Ruta\a\keepass-sync.exe`
   - Iniciar en: `C:\Ruta\a\cpp`

---

### 🔍 Solución de Problemas

#### Errores de compilación

**Problema**: C++11 no soportado

**Solución**:
```bash
# Verificar versión del compilador
gcc --version  # Debería ser 4.8.1+

# Actualizar compilador si es necesario
```

#### "jsoncpp no encontrado"

**Problema**: jsoncpp no está instalado (opcional)

**Solución**: La variante básica funciona SIN jsoncpp, usa analizador simplificado.

#### "lftp not found"

**Problema**: lftp no está instalado

**Solución**: Ver instalación arriba

#### Errores del enlazador

**Problema**: Bibliotecas no encontradas

**Solución**:
```bash
# Con jsoncpp (si se usa)
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp

# Verificar rutas de bibliotecas
pkg-config --libs jsoncpp  # Linux
```

---

### 🙏 Agradecimientos

#### Estándar C++

- **Desarrollador**: Comité ISO C++
- **Sitio Web**: [https://isocpp.org/](https://isocpp.org/)
- **Estándar**: C++11 / C++14 / C++17

#### GCC

- **Desarrollador**: Proyecto GNU
- **Sitio Web**: [https://gcc.gnu.org/](https://gcc.gnu.org/)
- **Licencia**: GPL

#### Clang

- **Desarrollador**: Proyecto LLVM
- **Sitio Web**: [https://clang.llvm.org/](https://clang.llvm.org/)
- **Licencia**: Apache 2.0

#### Visual Studio

- **Desarrollador**: Microsoft
- **Sitio Web**: [https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/)

#### CMake

- **Desarrollador**: Kitware
- **Sitio Web**: [https://cmake.org/](https://cmake.org/)
- **Licencia**: BSD 3-Clause

#### jsoncpp (Opcional)

- **Desarrollador**: Colaboradores jsoncpp
- **Sitio Web**: [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp)
- **Licencia**: Dominio Público / MIT

---

<div align="center">

**⚙️ C/C++-Variante: Schnellster Code, minimaler Memory-Footprint**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>
