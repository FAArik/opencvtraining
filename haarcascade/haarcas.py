import cv2
import numpy as np


img =cv2.imread("D:\\1pyt\\opencvtraining\\haarcascade\\emma.jpg")
face_cas=cv2.CascadeClassifier("D:\\1pyt\\opencvtraining\\haarcascade\\haarcascades\\haarcascade_frontalface_alt.xml")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cas.detectMultiScale(gry,1.3,3)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)




cv2.imshow("res",img)
cv2.imwrite("haarcascade/foundfac.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()