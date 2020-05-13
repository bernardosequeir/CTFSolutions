So... I'm pretty sure that this is not the intended solution for this level but ... it worked so I don't really care.
 
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```
This level tries to fix your command injection by catching the use of the characters you regularly use to do it. After seeing that they were only banning three things I was kinda suspicious and thought to check the [OWASP page for command injection](https://owasp.org/www-community/attacks/Command_Injection) and I was greatly rewarded. At the bottom it talks about mitigation and how you should not only block ";" but also "&&", "|" and "...". Wait what? "..."? Let's try it out with essentially the same command as the last level:

![Print Screen of the page]("../Images/Natas10.png")