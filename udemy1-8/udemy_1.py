import cv2
import numpy as np      

#cv2.namedWindow("pencere ismi",cv2.WINDOW_NORMAL)=> ayarlanabilir pencere için



resim=cv2.imread("bo.jpg")


cv2.namedWindow("bo",cv2.WINDOW_NORMAL)
resim =cv2.resize(resim,(600,600))
cv2.imshow("bo",resim)



cv2.waitKey(0)
cv2.destroyAllWindows
