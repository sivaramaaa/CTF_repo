33c3tf 2016 writeup

1) MISC -- pdfmaker 
  This problem has pdflatex vulnerability ...
  It has easy RCE by using \immediate\write18{shell_command > dump.log } && \input{dump.log}
  BUt write18 is blocked but allows only few commands . But one of then is mpost which allows RCE
  
  Refer http://scumjr.github.io/2016/11/28/pwning-coworkers-thanks-to-latex/
        https://github.com/EdwardPwnden/ctf-2016/tree/master/33c3/pdfmaker
        
 2) heap Exploit 
 
    
