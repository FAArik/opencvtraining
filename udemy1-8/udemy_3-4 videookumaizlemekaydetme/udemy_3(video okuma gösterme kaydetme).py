import cv2

cap = cv2.VideoCapture(0) #webcam için 

while True:
    ret,frame=cap.read() #ret komutu görüntü alınıp alınmadığını kontrol eder frame ise görüntüyü alır

    cv2.imshow("webcam",frame)
    frame=cv2.flip(frame,1) #görüntüyü çevirmek için kullanılır. 1 y ekseni için kullanılır imshow
    # üzerinde olması lazım tabiki :)
    

    if cv2.waitKey(1) & 0xFF ==ord("q"): #frame rate ayarı burdan yapılıyor
        break
cap.release()
cv2.destroyAllWindows