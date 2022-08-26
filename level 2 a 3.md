# Retos Bandit

## Objetivos

The password for the next level is stored in a file called **spaces in this filename** located in the home directory

## Datos de acceso

User: bandit2
Password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
Host: bandit.labs.overthewire.org  
Port: 2220

## Solución

```bash
>>C:\Users\jose_>ssh bandit2@bandit.labs.overthewire.org -p 2220
>>This is a OverTheWire game server. More information on http://www.overthewire.org/wargames
>>bandit2@bandit.labs.overthewire.orgs password:
>>Linux bandit.otw.local 5.4.8 x86_64 GNU/Linux
>>ls
>>cat "spaces in this filename"
>>UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```
## Notas adicionales

Cuando un archivo tiene espacios en el nombre se pueden utilizar comillas entre los espacios

## Referencias