https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx

```powershell

PS C:\users\Oracle13\desktop> get-winevent -path .\security.evtx | where {$_.ID -like "4727"} | Format-List -Property *                                             
                                                                                  
                                                                                  
Message              : A security-enabled global group was created.               
                                                                                  
                       Subject:                                                   
                        Security ID:                                              
                       S-1-5-21-2268727836-2773903800-2952248001-1621             
                        Account Name:           gamora                            
                        Account Domain:         UNDERTHEWIRE                      
                        Logon ID:               0xBC24FF                          
                                                                                  
                       New Group:                                                 
                        Security ID:                                              
                       S-1-5-21-2268727836-2773903800-2952248001-1626             
                        Group Name:             Galaxy                            
                        Group Domain:           UNDERTHEWIRE                      
                                                                                  
                       Attributes:                                                
                        SAM Account Name:       Galaxy                            
                        SID History:            -                                 
                                                                                  
                       Additional Information:                                    
                        Privileges:             -                                 
Id                   : 4727                                                       
Version              : 0                                                          
Qualifiers           :                                                            
Level                : 0                                                          
Task                 : 13826    

(...)


PS C:\users\Oracle13\desktop> ls                                                  
                                                                                  
                                                                                  
    Directory: C:\users\Oracle13\desktop                                          
                                                                                  
                                                                                  
Mode                LastWriteTime         Length Name                             
----                -------------         ------ ----                             
-a----        8/30/2018  10:51 AM              0 88                               
-a----        8/30/2018   5:52 AM        2166784 security.evtx 
```