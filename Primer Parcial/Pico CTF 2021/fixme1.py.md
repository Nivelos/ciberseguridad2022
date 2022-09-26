# Primer parcial 

## Descripcion

Fix the syntax error in this Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/39/fixme1.py)

## Pistas (Si hay)

1.- Indentation is very meaningful in Python

2.- To view the file in the webshell, do: `$ nano fixme1.py`

3.- To exit `nano`, press Ctrl and x and follow the on-screen prompts.

4.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

``` Bash

┌──(kali㉿kali)-[~/Downloads]
└─$ python fixme1.py
  File "/home/kali/Downloads/fixme1.py", line 20
    print('That is correct! Here\s your flag: ' + flag)
IndentationError: unexpected indent
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ nano fixme1.py  
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python fixme1.py
That is correct! Heres your flag: picoCTF{1nd3nt1ty_cr1515_182342f7}

Estaba mas identado y correguimos eso

```

## Referencias