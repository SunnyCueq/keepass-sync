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
import argparse
import time
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
    supported_languages = ['de', 'en', 'es', 'fr', 'it', 'pt', 'nl', 'pl', 'ru', 'zh', 'ja', 'ko']
    
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
        
        # Protokoll-Informationen aus Config extrahieren
        ftp_config = config['ftp']
        protocol = ftp_config.get('type', 'ftp').lower()
        
        # Basis-Einstellungen
        settings = {
            'keepassxc': config['keepass'].get('keepassXCPath', 'keepassxc-cli').replace('~', home),
            'protocol': protocol,
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
        
        # Protokoll-spezifische Einstellungen
        if protocol in ['ftp', 'sftp']:
            settings.update({
                'host': ftp_config['host'],
                'user': ftp_config['user'],
                'password': ftp_config.get('password', ''),
                'remote_path': ftp_config['remotePath'],
                'port': ftp_config.get('port', 21 if protocol == 'ftp' else 22),
            })
        elif protocol == 'smb':
            settings.update({
                'host': ftp_config['host'],
                'share': ftp_config['share'],
                'user': ftp_config['user'],
                'password': ftp_config.get('password', ''),
                'domain': ftp_config.get('domain', 'WORKGROUP'),
                'remote_path': ftp_config['remotePath'],
            })
        elif protocol == 'scp':
            settings.update({
                'host': ftp_config['host'],
                'user': ftp_config['user'],
                'password': ftp_config.get('password', ''),
                'remote_path': ftp_config['remotePath'],
                'port': ftp_config.get('port', 22),
            })
        
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

def download_file(host, user, password, remote_path, temp_file, protocol='ftp', max_retries=3, initial_delay=5, **kwargs):
    """Lade Datei herunter - unterstützt FTP, SFTP, SMB, SCP mit Retry-Logic"""
    for attempt in range(max_retries):
        if attempt > 0:
            delay = min(initial_delay * (2 ** (attempt - 1)), 60)  # Exponential Backoff, max 60s
            write_log(f"Wiederholung {attempt}/{max_retries-1} in {delay} Sekunden...")
            time.sleep(delay)
        
        if protocol.lower() in ['ftp', 'sftp']:
            result = download_ftp(host, user, password, remote_path, temp_file, protocol)
        elif protocol.lower() == 'smb':
            result = download_smb(host, kwargs.get('share', ''), user, password, remote_path, temp_file, kwargs.get('domain', 'WORKGROUP'))
        elif protocol.lower() == 'scp':
            result = download_scp(host, user, password, remote_path, temp_file, kwargs.get('port', 22))
        else:
            write_log(f"Unbekanntes Protokoll: {protocol}")
            return False
        
        if result:
            return True
    
    write_log(f"Download nach {max_retries} Versuchen fehlgeschlagen")
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

def upload_file(host, user, password, remote_path, local_file, protocol='ftp', max_retries=3, initial_delay=5, **kwargs):
    """Lade Datei hoch - unterstützt FTP, SFTP, SMB, SCP mit Retry-Logic"""
    for attempt in range(max_retries):
        if attempt > 0:
            delay = min(initial_delay * (2 ** (attempt - 1)), 60)  # Exponential Backoff, max 60s
            write_log(f"Wiederholung {attempt}/{max_retries-1} in {delay} Sekunden...")
            time.sleep(delay)
        
        if protocol.lower() in ['ftp', 'sftp']:
            result = upload_ftp(host, user, password, remote_path, local_file, protocol)
        elif protocol.lower() == 'smb':
            result = upload_smb(host, kwargs.get('share', ''), user, password, remote_path, local_file, kwargs.get('domain', 'WORKGROUP'))
        elif protocol.lower() == 'scp':
            result = upload_scp(host, user, password, remote_path, local_file, kwargs.get('port', 22))
        else:
            write_log(f"Unbekanntes Protokoll: {protocol}")
            return False
        
        if result:
            return True
    
    write_log(f"Upload nach {max_retries} Versuchen fehlgeschlagen")
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

def download_smb(host, share, user, password, remote_path, temp_file, domain='WORKGROUP'):
    """Lade Datei von SMB/CIFS-Freigabe herunter"""
    write_log(messages.get("MSG_DOWNLOAD_START", "Starte Download..."))
    
    try:
        # Verwende smbclient (Linux/macOS) oder native Windows-Tools
        if platform.system() == 'Windows':
            # Windows: Verwende net use oder robocopy
            # Für einfache Implementierung: Python Library pysmb
            write_log("SMB auf Windows: Verwende native Methode")
            # Fallback: Versuche mit pysmb falls installiert
            try:
                from smb.SMBConnection import SMBConnection
                conn = SMBConnection(user, password, 'keepass-sync', host, domain=domain, use_ntlm_v2=True)
                conn.connect(host, 139)
                
                with open(temp_file, 'wb') as local_file:
                    conn.retrieveFile(share, remote_path, local_file)
                
                conn.close()
                
                if os.path.exists(temp_file):
                    write_log(messages.get("MSG_DOWNLOAD_SUCCESS", "Download erfolgreich"))
                    return True
            except ImportError:
                write_log("Fehler: pysmb nicht installiert. Installiere mit: pip install pysmb")
                return False
        else:
            # Linux/macOS: Verwende smbclient
            smb_url = f"//{host}/{share}"
            cmd = [
                'smbclient',
                smb_url,
                '-U', f"{domain}\\{user}%{password}",
                '-c', f'get "{remote_path}" "{temp_file}"'
            ]
            
            process = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if os.path.exists(temp_file):
                write_log(messages.get("MSG_DOWNLOAD_SUCCESS", "Download erfolgreich"))
                return True
            else:
                write_log(f"{messages.get('MSG_DOWNLOAD_FAIL', 'Download fehlgeschlagen')}: {process.stderr}")
                return False
    except FileNotFoundError:
        write_log("SMB-Client nicht gefunden. Installiere smbclient: sudo apt install smbclient")
        return False
    except Exception as e:
        write_log(f"{messages.get('MSG_DOWNLOAD_FAIL', 'Download fehlgeschlagen')}: {e}")
        return False

def upload_smb(host, share, user, password, remote_path, local_file, domain='WORKGROUP'):
    """Lade Datei zu SMB/CIFS-Freigabe hoch"""
    write_log(messages.get("MSG_UPLOAD_START", "Starte Upload..."))
    
    try:
        if platform.system() == 'Windows':
            # Windows: Verwende pysmb
            try:
                from smb.SMBConnection import SMBConnection
                conn = SMBConnection(user, password, 'keepass-sync', host, domain=domain, use_ntlm_v2=True)
                conn.connect(host, 139)
                
                with open(local_file, 'rb') as local_file_obj:
                    conn.storeFile(share, remote_path, local_file_obj)
                
                conn.close()
                write_log(messages.get("MSG_UPLOAD_SUCCESS", "Upload erfolgreich"))
                return True
            except ImportError:
                write_log("Fehler: pysmb nicht installiert. Installiere mit: pip install pysmb")
                return False
        else:
            # Linux/macOS: Verwende smbclient
            smb_url = f"//{host}/{share}"
            cmd = [
                'smbclient',
                smb_url,
                '-U', f"{domain}\\{user}%{password}",
                '-c', f'put "{local_file}" "{remote_path}"'
            ]
            
            process = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if process.returncode == 0:
                write_log(messages.get("MSG_UPLOAD_SUCCESS", "Upload erfolgreich"))
                return True
            else:
                write_log(f"{messages.get('MSG_UPLOAD_FAIL', 'Upload fehlgeschlagen')}: {process.stderr}")
                return False
    except FileNotFoundError:
        write_log("SMB-Client nicht gefunden. Installiere smbclient: sudo apt install smbclient")
        return False
    except Exception as e:
        write_log(f"{messages.get('MSG_UPLOAD_FAIL', 'Upload fehlgeschlagen')}: {e}")
        return False

def download_scp(host, user, password, remote_path, temp_file, port=22):
    """Lade Datei via SCP herunter"""
    write_log(messages.get("MSG_DOWNLOAD_START", "Starte Download..."))
    
    try:
        # Verwende sshpass für Passwort-Übergabe, oder paramiko
        # Option 1: scp mit sshpass (Linux/macOS)
        if platform.system() != 'Windows':
            cmd = [
                'sshpass', '-p', password,
                'scp', '-P', str(port),
                '-o', 'StrictHostKeyChecking=no',
                '-o', 'UserKnownHostsFile=/dev/null',
                f"{user}@{host}:{remote_path}",
                temp_file
            ]
            
            process = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if os.path.exists(temp_file):
                write_log(messages.get("MSG_DOWNLOAD_SUCCESS", "Download erfolgreich"))
                return True
            else:
                write_log(f"{messages.get('MSG_DOWNLOAD_FAIL', 'Download fehlgeschlagen')}: {process.stderr}")
                return False
        else:
            # Windows: Verwende paramiko
            try:
                import paramiko
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=port, username=user, password=password)
                
                sftp = ssh.open_sftp()
                sftp.get(remote_path, temp_file)
                sftp.close()
                ssh.close()
                
                if os.path.exists(temp_file):
                    write_log(messages.get("MSG_DOWNLOAD_SUCCESS", "Download erfolgreich"))
                    return True
            except ImportError:
                write_log("Fehler: paramiko nicht installiert. Installiere mit: pip install paramiko")
                return False
    except FileNotFoundError:
        write_log("SCP-Tool nicht gefunden. Installiere sshpass: sudo apt install sshpass")
        return False
    except Exception as e:
        write_log(f"{messages.get('MSG_DOWNLOAD_FAIL', 'Download fehlgeschlagen')}: {e}")
        return False

