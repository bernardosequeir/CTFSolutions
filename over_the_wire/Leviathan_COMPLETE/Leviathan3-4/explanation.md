```bash
leviathan3@leviathan:~$ ls
level3
leviathan3@leviathan:~$ ./vel
-bash: ./vel: No such file or directory
leviathan3@leviathan:~$ ./level3
Enter the password> a
bzzzzzzzzap. WRONG
leviathan3@leviathan:~$ ltrace ./level3
__libc_start_main(0x8048618, 1, 0xffffd794, 0x80486d0 <unfinished ...>
strcmp("h0no33", "kakaka")                                     = -1
printf("Enter the password> ")                                 = 20
fgets(Enter the password> aa
"aa\n", 256, 0xf7fc55a0)                                 = 0xffffd5a0
strcmp("aa\n", "snlprintf\n")                                  = -1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                     = 19
+++ exited (status 0) +++
leviathan3@leviathan:~$ ./level3
Enter the password> snlprintf\n
bzzzzzzzzap. WRONG
leviathan3@leviathan:~$ ./level3
Enter the password> snlprintf
[You've got shell]!
$ /bin/bash
leviathan4@leviathan:~$ ls
level3
leviathan4@leviathan:~$ cat /etc/leviathan_pass/leviathan4
vuH0coox6m
```