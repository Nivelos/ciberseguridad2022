# Ejercicios de tarea

## Descripcion

Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download disk image](https://artifacts.picoctf.net/c/114/disk.img.gz)
-   Access checker program: `nc saturn.picoctf.net 52279`

## Pistas (Si hay)



## Solución

``` Bash

Se usa el mmls para ver el tamaño del disco y se introduce el link de la pagina con los datos que nos da el mmls.

┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/PicoCTF 2022/Sleuthkit Intr]
└─$ mmls -V              
The Sleuth Kit ver 4.11.1
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/PicoCTF 2022/Sleuthkit Intr]
└─$ man mmls 
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/PicoCTF 2022/Sleuthkit Intr]
└─$ mmls disk.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/PicoCTF 2022/Sleuthkit Intr]
└─$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 204799
204799
That is not correct. Feel free to try again.
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/PicoCTF 2022/Sleuthkit Intr]
└─$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}


```

## Referencias