```powershell
get-winevent -path .\security.evtx | where {$_.ID -like "4728"} | Format-List -Property *                                             
                                                                                  
                                                                                  
                                                                                  
Message              : A member was added to a security-enabled global group.     
                                                                                  
                       Subject:                                                   
                        Security ID:                                              
                       S-1-5-21-2268727836-2773903800-2952248001-1622             
                        Account Name:           nebula                            
                        Account Domain:         UNDERTHEWIRE                      
                        Logon ID:               0xBD8CC7                          
                                                                                  
                       Member:                                                    
                        Security ID:                                              
                       S-1-5-21-2268727836-2773903800-2952248001-1623             
                        Account Name:           CN=Bereet,OU=Morag,DC=UNDERTHEWIRE
,DC=TECH                                                                          
                                                                                  
                       Group:                                                     
                        Security ID:                                              
                       S-1-5-21-2268727836-2773903800-2952248001-1626             
                        Group Name:             Galaxy                            
                        Group Domain:           UNDERTHEWIRE                      
                                                                                  
                       Additional Information:       


PS C:\users\Oracle14\desktop> ls                                                  
                                                                                  
                                                                                  
    Directory: C:\users\Oracle14\desktop                                          
                                                                                  
                                                                                  
Mode                LastWriteTime         Length Name                             
----                -------------         ------ ----                             
-a----        8/30/2018  10:51 AM              0 2112                             
-a----        8/30/2018   5:52 AM        2166784 security.evtx                    
                                                       
```