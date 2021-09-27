import cv2
import numpy as np      

img=cv2.imread("bo.jpg")

imgcnv=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgcnvhsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imgcnvgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgcnvhls=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)




cv2.imshow("bo",img)
#cv2.imshow("borgb",imgcnv)
cv2.imshow("bohsv",imgcnvhsv)
cv2.imshow("bogray",imgcnvgray)
cv2.imshow("bohls",imgcnvhls)



cv2.waitKey(0)
cv2.destroyAllWindows()