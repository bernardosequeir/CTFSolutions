```powershell

PS C:\users\Groot12\desktop> ls


    Directory: C:\users\Groot12\desktop


Mode                LastWriteTime         Length Name                               
----                -------------         ------ ----                               
d-----        8/30/2018  10:51 AM                Nine Realms                        


PS C:\users\Groot12\desktop> Get-Acl '.\Nine Realms' | Select-Object Owner

Owner               
-----               
underthewire\Airwolf

```