import cv2
import numpy as np  

cap=cv2.VideoCapture("D:\\1pyt\\vido\\background subt\\22.mp4")
circles=[]
def mouse(event,x,y,flags,params):
    
    if event==cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))
cv2.namedWindow("frame")
cv2.setMouseCallback("frame",mouse)

while 1:
    ret,frame=cap.read()
    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)

    cv2.imshow("frame",frame)


    key=cv2.waitKey(35)

    if key==27:
        break
    elif key==ord("c"):
        circles=[]    


cap.release()
cv2.destroyAllWindows()
