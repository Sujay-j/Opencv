import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

kernal = np.ones((5,5),np.float32)/25
img = cv2.imread('DSC.jpg',0)
canny = cv2.Canny(img,100,200)

def nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar("can",'Tracking',100,255,nothing)

cv2.imshow('frame1',canny)

#for i in range(3):
#    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    cann=cv2.getTrackbarPos('can','Tracking')
    img=cv2.Canny(img,200,cann)
    cv2.imshow('image',img)

#cv2.imshow('frame',img)
#cv2.imshow('frame1',canny)
#cv2.imshow('frame2',sobelx)
#cv2.imshow('frame3',sobely)
#cv2.imshow('frame4',sobelCombine)
#cv2.imshow('frame5',bilateral)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
