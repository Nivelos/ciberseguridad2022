# Primer parcial 

## Descripcion

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static)? This [BASH script](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh) might help!

## Pistas (Si hay)



## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ cd Downloads 
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 808
drwxr-xr-x  2 kali kali   4096 Sep 26 01:11 .
drwxr-xr-x 19 kali kali   4096 Sep 26 01:07 ..
-rw-r--r--  1 kali kali  14551 Sep 21 20:01 file
-rw-r--r--  1 kali kali   8376 Sep 26 01:11 static
-rw-r--r--  1 kali kali 776032 Sep 21 20:13 strings
-rw-r--r--  1 kali kali  10936 Sep 21 20:28 warm
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ strings static | grep pico               
picoCTF{d15a5m_t34s3r_ccb2b43e}


```

## Referencias