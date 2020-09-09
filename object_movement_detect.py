import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

cap =cv2.VideoCapture('vtest.avi')
ret,frame1 = cap.read()
ret,frame2 = cap.read()
while(True):
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _ , thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations = 3)
    contours , _ =cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour)< 900:
            continue
        cv2.rectangle(frame1,(x,y),(x+w , y+h),(0,255,0),2)
        cv2.putText(frame1,"status :{}".format('movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

        
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    
    
    cv2.imshow("feed",frame1)
    frame1=frame2
    ret,frame2 = cap.read()










    #cv2.imshow("inter",frame)
    if cv2.waitKey(40) == 27:
        break





#cv2.imshow('frame1',img)
#cv2.imshow('frame2',imgray)
#cv2.imshow('frame3',apple_orange)
#cv2.imshow('frame4',apple_orange_reconstruct)
#cv2.imshow('frame5',bilateral)





#cv2.waitKey(0)   
cv2.destroyAllWindows()
cap.release()
