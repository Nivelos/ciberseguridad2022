# Primer parcial Strings it

## Descripcion

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

## Pistas (Si hay)

[strings](https://linux.die.net/man/1/strings)

## Solución

``` Bash

┌──(kali㉿kali)-[~/Downloads]
└─$ strings -d strings | grep pico
picoCTF{5tRIng5_1T_d66c7bb7}

```

## Referencias

https://www.educba.com/linux-string-command/