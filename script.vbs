Set WshShell = CreateObject("WScript.Shell")

' Lancer interface.exe
WshShell.Run "interface.exe", 1, False

' Lancer run.bat
WshShell.Run "cmd /c run.bat", 0, False

Set WshShell = Nothing
