import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

img = cv2.imread('shapes.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_ ,thresh = cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,255,255),3)
    x = approx.ravel()[0]-5
    y = approx.ravel()[1]-5
    if len(approx) == 3:
        cv2.putText(img,"TRIANGEL",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),3)
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio >= 0.95 and aspectratio<=1.05:
            cv2.putText(img,"rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
        else:
            cv2.putText(img,"rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
    elif len(approx) == 10:
        cv2.putText(img,"star",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
    else:
        cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
        
cv2.imshow('frame1',img)
#cv2.imshow('frame2',imgray)
#cv2.imshow('frame3',apple_orange)
#cv2.imshow('frame4',apple_orange_reconstruct)
#cv2.imshow('frame5',bilateral)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
