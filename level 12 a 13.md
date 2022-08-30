# Retos Bandit

## Objetivos

The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)


## Datos de acceso

User: bandit12
Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit12@bandit:~$ cat data.txt | xxd -r
J쌑Oϊ{RBpQixYZ!dj(搿ݳ/A#dbX?z2<A n}4hFF4LM@zFMChFC@4@fhihPhMh
5(3AwOR6XS{
9?LPyB=zm?LNt*7{qP̜%"w9qm4 N36KH䋑[}!d3A4$M~\JCkUƦ\\FSN&=[q      \)$:Ht&/(]BB9<s h=bandit12@bandit:~$ cat data.txt | xxd -r | file -
/dev/stdin: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ cat data.txt | xxd -r | zcat |  file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat |  file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | TAR XO | file -
-bash: TAR: command not found
/dev/stdin: empty
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | tar xO | file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | tar xO | bzcat  | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | tar xO | bzcat | tar xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | tar xO | bzcat | tar xO | zcatt  |f
ile -
-bash: zcatt: command not found
/dev/stdin: empty
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | tar xO | bzcat | tar xO | zcat  |fi
le -
/dev/stdin: ASCII text
bandit12@bandit:~$ cat data.txt | xxd -r | zcat | bzcat | zcat  | tar xO | tar xO | bzcat | tar xO | zcat
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

## Notas adicionales

## Referencias