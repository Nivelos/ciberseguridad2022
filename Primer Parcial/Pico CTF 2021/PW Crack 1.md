# Primer parcial 

## Descripcion

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/52/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/52/level1.flag.txt.enc) in the same directory too.

## Pistas (Si hay)

1.- To view the file in the webshell, do: `$ nano level1.py`

2.- To exit `nano`, press Ctrl and x and follow the on-screen prompts.

3.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

``` Bash

┌──(kali㉿kali)-[~/Downloads]
└─$ nano level1.py        
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}

En el codigo de python esta la contraseña que tenemos que poner, la cual es 1e1a

```

## Referencias