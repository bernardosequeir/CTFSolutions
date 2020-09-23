This level introduces command injection, so let's get right into it and get our hands dirty, this is one of the things that felt really cool when I was starting out, so I hope you like it.

All the code that matters for this level is displayed right here:

```php 
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

Let's focus on the [passthru](https://www.php.net/manual/en/function.passthru.php) function, it uses our input as a filter for the grep command, and it's our only way of interacting with the website so we've gotta do something with it! What happens if you insert a ; in the middle of a bash command? Oh, you interrupt it? And in this case we can run anything we want instead of that lousy grep? Huh maybe if we cat /etc/natas_webpass/natas10 we can get the password 😉
