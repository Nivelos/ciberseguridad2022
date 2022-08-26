# Retos Bandit

## Objetivos

The password for the next level is stored in the file **data.txt** next to the word **millionth**

## Datos de acceso

User: bandit7
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit7@bandit:~$ ls -la
total 4108
drwxr-xr-x  2 root    root       4096 May  7  2020 .
drwxr-xr-x 41 root    root       4096 May  7  2020 ..
-rw-r--r--  1 root    root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root       3526 May 15  2017 .bashrc
-rw-r-----  1 bandit8 bandit7 4184396 May  7  2020 data.txt
-rw-r--r--  1 root    root        675 May 15  2017 .profile
bandit7@bandit:~$ grep millionth  data.txt
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## Notas adicionales

## Referencias