# Segundo parcial

## Descripcion

This [garden](https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg) contains more than it seems.

## Pistas (Si hay)

What is a hex editor?

## Solución

``` Bash

┌──(kali㉿kali)-[~/picoCTF/Forensic/gloryofgarden]
└─$ strings garden.jpg -n 15 | grep pico  
Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"

o podemos utilizar el editor hexidecimal con el siguiente comando

┌──(kali㉿kali)-[~/picoCTF/Forensic/gloryofgarden]
└─$ hexeditor garden.jpg  

```

## Referencias
