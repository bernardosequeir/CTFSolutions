So i found out the default location of the IIS Logs from [here](https://stackify.com/where-are-iis-log-files-located/)

I found the log in 'C:\inetpub\logs\logfiles\w3svc1'

Sooo... this log is pretty huge so we're going to have to ***grep*** it. The equivalent

```powershell 
   PS C:\inetpub\logs\logfiles\w3svc1> cat .\u_ex160413.log | Select-String -NotMatch -Pattern 'Mozilla|Opera'                                                                                                       
                                                                                                         
#Software: Microsoft Internet Information Services 8.5                                                   
#Version: 1.0                                                                                            
#Date: 2016-04-13 04:14:01                                                                               
#Fields: date time s-sitename s-computername s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username  
c-ip cs-version cs(User-Agent) cs(Cookie) cs(Referer) cs-host sc-status sc-substatus sc-win32-status     
sc-bytes cs-bytes time-taken                                                                             
2016-04-13 04:14:12 W3SVC1 Century 172.31.45.65 GET / - 80 - 172.31.45.65 HTTP/1.1                       
LordHelmet/5.0+(CombTheDesert)+Password+is:spaceballs - - century.underthewire.tech 200 0 0 925 118 0    
                                                                                                         
                          
```

So the password is in the middle of the remaining text: **spaceballs**