# Crypto 2019

## Descripcion

I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled2.png)

## Pistas (Si hay)

1.- [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)

2.- Think of different ways you can "stack" images

## Solución

``` Bash

Utilizamos la herramienta de stegsolve para poder juntar ambas imagenes, de esta forma capturamos la bandera.

┌──(kali㉿kali)-[~/bin]
└─$ java -jar stegsolve.jar     
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true

La bandera es:

picoCTF{0542dc1d}

```

## Referencias