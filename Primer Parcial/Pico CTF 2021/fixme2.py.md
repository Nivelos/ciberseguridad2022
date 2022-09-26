# Primer parcial 

## Descripcion

Fix the syntax error in the Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/65/fixme2.py)

## Pistas (Si hay)

1.- Are equality and assignment the same symbol?

2.- To view the file in the webshell, do: `$ nano fixme2.py

3.- To exit `nano`, press Ctrl and x and follow the on-screen prompts.`

4.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

``` Bash

┌──(kali㉿kali)-[~/Downloads]
└─$ python fixme2.py
  File "/home/kali/Downloads/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ 
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ nano fixme2.py  
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}

La sintaxis era incorrecta y la correguimos con un =

```

## Referencias