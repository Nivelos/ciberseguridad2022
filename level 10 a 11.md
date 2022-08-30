# Retos Bandit

## Objetivos

The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

## Datos de acceso

User: bandit10
Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit10@bandit:~$ cat data.txt  | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## Notas adicionales

Utilizamos la herramienta de cyberchef en el cual se puede descodificar las contraseñas

## Referencias