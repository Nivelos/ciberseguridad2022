# picoCTF 2021

## Descripcion

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg)

## Pistas (Si hay)

1.- Wait, you can hide files inside files? But how do you find them?

2- Make sure to submit the flag as picoCTF{XXXXX}

## Solución

``` Bash

┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3]
└─$ ls -la
total 660
drwxr-xr-x 4 kali kali   4096 Oct 11 09:10  .
drwxr-xr-x 7 kali kali   4096 Oct 11 09:08  ..
-rw-r--r-- 1 kali kali 651636 Mar 15  2021  dolls.jpg
drwxr-xr-x 2 kali kali   4096 Oct 11 09:09 'Matryoshka doll'
drwxr-xr-x 2 kali kali   4096 Oct 11 09:09  .obsidian
-rwxrwx--- 1 kali kali    108 Oct 10 20:30 'Plantilla 1.md'
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3]
└─$ cd Matryoshka\ doll                                 
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll]
└─$ ls -la
total 652
drwxr-xr-x 2 kali kali   4096 Oct 11 09:11 .
drwxr-xr-x 4 kali kali   4096 Oct 11 09:11 ..
-rw-r--r-- 1 kali kali 651636 Mar 15  2021 dolls.jpg
-rw-r--r-- 1 kali kali    108 Oct 11 09:10 Untitled.md
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll]
└─$ binwalk dolls.jpg -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378956, uncompressed size: 383938, name: base_images/2_c.jpg
651614        0x9F15E         End of Zip archive, footer length: 22

                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll]
└─$ cd _dolls.jpg.extracted 
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll/_dolls.jpg.extracted]
└─$ ls -la
total 384
drwxr-xr-x 3 kali kali   4096 Oct 11 09:11 .
drwxr-xr-x 3 kali kali   4096 Oct 11 09:11 ..
-rw-r--r-- 1 kali kali 379144 Oct 11 09:11 4286C.zip
drwxr-xr-x 2 kali kali   4096 Oct 11 09:11 base_images
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll/_dolls.jpg.extracted]
└─$ open base_images 
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll/_dolls.jpg.extracted]
└─$ ls -la
total 384
drwxr-xr-x 3 kali kali   4096 Oct 11 09:11 .
drwxr-xr-x 3 kali kali   4096 Oct 11 09:11 ..
-rw-r--r-- 1 kali kali 379144 Oct 11 09:11 4286C.zip
drwxr-xr-x 2 kali kali   4096 Oct 11 09:11 base_images
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll/_dolls.jpg.extracted]
└─$ cd base_images         
                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll/_dolls.jpg.extracted/base_images]
└─$ binwalk 2_c.jpg -e  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg
383805        0x5DB3D         End of Zip archive, footer length: 22
383916        0x5DBAC         End of Zip archive, footer length: 22

                                                                                                                    
┌──(kali㉿kali)-[~/…/Retos: Forensic picoCTF 2021,2022 - Parte 3/Matryoshka doll/_dolls.jpg.extracted/base_images]
└─$ cd _2_c.jpg.extracted/base_images 
                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls -la
total 208
drwxr-xr-x 2 kali kali   4096 Oct 11 09:13 .
drwxr-xr-x 3 kali kali   4096 Oct 11 09:13 ..
-rw-r--r-- 1 kali kali 201445 Mar 15  2021 3_c.jpg
                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ open 3_c.jpg    
                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ binwalk 3_c.jpg   

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79808, name: base_images/4_c.jpg
201423        0x312CF         End of Zip archive, footer length: 22

                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls -la
total 208
drwxr-xr-x 2 kali kali   4096 Oct 11 09:13 .
drwxr-xr-x 3 kali kali   4096 Oct 11 09:13 ..
-rw-r--r-- 1 kali kali 201445 Mar 15  2021 3_c.jpg
                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ binwalk 3_c.jpg -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79808, name: base_images/4_c.jpg
201423        0x312CF         End of Zip archive, footer length: 22

                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls -la                           
total 212
drwxr-xr-x 3 kali kali   4096 Oct 11 09:14 .
drwxr-xr-x 3 kali kali   4096 Oct 11 09:13 ..
-rw-r--r-- 1 kali kali 201445 Mar 15  2021 3_c.jpg
drwxr-xr-x 3 kali kali   4096 Oct 11 09:14 _3_c.jpg.extracted
                                                                                                                    
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ cd _3_c.jpg.extracted/base_images 
                                                                                                                    
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ ls -la
total 88
drwxr-xr-x 2 kali kali  4096 Oct 11 09:14 .
drwxr-xr-x 3 kali kali  4096 Oct 11 09:14 ..
-rw-r--r-- 1 kali kali 79808 Mar 15  2021 4_c.jpg
                                                                                                                    
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ binwalk 4_c.jpg -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 64, uncompressed size: 81, name: flag.txt
79786         0x137AA         End of Zip archive, footer length: 22

                                                                                                                    
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ ls -la
total 92
drwxr-xr-x 3 kali kali  4096 Oct 11 09:15 .
drwxr-xr-x 3 kali kali  4096 Oct 11 09:14 ..
-rw-r--r-- 1 kali kali 79808 Mar 15  2021 4_c.jpg
drwxr-xr-x 2 kali kali  4096 Oct 11 09:15 _4_c.jpg.extracted
                                                                                                                    
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ cd _4_c.jpg.extracted 
                                                                                                                    
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ ls -la
total 16
drwxr-xr-x 2 kali kali 4096 Oct 11 09:15 .
drwxr-xr-x 3 kali kali 4096 Oct 11 09:15 ..
-rw-r--r-- 1 kali kali  230 Oct 11 09:15 136DA.zip
-rw-r--r-- 1 kali kali   81 Mar 15  2021 flag.txt
                                                                                                                    
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ open flag.txt 
                                                                                                                    
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ cat flag.txt         
picoCTF{336cf6d51c9d9774fd37196c1d7320ff}

```

## Referencias