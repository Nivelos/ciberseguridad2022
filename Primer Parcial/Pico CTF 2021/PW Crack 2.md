# Primer parcial 

## Descripcion

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/18/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level2.flag.txt.enc) in the same directory too.

## Pistas (Si hay)

1.- Does that encoding look familiar?

2.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

``` Bash

┌──(kali㉿kali)-[~/Downloads]
└─$ nano level2.py  
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ nano contralevel2.py
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python contralevel2.py 
39ce
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python level2.py    
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}

La contraseña esta encriptada en ASCII, tome la contraseña del archivo level2 e hice un programa que me imprimiera la traduccion de este en texto, al final la contraseña era 39ce

```

## Referencias