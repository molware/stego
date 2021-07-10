#!/usr/bin/env python3
from PIL import Image 
import os
file=input("Filename: ")
image=Image.open(file)
cord=image.load()
##The text you want to embed in the image
cleartext="testing"
pointer=0
#Copy the image, and load its pixels
img2=image
pixelsNew=img2.load()

#Modify a specific range of pixels in the image, and then save.
for y in range(16):
        for x in range(299):
                red, green, blue = cord[x,y];
                char = ord(cleartext[pointer])
                high = char>>4
                low = char & 0xf
                pointer+=1
                newgreen = ((green>>4) * 16) | low
                newblue = ((green>>4)*16) | high
                cord[x,y] = (red, newgreen,newblue)
                red, green, blue = cord[x,y]
                pixelsNew[x,y] = (red,newgreen,newblue)
                cleartext+=chr(int((blue & 15) * 16 | green & 15))
#Save file
file="stego_" + file                
stego_path=os.path.join("stego",file)
img2.save(stego_path,"PNG")
