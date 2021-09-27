import cv2
import numpy as np


font=cv2.FONT_HERSHEY_SIMPLEX
font1=cv2.FONT_HERSHEY_COMPLEX

img =cv2.imread("D:\\1pyt\\vido\\shapededect\\polygons.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,tresh=cv2.threshold(gray,200,250,cv2.THRESH_BINARY)

contours=cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0] 

# This runtime error is caused by the fact that when you redefine cnt on line 13 as

# cnt = cv2.findContours(dst.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# you are setting it is the tuple of the two return values of cv2.findContours.
# Look at your earlier call to the function on line 37 as a guide. 
# All you need to do is change line 42 to
# cnt = cv2.findContours(dst.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

for cont in contours:

    epsil=0.01*cv2.arcLength(cont,True)
    aprox=cv2.approxPolyDP(cont,epsil,True)
    cv2.drawContours(img,[aprox],0,(0),5)

    x=aprox.ravel()[0]
    y=aprox.ravel()[1]
    print(aprox)
    print(len(aprox))
    if len(aprox)==3:
        cv2.putText(img,"triangl",(x,y),font,1,(0))
    
    if len(aprox)==4:
        cv2.putText(img,"rectang",(x,y),font,1,(0))
    
    if len(aprox)==5:
        cv2.putText(img,"pentag",(x,y),font,1,(0))
    
    if len(aprox)==6:
        cv2.putText(img,"hexag",(x,y),font,1,(0))
    
    if len(aprox)>=7:
        cv2.putText(img,"ellipse",(x,y),font,1,(0))
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()