# Reversing

## Descripcion

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java)

## Pistas (Si hay)

Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Solución

``` Bash

┌──(kali㉿kali)-[~/picoCTF/Retos Reversing picoCTF 2019  Parte 1/vault-door-3]
└─$ code VaultDoor3.java 
                                                                                                                   
┌──(kali㉿kali)-[~/picoCTF/Retos Reversing picoCTF 2019  Parte 1/vault-door-3]
└─$ java VaultDoor3      
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}
Access granted.

---------------------------Terminal 2-------------------------

allow pasting
Uncaught SyntaxError: unexpected token: identifier
var password = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f'
undefined
var buffer = Array(32);
undefined
for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
"g"
buffer.join("")
"jU5t_a_s1mpl3_an4gr4m_4_u_79958f"

```

## Referencias