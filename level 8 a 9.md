# Retos Bandit

## Objetivos

The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

## Datos de acceso

User: bandit8
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit8@bandit:~$ ls -la
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## Notas adicionales

El comando sourt nos permite ordenar las lineas de codigo, solamente con las lineas de codigo ordenadas podremos utilizar correctamente el comando uniq, que sirve para encontrar lineas uncias

## Referencias