# Segundo parcial

## Descripcion

I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt) is all blank!

## Pistas (Si hay)



## Solución

``` Bash

Existen dos tipos de espacios en unicode, dandonos a entender que uno es el 0 y el otro es 1, haremos un pequeño script que nos ayudara a seguir el proceso y obtener la bandera

from pwn import *
file = open('whitepages.txt', 'rb')
data = bytearray(file.read())
data = data.replace(b'\xe2\x80\x83', b'0')
data = data.replace(b'\x20',b'1')
data = data.decode('ascii')
print(data)

Al momento de ejecutar el script nos aparece lo siguiente

┌──(kali㉿kali)-[~/picoCTF/Forensic/whitepages]
└─$ python binario.py
b'\n\t\tpicoCTF\n\n\t\tSEE PUBLIC RECORDS & BACKGROUND REPORT\n\t\t5000 Forbes Ave, Pittsburgh, PA 15213\n\t\tpicoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}\n\t\t'




```

## Referencias
