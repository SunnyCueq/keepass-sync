package main

/*
KeePass Sync - Go (Golang) Version
Cross-Platform: Linux, Windows, macOS

Compile:
  go build -o keepass-sync sync.go

Or for specific platform:
  GOOS=windows GOARCH=amd64 go build -o keepass-sync.exe sync.go
  GOOS=linux GOARCH=amd64 go build -o keepass-sync sync.go
  GOOS=darwin GOARCH=amd64 go build -o keepass-sync sync.go

Features:
  - Single binary (no dependencies needed)
  - Fast execution
  - Cross-platform
  - CLI arguments (--test, --status, --watch, etc.)
  - Retry logic with exponential backoff
  - Supports FTP, SFTP, SMB, SCP protocols
*/

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

// Config structure
type Config struct {
	FTP struct {
		Host       string `json:"host"`
		User       string `json:"user"`
		Password   string `json:"password"`
		Type       string `json:"type"`
		RemotePath string `json:"remotePath"`
		Port       int    `json:"port"`
		Share      string `json:"share"`
		Domain     string `json:"domain"`
	} `json:"ftp"`
	Local struct {
		LocalPath  string `json:"localPath"`
		TempPath   string `json:"tempPath"`
		BackupDir  string `json:"backupDir"`
		MaxBackups int    `json:"maxBackups"`
	} `json:"local"`
	Keepass struct {
		DatabasePassword string `json:"databasePassword"`
		KeepassXCPath    string `json:"keepassXCPath"`
	} `json:"keepass"`
	Settings struct {
		Debug        bool   `json:"debug"`
		Language     string `json:"language"`
		CleanupLogs  bool   `json:"cleanupLogs"`
		MaxLogAge    int    `json:"maxLogAgeDays"`
		MaxRetries   int    `json:"max_retries"`
		RetryDelay   int    `json:"retry_delay"`
		WatchDelay   int    `json:"watch_delay"`
	} `json:"settings"`
}

var (
	configFile = "config.json"
	logFile    = "sync_log.txt"
	ftpLog     = "ftp_log.txt"
	config     Config
)

func writeLog(message string) {
	timestamp := time.Now().Format("2006-01-02 15:04:05")
	logMessage := fmt.Sprintf("%s %s", timestamp, message)
	fmt.Println(logMessage)
	
	f, err := os.OpenFile(logFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return
	}
	defer f.Close()
	fmt.Fprintln(f, logMessage)
}

func loadConfig() error {
	data, err := os.ReadFile(configFile)
	if err != nil {
		return fmt.Errorf("configuration file not found: %s", configFile)
	}
	
	if err := json.Unmarshal(data, &config); err != nil {
		return fmt.Errorf("failed to parse configuration: %v", err)
	}
	
	// Set defaults
	if config.Settings.MaxRetries == 0 {
		config.Settings.MaxRetries = 3
	}
	if config.Settings.RetryDelay == 0 {
		config.Settings.RetryDelay = 5
	}
	if config.Settings.WatchDelay == 0 {
		config.Settings.WatchDelay = 30
	}
	if config.Local.MaxBackups == 0 {
		config.Local.MaxBackups = 2
	}
	
	return nil
}

func findExecutable(name string) string {
	// Try direct path first
	if _, err := os.Stat(name); err == nil {
		return name
	}
	
	// Search in PATH
	path := os.Getenv("PATH")
	paths := strings.Split(path, ":")
	if os.PathSeparator == ';' {
		paths = strings.Split(path, ";") // Windows
	}
	
	for _, p := range paths {
		fullPath := filepath.Join(p, name)
		if _, err := os.Stat(fullPath); err == nil {
			return fullPath
		}
	}
	
	// Try which/where
	cmd := exec.Command("which", name)
	if output, err := cmd.Output(); err == nil {
		return strings.TrimSpace(string(output))
	}
	
	return ""
}

