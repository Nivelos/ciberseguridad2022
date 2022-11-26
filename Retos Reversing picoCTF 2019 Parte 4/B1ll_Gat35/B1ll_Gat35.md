# Retos: Reversing picoCTF 2019 - Parte 4

## Descripcion

Can you reverse this [Windows Binary](https://jupiter.challenges.picoctf.org/static/0ef5d0d6d552cd5e0bd60c2adbddaa94/win-exec-1.exe)?

## Pistas (Si hay)

1.- Microsoft provides windows virtual machines https://developer.microsoft.com/en-us/windows/downloads/virtual-machines

2.- Ollydbg may be helpful

3.- Flag format: PICOCTF{XXXX}

## Solución

``` Bash

Utilizando hidra hacemos una modificacion a un JNZ para que nos de la bandera directamente

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/B1ll_Gat35]
└─$ ghidra &
[1] 27831
                                                                                                                   
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/B1ll_Gat35]
└─$ Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true

[1]  + done       ghidra
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/B1ll_Gat35]
└─$ mv win-exec-2.exe.bin win-exec-2.exe 
                                                                                                                   
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Reversing picoCTF 2019 Parte 4/B1ll_Gat35]
└─$ wine win-exec-2.exe 
Input a number between 1 and 5 digits: 4
Initializing...
Enter the correct key to get the access codes: 4
Correct input. Printing flag: PICOCTF{These are the access codes to the vault: 1063340} 

```

## Referencias