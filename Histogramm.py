import numpy as np
import cv2
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt 


#img= np.zeros((200,200),np.uint8)
#cv2.rectangle(img,(0,100),(200,200),(255),-1)
#cv2.rectangle(img,(0,50),(100,100),(127),-1)
img = cv2.imread('DSC.jpg',0)
#b,g,r = cv2.split(img)

hist =cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256])
#plt.hist(b.ravel(),256,[0,256])
#plt.hist(g.ravel(),256,[0,256])
#plt.hist(r.ravel(),256,[0,256])
#plt.show()
plt.plot(hist)
plt.show()
        
#cv2.imshow('frame1',hist)
#cv2.imshow('frame2',b)
#cv2.imshow('frame3',g)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


#cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