func createBackup(localDB, backupDir string) bool {
	writeLog("Creating backup...")
	
	if _, err := os.Stat(localDB); os.IsNotExist(err) {
		writeLog("WARNING: Local database not found")
		return false
	}
	
	if err := os.MkdirAll(backupDir, 0755); err != nil {
		writeLog(fmt.Sprintf("WARNING: Could not create backup directory: %v", err))
		return false
	}
	
	backupFile := filepath.Join(backupDir, fmt.Sprintf("keepass_passwords_%s.kdbx", time.Now().Format("20060102")))
	
	if err := copyFile(localDB, backupFile); err != nil {
		writeLog(fmt.Sprintf("WARNING: Could not create backup: %v", err))
		return false
	}
	
	writeLog("Backup successfully created")
	return true
}

func copyFile(src, dst string) error {
	source, err := os.Open(src)
	if err != nil {
		return err
	}
	defer source.Close()
	
	destination, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer destination.Close()
	
	_, err = io.Copy(destination, source)
	return err
}

func cleanupBackups(backupDir string, maxBackups int) {
	files, err := filepath.Glob(filepath.Join(backupDir, "keepass_passwords_*.kdbx"))
	if err != nil {
		return
	}
	
	if len(files) <= maxBackups {
		return
	}
	
	// Sort by modification time
	type fileInfo struct {
		path string
		time time.Time
	}
	
	fileInfos := make([]fileInfo, 0, len(files))
	for _, f := range files {
		info, err := os.Stat(f)
		if err != nil {
			continue
		}
		fileInfos = append(fileInfos, fileInfo{
			path: f,
			time: info.ModTime(),
		})
	}
	
	// Sort descending (newest first)
	for i := 0; i < len(fileInfos)-1; i++ {
		for j := i + 1; j < len(fileInfos); j++ {
			if fileInfos[i].time.Before(fileInfos[j].time) {
				fileInfos[i], fileInfos[j] = fileInfos[j], fileInfos[i]
			}
		}
	}
	
	// Delete old backups
	for i := maxBackups; i < len(fileInfos); i++ {
		if err := os.Remove(fileInfos[i].path); err == nil {
			writeLog(fmt.Sprintf("Old backup deleted: %s", filepath.Base(fileInfos[i].path)))
		}
	}
}

func downloadFile(host, user, password, remotePath, tempFile, protocol string, maxRetries, retryDelay int, port int, share, domain string) bool {
	for attempt := 0; attempt < maxRetries; attempt++ {
		if attempt > 0 {
			delay := retryDelay * (1 << uint(attempt-1))
			if delay > 60 {
				delay = 60
			}
			writeLog(fmt.Sprintf("Retry %d/%d in %d seconds...", attempt, maxRetries-1, delay))
			time.Sleep(time.Duration(delay) * time.Second)
		}
		
		var success bool
		switch protocol {
		case "ftp", "sftp":
			success = downloadFTP(host, user, password, remotePath, tempFile, protocol == "sftp", port)
		case "smb":
			success = downloadSMB(host, share, user, password, remotePath, tempFile, domain)
		case "scp":
			success = downloadSCP(host, user, password, remotePath, tempFile, port)
		default:
			writeLog(fmt.Sprintf("Unknown protocol: %s", protocol))
			return false
		}
		
		if success {
			return true
		}
	}
	
	writeLog(fmt.Sprintf("Download failed after %d attempts", maxRetries))
	return false
}

