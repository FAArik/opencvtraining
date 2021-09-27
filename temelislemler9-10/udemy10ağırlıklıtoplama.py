import cv2
import numpy as np


#f(x,y)= ax+ by +c bu ne aq 

circle=np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,(256,256),60,(255,0,0),-1)

rect=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(rect,(150,150),(350,350),(0,0,255),-1)

dst= cv2.addWeighted(circle,0.5,rect,0.5,0)




cv2.imshow("daire",circle)
cv2.imshow("dikdört.",rect)
cv2.imshow("ağrtpl",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()