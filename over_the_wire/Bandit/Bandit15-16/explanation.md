```bash
bandit14@bandit:~$ openssl s_client -connect localhost:30001
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
MIICBjCCAW+gAwIBAgIEYo1NxTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjAwMTA1MTQzNTU4WhcNMjEwMTA0MTQzNTU4WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKF4u2eu
a8VipZPviX0hfNiCnaD2ojAffdBhKTy1bmZSNRuHPBDnU7z8rblNSknSjCITda1C
GEAI8ZktRbtLpBTbYeTgqPN/EiN5UIRMKbU6P2O93zNFPBsmyfQLrgt+DSLnsxlB
i/yYyT7WLdtNVBpgwRwkqi9K7dk9vf9waswLAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAJECW6IB3Ria4xG002BqD3zEbtmrDlK6nmJq+uQ4eJ6cT18o9REb
npy/lFzlv2LfcrYAnuAp6Fh89MKaYjNzJURjRQ9RkmcYgQJa1n+OBkATb7V+84/a
k9PDRkscxdNFMGBSvzFD33XZ5lbaGdrwCPyoxenoYghV/753wffN7J6H
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
    Session-ID: 414837D1C525B44297DC83E2037247706958FE89BE0F7DEE42555BEA04112E23
    Session-ID-ctx:
    Master-Key: F081B92A22240EF6F26581D067BEEF9D1AAE775746137CF8607BB5AD3838EE506192943718B778D5789E7DB7F28CFA2C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 56 e9 4e 87 6a 28 48 d0-13 42 5f b9 61 b0 dd d0   V.N.j(H..B_.a...
    0010 - 3d 3f 27 f7 c6 bc b9 4c-c9 59 06 8f d4 76 72 49   =?'....L.Y...vrI
    0020 - 0d 8f 4f 05 00 7a bc fb-59 bf d9 82 e1 e4 41 5a   ..O..z..Y.....AZ
    0030 - a7 6a 1c f1 15 96 d0 c6-90 68 e4 46 56 fe 11 0c   .j.......h.FV...
    0040 - 35 1d 74 d3 5a 05 4b 63-c6 36 6d db 45 a2 cf 2d   5.t.Z.Kc.6m.E..-
    0050 - 18 07 67 a1 86 bd 42 6c-ed 11 c1 db 9a f9 5b 00   ..g...Bl......[.
    0060 - ac 37 04 b4 b5 98 70 d5-26 5f d8 38 97 7c de ef   .7....p.&_.8.|..
    0070 - 84 cb 8d cc b6 de fa f0-e9 51 3b 0c 98 6f e4 ef   .........Q;..o..
    0080 - 9f 93 cf 85 df 54 37 29-01 13 5b 82 8e 1d bf e5   .....T7)..[.....
    0090 - 21 24 b8 07 3b 54 67 06-a3 fc 27 0d ab 48 f6 53   !$..;Tg...'..H.S

    Start Time: 1583581126
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```
