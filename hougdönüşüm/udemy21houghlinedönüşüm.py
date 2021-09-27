import cv2
import numpy as np

img=cv2.imread("E:\\belgeler\\ind\\h_line.png")
#img=cv2.imread("C:\\Users\\Fatih Ali\\Documents\\1pyt\\vido\\hougdönüşüm\\hline.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges =cv2.Canny(gray,75,150) #75 min 150 max val

lines =cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=150)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("img",img)
print(lines)
cv2.waitKey(0)
cv2.destroyAllWindows