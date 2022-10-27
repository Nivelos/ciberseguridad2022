# Ejercicios de tarea

## Descripcion

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/d6f9aa16d2a2c51d2e431e658d87af9e/shark1.pcapng).

## Pistas (Si hay)



## Solución

``` Bash

┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea ]
└─$ wireshark shark1.pcapng                                                               
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea ]
└─$ ls -la
total 1560
drwxr-xr-x  9 kali kali    4096 Oct 26 21:39  .
drwxr-xr-x 12 kali kali    4096 Oct 26 21:27  ..
drwxr-xr-x  2 kali kali    4096 Oct 26 21:21  information
-rw-r--r--  1 kali kali 1558808 Mar 15  2021  shark1.pcapng
drwxr-xr-x  2 kali kali    4096 Oct 26 21:03 'Untitled 2'
drwxr-xr-x  2 kali kali    4096 Oct 26 21:03 'Untitled 3'
drwxr-xr-x  2 kali kali    4096 Oct 26 21:03 'Untitled 4'
drwxr-xr-x  2 kali kali    4096 Oct 26 21:03 'Untitled 5'
drwxr-xr-x  2 kali kali    4096 Oct 26 21:03 'Untitled 6'
drwxr-xr-x  2 kali kali    4096 Oct 26 21:43 'Wireshark doo dooo do doo...'
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea ]
└─$ cd Wireshark\ doo\ dooo\ do\ doo... 
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /Wireshark doo dooo do doo...]
└─$ ls -la
total 16
drwxr-xr-x 2 kali kali 4096 Oct 26 21:43  .
drwxr-xr-x 9 kali kali 4096 Oct 26 21:39  ..
-rw-r--r-- 1 kali kali  756 Oct 26 21:43  TCPFollow
-rw-r--r-- 1 kali kali  230 Oct 26 21:37 'Wireshark doo dooo do doo....md'
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /Wireshark doo dooo do doo...]
└─$ nano TCPFollow 
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /Wireshark doo dooo do doo...]
└─$         


La bandera es: 

The flag is picoCTF{p
```

## Referencias