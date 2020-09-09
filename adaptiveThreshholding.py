import numpy as np
import cv2

img = cv2.imread('sudoku.jpg',0)
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2);

#_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)


cv2.imshow("image",img) 
#cv2.imshow("image1",th1) 
cv2.imshow("image2",th2)
cv2.imshow("image3",th3) 
#cv2.imshow("image4",th4)

cv2.waitKey(0)
   
cv2.destroyAllWindows()
#cap.release()