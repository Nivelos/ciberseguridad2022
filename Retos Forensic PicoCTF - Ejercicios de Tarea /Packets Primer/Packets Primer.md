# Ejercicios de tarea

## Descripcion

Download the packet capture file and use packet analysis software to find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/201/network-dump.flag.pcap)

## Pistas (Si hay)



## Solución

``` Bash

┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /Packets Primer]
└─$ wireshark network-dump.flag.pcap                               
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /Packets Primer]
└─$ open bandera  

Al momento de hacer un wireshark en la captura de paquete e inspeccionar los archivos TCP podemos ver que uno contiene la bandera

La bandera es: 

picoCTF{p4ck37_5h4rk_01b0a0d6}

```

## Referencias