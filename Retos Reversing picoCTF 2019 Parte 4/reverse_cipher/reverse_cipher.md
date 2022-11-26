# Metared International CTF 2022

## Descripcion

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev_this). Can you reverse the flag.

## Pistas (Si hay)

objdump and Gihdra are some tools that could assist with this

## Solución

``` Bash

Utilizamos ghidra para cambiar las variables desde el decompilador, al final nos arroja la bandera

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/reverse_cipher]
└─$ python3 exp.py
picoCTF{w1{1wq84fb<1>49}
r3v3rs36ad73964

```

## Referencias