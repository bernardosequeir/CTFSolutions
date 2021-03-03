```
PS C:\users\Groot3\desktop> (gc .\words.txt | Select-String -pattern "beetle" -AllMat
ches).length
1
PS C:\users\Groot3\desktop> (gc .\words.txt | Select-String -pattern "beetle" -AllMat
ches).matches.count
5
```