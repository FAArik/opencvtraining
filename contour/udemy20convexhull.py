import cv2
import numpy as np

star=cv2.imread("C:\\Users\\Fatih Ali\\Documents\\1pyt\\vido\\contour\\star.png")

gray=cv2.cvtColor(star,cv2.COLOR_BGR2GRAY)

_,tresh=cv2.threshold(gray,127,255,0)
contour,_=cv2.findContours(tresh,2,1)
cnt=contour[0]
hull =cv2.convexHull(cnt,returnPoints=False)

defects=cv2.convexityDefects(cnt,hull)

for i in range (defects.shape[0]):
    s,e,f,d=defects[i,0]        #s=startpoint e=endpoint f=farest point d=distance
    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    farest=tuple(cnt[f][0])
    cv2.line(star,start,end,[0,255,0],2)
    cv2.circle(star,farest,5,[0,255,255],-1)

cv2.imshow("yıldız",star)

cv2.waitKey(0)
cv2.destroyAllWindows