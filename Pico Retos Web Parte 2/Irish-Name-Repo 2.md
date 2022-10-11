# Primer parcial 

## Descripcion

There is a website running at `https://jupiter.challenges.picoctf.org/problem/53751/` ([link](https://jupiter.challenges.picoctf.org/problem/53751/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751

## Pistas (Si hay)

The password is being filtered.

## Solución

``` Bash

Inspeccionamos la pagina y volvimos una linea en valor 1 para poder ver el query de SQL de la pagina, para que saliera entonces utilizamos el comando "admin';" para poder entrar, la bandera es:

Your flag is: picoCTF{m0R3_SQL_plz_c34df170}

```

## Referencias
