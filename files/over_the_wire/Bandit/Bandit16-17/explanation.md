```bash

bandit15@bandit:~$ nmap -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2020-03-07 12:47 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00022s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
bandit15@bandit:~$ openssl s_client -connect localhost:31046 -ign_eof
CONNECTED(00000003)
140234854395968:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:284:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 176 bytes and written 183 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID:
    Session-ID-ctx:
    Master-Key:
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1583581919
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
---
bandit15@bandit:~$ openssl s_client -connect localhost:31518 -ign_eof
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIES250rzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjAwMjA5MjA0NzIwWhcNMjEwMjA4MjA0NzIwWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBANWyxh7K
T86zWM4NFe95x2KNEBUDz2XlGvU7KxUM9z1OfakmLDYCiujYdR6gI4ZBtyhEql5P
taCiNWO+ZDJCKWhjH/TyIywxjW9/PBHRC8UEzhsxc0wMHbLrlYFwzxT2KjhI3EVY
5VIWkzKrgHuON6PuBbmN0g0z5NN/xYch4kPpAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAFX4+KlTXWb4R/pUVt7i4FWvp3CuqgLUtgU3vRZqJ3wShIyDbsFK
a4S9uSuWcLLvyq0aa4kLhmoepyNlI3BGUSZZbRXwo/1e5IpCX3RdHhlIc3/Sd7ln
usTkejgEftWMmmBc03RY07EMxbNeXE8zzh2NP+5kVfwWG6GoGuQMXhy8
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 0E4100E039967B43A5161E5158C8A59C8F2164D9B75B2FB228237151B2F5615D
    Session-ID-ctx:
    Master-Key: 35788996799A49FF0334146313AA273BFF56E22EC0AFCEC7D5B3CC532F9F5C4FF6D817357E6A42F06E4260D610BC03A8
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 26 1a 05 91 72 ce a3 a6-e5 fa 17 b1 24 c4 2b 6f   &...r.......$.+o
    0010 - 52 d4 59 11 78 0a 4a 49-ed 57 57 4c e3 a0 9e 18   R.Y.x.JI.WWL....
    0020 - 98 db cb 36 1a 01 2c 73-60 f4 b6 fb 61 f8 7b a0   ...6..,s`...a.{.
    0030 - 5c 94 bc f6 c3 06 52 1d-96 2d 6e 54 ea d0 35 65   \.....R..-nT..5e
    0040 - e1 07 27 b4 fb cd c4 a8-de 08 f1 dc 0e c0 19 7c   ..'............|
    0050 - 32 a2 2c 28 48 c8 2b f9-63 4e c2 86 82 0b 1e 65   2.,(H.+.cN.....e
    0060 - aa 60 b4 43 90 03 09 97-54 a8 24 f6 8d a6 76 0c   .`.C....T.$...v.
    0070 - a9 d9 e0 f8 c6 b7 db 4d-fa af b7 04 6b 2a 36 5f   .......M....k*6_
    0080 - 93 7b 83 c1 3f 25 5f 4b-24 f3 b1 b1 a2 bf 47 bd   .{..?%_K$.....G.
    0090 - 8d 7f 6a 51 9e ed 2b e2-bf 28 39 a9 a4 b9 c2 0d   ..jQ..+..(9.....

    Start Time: 1583581937
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
cluFn7wTiGryunymYOu4RcffSxQluehd
^C
bandit15@bandit:~$ openssl s_client -connect localhost:31790 -ign_eof
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEGPttrzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjAwMjA5MjA0NzE5WhcNMjEwMjA4MjA0NzE5WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAPiElqK1
D097ZCNDgKFxqX1ZUUpFfuoiDSP2dw5KrIruaTQMmfqCxo6dSHvkj1sF//YRI28k
BGyu9pE3zLO45uk4PrjoORYLoQjTCb61oVZLECCOIG21WQUbrhjW4zlZGmtWrqw6
zGLk7dZ8MeYHVSvK0n3Ar45hVedpsLC618ZTAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBADJEAM0VceCYaqhfzpzkzf6dhCIWbb/8P+51Wxw24sn9iLHxdqYe
1WNfxtQb8IYb3q/6JJDJ3d6plNKmFMkFBe5AiN05PCDeMymkTv8vlKj18UNR/4GL
AH1aFGcEYVXkwX0Kl844muUrK7S0AbOvcHmzzA++qTmfB1UK264G0iAH
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 52B1D187A419A11F4D4BB0D89144E934B9A585707C4CC8FA647F70FB56D62169
    Session-ID-ctx:
    Master-Key: DC0A9F5CF2D8D3E4F663D0E1F509DD042E62C8B5BAF6B0350FA91C41681CF0CED043B5E9DF4588C0B1B2098EC9728F2E
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 9f 82 12 97 ac 31 10 5b-65 4b 5d fb 71 e9 e8 02   .....1.[eK].q...
    0010 - fa e6 c8 4f b4 43 67 3a-c3 d8 df 16 3c 48 b0 2a   ...O.Cg:....<H.*
    0020 - 9b a7 4c 27 ad 83 d3 44-84 7f 2d 85 7f fd 85 eb   ..L'...D..-.....
    0030 - 74 2e 2c 6a e1 f6 af 1d-5f 2d 19 cb 41 44 65 38   t.,j...._-..ADe8
    0040 - df bf d0 b1 cd cc f9 c8-ec e8 47 b9 bb 86 78 61   ..........G...xa
    0050 - 69 39 47 b6 7d 70 f8 9d-9f b8 7b ac 23 f5 99 51   i9G.}p....{.#..Q
    0060 - 4d 3c 53 fe 94 5a 64 e8-6d 23 e5 a6 7b 2e d3 a9   M<S..Zd.m#..{...
    0070 - fb 05 4d 2b 74 77 fb b4-b4 98 6b 20 56 27 97 70   ..M+tw....k V'.p
    0080 - eb 1d 29 aa 92 b6 8c 0a-fb b5 74 dd d3 33 c2 4b   ..).......t..3.K
    0090 - 96 91 84 60 79 47 c7 d6-9f 66 ae 06 98 77 4a b4   ...`yG...f...wJ.

    Start Time: 1583582074
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```
