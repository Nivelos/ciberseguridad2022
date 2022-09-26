# Primer parcial 

## Descripcion

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag).

## Pistas (Si existen)

1.- Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.

2.- To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag`

3.- $ man cat

## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ wget https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag       
--2022-09-13 10:22:50--  https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: ‘flag’

flag                100%[================>]      34  --.-KB/s    in 0s      

2022-09-13 10:22:51 (46.3 MB/s) - ‘flag’ saved [34/34]

                                                                             
┌──(kali㉿kali)-[~]
└─$ ls
Desktop    Downloads  hacking  Pictures  Templates
Documents  flag       Music    Public    Videos
                                                                             
┌──(kali㉿kali)-[~]
└─$ cat flag 
picoCTF{s4n1ty_v3r1f13d_28e8376d}


```

## Referencias