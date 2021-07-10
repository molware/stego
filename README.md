# Malware Stego Sample

This project represents some PoC for least significant bit malware steganography as identified in a wild [malware sample](https://www.hybrid-analysis.com/sample/f1f0341bfe3b803ca654f43290410584c03c80c22c1ae1e7e87ef1d7f5b7e6ed?environmentId=120).

[Virustotal](https://www.virustotal.com/gui/file/f1f0341bfe3b803ca654f43290410584c03c80c22c1ae1e7e87ef1d7f5b7e6ed/detection)

The malware sample was originally an HTA file attachment delivered via email that appeared to represent a job offer. Inside the HTA file was an obfuscated Powershell script which pulled down a file named banana.png and performed an operation on it. Seemingly harmless, the png image file concealled a series of modified values within the green and blue rgb values of a subset of pixels within the image. These modified pixels are meaningles without the PowerShell script which carefully selects the modified range of pixels, and extracts the hidden values, resulting in the execution of another Powershell script which connects to a remote attacker controlled server over SSL, andattempts to download instrcutions every few minutes.

#Makestego.py

Makestego.py takes a cover image file and embeds it with any desired text in a range of pixels just like the malware authors embedded their code.

#rstego.py 

rstego.py reverses a stegonographic image, created by make stego.py and prints the cleartext of the embedded values in the image. Use rstego.py on the banana.png sample to see the malicious script embedded by the attackers.

I've provided some sample images to visualize what's taking place.

Starting with a blank white image [blank.png](https://github.com/molware/stego/blob/master/cover/blank.png)  
![blank](https://user-images.githubusercontent.com/58926312/125150018-932c2b00-e10a-11eb-8b35-65b779ad2991.png)

After running makestego.py to embed it with cleartext the image becomees [stego_blank.png](https://github.com/molware/stego/blob/master/stego/stego_blank.png)  
![stego_blank](https://user-images.githubusercontent.com/58926312/125150114-30875f00-e10b-11eb-9a96-eda94297b43b.png)


If it's hard to see on a white image, you can see which range of pixels were modified highlighted in [red.png](https://github.com/molware/stego/blob/master/cover/red.png)  
![red](https://user-images.githubusercontent.com/58926312/125150120-3da44e00-e10b-11eb-907d-c2cb6d03aea9.png)

