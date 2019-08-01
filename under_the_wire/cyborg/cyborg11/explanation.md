```powershell PS C:\Users\cyborg10\documents> Get-AppLockerPolicy -Effective -Xml
<AppLockerPolicy Version="1"><RuleCollection Type="Appx" EnforcementMode="NotConfigured" /><RuleCollectio
n Type="Dll" EnforcementMode="NotConfigured" /><RuleCollection Type="Exe" EnforcementMode="NotConfigured"
><FilePathRule Id="cf7f9744-e5de-4189-8499-236666a32796" Name="C:\Users\cyborg10\Documents\ill_be_back.ex
e" Description="terminated!" UserOrGroupSid="S-1-1-0" Action="Deny"><Conditions><FilePathCondition Path="
C:\Users\cyborg10\Documents\ill_be_back.exe" /></Conditions></FilePathRule></RuleCollection><RuleCollecti
on Type="Msi" EnforcementMode="NotConfigured" /><RuleCollection Type="Script" EnforcementMode="NotConfigu
red" /></AppLockerPolicy>

PS C:\Users\cyborg10\documents> ls ..\Desktop


    Directory: C:\Users\cyborg10\Desktop


Mode                LastWriteTime         Length Name                                                   
----                -------------         ------ ----                                                   
-a----        8/30/2018  10:45 AM              0 99                                                     
```