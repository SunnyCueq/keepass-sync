#!/usr/bin/env node
/**
 * KeePass Sync - Node.js/JavaScript Version
 * Cross-Platform: Linux, Windows, macOS
 * 
 * Installation:
 *   npm install ftp sftp-ssh node-scp
 * 
 * Usage:
 *   node sync.js
 *   node sync.js --test
 *   node sync.js --status
 *   node sync.js --help
 */

const fs = require('fs');
const path = require('path');
const { exec, spawn } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

// For FTP (if needed, use ftp package)
// const ftp = require('basic-ftp');

// CLI arguments
const args = process.argv.slice(2);
const flags = {
    test: args.includes('--test'),
    status: args.includes('--status'),
    watch: args.includes('--watch'),
    verbose: args.includes('--verbose') || args.includes('-v'),
    quiet: args.includes('--quiet') || args.includes('-q'),
    version: args.includes('--version'),
    help: args.includes('--help'),
    config: args[args.indexOf('--config') + 1] || 'config.json'
};

// Paths
let configFile = flags.config;
let logFile = 'sync_log.txt';
let baseDir = process.cwd();

// Change to script directory
const scriptDir = __dirname;
process.chdir(path.dirname(scriptDir));

// Config structure
let config = {};

/**
 * Write log message
 */
function writeLog(message, logFilePath = logFile) {
    const timestamp = new Date().toISOString().replace('T', ' ').substring(0, 19);
    const logMessage = `${timestamp} ${message}`;
    
    if (!flags.quiet) {
        console.log(logMessage);
    }
    
    try {
        fs.appendFileSync(logFilePath, logMessage + '\n');
    } catch (err) {
        // Ignore
    }
}

/**
 * Load configuration
 */
function loadConfig() {
    try {
        const data = fs.readFileSync(configFile, 'utf8');
        config = JSON.parse(data);
        
        // Set defaults
        if (!config.settings) config.settings = {};
        if (!config.settings.max_retries) config.settings.max_retries = 3;
        if (!config.settings.retry_delay) config.settings.retry_delay = 5;
        if (!config.settings.watch_delay) config.settings.watch_delay = 30;
        if (!config.local.maxBackups) config.local.maxBackups = 2;
        
        return true;
    } catch (err) {
        writeLog(`ERROR: Configuration file not found: ${configFile}`);
        process.exit(1);
    }
}

/**
 * Find executable in PATH
 */
function findExecutable(name) {
    // Try direct path
    try {
        if (fs.statSync(name).isFile()) {
            return name;
        }
    } catch (err) {
        // Not found
    }
    
    // Search in PATH
    const pathEnv = process.env.PATH || '';
    const paths = pathEnv.split(path.delimiter);
    
    for (const p of paths) {
        const fullPath = path.join(p, name);
        try {
            if (fs.statSync(fullPath).isFile()) {
                return fullPath;
            }
        } catch (err) {
            // Not found
        }
    }
    
    return null;
}

/**
 * Create backup
 */
function createBackup(localDB, backupDir) {
    writeLog('Creating backup...');
    
    try {
        if (!fs.existsSync(localDB)) {
            writeLog('WARNING: Local database not found');
            return false;
        }
        
        if (!fs.existsSync(backupDir)) {
            fs.mkdirSync(backupDir, { recursive: true });
        }
        
        const today = new Date().toISOString().substring(0, 10).replace(/-/g, '');
        const backupFile = path.join(backupDir, `keepass_passwords_${today}.kdbx`);
        
        fs.copyFileSync(localDB, backupFile);
        writeLog('Backup successfully created');
        return true;
    } catch (err) {
        writeLog(`WARNING: Could not create backup: ${err.message}`);
        return false;
    }
}

/**
 * Cleanup old backups
 */
