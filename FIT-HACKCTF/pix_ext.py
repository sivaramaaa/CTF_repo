from PIL import Image
from os import listdir
from os.path import isfile, join
mypath = "/root/Downloads/animizer_downloads"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
flag = ""
for image in onlyfiles :
        im = Image.open("/root/Downloads/animizer_downloads/"+image) #Can be many different formats.
	pix = im.convert('RGB')
        #print pix[0,0]
	(r,g,b)= pix.getpixel((1, 1)) #Get the RGBA Value of the a pixel of an image
        print chr(r)+chr(g)+chr(b)
        flag += chr(r)+chr(g)+chr(b)


print flag
