import cv2
import numpy as np

img=cv2.imread("C:\\Users\\Fatih Ali\\Documents\\1pyt\\vido\\corner detection16-\\ucgen.jpg")


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)


corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)

corners=np.int0(corners)
for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),5,(0,0,0),-1)

cv2.imshow("triang",img)

cv2.waitKey(0)
cv2.destroyAllWindows()