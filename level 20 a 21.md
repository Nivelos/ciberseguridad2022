# Retos Bandit

## Objetivos

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think

## Datos de acceso

User: bandit20
Password: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

``` Bash
bandit20@bandit:~$ nc -lvp 2930 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[3] 635330
bandit20@bandit:~$ Listening on 0.0.0.0 2930

bandit20@bandit:~$ jobs
[1]-  Stopped                 nc localhost 2020
[2]+  Stopped                 nc -lvp 2930 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
[3]   Running                 nc -lvp 2930 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
bandit20@bandit:~$ ./suconnect 2930

^Z
[4]+  Stopped                 ./suconnect 2930
bandit20@bandit:~$
bandit20@bandit:~$ jobs
[1]   Stopped                 nc localhost 2020
[2]-  Stopped                 nc -lvp 2930 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
[3]   Running                 nc -lvp 2930 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[4]+  Stopped                 ./suconnect 2930
bandit20@bandit:~$ ./suconnect 2930
^Z
[5]+  Stopped                 ./suconnect 2930
bandit20@bandit:~$ ./suconnect 2930
Connection received on localhost 33608
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[3]   Done                    nc -lvp 2930 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
```

## Notas adicionales

## Referencias