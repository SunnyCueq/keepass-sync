#!/usr/bin/env python3
"""
KeePass Sync Script - Cross-Platform Version
Unterstützt: Linux, Windows, macOS
"""

import os
import sys
import platform
import subprocess
import shutil
import json
import glob
from datetime import datetime, timedelta
from pathlib import Path

# Konfiguration
CONFIG_FILE = "config.json"
LOG_FILE = "sync_log.txt"
FTP_LOG = "ftp_log.txt"
LANG_DIR = "lang"

# Sprachdateien laden (vor write_log verfügbar machen)
messages = {}

def load_language(lang='de'):
    """Lade Sprachdatei im JSON-Format"""
    global messages
    supported_languages = ['de', 'en', 'es']  # Unterstützte Sprachen
    
    # Validiere Sprachcode
    if lang not in supported_languages:
        lang = 'de'  # Fallback auf Deutsch
    
    lang_file = os.path.join(LANG_DIR, f"{lang}.json")
    
    if os.path.exists(lang_file):
        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                messages = json.load(f)
            return messages
        except Exception as e:
            # Fallback wenn messages noch nicht geladen
            error_msg = "Warning: Language file could not be loaded" if lang == 'en' else "Warnung: Sprachdatei konnte nicht geladen werden"
            print(f"{error_msg}: {e}")
    
    # Fallback: Englisch, dann Deutsch
    if lang != 'en':
        return load_language('en')
    if lang != 'de':
        return load_language('de')
    
    return {}

