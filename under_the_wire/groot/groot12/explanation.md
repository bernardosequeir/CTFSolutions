https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/

```
PS C:\users\Groot11\desktop> gci -recurse | % { gi $_.FullName -stream * } | where st
ream -ne ':$Data'                                                                    
                                                                                     
                                                                                     
PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\users\Groot11\desktop\TPS_R 
                eports04.pdf:secret                                                  
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\Groot11\desktop       
PSChildName   : TPS_Reports04.pdf:secret                                             
PSDrive       : C                                                                    
PSProvider    : Microsoft.PowerShell.Core\FileSystem                                 
PSIsContainer : False                                                                
FileName      : C:\users\Groot11\desktop\TPS_Reports04.pdf                           
Stream        : secret                                                               
Length        : 12                                                                   
                                                                                     
                                                                                     
                                                                                     
PS C:\users\Groot11\desktop> gc .\TPS_Reports04.pdf -stream secret                   
spaceships 
``` 