#!/usr/bin/env php
<?php
/**
 * ⚠️ WARNUNG: SICHERHEITSRISIKO ⚠️
 * 
 * Dieses Script verarbeitet SENSIBLE PASSWÖRTER auf einem SERVER!
 * 
 * GEFAHREN:
 * - Bei Server-Kompromittierung = alle Passwörter weg
 * - PHP-Fehler könnten sensible Daten loggen
 * - Zugriff über Web = hohes Risiko
 * - Passwörter werden im RAM verarbeitet
 * 
 * ANFORDERUNGEN:
 * - ✅ Nur auf VERTRAUENSWÜRDIGEM Server verwenden (VPS/Dedicated)
 * - ✅ .htaccess mit Zugriffsbeschränkung (Apache)
 * - ✅ Nginx: location block mit deny all
 * - ✅ HTTPS zwingend erforderlich
 * - ✅ Regelmäßige Sicherheits-Updates
 * - ✅ Logs regelmäßig prüfen
 * - ✅ KeePassXC-CLI muss auf Server installiert sein
 * - ✅ Script sollte NUR über Cronjob laufen (nicht über Web)
 * 
 * EMPFOHLEN: Für Desktop-Nutzung besser Python-Variante verwenden (sicherer)
 * 
 * @package KeePassSync
 * @version 1.0.0
 */

// Nur für CLI-Ausführung erlauben (nicht über Web)
if (php_sapi_name() !== 'cli') {
    http_response_code(403);
    die("ERROR: This script must be run from command line (CLI) only!\n" .
        "For security reasons, web access is forbidden.\n");
}

// Fehlerbehandlung
error_reporting(E_ALL);
ini_set('display_errors', 0); // Keine Fehler in Output (nur Logs)
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/php_error.log');

// Pfade
$SCRIPT_DIR = __DIR__;
$BASE_DIR = dirname($SCRIPT_DIR);
$CONFIG_FILE = $BASE_DIR . '/config.json';
$LOG_FILE = $BASE_DIR . '/sync_log.txt';
$FTP_LOG = $BASE_DIR . '/ftp_log.txt';

// In Basis-Verzeichnis wechseln
chdir($BASE_DIR);

/**
 * Schreibe Nachricht ins Log
 */
function write_log($message, $log_file = null) {
    global $LOG_FILE;
    if ($log_file === null) {
        $log_file = $LOG_FILE;
    }
    
    $timestamp = date('Y-m-d H:i:s');
    $log_message = "$timestamp $message\n";
    echo $log_message;
    
    @file_put_contents($log_file, $log_message, FILE_APPEND);
}

/**
 * Lade Konfiguration
 */
function load_config() {
    global $CONFIG_FILE;
    
    if (!file_exists($CONFIG_FILE)) {
        write_log("ERROR: Configuration file not found: $CONFIG_FILE");
        exit(1);
    }
    
    $config = @json_decode(file_get_contents($CONFIG_FILE), true);
    if ($config === null) {
        write_log("ERROR: Failed to parse configuration file");
        exit(1);
    }
    
    return $config;
}

/**
 * Finde KeePassXC-CLI
 */
function find_keepassxc($hint = 'keepassxc-cli') {
    // Versuche direkt
    if ($hint && is_executable($hint)) {
        return $hint;
    }
    
    // Suche im PATH
    $paths = explode(':', getenv('PATH') ?: '');
    foreach ($paths as $path) {
        $full_path = $path . '/' . $hint;
        if (is_executable($full_path)) {
            return $full_path;
        }
    }
    
    // Versuche which/whereis
    $which = trim(shell_exec("which $hint 2>/dev/null"));
    if ($which && is_executable($which)) {
        return $which;
    }
    
    return null;
}

/**
 * Erstelle Backup
 */
function create_backup($local_db, $backup_dir) {
    if (!file_exists($local_db)) {
        write_log("WARNING: Local database not found: $local_db");
        return false;
    }
    
    if (!is_dir($backup_dir)) {
        @mkdir($backup_dir, 0755, true);
    }
    
    $backup_file = $backup_dir . '/' . 'keepass_passwords_' . date('Ymd') . '.kdbx';
    
    if (@copy($local_db, $backup_file)) {
        write_log("Backup successfully created: " . basename($backup_file));
        return true;
    } else {
        write_log("WARNING: Could not create backup");
        return false;
    }
}

/**
 * Räume alte Backups auf
 */
function cleanup_backups($backup_dir, $max_backups = 2) {
    $backups = glob($backup_dir . '/keepass_passwords_*.kdbx');
    if (count($backups) <= $max_backups) {
        return;
    }
    
    // Sortiere nach Änderungszeit
    usort($backups, function($a, $b) {
        return filemtime($b) - filemtime($a);
    });
    
    // Lösche alte Backups
    foreach (array_slice($backups, $max_backups) as $old_backup) {
        @unlink($old_backup);
        write_log("Old backup deleted: " . basename($old_backup));
    }
}

/**
 * Download von FTP-Server
 */
