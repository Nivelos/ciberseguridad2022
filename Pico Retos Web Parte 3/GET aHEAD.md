# Web picoCTF

## Descripcion

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:47967/](http://mercury.picoctf.net:47967/)

## Pistas (Si hay)

1.- Maybe you have more than 2 choices

2.- Check out tools like Burpsuite to modify your requests and look at the responses

## Solución

``` Bash

Inspeccionamos la pagina, en el apartado de network cambiamos el metodo http de GET a HEAD y nos da como respuesta la contraseña del problema

picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}

En consola seria:

┌──(kali㉿kali)-[~]
└─$ curl -X HEAD http://mercury.picoctf.net:47967/index.php
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the 
Warning: way you want. Consider using -I/--head instead.


┌──(kali㉿kali)-[~]
└─$ curl -I  http://mercury.picoctf.net:47967/index.php
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}
Content-type: text/html; charset=UTF-8


```

## Referencias