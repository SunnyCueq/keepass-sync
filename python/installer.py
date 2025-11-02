#!/usr/bin/env python3
"""
KeePass Sync - Interaktiver Cross-Platform Installer
Erkennt System, Sprache, Protokoll und erstellt config.json
"""

import os
import sys
import platform
import json
import getpass

def clear_screen():
    """Bildschirm löschen (Cross-Platform)"""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_header():
    """Header anzeigen"""
    print("=" * 60)
    print("🔐 KeePass Sync - Interaktiver Installer")
    print("=" * 60)
    print()

def detect_system():
    """System-Spezifikationen erkennen und anzeigen"""
    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    
    print("📊 System-Informationen:")
    print(f"  Betriebssystem: {system} {release}")
    print(f"  Version: {version}")
    print(f"  Architektur: {machine}")
    if processor:
        print(f"  Prozessor: {processor}")
    print()
    
    return system

def detect_language():
    """System-Sprache erkennen"""
    lang_map = {
        'de': 'Deutsch',
        'en': 'English',
        'es': 'Español',
        'fr': 'Français',
        'it': 'Italiano'
    }
    
    # System-Sprache erkennen
    system_lang = os.environ.get('LANG', '').split('_')[0] or os.environ.get('LC_ALL', '').split('_')[0] or 'en'
    if system_lang not in ['de', 'en', 'es']:
        system_lang = 'en'
    
    default_name = lang_map.get(system_lang, 'English')
    
    print(f"🌍 Erkannte Sprache: {default_name} ({system_lang})")
    print()
    
    return system_lang

def select_language():
    """Sprache auswählen"""
    print("Sprache wählen / Select language / Seleccionar idioma:")
    print("  1. Deutsch")
    print("  2. English")
    print("  3. Español")
    
    while True:
        choice = input("Auswahl / Choice / Elección [1-3] (Enter für erkannte Sprache): ").strip()
        
        if not choice:
            return detect_language()
        
        lang_map = {'1': 'de', '2': 'en', '3': 'es'}
        if choice in lang_map:
            return lang_map[choice]
        
        print("❌ Ungültige Auswahl. Bitte 1, 2 oder 3 eingeben.")

def select_protocol():
    """Protokoll auswählen"""
    print("\n📡 Protokoll wählen / Select protocol / Seleccionar protocolo:")
    print("  1. FTP (Standard)")
    print("  2. SFTP (SSH File Transfer - Verschlüsselt)")
    print("  3. SMB/CIFS (Windows-Netzwerk-Freigaben)")
    print("  4. SCP (Secure Copy - SSH-basiert)")
    
    while True:
        choice = input("Auswahl / Choice / Elección [1-4] (Enter = FTP): ").strip()
        
        if not choice:
            return 'ftp'
        
        protocol_map = {'1': 'ftp', '2': 'sftp', '3': 'smb', '4': 'scp'}
        if choice in protocol_map:
            return protocol_map[choice]
        
        print("❌ Ungültige Auswahl. Bitte 1, 2, 3 oder 4 eingeben.")

