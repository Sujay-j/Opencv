import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

img = cv2.imread('DSC2.jpg')

layer = img.copy()
gp = [layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow('upgau',layer)
lp = [layer]

for i in range(5,0,-1):
    gausian_extended = cv2.pyrUp(gp[i])
    laplasian = cv2.subtract(gp[i-1], gausian_extended)
    cv2.imshow(str(i),laplasian)

#cv2.imshow('frame1',img)
#cv2.imshow('frame2',lr1)
#cv2.imshow('frame3',lr2)
#cv2.imshow('frame4',upresolution)
#cv2.imshow('frame5',bilateral)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
