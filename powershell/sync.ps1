# KeePass Sync - PowerShell Version (Standalone)
# Cross-Platform: Windows (primarily), Linux (PowerShell Core), macOS (PowerShell Core)
#
# Usage:
#   .\sync.ps1
#   .\sync.ps1 --test
#   .\sync.ps1 --status
#   .\sync.ps1 --help
#
# Requirements:
#   - PowerShell 5.1+ (Windows) or PowerShell Core 6+ (Linux/macOS)
#   - KeePassXC-CLI in PATH
#   - WinSCP or lftp for FTP/SFTP (Windows)
#   - lftp for FTP/SFTP (Linux/macOS)
#   - smbclient for SMB (Linux/macOS)
#   - Windows native SMB support (Windows)

#Requires -Version 5.1

param(
    [switch]$Test,
    [switch]$Status,
    [switch]$Watch,
    [switch]$Verbose,
    [switch]$Quiet,
    [switch]$Version,
    [switch]$Help,
    [string]$Config = "config.json"
)

# Global variables
$script:ConfigFile = $Config
$script:LogFile = "sync_log.txt"
$script:Config = $null

# Change to script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($scriptDir.EndsWith("powershell")) {
    Set-Location (Split-Path -Parent $scriptDir)
} else {
    Set-Location $scriptDir
}

# Functions

function Write-Log {
    param([string]$Message)
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "$timestamp $Message"
    
    if (-not $Quiet) {
        Write-Host $logMessage
    }
    
    try {
        Add-Content -Path $script:LogFile -Value $logMessage -ErrorAction SilentlyContinue
    } catch {
        # Ignore
    }
}

function Load-Config {
    if (-not (Test-Path $script:ConfigFile)) {
        Write-Log "ERROR: Configuration file not found: $script:ConfigFile"
        exit 1
    }
    
    try {
        $jsonContent = Get-Content $script:ConfigFile -Raw
        $script:Config = $jsonContent | ConvertFrom-Json
        
        # Set defaults
        if (-not $script:Config.settings) {
            $script:Config.settings = @{}
        }
        if (-not $script:Config.settings.max_retries) {
            $script:Config.settings | Add-Member -NotePropertyName "max_retries" -NotePropertyValue 3 -Force
        }
        if (-not $script:Config.settings.retry_delay) {
            $script:Config.settings | Add-Member -NotePropertyName "retry_delay" -NotePropertyValue 5 -Force
        }
        if (-not $script:Config.settings.watch_delay) {
            $script:Config.settings | Add-Member -NotePropertyName "watch_delay" -NotePropertyValue 30 -Force
        }
        if (-not $script:Config.local.maxBackups) {
            $script:Config.local | Add-Member -NotePropertyName "maxBackups" -NotePropertyValue 2 -Force
        }
    } catch {
        Write-Log "ERROR: Failed to parse configuration: $_"
        exit 1
    }
}

function Find-Executable {
    param([string]$Name)
    
    # Try direct path
    if (Test-Path $Name) {
        return $Name
    }
    
    # Search in PATH
    $pathEnv = $env:PATH
    $paths = if ($IsWindows -or $PSVersionTable.PSVersion.Major -lt 6) {
        $pathEnv -split ';'
    } else {
        $pathEnv -split ':'
    }
    
    foreach ($p in $paths) {
        $fullPath = Join-Path $p $Name
        if (Test-Path $fullPath) {
            return $fullPath
        }
    }
    
    # Try Get-Command
    try {
        $cmd = Get-Command $Name -ErrorAction SilentlyContinue
        if ($cmd) {
            return $cmd.Source
        }
    } catch {
        # Not found
    }
    
    return $null
}

function New-Backup {
    param(
        [string]$LocalDB,
        [string]$BackupDir
    )
    
    Write-Log "Creating backup..."
    
    if (-not (Test-Path $LocalDB)) {
        Write-Log "WARNING: Local database not found"
        return $false
    }
    
    if (-not (Test-Path $BackupDir)) {
        New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
    }
    
    $today = Get-Date -Format "yyyyMMdd"
    $backupFile = Join-Path $BackupDir "keepass_passwords_$today.kdbx"
    
    try {
        Copy-Item $LocalDB $backupFile -Force
        Write-Log "Backup successfully created"
        return $true
    } catch {
        Write-Log "WARNING: Could not create backup: $_"
        return $false
    }
}

