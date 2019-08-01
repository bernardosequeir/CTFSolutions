```powershell 
PS C:\Users\cyborg8\Desktop> Get-Item .\1_qs5nwlcl7f_-SwNlQvOrAw.png -stream *  
                                                                                
                                                                                
PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\cyborg8\Desktop\ 
                1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA                             
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\cyborg8\Desktop  
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA                             
PSDrive       : C                                                               
PSProvider    : Microsoft.PowerShell.Core\FileSystem                            
PSIsContainer : False                                                           
FileName      : C:\Users\cyborg8\Desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png           
Stream        : :$DATA                                                          
Length        : 60113                                                           
                                                                                
PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\cyborg8\Desktop\ 
                1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier                    
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\cyborg8\Desktop  
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier                    
PSDrive       : C                                                               
PSProvider    : Microsoft.PowerShell.Core\FileSystem                            
PSIsContainer : False                                                           
FileName      : C:\Users\cyborg8\Desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png           
Stream        : Zone.Identifier                                                 
Length        : 26

PS C:\Users\cyborg8\Desktop> Get-Content .\1_qs5nwlcl7f_-SwNlQvOrAw.png -stream 
Zone.Identifier
[ZoneTransfer]                                                          
ZoneId=4      
``` 