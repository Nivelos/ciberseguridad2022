# Primer parcial 

## Descripcion

Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210

## Pistas (Si hay)

1.- What is that cookie?

2.-Have you heard of JWT?

## Solución

``` Bash

Primero hacemos un intento de login en la pagina con el usuario de Admin y nos da acceso denegado, ponemos un usuario cualquiera y se genera una cookie que podemos editar en el JSON Web Tokens y editamos nuestro usuario cualquiera por el admin, despues utilizamos la herramienta de John the reapper para poder editar la encriptacion y asi nos da la contraseña en el JaWT.

```

## Referencias