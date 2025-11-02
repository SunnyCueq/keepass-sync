# ⚙️ KeePass Sync - C/C++ Variante

<div align="center">

**🌍 Languages: [🇩🇪 Deutsch](#-deutsch) | [🇬🇧 English](#-english) | [🇪🇸 Español](#-español)**

[![C++](https://img.shields.io/badge/C%2B%2B-11+-00599C.svg)](https://isocpp.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)

> **Schnellster Code, minimaler Memory-Footprint, native Performance**

</div>

---

## 🇩🇪 Deutsch

### ⚠️ HINWEIS: Basis-Implementierung

Die C/C++-Variante ist eine **Basis-Implementierung** mit vereinfachtem JSON-Parser. Für Produktionsnutzung sollte `jsoncpp` oder eine andere JSON-Library verwendet werden.

### Vorteile der C/C++-Variante

✅ **Performance**: Schnellster Code (native Compilation)  
✅ **Memory**: Minimaler Memory-Footprint  
✅ **Keine Runtime**: Kompiliert zu nativen Binaries  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry-Logic**: Exponential Backoff  
✅ **Protokolle**: FTP, SFTP (SMB/SCP über externe Tools)

### Installation

#### 1. Compiler installieren

**Linux:**
```bash
sudo apt install build-essential g++  # Debian/Ubuntu
sudo pacman -S gcc gcc-libs            # Arch/CachyOS
```

**macOS:**
```bash
# Xcode Command Line Tools
xcode-select --install

# Oder mit Homebrew
brew install gcc
```

**Windows:**
- MinGW-w64: https://www.mingw-w64.org/
- MSYS2: https://www.msys2.org/
- Visual Studio: https://visualstudio.microsoft.com/

#### 2. Kompilieren

**Mit Make:**
```bash
cd cpp
make
```

**Mit CMake:**
```bash
cd cpp
mkdir build && cd build
cmake ..
make  # Linux/macOS
# Oder: cmake --build . --config Release  # Windows
```

**Manuell:**
```bash
g++ -std=c++11 -Wall -O2 -o keepass-sync sync.cpp
```

#### 3. Installation (optional)

```bash
# Linux/macOS
sudo cp keepass-sync /usr/local/bin/

# Windows
# Kopiere keepass-sync.exe nach C:\Program Files\KeePass Sync\
```

### Verwendung

```bash
# Normale Synchronisation
./keepass-sync

# Verbindung testen
./keepass-sync --test

# Status anzeigen
./keepass-sync --status

# Alternative Config
./keepass-sync --config /pfad/zu/config.json

# Version
./keepass-sync --version

# Hilfe
./keepass-sync --help
```

### Konfiguration

Die C++-Variante nutzt die gleiche `config.json` wie die Python-Variante.

**WICHTIG:** Der integrierte JSON-Parser ist vereinfacht. Für komplexe JSON-Strukturen sollte `jsoncpp` verwendet werden.

### Voraussetzungen

- **C++11 Compiler**: g++, clang++, oder MSVC
- **KeePassXC-CLI**: Muss im PATH verfügbar sein
- **lftp**: Für FTP/SFTP (Linux/macOS)
- **smbclient**: Für SMB (Linux/macOS, über externe Calls)
- **sshpass** & **scp**: Für SCP (Linux/macOS, über externe Calls)

### Erweiterte Kompilierung (mit jsoncpp)

Für besseres JSON-Parsing:

```bash
# Linux
sudo apt install libjsoncpp-dev  # Debian/Ubuntu
sudo pacman -S jsoncpp            # Arch/CachyOS

# Kompilieren mit jsoncpp
g++ -std=c++11 -o keepass-sync sync.cpp -ljsoncpp
```

### Unterschiede zur Python-Variante

- ❌ **Datei-Überwachung (`--watch`)**: Nicht implementiert
- ⚠️ **JSON-Parser**: Vereinfacht (nutze jsoncpp für Produktion)
- ✅ **Performance**: Sehr schnell (native Code)
- ✅ **Memory**: Minimaler Footprint

### Fehlerbehebung

**"jsoncpp not found"**
- Die Basis-Variante funktioniert auch OHNE jsoncpp
- Für besseres Parsing: Installiere `libjsoncpp-dev` (Linux)

**"lftp not found"**
```bash
sudo apt install lftp  # Debian/Ubuntu
sudo pacman -S lftp    # Arch/CachyOS
```

**Kompilierungsfehler**
```bash
# Stelle sicher, dass C++11 unterstützt wird
g++ --version  # Sollte g++ 4.8.1+ zeigen

# Für Windows: Nutze MinGW-w64 oder Visual Studio
```

### Vorteile für Performance-Critical Anwendungen

✅ **Sehr schnell**: Native Compilation  
✅ **Wenig Memory**: Minimaler Footprint  
✅ **Keine Runtime**: Keine Interpreter-Abhängigkeiten

### Nachteile

❌ **Komplexer**: Mehr Code, schwierigere Entwicklung  
❌ **Plattform-spezifisch**: Unterschiedliche Compiler für verschiedene Plattformen  
❌ **Wartung**: Schwerer zu debuggen als Python/Node.js

---

## 🇬🇧 English

### ⚠️ NOTE: Basic Implementation

The C/C++ variant is a **basic implementation** with a simplified JSON parser. For production use, `jsoncpp` or another JSON library should be used.

### Advantages of C/C++ Variant

✅ **Performance**: Fastest code (native compilation)  
✅ **Memory**: Minimal memory footprint  
✅ **No Runtime**: Compiled to native binaries  
✅ **CLI Arguments**: `--test`, `--status`, etc.  
✅ **Retry Logic**: Exponential backoff  
✅ **Protocols**: FTP, SFTP (SMB/SCP via external tools)

### Installation

#### 1. Install Compiler

**Linux:**
```bash
sudo apt install build-essential g++
```

**macOS:**
```bash
xcode-select --install
```

**Windows:**
- MinGW-w64 or MSYS2
- Visual Studio

#### 2. Compile

**With Make:**
```bash
cd cpp
make
```

**With CMake:**
```bash
cd cpp
mkdir build && cd build
cmake ..
make
```

### Usage

```bash
# Normal synchronization
./keepass-sync

# Test connection
./keepass-sync --test

# Show status
./keepass-sync --status
```

### Requirements

- **C++11 Compiler**: g++, clang++, or MSVC
- **KeePassXC-CLI**: Must be available in PATH
- **lftp**: For FTP/SFTP (Linux/macOS)

---

## 🇪🇸 Español

### ⚠️ NOTA: Implementación Básica

La variante C/C++ es una **implementación básica** con un analizador JSON simplificado. Para uso en producción, se debe usar `jsoncpp` u otra biblioteca JSON.

### Ventajas de la Variante C/C++

✅ **Rendimiento**: Código más rápido (compilación nativa)  
✅ **Memoria**: Huella de memoria mínima  
✅ **Sin Runtime**: Compilado a binarios nativos  
✅ **Argumentos CLI**: `--test`, `--status`, etc.  
✅ **Lógica de Reintento**: Retroceso exponencial  
✅ **Protocolos**: FTP, SFTP (SMB/SCP vía herramientas externas)

### Instalación

#### 1. Instalar Compilador

```bash
sudo apt install build-essential g++
```

#### 2. Compilar

```bash
cd cpp
make
```

---

<div align="center">

**⚙️ C/C++-Variante: Schnellster Code, minimaler Memory-Footprint**

</div>

