import numpy as np
import cv2
#import matplotlib.pyplot as plt 

img = cv2.imread('hough.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges =cv2.Canny(gray,50,150,apertureSize=3)
lines =  cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength =  100,maxLineGap = 10) 

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)

     
cv2.imshow('frame1',img)
cv2.imshow('frame2',edges)
#cv2.imshow('frame3',lines)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
