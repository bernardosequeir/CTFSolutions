```powershell
PS C:\Users\cyborg14\documents> Get-WmiObject -Class win32_DCOMApplicationSettin
g -Filter "AppId='{59B8AFA0-229E-46D9-B980-DDA2C817EC7E}'"                      
                                                                                
                                                                                
__GENUS                   : 2                                                   
__CLASS                   : Win32_DCOMApplicationSetting                        
__SUPERCLASS              : Win32_COMSetting                                    
__DYNASTY                 : CIM_Setting                                         
__RELPATH                 : Win32_DCOMApplicationSetting.AppID="{59B8AFA0-229E- 
                            46d9-B980-DDA2C817EC7E}"                            
__PROPERTY_COUNT          : 12                                                  
__DERIVATION              : {Win32_COMSetting, CIM_Setting}                     
__SERVER                  : UTW                                                 
__NAMESPACE               : root\cimv2                                          
__PATH                    : \\UTW\root\cimv2:Win32_DCOMApplicationSetting.AppID 
                            ="{59B8AFA0-229E-46d9-B980-DDA2C817EC7E}"           
AppID                     : {59B8AFA0-229E-46d9-B980-DDA2C817EC7E}              
AuthenticationLevel       :                                                     
Caption                   : propshts                                            
CustomSurrogate           :                                                     
Description               : propshts                                            
EnableAtStorageActivation : False                                               
LocalService              :                                                     
RemoteServerName          :                                                     
RunAsUser                 :                                                     
ServiceParameters         :                                                     
SettingID                 :                                                     
UseSurrogate              : False                                               
PSComputerName            : UTW                                                 
                                                                                
                                                                                
PS C:\Users\cyborg14\documents> ls ..\Desktop                                   
                                                                                
                                                                                
    Directory: C:\Users\cyborg14\Desktop                                        
                                                                                
                                                                                
Mode                LastWriteTime         Length Name                           
----                -------------         ------ ----                           
-a----        8/30/2018  10:45 AM              0 _objects                                                                                                    
``` 