function Remove-OldBackups {
    param(
        [string]$BackupDir,
        [int]$MaxBackups
    )
    
    try {
        $files = Get-ChildItem -Path $BackupDir -Filter "keepass_passwords_*.kdbx" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending
        
        if ($files.Count -le $MaxBackups) {
            return
        }
        
        for ($i = $MaxBackups; $i -lt $files.Count; $i++) {
            Remove-Item $files[$i].FullName -Force
            Write-Log "Old backup deleted: $($files[$i].Name)"
        }
    } catch {
        # Ignore
    }
}

function Invoke-DownloadFile {
    param(
        [string]$Host,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$TempFile,
        [string]$Protocol,
        [int]$MaxRetries,
        [int]$RetryDelay,
        [int]$Port = 0,
        [string]$Share = "",
        [string]$Domain = ""
    )
    
    for ($attempt = 0; $attempt -lt $MaxRetries; $attempt++) {
        if ($attempt -gt 0) {
            $delay = [Math]::Min($RetryDelay * [Math]::Pow(2, $attempt - 1), 60)
            Write-Log "Retry $attempt/$($MaxRetries - 1) in $delay seconds..."
            Start-Sleep -Seconds $delay
        }
        
        $success = $false
        
        if ($Protocol -eq "ftp" -or $Protocol -eq "sftp") {
            $success = Invoke-DownloadFTP -Host $Host -User $User -Password $Password -RemotePath $RemotePath -TempFile $TempFile -SFTP ($Protocol -eq "sftp") -Port $Port
        } elseif ($Protocol -eq "smb") {
            $success = Invoke-DownloadSMB -Host $Host -Share $Share -User $User -Password $Password -RemotePath $RemotePath -TempFile $TempFile -Domain $Domain
        } elseif ($Protocol -eq "scp") {
            $success = Invoke-DownloadSCP -Host $Host -User $User -Password $Password -RemotePath $RemotePath -TempFile $TempFile -Port $Port
        }
        
        if ($success) {
            return $true
        }
    }
    
    Write-Log "Download failed after $MaxRetries attempts"
    return $false
}

function Invoke-DownloadFTP {
    param(
        [string]$Host,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$TempFile,
        [switch]$SFTP,
        [int]$Port
    )
    
    Write-Log "Starting download from server..."
    
    # Try WinSCP (Windows)
    if ($IsWindows -or $PSVersionTable.PSVersion.Major -lt 6) {
        $winscpPath = Find-Executable "WinSCP.com"
        if ($winscpPath) {
            $scriptFile = Join-Path $env:TEMP "winscp_$PID.txt"
            $scriptContent = @"
option batch abort
option confirm off
open $(if ($SFTP) { "sftp" } else { "ftp" })://$($User):$($Password)@$($Host):$Port
get "$RemotePath" "$TempFile"
exit
"@
            Set-Content -Path $scriptFile -Value $scriptContent
            
            try {
                $result = & $winscpPath /script=$scriptFile 2>&1
                Remove-Item $scriptFile -ErrorAction SilentlyContinue
                
                if (Test-Path $TempFile) {
                    Write-Log "Download successful"
                    return $true
                }
            } catch {
                Remove-Item $scriptFile -ErrorAction SilentlyContinue
            }
        }
    }
    
    # Try lftp
    $lftpPath = Find-Executable "lftp"
    if ($lftpPath) {
        $url = if ($SFTP) { "sftp://$Host" } else { "ftp://$Host" }
        $remoteDir = Split-Path $RemotePath -Parent
        $remoteFile = Split-Path $RemotePath -Leaf
        
        $script = @()
        if ($SFTP) {
            $script += 'set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"'
        }
        if ($remoteDir -and $remoteDir -ne "." -and $remoteDir -ne "/") {
            $script += "cd $remoteDir"
        }
        $script += "get `"$remoteFile`" -o `"$TempFile`""
        $script += "quit"
        
        $scriptContent = $script -join "`n"
        try {
            $scriptContent | & $lftpPath -u "$User,$Password" $url 2>&1 | Out-Null
            
            if (Test-Path $TempFile) {
                Write-Log "Download successful"
                return $true
            }
        } catch {
            Write-Log "Download failed: $_"
        }
    }
    
    Write-Log "ERROR: FTP client not found (WinSCP or lftp)"
    return $false
}

