import cv2
import numpy as np      


resim=cv2.imread("bo.jpg")

blur = cv2.blur(resim,(7,5))

gauss =cv2.GaussianBlur(resim,(5,5),cv2.BORDER_DEFAULT)


bilateral=cv2.bilateralFilter(resim,9,50,50)
bilateral2=cv2.bilateralFilter(resim,7,100,100)



cv2.imshow("bo",resim)
cv2.imshow("bilateral2",bilateral2)
cv2.imshow("gauss",gauss)
cv2.imshow("bilateral",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows
