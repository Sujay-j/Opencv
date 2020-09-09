import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

img = cv2.imread('DSC.jpg')

lowresolution = cv2.pyrDown(img)
lr1 = cv2.pyrDown(lowresolution)
lr2 = cv2.pyrDown(lr1)



upresolution = cv2.pyrUp(lr1)



cv2.imshow('frame',img)
cv2.imshow('frame1',lowresolution)
cv2.imshow('frame2',lr1)
cv2.imshow('frame3',lr2)
cv2.imshow('frame4',upresolution)
#cv2.imshow('frame5',bilateral)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