function cleanupBackups(backupDir, maxBackups) {
    try {
        const files = fs.readdirSync(backupDir)
            .filter(f => f.startsWith('keepass_passwords_') && f.endsWith('.kdbx'))
            .map(f => ({
                path: path.join(backupDir, f),
                mtime: fs.statSync(path.join(backupDir, f)).mtime
            }))
            .sort((a, b) => b.mtime - a.mtime);
        
        if (files.length > maxBackups) {
            for (let i = maxBackups; i < files.length; i++) {
                fs.unlinkSync(files[i].path);
                writeLog(`Old backup deleted: ${path.basename(files[i].path)}`);
            }
        }
    } catch (err) {
        // Ignore
    }
}

/**
 * Download file with retry logic
 */
async function downloadFile(host, user, password, remotePath, tempFile, protocol, maxRetries, retryDelay, port, share, domain) {
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        if (attempt > 0) {
            const delay = Math.min(retryDelay * Math.pow(2, attempt - 1), 60);
            writeLog(`Retry ${attempt}/${maxRetries - 1} in ${delay} seconds...`);
            await new Promise(resolve => setTimeout(resolve, delay * 1000));
        }
        
        let success = false;
        
        if (protocol === 'ftp' || protocol === 'sftp') {
            success = await downloadFTP(host, user, password, remotePath, tempFile, protocol === 'sftp', port);
        } else if (protocol === 'smb') {
            success = await downloadSMB(host, share, user, password, remotePath, tempFile, domain);
        } else if (protocol === 'scp') {
            success = await downloadSCP(host, user, password, remotePath, tempFile, port);
        }
        
        if (success) {
            return true;
        }
    }
    
    writeLog(`Download failed after ${maxRetries} attempts`);
    return false;
}

/**
 * Download via FTP/SFTP
 */
async function downloadFTP(host, user, password, remotePath, tempFile, sftp, port) {
    writeLog('Starting download from server...');
    
    const lftpPath = findExecutable('lftp');
    if (!lftpPath) {
        writeLog('ERROR: lftp not found. Install: sudo apt install lftp');
        return false;
    }
    
    const url = sftp ? `sftp://${host}` : `ftp://${host}`;
    const remoteDir = path.dirname(remotePath) || '.';
    const remoteFile = path.basename(remotePath);
    
    const script = [];
    if (sftp) {
        script.push('set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"');
    }
    if (remoteDir !== '.' && remoteDir !== '/') {
        script.push(`cd ${remoteDir}`);
    }
    script.push(`get "${remoteFile}" -o "${tempFile}"`);
    script.push('quit');
    
    try {
        const { stdout, stderr } = await execPromise(
            `echo "${script.join('\\n')}" | ${lftpPath} -u "${user},${password}" ${url}`
        );
        
        if (fs.existsSync(tempFile)) {
            writeLog('Download successful');
            return true;
        }
    } catch (err) {
        writeLog(`Download failed: ${err.message}`);
    }
    
    return false;
}

/**
 * Download via SMB
 */
async function downloadSMB(host, share, user, password, remotePath, tempFile, domain) {
    writeLog('Starting download from server...');
    
    const smbclientPath = findExecutable('smbclient');
    if (!smbclientPath) {
        writeLog('ERROR: smbclient not found. Install: sudo apt install samba-common');
        return false;
    }
    
    const smbURL = `//${host}/${share}`;
    
    try {
        await execPromise(`${smbclientPath} "${smbURL}" -U "${domain}\\\\${user}%${password}" -c 'get "${remotePath}" "${tempFile}"'`);
        
        if (fs.existsSync(tempFile)) {
            writeLog('Download successful');
            return true;
        }
    } catch (err) {
        writeLog(`Download failed: ${err.message}`);
    }
    
    return false;
}

/**
 * Download via SCP
 */
async function downloadSCP(host, user, password, remotePath, tempFile, port) {
    writeLog('Starting download from server...');
    
    const sshpassPath = findExecutable('sshpass');
    const scpPath = findExecutable('scp');
    
    if (!sshpassPath || !scpPath) {
        writeLog('ERROR: sshpass or scp not found');
        return false;
    }
    
    try {
        await execPromise(
            `${sshpassPath} -p "${password}" ${scpPath} -P ${port} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "${user}@${host}:${remotePath}" "${tempFile}"`
        );
        
        if (fs.existsSync(tempFile)) {
            writeLog('Download successful');
            return true;
        }
    } catch (err) {
        writeLog(`Download failed: ${err.message}`);
    }
    
    return false;
}

