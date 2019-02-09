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