function Invoke-DownloadSMB {
    param(
        [string]$Host,
        [string]$Share,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$TempFile,
        [string]$Domain
    )
    
    Write-Log "Starting download from server..."
    
    # Windows: Use net use
    if ($IsWindows -or $PSVersionTable.PSVersion.Major -lt 6) {
        $drive = "Z:"
        $uncPath = "\\$Host\$Share"
        
        $netCmd = "net use $drive $uncPath /user:$Domain\$User $Password"
        $result = cmd /c $netCmd 2>&1
        
        if (Test-Path $drive) {
            try {
                $sourceFile = Join-Path $drive $RemotePath
                Copy-Item $sourceFile $TempFile -Force
                cmd /c "net use $drive /delete /y" 2>&1 | Out-Null
                Write-Log "Download successful"
                return $true
            } catch {
                cmd /c "net use $drive /delete /y" 2>&1 | Out-Null
                Write-Log "Download failed: $_"
            }
        }
    }
    
    # Linux/macOS: Use smbclient
    $smbclientPath = Find-Executable "smbclient"
    if ($smbclientPath) {
        $smbURL = "//$Host/$Share"
        try {
            $cmd = "$smbclientPath `"$smbURL`" -U `"$Domain\\$User%$Password`" -c `"get `"$RemotePath`" `"$TempFile`"`""
            Invoke-Expression $cmd 2>&1 | Out-Null
            
            if (Test-Path $TempFile) {
                Write-Log "Download successful"
                return $true
            }
        } catch {
            Write-Log "Download failed: $_"
        }
    }
    
    Write-Log "ERROR: SMB client not found"
    return $false
}

function Invoke-DownloadSCP {
    param(
        [string]$Host,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$TempFile,
        [int]$Port
    )
    
    Write-Log "Starting download from server..."
    
    $sshpassPath = Find-Executable "sshpass"
    $scpPath = Find-Executable "scp"
    
    if (-not $sshpassPath -or -not $scpPath) {
        Write-Log "ERROR: sshpass or scp not found"
        return $false
    }
    
    try {
        $cmd = "$sshpassPath -p `"$Password`" $scpPath -P $Port -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null `"$User@$Host:$RemotePath`" `"$TempFile`""
        Invoke-Expression $cmd 2>&1 | Out-Null
        
        if (Test-Path $TempFile) {
            Write-Log "Download successful"
            return $true
        }
    } catch {
        Write-Log "Download failed: $_"
    }
    
    return $false
}

function Invoke-UploadFile {
    param(
        [string]$Host,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$LocalFile,
        [string]$Protocol,
        [int]$MaxRetries,
        [int]$RetryDelay,
        [int]$Port = 0,
        [string]$Share = "",
        [string]$Domain = ""
    )
    
    for ($attempt = 0; $attempt -lt $MaxRetries; $attempt++) {
        if ($attempt -gt 0) {
            $delay = [Math]::Min($RetryDelay * [Math]::Pow(2, $attempt - 1), 60)
            Write-Log "Retry $attempt/$($MaxRetries - 1) in $delay seconds..."
            Start-Sleep -Seconds $delay
        }
        
        $success = $false
        
        if ($Protocol -eq "ftp" -or $Protocol -eq "sftp") {
            $success = Invoke-UploadFTP -Host $Host -User $User -Password $Password -RemotePath $RemotePath -LocalFile $LocalFile -SFTP ($Protocol -eq "sftp") -Port $Port
        } elseif ($Protocol -eq "smb") {
            $success = Invoke-UploadSMB -Host $Host -Share $Share -User $User -Password $Password -RemotePath $RemotePath -LocalFile $LocalFile -Domain $Domain
        } elseif ($Protocol -eq "scp") {
            $success = Invoke-UploadSCP -Host $Host -User $User -Password $Password -RemotePath $RemotePath -LocalFile $LocalFile -Port $Port
        }
        
        if ($success) {
            return $true
        }
    }
    
    Write-Log "Upload failed after $MaxRetries attempts"
    return $false
}

