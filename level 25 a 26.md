# Retos Bandit

## Objetivos

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

## Datos de acceso

User: bandit26
Password: p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

``` Bash
  Enjoy your stay!

  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
:shell
bandit26@bandit:~$ ls -la
total 44
drwxr-xr-x  3 root     root      4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root      4096 Sep  1 06:30 ..
-rwsr-x---  1 bandit27 bandit26 14872 Sep  1 06:30 bandit27-do
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
drwxr-xr-x  2 root     root      4096 Sep  1 06:30 .ssh
-rw-r-----  1 bandit26 bandit26   258 Sep  1 06:30 text.txt
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

```

## Notas adicionales

## Referencias