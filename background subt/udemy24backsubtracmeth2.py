import cv2
import numpy as np  

cap=cv2.VideoCapture("D:\\1pyt\\vido\\background subt\\car.mp4")

subt=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)
while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))

    mask=subt.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(30)& 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

