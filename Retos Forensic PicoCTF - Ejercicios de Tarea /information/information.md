# Ejercicios de tarea

## Descripcion

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg)

## Pistas (Si hay)

1.- Look at the details of the file

2.- Make sure to submit the flag as picoCTF{XXXXX}

## Solución

``` Bash

Primero vi si con el cat podia encontrar la bandera, al ver que no encontre en la herramienta hexeditor y ahi pude encontrar pedazos de base64, al momento de ponerlas en un nano y correrlas me dio la bandera

┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ cat | grep pico                                                                                           
^C
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ hexeditor cat.jpg          
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ nano gato                   
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ base64 gato -d    
[�42���!����573��]                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ hexeditor cat.jpg
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ nano gato        
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ base64 gato -d   
[�42���!����573��]picoCTF{the_m3XY▒]▒W�\��[�▒Y�YYbase64: invalid input
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ nano gato     
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ base64 gato -d
picoCTF{the_m3XY▒]▒W�\��[�▒Y�YYbase64: invalid input
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ hexeditor cat.jpg
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ nano gato        
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Forensic PicoCTF - Ejercicios de Tarea /information]
└─$ base64 gato -d   
picoCTF{the_m3tadata_1s_modified} 

```

## Referencias