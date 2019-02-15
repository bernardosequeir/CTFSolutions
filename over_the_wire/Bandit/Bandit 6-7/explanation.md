```bash find: ‘/run/lvm’: Permission denied
find: ‘/run/screen/S-bandit15’: Permission denied
find: ‘/run/screen/S-bandit9’: Permission denied
find: ‘/run/screen/S-bandit8’: Permission denied
find: ‘/run/screen/S-bandit7’: Permission denied
find: ‘/run/screen/S-bandit3’: Permission denied
find: ‘/run/screen/S-bandit2’: Permission denied
find: ‘/run/screen/S-bandit1’: Permission denied
find: ‘/run/screen/S-bandit30’: Permission denied
find: ‘/run/screen/S-bandit16’: Permission denied
find: ‘/run/screen/S-bandit27’: Permission denied
find: ‘/run/screen/S-bandit26’: Permission denied
find: ‘/run/screen/S-bandit17’: Permission denied
find: ‘/run/screen/S-bandit28’: Permission denied
find: ‘/run/screen/S-bandit22’: Permission denied
find: ‘/run/screen/S-bandit10’: Permission denied
find: ‘/run/screen/S-bandit31’: Permission denied
find: ‘/run/screen/S-bandit4’: Permission denied
find: ‘/run/screen/S-bandit13’: Permission denied
find: ‘/run/screen/S-bandit14’: Permission denied
find: ‘/run/screen/S-bandit23’: Permission denied
find: ‘/run/screen/S-bandit24’: Permission denied
find: ‘/run/screen/S-bandit5’: Permission denied
find: ‘/run/screen/S-bandit25’: Permission denied
find: ‘/run/screen/S-bandit20’: Permission denied
find: ‘/run/screen/S-bandit21’: Permission denied
find: ‘/run/shm’: Permission denied
find: ‘/run/lock/lvm’: Permission denied
find: ‘/var/spool/bandit24’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/log’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/cache/apt/archives/partial’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
find: ‘/cgroup2/csessions’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/home/bandit31-git’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/tmp’: Permission denied
find: ‘/lost+found’: Permission denied
find: ‘/root’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/etc/lvm/backup’: Permission denied
find: ‘/etc/lvm/archive’: Permission denied
find: ‘/etc/polkit-1/localauthority’: Permission denied
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/4332/task/4332/fd/6’: No such file or directory
find: ‘/proc/4332/task/4332/fdinfo/6’: No such file or directory
find: ‘/proc/4332/fd/5’: No such file or directory
find: ‘/proc/4332/fdinfo/5’: No such file or directory
find: ‘/boot/lost+found’: Permission denied
bandit6@bandit:~$ find / -user "bandit7" -group "bandit6" -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```