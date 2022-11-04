# Crypto 2019

## Descripcion

We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/394/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Pistas (Si hay)

1.- Do you know what `mod 37` means?

2.- `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.

## Solución

``` Bash

──(kali㉿kali)-[~/picoCTF/Retos Crypto picoCTF 2019 - Parte 3/basic - mod 1]
└─$ python3 exp.py 
['202', '137', '390', '235', '114', '369', '198', '110', '350', '396', '390', '383', '225', '258', '38', '291', '75', '324', '401', '142', '288', '397']
R0UND_N_R0UND_B6B2553

La bandera quedaria como:

picoCTF{R0UND_N_R0UND_B6B2553}

```

## Referencias