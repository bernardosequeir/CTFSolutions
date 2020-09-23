```bash
bandit2@bandit:~$ cat ./
.bash_logout             .bashrc                  .profile                 spaces in this filename
bandit2@bandit:~$ cat ./spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

This is be a challenge because cat uses the space as a delimiter between arguments, so you can either "escape" the space character (using the \\), or in this case, you can just use tab autocompletion, because there aren't any other files that start with an 's'
