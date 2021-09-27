import cv2
import numpy as np

img2 =cv2.imread("D:\\1pyt\\vido\\imagecomp\\bo.jpg")
img =cv2.imread("D:\\1pyt\\vido\\imagecomp\\bo.jpg")
img=cv2.resize(img,(640,480))
img2=cv2.resize(img,(640,480))
#img=cv2.medianBlur(img,5)


if img.shape==img2.shape:
    print("same size")
else:
    print("not same size")

diff=cv2.subtract(img,img2)
b,g,r=cv2.split(diff)

if cv2.countNonZero(b)==0&cv2.countNonZero(g)==0&cv2.countNonZero(r):
    print("comp. eq")
else:
    print("not comp eq")



cv2.imshow("dif",diff)
cv2.imshow("bo",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 