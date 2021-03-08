```powershell
PS C:\users\Oracle8\desktop> gc .\logs.txt |Out-string -stream | select-string -pa
ttern 'guardian.galaxy.com'                                                       
                                                                                  
guardian.galaxy.com - - [28/Jul/1995:13:03:55 -0400] "GET /images/star-lord.gif   
HTTP/1.0" 200 786                                                                 
      
```