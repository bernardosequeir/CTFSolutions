```
  PS C:\users\Groot9\desktop> Get-ADOrganizationalUnit -filter * -Properties ProtectedF
romAccidentalDeletion | where {$_.ProtectedFromAccidentalDeletion -eq $false}        
                                                                                     
                                                                                     
City                            :                                                    
Country                         :                                                    
DistinguishedName               : OU=T-25,OU=X-Wing,DC=underthewire,DC=tech          
LinkedGroupPolicyObjects        : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=poli 
                                  cies,cn=system,DC=underthewire,DC=tech}            
ManagedBy                       :                                                    
Name                            : T-25                                               
ObjectClass                     : organizationalUnit                                 
ObjectGUID                      : fc15c303-dd9a-4c44-a941-314cc6fdd394               
PostalCode                      :                                                    
ProtectedFromAccidentalDeletion : False                                              
State                           :                                                    
StreetAddress                   :                                                    


PS C:\users\Groot9\desktop> ls                                                       
                                                                                     
                                                                                     
    Directory: C:\users\Groot9\desktop                                               
                                                                                     
                                                                                     
Mode                LastWriteTime         Length Name                                
----                -------------         ------ ----                                
-a----        8/30/2018  10:51 AM              0 _tester                             
                                                                                           
```