def write_log(message, log_file=LOG_FILE):
    """Schreibe Nachricht ins Log mit Timestamp"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"{timestamp} {message}"
    print(log_message)
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    except Exception:
        pass  # Falls Log nicht geschrieben werden kann

def cleanup_old_backups(backup_dir, max_backups=2):
    """Lösche alte Backups, behalte nur die neuesten"""
    try:
        backup_files = sorted(
            glob.glob(os.path.join(backup_dir, "keepass_passwords_*.kdbx")),
            key=os.path.getmtime,
            reverse=True
        )
        
        if len(backup_files) > max_backups:
            for old_backup in backup_files[max_backups:]:
                try:
                    os.remove(old_backup)
                    write_log(f"{messages.get('MSG_BACKUP_DELETED', 'Old backup deleted')}: {os.path.basename(old_backup)}")
                except Exception as e:
                    write_log(f"{messages.get('MSG_BACKUP_DELETE_FAIL', 'Could not delete backup')}: {e}")
    except Exception as e:
        write_log(f"{messages.get('MSG_CLEANUP_BACKUPS_ERROR', 'Error cleaning up backups')}: {e}")

def cleanup_old_logs(max_age_days=7):
    """Lösche alte Log-Dateien"""
    try:
        cutoff_date = datetime.now() - timedelta(days=max_age_days)
        log_files = glob.glob("*.log") + glob.glob("*_log.txt")
        
        for log_file in log_files:
            try:
                file_time = datetime.fromtimestamp(os.path.getmtime(log_file))
                if file_time < cutoff_date:
                    os.remove(log_file)
                    write_log(f"{messages.get('MSG_LOG_DELETED', 'Old log file deleted')}: {log_file}")
            except Exception:
                pass
    except Exception as e:
        write_log(f"{messages.get('MSG_CLEANUP_LOGS_ERROR', 'Error cleaning up logs')}: {e}")

def find_executable(name, path_hint=None):
    """Finde ausführbare Datei im PATH"""
    if path_hint and os.path.isfile(path_hint):
        return path_hint
    
    is_windows = platform.system() == 'Windows'
    if is_windows and not name.endswith('.exe'):
        name = name + '.exe'
    
    for path in os.environ.get('PATH', '').split(os.pathsep):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    
    return None

def parse_config():
    """Lade Konfiguration aus JSON"""
    if not os.path.exists(CONFIG_FILE):
        print(messages.get("MSG_CONFIG_NOT_FOUND", "Konfigurationsdatei nicht gefunden!"))
        sys.exit(1)
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Pfade expandieren
        home = os.path.expanduser('~')
        settings = {
            'keepassxc': config['keepass'].get('keepassXCPath', 'keepassxc-cli').replace('~', home),
            'ftp_host': config['ftp']['host'],
            'ftp_user': config['ftp']['user'],
            'ftp_pass': config['ftp'].get('password', ''),
            'ftp_type': config['ftp'].get('type', 'ftp'),
            'ftp_db': config['ftp']['remotePath'],
            'local_db': config['local']['localPath'].replace('~', home),
            'temp_db': config['local']['tempPath'].replace('~', home),
            'backup_dir': config['local']['backupDir'],
            'max_backups': config['local'].get('maxBackups', 2),
            'db_password': config['keepass']['databasePassword'],
            'debug': config['settings'].get('debug', False),
            'language': config['settings'].get('language', 'de'),
            'cleanup_logs': config['settings'].get('cleanupLogs', True),
            'max_log_age': config['settings'].get('maxLogAgeDays', 7),
        }
        
        return settings
    except Exception as e:
        print(messages.get("MSG_CONFIG_LOAD_ERROR", f"Error loading configuration: {e}"))
        sys.exit(1)

def create_backup(local_db, backup_dir):
    """Erstelle Backup der lokalen Datenbank"""
    if not os.path.exists(local_db):
        write_log(messages.get("MSG_BACKUP_FAIL", "Lokale Datenbank nicht gefunden"))
        return False
    
    os.makedirs(backup_dir, exist_ok=True)
    backup_file = os.path.join(backup_dir, f"keepass_passwords_{datetime.now().strftime('%Y%m%d')}.kdbx")
    
    try:
        shutil.copy2(local_db, backup_file)
        write_log(messages.get("MSG_BACKUP_SUCCESS", "Backup erfolgreich erstellt"))
        return True
    except Exception as e:
        write_log(f"{messages.get('MSG_BACKUP_FAIL', 'Backup fehlgeschlagen')}: {e}")
        return False

def download_ftp(host, user, password, remote_path, temp_file, ftp_type='ftp'):
    """Lade Datei vom FTP-Server herunter"""
    write_log(messages.get("MSG_DOWNLOAD_START", "Starte Download..."))
    
    remote_dir = os.path.dirname(remote_path) or ''
    remote_file = os.path.basename(remote_path)
    if remote_dir == '/':
        remote_dir = ''
    
    lftp_cmd = ['lftp']
    if password:
        lftp_cmd.extend(['-u', f"{user},{password}"])
    else:
        lftp_cmd.extend(['-u', user])
    
    if ftp_type.lower() == 'ftp':
        lftp_cmd.append(f"ftp://{host}")
    else:
        lftp_cmd.append(f"sftp://{host}")
    
    lftp_script = []
    if ftp_type.lower() == 'sftp':
        lftp_script.append('set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"')
    
    if remote_dir:
        lftp_script.append(f"cd {remote_dir}")
    
    lftp_script.append(f'get "{remote_file}" -o "{temp_file}"')
    lftp_script.append('quit')
    
    script_content = '\n'.join(lftp_script) + '\n'
    
    try:
        with open(FTP_LOG, 'w', encoding='utf-8') as log_file:
            process = subprocess.Popen(
                lftp_cmd,
                stdin=subprocess.PIPE,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True
            )
            process.stdin.write(script_content)
            process.stdin.close()
            process.wait()
        
        if os.path.exists(temp_file):
            write_log(messages.get("MSG_DOWNLOAD_SUCCESS", "Download erfolgreich"))
            return True
        else:
            with open(FTP_LOG, 'r', encoding='utf-8') as f:
                error = f.read()
            write_log(f"{messages.get('MSG_DOWNLOAD_FAIL', 'Download fehlgeschlagen')}: {error}")
            return False
    except FileNotFoundError:
        write_log(messages.get("MSG_FTP_CLIENT_NOT_FOUND", "FTP-Client nicht gefunden"))
        return False
    except Exception as e:
        write_log(f"{messages.get('MSG_DOWNLOAD_FAIL', 'Download fehlgeschlagen')}: {e}")
        return False

def merge_databases(keepassxc, local_db, temp_db, password):
    """Führe Merge der Datenbanken durch"""
    write_log(messages.get("MSG_MERGE_START", "Führe Merge durch..."))
    
    if not os.path.exists(temp_db):
        write_log(messages.get("MSG_MERGE_FAIL", "Merge fehlgeschlagen: Temporäre Datei nicht gefunden"))
        return False
    
    try:
        cmd = [keepassxc, 'merge', '-s', local_db, temp_db, '--same-credentials']
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=password)
        
        if process.returncode == 0:
            write_log(messages.get("MSG_MERGE_SUCCESS", "Merge erfolgreich"))
            return True
        else:
            write_log(f"{messages.get('MSG_MERGE_FAIL', 'Merge fehlgeschlagen')}: {stderr}")
            return False
    except FileNotFoundError:
        write_log(messages.get("MSG_KEEPASSXC_NOT_FOUND", "KeePassXC-CLI nicht gefunden"))
        return False
    except Exception as e:
        write_log(f"{messages.get('MSG_MERGE_FAIL', 'Merge fehlgeschlagen')}: {e}")
        return False

def upload_ftp(host, user, password, remote_path, local_file, ftp_type='ftp'):
    """Lade Datei zum FTP-Server hoch"""
    write_log(messages.get("MSG_UPLOAD_START", "Starte Upload..."))
    
    remote_dir = os.path.dirname(remote_path) or ''
    remote_file = os.path.basename(remote_path)
    if remote_dir == '/':
        remote_dir = ''
    
    lftp_cmd = ['lftp']
    if password:
        lftp_cmd.extend(['-u', f"{user},{password}"])
    else:
        lftp_cmd.extend(['-u', user])
    
    if ftp_type.lower() == 'ftp':
        lftp_cmd.append(f"ftp://{host}")
    else:
        lftp_cmd.append(f"sftp://{host}")
    
    lftp_script = []
    if ftp_type.lower() == 'sftp':
        lftp_script.append('set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"')
    
    if remote_dir:
        lftp_script.append(f"cd {remote_dir}")
    
    lftp_script.append(f'put "{local_file}" -o "{remote_file}"')
    lftp_script.append('quit')
    
    script_content = '\n'.join(lftp_script) + '\n'
    
    try:
        with open(FTP_LOG, 'w', encoding='utf-8') as log_file:
            process = subprocess.Popen(
                lftp_cmd,
                stdin=subprocess.PIPE,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True
            )
            process.stdin.write(script_content)
            process.stdin.close()
            process.wait()
        
        write_log(messages.get("MSG_UPLOAD_SUCCESS", "Upload erfolgreich"))
        return True
    except Exception as e:
        write_log(f"{messages.get('MSG_UPLOAD_FAIL', 'Upload fehlgeschlagen')}: {e}")
        return False

def main():
    """Hauptfunktion"""
    # Arbeitsverzeichnis auf Hauptverzeichnis setzen (ein Level nach oben von python/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Ein Level nach oben
    os.chdir(base_dir)
    
    # Sprache beim Start laden (aus System oder Config)
    system_lang = os.environ.get('LANG', '').split('_')[0] or os.environ.get('LC_ALL', '').split('_')[0]
    supported_languages = ['de', 'en', 'es']
    if system_lang not in supported_languages:
        system_lang = 'de'  # Standard: Deutsch
    
    # Temporär Sprache laden für Config-Laden
    load_language(system_lang)
    
    # Konfiguration laden
    config = parse_config()
    
    # Sprache aus Config verwenden
    load_language(config['language'])
    
    # Aufräumen: Alte Logs und temporäre Dateien
    if config.get('cleanup_logs', True):
        cleanup_old_logs(config.get('max_log_age', 7))
    
    # Temporäre Dateien und Python-Cache aufräumen
    for temp_pattern in ['temp_*', '*.tmp']:
        for temp_file in glob.glob(temp_pattern):
            try:
                if os.path.isfile(temp_file):
                    os.remove(temp_file)
            except Exception:
                pass
    
    # Python-Cache aufräumen (falls vorhanden)
    for pycache_dir in ['__pycache__', 'python/__pycache__']:
        if os.path.exists(pycache_dir):
            try:
                shutil.rmtree(pycache_dir)
            except Exception:
                pass
    
    # Log-Dateien löschen (neues Log starten)
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    if os.path.exists(FTP_LOG):
        os.remove(FTP_LOG)
    
    write_log(f"=== KeePass Sync - {platform.system()} ===")
    
    # Debug-Ausgabe
    if config['debug']:
        write_log(f"Debug: KEEPASSXC={config['keepassxc']}")
        write_log(f"Debug: FTP_HOST={config['ftp_host']}")
        write_log(f"Debug: FTP_USER={config['ftp_user']}")
        write_log(f"Debug: FTP_TYPE={config['ftp_type']}")
    
    # KeePassXC finden
    keepassxc = find_executable(config['keepassxc'])
    if not keepassxc:
        write_log(messages.get("MSG_KEEPASSXC_NOT_FOUND", "KeePassXC-CLI nicht gefunden"))
        sys.exit(1)
    
    config['keepassxc'] = keepassxc
    
    # Backup erstellen
    write_log(messages.get("MSG_BACKUP", "Erstelle Backup..."))
    create_backup(config['local_db'], config['backup_dir'])
    
    # Alte Backups aufräumen
    cleanup_old_backups(config['backup_dir'], config['max_backups'])
    
    # Download
    if not download_ftp(
        config['ftp_host'],
        config['ftp_user'],
        config['ftp_pass'],
        config['ftp_db'],
        config['temp_db'],
        config['ftp_type']
    ):
        sys.exit(1)
    
    # Merge
    if not merge_databases(
        config['keepassxc'],
        config['local_db'],
        config['temp_db'],
        config['db_password']
    ):
        sys.exit(1)
    
    # Upload
    if not upload_ftp(
        config['ftp_host'],
        config['ftp_user'],
        config['ftp_pass'],
        config['ftp_db'],
        config['local_db'],
        config['ftp_type']
    ):
        sys.exit(1)
    
    # Aufräumen
    if os.path.exists(config['temp_db']):
        os.remove(config['temp_db'])
    
    write_log(messages.get("MSG_SYNC_COMPLETE", "Synchronisation abgeschlossen"))

if __name__ == '__main__':
    main()
