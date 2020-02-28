---
title: "Over The Wire Bandit Wargame Write-Up"
---

## Bandit 0->1

### How To Connect

```bash
ssh bandit.labs.overthewire.org -p 2220 -l bandit0
```

### How To Get The Pass

```bash
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

## Bandit 1->2

```bash
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

The dash (-) is a synonym for stdin, so if you just put it in front of cat it will just present a prompt for you to write. So you need to provide the relative path, because this way, bash can grasp that we are talking about a file.

## Bandit 0->1

```bash
bandit2@bandit:~$ cat ./
.bash_logout             .bashrc                  .profile                 spaces in this filename
bandit2@bandit:~$ cat ./spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

This is be a challenge because cat uses the space as a delimiter between arguments, so you can either "escape" the space character (using the \\), or in this case, you can just use tab autocompletion, because there aren't any other files that start with an 's'
