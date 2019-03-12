# Bandit Wargame Write-Up

Bandit is the easiest wargame that the folks at [OverTheWire](http://overthewire.org) have to offer, it's great for people who are getting into CyberSecurity and don't know much about Linux/unix and working in a shell.

This write-up is currently being written as I'm playing this wargame again and now trying to document everything, so if something isn't here just wait a couple of days and then it might be here! 😁

### Bandit 0 -> 1 

First of all, and this is almost the same for every level, so I won't do it again, we have to ssh into the server, to do that we just need to do:
```bash 
     ssh bandit0@bandit.labs.overthewire.org -p 2220
 ```

And then input the password when it is asked (bandit0). 

If you have never used ssh before, it's really simple, you just specify the user you want to login as (in this case bandit0), the domain that that user belongs to (bandit.labs.overthewire.org) , and then, if you need to ssh into a specific port, you use -p to do it.

So then all that's left is to get the password for Bandit 1 from the readme file.

The file is in the home folder, which is where we were dropped in when we connected so, you can just cat it out.

```bash 
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

### Bandit 1 -> 2 

Before starting this explanation, I have to say two things:

1. It's okay to make mistakes, it's how you learn, I've left some failures in the code presented here because trying things out is **THE BEST WAY** to figure out if it works or not.

2. If you are new to this, the hints and suggested links in the pages for the levels of this game really help out, along with checking out other people's write-ups and videos on youtube (S/o [John Hammond](https://www.youtube.com/user/RootOfTheNull/featured), he has a great playlist where he goes through every level of this game). In my opinion, there is nothing wrong with checking out write-ups when you're just starting out, it's way faster to learn this way.

So onwards with the explanation, **-** is a special character for bash - it is how you specify options for the programs you use and can also be used to redirect *stdin* and *stdout*. As you can see in my example below, if you just try to cat it out normally it doesn't work, you have to provide the full path (starting on the folder you are on, in this case), this is often the solution for challenges similar to this, so keep this one on your back-pocket.

```bash
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat -

^C
bandit1@bandit:~$ cat "-"

^C
bandit1@bandit:~$ cat *
^C
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

### Bandit 2 -> 3 

Similar to the level before, this time you have to cat out a file with spaces in its file name, but you can beat this one in an even easier way, if you are not aware of it, bash supports [tab-completion](https://en.wikipedia.org/wiki/Command-line_completion), and its one of the most useful things it has, if you write just the "s" of "spaces" and hit Tab, the "s" will expand to the full filename, properly escaped and ready to use, so you avoid learning how to handle files with spaces in their names (even though you kinda do learn it, it's just adding a \ at the end of each word, so that it escapes the space "character")  

```bash 
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

### Bandit 3 -> 4 

This level introduces the concept of [hidden files](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory), but don't fret, it's not hard to deal with them, if you run ***ls -a*** they become visible, but I'd argue that it's even  better to use ***ls-la***, as it shows all files and directories (hidden or not) and displayed neatly in a table with loads of information (don't worry, over time, you begin to know what it all means and start using without event thinking).

So, after knowing that, we can just cat the hidden file like it's nothing.

```bash 
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct 16 14:00 .
drwxr-xr-x 3 root    root    4096 Oct 16 14:00 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 16 14:00 .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

### Bandit 4 -> 5

This level introduces *-expansion (I don't know if that's the actual name, sorry), basically if you use the asterisk on a command like file, like ```file *```, it will try to run the file command on all the files on the current folder. Due to the weird file names on this folder, we have to adapt the solution we used on level 2. I've left my error in the below code so that you can see what I mean (Not sure why the colours are messed up but they are, sorry for that).

```bash 
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ ls -la
total 48
drwxr-xr-x 2 root    root    4096 Oct 16 14:00 .
drwxr-xr-x 3 root    root    4096 Oct 16 14:00 ..
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file00
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file01
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file02
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file03
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file04
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file05
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file06
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file07
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file08
-rw-r----- 1 bandit5 bandit4   33 Oct 16 14:00 -file09
bandit4@bandit:~/inhere$ file *
file: Cannot open `ile00' (No such file or directory).
file: Cannot open `ile01' (No such file or directory).
file: Cannot open `ile02' (No such file or directory).
file: Cannot open `ile03' (No such file or directory).
file: Cannot open `ile04' (No such file or directory).
file: Cannot open `ile05' (No such file or directory).
file: Cannot open `ile06' (No such file or directory).
file: Cannot open `ile07' (No such file or directory).
file: Cannot open `ile08' (No such file or directory).
file: Cannot open `ile09' (No such file or directory).
bandit4@bandit:~/inhere$ file ./-*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

### Bandit 5 -> 6

This level serves as an introduction to the ***find*** command, and the flags you can youse with it, in this case, the ***-size*** flag. Okay, so you could need to use more than that but it just happens that there's only one file with 1033 bytes in size so we can keep it simple for this level. Using ***find -size 1033c*** (c is for Bytes ??? I guess?) you are presented with a list of files, recursively found within the folders inside the current directory.   

```bash 
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ ls -la
total 88
drwxr-x--- 22 root bandit5 4096 Oct 16 14:00 .
drwxr-xr-x  3 root root    4096 Oct 16 14:00 ..
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere00
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere01
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere02
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere03
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere04
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere05
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere06
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere07
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere08
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere09
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere10
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere11
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere12
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere13
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere14
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere15
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere16
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere17
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere18
drwxr-x---  2 root bandit5 4096 Oct 16 14:00 maybehere19
bandit5@bandit:~/inhere$ find -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    bandit5@bandit:~/inhere$
```

By the way, when you run ***ls -la*** if the first letter in the permissions column is a d, it means that it's a file, these details help in the long run.

Also, you might have been confused as why your terminal looks messed up after cat'ing out the password, I was when I first saw it, but it's actually the reason the file has 1033 bytes, the file is just the password and then a bunch of spaces.

### Bandit 6 -> 7

On the description for this level it is hinted that the file can be anywhere on the server so we need to use ***/*** on our ***find*** command so that it searches starting on the base folder of the server, in this level we also need to use the ***-user*** and ***-group*** flags on the ***find*** command.  

```bash
bandit6@bandit:~$ find / -user "bandit7" -group "bandit6" -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

If you try to run the ***find*** without the ***2>/dev/null*** you'll have some problems trying to find the file that is returned on the command when it's there, that's because the snippet at the end redirects the errors (stderr) to ***dev/null*** aka nowhere, and just leaves the normal output for us (stdout). Keep those names in mind, you will eventually need to learn more about them.

### Bandit 7 -> 8

This level serves as in introduction to the ***grep*** command, which is useful to find a certain word or pattern inside a file. Using it makes this level take seconds to complete, which is ridiculous if you think of the time it would take to check the 98567(!!!) lines of this file by hand.
```bash
bandit7@bandit:~$ wc -l data.txt
98567 data.txt
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

