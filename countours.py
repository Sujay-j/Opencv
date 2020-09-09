#import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

img = cv2.imread('sudoku.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_ ,thresh = cv2.threshold(imgray,110,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("number of countours = "+ str(len(contours)))
print(contours)

cv2.drawContours(img,contours,-1,(0,255,255),3)


cv2.imshow('frame1',img)
cv2.imshow('frame2',imgray)
#cv2.imshow('frame3',apple_orange)
#cv2.imshow('frame4',apple_orange_reconstruct)
#cv2.imshow('frame5',bilateral)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
