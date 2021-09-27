import cv2
import numpy as np



cap = cv2.VideoCapture(0)
#1.mp4 yerine tam dosya komutunu yaz \ kullanma \\ kullan yerine / da kullanabilirsin


cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",500,300)
cv2.namedWindow("hsv")
def nothng(x):
    pass
cv2.namedWindow("vido",cv2.WINDOW_NORMAL)

cv2.createTrackbar("hLOW","trackbar",0,180,nothng)
cv2.createTrackbar("sLOW","trackbar",0,255,nothng)
cv2.createTrackbar("vLOW","trackbar",0,255,nothng)

cv2.createTrackbar("hUPP","trackbar",0,180,nothng)
cv2.createTrackbar("sUPP","trackbar",0,255,nothng)
cv2.createTrackbar("vUPP","trackbar",0,255,nothng)

cv2.setTrackbarPos("hUPP","trackbar",180)
cv2.setTrackbarPos("sUPP","trackbar",255)
cv2.setTrackbarPos("vUPP","trackbar",255)


while True:
    ret, frame = cap.read()

    frame_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)

    
    lowH=cv2.getTrackbarPos("hLOW","trackbar")
    lowS=cv2.getTrackbarPos("sLOW","trackbar")
    lowV=cv2.getTrackbarPos("vLOW","trackbar")

    uppH=cv2.getTrackbarPos("hUPP","trackbar")
    uppS=cv2.getTrackbarPos("sUPP","trackbar")
    uppV=cv2.getTrackbarPos("vUPP","trackbar")

    lowercolor=np.array([lowH,lowS,lowV])
    uppcolor=np.array([uppH,uppS,uppV])
    mask=cv2.inRange(frame_hsv,lowercolor,uppcolor)

    

    if ret==False:
        print(cap.isOpened())
        break


    cv2.imshow("vido",frame)
    cv2.imshow("hsv",mask)

    if cv2.waitKey(20)& 0xFF==ord("q"):
        break 


cap.release()
cv2.destroyAllWindows()