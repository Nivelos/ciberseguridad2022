# Metared International CTF 2022

## Descripcion

PROFE SE ME OLVIDO PONER LA DESCRIPCION PERDON

## Pistas (Si hay)



## Solución

``` Bash

Al momento de utilizar el comando head en el documento nos suelta un texto en base64, despues de pasarlo varias veces por el cyberchef nos da la bandera.

┌──(kali㉿kali)-[~/Downloads]
└─$ head Fakepgp.txt 
-----BEGIN PGP MESSAGE-----
Charset: ISO-8859-1
Version: GnuPG v1.2.5 (MingW32)
Comment: Using GnuPG with Thunderbird - http://enigmail.mozdev.org - 10 TIMES ENCODE


Vm0wd2QyVkhVWGhVYmxKV1YwZDRXRmxVUm5kVlJscHpXa2M1VjFKdGVGWlZNbmhQWVd4S2MxTnNXbGRTTTFKUVdWY3hTMUl4WkhWalJtUk9ZV3RhU1ZadGNFdFRNVWw0Vkc1T1lWSnRVbGhVVkVwdlpWWmFkR05GZEZSTlZXdzFWa2QwWVZkSFNrZGpTRUpYWVRGYWFGVXhXbUZqTVZaeVpFWlNUbFpYZHpCV01uUnZWakpHYzFOdVVsWmlSMmhXVm10V1lWUkdVblJsUjBaclVqRktTVlZ0ZUhkV01rcEpVV3hzVjJGcmEzaFZla1pUWXpGa2RWVnNXbWxXUjNoWFZtMHhOR1F3TUhoVmJHaHNVakJhV1ZWc1VrZFdiRnBZWlVoa1YwMXJWalpWVm1oclZqRmFObEpZWkZoV2JWSklXWHBHVDJSV1VuTmhSMnhYVWpOb1dGWnRNWGRVTWtsNFZXdGtXR0pzU25OVmFrNVRZMnhXY1ZKdFJsTk5WbXcxV2xWV1QxWXdNWEpXYWs1YVRVWndWRlpxUm1GV01rNUhWRzFHVTFKV2NFVldiR1EwVVRGYVZrMVZWazVTUkVFNQ==
-----END PGP MESSAGE-----

flag{DONTOVERTHINKTHETHINGS}


```

## Referencias