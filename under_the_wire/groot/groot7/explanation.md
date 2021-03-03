```powershell

PS C:\users\Groot6\desktop> ls                                                       
                                                                                     
                                                                                     
    Directory: C:\users\Groot6\desktop                                               
                                                                                     
                                                                                     
Mode                LastWriteTime         Length Name                                
----                -------------         ------ ----                                
-a----        8/21/2020   1:24 PM              0 _rules                              
                                                         
PS C:\users\Groot6\desktop> Get-CimInstance Win32_StartupCommand | Select-Object Name
, command, Location, User | Format-List                                              
                                                                                     
                                                                                     
Name     : New Value #1                                                              
command  :                                                                           
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windo 
           ws\CurrentVersion\Run                                                     
User     : underthewire\Groot6                                                       
                                                                                     
Name     : New Value #2                                                              
command  :                                                                           
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windo 
           ws\CurrentVersion\Run                                                     
User     : underthewire\Groot6                                                       
                                                                                     
Name     : New Value #3                                                              
command  :                                                                           
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windo 
           ws\CurrentVersion\Run                                                     
User     : underthewire\Groot6                                                       
                                                                                     
Name     : New Value #4                                                              
command  :                                                                           
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windo 
           ws\CurrentVersion\Run                                                     
User     : underthewire\Groot6                                                       
                                                                                     
Name     : star-lord                                                                 
command  : C:\star-lord.exe                                                          
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windo 
           ws\CurrentVersion\Run                                                     
User     : underthewire\Groot6  

``` 