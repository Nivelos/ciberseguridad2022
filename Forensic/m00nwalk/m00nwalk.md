# Segundo parcial

## Descripcion

Decode this [message](https://jupiter.challenges.picoctf.org/static/14393e18d98fedbaedbc28896d7ef31a/message.wav) from the moon.

## Pistas (Si hay)

1.- How did pictures from the moon landing get sent back to Earth?

2.- What is the CMU mascot?, that might help select a RX option

## Solución

``` Bash

Descargamos una herramienta llamada SSTV Decoder que nos permite decodificar este tipo de imagenes, hacemos lo siguiente en la consola: 

┌──(kali㉿kali)-[~/picoCTF/Forensic/m00nwalk]
└─$ sstv -d message.wav -o result.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [#################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Forensic/m00nwalk]
└─$ open result.png 
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Forensic/m00nwalk]
└─$ 

Al momento de abrir la imagen resultante, esta tendra la bandera adentro

```

## Referencias