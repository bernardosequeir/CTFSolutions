bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ ls -la
total 48
drwxr-xr-x 2 root    root    4096 Oct 16 14:00 .
drwxr-xr-x 3 root    root    4096 Oct 16 14:00 ..
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file00
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file01
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file02
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file03
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file04
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file05
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file06
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file07
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file08
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file09
bandit4@bandit:~/inhere$ file *
file: Cannot open `ile00' (No such file or directory).
file: Cannot open `ile01' (No such file or directory).
file: Cannot open `ile02' (No such file or directory).
file: Cannot open `ile03' (No such file or directory).
file: Cannot open `ile04' (No such file or directory).
file: Cannot open `ile05' (No such file or directory).
file: Cannot open `ile06' (No such file or directory).
file: Cannot open `ile07' (No such file or directory).
file: Cannot open `ile08' (No such file or directory).
file: Cannot open `ile09' (No such file or directory).
bandit4@bandit:~/inhere$ file ./-*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh