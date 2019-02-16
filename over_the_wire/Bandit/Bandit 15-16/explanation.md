```
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
(...)
    0000 - 32 a4 5b 29 4b c8 06 db-a5 7e c7 95 4f fd c4 c1   2.[)K....~..O...
    0010 - d4 e7 a7 b5 4a 38 1d f6-d0 5f c3 df fe bd 91 e8   ....J8..._......
    0020 - 5e f7 05 40 a6 85 e2 12-b9 8a 7e 43 fa 26 5b 7a   ^..@......~C.&[z
    0030 - 8d 61 3e 7e ba bd b5 8e-1e 9a 49 5c 22 45 2b 19   .a>~......I\"E+.
    0040 - b2 40 ce 74 be e5 d2 df-fc ac 7f d1 81 f7 04 66   .@.t...........f
    0050 - df ea 18 3b 7a 5d a8 0a-41 ac 49 87 69 dd 26 a6   ...;z]..A.I.i.&.
    0060 - e4 7f 93 79 d7 2c d7 84-07 e2 07 13 91 4f 3a d0   ...y.,.......O:.
    0070 - a5 bb 87 47 54 8e d2 ae-59 d7 f7 10 97 37 10 00   ...GT...Y....7..
    0080 - 82 f7 cf 38 6f d5 d7 71-39 2f b2 31 93 57 1d 3d   ...8o..q9/.1.W.=
    0090 - be 3d e9 7e f4 63 3f ef-eb 59 dc f9 71 7a 38 c8   .=.~.c?..Y..qz8.

    Start Time: 1550315200
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```