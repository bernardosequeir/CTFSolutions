```powershell
  PS C:\Users\cyborg9\documents> Get-ADUser -Property OfficePhone -Filter 'telepho
neNumber -like"*5309*" '                                                        
                                                                                
                                                                                
DistinguishedName : CN=Garick\, Onita  \                                        
                    ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech                  
Enabled           : False                                                       
GivenName         : Onita                                                       
Name              : Garick, Onita                                               
ObjectClass       : user                                                        
ObjectGUID        : 5fc5bb5b-272a-4b70-877a-ed774029e247                        
OfficePhone       : 876-5309                                                    
SamAccountName    : Onita.Garick                                                
SID               : S-1-5-21-758131494-606461608-3556270690-2124                
Surname           : Garick                                                      
UserPrincipalName : Onita.Garick                                                
                                  

PS C:\Users\cyborg9\documents> ls ..\Desktop                                    
                                                                                
                                                                                
    Directory: C:\Users\cyborg9\Desktop                                         
                                                                                
                                                                                
Mode                LastWriteTime         Length Name                           
----                -------------         ------ ----                           
-a----        8/30/2018  10:45 AM              0 99                             
                                                                                
                                                     
```