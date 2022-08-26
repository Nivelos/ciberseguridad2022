# Retos Bandit

## Objetivos

The password for the next level is stored in a file called **-** located in the home directory

## Datos de acceso

User: bandit1
Password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```bash
>>C:\Users\jose_>ssh bandit1@bandit.labs.overthewire.org -p 2220
>>This is a OverTheWire game server. More information on http://www.overthewire.org/wargames
>>bandit1@bandit.labs.overthewire.org's password:
>>Linux bandit.otw.local 5.4.8 x86_64 GNU/Linux
>>bandit1@bandit:~$ cat ./-
>>CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9 
```
## Notas adicionales

Al "-" ser un caracter especial, tenemos que agregar un ./ para que se pueda utilizar el comando cat

## Referencias

https://www.google.com/search?q=dashed+filename

http://tldp.org/LDP/abs/html/special-chars.html