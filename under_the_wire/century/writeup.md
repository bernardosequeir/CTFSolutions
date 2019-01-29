# Century Wargame Write-Up

### Century 1 Solution 

This level is very simple, as the flag is just the build version of powershell running on the server.
To determine the version, you only need to type: 

```powershell 
    $PSVersionTable
```

The output of that command will be a table sorta like this one :
   
```powershell
Name                           Value
----                           -----
PSVersion                      5.1.14393.2636
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.14393.2636
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1

```

So in this case the flag is 10.0.14393.2636

### Century 2 Solution

This level continues to ease us into Powershell, now the new flag is the the name of the built-in cmdlet that "emulates" wget and the name of the file that is on the user's desktop.

To get the name of the cmdlet you can just run:

```powershell
PS C:\Users\century2\Documents> Get-Alias wget

CommandType     Name                      Version    Source
-----------     ----                      -------    ------
Alias           wget -> Invoke-WebRequest
```

And you can get the filename just as easy with:

```powershell 
PS C:\Users\century2\Documents> ls ..\Desktop


    Directory: C:\Users\century2\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 443


```

So the flag is just invoke-webrequest443 (lowercase as indicated on the challenge page)


### Century 3 Solution

Still an easy one, the flag is just the number of files on the user's desktop. It's the first time we have to use a Powershell command though. (Obviously all we've used until now are Powershell commands but aliased as their bash names). The solution is just: 

```powershell
PS C:\Users\century3\documents> echo ( ls ..\Desktop | Measure-Object).Count
123
```

Onwards to century4 with 123 we go.

### Century 4 Solution

Now this one has a trick, the flag is still just a filename but the file is inside a folder which has spaces, but you can circumvent it using tab-completion, just write the C and then hit tab and it will expand to the full name, as pictured below:

```powershell 
PS C:\Users\century4\Documents> ls '..\Desktop\Can You Open Me'


    Directory: C:\Users\century4\Desktop\Can You Open Me


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             24 61580


```

### Century 5 Solution

So this one is a little bit trickier, the flag is the short name of the domain where the machine is and the name of the file on the desktop.

Poking around on google there's a really easy command that returns the domain name

```powershell
PS C:\Users\century5\documents> (gwmi Win32_NTDomain).DomainName
underthewire
```
And as we've done a couple of times now, we get the filename like this

```powershell
PS C:\Users\century5\documents> ls ..\Desktop


    Directory: C:\Users\century5\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             54 3347
```

So, the flag would just be underthewire3347
 

### Century 6 Solution

The solution to this one is the same as Century 3, I was afraid we'd have to learn how to filter files and folders, but appears not, since the solution worked right away for me.

```powershell 
PS C:\Users\century6\documents> echo ( ls ..\Desktop | Measure-Object).Count
197
``` 

### Century 7 Solution

The flag for this level is the content of a file hidden inside the user's folders. All we know is that the flag is inside a readme so, if we search for a command that works similar to grep we find that ***Get-ChildItem*** (aliased as ls in the example below) is capable of doing just that. All we have to do is cd into the parent folder of the user and search for a file that *includes* read and do it *recursively*, so that it searches every folder available.

```powershell
PS C:\Users\century7\documents> cd ..
PS C:\Users\century7> ls -Include *read* -Recurse


    Directory: C:\Users\century7\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM              7 Readme
```

Now that we know where the file is, we just nead to cat (***Get-Content*** alias) it out

```powershell
PS C:\Users\century7> cat .\Downloads\Readme
7points
``` 
So the flag is just 7points.


### Century 8 Solution

The flag for this level is the number of unique lines on the file on the file on the desktop. So, using our bash trained minds, we instantly think of ``` sort | uniq```, so translating to Powershell, we can use ***Get-Unique***, in bash we'd have to sort it first, due to how uniq works, but here ***Get-Unique*** works by itself. So we can just count the lines left after removing duplicates. 


```powershell 
PS C:\Users\century8\Desktop> (cat .\unique.txt | Get-Unique).count
696
```

The flag is 696.


### Century 9 Solution

This level asks for us to retrieve the 161th word of the document on the desktop, which is really simple, we just have to open the file, split it using ***split(" ")*** and then get the desired item, which we can do with brackets, like this:

```powershell
PS C:\Users\century9\Desktop> (cat .\Word_File.txt).split(" ")[160]
pierid
```

### Century 10 Solution

We need to get the 10th and the 8th word of the description of the windows update service and the name of the file on the desktop, with ***Get-Service***, you get a list of all the services that machine has, and at the bottom of the list you can see *wuauserv*, the name of the windows update service. 

```powershell 
PS C:\Users\century10\documents> Get-WMIObject -Class Win32_Service -Filter "Nam
e='wuauserv'" | Select-Object Description | Format-Table -Wrap

Description
-----------
Enables the detection, download, and installation of updates for Windows and
other programs. If this service is disabled, users of this computer will not
be able to use Windows Update or its automatic updating feature, and programs
will not be able to use the Windows Update Agent (WUA) API.


```

So you need to get the service, needing to use a filter to get it, yeah, that threw me for a loop. So then you need to use ***Select-Object***, and get the Description field, but because and it doesn't fit there you need to use ***Format-Table***.

Getting the name of the desktop is trivial at this time so, the flag is windowsupdates110


### Century 11 Solution

```powershell
PS C:\Users\century11> cd .\Downloads
PS C:\Users\century11\Downloads> ls -Force


    Directory: C:\Users\century11\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--rh--        8/30/2018   3:34 AM             30 secret_sauce
```

### Century 12 Solution

The flag for this level is the description of the domain's controller computer, plus the name of the file on the desktop, so, to get the description of the domain's controller, we use ***Get-ADDomainController***.

```powershell
    PS C:\Users\century12\Desktop> Get-ADDomainController


ComputerObjectDN           : CN=UTW,OU=Domain
                             Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
Enabled                    : True
Forest                     : underthewire.tech
HostName                   : utw.underthewire.tech
InvocationId               : 09ee1897-2210-4ac9-989d-e19b4241e9c6
IPv4Address                : 192.99.167.156
IPv6Address                :
...
```

The ComputerObjectDN value gives us the domain's controller computer name (CN), so if we use ***Get-ADComputer***, we can get the information we want.


```powershell 
PS C:\Users\century12\Desktop> Get-ADComputer -Filter {Name -eq "UTW"} -Prop Des
cription


Description       : I_Authenticate
DistinguishedName : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DNSHostName       : utw.underthewire.tech
Enabled           : True
Name              : UTW
ObjectClass       : computer
ObjectGUID        : 5ca56844-bb73-4234-ac85-eed2d0d01a2e
SamAccountName    : UTW$
SID               : S-1-5-21-758131494-606461608-3556270690-1000
UserPrincipalName :

```

The flag is I_Authenticate_things (the name of the file on the desktop).


### Century 13 Solution