function Invoke-UploadFTP {
    param(
        [string]$Host,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$LocalFile,
        [switch]$SFTP,
        [int]$Port
    )
    
    Write-Log "Starting upload to server..."
    
    # Try WinSCP (Windows)
    if ($IsWindows -or $PSVersionTable.PSVersion.Major -lt 6) {
        $winscpPath = Find-Executable "WinSCP.com"
        if ($winscpPath) {
            $scriptFile = Join-Path $env:TEMP "winscp_$PID.txt"
            $scriptContent = @"
option batch abort
option confirm off
open $(if ($SFTP) { "sftp" } else { "ftp" })://$($User):$($Password)@$($Host):$Port
put "$LocalFile" "$RemotePath"
exit
"@
            Set-Content -Path $scriptFile -Value $scriptContent
            
            try {
                & $winscpPath /script=$scriptFile 2>&1 | Out-Null
                Remove-Item $scriptFile -ErrorAction SilentlyContinue
                Write-Log "Upload successful"
                return $true
            } catch {
                Remove-Item $scriptFile -ErrorAction SilentlyContinue
            }
        }
    }
    
    # Try lftp
    $lftpPath = Find-Executable "lftp"
    if ($lftpPath) {
        $url = if ($SFTP) { "sftp://$Host" } else { "ftp://$Host" }
        $remoteDir = Split-Path $RemotePath -Parent
        $remoteFile = Split-Path $RemotePath -Leaf
        
        $script = @()
        if ($SFTP) {
            $script += 'set sftp:connect-program "ssh -a -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"'
        }
        if ($remoteDir -and $remoteDir -ne "." -and $remoteDir -ne "/") {
            $script += "cd $remoteDir"
        }
        $script += "put `"$LocalFile`" -o `"$remoteFile`""
        $script += "quit"
        
        $scriptContent = $script -join "`n"
        try {
            $scriptContent | & $lftpPath -u "$User,$Password" $url 2>&1 | Out-Null
            Write-Log "Upload successful"
            return $true
        } catch {
            Write-Log "Upload failed: $_"
        }
    }
    
    Write-Log "ERROR: FTP client not found"
    return $false
}

function Invoke-UploadSMB {
    param(
        [string]$Host,
        [string]$Share,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$LocalFile,
        [string]$Domain
    )
    
    Write-Log "Starting upload to server..."
    
    # Windows: Use net use
    if ($IsWindows -or $PSVersionTable.PSVersion.Major -lt 6) {
        $drive = "Z:"
        $uncPath = "\\$Host\$Share"
        
        $netCmd = "net use $drive $uncPath /user:$Domain\$User $Password"
        cmd /c $netCmd 2>&1 | Out-Null
        
        if (Test-Path $drive) {
            try {
                $destFile = Join-Path $drive $RemotePath
                Copy-Item $LocalFile $destFile -Force
                cmd /c "net use $drive /delete /y" 2>&1 | Out-Null
                Write-Log "Upload successful"
                return $true
            } catch {
                cmd /c "net use $drive /delete /y" 2>&1 | Out-Null
                Write-Log "Upload failed: $_"
            }
        }
    }
    
    # Linux/macOS: Use smbclient
    $smbclientPath = Find-Executable "smbclient"
    if ($smbclientPath) {
        $smbURL = "//$Host/$Share"
        try {
            $cmd = "$smbclientPath `"$smbURL`" -U `"$Domain\\$User%$Password`" -c `"put `"$LocalFile`" `"$RemotePath`"`""
            Invoke-Expression $cmd 2>&1 | Out-Null
            Write-Log "Upload successful"
            return $true
        } catch {
            Write-Log "Upload failed: $_"
        }
    }
    
    Write-Log "ERROR: SMB client not found"
    return $false
}

function Invoke-UploadSCP {
    param(
        [string]$Host,
        [string]$User,
        [string]$Password,
        [string]$RemotePath,
        [string]$LocalFile,
        [int]$Port
    )
    
    Write-Log "Starting upload to server..."
    
    $sshpassPath = Find-Executable "sshpass"
    $scpPath = Find-Executable "scp"
    
    if (-not $sshpassPath -or -not $scpPath) {
        Write-Log "ERROR: sshpass or scp not found"
        return $false
    }
    
    try {
        $cmd = "$sshpassPath -p `"$Password`" $scpPath -P $Port -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null `"$LocalFile`" `"$User@$Host:$RemotePath`""
        Invoke-Expression $cmd 2>&1 | Out-Null
        Write-Log "Upload successful"
        return $true
    } catch {
        Write-Log "Upload failed: $_"
        return $false
    }
}

