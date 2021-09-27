import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    
    ret,frame=cap.read()


   
    edges=cv2.Canny(frame,100,200)
    
    
    cv2.imshow("frame",frame)

    cv2.imshow("edge",edges)
    if cv2.waitKey(5)& 0xff==ord("q"):
        break    


cap.release

cv2.destroyAllWindows()