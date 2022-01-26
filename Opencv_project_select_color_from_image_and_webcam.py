# 1. image select
#import libraries
import cv2
import numpy as np
image=cv2.imread("ball.jpg")
image=cv2.resize(image,(400,300))

cv2.namedWindow("color")
def xx(x):
    pass
cv2.createTrackbar("lower_h","color",0,255,xx)
cv2.createTrackbar("lower_s","color",0,255,xx)
cv2.createTrackbar("lower_v","color",0,255,xx)

cv2.createTrackbar("uper_h","color",255,255,xx)
cv2.createTrackbar("uper_s","color",255,255,xx)
cv2.createTrackbar("uper_v","color",255,255,xx)

while True:
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos("lower_h","color")
    l_s=cv2.getTrackbarPos("lower_s","color")
    l_v=cv2.getTrackbarPos("lower_v","color")
    
    u_h=cv2.getTrackbarPos("uper_h","color")
    u_s=cv2.getTrackbarPos("uper_s","color")
    u_v=cv2.getTrackbarPos("uper_v","color")
    
    lower_b=np.array([l_h,l_s,l_v])
    uper_b=np.array([u_h,u_s,u_v])
    
    mask=cv2.inRange(hsv,lower_b,uper_b)
    
    res=cv2.bitwise_and(image,image,mask=mask)
    res=cv2.resize(res,(800,300))
    
        
    cv2.imshow("orignal",image)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    
    if cv2.waitKey(1) & 0xff==27:
        break
cv2.destroyAllWindows()
     
# 2. Webcam select
#import libraries
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

cv2.namedWindow("color")
def xx(x):
    pass
cv2.createTrackbar("lower_h","color",0,255,xx)
cv2.createTrackbar("lower_s","color",0,255,xx)
cv2.createTrackbar("lower_v","color",0,255,xx)

cv2.createTrackbar("uper_h","color",255,255,xx)
cv2.createTrackbar("uper_s","color",255,255,xx)
cv2.createTrackbar("uper_v","color",255,255,xx)

while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(400,300))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos("lower_h","color")
    l_s=cv2.getTrackbarPos("lower_s","color")
    l_v=cv2.getTrackbarPos("lower_v","color")
    
    u_h=cv2.getTrackbarPos("uper_h","color")
    u_s=cv2.getTrackbarPos("uper_s","color")
    u_v=cv2.getTrackbarPos("uper_v","color")
    
    lower_b=np.array([l_h,l_s,l_v])
    uper_b=np.array([u_h,u_s,u_v])
    
    mask=cv2.inRange(hsv,lower_b,uper_b)
    mask=cv2.resize(mask,(400,300))
    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    res=cv2.resize(res,(600,600))
    
        
    cv2.imshow("orignal",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    
    if cv2.waitKey(1) & 0xff==27:
        break
cv2.destroyAllWindows()
