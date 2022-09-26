# Primer parcial First GRep

## Descripcion

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Pistas (Si hay)

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solución

``` Bash

Abri el archivo y busque el caracter "{}" encontrando la contraseña picoCTF{grep_is_good_to_find_things_f77e0797}

Igualmente utilice la consola con el comando grep para encontrar el caracter especial "{}"

┌──(kali㉿kali)-[~/Downloads]
└─$ grep { file
picoCTF{grep_is_good_to_find_things_f77e0797}


```

## Referencias

https://ryanstutorials.net/linuxtutorial/grep.php