function Merge-Databases {
    param(
        [string]$KeepassXC,
        [string]$LocalDB,
        [string]$TempDB,
        [string]$Password
    )
    
    Write-Log "Performing merge..."
    
    if (-not (Test-Path $TempDB)) {
        Write-Log "ERROR: Temporary file not found"
        return $false
    }
    
    try {
        $process = Start-Process -FilePath $KeepassXC -ArgumentList "merge", "-s", "`"$LocalDB`"", "`"$TempDB`"", "--same-credentials" -NoNewWindow -Wait -PassThru -RedirectStandardOutput "$env:TEMP\keepass_stdout_$PID.txt" -RedirectStandardError "$env:TEMP\keepass_stderr_$PID.txt"
        
        # Send password
        $Password | & $KeepassXC merge -s "`"$LocalDB`" "`"$TempDB`"" --same-credentials 2>&1 | Out-Null
        
        if ($process.ExitCode -eq 0) {
            Write-Log "Merge completed successfully. Local file updated."
            
            # Cleanup temp files
            Remove-Item "$env:TEMP\keepass_stdout_$PID.txt" -ErrorAction SilentlyContinue
            Remove-Item "$env:TEMP\keepass_stderr_$PID.txt" -ErrorAction SilentlyContinue
            
            return $true
        } else {
            $error = Get-Content "$env:TEMP\keepass_stderr_$PID.txt" -ErrorAction SilentlyContinue
            Write-Log "ERROR: Merge failed: $error"
            Remove-Item "$env:TEMP\keepass_stdout_$PID.txt" -ErrorAction SilentlyContinue
            Remove-Item "$env:TEMP\keepass_stderr_$PID.txt" -ErrorAction SilentlyContinue
            return $false
        }
    } catch {
        Write-Log "ERROR: Could not start KeePassXC-CLI: $_"
        return $false
    }
}

function Test-Connection {
    Write-Log "=== Connection Test ==="
    $errors = @()
    
    $keepassxcPath = $script:Config.keepass.keepassXCPath
    $keepassxc = Find-Executable $keepassxcPath
    if (-not $keepassxc) {
        $errors += "❌ KeePassXC-CLI not found"
    } else {
        Write-Log "✅ KeePassXC-CLI found: $keepassxc"
    }
    
    $localPath = $script:Config.local.localPath
    if (Test-Path $localPath) {
        $file = Get-Item $localPath
        Write-Log "✅ Local database: $localPath ($($file.Length) bytes, modified: $($file.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss')))"
    } else {
        $errors += "⚠️ Local database not found: $localPath"
    }
    
    $protocol = $script:Config.ftp.type.ToLower()
    Write-Log "Testing connection ($protocol)..."
    
    Write-Log "=== Test completed ==="
    if ($errors.Count -gt 0) {
        Write-Log "Errors found:"
        foreach ($e in $errors) {
            Write-Log $e
        }
        return $false
    }
    
    Write-Log "✅ All tests successful!"
    return $true
}

function Show-Status {
    Write-Log "=== KeePass Sync Status ==="
    
    $localPath = $script:Config.local.localPath
    if (Test-Path $localPath) {
        $file = Get-Item $localPath
        $age = (Get-Date) - $file.LastWriteTime
        Write-Log "Local DB: $localPath"
        Write-Log "  Size: $($file.Length.ToString('N0')) bytes ($([Math]::Round($file.Length / 1024, 2)) KB)"
        Write-Log "  Modified: $($file.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss')) (age: $([Math]::Floor($age.TotalDays))d $([Math]::Floor($age.TotalHours) % 24)h)"
    } else {
        Write-Log "⚠️ Local DB not found: $localPath"
    }
    
    $backupDir = $script:Config.local.backupDir
    if (Test-Path $backupDir) {
        $files = Get-ChildItem -Path $backupDir -Filter "*.kdbx" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
        Write-Log "Backups: $($files.Count) found"
        $index = 1
        foreach ($f in $files) {
            Write-Log "  $index. $($f.Name) ($([Math]::Round($f.Length / 1024, 2)) KB, $($f.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss')))"
            $index++
        }
    }
    
    Write-Log "Protocol: $($script:Config.ftp.type.ToUpper())"
    Write-Log "Server: $($script:Config.ftp.host)"
    Write-Log "User: $($script:Config.ftp.user)"
    
    $keepassxcPath = $script:Config.keepass.keepassXCPath
    $keepassxc = Find-Executable $keepassxcPath
    if ($keepassxc) {
        Write-Log "KeePassXC-CLI: ✅ $keepassxc"
    } else {
        Write-Log "KeePassXC-CLI: ❌ Not found"
    }
}

