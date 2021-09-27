import cv2

def aspectratioresize(img,width=None,height=None, inter = cv2.INTER_AREA):
    dimension = None
    (h,w)=img.shape[:2]

    if width is None and height is None:
        return img
    
    if width is None:
        r=height/float(h)
        dimension=(int(r*w),height)
    

    else:
        r=width/float(w)
        dimension=(width,int(h*r))
    
    return cv2.resize(img,dimension,interpolation=inter)

resim=cv2.imread("bo.jpg")
resresim=aspectratioresize(resim,width=None,height=500, inter = cv2.INTER_AREA)

cv2.imshow("resim",resim)
cv2.imshow("resresim",resresim)

cv2.waitKey(0)
cv2.destroyAllWindows


