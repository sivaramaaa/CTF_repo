import struct


f = open('elif','r+b') 
fl = open('flag','w+b')
s = ''
while True :
   line = f.readline()
   if line == '':
        break
   else:
        for words in line:
               s+=words
               print repr(words) 

for i in range(1,len(s),4):
        payload = s[-i]+s[-i-1]+s[-i-2]+s[-i-3]
        fl.write(payload)
        print repr(payload)
