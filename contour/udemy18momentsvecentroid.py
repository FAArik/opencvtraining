import cv2
import numpy as np

img=cv2.imread("C:\\Users\\Fatih Ali\\Documents\\1pyt\\vido\\corner detection16-17\\ucgen.jpg")


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

M=cv2.moments(thresh)

X=int(M["m10"]/M["m00"])
Y=int(M["m01"]/M["m00"])

cv2.circle(img,(X,Y,),5,(255,0,255),-1)


cv2.imshow("aa",img)
cv2.waitKey(0)
cv2.destroyAllWindows()