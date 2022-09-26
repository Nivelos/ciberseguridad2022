# Primer parcial 

## Descripcion

Our flag printing service has started glitching! `$ nc saturn.picoctf.net 51109`

## Pistas (Si hay)

1.- ASCII is one of the most common encodings used in programming

2.- We know that the glitch output is valid Python, somehow!

3.- Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ nc saturn.picoctf.net 51109 
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
                                                                             
┌──(kali㉿kali)-[~]
└─$ 
                                                                             
┌──(kali㉿kali)-[~]
└─$ nano pico.py  
                                                                             
┌──(kali㉿kali)-[~]
└─$ python pico.py 
picoCTF{gl17ch_m3_n07_bda68f75}

```

## Referencias