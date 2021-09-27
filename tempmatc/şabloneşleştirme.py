import cv2
import numpy as np


img =cv2.imread("D:\\1pyt\\vido\\tempmatc\\bo.jpg")
grim=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
tem =cv2.imread("D:\\1pyt\\vido\\tempmatc\\bo2.jpg")
grtm=cv2.cvtColor(tem,cv2.COLOR_BGR2GRAY)
result=cv2.matchTemplate(grim,grtm,cv2.TM_CCOEFF_NORMED)

loc=np.where(result>=0.7)

for point in zip(*loc[::-1]):
    print(point)





cv2.imshow("res",result)
cv2.waitKey(0)
cv2.destroyAllWindows() 