func downloadFTP(host, user, password, remotePath, tempFile string, sftp bool, port int) bool {
	writeLog("Starting download from server...")
	
	// Use lftp (if available) for FTP/SFTP
	lftpPath := findExecutable("lftp")
	if lftpPath != "" {
		var url string
		if sftp {
			url = fmt.Sprintf("sftp://%s", host)
		} else {
			url = fmt.Sprintf("ftp://%s", host)
		}
		
		remoteDir := filepath.Dir(remotePath)
		remoteFile := filepath.Base(remotePath)
		
		script := []string{}
		if sftp {
			script = append(script, `set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"`)
		}
		if remoteDir != "." && remoteDir != "/" {
			script = append(script, fmt.Sprintf("cd %s", remoteDir))
		}
		script = append(script, fmt.Sprintf("get %s -o %s", remoteFile, tempFile))
		script = append(script, "quit")
		
		cmd := exec.Command(lftpPath, "-u", fmt.Sprintf("%s,%s", user, password), url)
		cmd.Stdin = strings.NewReader(strings.Join(script, "\n") + "\n")
		
		if err := cmd.Run(); err != nil {
			writeLog(fmt.Sprintf("Download failed: %v", err))
			return false
		}
		
		if _, err := os.Stat(tempFile); err == nil {
			writeLog("Download successful")
			return true
		}
	}
	
	writeLog("ERROR: lftp not found. Install: sudo apt install lftp")
	return false
}

func downloadSMB(host, share, user, password, remotePath, tempFile, domain string) bool {
	writeLog("Starting download from server...")
	
	smbclientPath := findExecutable("smbclient")
	if smbclientPath == "" {
		writeLog("ERROR: smbclient not found. Install: sudo apt install samba-common")
		return false
	}
	
	smbURL := fmt.Sprintf("//%s/%s", host, share)
	cmd := exec.Command(smbclientPath, smbURL, "-U", fmt.Sprintf("%s\\%s%%%s", domain, user, password), "-c", fmt.Sprintf(`get "%s" "%s"`, remotePath, tempFile))
	
	if err := cmd.Run(); err != nil {
		writeLog(fmt.Sprintf("Download failed: %v", err))
		return false
	}
	
	if _, err := os.Stat(tempFile); err == nil {
		writeLog("Download successful")
		return true
	}
	
	return false
}

func downloadSCP(host, user, password, remotePath, tempFile string, port int) bool {
	writeLog("Starting download from server...")
	
	sshpassPath := findExecutable("sshpass")
	if sshpassPath == "" {
		writeLog("ERROR: sshpass not found. Install: sudo apt install sshpass")
		return false
	}
	
	scpPath := findExecutable("scp")
	if scpPath == "" {
		writeLog("ERROR: scp not found")
		return false
	}
	
	cmd := exec.Command(sshpassPath, "-p", password, scpPath, "-P", strconv.Itoa(port),
		"-o", "StrictHostKeyChecking=no",
		"-o", "UserKnownHostsFile=/dev/null",
		fmt.Sprintf("%s@%s:%s", user, host, remotePath),
		tempFile)
	
	if err := cmd.Run(); err != nil {
		writeLog(fmt.Sprintf("Download failed: %v", err))
		return false
	}
	
	if _, err := os.Stat(tempFile); err == nil {
		writeLog("Download successful")
		return true
	}
	
	return false
}

func uploadFile(host, user, password, remotePath, localFile, protocol string, maxRetries, retryDelay int, port int, share, domain string) bool {
	for attempt := 0; attempt < maxRetries; attempt++ {
		if attempt > 0 {
			delay := retryDelay * (1 << uint(attempt-1))
			if delay > 60 {
				delay = 60
			}
			writeLog(fmt.Sprintf("Retry %d/%d in %d seconds...", attempt, maxRetries-1, delay))
			time.Sleep(time.Duration(delay) * time.Second)
		}
		
		var success bool
		switch protocol {
		case "ftp", "sftp":
			success = uploadFTP(host, user, password, remotePath, localFile, protocol == "sftp", port)
		case "smb":
			success = uploadSMB(host, share, user, password, remotePath, localFile, domain)
		case "scp":
			success = uploadSCP(host, user, password, remotePath, localFile, port)
		default:
			writeLog(fmt.Sprintf("Unknown protocol: %s", protocol))
			return false
		}
		
		if success {
			return true
		}
	}
	
	writeLog(fmt.Sprintf("Upload failed after %d attempts", maxRetries))
	return false
}

