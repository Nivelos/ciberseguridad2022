# Primer parcial 

## Descripcion

There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!

## Pistas (Si hay)

Seems like the password is encrypted.

## Solución

``` Bash

Inspeccionamos la pagina y volvimos una linea en valor 1 para poder ver el query de SQL de la pagina,, al momento de inspeccionarla podemos notar que el resultado de poner la contraseña esta encriptado en ROT13, por lo que utilizaremos un encriptador para dar una contraseña trucada, la cual es ' be 1=1;

' Al momento de registrarnos con esa contraseña nos daran la bandera la cual es:

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}

```

## Referencias
