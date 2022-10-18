# Ejercicios de tarea

## Descripcion

Figure out how they moved the [flag](https://mercury.picoctf.net/static/88553d672efbccbc5868002f4c6eb737/tftp.pcapng).

## Pistas (Si hay)

What are some other ways to hide data?

## Solución

``` Bash

┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ wireshark tftp.pcapng &
[1] 7654
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ LS -LA
LS: command not found
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ ls -la
total 89020
drwxr-xr-x 2 kali kali     4096 Oct 11 10:12  .
drwxr-xr-x 6 kali kali     4096 Oct 11 09:54  ..
-rw-r--r-- 1 kali kali      113 Oct 11 10:12  instructions.txt
-rw-r--r-- 1 kali kali   824518 Oct 11 10:12  picture1.bmp
-rw-r--r-- 1 kali kali 36578358 Oct 11 10:12  picture2.bmp
-rw-r--r-- 1 kali kali  1466574 Oct 11 10:12  picture3.bmp
-rw-r--r-- 1 kali kali       59 Oct 11 10:12  plan
-rw-r--r-- 1 kali kali   138310 Oct 11 10:12  program.deb
-rw-r--r-- 1 kali kali 52116496 Mar 15  2021  tftp.pcapng
-rw-r--r-- 1 kali kali      264 Oct 11 09:55 'Trivial Flag Transfer Protocol.md'
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ open instructions.txt 
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ cat instructions.txt                
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ cat plan            
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ data plan  
Command 'data' not found, did you mean:
  command 'dat' from deb liballegro4-dev
  command 'date' from deb coreutils
Try: sudo apt install <deb name>
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ cat instructions.txt | tr [A-Z] [N-ZA-M]
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ cat plan | tr [A-Z] [N-ZA-M]
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ dpkg -I program.deb 
 new Debian package, version 2.0.
 size 138310 bytes: control archive=1250 bytes.
     826 bytes,    18 lines      control              
    1184 bytes,    17 lines      md5sums              
 Package: steghide
 Source: steghide (0.5.1-9.1)
 Version: 0.5.1-9.1+b1
 Architecture: amd64
 Maintainer: Ola Lundqvist <opal@debian.org>
 Installed-Size: 426
 Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
 Section: misc
 Priority: optional
 Description: A steganography hiding tool
  Steghide is steganography program which hides bits of a data file
  in some of the least significant bits of another file in such a way
  that the existence of the data file is not visible and cannot be proven.
  .
  Steghide is designed to be portable and configurable and features hiding
  data in bmp, wav and au files, blowfish encryption, MD5 hashing of
  passphrases to blowfish keys, and pseudo-random distribution of hidden bits
  in the container data.
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ sudo dpkg -i program.deb
[sudo] password for kali: 
dpkg: warning: downgrading steghide from 0.5.1-15 to 0.5.1-9.1+b1
(Reading database ... 343839 files and directories currently installed.)
Preparing to unpack program.deb ...
Unpacking steghide (0.5.1-9.1+b1) over (0.5.1-15) ...
Setting up steghide (0.5.1-9.1+b1) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for kali-menu (2022.3.1) ...
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ steghide program.deb    
steghide: unknown command "program.deb".
steghide: type "steghide --help" for help.
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture1.bmp -p DUEDILIGENCE
steghide: could not extract any data with that passphrase!
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture2.bmp -p DUEDILIGENCE
steghide: could not extract any data with that passphrase!
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture3.bmp -p DUEDILIGENCE
wrote extracted data to "flag.txt".
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos: Forensic picoCTF 2021,2022 - Parte 3/picoCTF 2021/Trivial Flag Transfer Protocol]
└─$ cat flag.txt                
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}


```

## Referencias