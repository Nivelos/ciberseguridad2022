# Primer parcial 

## Descripcion

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip)

## Pistas (Si hay)

After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solución

``` Bash

┌──(kali㉿kali)-[~/Downloads]
└─$ unzip Addadshashanammu.zip
Archive:  Addadshashanammu.zip
replace Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet? [y]es, [n]o, [A]ll, [N]one, [r]ename: yes
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku 
                                                                             
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ ls .la
ls: cannot access '.la': No such file or directory
                                                                             
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ ls -la
total 20
drwxr-xr-x 2 kali kali 4096 Sep 26 01:22 .
drwxr-xr-x 3 kali kali 4096 Sep 26 01:21 ..
-rwxr-xr-x 1 kali kali 8320 Mar 15  2021 fang-of-haynekhtnamet
                                                                             
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ cat fang-of-haynekhtnamet   
 HH/lib64/ld-linux-x86-64.so.2GNUGNU��$�SyyZ;�`&}�^��m#= 
                                                         Y h "libc.so.6puts__cxa_finalize__libc_start_mainGLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_sta � � � � � � H�H��MCloneTableu▒i        1�
 H��t��H���5�
 �%�
 @�%�
 h������%�
H�=�����^H��H���PTL��H�
 �DH�=�
 UH��
 H9�H��tH�Z
]��f.�]�@f.�H�=i
 H�5b
 UH)�H��H��H��H��?H�H��t▒H�!
 H��t
     ]��f�]�@f.��=
8#TT 1tt$D���o�N
�� ��0)@▒�    H�(;▒�                                                                             ��t 1��L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��*ZAP!* ┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ strings fang-of-haynekhtnamet | grep {
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}

Si dejamos el tab no tenemos que escribir todo el texto

```

## Referencias