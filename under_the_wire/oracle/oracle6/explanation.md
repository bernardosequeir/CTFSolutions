```powershell
PS C:\users\Oracle5\desktop> get-gpo -all | where {$_.Description -like "*groot*"}   
                                                                                     
                                                                                     
DisplayName      : Charlie                                                           
DomainName       : underthewire.tech                                                 
Owner            : underthewire\Domain Admins                                        
Id               : 44080cf1-1053-467d-b000-2ea3f27dbbfa                              
GpoStatus        : AllSettingsEnabled                                                
Description      : I_am_Groot                                                        
CreationTime     : 11/20/2018 12:18:09 AM                                            
ModificationTime : 11/20/2018 12:18:08 AM                                            
UserVersion      : AD Version: 0, SysVol Version: 0                                  
ComputerVersion  : AD Version: 0, SysVol Version: 0                                  
WmiFilter        :                                                                   
                                                                                     
                                                                                     
                                                                                     
PS C:\users\Oracle5\desktop> ls                                                      
                                                                                     
                                                                                     
    Directory: C:\users\Oracle5\desktop                                              
                                                                                     
                                                                                     
Mode                LastWriteTime         Length Name                                
----                -------------         ------ ----                                
-a----        8/30/2018  10:50 AM              0 1337
```