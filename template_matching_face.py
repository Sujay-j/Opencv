import numpy as np
import cv2
#import matplotlib.pyplot as plt 

img = cv2.imread('DSC.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('face.jpg',0)
w,h =template.shape[::-1]


res = cv2.matchTemplate(gray , template , cv2.TM_CCORR_NORMED)
print(res)

threshold = 0.99# thre brighter point or  max point

loc = np.where(res >= threshold)

print(loc)

for pt  in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    

        
cv2.imshow('frame1',img)
#cv2.imshow('frame2',template)
#cv2.imshow('frame3',g)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
