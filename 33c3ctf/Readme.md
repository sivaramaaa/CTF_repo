33c3tf 2016 writeup

<b>1) MISC -- pdfmaker  - 75 </b> <br>
  This problem has pdflatex vulnerability ... <br>
  It has easy RCE by using \immediate\write18{shell_command > dump.log } && \input{dump.log}  <br>
  BUt write18 is blocked but allows only few commands . But one of them is mpost which allows RCE <br>
  
  Refer http://scumjr.github.io/2016/11/28/pwning-coworkers-thanks-to-latex/ <br>
        https://github.com/EdwardPwnden/ctf-2016/tree/master/33c3/pdfmaker   <br>
    
  So we create a vuln.mp  <br>
  and in tex file use mpost(which is allowed in write18) to compile .mp file which leads to RCE :) <br>
    
    
 <b>2) Heap Exploit -- 150 </b> <br>
  In this we have somehow mannage to overwrite a heap addr in located in heap and attain a arrbitary overwrite . <br>
  So we first leak the libc addr by modifying the pointer to text chunk addr to a got addr and use display func to attain leak <br>
  Next we overwrite the heap@got which has heap addr as argument which we can control <br>
 
    