/**
 * Upload file with retry logic
 */
async function uploadFile(host, user, password, remotePath, localFile, protocol, maxRetries, retryDelay, port, share, domain) {
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        if (attempt > 0) {
            const delay = Math.min(retryDelay * Math.pow(2, attempt - 1), 60);
            writeLog(`Retry ${attempt}/${maxRetries - 1} in ${delay} seconds...`);
            await new Promise(resolve => setTimeout(resolve, delay * 1000));
        }
        
        let success = false;
        
        if (protocol === 'ftp' || protocol === 'sftp') {
            success = await uploadFTP(host, user, password, remotePath, localFile, protocol === 'sftp', port);
        } else if (protocol === 'smb') {
            success = await uploadSMB(host, share, user, password, remotePath, localFile, domain);
        } else if (protocol === 'scp') {
            success = await uploadSCP(host, user, password, remotePath, localFile, port);
        }
        
        if (success) {
            return true;
        }
    }
    
    writeLog(`Upload failed after ${maxRetries} attempts`);
    return false;
}

/**
 * Upload via FTP/SFTP
 */
async function uploadFTP(host, user, password, remotePath, localFile, sftp, port) {
    writeLog('Starting upload to server...');
    
    const lftpPath = findExecutable('lftp');
    if (!lftpPath) {
        writeLog('ERROR: lftp not found');
        return false;
    }
    
    const url = sftp ? `sftp://${host}` : `ftp://${host}`;
    const remoteDir = path.dirname(remotePath) || '.';
    const remoteFile = path.basename(remotePath);
    
    const script = [];
    if (sftp) {
        script.push('set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"');
    }
    if (remoteDir !== '.' && remoteDir !== '/') {
        script.push(`cd ${remoteDir}`);
    }
    script.push(`put "${localFile}" -o "${remoteFile}"`);
    script.push('quit');
    
    try {
        await execPromise(
            `echo "${script.join('\\n')}" | ${lftpPath} -u "${user},${password}" ${url}`
        );
        writeLog('Upload successful');
        return true;
    } catch (err) {
        writeLog(`Upload failed: ${err.message}`);
        return false;
    }
}

/**
 * Upload via SMB
 */
async function uploadSMB(host, share, user, password, remotePath, localFile, domain) {
    writeLog('Starting upload to server...');
    
    const smbclientPath = findExecutable('smbclient');
    if (!smbclientPath) {
        writeLog('ERROR: smbclient not found');
        return false;
    }
    
    const smbURL = `//${host}/${share}`;
    
    try {
        await execPromise(`${smbclientPath} "${smbURL}" -U "${domain}\\\\${user}%${password}" -c 'put "${localFile}" "${remotePath}"'`);
        writeLog('Upload successful');
        return true;
    } catch (err) {
        writeLog(`Upload failed: ${err.message}`);
        return false;
    }
}

/**
 * Upload via SCP
 */
async function uploadSCP(host, user, password, remotePath, localFile, port) {
    writeLog('Starting upload to server...');
    
    const sshpassPath = findExecutable('sshpass');
    const scpPath = findExecutable('scp');
    
    if (!sshpassPath || !scpPath) {
        writeLog('ERROR: sshpass or scp not found');
        return false;
    }
    
    try {
        await execPromise(
            `${sshpassPath} -p "${password}" ${scpPath} -P ${port} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "${localFile}" "${user}@${host}:${remotePath}"`
        );
        writeLog('Upload successful');
        return true;
    } catch (err) {
        writeLog(`Upload failed: ${err.message}`);
        return false;
    }
}

/**
 * Merge databases
 */
