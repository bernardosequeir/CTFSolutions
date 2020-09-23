```bash
bandit12@bandit:~$ mkdir /tmp/bernardosequeir
bandit12@bandit:~$ cd /tmp/bernardosequeir
bandit12@bandit:/tmp/bernardosequeir$ ls
bandit12@bandit:/tmp/bernardosequeir$ cp ~/
.bash_logout  .bashrc       data.txt      .profile
bandit12@bandit:/tmp/bernardosequeir$ cp ~/data.txt .
bandit12@bandit:/tmp/bernardosequeir$ ls
data.txt
bandit12@bandit:/tmp/bernardosequeir$ ls
data.txt
bandit12@bandit:/tmp/bernardosequeir$ xxd -r data.txt > data
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data.txt
bandit12@bandit:/tmp/bernardosequeir$ file data
data: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/bernardosequeir$ gunzip data
gzip: data: unknown suffix -- ignored
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data.txt
bandit12@bandit:/tmp/bernardosequeir$ mv data data.gzip
bandit12@bandit:/tmp/bernardosequeir$ gunzip data.gzip
gzip: data.gzip: unknown suffix -- ignored
bandit12@bandit:/tmp/bernardosequeir$ mv data.gzip data.gz
bandit12@bandit:/tmp/bernardosequeir$ gunzip data.gz
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data.txt
bandit12@bandit:/tmp/bernardosequeir$ file data
data: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/bernardosequeir$ bunzip data
-bash: bunzip: command not found
bandit12@bandit:/tmp/bernardosequeir$ bunzip2 data
bunzip2: Can't guess original name for data -- using data.out
bandit12@bandit:/tmp/bernardosequeir$ file data.out
data.out: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/bernardosequeir$ mv data.out data.gz
bandit12@bandit:/tmp/bernardosequeir$ gunzip data.gz
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data.txt
bandit12@bandit:/tmp/bernardosequeir$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/bernardosequeir$ tar -xvf data
data5.bin
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data5.bin  data.txt
bandit12@bandit:/tmp/bernardosequeir$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/bernardosequeir$ tar -xvf data5.bin
data6.bin
bandit12@bandit:/tmp/bernardosequeir$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/bernardosequeir$ bunzip2 data6.bin
bunzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data5.bin  data6.bin.out  data.txt
bandit12@bandit:/tmp/bernardosequeir$ file data6.bin.out
data6.bin.out: POSIX tar archive (GNU)
bandit12@bandit:/tmp/bernardosequeir$ tar -xvf data6.bin.out
data8.bin
bandit12@bandit:/tmp/bernardosequeir$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/bernardosequeir$ mv data
data           data5.bin      data6.bin.out  data8.bin      data.txt
bandit12@bandit:/tmp/bernardosequeir$ mv data8.bin data8.gz
bandit12@bandit:/tmp/bernardosequeir$ gunzip data8.gz
bandit12@bandit:/tmp/bernardosequeir$ ls
data  data5.bin  data6.bin.out  data8  data.txt
bandit12@bandit:/tmp/bernardosequeir$ file data8
data8: ASCII text
bandit12@bandit:/tmp/bernardosequeir$ cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
