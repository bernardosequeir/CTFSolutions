```
PS C:\users\Groot10\desktop> ls


    Directory: C:\users\Groot10\desktop


Mode                LastWriteTime         Length Name                               
----                -------------         ------ ----                               
-a----        8/30/2018   5:52 AM          17324 new.txt                            
-a----        8/30/2018   5:52 AM          17313 old.txt                            


PS C:\users\Groot10\desktop> compare-object (gc .\new.txt ) (gc .\old.txt)

InputObject SideIndicator
----------- -------------
taserface   <=           
                                                                                     
                           
```