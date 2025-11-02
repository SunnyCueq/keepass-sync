#cs
	Quick Test für Json.au3 und BinaryCall.au3
	Testet die grundlegenden Funktionen, die in sync.au3 verwendet werden
#ce

#include "Json.au3"

; Test 1: Json_Decode
ConsoleWrite("=== Test 1: Json_Decode ===" & @CRLF)
Local $testJson = '{"test": "value", "number": 123, "nested": {"key": "value"}}'
Local $decoded = Json_Decode($testJson)
If @error Then
	ConsoleWrite("❌ Json_Decode FEHLER: " & @error & @CRLF)
	Exit 1
Else
	ConsoleWrite("✅ Json_Decode erfolgreich" & @CRLF)
EndIf

; Test 2: Json_Get
ConsoleWrite("=== Test 2: Json_Get ===" & @CRLF)
Local $value = Json_Get($decoded, ".test")
If $value = "value" Then
	ConsoleWrite("✅ Json_Get erfolgreich: " & $value & @CRLF)
Else
	ConsoleWrite("❌ Json_Get FEHLER: Erwartet 'value', erhalten '" & $value & "'" & @CRLF)
	Exit 1
EndIf

; Test 3: Json_Get (nested)
ConsoleWrite("=== Test 3: Json_Get (nested) ===" & @CRLF)
Local $nestedValue = Json_Get($decoded, ".nested.key")
If $nestedValue = "value" Then
	ConsoleWrite("✅ Json_Get (nested) erfolgreich: " & $nestedValue & @CRLF)
Else
	ConsoleWrite("❌ Json_Get (nested) FEHLER: Erwartet 'value', erhalten '" & $nestedValue & "'" & @CRLF)
	Exit 1
EndIf

; Test 4: Json_Put
ConsoleWrite("=== Test 4: Json_Put ===" & @CRLF)
Json_Put($decoded, ".newkey", "newvalue")
Local $newValue = Json_Get($decoded, ".newkey")
If $newValue = "newvalue" Then
	ConsoleWrite("✅ Json_Put erfolgreich: " & $newValue & @CRLF)
Else
	ConsoleWrite("❌ Json_Put FEHLER: Erwartet 'newvalue', erhalten '" & $newValue & "'" & @CRLF)
	Exit 1
EndIf

; Test 5: Real-world config.json test
ConsoleWrite("=== Test 5: Real-world config.json format ===" & @CRLF)
Local $configJson = '{"ftp":{"host":"test.com","user":"user","password":"pass","type":"ftp","remotePath":"/file.kdbx"},"local":{"localPath":"file.kdbx","tempPath":"temp.kdbx","backupDir":"backups","maxBackups":2},"keepass":{"databasePassword":"pass","keepassXCPath":"keepassxc-cli"},"settings":{"debug":false,"language":"de","max_retries":3,"retry_delay":5}}'
Local $config = Json_Decode($configJson)
If @error Then
	ConsoleWrite("❌ Config JSON Decode FEHLER: " & @error & @CRLF)
	Exit 1
EndIf

Local $host = Json_Get($config, ".ftp.host")
Local $maxBackups = Json_Get($config, ".local.maxBackups")
If $host = "test.com" And $maxBackups = 2 Then
	ConsoleWrite("✅ Real-world config test erfolgreich" & @CRLF)
	ConsoleWrite("   Host: " & $host & @CRLF)
	ConsoleWrite("   MaxBackups: " & $maxBackups & @CRLF)
Else
	ConsoleWrite("❌ Real-world config test FEHLER" & @CRLF)
	Exit 1
EndIf

ConsoleWrite(@CRLF & "=== ALLE TESTS ERFOLGREICH ===" & @CRLF)
ConsoleWrite("✅ Json.au3 und BinaryCall.au3 funktionieren korrekt!" & @CRLF)

