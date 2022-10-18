# picoCTF 2021

## Descripcion

We found this [file](https://mercury.picoctf.net/static/d0129ad98ba9258ab59e7700a1b18c14/tunn3l_v1s10n). Recover the flag.

## Pistas (Si hay)

Weird that it won't display right...

## Solución

``` Bash

Se edita el hexadecimal de el archivo dado para reparar la imagen y que sea visible

┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ xxd tunn3l_v1s10n.bmp | head
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 bad0  BM.&,...........
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
00000040: 211e 261d 1a31 2825 352c 2933 2a27 382f  !.&..1(%5,)3*'8/
00000050: 2c2f 2623 332a 262d 2420 3b32 2e32 2925  ,/&#3*&-$ ;2.2)%
00000060: 3027 2333 2a26 382c 2836 2b27 392d 2b2f  0'#3*&8,(6+'9-+/
00000070: 2623 1d12 0e23 1711 2916 0e55 3d31 9776  &#...#..)..U=1.v
00000080: 668b 6652 996d 569e 7058 9e6f 549c 6f54  f.fR.mV.pX.oT.oT
00000090: ab7e 63ba 8c6d bd8a 69c8 9771 c193 71c1  .~c..m..i..q..q.
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ 
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ hexeditor tunn3l_v1s10n.bmp     
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ open tunn3l_v1s10n.bmp 
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ exiftool tunn3l_v1s10n.bmp 
ExifTool Version Number         : 12.44
File Name                       : tunn3l_v1s10n.bmp
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2022:10:11 09:36:05-04:00
File Access Date/Time           : 2022:10:11 09:36:14-04:00
File Inode Change Date/Time     : 2022:10:11 09:36:05-04:00
File Permissions                : -rw-r--r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Windows V3
Image Width                     : 1134
Image Height                    : 306
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 2627109
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Image Size                      : 1134x306
Megapixels                      : 0.347
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ python3 -c 'print(hex(1134))'
0x46e
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ hexeditor tunn3l_v1s10n.bmp
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ open tunn3l_v1s10n.bmp    
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/tunn3l_v1s10n]
└─$ 


picoCTF{qu1t3_a_v13w_2020}

```

## Referencias