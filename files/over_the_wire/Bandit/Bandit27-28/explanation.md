```bash
bandit27@bandit:~$ cd /tmp/bernardo
bandit27@bandit:/tmp/bernardo$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password:
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/bernardo$ ls
bruteforce.sh  f1  f2  messages  nc  repo  results  s.sh  totallynotthepass.txt
bandit27@bandit:/tmp/bernardo$ cd repo/
bandit27@bandit:/tmp/bernardo/repo$ ls
README
bandit27@bandit:/tmp/bernardo/repo$ cat README
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
bandit27@bandit:/tmp/bernardo/repo$
```