def get_protocol_config(protocol, language='en'):
    """Protokoll-spezifische Konfiguration abfragen"""
    config = {}
    
    if protocol in ['ftp', 'sftp']:
        print(f"\n📡 {protocol.upper()} Konfiguration:")
        config['host'] = input("Server-Adresse / Server address / Dirección del servidor: ").strip()
        config['user'] = input("Benutzername / Username / Nombre de usuario: ").strip()
        config['password'] = getpass.getpass("Passwort / Password / Contraseña: ")
        config['type'] = protocol
        
        if protocol == 'sftp':
            port = input("Port (Enter für 22 / Enter for 22 / Enter para 22): ").strip()
            config['port'] = int(port) if port.isdigit() else 22
        else:
            port = input("Port (Enter für 21 / Enter for 21 / Enter para 21): ").strip()
            config['port'] = int(port) if port.isdigit() else 21
        
        config['remotePath'] = input("Remote-Pfad / Remote path / Ruta remota (z.B. /keepass_passwords.kdbx): ").strip()
        if not config['remotePath']:
            config['remotePath'] = "/keepass_passwords.kdbx"
    
    elif protocol == 'smb':
        print("\n📡 SMB/CIFS Konfiguration:")
        config['host'] = input("Server-Adresse / Server address / Dirección del servidor: ").strip()
        config['share'] = input("Freigabe-Name / Share name / Nombre del recurso compartido: ").strip()
        config['user'] = input("Benutzername / Username / Nombre de usuario: ").strip()
        config['password'] = getpass.getpass("Passwort / Password / Contraseña: ")
        domain = input("Domain/Workgroup (Enter = WORKGROUP): ").strip()
        config['domain'] = domain if domain else "WORKGROUP"
        config['type'] = 'smb'
        config['remotePath'] = input("Remote-Pfad / Remote path / Ruta remota (z.B. keepass_passwords.kdbx): ").strip()
        if not config['remotePath']:
            config['remotePath'] = "keepass_passwords.kdbx"
    
    elif protocol == 'scp':
        print("\n📡 SCP Konfiguration:")
        config['host'] = input("Server-Adresse / Server address / Dirección del servidor: ").strip()
        config['user'] = input("Benutzername / Username / Nombre de usuario: ").strip()
        config['password'] = getpass.getpass("Passwort / Password / Contraseña: ")
        port = input("Port (Enter für 22 / Enter for 22 / Enter para 22): ").strip()
        config['port'] = int(port) if port.isdigit() else 22
        config['type'] = 'scp'
        config['remotePath'] = input("Remote-Pfad / Remote path / Ruta remota (z.B. /home/user/keepass_passwords.kdbx): ").strip()
        if not config['remotePath']:
            config['remotePath'] = "/keepass_passwords.kdbx"
    
    return config

def get_keeppass_config():
    """KeePass-Konfiguration abfragen"""
    print("\n🔐 KeePass Konfiguration:")
    password = getpass.getpass("KeePass Master-Passwort / Master password / Contraseña maestra: ")
    
    print("\nKeePassXC-CLI Pfad (Enter für Standard / Enter for default):")
    keepassxc_path = input("Pfad / Path / Ruta: ").strip()
    if not keepassxc_path:
        keepassxc_path = "keepassxc-cli"
    
    return {
        'databasePassword': password,
        'keepassXCPath': keepassxc_path
    }

def create_config_file(config_data):
    """config.json erstellen"""
    config_file = "config.json"
    
    if os.path.exists(config_file):
        overwrite = input(f"\n⚠️  {config_file} existiert bereits. Überschreiben? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("❌ Abgebrochen.")
            return False
    
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)
        
        # Dateirechte setzen (Linux/macOS)
        if platform.system() != 'Windows':
            os.chmod(config_file, 0o600)  # Nur für Besitzer lesbar/schreibbar
        
        print(f"\n✅ {config_file} erfolgreich erstellt!")
        return True
    except Exception as e:
        print(f"\n❌ Fehler beim Erstellen von {config_file}: {e}")
        return False

def main():
    """Hauptfunktion"""
    clear_screen()
    print_header()
    
    # System erkennen
    system = detect_system()
    
    # Sprache
    default_lang = detect_language()
    language = select_language()
    
    # Protokoll wählen
    protocol = select_protocol()
    
    # Protokoll-Konfiguration
    if protocol == 'ftp':
        ftp_config = get_protocol_config('ftp', language)
    elif protocol == 'sftp':
        ftp_config = get_protocol_config('sftp', language)
    elif protocol == 'smb':
        ftp_config = get_protocol_config('smb', language)
    elif protocol == 'scp':
        ftp_config = get_protocol_config('scp', language)
    
    # KeePass-Konfiguration
    keepass_config = get_keeppass_config()
    
    # Config-Struktur aufbauen
    config_data = {
        'ftp': ftp_config,
        'local': {
            'localPath': 'keepass_passwords.kdbx',
            'tempPath': 'temp_keepass_passwords.kdbx',
            'backupDir': 'backups',
            'maxBackups': 2
        },
        'keepass': keepass_config,
        'settings': {
            'debug': False,
            'language': language,
            'cleanupLogs': True,
            'maxLogAgeDays': 7
        }
    }
    
    # Config erstellen
    if create_config_file(config_data):
        print("\n🎉 Installation abgeschlossen!")
        print("\nNächste Schritte:")
        print("  1. Testen: python3 sync.py")
        print("  2. Automatische Installation: ./linux/install.sh (Linux)")
        print("  3. Siehe README.md für weitere Informationen")
    else:
        print("\n❌ Installation fehlgeschlagen.")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Installation abgebrochen.")
        sys.exit(1)

