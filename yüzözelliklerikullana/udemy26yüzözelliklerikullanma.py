import cv2
import numpy as np  

cap=cv2.VideoCapture("D:\\1pyt\\vido\\yüzözelliklerikullana\\1.mp4")
cv2.namedWindow("frame",cv2.WINDOW_GUI_NORMAL)

while 1:

    ret,frame=cap.read()
    
    roi=frame[50:250,250:450]
    cv2.rectangle(frame,(450,50),(1200,700),(0,255,100),2)
    
    cv2.imshow("frame",frame)

    if cv2.waitKey(30)&0xff==ord("q"):
        break
    

   

cap.release()
cv2.destroyAllWindows()
