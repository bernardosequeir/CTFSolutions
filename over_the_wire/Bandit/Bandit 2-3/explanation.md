Similar to the level before, this time you have to cat out a file with spaces in its file name, but you can beat this one in an even easier way, if you are not aware of it, bash supports [tab-completion](https://en.wikipedia.org/wiki/Command-line_completion), and its one of the most useful things it has, if you write just the "s" of "spaces" and hit Tab, the "s" will expand to the full filename, properly escaped and ready to use, so you avoid learning how to handle files with spaces in their names (even though you kinda do learn it, it's just adding a \ at the end of each word, so that it escapes the space "character")  

```bash 
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK