```bash 
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ ls -la
total 88
drwxr-x--- 22 root bandit5 4096 Oct 16 14:00 .
drwxr-xr-x  3 root root    4096 Oct 16 14:00 ..
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere00
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere01
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere02
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere03
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere04
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere05
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere06
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere07
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere08
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere09
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere10
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere11
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere12
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere13
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere14
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere15
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere16
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere17
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere18
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere19
bandit5@bandit:~/inhere$ man du
bandit5@bandit:~/inhere$ du *
68      maybehere00
76      maybehere01
64      maybehere02
76      maybehere03
56      maybehere04
60      maybehere05
60      maybehere06
52      maybehere07
52      maybehere08
72      maybehere09
52      maybehere10
68      maybehere11
68      maybehere12
60      maybehere13
56      maybehere14
60      maybehere15
76      maybehere16
68      maybehere17
64      maybehere18
72      maybehere19
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$
bandit5@bandit:~/inhere$ man du
bandit5@bandit:~/inhere$ du -b *
49973   maybehere00
53375   maybehere01
50730   maybehere02
55021   maybehere03
35993   maybehere04
40561   maybehere05
43400   maybehere06
33920   maybehere07
35827   maybehere08
57123   maybehere09
32522   maybehere10
42429   maybehere11
44438   maybehere12
40360   maybehere13
32865   maybehere14
35179   maybehere15
57233   maybehere16
43901   maybehere17
44838   maybehere18
54678   maybehere19
bandit5@bandit:~/inhere$ man find
bandit5@bandit:~/inhere$ find -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      bandit5@bandit:~/inhere$
```