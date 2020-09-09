import numpy as np
import cv2
#import matplotlib.pyplot as plt 
cap = cv2.VideoCapture('slow_traffic_small.mp4')

ret , frame = cap.read()
x,y,w,h = 300,200,100,50
track_window = (x,y,w,h)
roi = frame[y:y+h,x:x+w]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask  = cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])

cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_crit=(cv2.TermCriteria_EPS | cv2.TERM_CRITERIA_COUNT,10,1)
cv2.imshow('frame1',roi)



while(True):
    ret,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret,track_window = cv2.CamShift(dst,track_window,term_crit)
        print(ret)
        #x,y,w,h = track_window
        #final_image = cv2.rectangle(frame,(x,y),(x+w,y+h),255,2)
        pts= cv2.boxPoints(ret)
        print(pts)
        pts = np.int0(pts)
        final_image = cv2.polylines(frame,[pts],True,(0,255,255),21)
        cv2.imshow('frame',final_image)
        cv2.imshow('frame2',dst)
        if cv2.waitKey(30) & 0xFF ==ord('q'):
            break
    else:
        break
    
#cv2.imshow('frame1',img)
#cv2.imshow('frame2',edges)
#cv2.imshow('frame3',lines)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


#cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