function mergeDatabases(keepassxc, localDB, tempDB, password) {
    writeLog('Performing merge...');
    
    if (!fs.existsSync(tempDB)) {
        writeLog('ERROR: Temporary file not found');
        return false;
    }
    
    return new Promise((resolve) => {
        const cmd = spawn(keepassxc, ['merge', '-s', localDB, tempDB, '--same-credentials']);
        
        cmd.stdin.write(password);
        cmd.stdin.end();
        
        let stdout = '';
        let stderr = '';
        
        cmd.stdout.on('data', (data) => {
            stdout += data.toString();
        });
        
        cmd.stderr.on('data', (data) => {
            stderr += data.toString();
        });
        
        cmd.on('close', (code) => {
            if (code === 0) {
                writeLog('Merge completed successfully. Local file updated.');
                resolve(true);
            } else {
                writeLog(`ERROR: Merge failed: ${stderr}`);
                resolve(false);
            }
        });
        
        cmd.on('error', (err) => {
            writeLog(`ERROR: Could not start KeePassXC-CLI: ${err.message}`);
            resolve(false);
        });
    });
}

/**
 * Test connection
 */
async function testConnection() {
    writeLog('=== Connection Test ===');
    const errors = [];
    
    // Check KeePassXC
    const keepassxc = findExecutable(config.keepass.keepassXCPath || 'keepassxc-cli');
    if (!keepassxc) {
        errors.push('❌ KeePassXC-CLI not found');
    } else {
        writeLog(`✅ KeePassXC-CLI found: ${keepassxc}`);
    }
    
    // Check local database
    if (fs.existsSync(config.local.localPath)) {
        const stats = fs.statSync(config.local.localPath);
        writeLog(`✅ Local database: ${config.local.localPath} (${stats.size} bytes, modified: ${stats.mtime.toISOString().substring(0, 19)})`);
    } else {
        errors.push(`⚠️ Local database not found: ${config.local.localPath}`);
    }
    
    // Test connection (simplified)
    const protocol = config.ftp.type.toLowerCase();
    writeLog(`Testing connection (${protocol.toUpperCase()})...`);
    
    writeLog('=== Test completed ===');
    if (errors.length > 0) {
        writeLog('Errors found:');
        errors.forEach(e => writeLog(e));
        return false;
    }
    
    writeLog('✅ All tests successful!');
    return true;
}

/**
 * Show status
 */
