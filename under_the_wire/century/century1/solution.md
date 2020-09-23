# Century 1 Solution 

This level is very simple, as the flag is just the version of powershell running on the server.
To determine the version, you only need to type: 

```powershell 
    $PSVersionTable.PSVersion
```

The output of that command will be a table sorta like this one :
   
 ```
    Major   Minor   Build   Revision
    -----   -----   -----   --------
    5       1       14393   2636 
```

So in this case the flag is 5.1.14393.2636