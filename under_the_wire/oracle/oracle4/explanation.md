```powershell 

PS C:\users\Oracle3\desktop> Get-WinEvent -Path .\Oracle3_Security.evtx                                                                                                                                        
                                                                                                                                                                                                               
                                                                                                                                                                                                               
   ProviderName: Microsoft-Windows-Security-Auditing                                                                                                                                                           
                                                                                                                                                                                                               
TimeCreated                     Id LevelDisplayName Message                                                                                                                                                    
-----------                     -- ---------------- -------                                                                                                                                                    
5/18/2017 11:38:23 PM         4624 Information      An account was successfully logged on....                                                                                                                  
5/18/2017 11:38:23 PM         4672 Information      Special privileges assigned to new logon....                                                                                                               
5/18/2017 11:38:23 PM         4634 Information      An account was logged off....                                                                                                                              
5/18/2017 11:37:38 PM         4624 Information      An account was successfully logged on....                                                                                                                  
(...)                                                                                                                                                                                                   
                                                                                                                                                                                                               
   ProviderName: Microsoft-Windows-Eventlog                                                                                                                                                                    
                                                                                                                                                                                                               
TimeCreated                     Id LevelDisplayName Message                                                                                                                                                    
-----------                     -- ---------------- -------                                                                                                                                                    
5/9/2017 11:36:05 PM          1102 Information      The audit log was cleared....                                                                                                                              
                                                                                                                                                                                                               
                                                                                                                                                                                                               
   ProviderName: Microsoft-Windows-Security-Auditing                                                                                                                                                           
                                                                                                                                                                                                               
TimeCreated                     Id LevelDisplayName Message                                                                                                                                                    
-----------                     -- ---------------- -------                                                                                                                                                    
5/9/2017 11:36:04 PM          4634 Information      An account was logged off....                                                                                                                              
5/9/2017 11:36:04 PM          4624 Information      An account was successfully logged on....                                                                                                                  
5/9/2017 11:36:04 PM          4672 Information      Special privileges assigned to new logon....                                                                                                               
5/9/2017 11:36:04 PM          4688 Information      A new process has been created....                                                                                                                         
5/9/2017 11:36:04 PM          4670 Information      Permissions on an object were changed....                                                                                                                  
5/9/2017 11:36:04 PM          4670 Information      Permissions on an object were changed....                                                                                                                  
5/9/2017 11:36:04 PM          4670 Information      Permissions on an object were changed....                                                                                                                  
5/9/2017 11:36:04 PM          4688 Information      A new process has been created....                                                                                                                         
                                                                                                                                                                                                               

PS C:\users\Oracle3\desktop> Get-WinEvent -Path .\Oracle3_Security.evtx | where {$_.Id -eq 1102}                                                                                                               
                                                                                                                                                                                                               
                                                                                                                                                                                                               
   ProviderName: Microsoft-Windows-Eventlog                                                                                                                                                                    
                                                                                                                                                                                                               
TimeCreated                     Id LevelDisplayName Message                                                                                                                                                    
-----------                     -- ---------------- -------                                                                                                                                                    
5/9/2017 11:36:05 PM          1102 Information      The audit log was cleared....                  

``` 