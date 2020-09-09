import numpy as np
import cv2
#import matplotlib.pyplot as plt 
cap = cv2.VideoCapture('vtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) #shadows
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()#statistical  
fgbg = cv2.createBackgroundSubtractorKNN()

#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
while True:
    ret,frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    
    cv2.imshow('frame',frame)
    cv2.imshow('frame1',fgmask)
    key = cv2.waitKey(30)
    if key == 'q' or key == 27:
        break
    
#cv2.imshow('frame1',img)
#cv2.imshow('frame2',edges)
#cv2.imshow('frame3',lines)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


#cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
