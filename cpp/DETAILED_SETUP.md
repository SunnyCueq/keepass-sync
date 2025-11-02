# 📖 Detaillierte Installations- und Setup-Anleitung - C/C++ Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![C++](https://img.shields.io/badge/C%2B%2B-11+-00599C.svg?logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Native Performance - Vollständige Anleitung für Anfänger - Schritt für Schritt**

</div>

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

<div align="center">

**⚙️ C/C++-Variante: Schnellster Code, minimaler Memory-Footprint**

**Version**: 1.1.0 | **Letzte Aktualisierung**: 2025

</div>

