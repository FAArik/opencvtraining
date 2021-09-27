import cv2


cap = cv2.VideoCapture('C:\\Users\\Fatih Ali\\Documents\\1pyt\\vido\\renkuzayı\\1.mp4')
#1.mp4 yerine tam dosya komutunu yaz \ kullanma \\ kullan yerine / da kullanabilirsin
while True:
    ret, frame = cap.read()
    frame =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("vido",cv2.WINDOW_NORMAL)
    if ret==False:
        print(cap.isOpened())
        break


    cv2.imshow("vido",frame)


    if cv2.waitKey(20)& 0xFF==ord("q"):
        break 


cap.release()
cv2.destroyAllWindows()