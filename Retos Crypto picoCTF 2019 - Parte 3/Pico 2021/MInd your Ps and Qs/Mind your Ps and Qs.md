# Crypto 2019

## Descripcion

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/38f30029ab93478310e906d3d084a4c1/values)

## Pistas (Si hay)

Bits are expensive, I used only a little bit over 100 to save money

## Solución

``` Bash

┌──(kali㉿kali)-[~/RsaCtfTool]
└─$ python3 RsaCtfTool.py -n 831416828080417866340504968188990032810316193533653516022175784399720141076262857 -e 65537 --uncipher 240986837130071017759137533082982207147971245672412893755780400885108149004760496
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmpezjg86am.
attack initialized...
[*] Performing smallq attack on /tmp/tmpezjg86am.
[*] Performing factordb attack on /tmp/tmpezjg86am.
[*] Attack success with factordb method !

Results for /tmp/tmpezjg86am:

Unciphered data :
HEX : 0x7069636f4354467b736d6131315f4e5f6e305f67306f645f32333534303336387d
INT (big endian) : 13016382529449106065927291425342535437996222135352905256639592405461024281868413
INT (little endian) : 14499436437215324629163244483024452477715848127212044465501836292547934115031408
utf-8 : picoCTF{sma11_N_n0_g0od_23540368}
STR : b'picoCTF{sma11_N_n0_g0od_23540368}'
HEX : 0x007069636f4354467b736d6131315f4e5f6e305f67306f645f32333534303336387d
INT (big endian) : 13016382529449106065927291425342535437996222135352905256639592405461024281868413
INT (little endian) : 3711855727927123105065790587654259834295257120566283383168470090892271133448040448
utf-8 : picoCTF{sma11_N_n0_g0od_23540368}
utf-16 : 瀀捩䍯䙔獻慭ㄱ也湟弰で摯㉟㔳〴㘳紸
STR : b'\x00picoCTF{sma11_N_n0_g0od_23540368}'


```

## Referencias