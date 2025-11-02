# 🔐 KeePass Sync - Sincroniza tus Contraseñas Automáticamente

<div align="center">

**🌍 Idiomas: [🇩🇪 Deutsch](README.de.md) | [🇬🇧 English](README.en.md) | [🇪🇸 Español](README.es.md)**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](.)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](.)

> **Sincroniza automáticamente tu base de datos KeePass entre múltiples computadoras a través de un servidor FTP.**

[🚀 Inicio Rápido](#-inicio-rápido) • [📖 Documentación](#-documentación) • [🛠️ Instalación](#️-instalación) • [❓ FAQ](#-preguntas-frecuentes) • [🤝 Contribuir](#-contribuir)

</div>

---

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

El script soporta **12 idiomas**: Alemán (de), Inglés (en), Español (es), Francés (fr), Italiano (it), Portugués (pt), Neerlandés (nl), Polaco (pl), Ruso (ru), Chino (zh), Japonés (ja), Coreano (ko).

El idioma se detecta automáticamente o se puede configurar en `config.json`:
```json
{
  "settings": {
    "language": "es"
  }
}
```

### 🎯 Opciones CLI y Características

El script ofrece varias opciones para diferentes casos de uso:

**Probar conexión (sin sincronización):**
```bash
python3 python/sync_ftp.py --test
```
- ✅ Verifica disponibilidad de KeePassXC-CLI
- ✅ Verifica base de datos local
- ✅ Prueba conexión al servidor
- ✅ No se necesita respaldo, no hay cambios de datos

**Mostrar estado:**
```bash
python3 python/sync_ftp.py --status
```
Muestra:
- Información de la BD local (tamaño, antigüedad)
- Resumen de respaldos
- Detalles de configuración

**Vigilar archivo automáticamente:**
```bash
python3 python/sync_ftp.py --watch
```
- Inicia automáticamente la sincronización cuando cambia la base de datos local
- Retraso configurable (por defecto: 30 segundos)
- Se ejecuta continuamente en segundo plano

**Sincronización normal:**
```bash
python3 python/sync_ftp.py        # Sincronización estándar
python3 python/sync_ftp.py --sync # Sincronización explícita
python3 python/sync_ftp.py -v     # Verboso (salida de depuración)
python3 python/sync_ftp.py -q     # Silencioso (solo errores)
```

**Más opciones:**
```bash
python3 python/sync_ftp.py --config alt_config.json  # Config alternativo
python3 python/sync_ftp.py --help                     # Mostrar ayuda
python3 python/sync_ftp.py --version                  # Mostrar versión
```

### 🔄 Lógica de Reintento Mejorada

El script reintenta automáticamente las operaciones fallidas:
- **Exponential Backoff**: 5s → 10s → 20s → máx 60s
- **Configurable** en `config.json`:
```json
{
  "settings": {
    "max_retries": 3,
    "retry_delay": 5
  }
}
```
- Resistente a errores temporales de red

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
- `fr` - Français | French | Francés ✅
- `it` - Italiano | Italian | Italiano ✅
- `pt` - Português | Portuguese | Portugués ✅
- `nl` - Nederlands | Dutch | Neerlandés ✅
- `pl` - Polski | Polish | Polaco ✅
- `ru` - Русский | Russian | Ruso ✅
- `zh` - 中文 | Chinese | Chino ✅
- `ja` - 日本語 | Japanese | Japonés ✅
- `ko` - 한국어 | Korean | Coreano ✅

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
