import cv2
import numpy as np  

linevid=cv2.VideoCapture("E:\\belgeler\\ind\\line.mp4")


while True:
    ret,frame=linevid.read()
    frame=cv2.resize(frame,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowyell=np.array([18,94,140],np.uint8)
    uppyell=np.array([48,255,255],np.uint8)

    mask=cv2.inRange(hsv,lowyell,uppyell)
    edges=cv2.Canny(mask,75,250)

    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=100)

    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

        
    cv2.imshow("line",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(30)&0xff==ord("q"):
        break


linevid.release()
cv2.destroyAllWindows()