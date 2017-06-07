import gdb 


keyspace = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#%&()+,-.:;_{|}~ ")

gdb.execute("set pagination off")
flag = ""
gdb.execute("b main",True,True)
gdb.execute("b *0x80485cc",True,True)

for i in range(43):
	for char in keyspace:
		gdb.execute("r ",True,True)
		gdb.execute("set $eip=0x080485c2",True,True)
		gdb.execute("si",True,True)
		gdb.execute("set $eax="+hex(ord(char)),True,True)
		gdb.execute("set $edx="+str(i),True,True)
		gdb.execute("c ",True,True)
		eax = gdb.execute("p/d $eax",True,True)
		eax = int(eax.split("=")[1])                
		if eax == 1 :
			flag+=char
			print("[+] "+flag)
			break



"""payload = list("A"*44)
flag = ''	
map = {0,}
retry = True
tried = 0
brute = 0 
while True:
	payload[tried] = keyspace[brute] 
	gdb.execute("r "+'"'+"".join(payload)+'"',True,True)
	print("[-] payload "+"".join(payload))	
	for i in range(43) :
		eax = gdb.execute("p/d $eax",True,True)
		eax = int(eax.split("=")[1])                
		print(eax)
		print(gdb.execute("x/s $edx",True,True))                
		if eax == 0 :
			brute+=1
			print("[+] false hit")
			break
			                      
		else:
			flag += payload[tried]        
			print("[+]"+flag)
			tried+=1
			brute=0 
			gdb.execute("c ",True,True)"""
			 
			
	 


