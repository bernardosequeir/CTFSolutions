```powershell 
  PS C:\users\Groot4\desktop> Get-ChildItem -Path HKCU:\ -Recurse | Select-String Drax 
                                                                                     
HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax                                 
HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax\destroyer
```