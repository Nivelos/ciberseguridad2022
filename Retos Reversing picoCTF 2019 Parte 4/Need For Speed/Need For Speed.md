# Retos: Reversing picoCTF 2019 - Parte 4

## Descripcion

The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/27dd5548b14661f65ce3ac6a8a8f575b/need-for-speed).

## Pistas (Si hay)



## Solución

``` Bash

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/Need For Speed]
└─$ sudo apt install gdb    
[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  freeglut3 libatk1.0-data libev4 libexporter-tiny-perl libflac8 libfmt8 libgeos3.11.0 libgs9-common
  libgssdp-1.2-0 libgupnp-1.2-1 libhttp-server-simple-perl libilmbase25 liblerc3 liblist-moreutils-perl
  liblist-moreutils-xs-perl libopenexr25 libopenh264-6 libperl5.34 libplacebo192 libpoppler118
  libpython3.9-minimal libpython3.9-stdlib libsvtav1enc0 libwebsockets16 libwireshark15 libwiretap12 libwsutil13
  openjdk-11-jre perl-modules-5.34 python3-dataclasses-json python3-limiter python3-marshmallow-enum
  python3-mypy-extensions python3-ntlm-auth python3-requests-ntlm python3-responses python3-spyse
  python3-token-bucket python3-typing-inspect python3.9 python3.9-minimal
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libbabeltrace1 libboost-regex1.74.0 libc6-dbg libdebuginfod-common libdebuginfod1 libipt2
  libsource-highlight-common libsource-highlight4v5
Suggested packages:
  gdb-doc gdbserver
The following NEW packages will be installed:
  gdb libbabeltrace1 libboost-regex1.74.0 libc6-dbg libdebuginfod-common libdebuginfod1 libipt2
  libsource-highlight-common libsource-highlight4v5
0 upgraded, 9 newly installed, 0 to remove and 75 not upgraded.
Need to get 12.1 MB of archives.
After this operation, 27.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://kali.download/kali kali-rolling/main amd64 libdebuginfod-common all 0.187-4 [25.6 kB]
Get:2 http://http.kali.org/kali kali-rolling/main amd64 libbabeltrace1 amd64 1.5.11-1+b1 [172 kB]
Get:3 http://kali.download/kali kali-rolling/main amd64 libdebuginfod1 amd64 0.187-4 [31.8 kB]
Get:4 http://kali.download/kali kali-rolling/main amd64 libipt2 amd64 2.0.5-1 [43.9 kB]
Get:5 http://kali.download/kali kali-rolling/main amd64 libsource-highlight-common all 3.1.9-4.2 [77.4 kB]
Get:6 http://http.kali.org/kali kali-rolling/main amd64 libboost-regex1.74.0 amd64 1.74.0-17+b2 [487 kB]
Get:7 http://http.kali.org/kali kali-rolling/main amd64 libsource-highlight4v5 amd64 3.1.9-4.2+b2 [257 kB]
Get:8 http://kali.download/kali kali-rolling/main amd64 gdb amd64 12.1-4 [3,595 kB]
Get:9 http://kali.download/kali kali-rolling/main amd64 libc6-dbg amd64 2.36-4 [7,448 kB]
Fetched 12.1 MB in 3s (3,715 kB/s)     
Preconfiguring packages ...
Selecting previously unselected package libdebuginfod-common.
(Reading database ... 385870 files and directories currently installed.)
Preparing to unpack .../0-libdebuginfod-common_0.187-4_all.deb ...
Unpacking libdebuginfod-common (0.187-4) ...
Selecting previously unselected package libbabeltrace1:amd64.
Preparing to unpack .../1-libbabeltrace1_1.5.11-1+b1_amd64.deb ...
Unpacking libbabeltrace1:amd64 (1.5.11-1+b1) ...
Selecting previously unselected package libdebuginfod1:amd64.
Preparing to unpack .../2-libdebuginfod1_0.187-4_amd64.deb ...
Unpacking libdebuginfod1:amd64 (0.187-4) ...
Selecting previously unselected package libipt2.
Preparing to unpack .../3-libipt2_2.0.5-1_amd64.deb ...
Unpacking libipt2 (2.0.5-1) ...
Selecting previously unselected package libsource-highlight-common.
Preparing to unpack .../4-libsource-highlight-common_3.1.9-4.2_all.deb ...
Unpacking libsource-highlight-common (3.1.9-4.2) ...
Selecting previously unselected package libboost-regex1.74.0:amd64.
Preparing to unpack .../5-libboost-regex1.74.0_1.74.0-17+b2_amd64.deb ...
Unpacking libboost-regex1.74.0:amd64 (1.74.0-17+b2) ...
Selecting previously unselected package libsource-highlight4v5:amd64.
Preparing to unpack .../6-libsource-highlight4v5_3.1.9-4.2+b2_amd64.deb ...
Unpacking libsource-highlight4v5:amd64 (3.1.9-4.2+b2) ...
Selecting previously unselected package gdb.
Preparing to unpack .../7-gdb_12.1-4_amd64.deb ...
Unpacking gdb (12.1-4) ...
Selecting previously unselected package libc6-dbg:amd64.
Preparing to unpack .../8-libc6-dbg_2.36-4_amd64.deb ...
Unpacking libc6-dbg:amd64 (2.36-4) ...
Setting up libdebuginfod-common (0.187-4) ...
Setting up libdebuginfod1:amd64 (0.187-4) ...
Setting up libsource-highlight-common (3.1.9-4.2) ...
Setting up libc6-dbg:amd64 (2.36-4) ...
Setting up libboost-regex1.74.0:amd64 (1.74.0-17+b2) ...
Setting up libipt2 (2.0.5-1) ...
Setting up libbabeltrace1:amd64 (1.5.11-1+b1) ...
Setting up libsource-highlight4v5:amd64 (3.1.9-4.2+b2) ...
Setting up gdb (12.1-4) ...
Processing triggers for libc-bin (2.36-4) ...
Processing triggers for man-db (2.11.0-1+b1) ...
Processing triggers for kali-menu (2022.4.1) ...
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/Need For Speed]
└─$ gdb need-for-speed 
GNU gdb (Debian 12.1-4) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from need-for-speed...
(No debugging symbols found in need-for-speed)
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x00000000000005d8  _init
0x0000000000000600  putchar@plt
0x0000000000000610  puts@plt
0x0000000000000620  alarm@plt
0x0000000000000630  __sysv_signal@plt
0x0000000000000640  exit@plt
0x0000000000000650  __cxa_finalize@plt
0x0000000000000660  _start
0x0000000000000690  deregister_tm_clones
0x00000000000006d0  register_tm_clones
0x0000000000000720  __do_global_dtors_aux
0x0000000000000760  frame_dummy
0x000000000000076a  decrypt_flag
0x00000000000007f1  calculate_key
0x000000000000080e  alarm_handler
0x000000000000082f  set_timer
0x000000000000087d  get_key
0x00000000000008ac  print_flag
0x00000000000008d8  header
0x000000000000091a  main
0x0000000000000960  __libc_csu_init
0x00000000000009d0  __libc_csu_fini
0x00000000000009d4  _fini
(gdb) set disassembly-flavor intel
(gdb) dissamble main
Undefined command: "dissamble".  Try "help".
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000000091a <+0>:     push   rbp
   0x000000000000091b <+1>:     mov    rbp,rsp
   0x000000000000091e <+4>:     sub    rsp,0x10
   0x0000000000000922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:    mov    eax,0x0
   0x000000000000092e <+20>:    call   0x8d8 <header>
   0x0000000000000933 <+25>:    mov    eax,0x0
   0x0000000000000938 <+30>:    call   0x82f <set_timer>
   0x000000000000093d <+35>:    mov    eax,0x0
   0x0000000000000942 <+40>:    call   0x87d <get_key>
   0x0000000000000947 <+45>:    mov    eax,0x0
   0x000000000000094c <+50>:    call   0x8ac <print_flag>
   0x0000000000000951 <+55>:    mov    eax,0x0
   0x0000000000000956 <+60>:    leave  
   0x0000000000000957 <+61>:    ret    
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x91e
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000000000000091e <main+4>
(gdb) run
Starting program: /home/kali/Documents/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/Need For Speed/need-for-speed                                                                                                        
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555540091e in main ()
(gdb) break main
Note: breakpoint 1 also set at pc 0x55555540091e.
Breakpoint 2 at 0x55555540091e
(gdb) call (int) get_key
$1 = 1430259837
(gdb) call (int) print_flag
$2 = 1430259884
(gdb) call (int) print_flag()
Printing flag:
pDcBcYfvgbOi
$3 = 13
(gdb) Quit
(gdb) Quit
(gdb) Quit
(gdb) 
Printing flag:
pDcBbYdvebLigKofChVdIo]~        .▒lH9In
                                       ~]hKiGcH-Qa_cV,O
$4 = 56
(gdb) Quit
Undefined command: "Quit".  Try "help".
(gdb) exit
A debugging session is active.

        Inferior 1 [process 44538] will be killed.

Quit anyway? (y or n) y
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/Need For Speed]
└─$ gdb need-for-speed
GNU gdb (Debian 12.1-4) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from need-for-speed...
(No debugging symbols found in need-for-speed)
(gdb) set di
directories            disassemble-next-line  disassembly-flavor     disconnected-tracing   
disable-randomization  disassembler-options   disconnected-dprintf   displaced-stepping     
(gdb) set di
directories            disassemble-next-line  disassembly-flavor     disconnected-tracing   
disable-randomization  disassembler-options   disconnected-dprintf   displaced-stepping     
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000000091a <+0>:     push   rbp
   0x000000000000091b <+1>:     mov    rbp,rsp
   0x000000000000091e <+4>:     sub    rsp,0x10
   0x0000000000000922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:    mov    eax,0x0
   0x000000000000092e <+20>:    call   0x8d8 <header>
   0x0000000000000933 <+25>:    mov    eax,0x0
   0x0000000000000938 <+30>:    call   0x82f <set_timer>
   0x000000000000093d <+35>:    mov    eax,0x0
   0x0000000000000942 <+40>:    call   0x87d <get_key>
   0x0000000000000947 <+45>:    mov    eax,0x0
   0x000000000000094c <+50>:    call   0x8ac <print_flag>
   0x0000000000000951 <+55>:    mov    eax,0x0
   0x0000000000000956 <+60>:    leave  
   0x0000000000000957 <+61>:    ret    
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x91e
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000000000000091e <main+4>
(gdb) run
Starting program: /home/kali/Documents/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/Need For Speed/need-for-speed                                                                                                        
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555540091e in main ()
(gdb) disassemble main
Dump of assembler code for function main:
   0x000055555540091a <+0>:     push   rbp
   0x000055555540091b <+1>:     mov    rbp,rsp
=> 0x000055555540091e <+4>:     sub    rsp,0x10
   0x0000555555400922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000555555400925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000555555400929 <+15>:    mov    eax,0x0
   0x000055555540092e <+20>:    call   0x5555554008d8 <header>
   0x0000555555400933 <+25>:    mov    eax,0x0
   0x0000555555400938 <+30>:    call   0x55555540082f <set_timer>
   0x000055555540093d <+35>:    mov    eax,0x0
   0x0000555555400942 <+40>:    call   0x55555540087d <get_key>
   0x0000555555400947 <+45>:    mov    eax,0x0
   0x000055555540094c <+50>:    call   0x5555554008ac <print_flag>
   0x0000555555400951 <+55>:    mov    eax,0x0
   0x0000555555400956 <+60>:    leave  
   0x0000555555400957 <+61>:    ret    
End of assembler dump.
(gdb) call (int) get_key()
Creating key...
Finished
$1 = 9
(gdb) call (int) print_flag
$2 = 1430259884
(gdb) call (int) print_flag()
Printing flag:
PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}

```

## Referencias