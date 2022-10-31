# Crypto 2029

## Descripcion

Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

## Pistas (Si hay)

1.- What kind of encoding uses dashes and dots?

2.- The flag is in the format PICOCTF{}

## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ nc jupiter.challenges.picoctf.org 9422  
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } 

Al ponerlo en una pagina de traduccion de codigo morse nos dan la bandera:

PICOCTF{M0RS3C0D31SFUN2683824610}

```

## Referencias