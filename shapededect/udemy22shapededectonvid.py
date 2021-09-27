import cv2
import numpy as np

def noth():
    pass

font=cv2.FONT_HERSHEY_DUPLEX

cap=cv2.VideoCapture(0)
cv2.namedWindow("settings")
cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
cv2.createTrackbar("l-hue","settings",0,180,noth)
cv2.createTrackbar("l-sat","settings",0,255,noth)
cv2.createTrackbar("l-val","settings",0,255,noth)
cv2.createTrackbar("h-hue","settings",0,180,noth)
cv2.createTrackbar("h-sat","settings",0,255,noth)
cv2.createTrackbar("h-val","settings",0,255,noth)


while 1:
    ret,frame=cap.read()

    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gry=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lh=cv2.getTrackbarPos("l-hue","settings")
    ls=cv2.getTrackbarPos("l-sat","settings")
    lv=cv2.getTrackbarPos("l-val","settings")
    hh=cv2.getTrackbarPos("h-hue","settings")
    hs=cv2.getTrackbarPos("h-sat","settings")
    hv=cv2.getTrackbarPos("h-val","settings")

    lowcol=np.array([lh,ls,lv])
    upcol=np.array([hh,hs,hv])

    mask=cv2.inRange(hsv,lowcol,upcol)

    kernel=np.ones((7,7),np.uint8)
    mask=cv2.erode(mask,kernel)
    mask=cv2.dilate(mask,kernel)

    hsv=cv2.convertScaleAbs(hsv)

    contours=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]#daha önce hsv yi atmıştın
    #maskelenmiş olanı at

    for cnt in contours:
        area=cv2.contourArea(cnt)
        epsil=0.02*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsil,True)
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        if area>400:
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            if len(approx)==3:
                cv2.putText(frame,"ucgen",(x,y),font,1,(0,0,0))
            
            elif len(approx)==4:
                cv2.putText(frame,"dortgen",(x,y),font,1,(0,0,0))
            
            elif len(approx)>6:
                cv2.putText(frame,"daire",(x,y),font,1,(0,0,0))

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5)&0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()