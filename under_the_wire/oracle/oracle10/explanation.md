```powershell

PS C:\users\Oracle9\desktop> Get-DnsServerResourceRecord -ZoneName UnderTheWire.te
ch

HostName                  RecordType Type       Timestamp            TimeToLive  
--------                  ---------- ----       ---------            ----------  
@                         A          1          3/2/2021 12:00:00 PM 00:10:00    
@                         NS         2          0                    01:00:00    
@                         SOA        6          0                    01:00:00    
_msdcs                    NS         2          0                    01:00:00    
_gc._tcp.Default-First... SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_kerberos._tcp.Default... SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_ldap._tcp.Default-Fir... SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_gc._tcp                  SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_kerberos._tcp            SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_kpasswd._tcp             SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_ldap._tcp                SRV        33         3/2/2021 12:00:00 PM 00:10:00    
_kerberos._udp            SRV        33         3/2/2021 12:00:00 PM 00:10:00     
_kpasswd._udp             SRV        33         3/2/2021 12:00:00 PM 00:10:00     
CYBORG718W100N            A          1          0                    01:00:00     
DomainDnsZones            A          1          3/2/2021 1:00:00 PM  00:10:00     
_ldap._tcp.Default-Fir... SRV        33         3/2/2021 1:00:00 PM  00:10:00     
_ldap._tcp.DomainDnsZones SRV        33         3/2/2021 1:00:00 PM  00:10:00     
ForestDnsZones            A          1          3/2/2021 1:00:00 PM  00:10:00     
_ldap._tcp.Default-Fir... SRV        33         3/2/2021 1:00:00 PM  00:10:00     
_ldap._tcp.ForestDnsZones SRV        33         3/2/2021 1:00:00 PM  00:10:00     
utw                       A          1          0                    01:00:00     
utw_exch                  MX         15         0                    01:00:00

PS C:\users\Oracle9\desktop> ls                                                   
                                                                                  
                                                                                  
    Directory: C:\users\Oracle9\desktop                                           
                                                                                  
                                                                                  
Mode                LastWriteTime         Length Name                             
----                -------------         ------ ----                             
-a----        8/30/2018  10:51 AM              0 9229                             
                                                                                  

```