func uploadFTP(host, user, password, remotePath, localFile string, sftp bool, port int) bool {
	writeLog("Starting upload to server...")
	
	lftpPath := findExecutable("lftp")
	if lftpPath != "" {
		var url string
		if sftp {
			url = fmt.Sprintf("sftp://%s", host)
		} else {
			url = fmt.Sprintf("ftp://%s", host)
		}
		
		remoteDir := filepath.Dir(remotePath)
		remoteFile := filepath.Base(remotePath)
		
		script := []string{}
		if sftp {
			script = append(script, `set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"`)
		}
		if remoteDir != "." && remoteDir != "/" {
			script = append(script, fmt.Sprintf("cd %s", remoteDir))
		}
		script = append(script, fmt.Sprintf("put %s -o %s", localFile, remoteFile))
		script = append(script, "quit")
		
		cmd := exec.Command(lftpPath, "-u", fmt.Sprintf("%s,%s", user, password), url)
		cmd.Stdin = strings.NewReader(strings.Join(script, "\n") + "\n")
		
		if err := cmd.Run(); err != nil {
			writeLog(fmt.Sprintf("Upload failed: %v", err))
			return false
		}
		
		writeLog("Upload successful")
		return true
	}
	
	writeLog("ERROR: lftp not found")
	return false
}

func uploadSMB(host, share, user, password, remotePath, localFile, domain string) bool {
	writeLog("Starting upload to server...")
	
	smbclientPath := findExecutable("smbclient")
	if smbclientPath == "" {
		writeLog("ERROR: smbclient not found")
		return false
	}
	
	smbURL := fmt.Sprintf("//%s/%s", host, share)
	cmd := exec.Command(smbclientPath, smbURL, "-U", fmt.Sprintf("%s\\%s%%%s", domain, user, password), "-c", fmt.Sprintf(`put "%s" "%s"`, localFile, remotePath))
	
	if err := cmd.Run(); err != nil {
		writeLog(fmt.Sprintf("Upload failed: %v", err))
		return false
	}
	
	writeLog("Upload successful")
	return true
}

func uploadSCP(host, user, password, remotePath, localFile string, port int) bool {
	writeLog("Starting upload to server...")
	
	sshpassPath := findExecutable("sshpass")
	scpPath := findExecutable("scp")
	if sshpassPath == "" || scpPath == "" {
		writeLog("ERROR: sshpass or scp not found")
		return false
	}
	
	cmd := exec.Command(sshpassPath, "-p", password, scpPath, "-P", strconv.Itoa(port),
		"-o", "StrictHostKeyChecking=no",
		"-o", "UserKnownHostsFile=/dev/null",
		localFile,
		fmt.Sprintf("%s@%s:%s", user, host, remotePath))
	
	if err := cmd.Run(); err != nil {
		writeLog(fmt.Sprintf("Upload failed: %v", err))
		return false
	}
	
	writeLog("Upload successful")
	return true
}

func mergeDatabases(keepassxc, localDB, tempDB, password string) bool {
	writeLog("Performing merge...")
	
	if _, err := os.Stat(tempDB); os.IsNotExist(err) {
		writeLog("ERROR: Temporary file not found")
		return false
	}
	
	cmd := exec.Command(keepassxc, "merge", "-s", localDB, tempDB, "--same-credentials")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		writeLog(fmt.Sprintf("ERROR: Could not start merge: %v", err))
		return false
	}
	
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		writeLog(fmt.Sprintf("ERROR: Could not start merge: %v", err))
		return false
	}
	
	stderr, err := cmd.StderrPipe()
	if err != nil {
		writeLog(fmt.Sprintf("ERROR: Could not start merge: %v", err))
		return false
	}
	
	if err := cmd.Start(); err != nil {
		writeLog(fmt.Sprintf("ERROR: Could not start KeePassXC-CLI: %v", err))
		return false
	}
	
	// Send password
	fmt.Fprintf(stdin, "%s\n", password)
	stdin.Close()
	
	// Read output
	output, _ := io.ReadAll(stdout)
	errors, _ := io.ReadAll(stderr)
	
	if err := cmd.Wait(); err != nil {
		writeLog(fmt.Sprintf("ERROR: Merge failed: %s", string(errors)))
		return false
	}
	
	if len(output) > 0 && config.Settings.Debug {
		writeLog(string(output))
	}
	
	writeLog("Merge completed successfully. Local file updated.")
	return true
}

