import numpy as np
import cv2

cap = cv2.VideoCapture(0);


def nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar("lh",'Tracking',0,255,nothing)
cv2.createTrackbar("ls",'Tracking',0,255,nothing)
cv2.createTrackbar("lv",'Tracking',0,255,nothing)
cv2.createTrackbar("uh",'Tracking',255,255,nothing)
cv2.createTrackbar("us",'Tracking',255,255,nothing)
cv2.createTrackbar("uv",'Tracking',255,255,nothing)


while(True):
    #frame = cv2.imread('smarties.png')
    rec,frame = cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("lh","Tracking")
    l_s = cv2.getTrackbarPos("ls","Tracking")
    l_v = cv2.getTrackbarPos("lv","Tracking")
    
    u_h = cv2.getTrackbarPos("uh","Tracking")
    u_s = cv2.getTrackbarPos("us","Tracking")
    u_v = cv2.getTrackbarPos("uv","Tracking")
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('frame1',mask)
    cv2.imshow('frame2',res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()