# Primer parcial 

## Descripcion

There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!

## Pistas (Si hay)

1.- There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?

2.-Try to think about how the website verifies your login.

## Solución

``` Bash

Inspeccionamos la pagina y volvimos una linea en valor 1 para poder ver el query de SQL de la pagina, para que saliera entonces utilizamos el comando "' or 1==1;" para poder entrar, esta entrada la cambiamos a rot13 para que nos de "' be 1==1;" y asi nos da la contraseña

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}
```

## Referencias
