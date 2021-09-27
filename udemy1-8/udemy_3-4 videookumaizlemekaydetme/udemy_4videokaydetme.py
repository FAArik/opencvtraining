import cv2

cap=cv2.VideoCapture(0 )#,cv2.CAP_DSHOW)

filename="C:/Users/Fatih Ali/Documents/fatih.mp4"
codec = cv2.VideoWriter_fourcc(*'mp4v')
framerate=30
res= (1280,720)
videofileoutp= cv2.VideoWriter(filename,codec,framerate, res)
while True:


    ret,frame = cap.read()
    frame =cv2.flip(frame,1)
    videofileoutp.write(frame)

    cv2.imshow("webcam",frame)
    
    if cv2.waitKey(30) & 0xFF ==ord("q"): 
        break
    

videofileoutp.release()
cap.release()
cv2.destroyAllWindows()
