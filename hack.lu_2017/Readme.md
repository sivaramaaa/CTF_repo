## Bit (Pwn)

The challange allowed us input 2 values i.e addr & bit position , the bit is flipped at given addr at given pos  
The exploit is simple write a shellcode in bss addr , and overwrite got to get shell
But actual problem i faced in ctf was to write the math to 
