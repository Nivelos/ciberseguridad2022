# Ejercicios de tarea

## Descripcion

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar). The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

## Pistas (Si hay)

Maybe other passwords will have hints about the leak?

## Solución

``` Bash

El usuario cultiris es el numero 374, al momento de tomar su contraseña y pasarla por ROT13 nos da la bandera ya codificada

┌──(kali㉿kali)-[~/picoCTF/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff]
└─$ tar -xvf leak.tar 
leak/
leak/passwords.txt
leak/usernames.txt
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff]
└─$ ls -la
total 48
drwxr-xr-x 3 kali kali  4096 Nov  3 21:51 .
drwxr-xr-x 6 kali kali  4096 Nov  3 21:47 ..
-rw-r--r-- 1 kali kali   523 Nov  3 21:48 credstuff.md
drwxr-xr-x 2 kali kali  4096 Mar 15  2022 leak
-rw-r--r-- 1 kali kali 30720 Mar 15  2022 leak.tar
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff]
└─$ cd leak         
                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff/leak]
└─$ ls -la
total 32
drwxr-xr-x 2 kali kali  4096 Mar 15  2022 .
drwxr-xr-x 3 kali kali  4096 Nov  3 21:51 ..
-rwxr-xr-x 1 kali kali 13130 Mar 15  2022 passwords.txt
-rwxr-xr-x 1 kali kali  7531 Mar 15  2022 usernames.txt
                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff/leak]
└─$ open usernames.txt 
                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff/leak]
└─$ libva error: vaGetDriverNameByIndex() failed with unknown libva error, driver_name = (null)
[18740:1103/215122.826785:ERROR:gpu_memory_buffer_support_x11.cc(44)] dri3 extension not supported.
[main 2022-11-04T01:51:23.044Z] update#setState idle
[main 2022-11-04T01:51:25.291Z] Starting extension host with pid 18814 (fork() took 11 ms).
[main 2022-11-04T01:51:37.038Z] Extension host with pid 18814 exited with code: 0, signal: null.

                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff/leak]
└─$ open passwords.txt 
                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos Crypto picoCTF Ejercicios de Tarea/picoCTF 2022/credstuff/leak]
└─$ libva error: vaGetDriverNameByIndex() failed with unknown libva error, driver_name = (null)
[19037:1103/215147.344031:ERROR:gpu_memory_buffer_support_x11.cc(44)] dri3 extension not supported.
[main 2022-11-04T01:51:47.614Z] update#setState idle
[main 2022-11-04T01:51:49.831Z] Starting extension host with pid 19113 (fork() took 17 ms).
[main 2022-11-04T01:52:17.627Z] update#setState checking for updates
[main 2022-11-04T01:52:17.640Z] update#setState available for download


La bandera es:

picoCTF{C7r1F_54V35_71M3}

```

## Referencias