# Ejercicios de tarea

## Descripcion

The flag is somewhere on this web application not necessarily on the website. Find it. Check [this](http://saturn.picoctf.net:64710/) out.

## Pistas (Si hay)



## Solución

``` Bash

Por el titulo del reto pense que debiamos utilizar la extension de robots.txt, edite el url de la pagina de manera que quero asi:

http://saturn.picoctf.net:64710/robots.txt

Despues de eso nos suelta el siguiente codigo:

User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/

Note que estaba codificado en base64, al utilizar un decodificador nos suelta el siguiente resultado:

js/myfile.txt

Al momento de modificar de nuevo la url con el siguiente vinculo:

http://saturn.picoctf.net:64710/js/myfile.txt

Nos da la bandera:

picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}

```

## Referencias