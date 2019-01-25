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

```powershell
PS C:\Users\century7\documents> cd ..
PS C:\Users\century7> ls -Include *read* -Recurse


    Directory: C:\Users\century7\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM              7 Readme


PS C:\Users\century7> cat .\Downloads\Readme
7points
``` 
So the flag is just 7points.