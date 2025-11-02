#cs
	KeePass Sync - AutoIt Version
	Platform: Windows only
	
	Compile:
	  AutoIt3 /in sync.au3 /out sync.exe
	  
	Requirements:
	  - AutoIt3 installed (https://www.autoitscript.com/site/autoit/downloads/)
	  - KeePassXC-CLI in PATH
	  - WinSCP or lftp for FTP/SFTP transfers
	  
	Features:
	  - Windows native (no Python/Node.js needed)
	  - GUI support possible
	  - CLI arguments (--test, --status, etc.)
	  - Retry logic with exponential backoff
	  - Supports FTP, SFTP protocols (SMB via Windows net use)
#ce

#include <JSON.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <StringConstants.au3>
#include <WinAPI.au3>
#include <Date.au3>

; Configuration
Global $g_configFile = "config.json"
Global $g_logFile = "sync_log.txt"
Global $g_config = Null

; CLI arguments
Global $g_flags = ObjCreate("Scripting.Dictionary")
$g_flags.Add("test", False)
$g_flags.Add("status", False)
$g_flags.Add("verbose", False)
$g_flags.Add("quiet", False)
$g_flags.Add("version", False)
$g_flags.Add("config", $g_configFile)

; Parse CLI arguments
For $i = 1 To $CmdLine[0]
	Switch StringLower($CmdLine[$i])
		Case "--test", "/test"
			$g_flags.Item("test") = True
		Case "--status", "/status"
			$g_flags.Item("status") = True
		Case "--verbose", "/verbose", "-v", "/v"
			$g_flags.Item("verbose") = True
		Case "--quiet", "/quiet", "-q", "/q"
			$g_flags.Item("quiet") = True
		Case "--version", "/version"
			$g_flags.Item("version") = True
		Case "--config", "/config"
			If $i + 1 <= $CmdLine[0] Then
				$g_configFile = $CmdLine[$i + 1]
				$g_flags.Item("config") = $g_configFile
				$i += 1
			EndIf
	EndSwitch
Next

; Change to script directory
Local $scriptDir = @ScriptDir
If StringInStr($scriptDir, "autoit") > 0 Then
	$scriptDir = StringRegExpReplace($scriptDir, "\\autoit.*", "")
EndIf
FileChangeDir($scriptDir)

; Main
If $g_flags.Item("version") Then
	ConsoleWrite("KeePass Sync 1.1.0 (AutoIt)" & @CRLF)
	Exit
EndIf

LoadConfig()

If Not $g_flags.Item("quiet") Then
	WriteLog("=== KeePass Sync - AutoIt (Windows) ===")
EndIf

If $g_flags.Item("test") Then
	Local $success = TestConnection()
	Exit ($success ? 0 : 1)
EndIf

If $g_flags.Item("status") Then
	ShowStatus()
	Exit 0
EndIf

; Normal sync
Local $success = PerformSync()
Exit ($success ? 0 : 1)

; Functions

Func WriteLog($message)
	Local $timestamp = _NowCalc()
	$timestamp = StringRegExpReplace($timestamp, "(\d{4})/(\d{2})/(\d{2})\s+(\d{2}):(\d{2}):(\d{2})", "$1-$2-$3 $4:$5:$6")
	Local $logMessage = $timestamp & " " & $message
	
	If Not $g_flags.Item("quiet") Then
		ConsoleWrite($logMessage & @CRLF)
	EndIf
	
	Local $hFile = FileOpen($g_logFile, $FO_APPEND + $FO_CREATEPATH)
	If $hFile <> -1 Then
		FileWriteLine($hFile, $logMessage)
		FileClose($hFile)
	EndIf
EndFunc

Func LoadConfig()
	If Not FileExists($g_configFile) Then
		WriteLog("ERROR: Configuration file not found: " & $g_configFile)
		Exit 1
	EndIf
	
	Local $jsonContent = FileRead($g_configFile)
	$g_config = Json_Decode($jsonContent)
	
	If @error Or Not IsObj($g_config) Then
		WriteLog("ERROR: Failed to parse configuration")
		Exit 1
	EndIf
	
	; Set defaults
	If Not Json_Get($g_config, ".settings.max_retries") Then
		Json_Put($g_config, ".settings.max_retries", 3)
	EndIf
	If Not Json_Get($g_config, ".settings.retry_delay") Then
		Json_Put($g_config, ".settings.retry_delay", 5)
	EndIf
EndFunc

Func FindExecutable($name)
	; Try direct path
	If FileExists($name) Then
		Return $name
	EndIf
	
	; Search in PATH
	Local $pathEnv = EnvGet("PATH")
	Local $paths = StringSplit($pathEnv, ";")
	
	For $i = 1 To $paths[0]
		Local $fullPath = $paths[$i] & "\" & $name
		If FileExists($fullPath) Then
			Return $fullPath
		EndIf
	Next
	
	; Try which/where
	Local $output = RunWait(@ComSpec & " /c where " & $name, "", @SW_HIDE, $STDERR_CHILD + $STDOUT_CHILD)
	Local $stdout = ""
	If ProcessWaitClose($output) Then
		$stdout = StdoutRead($output)
		If $stdout <> "" Then
			Return StringStripWS($stdout, $STR_STRIPALL)
		EndIf
	EndIf
	
	Return ""
EndFunc

Func CreateBackup($localDB, $backupDir)
	WriteLog("Creating backup...")
	
	If Not FileExists($localDB) Then
		WriteLog("WARNING: Local database not found")
		Return False
	EndIf
	
	If Not DirCreate($backupDir) And @error Then
		WriteLog("WARNING: Could not create backup directory")
		Return False
	EndIf
	
	Local $today = StringFormat("%04d%02d%02d", @YEAR, @MON, @MDAY)
	Local $backupFile = $backupDir & "\keepass_passwords_" & $today & ".kdbx"
	
	If FileCopy($localDB, $backupFile, $FC_OVERWRITE) Then
		WriteLog("Backup successfully created")
		Return True
	Else
		WriteLog("WARNING: Could not create backup")
		Return False
	EndIf
EndFunc

Func CleanupBackups($backupDir, $maxBackups)
	Local $files = _FileListToArray($backupDir, "keepass_passwords_*.kdbx", $FLTA_FILES)
	If @error Then Return
	
	If $files[0] <= $maxBackups Then Return
	
	; Sort by modification time
	Local $fileTimes[UBound($files)][2]
	For $i = 1 To $files[0]
		Local $filePath = $backupDir & "\" & $files[$i]
		$fileTimes[$i][0] = $filePath
		$fileTimes[$i][1] = FileGetTime($filePath, $FT_MODIFIED, $FT_ARRAY)
	Next
	
	; Simple bubble sort (newest first)
	For $i = 1 To $files[0] - 1
		For $j = $i + 1 To $files[0]
			If CompareFileTimes($fileTimes[$i][1], $fileTimes[$j][1]) < 0 Then
				Local $temp1 = $fileTimes[$i][0]
				Local $temp2 = $fileTimes[$i][1]
				$fileTimes[$i][0] = $fileTimes[$j][0]
				$fileTimes[$i][1] = $fileTimes[$j][1]
				$fileTimes[$j][0] = $temp1
				$fileTimes[$j][1] = $temp2
			EndIf
		Next
	Next
	
	; Delete old backups
	For $i = $maxBackups + 1 To $files[0]
		If FileDelete($fileTimes[$i][0]) Then
			WriteLog("Old backup deleted: " & StringRegExpReplace($fileTimes[$i][0], ".*\\", ""))
		EndIf
	Next
EndFunc

Func CompareFileTimes($time1, $time2)
	; Compare arrays: [0]=Year, [1]=Month, [2]=Day, [3]=Hour, [4]=Minute, [5]=Second
	For $i = 0 To 5
		If $time1[$i] < $time2[$i] Then Return -1
		If $time1[$i] > $time2[$i] Then Return 1
	Next
	Return 0
EndFunc

Func DownloadFile($host, $user, $password, $remotePath, $tempFile, $protocol, $maxRetries, $retryDelay, $port = 21, $share = "", $domain = "")
	Local $attempt
	For $attempt = 0 To $maxRetries - 1
		If $attempt > 0 Then
			Local $delay = $retryDelay * (2 ^ ($attempt - 1))
			If $delay > 60 Then $delay = 60
			WriteLog(StringFormat("Retry %d/%d in %d seconds...", $attempt, $maxRetries - 1, $delay))
			Sleep($delay * 1000)
		EndIf
		
		Local $success = False
		
		If $protocol = "ftp" Or $protocol = "sftp" Then
			$success = DownloadFTP($host, $user, $password, $remotePath, $tempFile, ($protocol = "sftp"), $port)
		ElseIf $protocol = "smb" Then
			$success = DownloadSMB($host, $share, $user, $password, $remotePath, $tempFile, $domain)
		EndIf
		
		If $success Then Return True
	Next
	
	WriteLog(StringFormat("Download failed after %d attempts", $maxRetries))
	Return False
EndFunc

Func DownloadFTP($host, $user, $password, $remotePath, $tempFile, $sftp, $port)
	WriteLog("Starting download from server...")
	
	; Try WinSCP first (Windows)
	Local $winscpPath = FindExecutable("WinSCP.com")
	If $winscpPath <> "" Then
		Local $scriptFile = @TempDir & "\winscp_" & @AutoItPID & ".txt"
		Local $hFile = FileOpen($scriptFile, $FO_OVERWRITE + $FO_CREATEPATH)
		If $hFile <> -1 Then
			FileWriteLine($hFile, "option batch abort")
			FileWriteLine($hFile, "option confirm off")
			If $sftp Then
				FileWriteLine($hFile, "open sftp://" & $user & ":" & $password & "@" & $host & ":" & $port)
			Else
				FileWriteLine($hFile, "open ftp://" & $user & ":" & $password & "@" & $host & ":" & $port)
			EndIf
			FileWriteLine($hFile, "get """ & $remotePath & """ """ & $tempFile & """")
			FileWriteLine($hFile, "exit")
			FileClose($hFile)
			
			Local $result = RunWait('"' & $winscpPath & '" /script="' & $scriptFile & '"', "", @SW_HIDE)
			FileDelete($scriptFile)
			
			If FileExists($tempFile) Then
				WriteLog("Download successful")
				Return True
			EndIf
		EndIf
	EndIf
	
	; Try lftp (if available via WSL or Git Bash)
	Local $lftpPath = FindExecutable("lftp.exe")
	If $lftpPath = "" Then
		$lftpPath = FindExecutable("lftp")
	EndIf
	
	If $lftpPath <> "" Then
		Local $url = ($sftp ? "sftp://" : "ftp://") & $host
		Local $cmd = $lftpPath & " -u """ & $user & "," & $password & """ " & $url & " -e ""get " & $remotePath & " -o " & $tempFile & "; quit"""
		Local $result = RunWait(@ComSpec & " /c " & $cmd, "", @SW_HIDE)
		
		If FileExists($tempFile) Then
			WriteLog("Download successful")
			Return True
		EndIf
	EndIf
	
	WriteLog("ERROR: FTP client not found (WinSCP or lftp)")
	Return False
EndFunc

Func DownloadSMB($host, $share, $user, $password, $remotePath, $tempFile, $domain)
	WriteLog("Starting download from server...")
	
	; Use Windows net use
	Local $drive = "Z:"
	Local $uncPath = "\\" & $host & "\" & $share
	
	; Map drive
	Local $netCmd = "net use " & $drive & " " & $uncPath & " /user:" & $domain & "\" & $user & " " & $password
	RunWait(@ComSpec & " /c " & $netCmd, "", @SW_HIDE)
	
	If DriveMapGet($drive) Then
		Local $sourceFile = $drive & "\" & $remotePath
		If FileCopy($sourceFile, $tempFile, $FC_OVERWRITE) Then
			RunWait(@ComSpec & " /c net use " & $drive & " /delete /y", "", @SW_HIDE)
			WriteLog("Download successful")
			Return True
		EndIf
		RunWait(@ComSpec & " /c net use " & $drive & " /delete /y", "", @SW_HIDE)
	EndIf
	
	WriteLog("Download failed")
	Return False
EndFunc

Func UploadFile($host, $user, $password, $remotePath, $localFile, $protocol, $maxRetries, $retryDelay, $port = 21, $share = "", $domain = "")
	Local $attempt
	For $attempt = 0 To $maxRetries - 1
		If $attempt > 0 Then
			Local $delay = $retryDelay * (2 ^ ($attempt - 1))
			If $delay > 60 Then $delay = 60
			WriteLog(StringFormat("Retry %d/%d in %d seconds...", $attempt, $maxRetries - 1, $delay))
			Sleep($delay * 1000)
		EndIf
		
		Local $success = False
		
		If $protocol = "ftp" Or $protocol = "sftp" Then
			$success = UploadFTP($host, $user, $password, $remotePath, $localFile, ($protocol = "sftp"), $port)
		ElseIf $protocol = "smb" Then
			$success = UploadSMB($host, $share, $user, $password, $remotePath, $localFile, $domain)
		EndIf
		
		If $success Then Return True
	Next
	
	WriteLog(StringFormat("Upload failed after %d attempts", $maxRetries))
	Return False
EndFunc

Func UploadFTP($host, $user, $password, $remotePath, $localFile, $sftp, $port)
	WriteLog("Starting upload to server...")
	
	; Try WinSCP
	Local $winscpPath = FindExecutable("WinSCP.com")
	If $winscpPath <> "" Then
		Local $scriptFile = @TempDir & "\winscp_" & @AutoItPID & ".txt"
		Local $hFile = FileOpen($scriptFile, $FO_OVERWRITE)
		If $hFile <> -1 Then
			FileWriteLine($hFile, "option batch abort")
			FileWriteLine($hFile, "option confirm off")
			If $sftp Then
				FileWriteLine($hFile, "open sftp://" & $user & ":" & $password & "@" & $host & ":" & $port)
			Else
				FileWriteLine($hFile, "open ftp://" & $user & ":" & $password & "@" & $host & ":" & $port)
			EndIf
			FileWriteLine($hFile, "put """ & $localFile & """ """ & $remotePath & """")
			FileWriteLine($hFile, "exit")
			FileClose($hFile)
			
			RunWait('"' & $winscpPath & '" /script="' & $scriptFile & '"', "", @SW_HIDE)
			FileDelete($scriptFile)
			WriteLog("Upload successful")
			Return True
		EndIf
	EndIf
	
	WriteLog("ERROR: FTP client not found")
	Return False
EndFunc

Func UploadSMB($host, $share, $user, $password, $remotePath, $localFile, $domain)
	WriteLog("Starting upload to server...")
	
	Local $drive = "Z:"
	Local $uncPath = "\\" & $host & "\" & $share
	
	Local $netCmd = "net use " & $drive & " " & $uncPath & " /user:" & $domain & "\" & $user & " " & $password
	RunWait(@ComSpec & " /c " & $netCmd, "", @SW_HIDE)
	
	If DriveMapGet($drive) Then
		Local $destFile = $drive & "\" & $remotePath
		If FileCopy($localFile, $destFile, $FC_OVERWRITE) Then
			RunWait(@ComSpec & " /c net use " & $drive & " /delete /y", "", @SW_HIDE)
			WriteLog("Upload successful")
			Return True
		EndIf
		RunWait(@ComSpec & " /c net use " & $drive & " /delete /y", "", @SW_HIDE)
	EndIf
	
	WriteLog("Upload failed")
	Return False
EndFunc

Func MergeDatabases($keepassxc, $localDB, $tempDB, $password)
	WriteLog("Performing merge...")
	
	If Not FileExists($tempDB) Then
		WriteLog("ERROR: Temporary file not found")
		Return False
	EndIf
	
	Local $cmd = '"' & $keepassxc & '" merge -s "' & $localDB & '" "' & $tempDB & '" --same-credentials'
	Local $pid = Run($cmd, "", @SW_HIDE, $STDIN_CHILD + $STDOUT_CHILD + $STDERR_CHILD)
	
	If @error Then
		WriteLog("ERROR: Could not start KeePassXC-CLI")
		Return False
	EndIf
	
	StdinWrite($pid, $password & @CRLF)
	StdinWrite($pid)
	
	Local $output = ""
	While ProcessExists($pid)
		$output &= StdoutRead($pid)
		Sleep(100)
	WEnd
	
	Local $exitCode = @extended
	If $exitCode = 0 Then
		WriteLog("Merge completed successfully. Local file updated.")
		Return True
	Else
		WriteLog("ERROR: Merge failed")
		Return False
	EndIf
EndFunc

Func TestConnection()
	WriteLog("=== Connection Test ===")
	Local $errors[0]
	
	Local $keepassxc = FindExecutable(Json_Get($g_config, ".keepass.keepassXCPath"))
	If $keepassxc = "" Then
		ReDim $errors[UBound($errors) + 1]
		$errors[UBound($errors) - 1] = "❌ KeePassXC-CLI not found"
	Else
		WriteLog("✅ KeePassXC-CLI found: " & $keepassxc)
	EndIf
	
	Local $localPath = Json_Get($g_config, ".local.localPath")
	If FileExists($localPath) Then
		Local $size = FileGetSize($localPath)
		Local $mtime = FileGetTime($localPath, $FT_MODIFIED, $FT_STRING)
		WriteLog("✅ Local database: " & $localPath & " (" & $size & " bytes, modified: " & $mtime & ")")
	Else
		ReDim $errors[UBound($errors) + 1]
		$errors[UBound($errors) - 1] = "⚠️ Local database not found: " & $localPath
	EndIf
	
	WriteLog("=== Test completed ===")
	If UBound($errors) > 0 Then
		WriteLog("Errors found:")
		For $i = 0 To UBound($errors) - 1
			WriteLog($errors[$i])
		Next
		Return False
	EndIf
	
	WriteLog("✅ All tests successful!")
	Return True
EndFunc

Func ShowStatus()
	WriteLog("=== KeePass Sync Status ===")
	
	Local $localPath = Json_Get($g_config, ".local.localPath")
	If FileExists($localPath) Then
		Local $size = FileGetSize($localPath)
		Local $mtime = FileGetTime($localPath, $FT_MODIFIED, $FT_STRING)
		WriteLog("Local DB: " & $localPath)
		WriteLog("  Size: " & $size & " bytes (" & Round($size / 1024, 2) & " KB)")
		WriteLog("  Modified: " & $mtime)
	Else
		WriteLog("⚠️ Local DB not found: " & $localPath)
	EndIf
	
	Local $protocol = Json_Get($g_config, ".ftp.type")
	Local $host = Json_Get($g_config, ".ftp.host")
	Local $user = Json_Get($g_config, ".ftp.user")
	
	WriteLog("Protocol: " & StringUpper($protocol))
	WriteLog("Server: " & $host)
	WriteLog("User: " & $user)
	
	Local $keepassxc = FindExecutable(Json_Get($g_config, ".keepass.keepassXCPath"))
	If $keepassxc <> "" Then
		WriteLog("KeePassXC-CLI: ✅ " & $keepassxc)
	Else
		WriteLog("KeePassXC-CLI: ❌ Not found")
	EndIf
EndFunc

Func PerformSync()
	Local $keepassxc = FindExecutable(Json_Get($g_config, ".keepass.keepassXCPath"))
	If $keepassxc = "" Then
		WriteLog("ERROR: KeePassXC-CLI not found")
		Return False
	EndIf
	
	Local $localPath = Json_Get($g_config, ".local.localPath")
	Local $backupDir = Json_Get($g_config, ".local.backupDir")
	Local $maxBackups = Json_Get($g_config, ".local.maxBackups")
	
	CreateBackup($localPath, $backupDir)
	CleanupBackups($backupDir, $maxBackups)
	
	Local $protocol = StringLower(Json_Get($g_config, ".ftp.type"))
	Local $host = Json_Get($g_config, ".ftp.host")
	Local $user = Json_Get($g_config, ".ftp.user")
	Local $password = Json_Get($g_config, ".ftp.password")
	Local $remotePath = Json_Get($g_config, ".ftp.remotePath")
	Local $tempPath = Json_Get($g_config, ".local.tempPath")
	Local $port = Json_Get($g_config, ".ftp.port")
	If $port = "" Then
		$port = ($protocol = "ftp" ? 21 : 22)
	EndIf
	Local $share = Json_Get($g_config, ".ftp.share")
	Local $domain = Json_Get($g_config, ".ftp.domain")
	
	Local $maxRetries = Json_Get($g_config, ".settings.max_retries")
	Local $retryDelay = Json_Get($g_config, ".settings.retry_delay")
	
	; Download
	If Not DownloadFile($host, $user, $password, $remotePath, $tempPath, $protocol, $maxRetries, $retryDelay, $port, $share, $domain) Then
		Return False
	EndIf
	
	; Merge
	Local $dbPassword = Json_Get($g_config, ".keepass.databasePassword")
	If Not MergeDatabases($keepassxc, $localPath, $tempPath, $dbPassword) Then
		Return False
	EndIf
	
	; Upload
	If Not UploadFile($host, $user, $password, $remotePath, $localPath, $protocol, $maxRetries, $retryDelay, $port, $share, $domain) Then
		Return False
	EndIf
	
	; Cleanup
	If FileExists($tempPath) Then
		FileDelete($tempPath)
	EndIf
	
	WriteLog("Synchronization completed.")
	Return True
EndFunc