def upload_scp(host, user, password, remote_path, local_file, port=22):
    """Lade Datei via SCP hoch"""
    write_log(messages.get("MSG_UPLOAD_START", "Starte Upload..."))
    
    try:
        if platform.system() != 'Windows':
            # Linux/macOS: scp mit sshpass
            remote_dir = os.path.dirname(remote_path) or '.'
            remote_file = os.path.basename(remote_path)
            
            # Erstelle Verzeichnis falls nötig
            mkdir_cmd = [
                'sshpass', '-p', password,
                'ssh', '-p', str(port),
                '-o', 'StrictHostKeyChecking=no',
                '-o', 'UserKnownHostsFile=/dev/null',
                f"{user}@{host}",
                f"mkdir -p {remote_dir}"
            ]
            subprocess.run(mkdir_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            cmd = [
                'sshpass', '-p', password,
                'scp', '-P', str(port),
                '-o', 'StrictHostKeyChecking=no',
                '-o', 'UserKnownHostsFile=/dev/null',
                local_file,
                f"{user}@{host}:{remote_path}"
            ]
            
            process = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if process.returncode == 0:
                write_log(messages.get("MSG_UPLOAD_SUCCESS", "Upload erfolgreich"))
                return True
            else:
                write_log(f"{messages.get('MSG_UPLOAD_FAIL', 'Upload fehlgeschlagen')}: {process.stderr}")
                return False
        else:
            # Windows: paramiko
            try:
                import paramiko
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=port, username=user, password=password)
                
                sftp = ssh.open_sftp()
                
                # Erstelle Verzeichnis falls nötig
                remote_dir = os.path.dirname(remote_path)
                if remote_dir:
                    try:
                        sftp.mkdir(remote_dir)
                    except:
                        pass  # Verzeichnis existiert bereits
                
                sftp.put(local_file, remote_path)
                sftp.close()
                ssh.close()
                
                write_log(messages.get("MSG_UPLOAD_SUCCESS", "Upload erfolgreich"))
                return True
            except ImportError:
                write_log("Fehler: paramiko nicht installiert. Installiere mit: pip install paramiko")
                return False
    except FileNotFoundError:
        write_log("SCP-Tool nicht gefunden. Installiere sshpass: sudo apt install sshpass")
        return False
    except Exception as e:
        write_log(f"{messages.get('MSG_UPLOAD_FAIL', 'Upload fehlgeschlagen')}: {e}")
        return False

