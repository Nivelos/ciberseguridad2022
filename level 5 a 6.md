# Retos Bandit

## Objetivos

The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

-   human-readable
-   1033 bytes in size
-   not executable

## Datos de acceso

User: bandit5
Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root    4096 May  7  2020 .
drwxr-xr-x 41 root root    4096 May  7  2020 ..
-rw-r--r--  1 root root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root root    3526 May 15  2017 .bashrc
drwxr-x--- 22 root bandit5 4096 May  7  2020 inhere
-rw-r--r--  1 root root     675 May 15  2017 .profile
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ file
Usage: file [-bcEhikLlNnprsvzZ0] [--apple] [--extension] [--mime-encoding] [--mime-type]
            [-e testname] [-F separator] [-f namefile] [-m magicfiles] file ...
       file -C [-m magicfiles]
       file [--help]
bandit5@bandit:~/inhere$ file ./*
./maybehere00: directory
./maybehere01: directory
./maybehere02: directory
./maybehere03: directory
./maybehere04: directory
./maybehere05: directory
./maybehere06: directory
./maybehere07: directory
./maybehere08: directory
./maybehere09: directory
./maybehere10: directory
./maybehere11: directory
./maybehere12: directory
./maybehere13: directory
./maybehere14: directory
./maybehere15: directory
./maybehere16: directory
./maybehere17: directory
./maybehere18: directory
./maybehere19: directory
bandit5@bandit:~/inhere$ find , -type f -size 1003c
find: ‘,’: No such file or directory
bandit5@bandit:~/inhere$ find . -type f -size 1003c
bandit5@bandit:~/inhere$ find . -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ cd maybehere07
bandit5@bandit:~/inhere/maybehere07$ ls
-file1  -file2  -file3  spaces file1  spaces file2  spaces file3
bandit5@bandit:~/inhere/maybehere07$ cat ./-file2
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
bandit5@bandit:~/inhere/maybehere07$ cd ..
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```
## Notas adicionales

## Referencias