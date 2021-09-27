import cv2


img=cv2.imread("C:\\Users\\Fatih Ali\\Documents\\1pyt\\vido\\corner detection16-17\\ucgen.jpg")

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,tresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)


contours,_=cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=contours[0]
area=cv2.contourArea(cnt)
print(area)

m=cv2.moments(cnt)
print(m["m00"])
perimeter=cv2.arcLength(cnt,True)
print(perimeter)
"""

cv2.imshow("resm",img)
cv2.imshow("gry",gray)
cv2.imshow("trsh",tresh)
"""












cv2.waitKey(0)
cv2.destroyAllWindows()