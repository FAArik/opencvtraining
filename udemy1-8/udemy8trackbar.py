import cv2
import numpy as np


def nothng(x):
    pass

img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("image")

cv2.createTrackbar("r","image",0,255,nothng) #tracbar oluşturma
cv2.createTrackbar("g","image",0,255,nothng)
cv2.createTrackbar("b","image",0,255,nothng)
switch="0:OFF, 1=ON"
cv2.createTrackbar(switch,"image",0,1,nothng)


while True:
    cv2.imshow("img",img)
    if(cv2.waitKey(1) & 0xFF==ord("q")):
        break
    
    r=cv2.cv2.getTrackbarPos("r","image") #rgb değerlerinin yerlerini kontrol edip değişkene atıyor
    g=cv2.cv2.getTrackbarPos("g","image")
    b=cv2.cv2.getTrackbarPos("b","image")
    s=cv2.cv2.getTrackbarPos(switch,"image") #switch i bir değişkene atamamız gerekiyor
    if (s==0):
        img[:]==[0,0,0]
    else:
        img[:]=[b,g,r]      #rgb değerlerinin yerlerini kontrol edip resim üzerinde uyguluyor
    

cv2.destroyAllWindows()