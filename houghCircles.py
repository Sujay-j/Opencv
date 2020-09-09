import numpy as np
import cv2
#import matplotlib.pyplot as plt 

img = cv2.imread('shapes.jpg')
output = img.copy()
gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp = 1,minDist = 20,param1 = 50,param2 = 30,minRadius = 0,maxRadius = 0)
detected_circles = np.uint16(np.around(circles))
for(x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(255,255,0),3)
    cv2.circle(output,(x,y),2,(255,0,255),3)

cv2.imshow('frame1',output)
#cv2.imshow('frame2',edges)
#cv2.imshow('frame3',lines)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
