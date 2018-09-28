from PIL import Image
import numpy as np
k=Image.open('file.jpg').getcolors()
j = max(k)
r = j[1][0]
g = j[1][1]
b = j[1][2]
rgb = np.array([r,g,b])
print (rgb)
cmy   = 1-rgb/255
print (cmy)
k = min(cmy)

if(k==1):
    cmy = 0
    k=1
else:
    cmy = (cmy-k)/(1-k)
cmyk = np.append(cmy,k)
print(cmyk)