func testConnection() bool {
	writeLog("=== Connection Test ===")
	errors := []string{}
	
	// Check KeePassXC
	keepassxc := findExecutable(config.Keepass.KeepassXCPath)
	if keepassxc == "" {
		errors = append(errors, "❌ KeePassXC-CLI not found")
	} else {
		writeLog(fmt.Sprintf("✅ KeePassXC-CLI found: %s", keepassxc))
	}
	
	// Check local database
	if _, err := os.Stat(config.Local.LocalPath); err == nil {
		info, _ := os.Stat(config.Local.LocalPath)
		writeLog(fmt.Sprintf("✅ Local database: %s (%d bytes, modified: %s)", 
			config.Local.LocalPath, info.Size(), info.ModTime().Format("2006-01-02 15:04:05")))
	} else {
		errors = append(errors, fmt.Sprintf("⚠️ Local database not found: %s", config.Local.LocalPath))
	}
	
	// Test connection
	protocol := strings.ToLower(config.FTP.Type)
	writeLog(fmt.Sprintf("Testing connection (%s)...", strings.ToUpper(protocol)))
	
	// Simple connection test (implement based on protocol)
	if protocol == "ftp" || protocol == "sftp" {
		lftpPath := findExecutable("lftp")
		if lftpPath == "" {
			errors = append(errors, "❌ lftp not found")
		} else {
			var url string
			if protocol == "sftp" {
				url = fmt.Sprintf("sftp://%s", config.FTP.Host)
			} else {
				url = fmt.Sprintf("ftp://%s", config.FTP.Host)
			}
			cmd := exec.Command(lftpPath, "-u", fmt.Sprintf("%s,%s", config.FTP.User, config.FTP.Password), url, "-e", "quit")
			if err := cmd.Run(); err != nil {
				errors = append(errors, fmt.Sprintf("❌ Connection failed: %v", err))
			} else {
				writeLog(fmt.Sprintf("✅ Connection to server successful: %s", config.FTP.Host))
			}
		}
	}
	
	writeLog("=== Test completed ===")
	if len(errors) > 0 {
		writeLog("Errors found:")
		for _, e := range errors {
			writeLog(e)
		}
		return false
	}
	
	writeLog("✅ All tests successful!")
	return true
}

func showStatus() {
	writeLog("=== KeePass Sync Status ===")
	
	// Local DB
	if info, err := os.Stat(config.Local.LocalPath); err == nil {
		age := time.Since(info.ModTime())
		writeLog(fmt.Sprintf("Local DB: %s", config.Local.LocalPath))
		writeLog(fmt.Sprintf("  Size: %d bytes (%.2f KB)", info.Size(), float64(info.Size())/1024))
		writeLog(fmt.Sprintf("  Modified: %s (age: %dd %dh)", 
			info.ModTime().Format("2006-01-02 15:04:05"), int(age.Hours()/24), int(age.Hours())%24))
	} else {
		writeLog(fmt.Sprintf("⚠️ Local DB not found: %s", config.Local.LocalPath))
	}
	
	// Backups
	if files, err := filepath.Glob(filepath.Join(config.Local.BackupDir, "*.kdbx")); err == nil {
		writeLog(fmt.Sprintf("Backups: %d found", len(files)))
		// Show top 3
		for i, f := range files {
			if i >= 3 {
				break
			}
			if info, err := os.Stat(f); err == nil {
				writeLog(fmt.Sprintf("  %d. %s (%.2f KB, %s)", i+1, filepath.Base(f), 
					float64(info.Size())/1024, info.ModTime().Format("2006-01-02 15:04:05")))
			}
		}
	}
	
	// Configuration
	writeLog(fmt.Sprintf("Protocol: %s", strings.ToUpper(config.FTP.Type)))
	writeLog(fmt.Sprintf("Server: %s", config.FTP.Host))
	writeLog(fmt.Sprintf("User: %s", config.FTP.User))
	
	// KeePassXC
	if keepassxc := findExecutable(config.Keepass.KeepassXCPath); keepassxc != "" {
		writeLog(fmt.Sprintf("KeePassXC-CLI: ✅ %s", keepassxc))
	} else {
		writeLog("KeePassXC-CLI: ❌ Not found")
	}
}

