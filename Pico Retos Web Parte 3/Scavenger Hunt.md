# Web picoCTF

## Descripcion

There is some interesting information hidden around this site [http://mercury.picoctf.net:39491/](http://mercury.picoctf.net:39491/). Can you find it?

## Pistas (Si hay)

1.- You should have enough hints to find the files, don't run a brute forcer.

## Solución

``` Bash

Primero inspeccionamos el html donde nos da la primera parte de la bandera:

 Heres the first part of the flag: picoCTF{t 

La segunda parte es abrir el formato CSS, hasta abajo aparece la segunda parte de la llave

/* CSS makes the page look nice, and yes, it also has part of the flag. Heres part 2: h4ts_4_l0 */

La tercera parte la hacemos abriendo el JavaScript donde hasta el final nos aparece 

/* How can I keep Google from indexing my website? */

Por ejercicios anteriores sabemos que se refiere al robots.txt, al abrirlo tenemos lo siguiente

User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?

El siguiente paso se basa en leer la documentacion de los servidores apache y ver la terminacion htaccess, al momento de hacerlo nos da lo siguiente

# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.

Por ultimo tenemos el archivo .DB_Store, lugar donde se almacenan distintos atributos de productos que utilizan macOS, al cambiar la direccion con terminacion .DS_Store nos da lo siguiente

Congrats! You completed the scavenger hunt. Part 5: _f7ce8828}

```

## Referencias