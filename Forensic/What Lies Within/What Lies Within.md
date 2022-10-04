# Segundo parcial

## Descripcion

There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?

## Pistas (Si hay)

There is data encoded somewhere... there might be an online decoder.

## Solución

``` Bash

Sabiendo que debemos descodificar la imagen buscamos una herramienta online para poder tener la bandera, dandonos como resultado

picoCTF{h1d1ng_1n_th3_b1t5}

Utilizando la herramienta zsget tenemos lo siguiente: 

┌──(kali㉿kali)-[~/picoCTF/Forensic/What Lies Within]
└─$ zsteg buildings.png 
b1,r,lsb,xy         .. text: "^5>R5YZrG"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b2,b,lsb,xy         .. text: "XuH}p#8Iy="
b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"
b4,r,lsb,xy         .. text: "fdD\"\"\"\" "
b4,r,msb,xy         .. text: "%Q#gpSv0c05"
b4,g,lsb,xy         .. text: "fDfffDD\"\""
b4,g,msb,xy         .. text: "f\"fff\"\"DD"
b4,b,lsb,xy         .. text: "\"$BDDDDf"
b4,b,msb,xy         .. text: "wwBDDDfUU53w"
b4,rgb,msb,xy       .. text: "dUcv%F#A`"
b4,bgr,msb,xy       .. text: " V\"c7Ga4"
b4,abgr,msb,xy      .. text: "gOC_$_@o"
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Forensic/What Lies Within]
└─$ zsteg buildings.png | grep pico
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"


```

## Referencias

https://www.esteganografia.com/
