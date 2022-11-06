# Reversing

## Descripcion

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://jupiter.challenges.picoctf.org/static/d31ce4356bdfd15d33a9af7e35ab4d0a/VaultDoor5.java)

## Pistas (Si hay)

1.- You may find an encoder/decoder tool helpful, such as https://encoding.tools/

2.- Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

## Solución

``` Bash

En el codigo tenemos un texto en base64, al decodificarlo tenemos otro texto pero ahora en codificacion de URL, al momento de decodificarlo tenemos la badnera, la cual es:

picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}

┌──(kali㉿kali)-[~/picoCTF/Retos Reversing picoCTF 2019 Parte 2/vault-door-5]
└─$ javac VaultDoor5.java | code VaultDoor5.java                                                      
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Reversing picoCTF 2019 Parte 2/vault-door-5]
└─$ java VaultDoor5                             
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}
Access granted.


```

## Referencias