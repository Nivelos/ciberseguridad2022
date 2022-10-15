# Segundo parcial

## Descripcion

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.

## Pistas (Si hay)

1.- Try using a tool like Wireshark.

2.- How can you decrypt the TLS stream?

## Solución

``` Bash

Entramos a la captura de paquetes, cargamos la llave asignada y buscamos una imagen que se esta procesando en esta, la cargamos en nuestro disco y aplicamos un string en la misma como se ve a continuacion

┌──(kali㉿kali)-[~/picoCTF/Forensic Pt 2/WebNet1]
└─$ wireshark capture.pcap &
[2] 46299
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Forensic Pt 2/WebNet1]
└─$  ** (wireshark:46299) 22:09:31.348506 [GUI WARNING] -- FIX Add drag reordering to UAT dialog
 ** (wireshark:46299) 22:10:45.008288 [GUI WARNING] -- QXcbConnection: XCB error: 3 (BadWindow), sequence: 9278, resource id: 22347559, major code: 40 (TranslateCoords), minor code: 0
            
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Forensic Pt 2/WebNet1]
└─$ open vulture.jpg 
                                                                                                                    
┌──(kali㉿kali)-[~/picoCTF/Forensic Pt 2/WebNet1]
└─$ strings vulture.jpg -n15                           
picoCTF{honey.roasted.peanuts}
 )/'%'/9339GDG]]}
 )/'%'/9339GDG]]}
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz


```

## Referencias