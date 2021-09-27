import cv2
import numpy as np  

cap=cv2.VideoCapture("D:\\1pyt\\vido\\yüzözelliklerikullana\\eye_motion.mp4")
#cap=cv2.VideoCapture(0)
cv2.namedWindow("frame",cv2.WINDOW_GUI_NORMAL)

while 1:

    ret,frame=cap.read()
    if ret is False:
        break
    
    
    roi=frame[80:210,230:450]
    rows,cols,cha=roi.shape
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,thres=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV)
    contours=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
    contours=sorted(contours,key=lambda x: cv2.contourArea(x),reverse=True)


    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        break
    
    roi=frame[80:210,230:450]=roi

    cv2.imshow("roi",roi)
    cv2.imshow("frame",frame)
    cv2.imshow("trh",thres)

    
    if cv2.waitKey(60)&0xff==ord("q"):
        break
    

   

cap.release()
cv2.destroyAllWindows()
