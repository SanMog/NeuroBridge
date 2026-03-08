Set WshShell = CreateObject("WScript.Shell")
strPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = strPath

' 1. ПРИНУДИТЕЛЬНАЯ ОЧИСТКА (Kill old instances)
' Закрываем старые процессы python, чтобы не было дублей в трее
On Error Resume Next
WshShell.Run "taskkill /F /IM python.exe /T", 0, True
On Error GoTo 0

' Небольшая пауза
WScript.Sleep 500

' 2. ЗАПУСК ИНТЕРФЕЙСОВ (Input & Output)
' Используем Chr(34) для обработки путей с точками и возможными пробелами
' ВНИМАНИЕ: Проверь, что путь .venv\Scripts\python.exe верный
WshShell.Run Chr(34) & strPath & "\.venv\Scripts\python.exe" & Chr(34) & " core\voice_input.py", 0, False
WshShell.Run Chr(34) & strPath & "\.venv\Scripts\python.exe" & Chr(34) & " core\voice_output.py", 0, False

Set WshShell = Nothing