function download_ftp($host, $user, $password, $remote_path, $local_file) {
    write_log("Starting download from server...");
    
    $conn = @ftp_connect($host);
    if (!$conn) {
        write_log("ERROR: Could not connect to FTP server: $host");
        return false;
    }
    
    $login = @ftp_login($conn, $user, $password);
    if (!$login) {
        write_log("ERROR: FTP login failed");
        @ftp_close($conn);
        return false;
    }
    
    // Aktiviere passiven Modus
    @ftp_pasv($conn, true);
    
    $result = @ftp_get($conn, $local_file, $remote_path, FTP_BINARY);
    @ftp_close($conn);
    
    if ($result && file_exists($local_file)) {
        write_log("Download successful");
        return true;
    } else {
        write_log("ERROR: Download failed");
        return false;
    }
}

/**
 * Upload zu FTP-Server
 */
function upload_ftp($host, $user, $password, $remote_path, $local_file) {
    write_log("Starting upload to server...");
    
    $conn = @ftp_connect($host);
    if (!$conn) {
        write_log("ERROR: Could not connect to FTP server: $host");
        return false;
    }
    
    $login = @ftp_login($conn, $user, $password);
    if (!$login) {
        write_log("ERROR: FTP login failed");
        @ftp_close($conn);
        return false;
    }
    
    // Aktiviere passiven Modus
    @ftp_pasv($conn, true);
    
    $result = @ftp_put($conn, $remote_path, $local_file, FTP_BINARY);
    @ftp_close($conn);
    
    if ($result) {
        write_log("Upload successful");
        return true;
    } else {
        write_log("ERROR: Upload failed");
        return false;
    }
}

/**
 * Merge Datenbanken mit KeePassXC-CLI
 */
function merge_databases($keepassxc, $local_db, $temp_db, $password) {
    write_log("Performing merge...");
    
    if (!file_exists($temp_db)) {
        write_log("ERROR: Temporary file not found: $temp_db");
        return false;
    }
    
    $cmd = escapeshellcmd($keepassxc) . 
           ' merge -s ' . 
           escapeshellarg($local_db) . ' ' . 
           escapeshellarg($temp_db) . 
           ' --same-credentials 2>&1';
    
    $descriptorspec = [
        0 => ['pipe', 'r'],  // stdin
        1 => ['pipe', 'w'],  // stdout
        2 => ['pipe', 'w']   // stderr
    ];
    
    $process = @proc_open($cmd, $descriptorspec, $pipes);
    if (!is_resource($process)) {
        write_log("ERROR: Could not start KeePassXC-CLI");
        return false;
    }
    
    // Passwort übergeben
    fwrite($pipes[0], $password);
    fclose($pipes[0]);
    
    $output = stream_get_contents($pipes[1]);
    $error = stream_get_contents($pipes[2]);
    fclose($pipes[1]);
    fclose($pipes[2]);
    
    $return_code = proc_close($process);
    
    if ($return_code === 0) {
        write_log("Merge completed successfully. Local file updated.");
        return true;
    } else {
        write_log("ERROR: Merge failed: $error");
        return false;
    }
}

/**
 * Hauptfunktion
 */
function main() {
    global $CONFIG_FILE, $BASE_DIR;
    
    write_log("=== KeePass Sync - PHP CLI ===");
    
    // Warnung ausgeben
    write_log("WARNING: This script processes sensitive passwords on a server!");
    write_log("Ensure proper security measures are in place.");
    
    // Konfiguration laden
    $config = load_config();
    
    // KeePassXC-CLI finden
    $keepassxc_path = $config['keepass']['keepassXCPath'] ?? 'keepassxc-cli';
    $keepassxc = find_keepassxc($keepassxc_path);
    
    if (!$keepassxc) {
        write_log("ERROR: KeePassXC-CLI not found. Install: apt install keepassxc");
        write_log("Or set correct path in config.json");
        exit(1);
    }
    
    write_log("KeePassXC-CLI found: $keepassxc");
    
    // Pfade
    $local_db = $config['local']['localPath'];
    $temp_db = $config['local']['tempPath'];
    $backup_dir = $config['local']['backupDir'];
    $max_backups = $config['local']['maxBackups'] ?? 2;
    $db_password = $config['keepass']['databasePassword'];
    
    // FTP-Konfiguration
    $ftp_config = $config['ftp'];
    $host = $ftp_config['host'];
    $user = $ftp_config['user'];
    $password = $ftp_config['password'];
    $remote_path = $ftp_config['remotePath'];
    $protocol = strtolower($ftp_config['type'] ?? 'ftp');
    
    // Nur FTP wird unterstützt (SFTP braucht ssh2 Extension)
    if ($protocol !== 'ftp') {
        write_log("WARNING: PHP-Variante unterstützt nur FTP. Für SFTP/SMB/SCP nutze Python-Variante.");
        write_log("Protocol '$protocol' wird als FTP behandelt.");
    }
    
    // Backup erstellen
    write_log("Creating backup...");
    create_backup($local_db, $backup_dir);
    cleanup_backups($backup_dir, $max_backups);
    
    // Download
    if (!download_ftp($host, $user, $password, $remote_path, $temp_db)) {
        exit(1);
    }
    
    // Merge
    if (!merge_databases($keepassxc, $local_db, $temp_db, $db_password)) {
        exit(1);
    }
    
    // Upload
    if (!upload_ftp($host, $user, $password, $remote_path, $local_db)) {
        exit(1);
    }
    
    // Aufräumen
    if (file_exists($temp_db)) {
        @unlink($temp_db);
    }
    
    write_log("Synchronization completed.");
}

// Ausführen
try {
    main();
} catch (Exception $e) {
    write_log("FATAL ERROR: " . $e->getMessage());
    exit(1);
}

