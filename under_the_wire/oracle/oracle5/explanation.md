```powershell
PS C:\users\Oracle4\desktop> get-gpo -all | Sort-Object -Property CreationTime       
                                                                                     
                                                                                     
DisplayName      : Default Domain Controllers Policy                                 
DomainName       : underthewire.tech                                                 
Owner            : underthewire\Domain Admins                                        
Id               : 6ac1786c-016f-11d2-945f-00c04fb984f9                              
GpoStatus        : AllSettingsEnabled                                                
Description      :                                                                   
CreationTime     : 8/30/2018 2:51:10 AM                                              
ModificationTime : 12/9/2018 8:25:40 PM                                              
UserVersion      : AD Version: 0, SysVol Version: 0                                  
ComputerVersion  : AD Version: 9, SysVol Version: 9                                  
WmiFilter        :                                                                   
                                                                                     
(...)                                                                                  
DisplayName      : Alpha                                                             
DomainName       : underthewire.tech                                                 
Owner            : underthewire\Domain Admins                                        
Id               : 49401c32-4145-463f-b5e7-816926d4f78d                              
GpoStatus        : AllSettingsEnabled                                                
Description      : Are you there?                                                    
CreationTime     : 1/13/2019 9:40:20 PM                                              
ModificationTime : 1/13/2019 9:40:20 PM                                              
UserVersion      : AD Version: 0, SysVol Version: 0                                  
ComputerVersion  : AD Version: 0, SysVol Version: 0                                  
WmiFilter        :                                                                   
                                                                                     
  
PS C:\users\Oracle4\desktop> ls                                                      
                                                                                     
                                                                                     
    Directory: C:\users\Oracle4\desktop                                              
                                                                                     
                                                                                     
Mode                LastWriteTime         Length Name                                
----                -------------         ------ ----                                
-a----        8/30/2018  10:49 AM              0 83                                  
                                                                                     
       

```