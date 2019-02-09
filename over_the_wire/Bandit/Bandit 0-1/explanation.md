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