def test_connection(config):
    """Teste Verbindung zum Server und prüfe Konfiguration"""
    write_log("=== Verbindungs-Test ===")
    errors = []
    
    # KeePassXC prüfen
    keepassxc = find_executable(config['keepassxc'])
    if not keepassxc:
        errors.append(f"❌ {messages.get('MSG_KEEPASSXC_NOT_FOUND', 'KeePassXC-CLI nicht gefunden')}")
    else:
        write_log(f"✅ KeePassXC-CLI gefunden: {keepassxc}")
    
    # Lokale Datei prüfen
    if os.path.exists(config['local_db']):
        size = os.path.getsize(config['local_db'])
        mtime = datetime.fromtimestamp(os.path.getmtime(config['local_db']))
        write_log(f"✅ Lokale Datenbank: {config['local_db']} ({size} bytes, modifiziert: {mtime.strftime('%Y-%m-%d %H:%M:%S')})")
    else:
        errors.append(f"⚠️ Lokale Datenbank nicht gefunden: {config['local_db']}")
    
    # Verbindung testen
    protocol = config['protocol']
    write_log(f"Teste Verbindung ({protocol.upper()})...")
    
    if protocol in ['ftp', 'sftp']:
        # Test-Download (nur Verbindung prüfen)
        test_file = config['temp_db'] + '.test'
        try:
            # Versuche Verbindung herzustellen (ohne Datei zu laden)
            if protocol == 'ftp':
                test_cmd = ['lftp', '-u', f"{config['user']},{config['password']}", f"ftp://{config['host']}", '-e', 'quit']
            else:
                test_cmd = ['lftp', '-u', f"{config['user']},{config['password']}", f"sftp://{config['host']}", '-e', 'set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"; quit']
            
            process = subprocess.run(test_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
            if process.returncode == 0:
                write_log(f"✅ Verbindung zum Server erfolgreich: {config['host']}")
            else:
                errors.append(f"❌ Verbindung fehlgeschlagen: {process.stderr.decode('utf-8', errors='ignore')}")
        except subprocess.TimeoutExpired:
            errors.append("❌ Verbindung fehlgeschlagen: Timeout")
        except FileNotFoundError:
            errors.append(f"❌ {messages.get('MSG_FTP_CLIENT_NOT_FOUND', 'FTP-Client nicht gefunden')}")
        except Exception as e:
            errors.append(f"❌ Verbindung fehlgeschlagen: {e}")
    
    elif protocol == 'smb':
        if platform.system() == 'Windows':
            write_log("⚠️ SMB-Test auf Windows: Bitte manuell prüfen")
        else:
            try:
                smb_url = f"//{config['host']}/{config['share']}"
                cmd = ['smbclient', smb_url, '-U', f"{config['domain']}\\{config['user']}%{config['password']}", '-c', 'ls']
                process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
                if process.returncode == 0:
                    write_log(f"✅ SMB-Verbindung erfolgreich: {smb_url}")
                else:
                    errors.append(f"❌ SMB-Verbindung fehlgeschlagen: {process.stderr.decode('utf-8', errors='ignore')}")
            except FileNotFoundError:
                errors.append("❌ smbclient nicht gefunden")
            except Exception as e:
                errors.append(f"❌ SMB-Verbindung fehlgeschlagen: {e}")
    
    elif protocol == 'scp':
        try:
            if platform.system() != 'Windows':
                cmd = ['sshpass', '-p', config['password'], 'ssh', '-o', 'ConnectTimeout=10', '-o', 'StrictHostKeyChecking=no', '-o', 'UserKnownHostsFile=/dev/null', '-p', str(config['port']), f"{config['user']}@{config['host']}", 'echo "OK"']
                process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
                if process.returncode == 0:
                    write_log(f"✅ SCP/SSH-Verbindung erfolgreich: {config['host']}:{config['port']}")
                else:
                    errors.append(f"❌ SCP-Verbindung fehlgeschlagen: {process.stderr.decode('utf-8', errors='ignore')}")
            else:
                write_log("⚠️ SCP-Test auf Windows: Bitte manuell prüfen (paramiko)")
        except FileNotFoundError:
            errors.append("❌ sshpass nicht gefunden")
        except Exception as e:
            errors.append(f"❌ SCP-Verbindung fehlgeschlagen: {e}")
    
    # Zusammenfassung
    write_log("=== Test abgeschlossen ===")
    if errors:
        write_log("Fehler gefunden:")
        for error in errors:
            write_log(error)
        return False
    else:
        write_log("✅ Alle Tests erfolgreich!")
        return True

def show_status(config):
    """Zeige Status-Informationen"""
    write_log("=== KeePass Sync Status ===")
    
    # Lokale Datei
    if os.path.exists(config['local_db']):
        size = os.path.getsize(config['local_db'])
        mtime = datetime.fromtimestamp(os.path.getmtime(config['local_db']))
        age = datetime.now() - mtime
        write_log(f"Lokale DB: {config['local_db']}")
        write_log(f"  Größe: {size:,} bytes ({size/1024:.2f} KB)")
        write_log(f"  Modifiziert: {mtime.strftime('%Y-%m-%d %H:%M:%S')} (vor {age.days}d {age.seconds//3600}h)")
    else:
        write_log(f"⚠️ Lokale DB nicht gefunden: {config['local_db']}")
    
    # Backups
    backup_dir = config['backup_dir']
    if os.path.exists(backup_dir):
        backups = sorted(glob.glob(os.path.join(backup_dir, "*.kdbx")), key=os.path.getmtime, reverse=True)
        write_log(f"Backups: {len(backups)} gefunden")
        for i, backup in enumerate(backups[:3], 1):
            size = os.path.getsize(backup)
            mtime = datetime.fromtimestamp(os.path.getmtime(backup))
            write_log(f"  {i}. {os.path.basename(backup)} ({size/1024:.2f} KB, {mtime.strftime('%Y-%m-%d %H:%M:%S')})")
    else:
        write_log(f"⚠️ Backup-Verzeichnis nicht gefunden: {backup_dir}")
    
    # Konfiguration
    write_log(f"Protokoll: {config['protocol'].upper()}")
    write_log(f"Server: {config.get('host', 'N/A')}")
    write_log(f"Benutzer: {config.get('user', 'N/A')}")
    
    # KeePassXC
    keepassxc = find_executable(config['keepassxc'])
    if keepassxc:
        write_log(f"KeePassXC-CLI: ✅ {keepassxc}")
    else:
        write_log(f"KeePassXC-CLI: ❌ Nicht gefunden")

def watch_file(config, delay=30):
    """Überwache Datei auf Änderungen und starte Sync automatisch"""
    write_log(f"=== Datei-Überwachung aktiviert (Verzögerung: {delay}s) ===")
    
    try:
        if platform.system() == 'Linux':
            try:
                import pyinotify
                wm = pyinotify.WatchManager()
                mask = pyinotify.IN_MODIFY | pyinotify.IN_CLOSE_WRITE
            
                class EventHandler(pyinotify.ProcessEvent):
                    def __init__(self, config, delay):
                        self.config = config
                        self.delay = delay
                        self.last_trigger = 0
                    
                    def process_IN_MODIFY(self, event):
                        self.trigger_sync()
                    
                    def process_IN_CLOSE_WRITE(self, event):
                        self.trigger_sync()
                    
                    def trigger_sync(self):
                        now = time.time()
                        if now - self.last_trigger < self.delay:
                            return
                        self.last_trigger = now
                        write_log(f"Datei-Änderung erkannt, starte Sync in {self.delay}s...")
                        time.sleep(self.delay)
                        write_log("Starte Synchronisation...")
                        perform_sync(self.config)
                
                handler = EventHandler(config, delay)
                notifier = pyinotify.Notifier(wm, handler)
                wm.add_watch(config['local_db'], mask)
                write_log(f"Überwache: {config['local_db']}")
                notifier.loop()
            except ImportError:
                write_log("⚠️ pyinotify nicht installiert. Installiere mit: pip install pyinotify")
                write_log("Fallback: Polling-Modus...")
                watch_file_polling(config, delay)
        else:
            # macOS/Windows: watchdog oder Polling
            try:
                from watchdog.observers import Observer
                from watchdog.events import FileSystemEventHandler
                
                class SyncHandler(FileSystemEventHandler):
                    def __init__(self, config, delay):
                        self.config = config
                        self.delay = delay
                        self.last_trigger = 0
                    
                    def on_modified(self, event):
                        if event.src_path == self.config['local_db']:
                            self.trigger_sync()
                    
                    def trigger_sync(self):
                        now = time.time()
                        if now - self.last_trigger < self.delay:
                            return
                        self.last_trigger = now
                        write_log(f"Datei-Änderung erkannt, starte Sync in {self.delay}s...")
                        time.sleep(self.delay)
                        write_log("Starte Synchronisation...")
                        perform_sync(self.config)
                
                event_handler = SyncHandler(config, delay)
                observer = Observer()
                observer.schedule(event_handler, os.path.dirname(config['local_db']), recursive=False)
                observer.start()
                write_log(f"Überwache: {config['local_db']}")
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    observer.stop()
                observer.join()
            except ImportError:
                write_log("⚠️ watchdog nicht installiert. Installiere mit: pip install watchdog")
                write_log("Fallback: Polling-Modus...")
                watch_file_polling(config, delay)
    except Exception as e:
        write_log(f"Fehler bei Datei-Überwachung: {e}")
        write_log("Fallback: Polling-Modus...")
        watch_file_polling(config, delay)

def watch_file_polling(config, delay=30):
    """Polling-basierte Datei-Überwachung (Fallback)"""
    write_log(f"Polling-Modus: Prüfe alle {delay} Sekunden...")
    last_mtime = os.path.getmtime(config['local_db']) if os.path.exists(config['local_db']) else 0
    
    try:
        while True:
            time.sleep(delay)
            if os.path.exists(config['local_db']):
                current_mtime = os.path.getmtime(config['local_db'])
                if current_mtime > last_mtime:
                    write_log("Datei-Änderung erkannt, starte Sync...")
                    last_mtime = current_mtime
                    perform_sync(config)
    except KeyboardInterrupt:
        write_log("Überwachung beendet")

def perform_sync(config, skip_backup=False):
    """Führe Synchronisation durch (kann von watch_file aufgerufen werden)"""
    # KeePassXC finden
    keepassxc = find_executable(config['keepassxc'])
    if not keepassxc:
        write_log(messages.get("MSG_KEEPASSXC_NOT_FOUND", "KeePassXC-CLI nicht gefunden"))
        return False
    
    config['keepassxc'] = keepassxc
    
    # Backup erstellen (optional)
    if not skip_backup:
        write_log(messages.get("MSG_BACKUP", "Erstelle Backup..."))
        create_backup(config['local_db'], config['backup_dir'])
        cleanup_old_backups(config['backup_dir'], config['max_backups'])
    
    # Retry-Einstellungen aus Config
    max_retries = config.get('max_retries', 3)
    retry_delay = config.get('retry_delay', 5)
    
    # Download (abhängig vom Protokoll)
    protocol = config['protocol']
    if protocol in ['ftp', 'sftp']:
        success = download_file(
            config['host'],
            config['user'],
            config['password'],
            config['remote_path'],
            config['temp_db'],
            protocol=protocol,
            max_retries=max_retries,
            initial_delay=retry_delay
        )
    elif protocol == 'smb':
        success = download_file(
            config['host'],
            config['user'],
            config['password'],
            config['remote_path'],
            config['temp_db'],
            protocol=protocol,
            max_retries=max_retries,
            initial_delay=retry_delay,
            share=config['share'],
            domain=config['domain']
        )
    elif protocol == 'scp':
        success = download_file(
            config['host'],
            config['user'],
            config['password'],
            config['remote_path'],
            config['temp_db'],
            protocol=protocol,
            max_retries=max_retries,
            initial_delay=retry_delay,
            port=config['port']
        )
    else:
        write_log(f"Unbekanntes Protokoll: {protocol}")
        return False
    
    if not success:
        return False
    
    # Merge
    if not merge_databases(
        config['keepassxc'],
        config['local_db'],
        config['temp_db'],
        config['db_password']
    ):
        return False
    
    # Upload (abhängig vom Protokoll)
    if protocol in ['ftp', 'sftp']:
        success = upload_file(
            config['host'],
            config['user'],
            config['password'],
            config['remote_path'],
            config['local_db'],
            protocol=protocol,
            max_retries=max_retries,
            initial_delay=retry_delay
        )
    elif protocol == 'smb':
        success = upload_file(
            config['host'],
            config['user'],
            config['password'],
            config['remote_path'],
            config['local_db'],
            protocol=protocol,
            max_retries=max_retries,
            initial_delay=retry_delay,
            share=config['share'],
            domain=config['domain']
        )
    elif protocol == 'scp':
        success = upload_file(
            config['host'],
            config['user'],
            config['password'],
            config['remote_path'],
            config['local_db'],
            protocol=protocol,
            max_retries=max_retries,
            initial_delay=retry_delay,
            port=config['port']
        )
    else:
        write_log(f"Unbekanntes Protokoll: {protocol}")
        return False
    
    if not success:
        return False
    
    # Aufräumen
    if os.path.exists(config['temp_db']):
        os.remove(config['temp_db'])
    
    write_log(messages.get("MSG_SYNC_COMPLETE", "Synchronisation abgeschlossen"))
    return True

def main():
    """Hauptfunktion"""
    # Arbeitsverzeichnis auf Hauptverzeichnis setzen (ein Level nach oben von python/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Ein Level nach oben
    os.chdir(base_dir)
    
    # CLI-Argumente parsen
    parser = argparse.ArgumentParser(
        description='KeePass Sync - Synchronisiere KeePass-Datenbanken über FTP/SFTP/SMB/SCP',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python3 sync_ftp.py              # Normale Synchronisation
  python3 sync_ftp.py --test       # Verbindung testen
  python3 sync_ftp.py --status     # Status anzeigen
  python3 sync_ftp.py --watch      # Datei überwachen und automatisch syncen
  python3 sync_ftp.py --config alt_config.json  # Alternative Config verwenden
        """
    )
    parser.add_argument('--sync', action='store_true', help='Synchronisation ausführen (Standard)')
    parser.add_argument('--test', action='store_true', help='Verbindung testen (ohne Sync)')
    parser.add_argument('--status', action='store_true', help='Status anzeigen')
    parser.add_argument('--watch', action='store_true', help='Datei überwachen und automatisch syncen')
    parser.add_argument('--config', type=str, help='Alternative Config-Datei verwenden')
    parser.add_argument('--verbose', '-v', action='store_true', help='Detaillierte Ausgabe')
    parser.add_argument('--quiet', '-q', action='store_true', help='Nur Fehler ausgeben')
    parser.add_argument('--version', action='version', version='KeePass Sync 1.1.0')
    
    args = parser.parse_args()
    
    # Globale CONFIG_FILE überschreiben wenn angegeben
    global CONFIG_FILE
    if args.config:
        CONFIG_FILE = args.config
    
    # Sprache beim Start laden (aus System oder Config)
    system_lang = os.environ.get('LANG', '').split('_')[0] or os.environ.get('LC_ALL', '').split('_')[0]
    supported_languages = ['de', 'en', 'es', 'fr', 'it', 'pt', 'nl', 'pl', 'ru', 'zh', 'ja', 'ko']
    if system_lang not in supported_languages:
        system_lang = 'de'  # Standard: Deutsch
    
    # Temporär Sprache laden für Config-Laden
    load_language(system_lang)
    
    # Konfiguration laden
    config = parse_config()
    
    # Sprache aus Config verwenden
    load_language(config['language'])
    
    # Retry-Einstellungen zu Config hinzufügen
    config['max_retries'] = config.get('max_retries', 3)
    config['retry_delay'] = config.get('retry_delay', 5)
    
    # Debug-Modus aktivieren wenn verbose
    if args.verbose:
        config['debug'] = True
    
    # Aufräumen: Alte Logs und temporäre Dateien (nur bei Sync)
    if not (args.test or args.status):
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
    
    if not args.quiet:
        write_log(f"=== KeePass Sync - {platform.system()} ===")
    
    # Debug-Ausgabe
    if config['debug'] and not args.quiet:
        write_log(f"Debug: KEEPASSXC={config['keepassxc']}")
        write_log(f"Debug: PROTOCOL={config['protocol']}")
        write_log(f"Debug: HOST={config.get('host', 'N/A')}")
        write_log(f"Debug: USER={config.get('user', 'N/A')}")
    
    # Aktionen basierend auf Argumenten
    if args.test:
        success = test_connection(config)
        sys.exit(0 if success else 1)
    elif args.status:
        show_status(config)
        sys.exit(0)
    elif args.watch:
        watch_delay = config.get('watch_delay', 30)
        watch_file(config, watch_delay)
    else:
        # Normale Synchronisation
        success = perform_sync(config)
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