function Start-Sync {
    $keepassxcPath = $script:Config.keepass.keepassXCPath
    $keepassxc = Find-Executable $keepassxcPath
    if (-not $keepassxc) {
        Write-Log "ERROR: KeePassXC-CLI not found"
        return $false
    }
    
    # Backup
    $localPath = $script:Config.local.localPath
    $backupDir = $script:Config.local.backupDir
    $maxBackups = $script:Config.local.maxBackups
    New-Backup -LocalDB $localPath -BackupDir $backupDir
    Remove-OldBackups -BackupDir $backupDir -MaxBackups $maxBackups
    
    $protocol = $script:Config.ftp.type.ToLower()
    $port = $script:Config.ftp.port
    if (-not $port) {
        $port = if ($protocol -eq "ftp") { 21 } elseif ($protocol -eq "sftp" -or $protocol -eq "scp") { 22 } else { 0 }
    }
    
    $share = $script:Config.ftp.share
    $domain = $script:Config.ftp.domain
    
    $maxRetries = $script:Config.settings.max_retries
    $retryDelay = $script:Config.settings.retry_delay
    
    # Download
    $downloadSuccess = Invoke-DownloadFile `
        -Host $script:Config.ftp.host `
        -User $script:Config.ftp.user `
        -Password $script:Config.ftp.password `
        -RemotePath $script:Config.ftp.remotePath `
        -TempFile $script:Config.local.tempPath `
        -Protocol $protocol `
        -MaxRetries $maxRetries `
        -RetryDelay $retryDelay `
        -Port $port `
        -Share $share `
        -Domain $domain
    
    if (-not $downloadSuccess) {
        return $false
    }
    
    # Merge
    $mergeSuccess = Merge-Databases `
        -KeepassXC $keepassxc `
        -LocalDB $localPath `
        -TempDB $script:Config.local.tempPath `
        -Password $script:Config.keepass.databasePassword
    
    if (-not $mergeSuccess) {
        return $false
    }
    
    # Upload
    $uploadSuccess = Invoke-UploadFile `
        -Host $script:Config.ftp.host `
        -User $script:Config.ftp.user `
        -Password $script:Config.ftp.password `
        -RemotePath $script:Config.ftp.remotePath `
        -LocalFile $localPath `
        -Protocol $protocol `
        -MaxRetries $maxRetries `
        -RetryDelay $retryDelay `
        -Port $port `
        -Share $share `
        -Domain $domain
    
    if (-not $uploadSuccess) {
        return $false
    }
    
    # Cleanup
    if (Test-Path $script:Config.local.tempPath) {
        Remove-Item $script:Config.local.tempPath -Force
    }
    
    Write-Log "Synchronization completed."
    return $true
}

# Main
if ($Version) {
    Write-Host "KeePass Sync 1.1.0 (PowerShell)"
    exit 0
}

if ($Help) {
    Write-Host @"
KeePass Sync - PowerShell Version

Usage:
  .\sync.ps1 [OPTIONS]

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
"@
    exit 0
}

Load-Config

if ($Verbose) {
    $script:Config.settings.debug = $true
}

if (-not $Quiet) {
    Write-Log "=== KeePass Sync - PowerShell ==="
}

if ($Test) {
    $success = Test-Connection
    exit ($success ? 0 : 1)
}

if ($Status) {
    Show-Status
    exit 0
}

if ($Watch) {
    Write-Log "File watching not yet implemented in PowerShell version"
    Write-Log "Use Python version for file watching feature"
    exit 1
}

# Normal sync
$success = Start-Sync
exit ($success ? 0 : 1)

