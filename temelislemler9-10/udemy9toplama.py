import cv2
import numpy as np

#img=cv2.imread("bo.jpg")

circle=np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,(256,256),60,(255,0,0),-1)

rect=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(rect,(150,150),(350,350),(0,0,255),-1)


add=cv2.add(circle,rect)
print(add)

cv2.imshow("topl",add)


#görüntü neden pembe çember oldu da kırmızı kare içerisinde mor çember olmadı?









cv2.imshow("daire",circle)
cv2.imshow("dikdört.",rect)

cv2.waitKey(0)
cv2.destroyAllWindows