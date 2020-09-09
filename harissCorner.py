import numpy as np
import cv2
#import matplotlib.pyplot as plt 

img = cv2.imread('chess_board.jpg')
cv2.imshow('frame',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)#cornerHarries takes only float32 dtype

dst = cv2.cornerHarris(gray,3,15,0.04)

dst = cv2.dilate(dst,None)

img[dst > 0.01 * dst.max()] = [(0,225,255)]



cv2.imshow('frame1',img)
#cv2.imshow('frame2',edges)
#cv2.imshow('frame3',lines)
#cv2.imshow('frame4',r)
#cv2.imshow('frame5',bilateral)


cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
