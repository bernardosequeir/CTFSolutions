from pwn import *
r = remote("echo.tghack.no",5555)
for x in range(50):
    line = r.recvline()
    print line
    r.send(line)
print r.recvline()

#flag TG19{behold_the_echo_chamber_of_secrets}