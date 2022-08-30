# Retos Bandit

## Objetivos

The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## Datos de acceso

User: bandit16
Password: cluFn7wTiGryunymYOu4RcffSxQluehd
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit16@bandit:~$ nc -v localhost 30000
localhost [127.0.0.1] 30000 (?) open
^Z
[1]+  Stopped                 nc -v localhost 30000
bandit16@bandit:~$ nc -v localhost 30918
localhost [127.0.0.1] 30918 (?) : Connection refused
bandit16@bandit:~$ nmap localhost -p 31000-32000

Starting Nmap 7.40 ( https://nmap.org ) at 2022-08-30 16:20 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00025s latency).
Not shown: 996 closed ports
PORT      STATE    SERVICE
31046/tcp open     unknown
31518/tcp filtered unknown
31691/tcp open     unknown
31790/tcp open     unknown
31960/tcp open     unknown

Nmap done: 1 IP address (1 host up) scanned in 1.27 seconds
bandit16@bandit:~$ openssl s_client -connect localhost:31691
CONNECTED(00000003)
140224060051520:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:284:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 176 bytes and written 183 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID:
    Session-ID-ctx:
    Master-Key:
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1661869343
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
---
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEJ4dj3zANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjIwODA0MTQ0NzAyWhcNMjMwODA0MTQ0NzAyWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOKNs5Hv
vMkLDL7DAWOObCsOxRATamcwQRU3vKGmhqx3h85DORvg/dcfD+4zMKe4svngMHb/
AvFb7kgx0UmlQ5ZNQ8R13D02iM2KtDzTYhRu72PG6go8xTs4uBVlsMDuzbJJsvu1
ihOxS2/U8k2VgSovPoWdUffAbYVJ04U/d4CfAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAN/dd5II2+QlVBcfezT+iAs8X35P8LIIiJsSksUJZlgG50V/3xqN
HitXAq4Qxh1KvmcO/09BF/UPHIX9I/aO4/SSJeYKBrtsYh79lySoS2xGzLrYD9vN
vd/FsuBHJ+eE0pM4LMoWEuFOpXavad5KcKk+T4HaXU0A/kL/Upj8jlRR
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 13CCBB37874D439A9CD43C495DF1D2BDFA3D6550FA2D2B2E44707840220EB4F6
    Session-ID-ctx:
    Master-Key: 55773294723A64DBFE301D86AB115436CE8145586EEF983EEEE130E96FFAE045F144B1BE8F75C13F88B17947BEA93A5C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 88 8b 84 42 b6 05 26 26-21 2f 2b 89 62 bd af 93   ...B..&&!/+.b...
    0010 - ac 07 ef 2b ea ca 43 d1-20 d2 f1 ae 70 14 dc 84   ...+..C. ...p...
    0020 - b9 0f ab 37 c6 4f 53 a1-cb 0f 6c 69 6f 58 86 0f   ...7.OS...lioX..
    0030 - 2e 4d 9e 93 5d 3f 1d 05-ef f0 1b 86 a7 0f 28 93   .M..]?........(.
    0040 - 5c 00 d6 1d 30 5a cd ec-a3 2f 49 6a ee e5 09 f3   \...0Z.../Ij....
    0050 - 2c af 7c 5b e6 ae ee 49-ae 81 58 82 ec f0 09 35   ,.|[...I..X....5
    0060 - 2b 00 e0 35 92 20 7d 14-37 d5 1c 46 ed 07 8e a1   +..5. }.7..F....
    0070 - 3b b3 7a ff 03 79 a8 b2-a8 62 7e 6a 13 c3 7a ca   ;.z..y...b~j..z.
    0080 - 8c 53 49 6a a7 7b 79 55-fe d6 0f fe 59 f5 d6 47   .SIj.{yU....Y..G
    0090 - 26 69 5f 2f e0 de b3 d4-37 8d dc 35 3c d4 98 dd   &i_/....7..5<...

    Start Time: 1661869357
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEJ4dj3zANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjIwODA0MTQ0NzAyWhcNMjMwODA0MTQ0NzAyWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOKNs5Hv
vMkLDL7DAWOObCsOxRATamcwQRU3vKGmhqx3h85DORvg/dcfD+4zMKe4svngMHb/
AvFb7kgx0UmlQ5ZNQ8R13D02iM2KtDzTYhRu72PG6go8xTs4uBVlsMDuzbJJsvu1
ihOxS2/U8k2VgSovPoWdUffAbYVJ04U/d4CfAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAN/dd5II2+QlVBcfezT+iAs8X35P8LIIiJsSksUJZlgG50V/3xqN
HitXAq4Qxh1KvmcO/09BF/UPHIX9I/aO4/SSJeYKBrtsYh79lySoS2xGzLrYD9vN
vd/FsuBHJ+eE0pM4LMoWEuFOpXavad5KcKk+T4HaXU0A/kL/Upj8jlRR
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 649057234E574DE4D013D49384047517E588BF235380E128EE415FF483D608FF
    Session-ID-ctx:
    Master-Key: 2332AD3C6FC9265AF962E3F9F4A6795EB448F538F0FEDEEAE50B80D094545B70AA451D386ECA3B79660943967CBF77C9
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 88 8b 84 42 b6 05 26 26-21 2f 2b 89 62 bd af 93   ...B..&&!/+.b...
    0010 - 2b a6 62 46 04 7d a2 67-4c 94 f2 1b c2 92 a4 2d   +.bF.}.gL......-
    0020 - f6 f5 a4 47 91 31 0f 25-bf 84 f0 ce 4d 06 9e 1c   ...G.1.%....M...
    0030 - d3 99 2b 65 5c e1 74 fe-87 7b 7a 8c 53 6e 38 1c   ..+e\.t..{z.Sn8.
    0040 - 25 2e 02 a1 b1 91 5f 9b-61 5e 64 d3 50 7c 0f d5   %....._.a^d.P|..
    0050 - 5d b9 e2 8c 20 e0 62 9a-a9 23 16 ac 63 8f 07 3f   ]... .b..#..c..?
    0060 - 9f a3 20 df 74 35 8b df-11 a7 69 0a 62 22 4e 35   .. .t5....i.b"N5
    0070 - 09 55 da eb 9c dd 89 e0-93 9e 6b 90 31 9f f9 b3   .U........k.1...
    0080 - 3f ea 79 6d a6 d9 f8 89-86 af 8f a9 2f 21 74 65   ?.ym......../!te
    0090 - 37 83 b5 f3 fa bd cc 2f-41 0b 70 68 3d 1a d7 a4   7....../A.ph=...

    Start Time: 1661869378
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$ ls -l
total 0
bandit16@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 May  7  2020 .
drwxr-xr-x 41 root     root     4096 May  7  2020 ..
-rw-r-----  1 bandit16 bandit16   33 May  7  2020 .bandit15.password
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
-rw-r--r--  1 root     root      675 May 15  2017 .profile
bandit16@bandit:~$ exit
logout
There are stopped jobs.
bandit16@bandit:~$ exit
logout

Connection to bandit.labs.overthewire.org closed.

C:\Users\jose_>nano lallave.txt
"nano" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Users\jose_>ssh -i lallave.txt bandit15@bandit.labs.overthewire.org -p 2220
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames
```

## Notas adicionales

## Referencias