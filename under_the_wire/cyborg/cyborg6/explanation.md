PS C:\Users\cyborg5\documents> Get-ADUser -Filter 'logonHours -like "*"' -Proper
ties logonHours                                                                 
                                                                                
                                                                                
DistinguishedName : CN=Administrator,CN=Users,DC=underthewire,DC=tech           
Enabled           : True                                                        
GivenName         :                                                             
logonHours        : {255, 255, 255, 255...}                                     
Name              : Administrator                                               
ObjectClass       : user                                                        
ObjectGUID        : 427058c2-1d57-4e49-a23d-204865b502ae                        
SamAccountName    : Administrator                                               
SID               : S-1-5-21-758131494-606461608-3556270690-500                 
Surname           :                                                             
UserPrincipalName :                                                             
                                                                                
DistinguishedName : CN=Rowray\, Benny  \                                        
                    ,OU=T-85,OU=X-Wing,DC=underthewire,DC=tech                  
Enabled           : False                                                       
GivenName         : Benny                                                       
logonHours        : {0, 0, 0, 0...}                                             
Name              : Rowray, Benny                                               
ObjectClass       : user                                                        
ObjectGUID        : c9aad4f3-3e4f-46b5-84db-2bb7105796dd                        
SamAccountName    : Benny.Rowray                                                
SID               : S-1-5-21-758131494-606461608-3556270690-1647                
Surname           : Rowray                                                      
UserPrincipalName : Benny.Rowray                                                
                                                                                
                                                                                
                                                                                
PS C:\Users\cyborg5\documents> ls ..\Desktop                                    
                                                                                
                                                                                
    Directory: C:\Users\cyborg5\Desktop                                         
                                                                                
                                                                                
Mode                LastWriteTime         Length Name                           
----                -------------         ------ ----                           
-a----        8/30/2018  10:45 AM              0 _timer                         
                                                                                
                              