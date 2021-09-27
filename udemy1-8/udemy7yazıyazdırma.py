import cv2
import numpy as np


canvas =np.zeros((512,512,3),np.uint8)+255 #255 eklenerek beyaz görüntü elde edilir

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_PLAIN


cv2.putText(canvas,"ğpencv",(10,100),font1,3,(0,0,0) ,cv2.LINE_AA)



cv2.imshow("canv",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()