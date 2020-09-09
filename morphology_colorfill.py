import numpy as np
import cv2
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt 

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_ , mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)


kernal = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,kernal,iterations = 2)
erosion = cv2.erode(mask,kernal,iterations = 1)

opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)

mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)

titles=['image','mask','dilation']
images=[img,mask,dilation]

#for i in range(3):
#    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

cv2.imshow('frame',img)
cv2.imshow('frame1',mask)
cv2.imshow('frame2',dilation)
cv2.imshow('frame3',erosion)
cv2.imshow('frame4',opening)
cv2.imshow('frame5',closing)
cv2.imshow('frame6',mg)
cv2.imshow('frame7',th)

cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
