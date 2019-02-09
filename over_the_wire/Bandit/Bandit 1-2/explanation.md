### Bandit 1 -> 2 Solution

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