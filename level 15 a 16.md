# Retos Bandit

## Objetivos

The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

**Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…**

## Datos de acceso

User: bandit15
Password: BfMYroe26WYalil77FoDi9qh59eK5xNr
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```Bash
bandit15@bandit:~$ openssl s_client -connect localhost:30001
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
MIICBjCCAW+gAwIBAgIEXcVbPTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjIwMzA5MTk0NzQyWhcNMjMwMzA5MTk0NzQyWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALDCas6k
DHxTRoxVISHtXOeCwJ8Sax5BZN76Hle8AH6pYTAdv9/FRssWL1xppFAtiGnFvglu
95FJvHEQirY4F0oPBTbtGU2xhzZzkWRL5Yj2C3Q2c99cyh+uWQT7sXPtB8W1osPc
YIo83YkXiArpt28474ZYdl+ohbPtP1oQHBv3AgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAC2693WiK/kXMCauf1fEg5DwuxIfm0saYKiLSceyZo1G4IggqOBO
9JCtvMIV/xRAmYEnPvJmf0JtYv+2fsicaPh9E1GRmU0vGoYDZzA7NTZOgRmHlRKe
ihh/XSGrY7tE1qU+EfizmhcB35iZ7W5INIKlu7oyBWcvk3rI4jtPQeZp
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
    Session-ID: A4014420893CD4E612BEA765338A4388C21DA1716E2F553356FAB22E649CB1F4
    Session-ID-ctx:
    Master-Key: 59AC7124D77D48367B0F9981BE35BC77DDAD265DE28432AC8F1B5C63EFE5EF4D63960853133BF36620D9A2A34E49E1B4
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - d3 53 01 d9 4c 2e 82 50-ef 16 38 c5 d8 1b dd f2   .S..L..P..8.....
    0010 - ff c0 fc 25 d1 bd 6c ae-1f 60 45 3a d4 8a 5e 28   ...%..l..`E:..^(
    0020 - 73 3c dc 9b 5c e8 3c 11-18 a6 71 0d 97 79 70 27   s<..\.<...q..yp'
    0030 - 96 e1 6f 4d 9b 02 95 af-a2 e9 da 4b cf 22 b4 36   ..oM.......K.".6
    0040 - b9 a0 3e f1 99 77 78 fe-ff 1f ee c9 18 cb d4 8b   ..>..wx.........
    0050 - 4c b0 5e f4 74 01 4f d0-7c d3 7b 6c d1 71 8b b9   L.^.t.O.|.{l.q..
    0060 - 99 1f 33 77 a7 95 f0 ee-0e 8d c2 6d 61 ab 1a 35   ..3w.......ma..5
    0070 - 4b 19 a8 b6 1d aa 4a 2b-7d b2 1e 7a e8 38 cf 90   K.....J+}..z.8..
    0080 - 2f 92 2b 48 c6 89 e2 81-6b be 20 5b 61 72 8e 6f   /.+H....k. [ar.o
    0090 - ed fa 67 dc cd 1e 8e ea-95 0c 28 92 41 d7 ab 49   ..g.......(.A..I

    Start Time: 1661868639
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

## Notas adicionales

## Referencias