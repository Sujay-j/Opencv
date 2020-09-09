import numpy as np
import cv2

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1) 
img2 = cv2.imread('bww.jpg')

#bitAnd= cv2.bitwise_and(img2,img1)
#bitAnd= cv2.bitwise_or(img2,img1)
#bitAnd= cv2.bitwise_xor(img2,img1)
bitAnd= cv2.bitwise_not(img1)

cv2.imshow('image',img1)
#cv2.imshow('image2',img2)
cv2.imshow('image3',bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()