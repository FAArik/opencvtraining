import numpy as np
import cv2 as c

cm=c.VideoCapture(0)

while True:
    ret,frame=cm.read()



    c.rectangle(frame,(150,150),(500,800),(0,0,255),2)##iimshow üstünde olması gerekiyor
    c.imshow("kamera işte aq ille söyleyelim mi aq",frame)
    

    
    if c.waitKey(1)&0xFF == ord("q"):
        break



c.destroyAllWindows
cm.release()
