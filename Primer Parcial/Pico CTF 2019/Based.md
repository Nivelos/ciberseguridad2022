# Primer parcial Based

## Descripcion

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.

## Pistas (Si hay)

1.- I hear python can convert things.

2.- It might help to have multiple windows open.

## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
sludge
Please give the 01110011 01101100 01110101 01100100 01100111 01100101 as a word.
...
you have 45 seconds.....

Input:
sludge
Please give me the  163 165 142 155 141 162 151 156 145 as a word.
Input:
submarine
Please give me the 636f6d7075746572 as a word.
Input:
computer
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}


```

## Referencias

https://onlinetexttools.com/convert-octal-to-text

https://www.rapidtables.com/convert/number/binary-to-ascii.html

https://www.duplichecker.com/hex-to-text.php