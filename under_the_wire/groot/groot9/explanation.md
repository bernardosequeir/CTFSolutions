```powershell

PS C:\users\Groot8\desktop> Get-NetFirewallRule | Where { $_.DisplayName -like '*mysq
l*'}                                                                                 
                                                                                     
                                                                                     
Name                  : {8ce6b97d-5c1d-4347-a7fd-1792feb42355}                       
DisplayName           : MySQL                                                        
Description           : call_me                                                      
DisplayGroup          :                                                              
Group                 :                                                              
Enabled               : True                                                         
Profile               : Any                                                          
Platform              : {}                                                           
Direction             : Inbound                                                      
Action                : Block                                                        
EdgeTraversalPolicy   : Block                                                        
LooseSourceMapping    : False                                                        
LocalOnlyMapping      : False                                                        
Owner                 :                                                              
PrimaryStatus         : OK                                                           
Status                : The rule was parsed successfully from the store. (65536)     
EnforcementStatus     : NotApplicable                                                
PolicyStoreSource     : PersistentStore                                              
PolicyStoreSourceType : Local                                                        
                                                                                     
PS C:\users\Groot8\desktop> ls                                                       
                                                                                     
                                                                                     
    Directory: C:\users\Groot8\desktop                                               
                                                                                     
                                                                                     
Mode                LastWriteTime         Length Name                                
----                -------------         ------ ----                                
-a----        8/30/2018  10:51 AM              0 _starlord

```