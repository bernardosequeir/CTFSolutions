```bash
bandit20@bandit:~$ nc -lvnp 3000
listening on [any] 3000 ...
^Z
[1]+  Stopped                 nc -lvnp 3000
bandit20@bandit:~$ ./suconnect 3000
^Z
[2]+  Stopped                 ./suconnect 3000
bandit20@bandit:~$ fg 1
nc -lvnp 3000
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 43954
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
^Z
[1]+  Stopped                 nc -lvnp 3000
bandit20@bandit:~$ fg 2
./suconnect 3000
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
bandit20@bandit:~$ fg 1
nc -lvnp 3000
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```