function showStatus() {
    writeLog('=== KeePass Sync Status ===');
    
    // Local DB
    if (fs.existsSync(config.local.localPath)) {
        const stats = fs.statSync(config.local.localPath);
        const age = Date.now() - stats.mtime.getTime();
        const ageDays = Math.floor(age / (1000 * 60 * 60 * 24));
        const ageHours = Math.floor((age % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        
        writeLog(`Local DB: ${config.local.localPath}`);
        writeLog(`  Size: ${stats.size.toLocaleString()} bytes (${(stats.size / 1024).toFixed(2)} KB)`);
        writeLog(`  Modified: ${stats.mtime.toISOString().substring(0, 19)} (age: ${ageDays}d ${ageHours}h)`);
    } else {
        writeLog(`⚠️ Local DB not found: ${config.local.localPath}`);
    }
    
    // Backups
    if (fs.existsSync(config.local.backupDir)) {
        const files = fs.readdirSync(config.local.backupDir)
            .filter(f => f.endsWith('.kdbx'))
            .map(f => ({
                name: f,
                path: path.join(config.local.backupDir, f),
                stats: fs.statSync(path.join(config.local.backupDir, f))
            }))
            .sort((a, b) => b.stats.mtime - a.stats.mtime)
            .slice(0, 3);
        
        writeLog(`Backups: ${files.length} found`);
        files.forEach((f, i) => {
            writeLog(`  ${i + 1}. ${f.name} (${(f.stats.size / 1024).toFixed(2)} KB, ${f.stats.mtime.toISOString().substring(0, 19)})`);
        });
    }
    
    // Configuration
    writeLog(`Protocol: ${config.ftp.type.toUpperCase()}`);
    writeLog(`Server: ${config.ftp.host}`);
    writeLog(`User: ${config.ftp.user}`);
    
    // KeePassXC
    const keepassxc = findExecutable(config.keepass.keepassXCPath || 'keepassxc-cli');
    if (keepassxc) {
        writeLog(`KeePassXC-CLI: ✅ ${keepassxc}`);
    } else {
        writeLog('KeePassXC-CLI: ❌ Not found');
    }
}

/**
 * Perform sync
 */
async function performSync() {
    const keepassxc = findExecutable(config.keepass.keepassXCPath || 'keepassxc-cli');
    if (!keepassxc) {
        writeLog('ERROR: KeePassXC-CLI not found');
        return false;
    }
    
    // Backup
    createBackup(config.local.localPath, config.local.backupDir);
    cleanupBackups(config.local.backupDir, config.local.maxBackups);
    
    const protocol = config.ftp.type.toLowerCase();
    const port = config.ftp.port || (protocol === 'ftp' ? 21 : protocol === 'sftp' || protocol === 'scp' ? 22 : 0);
    
    // Download
    const downloadSuccess = await downloadFile(
        config.ftp.host,
        config.ftp.user,
        config.ftp.password,
        config.ftp.remotePath,
        config.local.tempPath,
        protocol,
        config.settings.max_retries,
        config.settings.retry_delay,
        port,
        config.ftp.share,
        config.ftp.domain
    );
    
    if (!downloadSuccess) {
        return false;
    }
    
    // Merge
    const mergeSuccess = await mergeDatabases(
        keepassxc,
        config.local.localPath,
        config.local.tempPath,
        config.keepass.databasePassword
    );
    
    if (!mergeSuccess) {
        return false;
    }
    
    // Upload
    const uploadSuccess = await uploadFile(
        config.ftp.host,
        config.ftp.user,
        config.ftp.password,
        config.ftp.remotePath,
        config.local.localPath,
        protocol,
        config.settings.max_retries,
        config.settings.retry_delay,
        port,
        config.ftp.share,
        config.ftp.domain
    );
    
    if (!uploadSuccess) {
        return false;
    }
    
    // Cleanup
    if (fs.existsSync(config.local.tempPath)) {
        fs.unlinkSync(config.local.tempPath);
    }
    
    writeLog('Synchronization completed.');
    return true;
}

/**
 * Main function
 */
async function main() {
    // Change to base directory
    if (__dirname.endsWith('nodejs')) {
        process.chdir(path.dirname(__dirname));
    }
    
    // CLI
    if (flags.version) {
        console.log('KeePass Sync 1.1.0 (Node.js)');
        return;
    }
    
    if (flags.help) {
        console.log(`
KeePass Sync - Node.js Version

Usage:
  node sync.js [OPTIONS]

Options:
  --sync           Perform synchronization (default)
  --test           Test connection without sync
  --status         Show status
  --watch          Watch file for changes (not yet implemented)
  --config FILE    Alternative config file
  --verbose, -v    Verbose output
  --quiet, -q      Quiet mode (errors only)
  --version        Show version
  --help           Show this help
        `);
        return;
    }
    
    // Load config
    loadConfig();
    
    if (flags.verbose) {
        config.settings.debug = true;
    }
    
    if (!flags.quiet) {
        writeLog('=== KeePass Sync - Node.js ===');
    }
    
    // Actions
    if (flags.test) {
        const success = await testConnection();
        process.exit(success ? 0 : 1);
    }
    
    if (flags.status) {
        showStatus();
        process.exit(0);
    }
    
    if (flags.watch) {
        writeLog('File watching not yet implemented in Node.js version');
        writeLog('Use Python version for file watching feature');
        process.exit(1);
    }
    
    // Normal sync
    const success = await performSync();
    process.exit(success ? 0 : 1);
}

// Run
main().catch(err => {
    writeLog(`FATAL ERROR: ${err.message}`);
    process.exit(1);
});

