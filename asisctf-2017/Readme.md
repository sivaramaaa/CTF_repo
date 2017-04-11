#### PWN 100 

The binary was a 64 bit binary . 
It justs reads input and all the protection was off .
But as we cannot predict the buffer addr , we had to load our input into bss section by calling read again 
and then execute the bss section .

##### NOTE : IN 64 bit binary the arguments to function are in registers and not on stack 
          
 #####       Fill the buffer completely i.e to gain eip 24 bytes was sufficient but you have to fill 1024 bytes 
 #####       in order to read ur shellcode properly 
