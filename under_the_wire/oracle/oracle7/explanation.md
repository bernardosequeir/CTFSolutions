```powershell

PS C:\users\Oracle6\desktop> Get-ADOrganizationalUnit -Filter 'Name -like "*"' | F
ormat-List -Property *                                                         


(...)                                                                                

City                     :                                                        
Country                  :                                                        
DistinguishedName        : OU=T-50,OU=X-Wing,DC=underthewire,DC=tech              
LinkedGroupPolicyObjects : {}                                                     
ManagedBy                :                                                        
Name                     : T-50                                                   
ObjectClass              : organizationalUnit                                     
ObjectGUID               : 5ace8bef-c00e-4f58-a543-3fd45436f1d4                   
PostalCode               :                                                        
State                    :                                                        
StreetAddress            :                                                        
PropertyNames            : {City, Country, DistinguishedName,                     
                           LinkedGroupPolicyObjects...}                           
AddedProperties          : {}                                                     
RemovedProperties        : {}                                                     
ModifiedProperties       : {}                                                     
PropertyCount            : 11                                                     

(...)

PS C:\users\Oracle6\desktop> ls                                                   
                                                                                  
                                                                                  
    Directory: C:\users\Oracle6\desktop                                           
                                                                                  
                                                                                  
Mode                LastWriteTime         Length Name                             
----                -------------         ------ ----                             
-a----        8/30/2018  10:50 AM              0 _97                              
                                                                                  
     
```