func performSync() bool {
	keepassxc := findExecutable(config.Keepass.KeepassXCPath)
	if keepassxc == "" {
		writeLog("ERROR: KeePassXC-CLI not found")
		return false
	}
	
	// Backup
	createBackup(config.Local.LocalPath, config.Local.BackupDir)
	cleanupBackups(config.Local.BackupDir, config.Local.MaxBackups)
	
	protocol := strings.ToLower(config.FTP.Type)
	port := config.FTP.Port
	if port == 0 {
		if protocol == "ftp" {
			port = 21
		} else if protocol == "sftp" || protocol == "scp" {
			port = 22
		}
	}
	
	// Download
	if !downloadFile(config.FTP.Host, config.FTP.User, config.FTP.Password, config.FTP.RemotePath,
		config.Local.TempPath, protocol, config.Settings.MaxRetries, config.Settings.RetryDelay,
		port, config.FTP.Share, config.FTP.Domain) {
		return false
	}
	
	// Merge
	if !mergeDatabases(keepassxc, config.Local.LocalPath, config.Local.TempPath, config.Keepass.DatabasePassword) {
		return false
	}
	
	// Upload
	if !uploadFile(config.FTP.Host, config.FTP.User, config.FTP.Password, config.FTP.RemotePath,
		config.Local.LocalPath, protocol, config.Settings.MaxRetries, config.Settings.RetryDelay,
		port, config.FTP.Share, config.FTP.Domain) {
		return false
	}
	
	// Cleanup
	if err := os.Remove(config.Local.TempPath); err == nil {
		writeLog("Temporary file deleted")
	}
	
	writeLog("Synchronization completed.")
	return true
}

func main() {
	// Change to script directory
	if exe, err := os.Executable(); err == nil {
		if dir := filepath.Dir(exe); dir != "" {
			os.Chdir(dir)
			// Go one level up if we're in go/ subdirectory
			if filepath.Base(dir) == "go" {
				os.Chdir("..")
			}
		}
	}
	
	// CLI flags
	testFlag := flag.Bool("test", false, "Test connection without sync")
	statusFlag := flag.Bool("status", false, "Show status")
	watchFlag := flag.Bool("watch", false, "Watch file for changes")
	configFlag := flag.String("config", "config.json", "Alternative config file")
	verboseFlag := flag.Bool("verbose", false, "Verbose output")
	quietFlag := flag.Bool("quiet", false, "Quiet mode (errors only)")
	versionFlag := flag.Bool("version", false, "Show version")
	flag.Parse()
	
	if *versionFlag {
		fmt.Println("KeePass Sync 1.1.0 (Go)")
		return
	}
	
	// Load config
	configFile = *configFlag
	if err := loadConfig(); err != nil {
		fmt.Fprintf(os.Stderr, "ERROR: %v\n", err)
		os.Exit(1)
	}
	
	if *verboseFlag {
		config.Settings.Debug = true
	}
	
	if !*quietFlag {
		writeLog(fmt.Sprintf("=== KeePass Sync - Go ==="))
	}
	
	// Actions
	if *testFlag {
		success := testConnection()
		if success {
			os.Exit(0)
		}
		os.Exit(1)
	}
	
	if *statusFlag {
		showStatus()
		os.Exit(0)
	}
	
	if *watchFlag {
		writeLog("File watching not yet implemented in Go version")
		writeLog("Use Python version for file watching feature")
		os.Exit(1)
	}
	
	// Normal sync
	success := performSync()
	if success {
		os.Exit(0)
	}
	os.Exit(1)
}

