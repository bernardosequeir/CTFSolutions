https://jdhitsolutions.com/blog/powershell/49/reading-the-registry-in-powershell/

```powershell
    PS C:\users\Groot13\desktop> (Get-ItemProperty “HKLM:\Software\Microsoft\Windows NT\C
urrentVersion”).RegisteredOwner
UTW_Team
PS C:\users\Groot13\desktop> ls


    Directory: C:\users\Groot13\desktop


Mode                LastWriteTime         Length Name                               
----                -------------         ------ ----                               
-a----        8/30/2018  10:51 AM              0 _ned                               


```