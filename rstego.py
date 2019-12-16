#!/usr/bin/env python3

from PIL import Image

#Create Blank White Image

#img = Image.new('RGB', (300,168), (255, 255, 255))

#img.save("white.png", "PNG")

#Load Existing Image

file=input("Enter file name to reverse: ")

image=Image.open(file)

cord=image.load()

cleartext=""

for y in range(16):

        for x in range(299):

                change = cord[x,y]

                g=change[1]

                b=change[2]

                cleartext+=chr(int((b & 15) * 16) | (g & 15))

print(cleartext[:2857])


