import cv2
import numpy as np  
import time

cap=cv2.VideoCapture("D:\\1pyt\\vido\\background subt\\car.mp4")


while 1:
    ret,firstframe=cap.read()
    firstgry=cv2.cvtColor(firstframe,cv2.COLOR_BGR2GRAY)
    firstgry=cv2.GaussianBlur(firstgry,(5,5),0)
    time.sleep(0.009)
    ret,frame=cap.read()
    gry=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gry=cv2.GaussianBlur(gry,(5,5),0)

    diff =cv2.absdiff(firstgry,gry)
    _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)

    
    cv2.imshow("dif",diff)




    if cv2.waitKey(30)& 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()




