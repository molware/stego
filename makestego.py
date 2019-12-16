#!/usr/bin/env python3
from PIL import Image
file=input("Filename: ")
image=Image.open(file)
cord=image.load()
cleartext="testing"
#cleartext="testing123456dfshasndvhfhdsafj;hcnsadufvnsuadfpsvanpcufysavnfyvuvdscphfpavnuhasvcfusanhfvcmusavnhcsvdfunvnmcnuvhfcnivaimcashvnicuamfspnvuhacmfuvhsacufhpvcuvhpughvucmdfvughndsmcgvnhsndufhvgdsuihngcfdsuhgmvdsfunghmvcsghr7vnh9n5yv7w5y94tyrunvgh333nvbrewh4234v54n893234n52983475v243n5vb23weyutnuweyntvyqqqqty4b3ntyervyh734nv34v32959yv43n5y43v5y43nfry2394yyyyyyyyyyyyyyyyyyyyyynywr9q823rqewrqpwerpewrywebrwery[[qwr[yweryqwebrqw]qrqrqrquiryqiry"
#with open('malscript.txt','r') as file:
#	data=file.read()
#cleartext=data
#print(cleartext)
pointer=0

img2=image
pixelsNew=img2.load()

for y in range(84):
        for x in range(150):
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
img2.save('stego_',"PNG")
