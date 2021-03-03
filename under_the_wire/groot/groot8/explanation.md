```powershell

PS C:\Users\Groot7\Desktop> ls


    Directory: C:\Users\Groot7\Desktop


Mode                LastWriteTime         Length Name                               
----                -------------         ------ ----                               
-a----        8/21/2020   1:25 PM              0 _home

PS C:\users\Groot7\desktop> cd HKLM:\SYSTEM\CurrentControlSet\Services

PS HKLM:\SYSTEM\CurrentControlSet\Services> Get-Item applockerfltr                   
                                                                                     
                                                                                     
    Hive: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services                       
                                                                                     
                                                                                     
Name                           Property                                              
----                           --------                                              
applockerfltr                  DisplayName     :                                     
                               @%systemroot%\system32\srpapi.dll,-102                
                               ErrorControl    : 1                                   
                               ImagePath       : system32\drivers\applockerfltr.sys  
                               Start           : 3                                   
                               Type            : 1                                   
                               Description     :                                     
                               @%systemroot%\system32\srpapi.dll,-103                
                               DependOnService : {FltMgr, AppID, AppIDSvc} 



```