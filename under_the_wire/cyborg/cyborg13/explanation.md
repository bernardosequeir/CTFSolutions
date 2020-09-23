This level just wants us to find out the path of the executable that starts the service **i_heart_robots**

So i found a script that prints out details about services and just used it.


```powershell 
  Get-WmiObject win32_service | ?{$_.Name -like '*i_*'} | select Name, Disp
layName, State, PathName    

Name           DisplayName    State   PathName                   
----           -----------    -----   --------                   
i_heart_robots i_heart_robots Stopped c:\windows\system32\cmd.exe

PS C:\Users\cyborg12\documents> ls ..\Desktop


    Directory: C:\Users\cyborg12\Desktop


Mode                LastWriteTime         Length Name                                                   
----                -------------         ------ ----                                                   
-a----        8/30/2018  10:45 AM              0 _heart  

```


The second half of the challenge was to convert the path to base64 and keep the first four chars for our password. I assume that we were supposed to do that on powershell but I just used an online decoder.

The password is just : ***yzpc_heart***
