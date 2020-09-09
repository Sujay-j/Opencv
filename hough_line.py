import numpy as np
import cv2
#import matplotlib.pyplot as plt 

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges =cv2.Canny(gray,50,150,apertureSize=3)
lines =  cv2.HoughLines(edges,1,np.pi/180,200) 

for line in lines:
    rho,theta = line[0]#rho is the distance from the cordinate (0,0) and theta is angle
    a=np.cos(theta)
    b=np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    #x1 stores the rounded off value of (r * cos(theta)-1000 + cos(theta))
    x1=int(x0 + 1000 * (-b))
    #y1 stores the rounded off value of (r * sin(theta)+1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    #x2 stores the rounded off value of (r * cos(theta)+1000 * sin(theta))
    x2 = int(x0 -1000 *(-b))
    #y2 stores the rounded off value of (r * sin(theta)-1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)


     
cv2.imshow('frame1',img)
cv2.imshow('frame2',edges)
#cv2.imshow('frame3',lines)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
