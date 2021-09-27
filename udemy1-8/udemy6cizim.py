import cv2
import numpy as np

canvas =np.zeros((1000,1000,3),np.uint8)+255
"""
cv2.line(canvas,(520,550),(112,312),(255,0,0),thickness=5)
cv2.line(canvas,(10,50),(200,512),(0,255,0),thickness=8)
"""

p1=(100,200)
p2=(50,50)
p3=(300,100)

points=np.array([[[110,200],[330,200],[290,220],[220,250]]],np.int32)

cv2.polylines(canvas,[points],False,(0,0,100),5)



cv2.rectangle(canvas,(50,50),(512,512),(255,0,0),thickness=5)
#cv2.circle(canvas,(500,500),400,(0,0,0),-1)
cv2.imshow("canvas",canvas) 
cv2.waitKey(0)
cv2.destroyAllWindows