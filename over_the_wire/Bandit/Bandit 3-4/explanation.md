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