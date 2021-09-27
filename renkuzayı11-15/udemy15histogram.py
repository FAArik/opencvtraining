import cv2
import numpy as np  
from matplotlib import pyplot as plt

img =cv2.imread("bo.jpg")


cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)

b,g,r=cv2.split(img)
cv2.imshow("img",img)

#plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()