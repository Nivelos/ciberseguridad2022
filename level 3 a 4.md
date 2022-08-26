# Retos Bandit

## Objetivos

The password for the next level is stored in a hidden file in the **inhere** directory.

## Datos de acceso

User: bandit3
Password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash

C:\Users\jose_>ssh bandit3@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames


bandit3@bandit.labs.overthewire.orgs password:
Linux bandit.otw.local 5.4.8 x86_64 GNU/Linux
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  inhere  .profile
bandit3@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 May  7  2020 .
drwxr-xr-x 41 root root 4096 May  7  2020 ..
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc
drwxr-xr-x  2 root root 4096 May  7  2020 inhere
-rw-r--r--  1 root root  675 May 15  2017 .profile
bandit3@bandit:~$ open inhere
Couldnt get a file descriptor referring to the console
bandit3@bandit:~$ cat .hidden
cat: .hidden: No such file or directory
bandit3@bandit:~$ find inhere
inhere
inhere/.hidden
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

```
## Notas adicionales

## Referencias

