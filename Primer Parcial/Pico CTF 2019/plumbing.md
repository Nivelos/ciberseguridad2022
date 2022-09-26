# Primer parcial 

## Descripcion

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`.

## Pistas (Si hay)

1.- Remember the flag format is picoCTF{XXXX}

2.- What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ nc  jupiter.challenges.picoctf.org 14291 | grep {
picoCTF{digital_plumb3r_ea8bfec7}

```

## Referencias
