#import numpy as np
import cv2

img = cv2.imread('DSC.jpg')
img2 = cv2.imread('DSC2.jpg')

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
print(img.shape)
print(img.size)
print(img.dtype)
#b,g,r=cv2.split(img)
#img = cv2.merge((b,g,r))

#face = img[140:40, 200:90]
#img =img[135:35, 90:0] = face
#dst = cv2.add(img,img2)
dst=cv2.addWeighted(img,.30,img2,.70,5)


cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()